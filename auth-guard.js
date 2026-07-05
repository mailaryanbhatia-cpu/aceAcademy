/* ═══════════════════════════════════════════════════════
   aceAcademy — Auth Guard (Firebase + localStorage)
═══════════════════════════════════════════════════════ */
(function () {
  const LOGIN_URL = '/aceAcademy/login.html';

  // ── 1. Fast check: localStorage session ─────────────
  let session;
  try { session = JSON.parse(localStorage.getItem('aceSession') || 'null'); } catch (e) {}

  if (!session || (!session.uid && !session.username)) {
    // No local session — redirect immediately
    window.location.replace(LOGIN_URL);
    return;
  }

  // ── 2. Inject user pill ──────────────────────────────
  function injectUserPill() {
    const nav = document.querySelector('nav.topnav') || document.querySelector('header');
    if (!nav || nav.querySelector('#ace-auth-pill')) return;

    const name    = session.name || session.username || 'Student';
    const avatar  = session.avatar || '';
    const initials = name.split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2) || '?';

    const pill = document.createElement('div');
    pill.id = 'ace-auth-pill';
    pill.style.cssText = 'display:flex;align-items:center;gap:9px;margin-left:auto;flex-shrink:0;';

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

    // Insert before last item or append
    const themeBtn = nav.querySelector('[onclick*="toggleTheme"], #themeToggle');
    const profileLink = nav.querySelector('#ace-nav-profile');
    if (profileLink) profileLink.remove(); // remove old profile pill
    if (themeBtn) nav.insertBefore(pill, themeBtn);
    else nav.appendChild(pill);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectUserPill);
  } else {
    injectUserPill();
  }

  // ── 3. Firebase sign-out (works for both Google + local) ──
  window.aceLogout = function () {
    localStorage.removeItem('aceSession');
    // Sign out from Firebase if available
    if (window._aceAuth) {
      window._aceAuth.signOut().catch(function(){});
    }
    window.location.replace(LOGIN_URL);
  };
})();
