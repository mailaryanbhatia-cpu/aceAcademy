// ── aceAcademy Firestore Sync ────────────────────────────────────────────────
// Single document per user: users/{uid}/data
// Strategy: localStorage = fast local cache, Firestore = source of truth
// On login  → pull Firestore → populate localStorage
// On change → write localStorage immediately + queue Firestore write (debounced)

(function(){
  // Keys we sync between localStorage ↔ Firestore
  const SYNC_KEYS = {
    streak:            'ace_streak',
    lastChallengeDate: 'ace_last_challenge_date',
    coins:             'ace_coins',
    flashcards:        'ace_flashcard_due',
    testHistory:       'ace_test_history',
    goals:             'ace_goals',
    mastery:           'ace_mastery',
    profileName:       'ace_profile_name',
    avatar:            'ace_avatar',
    subjects:          'ace_subjects',
    onboarded:         'ace_onboarded',
    tourDone:          'ace_tour_done',
  };

  let _db = null;
  let _uid = null;
  let _saveTimer = null;

  // ── Init ──────────────────────────────────────────────────────────────────
  function init(db, uid) {
    _db  = db;
    _uid = uid;
    loadFromFirestore();
  }

  // ── Pull Firestore → localStorage ─────────────────────────────────────────
  function loadFromFirestore() {
    if (!_db || !_uid) return;
    _db.collection('users').doc(_uid).get().then(doc => {
      if (!doc.exists) {
        // First time user — push whatever's in localStorage up
        saveToFirestore();
        return;
      }
      const remote = doc.data();
      const remoteUpdated = remote.updatedAt ? remote.updatedAt.toMillis() : 0;

      // Merge: take whichever is newer (local vs remote)
      Object.entries(SYNC_KEYS).forEach(([fsKey, lsKey]) => {
        if (remote[fsKey] !== undefined) {
          const local = localStorage.getItem(lsKey);
          // For numbers (streak, coins) take the higher value
          if (fsKey === 'streak' || fsKey === 'coins') {
            const remoteVal = remote[fsKey] || 0;
            const localVal  = parseInt(local || '0');
            localStorage.setItem(lsKey, Math.max(remoteVal, localVal));
          } else {
            // For everything else, use remote if it exists
            const val = typeof remote[fsKey] === 'object'
              ? JSON.stringify(remote[fsKey])
              : String(remote[fsKey]);
            localStorage.setItem(lsKey, val);
          }
        }
      });

      // Fire event so any open page can refresh its UI
      window.dispatchEvent(new CustomEvent('ace-firestore-loaded'));
    }).catch(err => console.warn('Firestore load error:', err));
  }

  // ── Push localStorage → Firestore (debounced 3s) ─────────────────────────
  function queueSave() {
    clearTimeout(_saveTimer);
    _saveTimer = setTimeout(saveToFirestore, 3000);
  }

  function saveToFirestore() {
    if (!_db || !_uid) return;
    const data = { updatedAt: firebase.firestore.FieldValue.serverTimestamp() };

    Object.entries(SYNC_KEYS).forEach(([fsKey, lsKey]) => {
      const raw = localStorage.getItem(lsKey);
      if (raw === null) return;
      // Try to parse JSON (arrays/objects), otherwise store as string/number
      try {
        const parsed = JSON.parse(raw);
        data[fsKey] = parsed;
      } catch(e) {
        // Plain string or number
        const num = Number(raw);
        data[fsKey] = isNaN(num) ? raw : num;
      }
    });

    _db.collection('users').doc(_uid).set(data, { merge: true })
      .catch(err => console.warn('Firestore save error:', err));
  }

  // ── Public API ────────────────────────────────────────────────────────────
  window.aceFirestore = {
    init,
    save: saveToFirestore,
    queueSave,
    load: loadFromFirestore,
  };

  // ── Patch localStorage so writes auto-sync ────────────────────────────────
  const _origSetItem = localStorage.setItem.bind(localStorage);
  localStorage.setItem = function(key, value) {
    _origSetItem(key, value);
    const isSyncKey = Object.values(SYNC_KEYS).includes(key);
    if (isSyncKey && _uid) { queueSave(); }
  };

  // ── Wire up after Firebase auth is ready ──────────────────────────────────
  window.addEventListener('ace-auth-ready', function(e) {
    const session = e.detail || {};
    if (!session.uid) return; // local-only user, no Firestore
    try {
      const db = firebase.firestore();
      init(db, session.uid);
    } catch(err) {
      console.warn('Firestore init error:', err);
    }
  });

  // Also handle case where auth loads after this script
  if (window._aceAuth) {
    window._aceAuth.onAuthStateChanged(user => {
      if (user && !_uid) {
        try {
          const db = firebase.firestore();
          init(db, user.uid);
        } catch(err) {}
      }
    });
  }
})();
