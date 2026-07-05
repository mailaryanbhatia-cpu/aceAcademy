/**
 * onboarding.js — aceAcademy AI feature tour
 * Shows once on first visit. Re-trigger: aceOnboarding.show()
 * Add to any page: <script src="/aceAcademy/onboarding.js"></script>
 */
(function(){
'use strict';

var OB_KEY     = 'ace_onboarding_done_v2';
var OB_CSS_KEY = '_ace_ob_style';

var STEPS = [
  {
    id: 'welcome',
    icon: '🎓',
    title: 'Welcome to aceAcademy',
    subtitle: 'Your AI-powered AP study companion',
    body: 'In the next 60 seconds, we\'ll show you the features that set aceAcademy apart from every other study app. Let\'s go.',
    cta: 'Start Tour →',
    color: 'linear-gradient(135deg,#6366f1,#8b5cf6)',
    visual: `<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:20px 0">
      ${['📝 Essay AI','🎯 Thesis AI','⚔️ Debate AI','📈 Improvement','🃏 Flashcards','📊 50+ Tools'].map(t=>
        `<div style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:99px;padding:8px 16px;font-size:.82rem;font-weight:700;color:#fff">${t}</div>`
      ).join('')}
    </div>`
  },
  {
    id: 'essaygrader',
    icon: '📝',
    title: 'AI Essay Grader',
    subtitle: 'Get a real AP-style grade in seconds',
    body: 'Paste any essay and Claude AI gives you a letter grade, rubric breakdown, specific strengths, and exactly what to fix — just like a real AP teacher.',
    cta: 'Next →',
    color: 'linear-gradient(135deg,#0ea5e9,#6366f1)',
    visual: `<div style="background:rgba(0,0,0,.3);border-radius:12px;padding:16px;margin:16px 0;text-align:left;font-size:.8rem">
      <div style="color:#94a3b8;margin-bottom:8px;font-size:.72rem;text-transform:uppercase;font-weight:700">AI Output Preview</div>
      <div style="color:#fbbf24;font-weight:900;font-size:1.1rem;margin-bottom:6px">LETTER GRADE: B+</div>
      <div style="color:#34d399;margin-bottom:4px">✓ Strong thesis with clear argument</div>
      <div style="color:#34d399;margin-bottom:4px">✓ Good use of historical evidence</div>
      <div style="color:#f87171;margin-bottom:4px">✗ Conclusion lacks synthesis</div>
      <div style="color:#60a5fa;margin-top:8px;font-style:italic">"Your evidence selection is strong — focus on connecting each piece back to your central claim."</div>
    </div>`,
    link: 'essaygrader.html',
    linkLabel: 'Try Essay Grader'
  },
  {
    id: 'thesis',
    icon: '🎯',
    title: 'AI Thesis Generator',
    subtitle: '3 thesis options, instantly',
    body: 'Enter your topic and Claude generates 3 distinct, AP-quality thesis statements — argumentative, analytical, and comparative — each with a different angle.',
    cta: 'Next →',
    color: 'linear-gradient(135deg,#8b5cf6,#ec4899)',
    visual: `<div style="background:rgba(0,0,0,.3);border-radius:12px;padding:16px;margin:16px 0;text-align:left;font-size:.8rem">
      <div style="color:#94a3b8;margin-bottom:10px;font-size:.72rem;text-transform:uppercase;font-weight:700">Topic: "Causes of WWI"</div>
      <div style="margin-bottom:10px"><div style="color:#c084fc;font-weight:700;font-size:.75rem;margin-bottom:3px">OPTION 1 — Argumentative</div><div style="color:#e2e8f0;line-height:1.5">"While nationalism ignited WWI, it was the alliance system that transformed a regional conflict into a global catastrophe."</div></div>
      <div style="margin-bottom:10px"><div style="color:#f472b6;font-weight:700;font-size:.75rem;margin-bottom:3px">OPTION 2 — Analytical</div><div style="color:#e2e8f0;line-height:1.5">"The interplay of imperialism, militarism, and miscalculation created a powder keg that only needed a single spark."</div></div>
    </div>`,
    link: 'thesis.html',
    linkLabel: 'Try Thesis Generator'
  },
  {
    id: 'debate',
    icon: '⚔️',
    title: 'AI Debate Coach',
    subtitle: 'Practice and get real feedback',
    body: 'Pick a topic, choose your side, and debate. The AI suggests arguments, anticipates counterarguments, and grades your actual speech with specific feedback.',
    cta: 'Next →',
    color: 'linear-gradient(135deg,#f59e0b,#ef4444)',
    visual: `<div style="background:rgba(0,0,0,.3);border-radius:12px;padding:16px;margin:16px 0;text-align:left;font-size:.8rem">
      <div style="color:#94a3b8;margin-bottom:8px;font-size:.72rem;text-transform:uppercase;font-weight:700">AI Coach Feedback</div>
      <div style="color:#fbbf24;font-weight:900;margin-bottom:8px">SCORE: 8/10</div>
      <div style="color:#34d399;margin-bottom:4px">✓ Strong opening hook</div>
      <div style="color:#34d399;margin-bottom:4px">✓ Clear position statement</div>
      <div style="color:#f87171;margin-bottom:4px">✗ Evidence needs specific data</div>
      <div style="color:#60a5fa;margin-top:8px;font-weight:700">Coach's Advice: "Add one statistic per argument to make your case irrefutable."</div>
    </div>`,
    link: 'debate.html',
    linkLabel: 'Try Debate Coach'
  },
  {
    id: 'tracker',
    icon: '📈',
    title: 'Improvement Tracker',
    subtitle: 'See exactly where you\'re headed',
    body: 'The tracker analyzes your test scores, study habits, and streaks to show you score trends, predict where you\'ll be in 30 days, and pinpoint your weakest subjects.',
    cta: 'Next →',
    color: 'linear-gradient(135deg,#10b981,#0ea5e9)',
    visual: `<div style="background:rgba(0,0,0,.3);border-radius:12px;padding:16px;margin:16px 0">
      <div style="color:#94a3b8;margin-bottom:12px;font-size:.72rem;text-transform:uppercase;font-weight:700;text-align:left">30-Day Projection</div>
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
        <div style="text-align:left;flex:1"><div style="font-size:.72rem;color:#94a3b8">AP Calc Now</div><div style="background:#1e293b;height:8px;border-radius:99px;margin-top:4px"><div style="width:72%;background:#6366f1;height:8px;border-radius:99px"></div></div></div>
        <span style="color:#6366f1;font-weight:900">→</span>
        <div style="text-align:left;flex:1"><div style="font-size:.72rem;color:#10b981">In 30 days</div><div style="background:#1e293b;height:8px;border-radius:99px;margin-top:4px"><div style="width:86%;background:#10b981;height:8px;border-radius:99px"></div></div></div>
      </div>
      <div style="color:#10b981;font-weight:700;font-size:.85rem;text-align:center">72% → 86% projected ↑</div>
    </div>`,
    link: 'improvementtracker.html',
    linkLabel: 'Open Tracker'
  },
  {
    id: 'apikey',
    icon: '✦',
    title: 'Enable AI Features',
    subtitle: 'One key, all tools unlocked',
    body: 'The AI features use Claude by Anthropic. Enter your API key once and it\'s saved on this device — or skip this and you\'ll be prompted the first time you use an AI tool.',
    cta: null, // custom buttons
    color: 'linear-gradient(135deg,#6366f1,#8b5cf6)',
    visual: null,
    isKeyStep: true
  }
];

// ── Inject CSS ────────────────────────────────────────────────────────────────
function injectCSS(){
  if(document.getElementById(OB_CSS_KEY)) return;
  var s = document.createElement('style');
  s.id = OB_CSS_KEY;
  s.textContent = `
    #_ob_overlay{position:fixed;inset:0;z-index:999999;display:flex;align-items:center;justify-content:center;padding:20px;background:rgba(6,11,24,.85);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
    #_ob_card{background:#0d1526;border:1.5px solid rgba(99,102,241,.4);border-radius:24px;max-width:480px;width:100%;box-shadow:0 40px 80px rgba(0,0,0,.6);overflow:hidden;animation:_ob_pop .35s cubic-bezier(.34,1.56,.64,1)}
    @keyframes _ob_pop{from{opacity:0;transform:scale(.9) translateY(20px)}to{opacity:1;transform:scale(1) translateY(0)}}
    ._ob_header{padding:32px 28px 0;text-align:center}
    ._ob_icon{font-size:2.8rem;margin-bottom:12px;display:block;animation:_ob_bounce 2s infinite}
    @keyframes _ob_bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
    ._ob_title{font-size:1.35rem;font-weight:900;color:#e2e8f0;margin:0 0 4px}
    ._ob_subtitle{font-size:.85rem;font-weight:700;margin:0 0 14px;background:var(--_ob_grad,linear-gradient(135deg,#818cf8,#c084fc));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
    ._ob_body{font-size:.87rem;color:#94a3b8;line-height:1.7;margin:0 0 4px}
    ._ob_content{padding:0 28px 24px}
    ._ob_footer{padding:16px 28px 28px;display:flex;flex-direction:column;gap:10px}
    ._ob_cta{width:100%;padding:14px;border:none;border-radius:12px;font-size:.95rem;font-weight:800;cursor:pointer;color:#fff;transition:.15s}
    ._ob_cta:hover{opacity:.9;transform:translateY(-1px)}
    ._ob_skip{background:none;border:none;color:#475569;font-size:.8rem;cursor:pointer;padding:4px;font-weight:600}
    ._ob_skip:hover{color:#94a3b8}
    ._ob_dots{display:flex;justify-content:center;gap:6px;margin-bottom:16px}
    ._ob_dot{width:8px;height:8px;border-radius:99px;background:#1e293b;transition:all .25s;cursor:pointer}
    ._ob_dot.active{background:#6366f1;width:24px}
    ._ob_link{display:block;text-align:center;background:#1e293b;border:1px solid #334155;border-radius:10px;padding:10px;font-size:.82rem;font-weight:700;color:#a5b4fc;text-decoration:none;transition:.15s}
    ._ob_link:hover{border-color:#6366f1;background:rgba(99,102,241,.1)}
    ._ob_key_input{width:100%;box-sizing:border-box;background:#060b18;border:1.5px solid #1e293b;border-radius:10px;padding:12px 14px;color:#fff;font-size:.88rem;outline:none;margin:12px 0}
    ._ob_key_input:focus{border-color:#6366f1}
    ._ob_key_err{color:#f87171;font-size:.78rem;margin-bottom:8px;display:none}
    @media(max-width:480px){
      #_ob_card{border-radius:20px}
      ._ob_header{padding:24px 20px 0}
      ._ob_content{padding:0 20px 16px}
      ._ob_footer{padding:12px 20px 24px}
      ._ob_title{font-size:1.15rem}
    }
  `;
  document.head.appendChild(s);
}

// ── Build card HTML ───────────────────────────────────────────────────────────
function buildCard(stepIdx){
  var step  = STEPS[stepIdx];
  var total = STEPS.length;
  var dots  = STEPS.map((_,i)=>`<div class="_ob_dot${i===stepIdx?' active':''}" onclick="_aceOB.goTo(${i})"></div>`).join('');

  var footer = '';
  if(step.isKeyStep){
    footer = `
      <input class="_ob_key_input" id="_ob_key_inp" type="password" placeholder="sk-ant-api03-..." />
      <div class="_ob_key_err" id="_ob_key_err">Key must start with sk-ant-</div>
      <button class="_ob_cta" style="background:${step.color}" onclick="_aceOB.saveKey()">Save Key &amp; Finish ✦</button>
      <button class="_ob_skip" onclick="_aceOB.finish()">Skip — I'll set it up later</button>`;
  } else {
    footer = `
      ${step.link ? `<a class="_ob_link" href="${step.link}">${step.linkLabel}</a>` : ''}
      <button class="_ob_cta" style="background:${step.color}" onclick="_aceOB.next()">${step.cta}</button>
      <button class="_ob_skip" onclick="_aceOB.finish()">Skip tour</button>`;
  }

  return `
    <div id="_ob_card">
      <div class="_ob_header" style="--_ob_grad:${step.color}">
        <span class="_ob_icon">${step.icon}</span>
        <h2 class="_ob_title">${step.title}</h2>
        <p class="_ob_subtitle">${step.subtitle}</p>
      </div>
      <div class="_ob_content">
        <p class="_ob_body">${step.body}</p>
        ${step.visual || ''}
        ${step.isKeyStep ? '' : ''}
      </div>
      <div class="_ob_footer">
        <div class="_ob_dots">${dots}</div>
        ${footer}
        <div style="text-align:center;font-size:.72rem;color:#334155;margin-top:2px">${stepIdx+1} / ${total}</div>
      </div>
    </div>`;
}

// ── Controller ────────────────────────────────────────────────────────────────
var currentStep = 0;

function render(){
  var ov = document.getElementById('_ob_overlay');
  if(!ov) return;
  ov.innerHTML = buildCard(currentStep);
  // auto-focus key input
  if(STEPS[currentStep].isKeyStep){
    setTimeout(function(){ var el=document.getElementById('_ob_key_inp'); if(el) el.focus(); },100);
  }
}

function show(){
  if(document.getElementById('_ob_overlay')) return;
  injectCSS();
  currentStep = 0;
  var ov = document.createElement('div');
  ov.id = '_ob_overlay';
  ov.innerHTML = buildCard(0);
  document.body.appendChild(ov);
}

function next(){
  if(currentStep < STEPS.length-1){ currentStep++; render(); }
  else { finish(); }
}

function goTo(i){
  currentStep = i;
  render();
}

function finish(){
  localStorage.setItem(OB_KEY,'1');
  var ov = document.getElementById('_ob_overlay');
  if(ov){ ov.style.opacity='0'; ov.style.transition='opacity .3s'; setTimeout(function(){ ov.remove(); },300); }
}

function saveKey(){
  var inp = document.getElementById('_ob_key_inp');
  var err = document.getElementById('_ob_key_err');
  var val = inp ? inp.value.trim() : '';
  if(!val.startsWith('sk-ant-')){ if(err){err.style.display='';err.textContent='Key must start with sk-ant-';} return; }
  if(typeof aceAI !== 'undefined') aceAI.setKey(val);
  else localStorage.setItem('ace_claude_key', val);
  finish();
  // Small success toast
  var t = document.createElement('div');
  t.style.cssText='position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#10b981;color:#fff;padding:10px 24px;border-radius:99px;font-weight:800;font-size:.88rem;z-index:9999999;box-shadow:0 8px 24px rgba(16,185,129,.4)';
  t.textContent='✓ AI features unlocked!';
  document.body.appendChild(t);
  setTimeout(function(){ t.style.opacity='0'; t.style.transition='opacity .4s'; setTimeout(function(){t.remove();},400); },2500);
}

// ── Auto-show on first visit ──────────────────────────────────────────────────
window._aceOB = { show:show, next:next, goTo:goTo, finish:finish, saveKey:saveKey };

document.addEventListener('DOMContentLoaded', function(){
  // Don't show on login page
  if(location.pathname.indexOf('login') !== -1) return;
  if(!localStorage.getItem(OB_KEY)){
    setTimeout(show, 800);
  }
});

})();
