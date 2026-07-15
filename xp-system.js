// ── aceAcademy XP & Study Streak System ──────────────────────────
// Single source of truth for total XP, level, and the activity streak
// (current + longest + calendar history). Mirrors the coins.js /
// streak.js module pattern already used on this site so it fits the
// existing conventions -- IIFE, window.AceXP export, localStorage-only
// persistence, no build step.
//
// This absorbs the role the Daily-Challenge-only streak (dc-streak /
// dc-last / dc-history in index.html) used to play: any completed
// learning activity now advances ONE streak instead of just the daily
// challenge. Existing dc-* progress is migrated in automatically the
// first time this file runs, so nobody's current streak resets.
window.AceXP = (function () {
  var XP_KEY             = 'ace_xp_total';
  var XP_LOG_KEY          = 'ace_xp_log';
  var STREAK_KEY          = 'ace_streak';
  var STREAK_LONGEST_KEY  = 'ace_streak_longest';
  var STREAK_LAST_KEY     = 'ace_streak_last';
  var HISTORY_KEY         = 'ace_activity_history';

  // ── One-time migration from the old Daily-Challenge-only streak ──
  (function migrate() {
    if (localStorage.getItem(STREAK_KEY) !== null) return; // already initialized
    var oldStreak = parseInt(localStorage.getItem('dc-streak') || '0', 10);
    var oldLast   = localStorage.getItem('dc-last') || '';
    var oldHist   = [];
    try { oldHist = JSON.parse(localStorage.getItem('dc-history') || '[]'); } catch (e) {}
    localStorage.setItem(STREAK_KEY, String(oldStreak || 0));
    localStorage.setItem(STREAK_LONGEST_KEY, String(oldStreak || 0));
    localStorage.setItem(STREAK_LAST_KEY, oldLast);
    localStorage.setItem(HISTORY_KEY, JSON.stringify(oldHist));
  })();

  // ── XP + level ────────────────────────────────────────────────
  function getTotalXP() { return parseInt(localStorage.getItem(XP_KEY) || '0', 10); }
  function setTotalXP(n) { localStorage.setItem(XP_KEY, String(Math.max(0, n))); }

  function logXP(amount, reason) {
    var logs = [];
    try { logs = JSON.parse(localStorage.getItem(XP_LOG_KEY) || '[]'); } catch (e) {}
    logs.unshift({ amount: amount, reason: reason, date: new Date().toISOString() });
    if (logs.length > 100) logs = logs.slice(0, 100);
    localStorage.setItem(XP_LOG_KEY, JSON.stringify(logs));
  }

  // Increasing-threshold level curve: level 1→2 needs 100 XP, 2→3
  // needs 150, 3→4 needs 200, growing +50 each level -- gets harder
  // to level up the further you go, same shape as Duolingo's curve.
  function calcLevel(xp) {
    var level = 1, used = 0, next = 100;
    while (xp >= used + next) {
      used += next;
      level++;
      next += 50;
    }
    return { level: level, xpIntoLevel: xp - used, xpForNextLevel: next, totalAtLevelStart: used };
  }

  function getLevel() { return calcLevel(getTotalXP()); }

  // ── Streak ────────────────────────────────────────────────────
  function getStreak() {
    return {
      current: parseInt(localStorage.getItem(STREAK_KEY) || '0', 10),
      longest: parseInt(localStorage.getItem(STREAK_LONGEST_KEY) || '0', 10)
    };
  }

  function getHistory() {
    try { return JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]'); } catch (e) { return []; }
  }

  function bumpStreak() {
    var today = new Date().toDateString();
    var last  = localStorage.getItem(STREAK_LAST_KEY) || '';
    var streak  = parseInt(localStorage.getItem(STREAK_KEY) || '0', 10);
    var longest = parseInt(localStorage.getItem(STREAK_LONGEST_KEY) || '0', 10);
    var isNewDay = last !== today;

    if (isNewDay) {
      var yesterday = new Date(Date.now() - 86400000).toDateString();
      streak = (last === yesterday) ? streak + 1 : 1;
      localStorage.setItem(STREAK_LAST_KEY, today);
      localStorage.setItem(STREAK_KEY, String(streak));
      if (streak > longest) {
        longest = streak;
        localStorage.setItem(STREAK_LONGEST_KEY, String(longest));
      }
      var hist = getHistory();
      if (hist.indexOf(today) === -1) {
        hist.push(today);
        if (hist.length > 365) hist.shift();
        localStorage.setItem(HISTORY_KEY, JSON.stringify(hist));
      }
    }
    return { current: streak, longest: longest, isNewDay: isNewDay };
  }

  // ── Award XP for a completed activity (the main public entry point) ──
  function recordActivity(amount, reason) {
    var before = calcLevel(getTotalXP());
    setTotalXP(getTotalXP() + amount);
    logXP(amount, reason || 'Activity');
    var after = calcLevel(getTotalXP());
    var streakInfo = bumpStreak();

    updateAllBadges();
    showXpFloater('+' + amount + ' XP');
    if (window.AceSound) { try { window.AceSound.coin(); } catch (e) {} }

    if (after.level > before.level) {
      celebrateLevelUp(after.level);
    } else if (streakInfo.isNewDay && streakInfo.current > 1) {
      showStreakToast(streakInfo.current);
    }

    return { total: getTotalXP(), level: after.level, streak: streakInfo };
  }

  // ── Floating badge (level + streak flame), shown on pages that
  //    load this file. Stacks above the existing coin/streak-login
  //    badges from coins.js / streak.js if those are also present. ──
  function updateAllBadges() {
    var pill = document.getElementById('ace-xp-badge');
    if (!pill) return;
    var lv = getLevel();
    var st = getStreak();
    pill.innerHTML = '🔥 ' + st.current + ' &nbsp;·&nbsp; Lv ' + lv.level;
    pill.title = getTotalXP().toLocaleString() + ' total XP · Longest streak: ' + st.longest + ' days';
  }

  function injectBadge() {
    if (document.getElementById('ace-xp-badge')) return;
    var badge = document.createElement('div');
    badge.id = 'ace-xp-badge';
    badge.style.cssText = 'position:fixed;bottom:106px;right:18px;z-index:9998;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;font-size:.78rem;font-weight:800;padding:6px 13px;border-radius:999px;box-shadow:0 3px 12px rgba(99,102,241,.45);cursor:pointer;user-select:none;';
    badge.onclick = showXpPanel;
    document.body.appendChild(badge);
    updateAllBadges();
  }

  // ── "+N XP" pop animation ────────────────────────────────────────
  function showXpFloater(text) {
    var st = document.createElement('style');
    st.textContent = '@keyframes ace-xp-pop{0%{opacity:0;transform:translateY(10px) scale(.8)}40%{opacity:1;transform:translateY(-8px) scale(1.12)}100%{opacity:0;transform:translateY(-26px) scale(1)}}';
    document.head.appendChild(st);
    var el = document.createElement('div');
    el.style.cssText = 'position:fixed;bottom:150px;right:22px;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;font-weight:800;font-size:.92rem;padding:7px 15px;border-radius:99px;z-index:99998;pointer-events:none;box-shadow:0 4px 16px rgba(99,102,241,.4);animation:ace-xp-pop .7s ease forwards';
    el.textContent = text;
    document.body.appendChild(el);
    setTimeout(function () { el.remove(); }, 1100);
  }

  // ── Streak-extended toast ─────────────────────────────────────────
  function showStreakToast(days) {
    var st = document.createElement('style');
    st.textContent = '@keyframes ace-xp-ti{from{opacity:0;transform:translateX(-50%) translateY(-24px)}to{opacity:1;transform:translateX(-50%) translateY(0)}}';
    document.head.appendChild(st);
    var t = document.createElement('div');
    t.style.cssText = 'position:fixed;top:20px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,#f59e0b,#ef4444);color:#fff;font-size:1.02rem;font-weight:800;padding:12px 24px;border-radius:14px;box-shadow:0 8px 32px rgba(239,68,68,.4);z-index:99999;text-align:center;animation:ace-xp-ti .4s ease;white-space:nowrap';
    t.innerHTML = '🔥 ' + days + '-Day Streak!';
    document.body.appendChild(t);
    setTimeout(function () { t.style.transition = 'opacity .5s'; t.style.opacity = '0'; }, 2600);
    setTimeout(function () { t.remove(); }, 3100);
  }

  // ── Level-up celebration ──────────────────────────────────────────
  function loadConfettiThen(cb) {
    if (typeof confetti !== 'undefined') { cb(); return; }
    var s = document.createElement('script');
    s.src = 'https://cdnjs.cloudflare.com/ajax/libs/canvas-confetti/1.9.2/confetti.browser.min.js';
    s.onload = cb;
    document.head.appendChild(s);
  }

  function celebrateLevelUp(level) {
    loadConfettiThen(function () {
      var cols = ['#6366f1', '#8b5cf6', '#ec4899', '#f59e0b', '#10b981'];
      confetti({ particleCount: 140, spread: 100, origin: { y: .55 }, colors: cols });
    });

    var style = document.createElement('style');
    style.textContent = '@keyframes ace-lvl-in{from{opacity:0;transform:translate(-50%,-50%) scale(.6)}to{opacity:1;transform:translate(-50%,-50%) scale(1)}}';
    document.head.appendChild(style);

    var overlay = document.createElement('div');
    overlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.75);z-index:99998;backdrop-filter:blur(4px)';
    var modal = document.createElement('div');
    modal.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:linear-gradient(135deg,#0f172a,#1e1b4b);border:2px solid #8b5cf6;border-radius:24px;padding:40px 48px;text-align:center;z-index:99999;animation:ace-lvl-in .5s cubic-bezier(.34,1.56,.64,1) forwards;max-width:320px;width:90%';
    modal.innerHTML = '<div style="font-size:56px;line-height:1;margin-bottom:10px">⚡</div>'
      + '<div style="font-size:1.1rem;color:#94a3b8;margin-bottom:4px">Level Up!</div>'
      + '<div style="font-size:2.4rem;font-weight:900;color:#fff;margin-bottom:18px">Level ' + level + '</div>'
      + '<button onclick="this.parentNode.previousSibling.remove();this.parentNode.remove();" style="background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;border:none;padding:10px 28px;border-radius:99px;font-size:.95rem;font-weight:700;cursor:pointer">Nice! 🎉</button>';

    overlay.onclick = function () { overlay.remove(); modal.remove(); };
    document.body.appendChild(overlay);
    document.body.appendChild(modal);
  }

  // ── XP breakdown panel ──────────────────────────────────────────
  function showXpPanel() {
    var lv = getLevel();
    var st = getStreak();
    var logs = [];
    try { logs = JSON.parse(localStorage.getItem(XP_LOG_KEY) || '[]'); } catch (e) {}

    var rows = logs.slice(0, 15).map(function (l) {
      return '<div style="display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid #1e293b;font-size:.78rem">'
        + '<span style="color:#94a3b8">' + l.reason + '</span>'
        + '<span style="font-weight:700;color:#a5b4fc">+' + l.amount + ' XP</span></div>';
    }).join('') || '<div style="color:#475569;text-align:center;padding:12px">No XP earned yet — complete a test, flashcard session, or mark a topic practiced.</div>';

    var overlay = document.createElement('div');
    overlay.className = 'ace-xp-overlay';
    overlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:99998;backdrop-filter:blur(3px)';
    var panel = document.createElement('div');
    panel.style.cssText = 'position:fixed;bottom:150px;right:18px;background:#0f172a;border:1px solid #334155;border-radius:18px;padding:20px 22px;z-index:99999;min-width:260px;max-width:310px;max-height:420px;overflow-y:auto;box-shadow:0 12px 40px rgba(0,0,0,.5)';
    panel.innerHTML =
      '<div style="font-weight:800;font-size:1.05rem;color:#fff;margin-bottom:2px">Level ' + lv.level + '</div>'
      + '<div style="font-size:.78rem;color:#94a3b8;margin-bottom:10px">' + getTotalXP().toLocaleString() + ' total XP</div>'
      + '<div style="background:#1e293b;border-radius:8px;height:8px;overflow:hidden;margin-bottom:4px"><div style="height:100%;background:linear-gradient(90deg,#6366f1,#8b5cf6);width:' + Math.round(100 * lv.xpIntoLevel / lv.xpForNextLevel) + '%"></div></div>'
      + '<div style="font-size:.7rem;color:#64748b;margin-bottom:14px">' + lv.xpIntoLevel + ' / ' + lv.xpForNextLevel + ' XP to Level ' + (lv.level + 1) + '</div>'
      + '<div style="display:flex;gap:16px;margin-bottom:14px">'
      + '<div><div style="font-size:1.3rem;font-weight:800;color:#f59e0b">🔥 ' + st.current + '</div><div style="font-size:.68rem;color:#64748b">Current streak</div></div>'
      + '<div><div style="font-size:1.3rem;font-weight:800;color:#94a3b8">🏆 ' + st.longest + '</div><div style="font-size:.68rem;color:#64748b">Longest streak</div></div>'
      + '</div>'
      + '<div style="font-weight:700;font-size:.82rem;color:#e2e8f0;margin-bottom:6px">Recent XP</div>'
      + rows
      + '<button onclick="this.parentNode.remove();document.querySelector(\'.ace-xp-overlay\').remove();" style="margin-top:12px;width:100%;background:#1e293b;color:#94a3b8;border:none;padding:7px;border-radius:8px;cursor:pointer;font-size:.8rem">Close</button>';

    overlay.onclick = function () { overlay.remove(); panel.remove(); };
    document.body.appendChild(overlay);
    document.body.appendChild(panel);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectBadge);
  } else {
    injectBadge();
  }

  return {
    recordActivity: recordActivity,
    getTotalXP: getTotalXP,
    getLevel: getLevel,
    getStreak: getStreak,
    getHistory: getHistory,
    showXpPanel: showXpPanel,
    updateAllBadges: updateAllBadges
  };
})();
