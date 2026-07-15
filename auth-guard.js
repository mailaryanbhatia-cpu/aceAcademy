/* ═══════════════════════════════════════════════════════
   AcerAcademy — Auth Guard (Firebase + localStorage)
═══════════════════════════════════════════════════════ */
(function () {
  const LOGIN_URL = '/login.html';

  // Pages that are publicly accessible (no redirect)
  const PUBLIC_PAGES = ['/', '/index.html', ''];

  const path = window.location.pathname.replace(/\/+$/, '') || '/';
  const isPublic = PUBLIC_PAGES.some(p => path === p || path.endsWith('/index.html'));

  // ── 1. Fast check: localStorage session ─────────────
  let session;
  try { session = JSON.parse(localStorage.getItem('aceSession') || 'null'); } catch (e) {}

  const loggedIn = session && (session.uid || session.username);

  if (!loggedIn && !isPublic) {
    // Protected page, not logged in — redirect immediately
    window.location.replace(LOGIN_URL);
    return;
  }

  // ── 2. Inject nav pill ───────────────────────────────
  function injectNav() {
    const nav = document.querySelector('nav.topnav') || document.querySelector('header');
    if (!nav || nav.querySelector('#ace-auth-pill')) return;

    const pill = document.createElement('div');
    pill.id = 'ace-auth-pill';
    pill.style.cssText = 'display:flex;align-items:center;gap:8px;margin-left:auto;flex-shrink:0;';

    if (loggedIn) {
      // ── Logged-in: show avatar + name + logout ──
      const name     = session.name || session.username || 'Student';
      const avatar   = session.avatar || '';
      const initials = name.split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2) || '?';

      const av = document.createElement('div');
      if (avatar) {
        av.style.cssText = 'width:30px;height:30px;border-radius:50%;overflow:hidden;flex-shrink:0;box-shadow:0 0 0 2px rgba(129,140,248,.35);';
        const img = document.createElement('img');
        img.src = avatar;
        img.style.cssText = 'width:100%;height:100%;object-fit:cover;';
        img.onerror = function(){ av.innerHTML = initials; av.style.cssText += 'display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;font-size:.7rem;font-weight:800;'; };
        av.appendChild(img);
      } else {
        av.style.cssText = 'width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,#6366f1,#8b5cf6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:.7rem;font-weight:800;flex-shrink:0;box-shadow:0 0 0 2px rgba(129,140,248,.35);';
        av.textContent = initials;
      }

      const nameEl = document.createElement('span');
      nameEl.style.cssText = 'font-size:.78rem;font-weight:600;color:#94a3b8;white-space:nowrap;max-width:100px;overflow:hidden;text-overflow:ellipsis;';
      nameEl.textContent = name.split(' ')[0];

      const logoutBtn = document.createElement('button');
      logoutBtn.title = 'Sign out';
      logoutBtn.textContent = '⏻';
      logoutBtn.style.cssText = 'background:none;border:1px solid rgba(255,255,255,.08);border-radius:7px;color:#475569;width:28px;height:28px;cursor:pointer;font-size:.85rem;display:flex;align-items:center;justify-content:center;transition:all .15s;flex-shrink:0;';
      logoutBtn.onmouseenter = function(){ this.style.background='rgba(239,68,68,.12)';this.style.color='#f87171';this.style.borderColor='rgba(239,68,68,.3)'; };
      logoutBtn.onmouseleave = function(){ this.style.background='none';this.style.color='#475569';this.style.borderColor='rgba(255,255,255,.08)'; };
      logoutBtn.onclick = function(){ aceLogout(); };

      pill.appendChild(av);
      pill.appendChild(nameEl);
      pill.appendChild(logoutBtn);

    } else {
      // ── Logged-out (homepage only): show Login + Sign Up ──
      const loginBtn = document.createElement('a');
      loginBtn.href = LOGIN_URL;
      loginBtn.textContent = 'Log In';
      loginBtn.style.cssText = 'font-size:.8rem;font-weight:600;color:#94a3b8;text-decoration:none;padding:6px 14px;border:1px solid rgba(255,255,255,.12);border-radius:8px;transition:all .15s;white-space:nowrap;';
      loginBtn.onmouseenter = function(){ this.style.color='#e2e8f0';this.style.borderColor='rgba(255,255,255,.3)'; };
      loginBtn.onmouseleave = function(){ this.style.color='#94a3b8';this.style.borderColor='rgba(255,255,255,.12)'; };

      const signupBtn = document.createElement('a');
      signupBtn.href = LOGIN_URL + '?signup=1';
      signupBtn.textContent = 'Sign Up';
      signupBtn.style.cssText = 'font-size:.8rem;font-weight:700;color:#fff;text-decoration:none;padding:6px 14px;background:linear-gradient(135deg,#6366f1,#8b5cf6);border:1px solid transparent;border-radius:8px;transition:all .15s;white-space:nowrap;box-shadow:0 2px 8px rgba(99,102,241,.35);';
      signupBtn.onmouseenter = function(){ this.style.opacity='.88'; };
      signupBtn.onmouseleave = function(){ this.style.opacity='1'; };

      pill.appendChild(loginBtn);
      pill.appendChild(signupBtn);
    }

    // Insert before theme toggle, or append
    const themeBtn = nav.querySelector('[onclick*="toggleTheme"], #themeToggle, #themeToggleBtn');
    const profileLink = nav.querySelector('#ace-nav-profile');
    if (profileLink) profileLink.remove();
    if (themeBtn) nav.insertBefore(pill, themeBtn);
    else nav.appendChild(pill);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectNav);
  } else {
    injectNav();
  }

  // ── 3. Firebase sign-out ──────────────────────────────
  window.aceLogout = function () {
    localStorage.removeItem('aceSession');
    // Flag this as a deliberate logout so login.html -- which is the
    // page that actually has the Firebase SDK loaded, unlike most
    // pages auth-guard.js runs on -- knows to finish signing out of
    // Firebase itself instead of bouncing back here if it briefly
    // still sees a signed-in Firebase session on load.
    try { sessionStorage.setItem('ace_logout_requested', '1'); } catch (e) {}
    if (window._aceAuth) {
      window._aceAuth.signOut().catch(function(){});
    }
    window.location.replace(LOGIN_URL);
  };
})();
