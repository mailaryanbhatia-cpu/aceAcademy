#!/usr/bin/env python3
"""
Final polish pass:
1. Add hero welcome banner inside index.html main content
2. Add polish CSS to curriculum sidebar, cards, grade headers
3. Improve progress.html, flashcards.html stat displays
"""
import pathlib, re

base = pathlib.Path('/sessions/admiring-stoic-pascal/mnt/outputs')

# ── 1. index.html: inject hero banner above the curriculum grid ───────────────
HERO_CSS = '''
<style id="ace-hero-css">
/* ── Hero Banner ─────────────────────────────────────── */
.hero-banner {
  background: linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4338ca 100%);
  border-radius: 16px;
  padding: 36px 40px;
  margin-bottom: 32px;
  color: #fff;
  position: relative;
  overflow: hidden;
}
.hero-banner::before {
  content: '';
  position: absolute;
  top: -40px; right: -40px;
  width: 220px; height: 220px;
  background: rgba(255,255,255,.04);
  border-radius: 50%;
}
.hero-banner::after {
  content: '';
  position: absolute;
  bottom: -60px; right: 60px;
  width: 300px; height: 300px;
  background: rgba(255,255,255,.03);
  border-radius: 50%;
}
.hero-title {
  font-size: 1.9rem;
  font-weight: 900;
  letter-spacing: -0.5px;
  margin-bottom: 8px;
  line-height: 1.2;
}
.hero-title span { color: #a5b4fc; }
.hero-sub {
  font-size: 0.92rem;
  color: #c7d2fe;
  margin-bottom: 24px;
  max-width: 500px;
  line-height: 1.6;
}
.hero-chips {
  display: flex; gap: 8px; flex-wrap: wrap;
}
.hero-chip {
  background: rgba(255,255,255,.12);
  border: 1px solid rgba(255,255,255,.15);
  border-radius: 20px;
  padding: 5px 14px;
  font-size: 0.76rem;
  font-weight: 600;
  color: #e0e7ff;
  backdrop-filter: blur(4px);
}

/* ── Feature cards row ───────────────────────────────── */
.feature-row {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 12px;
  margin-bottom: 28px;
}
.feature-card {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 16px;
  text-decoration: none;
  color: #0f172a;
  transition: transform .15s, box-shadow .15s;
  box-shadow: 0 1px 3px rgba(0,0,0,.06);
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.feature-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(0,0,0,.1);
}
.feature-icon { font-size: 1.5rem; }
.feature-label {
  font-size: 0.8rem;
  font-weight: 700;
  color: #1e293b;
}
.feature-desc {
  font-size: 0.72rem;
  color: #64748b;
  line-height: 1.4;
}

/* ── Curriculum section header ───────────────────────── */
.section-divider {
  display: flex; align-items: center; gap: 12px;
  margin-bottom: 20px;
}
.section-divider h2 {
  font-size: 1rem; font-weight: 700; color: #0f172a; white-space: nowrap;
}
.section-divider::after {
  content: ''; flex: 1; height: 1px; background: #e2e8f0;
}
</style>
'''

HERO_HTML = '''<div class="hero-banner">
      <div class="hero-title">Learn Smarter.<br><span>Grades 6–12 Curriculum.</span></div>
      <div class="hero-sub">Everything you need — lessons, worksheets, practice tests, flashcards, and an AI tutor. All free, all in one place.</div>
      <div class="hero-chips">
        <span class="hero-chip">📐 Math</span>
        <span class="hero-chip">🔬 Science</span>
        <span class="hero-chip">📖 ELA</span>
        <span class="hero-chip">🏛 History</span>
        <span class="hero-chip">💻 CS</span>
        <span class="hero-chip">❤️ Health</span>
      </div>
    </div>
    <div class="feature-row">
      <a href="worksheets.html" class="feature-card">
        <div class="feature-icon">📄</div>
        <div class="feature-label">Worksheets</div>
        <div class="feature-desc">Practice problems with hints &amp; answers</div>
      </a>
      <a href="tests.html" class="feature-card">
        <div class="feature-icon">✏️</div>
        <div class="feature-label">Tests</div>
        <div class="feature-desc">Auto-graded unit quizzes</div>
      </a>
      <a href="flashcards.html" class="feature-card">
        <div class="feature-icon">🃏</div>
        <div class="feature-label">Flashcards</div>
        <div class="feature-desc">800+ vocab cards across all subjects</div>
      </a>
      <a href="tutor.html" class="feature-card">
        <div class="feature-icon">🎓</div>
        <div class="feature-label">AI Tutor</div>
        <div class="feature-desc">Socratic guided learning</div>
      </a>
      <a href="notebook.html" class="feature-card">
        <div class="feature-icon">📁</div>
        <div class="feature-label">Notebook</div>
        <div class="feature-desc">Subject folders for your notes</div>
      </a>
      <a href="progress.html" class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-label">Progress</div>
        <div class="feature-desc">Track your test scores &amp; streaks</div>
      </a>
      <a href="calendar.html" class="feature-card">
        <div class="feature-icon">📅</div>
        <div class="feature-label">Planner</div>
        <div class="feature-desc">Set goals &amp; deadlines</div>
      </a>
      <a href="language.html" class="feature-card">
        <div class="feature-icon">🌏</div>
        <div class="feature-label">Languages</div>
        <div class="feature-desc">Mandarin, Japanese, Hindi</div>
      </a>
    </div>
    <div class="section-divider"><h2>📚 Browse Curriculum</h2></div>
    '''

