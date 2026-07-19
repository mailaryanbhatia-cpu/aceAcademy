/**
 * firestore.js — AcerAcademy Sync Engine v3
 *
 * Architecture:
 *   localStorage = write-through cache (instant reads/writes, works offline)
 *   Firestore    = source of truth (cross-device, persists after cache clear)
 *
 * Conflict resolution: per-key timestamps (last-write-wins)
 *   Every key stored in LS and Firestore has a companion _ts_{key} timestamp.
 *   On merge: whichever timestamp is newer wins.
 *
 * Offline support:
 *   - Firestore SDK offline persistence enabled (IndexedDB)
 *   - Pending writes queued in localStorage, flushed on reconnect
 *   - onSnapshot() keeps real-time updates flowing between devices/tabs
 */
(function () {
  'use strict';

  // ── Keys to sync ──────────────────────────────────────────────────────────
  // LOCAL_ONLY: never leave the device (sensitive or device-specific)
  var LOCAL_ONLY = new Set([
    'ace_claude_key', 'ace_notif_enabled', 'ace_sounds', 'ace_timer_state',
    'ace_onboarding_done_v2', 'ace_tour_done', 'ace_onboarded',
    'color-theme', 'focus-mode', 'ace_notebook_active',
    'ace_notif_dismissed', 'ace_reviewed_today'
  ]);

  // SYNC: everything else that starts with ace_ or these legacy keys
  var SYNC_PREFIXES = ['ace_', 'aceTest', 'aceSession', 'aceAccounts'];
  var SYNC_EXTRA = [
    'aceTestHistory', 'satact_results', 'gradebook', 'annotatedbib',
    'concept-maps', 'cornell-notes', 'labreports', 'research-data',
    'spelling_mastery', 'cp-colleges', 'cp-checks', 'sim-history',
    'explainer-history', 'goal-date', 'goal-done', 'goal-target',
    'dc-history', 'dc-grade', 'dc-streak', 'tl-events', 'tl-saved',
    'venn-items', 'venn-saved'
  ];

  var PENDING_KEY = '_ace_pending_writes';
  var SNAP_KEY    = '_ace_firestore_snap_ts';

  var _db       = null;
  var _uid      = null;
  var _unsubFS  = null;   // onSnapshot unsubscriber
  var _saveTimer= null;
  var _online   = navigator.onLine;
  var _dirty    = {};     // keys changed since last Firestore write

  // ── Helpers ───────────────────────────────────────────────────────────────
  function isSyncKey(key) {
    if (!key || LOCAL_ONLY.has(key)) return false;
    for (var i = 0; i < SYNC_PREFIXES.length; i++) {
      if (key.startsWith(SYNC_PREFIXES[i])) return true;
    }
    return SYNC_EXTRA.includes(key);
  }

  function tsKey(key) { return '_ts_' + key; }

  function now() { return Date.now(); }

  function getLS(key) {
    try { return localStorage.getItem(key); } catch(e) { return null; }
  }
  function setLS(key, val) {
    try { _origSetItem.call(localStorage, key, val); } catch(e) {}
  }

  function parseVal(raw) {
    if (raw === null || raw === undefined) return null;
    try { return JSON.parse(raw); } catch(e) { return raw; }
  }
  function serializeVal(val) {
    if (typeof val === 'string') return val;
    return JSON.stringify(val);
  }

  // ── Pending write queue (for offline writes) ──────────────────────────────
  function getPending() {
    try { return JSON.parse(getLS(PENDING_KEY) || '{}'); } catch(e) { return {}; }
  }
  function setPending(obj) {
    setLS(PENDING_KEY, JSON.stringify(obj));
  }
  function queuePending(key, val, ts) {
    var p = getPending();
    p[key] = { val: val, ts: ts };
    setPending(p);
  }
  function clearPending() {
    setLS(PENDING_KEY, '{}');
  }

  // ── Build Firestore payload from dirty keys ───────────────────────────────
  function buildPayload(keys) {
    var data = {};
    var tsData = {};
    (keys || Object.keys(_dirty)).forEach(function(key) {
      if (!isSyncKey(key)) return;
      var raw = getLS(key);
      if (raw === null) return;
      var ts  = parseInt(getLS(tsKey(key)) || '0');
      data[key]   = parseVal(raw);
      tsData[key] = ts;
    });
    if (Object.keys(data).length === 0) return null;
    data['_ts']       = tsData;
    data['updatedAt'] = firebase.firestore.FieldValue.serverTimestamp();
    return data;
  }

  // ── Write to Firestore ────────────────────────────────────────────────────
  function flushToFirestore(force) {
    if (!_db || !_uid) return;
    var keys = Object.keys(_dirty);

    // Also flush pending queue
    var pending = getPending();
    Object.keys(pending).forEach(function(k) {
      if (!_dirty[k]) { _dirty[k] = true; keys.push(k); }
    });

    if (keys.length === 0 && !force) return;

    var payload = buildPayload(keys);
    if (!payload) return;

    _db.collection('users').doc(_uid).set(payload, { merge: true })
      .then(function() {
        _dirty = {};
        clearPending();
      })
      .catch(function(err) {
        console.warn('[aceSync] Firestore write failed, queuing:', err.message);
        // Keep in pending queue — will retry on next online event
      });
  }

  function scheduleFlush() {
    clearTimeout(_saveTimer);
    _saveTimer = setTimeout(function() { flushToFirestore(); }, 2500);
  }

  // ── Pull Firestore → localStorage ─────────────────────────────────────────
  function mergeFirestoreData(remote) {
    if (!remote) return;
    var remoteTsMap = remote['_ts'] || {};
    var uiNeedsRefresh = false;

    Object.keys(remote).forEach(function(key) {
      if (key === '_ts' || key === 'updatedAt') return;
      if (!isSyncKey(key)) return;

      var remoteVal = remote[key];
      var remoteTs  = remoteTsMap[key] || 0;
      var localTs   = parseInt(getLS(tsKey(key)) || '0');

      if (remoteTs >= localTs) {
        // Remote is newer (or same age) — use remote
        var serialized = serializeVal(remoteVal);
        var current    = getLS(key);
        if (current !== serialized) {
          setLS(key, serialized);
          setLS(tsKey(key), String(remoteTs));
          uiNeedsRefresh = true;
        }
      }
      // else: local is newer — keep local, it'll flush to Firestore shortly
    });

    if (uiNeedsRefresh) {
      window.dispatchEvent(new CustomEvent('ace-sync-updated'));
    }
  }

  // ── Initial load: one-time fetch + start real-time listener ───────────────
  function initSync() {
    if (!_db || !_uid) return;

    // Enable offline persistence (best-effort)
    _db.enablePersistence({ synchronizeTabs: true })
      .catch(function(err) {
        if (err.code !== 'failed-precondition' && err.code !== 'unimplemented') {
          console.warn('[aceSync] Persistence error:', err.code);
        }
      });

    // One-time initial load
    _db.collection('users').doc(_uid).get().then(function(doc) {
      if (!doc.exists) {
        // First time — push local data up
        _dirty = {};
        // Mark all sync keys as dirty so they get pushed
        Object.keys(localStorage).forEach(function(k) {
          if (isSyncKey(k)) _dirty[k] = true;
        });
        flushToFirestore(true);
      } else {
        mergeFirestoreData(doc.data());
      }
    }).catch(function(err) {
      console.warn('[aceSync] Initial load error:', err.message);
    });

    // Real-time listener for cross-device updates
    if (_unsubFS) _unsubFS(); // cancel any existing listener
    _unsubFS = _db.collection('users').doc(_uid).onSnapshot(
      { includeMetadataChanges: false },
      function(doc) {
        if (!doc.exists) return;
        // Ignore if this snapshot is from our own write (pending local changes)
        if (doc.metadata.hasPendingWrites) return;
        mergeFirestoreData(doc.data());
      },
      function(err) {
        console.warn('[aceSync] onSnapshot error:', err.message);
      }
    );
  }

  // ── Online / offline handling ─────────────────────────────────────────────
  window.addEventListener('online', function() {
    _online = true;
    if (_db && _uid) {
      // Flush anything that was queued while offline
      var pending = getPending();
      if (Object.keys(pending).length > 0) {
        Object.keys(pending).forEach(function(k) { _dirty[k] = true; });
        flushToFirestore(true);
      }
    }
  });
  window.addEventListener('offline', function() {
    _online = false;
  });

  // ── Patch localStorage.setItem ────────────────────────────────────────────
  var _origSetItem = localStorage.setItem.bind(localStorage);
  Object.defineProperty(localStorage, 'setItem', {
    configurable: true,
    writable:     true,
    value: function patchedSetItem(key, value) {
      _origSetItem(key, value);
      if (!isSyncKey(key)) return;
      // Stamp with current time
      var ts = now();
      _origSetItem(tsKey(key), String(ts));

      if (_uid) {
        _dirty[key] = true;
        if (_online) {
          scheduleFlush();
        } else {
          queuePending(key, value, ts);
        }
      }
    }
  });

  // ── Patch localStorage.removeItem ────────────────────────────────────────
  var _origRemoveItem = localStorage.removeItem.bind(localStorage);
  Object.defineProperty(localStorage, 'removeItem', {
    configurable: true,
    writable:     true,
    value: function patchedRemoveItem(key) {
      _origRemoveItem(key);
      _origRemoveItem(tsKey(key));
      // We don't push deletions to Firestore to avoid accidental data loss
    }
  });

  // ── Auth wiring ───────────────────────────────────────────────────────────
  function onUserSignedIn(uid) {
    if (_uid === uid) return; // already initialized for this user
    _uid = uid;
    try {
      _db = firebase.firestore();
      initSync();
    } catch(err) {
      console.warn('[aceSync] Firebase not ready:', err.message);
    }
  }

  function onUserSignedOut() {
    if (_unsubFS) { _unsubFS(); _unsubFS = null; }
    _uid = null;
    _db  = null;
    _dirty = {};
  }

  window.addEventListener('ace-auth-ready', function(e) {
    var session = (e && e.detail) || {};
    if (session.uid) { onUserSignedIn(session.uid); }
  });

  // Also catch auth state if firebase auth is already initialized
  document.addEventListener('DOMContentLoaded', function() {
    try {
      if (typeof firebase !== 'undefined' && firebase.auth) {
        firebase.auth().onAuthStateChanged(function(user) {
          // Anonymous identities (added 2026-07-19 so analytics can count
          // signed-out visitors -- see firebase-auth.js) must NOT trigger
          // the cross-device sync engine below: they're a throwaway
          // per-browser id with no continuity, so syncing to
          // users/{anonUid} would just pollute Firestore with one
          // never-reused doc per anonymous visitor, and wouldn't restore
          // anything real for the visitor either.
          if (user && !user.isAnonymous) { onUserSignedIn(user.uid); }
          else { onUserSignedOut(); }
        });
      }
    } catch(err) {}
  });

  // ── Public API ────────────────────────────────────────────────────────────
  window.aceFirestore = {
    /** Force an immediate Firestore write of all dirty keys */
    save: function() { flushToFirestore(true); },

    /** Manually trigger a pull from Firestore */
    pull: function() {
      if (!_db || !_uid) return Promise.resolve();
      return _db.collection('users').doc(_uid).get().then(function(doc) {
        if (doc.exists) mergeFirestoreData(doc.data());
      });
    },

    /** Check if a key is synced */
    isSynced: function(key) { return isSyncKey(key); },

    /** Status for UI display */
    status: function() {
      return {
        online:  _online,
        synced:  !!_uid && !!_db,
        pending: Object.keys(getPending()).length,
        dirty:   Object.keys(_dirty).length
      };
    }
  };

})();
