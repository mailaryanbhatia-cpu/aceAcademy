/* ═══════════════════════════════════════════════════════
   AcerAcademy — Firebase Google Authentication
   Include AFTER the Firebase SDK scripts.
═══════════════════════════════════════════════════════ */
(function () {
  const FIREBASE_CONFIG = {
    apiKey:            "AIzaSyAh6UBfoLXOhbHh0gvN65sVUP88kjWpSlA",
    authDomain:        "aceacademy-33738.firebaseapp.com",
    projectId:         "aceacademy-33738",
    storageBucket:     "aceacademy-33738.firebasestorage.app",
    messagingSenderId: "1043045890971",
    appId:             "1:1043045890971:web:ad87a815c082ca547abf3e"
  };

  // Init Firebase (guard against double-init)
  if (!firebase.apps.length) firebase.initializeApp(FIREBASE_CONFIG);

  // ── App Check (added 2026-07-19) ────────────────────
  // Loaded dynamically rather than as a 4th <script> tag on every one of
  // the ~85 pages that already load the Firebase SDK -- keeps this a
  // one-file change instead of a mechanical multi-page edit. Uses
  // reCAPTCHA v3 (site key below is public/client-side by design, same as
  // any reCAPTCHA site key -- the secret key that actually matters for
  // security lives only in the Firebase Console, never in this code).
  //
  // NOTE: App Check enforcement is OFF by default per Firebase service
  // (Firestore, Auth, etc.) until explicitly turned on in the App Check
  // console tab -- so loading this can't break anything on its own. Once
  // you're ready to enforce it, there's a small timing gap to know about:
  // this script loads asynchronously, so the very first Firestore write
  // on a page (e.g. the initial anonymous sign-in) could theoretically
  // fire before activate() finishes -- fine while unenforced, worth
  // revisiting if enforcement is ever turned on and early writes start
  // getting rejected.
  (function loadAppCheck() {
    var s = document.createElement('script');
    s.src = 'https://www.gstatic.com/firebasejs/9.23.0/firebase-app-check-compat.js';
    s.onload = function () {
      try {
        firebase.appCheck().activate('6Lcbo1stAAAAAN-ehDQCRZel1wjb5p3-FQfLnW7D', true);
      } catch (e) {
        console.warn('[firebase-auth] App Check activation failed:', e.message);
      }
    };
    document.head.appendChild(s);
  })();

  const auth = firebase.auth();
  const provider = new firebase.auth.GoogleAuthProvider();
  provider.addScope('email');
  provider.addScope('profile');

  // ── Public API ───────────────────────────────────────
  window.aceGoogleSignIn = function () {
    return auth.signInWithPopup(provider)
      .then(function (result) {
        _saveSession(result.user);
        return result.user;
      });
  };

  window.aceSignOut = function () {
    return auth.signOut().then(function () {
      localStorage.removeItem('aceSession');
      window.location.replace('/login.html');
    });
  };

  // ── Auth state observer ──────────────────────────────
  // A real (Google) sign-in dispatches 'ace-auth-ready' and persists the
  // session -- everything on the site that gates on being "signed in"
  // (admin.html, login.html, firestore.js's cross-device sync, the
  // homepage greeting) keys off that event, so it must mean a real account.
  //
  // An anonymous Firebase identity (see the else-branch below) is NOT
  // treated as a real session: no event, no localStorage session. It
  // exists purely so firebase.auth().currentUser is non-null for every
  // visitor -- letting analytics.js's site-wide counters and
  // contentOverrides writes satisfy firestore.rules' "signed in" check
  // even for visitors who never click "Sign in with Google" (con #3 fix,
  // 2026-07-19).
  auth.onAuthStateChanged(function (user) {
    if (user && !user.isAnonymous) {
      _saveSession(user);
      // Notify any listeners
      document.dispatchEvent(new CustomEvent('ace-auth-ready', { detail: user }));
    } else if (user && user.isAnonymous) {
      // Already have an anonymous identity for this browser -- nothing to do.
    } else {
      localStorage.removeItem('aceSession');
      // No session of any kind yet -- get an anonymous one. Requires the
      // Anonymous provider to be enabled in the Firebase console
      // (Authentication -> Sign-in method); fails silently and harmlessly
      // if it isn't (analytics/content-override writes just stay
      // signed-out-only, same as before this change).
      auth.signInAnonymously().catch(function (err) {
        console.warn('[firebase-auth] anonymous sign-in failed:', err.message);
      });
    }
  });

  function _saveSession(user) {
    const session = {
      uid:       user.uid,
      username:  user.displayName || user.email,
      name:      user.displayName || '',
      email:     user.email || '',
      avatar:    user.photoURL || '',
      loginTime: Date.now()
    };
    localStorage.setItem('aceSession', JSON.stringify(session));
    // Sync into profile fields used by nav-profile.js
    if (user.displayName) localStorage.setItem('ace_profile_name', user.displayName);
    if (user.photoURL)    localStorage.setItem('ace_avatar', user.photoURL);
    if (user.email)       localStorage.setItem('ace_profile_email', user.email);
  }

  // Expose auth instance for advanced use
  window._aceAuth = auth;
})();