# Patch index.html
p = base / 'index.html'
html = p.read_text(encoding='utf-8')

if 'hero-banner' not in html:
    # Inject CSS before </head>
    html = html.replace('</head>', HERO_CSS + '</head>', 1)
    # Inject hero inside <main id="mainContent"> using JS — prepend to renderGrade output
    # Find the renderGrade function and prepend the hero before the first grade render
    # Actually inject it as static HTML before the JS-rendered content
    old_main = '<main id="mainContent"></main>'
    new_main = '''<main id="mainContent">
    ''' + HERO_HTML + '''</main>'''
    if old_main in html:
        html = html.replace(old_main, new_main, 1)
        print('✅ index.html: hero banner injected')
    else:
        print('⚠️  index.html: main tag not matched')
    p.write_text(html, encoding='utf-8')
else:
    print('index.html: hero already present')

# ── 2. Polish progress.html stat cards ───────────────────────────────────────
p2 = base / 'progress.html'
h2 = p2.read_text(encoding='utf-8')
PROGRESS_POLISH = '''
<style id="ace-progress-polish">
.stat-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 14px; margin-bottom: 28px; }
.stat-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; box-shadow: 0 1px 4px rgba(0,0,0,.06); }
.stat-num { font-size: 2rem; font-weight: 900; line-height: 1; }
.stat-label { font-size: 0.75rem; color: #64748b; margin-top: 4px; font-weight: 500; text-transform: uppercase; letter-spacing: .5px; }
.section-title { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: .8px; color: #94a3b8; margin: 24px 0 10px; padding-bottom: 6px; border-bottom: 1px solid #e2e8f0; }
.score-bar-wrap { background: #fff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; margin-bottom: 8px; box-shadow: 0 1px 3px rgba(0,0,0,.05); }
main { padding: 28px 32px !important; max-width: 900px; }
</style>
'''
if 'ace-progress-polish' not in h2:
    h2 = h2.replace('</head>', PROGRESS_POLISH + '</head>', 1)
    p2.write_text(h2, encoding='utf-8')
    print('✅ progress.html: polished')

# ── 3. Polish flashcards.html ─────────────────────────────────────────────────
p3 = base / 'flashcards.html'
h3 = p3.read_text(encoding='utf-8')
FC_POLISH = '''
<style id="ace-fc-polish">
.fc-controls { background: #fff; border-bottom: 1px solid #e2e8f0; padding: 12px 24px; display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
.fc-card-wrap { display: flex; justify-content: center; align-items: center; padding: 40px 20px; }
.fc-card { border-radius: 18px !important; box-shadow: 0 8px 32px rgba(0,0,0,.13) !important; }
.fc-stats { background: #fff; border-top: 1px solid #e2e8f0; padding: 12px 24px; display: flex; gap: 20px; }
body { background: #f1f5f9; }
</style>
'''
if 'ace-fc-polish' not in h3:
    h3 = h3.replace('</head>', FC_POLISH + '</head>', 1)
    p3.write_text(h3, encoding='utf-8')
    print('✅ flashcards.html: polished')

