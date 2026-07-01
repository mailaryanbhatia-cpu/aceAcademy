#!/usr/bin/env python3
import pathlib

TIMER_WIDGET = r"""
<!-- ══ STUDY TIMER WIDGET ══════════════════════════════════════════════ -->
<style>
#timerBtn{position:fixed;bottom:84px;right:24px;width:52px;height:52px;border-radius:50%;
  background:#059669;color:#fff;border:none;font-size:1.3rem;cursor:pointer;
  box-shadow:0 4px 18px rgba(0,0,0,.22);z-index:9997;display:flex;align-items:center;
  justify-content:center;transition:transform .15s,box-shadow .15s;}
#timerBtn:hover{transform:scale(1.1);box-shadow:0 6px 24px rgba(0,0,0,.3);}
#timerBtn.running{animation:timerPulse 2s ease-in-out infinite;}
@keyframes timerPulse{0%,100%{box-shadow:0 0 0 0 rgba(5,150,105,.5);}50%{box-shadow:0 0 0 10px rgba(5,150,105,0);}}
#timerPanel{position:fixed;bottom:148px;right:24px;width:300px;background:#fff;
  border-radius:18px;box-shadow:0 8px 40px rgba(0,0,0,.22);z-index:9998;
  display:flex;flex-direction:column;opacity:0;pointer-events:none;
  transform:translateY(14px);transition:opacity .2s,transform .2s;overflow:hidden;}
#timerPanel.open{opacity:1;pointer-events:auto;transform:translateY(0);}
.tp-head{background:#059669;color:#fff;padding:13px 16px;
  display:flex;align-items:center;justify-content:space-between;}
.tp-head h3{margin:0;font-size:.95rem;font-weight:700;}
.tp-close{background:rgba(255,255,255,.2);border:none;color:#fff;border-radius:7px;
  padding:3px 9px;cursor:pointer;font-size:.85rem;}
.tp-close:hover{background:rgba(255,255,255,.35);}
.tp-mode-row{display:flex;border-bottom:1px solid #e2e8f0;background:#f8fafc;}
.tp-mode-btn{flex:1;padding:8px;border:none;background:none;cursor:pointer;font-size:.72rem;
  font-weight:700;color:#94a3b8;letter-spacing:.04em;transition:all .15s;}
.tp-mode-btn.active{color:#059669;border-bottom:2px solid #059669;background:#fff;}
.tp-circle-wrap{display:flex;justify-content:center;align-items:center;padding:22px 0 14px;}
.tp-svg{transform:rotate(-90deg);}
.tp-circle-bg{fill:none;stroke:#e2e8f0;stroke-width:8;}
.tp-circle-fg{fill:none;stroke:#059669;stroke-width:8;stroke-linecap:round;
  stroke-dasharray:283;stroke-dashoffset:0;transition:stroke-dashoffset .5s linear,stroke .3s;}
.tp-time-text{position:absolute;font-size:1.8rem;font-weight:800;color:#1a1a2e;letter-spacing:-.02em;}
.tp-session-label{position:absolute;top:68px;font-size:.65rem;font-weight:700;
  color:#94a3b8;letter-spacing:.06em;text-transform:uppercase;}
.tp-circle-center{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;}
.tp-controls{display:flex;justify-content:center;gap:10px;padding:0 16px 16px;}
.tp-ctrl-btn{padding:9px 22px;border-radius:10px;border:none;font-weight:700;
  font-size:.85rem;cursor:pointer;transition:all .15s;}
.tp-start{background:#059669;color:#fff;}
.tp-start:hover{background:#047857;}
.tp-reset{background:#f1f5f9;color:#475569;}
.tp-reset:hover{background:#e2e8f0;}
.tp-footer{background:#f8fafc;border-top:1px solid #e2e8f0;padding:10px 16px;
  display:flex;align-items:center;justify-content:space-between;font-size:.75rem;color:#64748b;}
.tp-sessions{font-weight:700;color:#059669;}
.tp-settings-row{display:flex;gap:8px;padding:0 16px 12px;align-items:center;}
.tp-settings-row label{font-size:.72rem;color:#64748b;font-weight:600;}
.tp-num{width:52px;padding:5px 6px;border:1px solid #e2e8f0;border-radius:7px;
  font-size:.82rem;font-weight:700;text-align:center;outline:none;}
.tp-num:focus{border-color:#059669;}
</style>

<button id="timerBtn" onclick="toggleTimer()" title="Study Timer">⏱</button>

<div id="timerPanel">
  <div class="tp-head">
    <h3>⏱ Study Timer</h3>
    <button class="tp-close" onclick="toggleTimer()">✕</button>
  </div>
  <div class="tp-mode-row">
    <button class="tp-mode-btn active" id="tmWork"  onclick="setTimerMode('work')">FOCUS</button>
    <button class="tp-mode-btn"        id="tmShort" onclick="setTimerMode('short')">SHORT BREAK</button>
    <button class="tp-mode-btn"        id="tmLong"  onclick="setTimerMode('long')">LONG BREAK</button>
  </div>
  <div class="tp-circle-wrap">
    <svg class="tp-svg" width="120" height="120" viewBox="0 0 100 100">
      <circle class="tp-circle-bg" cx="50" cy="50" r="45"/>
      <circle class="tp-circle-fg" id="timerArc" cx="50" cy="50" r="45"/>
    </svg>
    <div class="tp-circle-center" style="position:absolute;">
      <div class="tp-time-text" id="timerDisplay">25:00</div>
      <div class="tp-session-label" id="timerModeLabel">Focus Time</div>
    </div>
  </div>
  <div class="tp-settings-row">
    <label>Focus</label>
    <input class="tp-num" id="tpFocusMin" type="number" min="1" max="99" value="25" onchange="updateTimerSettings()"/>
    <label>min &nbsp; Short</label>
    <input class="tp-num" id="tpShortMin" type="number" min="1" max="30" value="5" onchange="updateTimerSettings()"/>
    <label>min</label>
  </div>
  <div class="tp-controls">
    <button class="tp-ctrl-btn tp-start" id="timerStartBtn" onclick="toggleTimerRun()">▶ Start</button>
    <button class="tp-ctrl-btn tp-reset" onclick="resetTimer()">↺ Reset</button>
  </div>
  <div class="tp-footer">
    <span>Sessions today: <span class="tp-sessions" id="tpSessionCount">0</span></span>
    <span id="tpStatusText" style="color:#94a3b8;">Ready</span>
  </div>
</div>

<script>
(function(){
  const MODES = {
    work:  {label:'Focus Time',  color:'#059669'},
    short: {label:'Short Break', color:'#0891b2'},
    long:  {label:'Long Break',  color:'#7c3aed'},
  };
  let mode='work', running=false, remaining=25*60, total=25*60;
  let intervalId=null, sessions=0, longBreakMin=15;

  function getFocusMin(){ return Math.max(1,parseInt(document.getElementById('tpFocusMin')?.value||25)); }
  function getShortMin(){ return Math.max(1,parseInt(document.getElementById('tpShortMin')?.value||5)); }

  function modeSeconds(m){
    if(m==='work')  return getFocusMin()*60;
    if(m==='short') return getShortMin()*60;
    return longBreakMin*60;
  }

  window.updateTimerSettings = function(){
    if(!running){ total=modeSeconds(mode); remaining=total; updateDisplay(); }
  };

  window.setTimerMode = function(m){
    if(running) stopTimer();
    mode=m;
    total=modeSeconds(m);
    remaining=total;
    document.querySelectorAll('.tp-mode-btn').forEach(b=>b.classList.remove('active'));
    const ids={work:'tmWork',short:'tmShort',long:'tmLong'};
    document.getElementById(ids[m])?.classList.add('active');
    document.getElementById('timerArc').style.stroke=MODES[m].color;
    document.getElementById('timerBtn').style.background=MODES[m].color;
    document.getElementById('timerModeLabel').textContent=MODES[m].label;
    updateDisplay();
    document.getElementById('tpStatusText').textContent='Ready';
  };

  window.toggleTimer = function(){
    const p=document.getElementById('timerPanel');
    p.classList.toggle('open');
  };

  window.toggleTimerRun = function(){
    running ? stopTimer() : startTimer();
  };

  function startTimer(){
    if(remaining<=0) resetTimer();
    running=true;
    intervalId=setInterval(tick,1000);
    document.getElementById('timerStartBtn').textContent='⏸ Pause';
    document.getElementById('timerBtn').classList.add('running');
    document.getElementById('tpStatusText').textContent=mode==='work'?'Studying…':'Resting…';
  }

  function stopTimer(){
    running=false;
    clearInterval(intervalId);
    document.getElementById('timerStartBtn').textContent='▶ Start';
    document.getElementById('timerBtn').classList.remove('running');
    document.getElementById('tpStatusText').textContent='Paused';
  }

  window.resetTimer = function(){
    stopTimer();
    remaining=total=modeSeconds(mode);
    updateDisplay();
    document.getElementById('tpStatusText').textContent='Ready';
  };

  function tick(){
    remaining--;
    if(remaining<=0){
      remaining=0;
      updateDisplay();
      stopTimer();
      playBell();
      if(mode==='work'){
        sessions++;
        document.getElementById('tpSessionCount').textContent=sessions;
        // auto-switch to break
        const nextMode = sessions%4===0?'long':'short';
        setTimeout(()=>{ setTimerMode(nextMode); playBell(); },500);
        document.getElementById('tpStatusText').textContent='Session done! 🎉';
      } else {
        setTimeout(()=>{ setTimerMode('work'); },500);
        document.getElementById('tpStatusText').textContent='Break over!';
      }
      // open panel so user sees the notification
      document.getElementById('timerPanel').classList.add('open');
      return;
    }
    updateDisplay();
  }

  function updateDisplay(){
    const m=Math.floor(remaining/60), s=remaining%60;
    document.getElementById('timerDisplay').textContent =
      String(m).padStart(2,'0')+':'+String(s).padStart(2,'0');
    const arc=document.getElementById('timerArc');
    if(arc){
      const pct = total>0 ? remaining/total : 1;
      arc.style.strokeDashoffset = String(Math.round(283*(1-pct)));
    }
    // Update page title while running
    if(running){
      document.title='⏱ '+String(m).padStart(2,'0')+':'+String(s).padStart(2,'0')+' — aceAcademy';
    } else {
      document.title = document.title.replace(/^⏱.*?—\s*/,'');
    }
  }

  function playBell(){
    try{
      const ctx=new(window.AudioContext||window.webkitAudioContext)();
      [0,0.15,0.3].forEach((delay,i)=>{
        const osc=ctx.createOscillator(), gain=ctx.createGain();
        osc.connect(gain); gain.connect(ctx.destination);
        osc.frequency.value=i===0?880:i===1?1046:1318;
        gain.gain.setValueAtTime(0.3,ctx.currentTime+delay);
        gain.gain.exponentialRampToValueAtTime(0.001,ctx.currentTime+delay+0.6);
        osc.start(ctx.currentTime+delay);
        osc.stop(ctx.currentTime+delay+0.7);
      });
    }catch(e){}
  }

  // Close on outside click (avoid conflicting with notes panel)
  document.addEventListener('click',function(e){
    const p=document.getElementById('timerPanel');
    const b=document.getElementById('timerBtn');
    if(p&&p.classList.contains('open')&&!p.contains(e.target)&&!b.contains(e.target)){
      p.classList.remove('open');
    }
  });

  // Shift notes button up so they don't overlap
  const nb=document.getElementById('notesBtn');
  if(nb) nb.style.bottom='84px';
  const tp=document.getElementById('timerBtn');
  if(tp) tp.style.bottom='24px';
})();
</script>
<!-- ══ END STUDY TIMER WIDGET ══════════════════════════════════════════ -->
"""

pages = ['index.html','curriculum.html','worksheets.html',
         'tests.html','tutor.html','language.html','notebook.html','progress.html','flashcards.html']
base = pathlib.Path('/sessions/admiring-stoic-pascal/mnt/outputs')

for name in pages:
    p = base / name
    if not p.exists():
        print(f'SKIP: {name}'); continue
    html = p.read_text(encoding='utf-8')
    if '<!-- ══ STUDY TIMER WIDGET' in html:
        print(f'Already has timer: {name}'); continue
    html = html.replace('</body>', TIMER_WIDGET + '\n</body>', 1)
    p.write_text(html, encoding='utf-8')
    print(f'Injected timer: {name}')

print('Done.')
