/* ═══════════════════════════════════════════════════════
   aceAcademy — Auth Guard
   Included on every protected page.
   - Redirects to login.html if no session exists
   - Injects user avatar + logout into the nav
═══════════════════════════════════════════════════════ */
(function () {
  // ── 1. Check session ──────────────────────────────────
  let session;
  try { session = JSON.parse(localStorage.getItem('aceSession') || 'null'); } catch (e) {}

  if (!session || !session.username) {
    window.location.replace('login.html');
    return;
  }

  // ── 2. Inject user pill into nav once DOM is ready ───
  function injectUserPill() {
    const header = document.querySelector('header') || document.querySelector('nav.topnav');
    if (!header) return;

    // Avoid duplicating
    if (header.querySelector('.ace-user-pill')) return;

    const initials = (session.name || session.username)
      .split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2);

    const gradeLabel = session.grade && session.grade !== 'teacher'
      ? 'Grade ' + session.grade
      : session.grade === 'teacher' ? 'Teacher' : '';

    const pill = document.createElement('div');
    pill.className = 'ace-user-pill';
    pill.innerHTML = `
      <div class="ace-avatar" title="${session.name || session.username}">${initials}</div>
      <div class="ace-user-info">
        <span class="ace-user-name">${session.name || session.username}</span>
        ${gradeLabel ? `<span class="ace-user-grade">${gradeLabel}</span>` : ''}
      </div>
      <button class="ace-logout-btn" onclick="aceLogout()" title="Sign out">⏻</button>
    `;
    header.appendChild(pill);

    // Inject CSS once
    if (!document.getElementById('ace-auth-css')) {
      const style = document.createElement('style');
      style.id = 'ace-auth-css';
      style.textContent = `
        .ace-user-pill {
          display: flex; align-items: center; gap: 8px;
          margin-left: 12px; flex-shrink: 0;
        }
        .ace-avatar {
          width: 32px; height: 32px; border-radius: 50%;
          background: linear-gradient(135deg, #6366f1, #a5b4fc);
          color: #fff; font-size: .72rem; font-weight: 800;
          display: flex; align-items: center; justify-content: center;
          flex-shrink: 0; letter-spacing: .5px;
          box-shadow: 0 0 0 2px rgba(99,102,241,.4);
        }
        .ace-user-info {
          display: flex; flex-direction: column; line-height: 1.2;
        }
        .ace-user-name {
          font-size: .78rem; font-weight: 700; color: #e8edf5;
          max-width: 110px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
        }
        .ace-user-grade {
          font-size: .65rem; color: #7a8fa8; font-weight: 500;
        }
        .ace-logout-btn {
          background: none; border: 1px solid #2a3a55;
          border-radius: 6px; color: #7a8fa8;
          width: 28px; height: 28px; cursor: pointer;
          font-size: .85rem; display: flex; align-items: center; justify-content: center;
          transition: background .15s, color .15s, border-color .15s;
          flex-shrink: 0;
        }
        .ace-logout-btn:hover {
          background: rgba(248,113,113,.15);
          border-color: #f87171; color: #f87171;
        }
        @media (max-width: 600px) {
          .ace-user-info { display: none; }
          .ace-user-pill { gap: 6px; margin-left: 8px; }
        }
      `;
      document.head.appendChild(style);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectUserPill);
  } else {
    injectUserPill();
  }

  // ── 3. Logout function ────────────────────────────────
  window.aceLogout = function () {
    localStorage.removeItem('aceSession');
    window.location.replace('login.html');
  };
})();
