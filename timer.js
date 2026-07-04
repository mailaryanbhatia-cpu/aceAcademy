// ── aceAcademy Persistent Timer ──────────────────────────────
(function(){
  const KEY = 'ace_timer_state';
  let _iv = null;

  function save(s){ try{ localStorage.setItem(KEY,JSON.stringify(s)); }catch(e){} }
  function load(){ try{ return JSON.parse(localStorage.getItem(KEY)||'null'); }catch(e){ return null; } }

  function getLeft(s){
    if(!s) return 0;
    if(!s.running) return s.left||0;
    return Math.max(0, (s.left||0) - Math.floor((Date.now()-(s.startedAt||Date.now()))/1000));
  }

  function fmt(secs){
    const m=Math.floor(secs/60), s=secs%60;
    return String(m).padStart(2,'0')+':'+String(s).padStart(2,'0');
  }

  // ── Badge pill (visible on every page when timer is running) ──
  function ensureBadge(){
    if(document.getElementById('ace-timer-badge')) return;
    const b = document.createElement('div');
    b.id = 'ace-timer-badge';
    b.title = 'Focus timer running — click to go to home';
    b.style.cssText = 'position:fixed;bottom:18px;left:18px;z-index:9990;'+
      'background:linear-gradient(135deg,#ef4444,#f97316);color:#fff;'+
      'font-size:.82rem;font-weight:800;padding:8px 14px;border-radius:999px;'+
      'box-shadow:0 4px 18px rgba(239,68,68,.5);cursor:pointer;'+
      'display:flex;align-items:center;gap:6px;user-select:none;'+
      'animation:tp-pulse 2s infinite';
    b.innerHTML = '⏱ <span id="ace-timer-badge-txt">--:--</span>';
    b.onclick = function(){ window.location.href = 'index.html'; };
    // pulse animation
    if(!document.getElementById('ace-timer-badge-style')){
      const st=document.createElement('style');
      st.id='ace-timer-badge-style';
      st.textContent='@keyframes tp-pulse{0%,100%{opacity:1}50%{opacity:.75}}';
      document.head.appendChild(st);
    }
    document.body.appendChild(b);
  }

  function removeBadge(){
    const b=document.getElementById('ace-timer-badge');
    if(b) b.remove();
  }

  function tick(){
    const s = load();
    const left = getLeft(s);

    // Update badge
    if(s && s.running && left > 0){
      ensureBadge();
      const t=document.getElementById('ace-timer-badge-txt');
      if(t) t.textContent = fmt(left);
    } else {
      removeBadge();
    }

    // Update index.html timer panel display if on that page
    const disp = document.getElementById('timerDisplay');
    if(disp) disp.textContent = fmt(left);
    const fab = document.getElementById('timerFab');
    if(fab){
      const lbl=fab.querySelector('.dock-label');
      if(lbl) lbl.textContent = (s&&s.running) ? fmt(left) : 'Timer';
      if(s&&s.running) fab.classList.add('running');
      else fab.classList.remove('running');
    }

    // Timer done
    if(s && s.running && left <= 0){
      s.running=false; s.left=0; save(s);
      removeBadge();
      const lb=document.getElementById('timerLabel');     if(lb)  lb.textContent="⏰ Time's up!";
      const sb=document.getElementById('timerStartBtn');  if(sb)  sb.textContent='Start';
      if(fab) fab.classList.remove('running');
      if(window.AceSound) AceSound.sessionDone();
      clearInterval(_iv); _iv=null;
    }
  }

  function startPolling(){
    if(_iv) clearInterval(_iv);
    _iv = setInterval(tick, 500);
    tick();
  }

  // ── Public API (used by index.html timer panel) ──
  window.AceTimer = {
    load, save, getLeft, fmt,
    start: function(){
      let s = load() || {total:600,left:600,running:false,startedAt:null};
      const left = getLeft(s);
      if(s.running){
        clearInterval(_iv); _iv=null;
        s.running=false; s.left=left; s.startedAt=null; save(s);
        removeBadge();
        const sb=document.getElementById('timerStartBtn'); if(sb) sb.textContent='Resume';
        const lb=document.getElementById('timerLabel');    if(lb) lb.textContent='Paused';
        const fab=document.getElementById('timerFab');     if(fab) fab.classList.remove('running');
      } else {
        s.running=true; s.startedAt=Date.now(); s.left=left; save(s);
        const sb=document.getElementById('timerStartBtn'); if(sb) sb.textContent='Pause';
        const lb=document.getElementById('timerLabel');    if(lb) lb.textContent='Focus!';
        const fab=document.getElementById('timerFab');     if(fab) fab.classList.add('running');
        startPolling();
      }
    },
    setPreset: function(mins, btn){
      clearInterval(_iv); _iv=null;
      const s={total:mins*60,left:mins*60,running:false,startedAt:null};
      save(s);
      removeBadge();
      const disp=document.getElementById('timerDisplay'); if(disp) disp.textContent=fmt(mins*60);
      const fab=document.getElementById('timerFab');     if(fab){fab.classList.remove('running');const lbl=fab.querySelector('.dock-label');if(lbl)lbl.textContent='Timer';}
      const sb=document.getElementById('timerStartBtn'); if(sb) sb.textContent='Start';
      const lb=document.getElementById('timerLabel');    if(lb) lb.textContent='Set your focus time';
      document.querySelectorAll('.timer-preset').forEach(b=>b.classList.remove('active'));
      if(btn) btn.classList.add('active');
    },
    reset: function(){
      clearInterval(_iv); _iv=null;
      const s=load()||{total:600};
      s.running=false; s.left=s.total||600; s.startedAt=null; save(s);
      removeBadge();
      const disp=document.getElementById('timerDisplay'); if(disp) disp.textContent=fmt(s.left);
      const fab=document.getElementById('timerFab');     if(fab){fab.classList.remove('running');const lbl=fab.querySelector('.dock-label');if(lbl)lbl.textContent='Timer';}
      const sb=document.getElementById('timerStartBtn'); if(sb) sb.textContent='Start';
      const lb=document.getElementById('timerLabel');    if(lb) lb.textContent='Set your focus time';
    }
  };

  // Boot: show badge on any page; on index.html also resume the circular timer
  document.addEventListener('DOMContentLoaded', function(){
    const s = load();
    if(s && s.running){
      startPolling();
      // If we're on index.html, resume the circular timer display
      resumeCircularTimer(s);
    } else {
      tick();
    }
  });

  function resumeCircularTimer(s){
    // Wait for the circular timer's JS to initialise, then patch remaining
    setTimeout(function(){
      const elapsed = Math.floor((Date.now() - (s.startedAt||Date.now())) / 1000);
      const left = Math.max(0, (s.left||0) - elapsed);
      // The circular timer uses `remaining` inside its closure; we can't reach it directly.
      // Instead, if the timer is still running and the circular panel exists,
      // auto-click Start to reconnect.
      const startBtn = document.getElementById('timerStartBtn');
      const statusEl = document.getElementById('tpStatusText');
      if(startBtn && statusEl && s.running && left > 0){
        // Circular timer starts paused on reload — resume it
        if(startBtn.textContent.trim() === '▶ Start'){
          startBtn.click();
        }
      }
    }, 400);
  }
})();
