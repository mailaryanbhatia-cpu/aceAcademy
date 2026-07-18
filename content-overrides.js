/**
 * AcerAcademy — content override loader
 *
 * Part of the hybrid content-management approach (added 2026-07-19): the
 * static *-data.js files stay the source of truth for all curriculum/
 * practice-sheet content (fast, no per-pageview database read for the bulk
 * of the site), but admin.html can write per-unit overrides to Firestore's
 * `contentOverrides/{unitKey}` collection, and this file fetches + applies
 * them on pages that display curriculum units.
 *
 * Load this AFTER firebase-app-compat.js / firebase-firestore-compat.js /
 * firebase-auth.js / firestore.js (needs `firebase` to already be
 * initialized) and AFTER curriculum-browser-data.js (needs CURRICULUM to
 * exist so applyContentOverride can be called against real unit objects).
 *
 * Usage on a page's render function:
 *   let u = someUnitFromCURRICULUM;
 *   u = applyContentOverride(u);      // returns u unchanged if no override
 *   // ...render u.unit / u.topics as normal...
 *   // and to merge in admin-added extra practice sheets:
 *   const extra = getExtraPracticeSheets(u.key);
 *   const allSheets = (existingSheets || []).concat(extra);
 *
 * The initial page render doesn't wait on this -- overrides are rare (an
 * admin edit, not routine content), so blocking first paint on a Firestore
 * round-trip for the common case of "no overrides exist" would repeat the
 * exact mistake already fixed once this cycle (see the practice-data.js
 * lazy-load work). Instead: render immediately with whatever's cached
 * (nothing, the first time), then silently re-render once real overrides
 * come back, via the same window['ace-content-overrides-updated'] event
 * every consuming page listens for.
 */
(function () {
  window._contentOverrides = window._contentOverrides || {};

  window._contentOverridesReady = new Promise(function (resolve) {
    function attemptLoad() {
      if (typeof firebase === 'undefined' || !firebase.firestore) {
        // Firebase SDK didn't load (offline, ad-blocker, CDN hiccup, etc.)
        // -- fail open with zero overrides rather than block the page.
        resolve();
        return;
      }
      firebase.firestore().collection('contentOverrides').get()
        .then(function (snap) {
          var any = false;
          snap.forEach(function (doc) {
            window._contentOverrides[doc.id] = doc.data();
            any = true;
          });
          resolve();
          if (any) document.dispatchEvent(new CustomEvent('ace-content-overrides-updated'));
        })
        .catch(function (err) {
          console.warn('[contentOverrides] load failed:', err.message);
          resolve();
        });
    }
    // Firebase's own scripts are loaded via plain <script src> tags (not
    // deferred/async in the pages this is used on), so by the time this
    // IIFE runs, firebase.initializeApp() (called synchronously inside
    // firebase-auth.js) has already run -- attemptLoad() can run
    // immediately rather than needing to wait for any event.
    attemptLoad();
  });

  // Returns a NEW object with any saved override's `unit` title / `topics`
  // list merged in (doesn't mutate the original CURRICULUM data, since that
  // same in-memory object is reused across re-renders and other pages
  // reading it shouldn't see it silently mutated).
  window.applyContentOverride = function (unit) {
    if (!unit || !unit.key) return unit;
    var ov = window._contentOverrides[unit.key];
    if (!ov) return unit;
    var merged = Object.assign({}, unit);
    if (ov.unit) merged.unit = ov.unit;
    if (ov.topics && ov.topics.length) merged.topics = ov.topics;
    return merged;
  };

  // Returns any admin-added extra practice sheets for a unit key (always an
  // array, empty if none) -- callers append these to whatever practice
  // sheets already exist for the unit, they don't replace them.
  window.getExtraPracticeSheets = function (unitKey) {
    var ov = window._contentOverrides[unitKey];
    return (ov && Array.isArray(ov.extraPracticeSheets)) ? ov.extraPracticeSheets : [];
  };
})();
