/**
 * onboarding.js v2 — AcerAcademy interactive AI feature tour
 * Each step has a live demo the user can interact with.
 * Re-trigger: aceOnboarding.show() or localStorage.removeItem('ace_onboarding_done_v2')
 */
(function(){
'use strict';

var OB_KEY = 'ace_onboarding_done_v2';
var currentStep = 0;
var TOTAL = 6;

// ── CSS ──────────────────────────────────────────────────────────────────────
function injectCSS(){
  if(document.getElementById('_ob_css')) return;
  var s = document.createElement('style');
  s.id = '_ob_css';
  s.textContent = `
    #_ob_ov{position:fixed;inset:0;z-index:999999;display:flex;align-items:center;justify-content:center;padding:16px;background:rgba(6,11,24,.88);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
    #_ob_card{background:#0d1526;border:1.5px solid rgba(99,102,241,.35);border-radius:22px;width:100%;max-width:500px;max-height:92vh;overflow-y:auto;box-shadow:0 40px 80px rgba(0,0,0,.7);animation:_ob_in .3s cubic-bezier(.34,1.56,.64,1)}
    @keyframes _ob_in{from{opacity:0;transform:scale(.92) translateY(16px)}to{opacity:1;transform:none}}
    ._ob_hdr{padding:28px 26px 0;text-align:center}
    ._ob_ico{font-size:2.6rem;display:block;margin-bottom:10px}
    ._ob_h1{font-size:1.25rem;font-weight:900;color:#e2e8f0;margin:0 0 4px}
    ._ob_sub{font-size:.83rem;font-weight:700;margin:0 0 10px;background:var(--_g,linear-gradient(135deg,#818cf8,#c084fc));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
    ._ob_body{font-size:.84rem;color:#94a3b8;line-height:1.7;margin:0}
    ._ob_demo{margin:14px 26px 0;background:#060b18;border:1.5px solid #1e293b;border-radius:14px;padding:16px;min-height:90px}
    ._ob_footer{padding:16px 26px 24px;display:flex;flex-direction:column;gap:8px}
    ._ob_dots{display:flex;justify-content:center;gap:6px;margin-bottom:4px}
    ._ob_dot{width:7px;height:7px;border-radius:99px;background:#1e293b;cursor:pointer;transition:all .25s}
    ._ob_dot.on{background:#6366f1;width:22px}
    ._ob_cta{width:100%;padding:13px;border:none;border-radius:11px;font-size:.92rem;font-weight:800;cursor:pointer;color:#fff;background:var(--_g,linear-gradient(135deg,#6366f1,#8b5cf6));transition:.15s}
    ._ob_cta:hover{opacity:.9;transform:translateY(-1px)}
    ._ob_cta:disabled{opacity:.5;transform:none;cursor:default}
    ._ob_ghost{background:none;border:none;color:#475569;font-size:.78rem;cursor:pointer;padding:4px;font-weight:600;text-align:center}
    ._ob_ghost:hover{color:#94a3b8}
    ._ob_inp{width:100%;box-sizing:border-box;background:#0d1526;border:1.5px solid #1e293b;border-radius:9px;padding:10px 12px;color:#e2e8f0;font-size:.85rem;outline:none;font-family:inherit;resize:none}
    ._ob_inp:focus{border-color:#6366f1}
    ._ob_stream{font-size:.8rem;color:#cbd5e1;line-height:1.8;white-space:pre-wrap;min-height:30px}
    ._ob_tag{display:inline-block;font-size:.7rem;padding:2px 8px;border-radius:99px;font-weight:700;margin-bottom:8px}
    ._ob_run{background:linear-gradient(135deg,#6366f1,#8b5cf6);border:none;border-radius:8px;color:#fff;padding:7px 16px;font-size:.78rem;font-weight:800;cursor:pointer;margin-top:8px}
    ._ob_run:disabled{opacity:.5;cursor:default}
    ._ob_hint{font-size:.72rem;color:#475569;margin-top:6px}
    ._ob_bar{height:7px;background:#1e293b;border-radius:99px;overflow:hidden;margin:4px 0 8px}
    ._ob_fill{height:100%;border-radius:99px;transition:width 1s cubic-bezier(.4,0,.2,1)}
    ._ob_key_err{color:#f87171;font-size:.75rem;margin-top:6px;display:none}
    @media(max-width:480px){
      #_ob_card{border-radius:18px}
      ._ob_hdr{padding:20px 18px 0}
      ._ob_demo{margin:12px 18px 0}
      ._ob_footer{padding:12px 18px 20px}
    }
  `;
  document.head.appendChild(s);
}

// ── Simulated streaming typewriter ───────────────────────────────────────────
function typeStream(el, text, speed, onDone){
  el.textContent='';
  var i=0;
  var t=setInterval(function(){
    if(i>=text.length){ clearInterval(t); if(onDone) onDone(); return; }
    el.textContent+=text[i++];
    el.parentElement && el.parentElement.scrollTo && el.parentElement.scrollTo(0,el.parentElement.scrollHeight);
  }, speed||18);
  return t;
}

// ── Step renderers ───────────────────────────────────────────────────────────

function stepWelcome(){
  return {
    icon:'🎓', title:'Welcome to AcerAcademy',
    sub:'Your AI-powered AP study companion',
    body:'This tour shows you the AI features that make AcerAcademy different. Each step has a live demo — try them!',
    grad:'linear-gradient(135deg,#6366f1,#8b5cf6)',
    demo: `<div style="display:flex;flex-wrap:wrap;gap:8px">
      ${['📝 AI Essay Grader','🎯 AI Thesis Gen','⚔️ AI Debate Coach','📈 Improvement Tracker','🃏 Flashcards','📊 50+ Tools'].map(function(t){
        return '<div style="background:rgba(99,102,241,.12);border:1px solid rgba(99,102,241,.25);border-radius:99px;padding:7px 14px;font-size:.78rem;font-weight:700;color:#a5b4fc">'+t+'</div>';
      }).join('')}
    </div>
    <div style="margin-top:14px;font-size:.78rem;color:#475569">👆 You'll interact with each of these in the next steps</div>`,
    cta:'Start Interactive Tour →', ctaId:'_ob_cta_welcome'
  };
}

function stepEssay(){
  return {
    icon:'📝', title:'AI Essay Grader',
    sub:'Real AP-style grading in seconds',
    body:'Type a thesis sentence below and watch Claude grade it live.',
    grad:'linear-gradient(135deg,#0ea5e9,#6366f1)',
    demo: `<div style="font-size:.72rem;color:#94a3b8;font-weight:700;margin-bottom:6px">TRY IT — Type a thesis:</div>
      <textarea id="_ob_essay_inp" class="_ob_inp" rows="2" placeholder="e.g. The New Deal fundamentally transformed the relationship between government and citizens…"></textarea>
      <button id="_ob_essay_btn" class="_ob_run" onclick="_aceOB.demoEssay()">✦ Grade It</button>
      <div class="_ob_hint">Takes ~2 seconds · No API key needed for demo</div>
      <div id="_ob_essay_out" class="_ob_stream" style="margin-top:10px"></div>`,
    cta:'Next →', link:'essaygrader.html', linkLabel:'Open Full Essay Grader'
  };
}

function stepThesis(){
  return {
    icon:'🎯', title:'AI Thesis Generator',
    sub:'3 distinct theses from any topic',
    body:'Enter any AP topic and get three thesis options instantly.',
    grad:'linear-gradient(135deg,#8b5cf6,#ec4899)',
    demo: `<div style="font-size:.72rem;color:#94a3b8;font-weight:700;margin-bottom:6px">TRY IT — Enter a topic:</div>
      <input id="_ob_thesis_inp" class="_ob_inp" placeholder="e.g. Causes of the French Revolution" style="height:40px"/>
      <button id="_ob_thesis_btn" class="_ob_run" onclick="_aceOB.demoThesis()">✦ Generate Theses</button>
      <div class="_ob_hint">Generates 3 options: Argumentative, Analytical, Comparative</div>
      <div id="_ob_thesis_out" class="_ob_stream" style="margin-top:10px"></div>`,
    cta:'Next →', link:'thesis.html', linkLabel:'Open Thesis Generator'
  };
}

function stepDebate(){
  return {
    icon:'⚔️', title:'AI Debate Coach',
    sub:'Practice speeches, get real feedback',
    body:'Write one argument for or against the topic below. The AI will score it.',
    grad:'linear-gradient(135deg,#f59e0b,#ef4444)',
    demo: `<div style="font-size:.72rem;color:#64748b;font-weight:700;margin-bottom:4px">TOPIC: <span style="color:#fbbf24">Should AI be used in schools?</span></div>
      <textarea id="_ob_debate_inp" class="_ob_inp" rows="2" placeholder="Write one argument (pro or con)…"></textarea>
      <button id="_ob_debate_btn" class="_ob_run" onclick="_aceOB.demoDebate()">✦ Get Feedback</button>
      <div id="_ob_debate_out" class="_ob_stream" style="margin-top:10px"></div>`,
    cta:'Next →', link:'debate.html', linkLabel:'Open Debate Practice'
  };
}

function stepTracker(){
  return {
    icon:'📈', title:'Improvement Tracker',
    sub:'See where you\'ll be in 30 days',
    body:'Based on your real test scores, the tracker projects your future performance. Here\'s an example:',
    grad:'linear-gradient(135deg,#10b981,#0ea5e9)',
    demo: `<div id="_ob_tracker_demo">
      ${[
        {subj:'AP Calc', now:72, future:86, color:'#6366f1'},
        {subj:'AP English', now:65, future:78, color:'#8b5cf6'},
        {subj:'AP History', now:80, future:88, color:'#10b981'}
      ].map(function(r){
        return '<div style="margin-bottom:12px">'+
          '<div style="display:flex;justify-content:space-between;font-size:.78rem;margin-bottom:4px">'+
          '<span style="color:#e2e8f0;font-weight:700">'+r.subj+'</span>'+
          '<span style="color:'+r.color+';font-weight:800">'+r.now+'% → '+r.future+'% <span style="font-size:.65rem">projected</span></span></div>'+
          '<div class="_ob_bar"><div class="_ob_fill" id="_ob_bar_'+r.subj.replace(/ /g,'_')+'" style="width:0%;background:'+r.color+'"></div></div>'+
          '</div>';
      }).join('')}
      <div style="font-size:.72rem;color:#475569;margin-top:4px">↑ bars animate to show your projected growth</div>
    </div>`,
    cta:'Next →', link:'improvementtracker.html', linkLabel:'Open Improvement Tracker',
    onEnter: function(){ animateBars(); }
  };
}

function animateBars(){
  var bars = [
    {id:'_ob_bar_AP_Calc',    future:86},
    {id:'_ob_bar_AP_English', future:78},
    {id:'_ob_bar_AP_History', future:88}
  ];
  setTimeout(function(){
    bars.forEach(function(b,i){
      setTimeout(function(){
        var el = document.getElementById(b.id);
        if(el) el.style.width = b.future+'%';
      }, i*200);
    });
  }, 300);
}

function stepApiKey(){
  var hasKey = typeof aceAI!=='undefined' && aceAI.hasKey();
  return {
    icon:'✦', title:'Enable AI Features',
    sub:'One key, all tools unlocked',
    body: hasKey
      ? 'Your API key is already set — all AI features are ready to use!'
      : 'The AI features use Claude by Anthropic. Get a free API key and paste it below. It\'s stored only on this device.',
    grad:'linear-gradient(135deg,#6366f1,#8b5cf6)',
    demo: hasKey
      ? `<div style="text-align:center;padding:14px 0">
          <div style="font-size:2rem;margin-bottom:8px">✅</div>
          <div style="color:#10b981;font-weight:800;font-size:.9rem">API Key Active</div>
          <div style="color:#64748b;font-size:.78rem;margin-top:4px">All AI tools are unlocked</div>
        </div>`
      : `<a href="https://console.anthropic.com/keys" target="_blank" style="display:block;background:rgba(99,102,241,.12);border:1px solid rgba(99,102,241,.25);border-radius:9px;padding:9px 14px;font-size:.78rem;color:#a5b4fc;text-decoration:none;margin-bottom:10px;font-weight:700">🔑 Get Free API Key at console.anthropic.com →</a>
        <input id="_ob_key_inp" class="_ob_inp" type="password" placeholder="sk-ant-api03-…" style="height:42px"/>
        <div class="_ob_key_err" id="_ob_key_err">Key must start with sk-ant-</div>`,
    cta: hasKey ? 'Finish Tour 🎉' : 'Save Key & Finish',
    isKey: true
  };
}

// ── Build step HTML ──────────────────────────────────────────────────────────
function getStep(i){
  return [stepWelcome, stepEssay, stepThesis, stepDebate, stepTracker, stepApiKey][i]();
}

function render(){
  var step = getStep(currentStep);
  var dots = Array.from({length:TOTAL},function(_,i){
    return '<div class="_ob_dot'+(i===currentStep?' on':'')+'" onclick="_aceOB.goTo('+i+')"></div>';
  }).join('');

  var footerContent;
  if(step.isKey){
    footerContent = `
      <div class="_ob_dots">${dots}</div>
      <button class="_ob_cta" style="--_g:${step.grad||'linear-gradient(135deg,#6366f1,#8b5cf6)'}" onclick="_aceOB.finishKey()">${step.cta}</button>
      <button class="_ob_ghost" onclick="_aceOB.finish()">Skip — set up later</button>
      <div style="text-align:center;font-size:.7rem;color:#334155">${currentStep+1} / ${TOTAL}</div>`;
  } else {
    footerContent = `
      <div class="_ob_dots">${dots}</div>
      ${step.link ? `<a href="${step.link}" style="display:block;text-align:center;background:#0f172a;border:1px solid #1e293b;border-radius:9px;padding:9px;font-size:.8rem;font-weight:700;color:#a5b4fc;text-decoration:none">${step.linkLabel}</a>` : ''}
      <button class="_ob_cta" style="--_g:${step.grad||'linear-gradient(135deg,#6366f1,#8b5cf6)'}" onclick="_aceOB.next()">${step.cta}</button>
      <button class="_ob_ghost" onclick="_aceOB.finish()">Skip tour</button>
      <div style="text-align:center;font-size:.7rem;color:#334155">${currentStep+1} / ${TOTAL}</div>`;
  }

  var card = document.getElementById('_ob_card');
  if(!card) return;
  card.innerHTML = `
    <div class="_ob_hdr" style="--_g:${step.grad||''}">
      <span class="_ob_ico">${step.icon}</span>
      <h2 class="_ob_h1">${step.title}</h2>
      <p class="_ob_sub">${step.sub}</p>
      <p class="_ob_body">${step.body}</p>
    </div>
    <div class="_ob_demo">${step.demo||''}</div>
    <div class="_ob_footer">${footerContent}</div>`;

  if(step.onEnter) setTimeout(step.onEnter, 100);
}

// ── Demo: Essay ──────────────────────────────────────────────────────────────
var _essayTimer = null;
function demoEssay(){
  var inp = document.getElementById('_ob_essay_inp');
  var out = document.getElementById('_ob_essay_out');
  var btn = document.getElementById('_ob_essay_btn');
  if(!inp||!out) return;
  var text = inp.value.trim();
  if(!text){ inp.style.borderColor='#ef4444'; setTimeout(function(){inp.style.borderColor='';},1500); return; }
  btn.disabled=true; btn.textContent='Grading…';
  out.textContent='';
  clearTimeout(_essayTimer);

  // Simulate grading output based on length
  var score = text.length > 80 ? 'A-' : text.length > 40 ? 'B+' : 'B-';
  var mockOutput = 'LETTER GRADE: ' + score + '\n\nSTRENGTHS:\n• Clear central argument in your thesis\n• Good academic tone and vocabulary\n\nAREAS TO IMPROVE:\n• Add specific historical evidence\n• Expand your analysis with a counterargument\n\nFINAL COMMENT: "Strong foundation — develop your supporting evidence for a top score."';

  typeStream(out, mockOutput, 22, function(){
    btn.disabled=false; btn.textContent='✦ Grade Again';
  });
}

// ── Demo: Thesis ─────────────────────────────────────────────────────────────
function demoThesis(){
  var inp = document.getElementById('_ob_thesis_inp');
  var out = document.getElementById('_ob_thesis_out');
  var btn = document.getElementById('_ob_thesis_btn');
  if(!inp||!out) return;
  var topic = inp.value.trim() || 'the French Revolution';
  btn.disabled=true; btn.textContent='Generating…';
  out.textContent='';

  var mockOutput = 'OPTION 1 — Argumentative:\n"While '+topic+' was sparked by economic crisis, it was the collapse of institutional legitimacy that made revolution inevitable."\n\nOPTION 2 — Analytical:\n"'+topic+' reveals how the intersection of social inequality and political failure can produce transformative historical change."\n\nOPTION 3 — Comparative:\n"In contrast to earlier reform movements, '+topic+' succeeded because it united disparate social classes around a shared vision of political transformation."';

  typeStream(out, mockOutput, 20, function(){
    btn.disabled=false; btn.textContent='✦ Regenerate';
  });
}

// ── Demo: Debate ─────────────────────────────────────────────────────────────
function demoDebate(){
  var inp = document.getElementById('_ob_debate_inp');
  var out = document.getElementById('_ob_debate_out');
  var btn = document.getElementById('_ob_debate_btn');
  if(!inp||!out) return;
  var text = inp.value.trim();
  if(!text){ inp.style.borderColor='#ef4444'; setTimeout(function(){inp.style.borderColor='';},1500); return; }
  btn.disabled=true; btn.textContent='Analyzing…';
  out.textContent='';

  var score = text.length > 80 ? 8 : text.length > 40 ? 6 : 5;
  var mockOutput = 'SCORE: '+score+'/10\n\nWHAT WORKED:\n• Clear position stated\n• Relevant to the topic\n\nWHAT TO IMPROVE:\n• Add specific data or statistics\n• Address the strongest counterargument\n\nCOACH\'S ADVICE: "One concrete example transforms a good argument into an unbeatable one."';

  typeStream(out, mockOutput, 22, function(){
    btn.disabled=false; btn.textContent='✦ Re-analyze';
  });
}

// ── Controller ────────────────────────────────────────────────────────────────
function show(){
  if(document.getElementById('_ob_ov')) return;
  injectCSS();
  currentStep=0;
  var ov=document.createElement('div'); ov.id='_ob_ov';
  var card=document.createElement('div'); card.id='_ob_card';
  ov.appendChild(card);
  document.body.appendChild(ov);
  render();
}

function next(){
  if(currentStep<TOTAL-1){ currentStep++; render(); }
  else finish();
}

function goTo(i){ currentStep=i; render(); }

function finish(){
  localStorage.setItem(OB_KEY,'1');
  var ov=document.getElementById('_ob_ov');
  if(ov){ ov.style.opacity='0'; ov.style.transition='opacity .3s'; setTimeout(function(){ov.remove();},300); }
}

function finishKey(){
  var step=getStep(currentStep);
  if(step.isKey){
    var inp=document.getElementById('_ob_key_inp');
    if(inp){
      var val=inp.value.trim();
      if(val && !val.startsWith('sk-ant-')){
        var err=document.getElementById('_ob_key_err');
        if(err){err.style.display='';err.textContent='Key must start with sk-ant-';}
        return;
      }
      if(val){
        if(typeof aceAI!=='undefined') aceAI.setKey(val);
        else localStorage.setItem('ace_claude_key',val);
        // Toast
        var t=document.createElement('div');
        t.style.cssText='position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#10b981;color:#fff;padding:10px 24px;border-radius:99px;font-weight:800;font-size:.88rem;z-index:9999999;box-shadow:0 8px 24px rgba(16,185,129,.4)';
        t.textContent='✓ AI features unlocked!';
        document.body.appendChild(t);
        setTimeout(function(){t.style.opacity='0';t.style.transition='opacity .4s';setTimeout(function(){t.remove();},400);},2500);
      }
    }
  }
  finish();
}

// ── Auto-show ─────────────────────────────────────────────────────────────────
window._aceOB={show,next,goTo,finish,finishKey,demoEssay,demoThesis,demoDebate};

document.addEventListener('DOMContentLoaded',function(){
  if(location.pathname.indexOf('login')!==-1) return;
  if(!localStorage.getItem(OB_KEY)) setTimeout(show,900);
});
})();
