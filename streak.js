(function(){
  // ── Streak logic ──────────────────────────────────────────────
  var KEY = 'ace_login_streak';
  var today = new Date().toISOString().split('T')[0];
  var data = JSON.parse(localStorage.getItem(KEY) || '{"count":0,"last":""}');
  var prev = data.last;
  var count = data.count || 0;
  var milestone = false;

  if (prev !== today) {
    var yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    var yd = yesterday.toISOString().split('T')[0];

    if (prev === yd) {
      count++;                       // continued streak
    } else if (prev === '') {
      count = 1;                     // first ever visit
    } else {
      count = 1;                     // streak broken, restart
    }
    data = { count: count, last: today };
    localStorage.setItem(KEY, JSON.stringify(data));

    // Milestone every 10 days
    if (count > 0 && count % 10 === 0) milestone = true;
  }

  // ── Badge UI ──────────────────────────────────────────────────
  function injectBadge() {
    if (document.getElementById('ace-streak-badge')) return;
    var badge = document.createElement('div');
    badge.id = 'ace-streak-badge';
    badge.title = count + '-day streak!';
    badge.style.cssText = [
      'position:fixed',
      'bottom:18px',
      'right:18px',
      'z-index:9999',
      'background:linear-gradient(135deg,#6366f1,#8b5cf6)',
      'color:#fff',
      'font-size:.82rem',
      'font-weight:700',
      'padding:7px 13px',
      'border-radius:999px',
      'box-shadow:0 4px 18px rgba(99,102,241,.45)',
      'cursor:default',
      'display:flex',
      'align-items:center',
      'gap:5px',
      'user-select:none',
      'transition:transform .15s'
    ].join(';');
    badge.innerHTML = '🔥 ' + count + ' day' + (count === 1 ? '' : 's');
    badge.onmouseenter = function(){ this.style.transform = 'scale(1.08)'; };
    badge.onmouseleave = function(){ this.style.transform = 'scale(1)'; };
    document.body.appendChild(badge);
  }

  // ── Confetti (every 10 days) ──────────────────────────────────
  function fireConfetti() {
    if (typeof confetti === 'undefined') return;
    var colors = ['#6366f1','#8b5cf6','#ec4899','#f59e0b','#10b981','#3b82f6'];
    confetti({ particleCount: 120, spread: 90, origin: { y: 0.6 }, colors: colors });
    setTimeout(function(){
      confetti({ particleCount: 80, spread: 120, origin: { y: 0.5 }, colors: colors });
    }, 400);
    setTimeout(function(){
      confetti({ particleCount: 60, spread: 80, origin: { x: 0.2, y: 0.7 }, colors: colors });
      confetti({ particleCount: 60, spread: 80, origin: { x: 0.8, y: 0.7 }, colors: colors });
    }, 800);

    // Toast message
    var toast = document.createElement('div');
    toast.style.cssText = [
      'position:fixed','top:24px','left:50%','transform:translateX(-50%)',
      'background:linear-gradient(135deg,#6366f1,#8b5cf6)',
      'color:#fff','font-size:1.1rem','font-weight:800',
      'padding:14px 28px','border-radius:14px',
      'box-shadow:0 8px 32px rgba(99,102,241,.5)',
      'z-index:99999','text-align:center',
      'animation:ace-toast-in .4s ease'
    ].join(';');
    toast.innerHTML = '🎉 ' + count + '-Day Streak! Keep it up!';
    var style = document.createElement('style');
    style.textContent = '@keyframes ace-toast-in{from{opacity:0;transform:translateX(-50%) translateY(-20px)}to{opacity:1;transform:translateX(-50%) translateY(0)}}';
    document.head.appendChild(style);
    document.body.appendChild(toast);
    setTimeout(function(){ toast.style.opacity='0'; toast.style.transition='opacity .5s'; }, 3500);
    setTimeout(function(){ toast.remove(); }, 4000);
  }

  // ── Init on DOM ready ─────────────────────────────────────────
  function init() {
    injectBadge();
    if (milestone) {
      // Load confetti lib then fire
      if (typeof confetti === 'undefined') {
        var s = document.createElement('script');
        s.src = 'https://cdnjs.cloudflare.com/ajax/libs/canvas-confetti/1.9.2/confetti.browser.min.js';
        s.onload = function(){ setTimeout(fireConfetti, 600); };
        document.head.appendChild(s);
      } else {
        setTimeout(fireConfetti, 600);
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Register service worker
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function(){
      navigator.serviceWorker.register('/aceAcademy/sw.js').catch(function(){});
    });
  }
})();
