(function(){
  // ── Streak logic ──────────────────────────────────────────────
  var STREAK_KEY  = 'ace_login_streak';
  var BADGES_KEY  = 'ace_badges';
  var today = new Date().toISOString().split('T')[0];

  var data  = JSON.parse(localStorage.getItem(STREAK_KEY) || '{"count":0,"last":""}');
  var count = data.count || 0;
  var confettiMilestone = false;
  var newBadge = null;

  if (data.last !== today) {
    var yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    var yd = yesterday.toISOString().split('T')[0];
    count = (data.last === yd || data.last === '') ? (data.last === '' ? 1 : count + 1) : 1;
    data  = { count: count, last: today };
    localStorage.setItem(STREAK_KEY, JSON.stringify(data));
    if (count > 0 && count % 10 === 0) confettiMilestone = true;

    // Badge check (30/60/90/365)
    var BADGE_DEFS = [
      { days:30,  id:'bronze',   emoji:'🥉', label:'Bronze Scholar',   color:'#cd7f32', desc:'30-day streak!' },
      { days:60,  id:'silver',   emoji:'🥈', label:'Silver Scholar',   color:'#c0c0c0', desc:'60-day streak!' },
      { days:90,  id:'gold',     emoji:'🥇', label:'Gold Scholar',     color:'#ffd700', desc:'90-day streak!' },
      { days:365, id:'diamond',  emoji:'💎', label:'Diamond Scholar',  color:'#b9f2ff', desc:'365-day streak!' }
    ];
    var earned = JSON.parse(localStorage.getItem(BADGES_KEY) || '[]');
    BADGE_DEFS.forEach(function(b){
      if (count >= b.days && earned.indexOf(b.id) === -1) {
        earned.push(b.id);
        newBadge = b;
      }
    });
    if (newBadge) localStorage.setItem(BADGES_KEY, JSON.stringify(earned));
  }

  // ── Push notifications ─────────────────────────────────────────
  function requestNotifPermission() {
    if (!('Notification' in window)) return;
    if (Notification.permission === 'default') {
      setTimeout(function(){
        Notification.requestPermission();
      }, 4000); // ask after 4s so it feels natural
    }
  }

  function scheduleStreakReminder() {
    if (!('serviceWorker' in navigator)) return;
    navigator.serviceWorker.ready.then(function(reg){
      // Periodic background sync (Chrome/Android PWA)
      if ('periodicSync' in reg) {
        reg.periodicSync.register('streak-reminder', { minInterval: 20 * 60 * 60 * 1000 })
          .catch(function(){});
      }
      // Store today so SW knows if reminder is needed
      localStorage.setItem('ace_last_visit_date', today);
    });
  }

  // ── Badge modal ───────────────────────────────────────────────
  function showBadgeModal(b) {
    var style = document.createElement('style');
    style.textContent = [
      '@keyframes ace-badge-in{from{opacity:0;transform:translate(-50%,-50%) scale(.6)}to{opacity:1;transform:translate(-50%,-50%) scale(1)}}',
      '@keyframes ace-badge-glow{0%,100%{box-shadow:0 0 30px '+b.color+'88}50%{box-shadow:0 0 60px '+b.color+'cc}}'
    ].join('');
    document.head.appendChild(style);

    var overlay = document.createElement('div');
    overlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.75);z-index:99998;backdrop-filter:blur(4px)';
    
    var modal = document.createElement('div');
    modal.style.cssText = [
      'position:fixed','top:50%','left:50%',
      'transform:translate(-50%,-50%)',
      'background:linear-gradient(135deg,#0f172a,#1e1b4b)',
      'border:2px solid '+b.color,
      'border-radius:24px','padding:40px 48px',
      'text-align:center','z-index:99999',
      'animation:ace-badge-in .5s cubic-bezier(.34,1.56,.64,1) forwards, ace-badge-glow 2s ease-in-out 0.5s infinite',
      'max-width:340px','width:90%'
    ].join(';');

    modal.innerHTML = [
      '<div style="font-size:72px;line-height:1;margin-bottom:12px">'+b.emoji+'</div>',
      '<div style="font-size:1.4rem;font-weight:800;color:'+b.color+';margin-bottom:6px">'+b.label+'</div>',
      '<div style="font-size:1rem;color:#94a3b8;margin-bottom:6px">'+b.desc+'</div>',
      '<div style="font-size:2rem;font-weight:900;color:#fff;margin-bottom:20px">🔥 '+count+' Days</div>',
      '<button onclick="this.closest(\'div\').previousSibling.remove();this.closest(\'div\').remove();" ',
      'style="background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;border:none;',
      'padding:10px 28px;border-radius:99px;font-size:.95rem;font-weight:700;cursor:pointer">',
      'Awesome! 🎉</button>'
    ].join('');

    overlay.onclick = function(){ overlay.remove(); modal.remove(); };
    document.body.appendChild(overlay);
    document.body.appendChild(modal);
  }

  // ── Confetti ──────────────────────────────────────────────────
  function fireConfetti() {
    if (typeof confetti === 'undefined') return;
    var cols = ['#6366f1','#8b5cf6','#ec4899','#f59e0b','#10b981','#3b82f6','#ffd700'];
    confetti({ particleCount:150, spread:100, origin:{y:.55}, colors:cols });
    setTimeout(function(){ confetti({ particleCount:80, spread:130, origin:{y:.45}, colors:cols }); }, 400);
    setTimeout(function(){
      confetti({ particleCount:70, spread:90, origin:{x:.15,y:.65}, colors:cols });
      confetti({ particleCount:70, spread:90, origin:{x:.85,y:.65}, colors:cols });
    }, 800);
  }

  function loadConfettiThen(cb){
    if (typeof confetti !== 'undefined') { cb(); return; }
    var s = document.createElement('script');
    s.src = 'https://cdnjs.cloudflare.com/ajax/libs/canvas-confetti/1.9.2/confetti.browser.min.js';
    s.onload = cb;
    document.head.appendChild(s);
  }

  // ── Streak toast ──────────────────────────────────────────────
  function showToast(msg) {
    var st = document.createElement('style');
    st.textContent = '@keyframes ace-ti{from{opacity:0;transform:translateX(-50%) translateY(-24px)}to{opacity:1;transform:translateX(-50%) translateY(0)}}';
    document.head.appendChild(st);
    var t = document.createElement('div');
    t.style.cssText = 'position:fixed;top:20px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;font-size:1.05rem;font-weight:800;padding:13px 26px;border-radius:14px;box-shadow:0 8px 32px rgba(99,102,241,.5);z-index:99999;text-align:center;animation:ace-ti .4s ease;white-space:nowrap';
    t.innerHTML = msg;
    document.body.appendChild(t);
    setTimeout(function(){ t.style.transition='opacity .5s'; t.style.opacity='0'; }, 3500);
    setTimeout(function(){ t.remove(); }, 4000);
  }

  // ── Badge pill in streak button ───────────────────────────────
  function getBadgeEmoji() {
    var earned = JSON.parse(localStorage.getItem(BADGES_KEY) || '[]');
    if (earned.indexOf('diamond') !== -1) return ' 💎';
    if (earned.indexOf('gold')    !== -1) return ' 🥇';
    if (earned.indexOf('silver')  !== -1) return ' 🥈';
    if (earned.indexOf('bronze')  !== -1) return ' 🥉';
    return '';
  }

  // ── Main badge ────────────────────────────────────────────────
  function injectBadge() {
    if (document.getElementById('ace-streak-badge')) return;
    var badge = document.createElement('div');
    badge.id = 'ace-streak-badge';
    badge.title = count + '-day streak! Click to see your badges';
    badge.style.cssText = 'position:fixed;bottom:18px;right:18px;z-index:9999;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;font-size:.82rem;font-weight:700;padding:8px 14px;border-radius:999px;box-shadow:0 4px 18px rgba(99,102,241,.45);cursor:pointer;display:flex;align-items:center;gap:5px;user-select:none;transition:transform .15s';
    badge.innerHTML = '🔥 ' + count + ' day' + (count===1?'':'s') + getBadgeEmoji();
    badge.onmouseenter = function(){ this.style.transform='scale(1.08)'; };
    badge.onmouseleave = function(){ this.style.transform='scale(1)'; };
    badge.onclick = showBadgePanel;
    document.body.appendChild(badge);
  }

  // ── Badge panel ───────────────────────────────────────────────
  function showBadgePanel() {
    var BADGE_DEFS = [
      { days:30,  id:'bronze',  emoji:'🥉', label:'Bronze Scholar',  color:'#cd7f32' },
      { days:60,  id:'silver',  emoji:'🥈', label:'Silver Scholar',  color:'#c0c0c0' },
      { days:90,  id:'gold',    emoji:'🥇', label:'Gold Scholar',    color:'#ffd700' },
      { days:365, id:'diamond', emoji:'💎', label:'Diamond Scholar', color:'#b9f2ff' }
    ];
    var earned = JSON.parse(localStorage.getItem(BADGES_KEY) || '[]');
    var overlay = document.createElement('div');
    overlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:99998;backdrop-filter:blur(3px)';
    var panel = document.createElement('div');
    panel.style.cssText = 'position:fixed;bottom:70px;right:18px;background:#0f172a;border:1px solid #334155;border-radius:18px;padding:20px 22px;z-index:99999;min-width:240px;box-shadow:0 12px 40px rgba(0,0,0,.5)';

    var rows = BADGE_DEFS.map(function(b){
      var got = earned.indexOf(b.id) !== -1;
      return '<div style="display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid #1e293b;opacity:'+(got?'1':'0.35')+'">'
        + '<span style="font-size:1.6rem">'+(got?b.emoji:'⬜')+'</span>'
        + '<div><div style="font-weight:700;color:'+(got?b.color:'#64748b')+';font-size:.88rem">'+b.label+'</div>'
        + '<div style="font-size:.73rem;color:#64748b">'+(got?'Earned!':b.days+' day streak')+'</div></div></div>';
    }).join('');

    panel.innerHTML = '<div style="font-weight:800;font-size:.95rem;color:#e2e8f0;margin-bottom:10px">🏆 Your Badges</div>'
      + '<div style="font-size:.8rem;color:#94a3b8;margin-bottom:8px">Current streak: 🔥 '+count+' days</div>'
      + rows
      + '<button onclick="this.parentNode.remove();document.querySelector(\'.ace-overlay\').remove();" style="margin-top:12px;width:100%;background:#1e293b;color:#94a3b8;border:none;padding:7px;border-radius:8px;cursor:pointer;font-size:.8rem">Close</button>';
    
    overlay.className = 'ace-overlay';
    overlay.onclick = function(){ overlay.remove(); panel.remove(); };
    document.body.appendChild(overlay);
    document.body.appendChild(panel);
  }

  // ── Init ──────────────────────────────────────────────────────
  function init() {
    injectBadge();
    requestNotifPermission();
    scheduleStreakReminder();

    if (newBadge) {
      loadConfettiThen(function(){
        setTimeout(function(){
          fireConfetti();
          setTimeout(function(){ showBadgeModal(newBadge); }, 600);
        }, 300);
      });
    } else if (confettiMilestone) {
      loadConfettiThen(function(){
        setTimeout(fireConfetti, 400);
        setTimeout(function(){ showToast('🎉 ' + count + '-Day Streak! You\'re on fire!'); }, 200);
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // ── Service worker registration ───────────────────────────────
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function(){
      navigator.serviceWorker.register('/aceAcademy/sw.js').catch(function(){});
    });
  }
})();
