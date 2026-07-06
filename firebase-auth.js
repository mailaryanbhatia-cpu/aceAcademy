/* ═══════════════════════════════════════════════════════
   aceAcademy — Firebase Google Authentication
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
  auth.onAuthStateChanged(function (user) {
    if (user) {
      _saveSession(user);
      // Notify any listeners
      document.dispatchEvent(new CustomEvent('ace-auth-ready', { detail: user }));
    } else {
      localStorage.removeItem('aceSession');
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
