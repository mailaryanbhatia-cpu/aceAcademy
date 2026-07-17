// ── AcerAcademy Pomodoro Study Timer (site-wide floating widget) ──────────
// Self-contained: injects its own CSS + HTML + logic. Just include this
// script anywhere in a page — no per-page markup needed. State persists in
// localStorage so the timer keeps running (and stays in sync) across page
// navigation and across multiple open tabs.
(function(){
  if (window.__AcePomodoroInit) return; // guard against double-injection
  window.__AcePomodoroInit = true;

  var KEY = 'ace_pomodoro_state';
  var SESS_KEY = 'ace_pomodoro_sessions'; // {date:'YYYY-MM-DD', count:N}

  var MODES = {
    work:  { label: 'Focus Time',  short: 'FOCUS',       color: '#059669' },
    short: { label: 'Short Break', short: 'SHORT BREAK', color: '#0891b2' },
    long:  { label: 'Long Break',  short: 'LONG BREAK',  color: '#7c3aed' }
  };

  function defaultSettings(){
    return { focusMin: 25, shortMin: 5, longMin: 15, longEvery: 4, autoAdvance: true };
  }

  function modeSeconds(settings, mode){
    if (mode === 'work') return settings.focusMin * 60;
    if (mode === 'short') return settings.shortMin * 60;
    return settings.longMin * 60;
  }

  function load(){
    var s;
    try { s = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch(e){ s = null; }
    var settings = Object.assign(defaultSettings(), (s && s.settings) || {});
    if (!s) {
      return { mode: 'work', running: false, left: modeSeconds(settings, 'work'), startedAt: null, settings: settings };
    }
    s.settings = settings;
    if (typeof s.left !== 'number') s.left = modeSeconds(settings, s.mode || 'work');
    if (!s.mode) s.mode = 'work';
    return s;
  }

  function save(s){ try { localStorage.setItem(KEY, JSON.stringify(s)); } catch(e){} }

  function todayStr(){ return new Date().toISOString().split('T')[0]; }

  function loadSessions(){
    var d;
    try { d = JSON.parse(localStorage.getItem(SESS_KEY) || 'null'); } catch(e){ d = null; }
    if (!d || d.date !== todayStr()) d = { date: todayStr(), count: 0 };
    return d;
  }

  function bumpSessions(){
    var d = loadSessions();
    d.count++;
    try { localStorage.setItem(SESS_KEY, JSON.stringify(d)); } catch(e){}
    return d.count;
  }

  function getLeft(s){
    if (!s.running) return s.left;
    var elapsed = Math.floor((Date.now() - (s.startedAt || Date.now())) / 1000);
    return Math.max(0, s.left - elapsed);
  }

  function fmt(sec){
    var m = Math.floor(sec / 60), r = sec % 60;
    return String(m).padStart(2, '0') + ':' + String(r).padStart(2, '0');
  }

  // ── Advance to next mode when a cycle completes ─────────────
  function completeCycle(s){
    if (s.mode === 'work') {
      var count = bumpSessions();
      var isLong = (count % s.settings.longEvery === 0);
      s.mode = isLong ? 'long' : 'short';
    } else {
      s.mode = 'work';
    }
    s.left = modeSeconds(s.settings, s.mode);
    if (s.settings.autoAdvance) {
      s.running = true;
      s.startedAt = Date.now();
    } else {
      s.running = false;
      s.startedAt = null;
    }
    if (window.AceSound) { try { AceSound.sessionDone(); } catch(e){} }
    return s;
  }

  // ── DOM injection ────────────────────────────────────────────
  var CSS = ''
    + '#ace-pomo-fab{position:fixed;bottom:20px;left:20px;width:52px;height:52px;border-radius:50%;'
    + 'background:#059669;color:#fff;border:none;font-size:1.3rem;cursor:pointer;z-index:9995;'
    + 'box-shadow:0 4px 18px rgba(0,0,0,.28);display:flex;align-items:center;justify-content:center;'
    + 'transition:transform .15s,box-shadow .15s;font-family:inherit}'
    + '#ace-pomo-fab:hover{transform:scale(1.08)}'
    + '#ace-pomo-fab.running{animation:ace-pomo-pulse 2s ease-in-out infinite}'
    + '@keyframes ace-pomo-pulse{0%,100%{box-shadow:0 0 0 0 rgba(5,150,105,.5)}50%{box-shadow:0 0 0 10px rgba(5,150,105,0)}}'
    + '#ace-pomo-fab .ace-pomo-fab-time{font-size:.62rem;font-weight:800;line-height:1;margin-top:2px;display:none}'
    + '#ace-pomo-fab.running .ace-pomo-fab-icon{display:none}'
    + '#ace-pomo-fab.running .ace-pomo-fab-time{display:block}'
    + '#ace-pomo-panel{position:fixed;bottom:84px;left:20px;width:290px;background:#1a2540;color:#e8edf5;'
    + 'border-radius:18px;box-shadow:0 8px 40px rgba(0,0,0,.35);z-index:9996;overflow:hidden;'
    + 'opacity:0;pointer-events:none;transform:translateY(14px);transition:opacity .2s,transform .2s;'
    + 'font-family:inherit}'
    + '#ace-pomo-panel.open{opacity:1;pointer-events:auto;transform:translateY(0)}'
    + '.ace-pomo-head{padding:13px 16px;display:flex;align-items:center;justify-content:space-between;color:#fff}'
    + '.ace-pomo-head h3{margin:0;font-size:.92rem;font-weight:700}'
    + '.ace-pomo-close{background:rgba(255,255,255,.18);border:none;color:#fff;border-radius:7px;'
    + 'padding:3px 9px;cursor:pointer;font-size:.82rem}'
    + '.ace-pomo-close:hover{background:rgba(255,255,255,.32)}'
    + '.ace-pomo-modes{display:flex;border-bottom:1px solid #2a3a55;background:#141d33}'
    + '.ace-pomo-mode-btn{flex:1;padding:8px 2px;border:none;background:none;cursor:pointer;font-size:.64rem;'
    + 'font-weight:700;color:#7a8fa8;letter-spacing:.03em;transition:all .15s}'
    + '.ace-pomo-mode-btn.active{border-bottom:2px solid currentColor}'
    + '.ace-pomo-circle-wrap{display:flex;justify-content:center;align-items:center;padding:20px 0 10px;position:relative}'
    + '.ace-pomo-svg{transform:rotate(-90deg)}'
    + '.ace-pomo-circle-bg{fill:none;stroke:#2a3a55;stroke-width:8}'
    + '.ace-pomo-circle-fg{fill:none;stroke-width:8;stroke-linecap:round;stroke-dasharray:283;'
    + 'stroke-dashoffset:0;transition:stroke-dashoffset .4s linear,stroke .3s}'
    + '.ace-pomo-center{position:absolute;display:flex;flex-direction:column;align-items:center;justify-content:center}'
    + '.ace-pomo-time{font-size:1.7rem;font-weight:800;letter-spacing:-.02em;color:#fff;font-variant-numeric:tabular-nums}'
    + '.ace-pomo-sub{font-size:.62rem;font-weight:700;color:#7a8fa8;letter-spacing:.05em;text-transform:uppercase;margin-top:2px}'
    + '.ace-pomo-controls{display:flex;justify-content:center;gap:8px;padding:2px 16px 12px}'
    + '.ace-pomo-btn{padding:8px 20px;border-radius:10px;border:none;font-weight:700;font-size:.8rem;cursor:pointer;transition:all .15s}'
    + '.ace-pomo-start{color:#fff}'
    + '.ace-pomo-reset{background:#0b1120;color:#7a8fa8}'
    + '.ace-pomo-reset:hover{background:#22314d}'
    + '.ace-pomo-settings{padding:0 16px 12px;border-top:1px solid #2a3a55;margin-top:2px}'
    + '.ace-pomo-settings-toggle{width:100%;text-align:left;background:none;border:none;color:#7a8fa8;'
    + 'font-size:.68rem;font-weight:700;cursor:pointer;padding:10px 0 4px;letter-spacing:.03em}'
    + '.ace-pomo-settings-body{display:none;padding-top:4px}'
    + '.ace-pomo-settings-body.open{display:block}'
    + '.ace-pomo-set-row{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:7px}'
    + '.ace-pomo-set-row label{font-size:.72rem;color:#aab8cc}'
    + '.ace-pomo-num{width:52px;padding:5px 6px;border:1px solid #2a3a55;border-radius:7px;background:#0b1120;'
    + 'color:#fff;font-size:.78rem;font-weight:700;text-align:center;outline:none}'
    + '.ace-pomo-num:focus{border-color:#059669}'
    + '.ace-pomo-check-row{display:flex;align-items:center;gap:7px;margin-bottom:2px}'
    + '.ace-pomo-check-row label{font-size:.72rem;color:#aab8cc;cursor:pointer}'
    + '.ace-pomo-footer{background:#141d33;border-top:1px solid #2a3a55;padding:9px 16px;'
    + 'display:flex;align-items:center;justify-content:space-between;font-size:.7rem;color:#7a8fa8}'
    + '.ace-pomo-footer strong{color:#059669;font-weight:800}'
    + '@media(max-width:480px){#ace-pomo-panel{left:12px;right:12px;width:auto}#ace-pomo-fab{left:12px}}';

  var HTML = ''
    + '<button id="ace-pomo-fab" title="Study Timer">'
      + '<span class="ace-pomo-fab-icon">⏱</span>'
      + '<span class="ace-pomo-fab-time" id="ace-pomo-fab-time">25:00</span>'
    + '</button>'
    + '<div id="ace-pomo-panel">'
      + '<div class="ace-pomo-head" id="ace-pomo-head"><h3>⏱ Study Timer</h3><button class="ace-pomo-close" id="ace-pomo-close">✕</button></div>'
      + '<div class="ace-pomo-modes">'
        + '<button class="ace-pomo-mode-btn" data-mode="work">FOCUS</button>'
        + '<button class="ace-pomo-mode-btn" data-mode="short">SHORT BREAK</button>'
        + '<button class="ace-pomo-mode-btn" data-mode="long">LONG BREAK</button>'
      + '</div>'
      + '<div class="ace-pomo-circle-wrap">'
        + '<svg class="ace-pomo-svg" width="120" height="120" viewBox="0 0 100 100">'
          + '<circle class="ace-pomo-circle-bg" cx="50" cy="50" r="45"/>'
          + '<circle class="ace-pomo-circle-fg" id="ace-pomo-arc" cx="50" cy="50" r="45"/>'
        + '</svg>'
        + '<div class="ace-pomo-center"><div class="ace-pomo-time" id="ace-pomo-time">25:00</div><div class="ace-pomo-sub" id="ace-pomo-sub">Focus Time</div></div>'
      + '</div>'
      + '<div class="ace-pomo-controls">'
        + '<button class="ace-pomo-btn ace-pomo-start" id="ace-pomo-startbtn">▶ Start</button>'
        + '<button class="ace-pomo-btn ace-pomo-reset" id="ace-pomo-resetbtn">↺ Reset</button>'
      + '</div>'
      + '<div class="ace-pomo-settings">'
        + '<button class="ace-pomo-settings-toggle" id="ace-pomo-settings-toggle">⚙ SETTINGS ▾</button>'
        + '<div class="ace-pomo-settings-body" id="ace-pomo-settings-body">'
          + '<div class="ace-pomo-set-row"><label>Focus (min)</label><input class="ace-pomo-num" id="ace-pomo-focusmin" type="number" min="1" max="99"></div>'
          + '<div class="ace-pomo-set-row"><label>Short break (min)</label><input class="ace-pomo-num" id="ace-pomo-shortmin" type="number" min="1" max="30"></div>'
          + '<div class="ace-pomo-set-row"><label>Long break (min)</label><input class="ace-pomo-num" id="ace-pomo-longmin" type="number" min="1" max="60"></div>'
          + '<div class="ace-pomo-set-row"><label>Long break every</label><input class="ace-pomo-num" id="ace-pomo-longevery" type="number" min="2" max="10"></div>'
          + '<div class="ace-pomo-check-row"><input type="checkbox" id="ace-pomo-autoadvance"><label for="ace-pomo-autoadvance">Auto-start next session</label></div>'
        + '</div>'
      + '</div>'
      + '<div class="ace-pomo-footer"><span>Sessions today: <strong id="ace-pomo-sessions">0</strong></span><span id="ace-pomo-status">Ready</span></div>'
    + '</div>';

  var _iv = null;

  function inject(){
    var st = document.createElement('style');
    st.id = 'ace-pomo-style';
    st.textContent = CSS;
    document.head.appendChild(st);

    var wrap = document.createElement('div');
    wrap.id = 'ace-pomo-root';
    wrap.innerHTML = HTML;
    document.body.appendChild(wrap);

    wireEvents();
    render();
    startPolling();
  }

  function $(id){ return document.getElementById(id); }

  function wireEvents(){
    $('ace-pomo-fab').addEventListener('click', togglePanel);
    $('ace-pomo-close').addEventListener('click', togglePanel);
    $('ace-pomo-startbtn').addEventListener('click', toggleRun);
    $('ace-pomo-resetbtn').addEventListener('click', resetCurrent);
    $('ace-pomo-settings-toggle').addEventListener('click', function(){
      var body = $('ace-pomo-settings-body');
      body.classList.toggle('open');
      this.textContent = body.classList.contains('open') ? '⚙ SETTINGS ▴' : '⚙ SETTINGS ▾';
    });
    document.querySelectorAll('.ace-pomo-mode-btn').forEach(function(btn){
      btn.addEventListener('click', function(){ switchMode(btn.dataset.mode); });
    });
    ['focusmin','shortmin','longmin','longevery'].forEach(function(key){
      $('ace-pomo-' + key).addEventListener('change', updateSettings);
    });
    $('ace-pomo-autoadvance').addEventListener('change', updateSettings);
    document.addEventListener('click', function(e){
      var panel = $('ace-pomo-panel'), fab = $('ace-pomo-fab');
      if (panel && panel.classList.contains('open') && !panel.contains(e.target) && !fab.contains(e.target)) {
        panel.classList.remove('open');
      }
    });
    window.addEventListener('storage', function(e){
      if (e.key === KEY || e.key === SESS_KEY) render();
    });
  }

  function togglePanel(){ $('ace-pomo-panel').classList.toggle('open'); }

  function toggleRun(){
    var s = load();
    if (s.running) {
      s.left = getLeft(s);
      s.running = false;
      s.startedAt = null;
    } else {
      if (s.left <= 0) s.left = modeSeconds(s.settings, s.mode);
      s.running = true;
      s.startedAt = Date.now();
    }
    save(s);
    render();
    startPolling();
  }

  function resetCurrent(){
    var s = load();
    s.running = false;
    s.startedAt = null;
    s.left = modeSeconds(s.settings, s.mode);
    save(s);
    render();
  }

  function switchMode(mode){
    var s = load();
    s.mode = mode;
    s.running = false;
    s.startedAt = null;
    s.left = modeSeconds(s.settings, mode);
    save(s);
    render();
  }

  function updateSettings(){
    var s = load();
    s.settings.focusMin = Math.max(1, parseInt($('ace-pomo-focusmin').value) || 25);
    s.settings.shortMin = Math.max(1, parseInt($('ace-pomo-shortmin').value) || 5);
    s.settings.longMin = Math.max(1, parseInt($('ace-pomo-longmin').value) || 15);
    s.settings.longEvery = Math.max(2, parseInt($('ace-pomo-longevery').value) || 4);
    s.settings.autoAdvance = $('ace-pomo-autoadvance').checked;
    if (!s.running) s.left = modeSeconds(s.settings, s.mode);
    save(s);
    render();
  }

  function render(){
    var root = $('ace-pomo-root');
    if (!root) return;
    var s = load();
    var left = getLeft(s);
    var total = modeSeconds(s.settings, s.mode);
    var info = MODES[s.mode];

    $('ace-pomo-time').textContent = fmt(left);
    $('ace-pomo-sub').textContent = info.label;
    $('ace-pomo-fab-time').textContent = fmt(left);
    $('ace-pomo-head').style.background = info.color;
    $('ace-pomo-arc').style.stroke = info.color;
    $('ace-pomo-fab').style.background = s.running ? info.color : '#059669';

    var pct = total > 0 ? left / total : 0;
    var dash = 283 * (1 - pct);
    $('ace-pomo-arc').style.strokeDashoffset = dash;

    document.querySelectorAll('.ace-pomo-mode-btn').forEach(function(btn){
      var active = btn.dataset.mode === s.mode;
      btn.classList.toggle('active', active);
      btn.style.color = active ? MODES[btn.dataset.mode].color : '';
    });

    $('ace-pomo-startbtn').textContent = s.running ? '⏸ Pause' : '▶ Start';
    $('ace-pomo-startbtn').style.background = info.color;
    $('ace-pomo-status').textContent = s.running ? info.label + '…' : (left === 0 ? 'Done!' : 'Ready');

    $('ace-pomo-focusmin').value = s.settings.focusMin;
    $('ace-pomo-shortmin').value = s.settings.shortMin;
    $('ace-pomo-longmin').value = s.settings.longMin;
    $('ace-pomo-longevery').value = s.settings.longEvery;
    $('ace-pomo-autoadvance').checked = !!s.settings.autoAdvance;

    $('ace-pomo-sessions').textContent = loadSessions().count;

    var fab = $('ace-pomo-fab');
    fab.classList.toggle('running', !!s.running);
  }

  function tick(){
    var s = load();
    var left = getLeft(s);
    if (s.running && left <= 0) {
      s = completeCycle(s);
      save(s);
    }
    render();
    var stillRunning = load().running;
    if (!stillRunning && _iv) { clearInterval(_iv); _iv = null; }
  }

  function startPolling(){
    if (_iv) clearInterval(_iv);
    _iv = setInterval(tick, 1000);
  }

  function boot(){
    inject();
    var s = load();
    if (s.running) startPolling();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