# ── 4. Fix curriculum/index aside h3 uppercase labels ───────────────────────
for fname in ['index.html', 'curriculum.html']:
    p4 = base / fname
    h4 = p4.read_text(encoding='utf-8')
    SIDEBAR_POLISH = '''
<style id="ace-sidebar-polish">
aside { background: #fff !important; }
.page { background: #f1f5f9; }
main { padding: 28px 36px !important; }
.grade-header { padding-bottom: 20px !important; margin-bottom: 24px !important; border-bottom: 2px solid #e2e8f0 !important; }
.grade-header h1 { font-size: 1.65rem !important; font-weight: 900 !important; color: #0f172a !important; letter-spacing: -.5px !important; }
.subject-section { margin-bottom: 32px !important; }
.subject-title h2 { font-size: 0.98rem !important; font-weight: 700 !important; }
.unit-card { margin-bottom: 6px; transition: box-shadow .18s, transform .18s; }
.unit-card:hover { transform: translateY(-1px); }
.unit-body { background: #fafbff; }
.unit-body ul li { font-size: 0.85rem !important; color: #334155 !important; }
.unit-body ul li::before { background: #a5b4fc !important; }
.practice-label { color: #4f46e5 !important; font-size: 0.68rem !important; letter-spacing: 1px !important; }
.ps-btn { border-radius: 8px !important; font-size: 0.8rem !important; font-weight: 600 !important; }
.ps-btn:hover, .ps-btn.active { background: #4f46e5 !important; color: #fff !important; border-color: #4f46e5 !important; }
.sheet-title { color: #4f46e5 !important; font-size: 0.9rem !important; font-weight: 700 !important; }
</style>
'''
    if 'ace-sidebar-polish' not in h4:
        h4 = h4.replace('</head>', SIDEBAR_POLISH + '</head>', 1)
        p4.write_text(h4, encoding='utf-8')
        print(f'✅ {fname}: sidebar polish')

# ── 5. Polish tests.html ──────────────────────────────────────────────────────
p5 = base / 'tests.html'
h5 = p5.read_text(encoding='utf-8')
TESTS_POLISH = '''
<style id="ace-tests-polish">
body { background: #f1f5f9 !important; }
.test-card, .question-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 1px 4px rgba(0,0,0,.06); }
.choice-btn { border-radius: 8px !important; transition: all .15s !important; border: 2px solid #e2e8f0 !important; }
.choice-btn:hover { border-color: #4f46e5 !important; background: #eef2ff !important; }
.choice-btn.correct { border-color: #059669 !important; background: #d1fae5 !important; color: #065f46 !important; }
.choice-btn.wrong   { border-color: #dc2626 !important; background: #fee2e2 !important; color: #7f1d1d !important; }
.score-display { background: linear-gradient(135deg,#1e1b4b,#4338ca); color: #fff; border-radius: 14px; padding: 24px; margin-bottom: 20px; }
</style>
'''
if 'ace-tests-polish' not in h5:
    h5 = h5.replace('</head>', TESTS_POLISH + '</head>', 1)
    p5.write_text(h5, encoding='utf-8')
    print('✅ tests.html: polished')

# ── 6. Polish worksheets.html ─────────────────────────────────────────────────
p6 = base / 'worksheets.html'
h6 = p6.read_text(encoding='utf-8')
WS_POLISH = '''
<style id="ace-ws-polish">
body { background: #f1f5f9 !important; }
.problem-card { background: #fff; border-radius: 12px !important; border: 1px solid #e2e8f0 !important; box-shadow: 0 1px 4px rgba(0,0,0,.06) !important; }
.problem-num { background: #4f46e5 !important; border-radius: 50% !important; }
.diff-badge { border-radius: 6px !important; font-weight: 700 !important; }
.hint-toggle { border-color: #4f46e5 !important; color: #4f46e5 !important; border-radius: 6px !important; }
.hint-toggle:hover { background: #eef2ff !important; }
.ans-btn { border-radius: 6px !important; }
.ans-btn:hover { border-color: #4f46e5 !important; color: #4f46e5 !important; }
.answer-panel { background: #eef2ff; border-left: 3px solid #4f46e5; border-radius: 0 8px 8px 0; }
.diff-section-label { font-size: 0.78rem; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: .8px; margin: 20px 0 10px; }
.canvas-toolbar { background: #f8fafc !important; border-radius: 8px !important; }
</style>
'''
if 'ace-ws-polish' not in h6:
    h6 = h6.replace('</head>', WS_POLISH + '</head>', 1)
    p6.write_text(h6, encoding='utf-8')
    print('✅ worksheets.html: polished')

print('\nAll polish complete.')
