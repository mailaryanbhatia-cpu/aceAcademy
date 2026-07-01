#!/usr/bin/env python3
"""
Professional polish pass for aceAcademy.
- Unified dark navbar across all pages
- Fix "EduPath" → "aceAcademy" branding
- Fix page titles
- Update sidebar sticky position
- Add footer
"""
import pathlib, re

base = pathlib.Path('/sessions/admiring-stoic-pascal/mnt/outputs')

# ── Shared nav HTML ───────────────────────────────────────────────────────────
# Each page gets this nav. Current page link has class="active" (set per-page below)
NAV_LINKS = [
    ('curriculum.html', '📚', 'Curriculum',  '#4f46e5'),
    ('worksheets.html', '📄', 'Worksheets',  '#0284c7'),
    ('tests.html',      '✏️', 'Tests',        '#059669'),
    ('language.html',   '🌏', 'Languages',   '#0891b2'),
    ('flashcards.html', '🃏', 'Flashcards',  '#7c3aed'),
    ('notebook.html',   '📁', 'Notebook',    '#d97706'),
    ('calendar.html',   '📅', 'Calendar',    '#0ea5e9'),
    ('progress.html',   '📊', 'Progress',    '#059669'),
    ('tutor.html',      '🎓', 'AI Tutor',    '#6366f1'),
]

def build_nav(active_page, extra_html=''):
    links_html = ''
    for href, icon, label, color in NAV_LINKS:
        is_active = href == active_page
        links_html += f'  <a href="{href}" class="nav-link{" active" if is_active else ""}" data-color="{color}">{icon} {label}</a>\n'
    return f'''<header>
  <a href="curriculum.html" class="brand">
    <span class="brand-icon">🎓</span>
    <span class="brand-name">ace<span class="brand-accent">Academy</span></span>
  </a>
  <div class="nav-spacer"></div>
  <nav class="nav-links">
{links_html}  </nav>{extra_html}
</header>'''

# ── Per-page config ───────────────────────────────────────────────────────────
PAGES = {
    'curriculum.html': {
        'active': 'curriculum.html',
        'title': 'aceAcademy — Curriculum',
        'extra_nav': '''
  <div class="nav-search">
    <svg width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
    <input type="text" id="searchInput" placeholder="Search topics…" />
  </div>''',
    },
    'index.html': {
        'active': 'curriculum.html',
        'title': 'aceAcademy — Grades 6–12',
        'extra_nav': '''
  <div class="nav-search">
    <svg width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
    <input type="text" id="searchInput" placeholder="Search topics…" />
  </div>''',
    },
    'worksheets.html': {'active': 'worksheets.html', 'title': 'aceAcademy — Worksheets'},
    'tests.html':      {'active': 'tests.html',      'title': 'aceAcademy — Tests'},
    'language.html':   {'active': 'language.html',   'title': 'aceAcademy — Languages'},
    'flashcards.html': {'active': 'flashcards.html', 'title': 'aceAcademy — Flashcards'},
    'notebook.html':   {'active': 'notebook.html',   'title': 'aceAcademy — Notebook'},
    'calendar.html':   {'active': 'calendar.html',   'title': 'aceAcademy — Goal Planner'},
    'progress.html':   {'active': 'progress.html',   'title': 'aceAcademy — Progress'},
    'tutor.html':      {'active': 'tutor.html',      'title': 'aceAcademy — AI Tutor'},
}

# ── Shared nav + theme CSS (injected into <head>) ─────────────────────────────
NAV_CSS = '''
<style id="ace-nav-css">
/* ── Brand / Nav ──────────────────────────────────────────── */
header {
  background: #0f172a !important;
  border-bottom: none !important;
  height: 60px !important;
  padding: 0 20px !important;
  display: flex !important;
  align-items: center !important;
  gap: 4px !important;
  position: sticky !important;
  top: 0 !important;
  z-index: 500 !important;
  box-shadow: 0 2px 16px rgba(0,0,0,.3) !important;
}
.brand {
  display: flex; align-items: center; gap: 8px;
  text-decoration: none; margin-right: 8px; flex-shrink: 0;
}
.brand-icon { font-size: 1.3rem; }
.brand-name {
  font-size: 1.1rem; font-weight: 800; color: #fff;
  letter-spacing: -0.5px; font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
}
.brand-accent { color: #818cf8; }
.nav-spacer { flex: 1; }
.nav-links {
  display: flex; align-items: center; gap: 2px; flex-wrap: nowrap;
  overflow-x: auto; -webkit-overflow-scrolling: touch;
}
.nav-links::-webkit-scrollbar { display: none; }
a.nav-link {
  display: inline-flex; align-items: center; gap: 4px;
  text-decoration: none; padding: 6px 10px; border-radius: 7px;
  font-size: 0.76rem; font-weight: 600; white-space: nowrap; color: #94a3b8;
  transition: background .15s, color .15s; font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
}
a.nav-link:hover  { background: rgba(255,255,255,.1); color: #fff; }
a.nav-link.active { background: rgba(99,102,241,.25); color: #a5b4fc; }
.nav-search {
  position: relative; margin-left: 8px; flex-shrink: 0;
}
.nav-search svg {
  position: absolute; left: 10px; top: 50%; transform: translateY(-50%); color: #64748b;
}
.nav-search input {
  background: #1e293b; border: 1px solid #334155; color: #e2e8f0;
  border-radius: 20px; padding: 6px 14px 6px 30px; font-size: 0.8rem;
  width: 180px; outline: none; font-family: inherit;
  transition: border-color .15s, width .2s;
}
.nav-search input::placeholder { color: #475569; }
.nav-search input:focus { border-color: #818cf8; width: 220px; }

/* Fix sidebar top offset for new nav height */
aside {
  top: 60px !important;
  height: calc(100vh - 60px) !important;
}
.sidebar {
  top: 60px !important;
  height: calc(100vh - 60px) !important;
}

/* Fix page min-height */
.page { min-height: calc(100vh - 60px) !important; }

/* ── General polish ───────────────────────────────────────── */
body {
  font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
  background: #f1f5f9;
  -webkit-font-smoothing: antialiased;
}
:root {
  --bg: #f1f5f9;
  --surface: #ffffff;
  --border: #e2e8f0;
  --text: #0f172a;
  --muted: #64748b;
  --accent: #4f46e5;
  --accent-hover: #4338ca;
  --accent-light: #eef2ff;
  --radius: 10px;
  --shadow-sm: 0 1px 3px rgba(0,0,0,.07), 0 1px 2px rgba(0,0,0,.04);
  --shadow: 0 4px 12px rgba(0,0,0,.08), 0 2px 4px rgba(0,0,0,.04);
}

/* Cards */
.unit-card { box-shadow: var(--shadow-sm) !important; border-radius: 10px !important; border: 1px solid #e2e8f0 !important; }
.unit-card:hover { box-shadow: var(--shadow) !important; }
.unit-header:hover { background: #f8fafc !important; }
.unit-num { background: #eef2ff !important; color: #4f46e5 !important; border: none !important; font-weight: 700 !important; border-radius: 6px !important; }
.unit-name { font-weight: 600 !important; color: #0f172a !important; }

/* Grade header */
.grade-header h1 { font-size: 1.6rem !important; font-weight: 800 !important; letter-spacing: -0.5px !important; color: #0f172a !important; }

/* Subject title */
.subject-title h2 { font-size: 1rem !important; font-weight: 700 !important; color: #0f172a !important; }

/* Sidebar */
aside { background: #fff !important; border-right: 1px solid #e2e8f0 !important; }
.grade-list li a { font-weight: 500 !important; color: #334155 !important; font-size: 0.87rem !important; }
.grade-list li a:hover { background: #eef2ff !important; color: #4f46e5 !important; }
.grade-list li a.active { border-left-color: #4f46e5 !important; background: #eef2ff !important; color: #4f46e5 !important; font-weight: 700 !important; }
aside h3 { color: #94a3b8 !important; font-size: 0.65rem !important; letter-spacing: 1px !important; }

/* Main content */
main { background: transparent !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

/* Footer */
footer { background: #0f172a !important; color: #94a3b8 !important; border-top: none !important; }

/* Stat cards */
.stat-card { box-shadow: var(--shadow-sm) !important; border-radius: 10px !important; }

/* Problem cards */
.problem-card { box-shadow: var(--shadow-sm) !important; border-radius: 10px !important; }

/* Flashcard */
.flashcard { border-radius: 16px !important; box-shadow: 0 8px 30px rgba(0,0,0,.12) !important; }

/* Test choice buttons */
.choice-btn { border-radius: 8px !important; font-weight: 500 !important; }

/* Canvas toolbar */
.canvas-toolbar { border-radius: 8px !important; }
</style>
'''

# ── Process each page ─────────────────────────────────────────────────────────
for fname, cfg in PAGES.items():
    p = base / fname
    if not p.exists():
        print(f'SKIP (not found): {fname}')
        continue

    html = p.read_text(encoding='utf-8')

    # 1. Fix <title>
    html = re.sub(r'<title>[^<]*</title>', f'<title>{cfg["title"]}</title>', html)

    # 2. Inject nav CSS (once, before </head>)
    if 'ace-nav-css' not in html:
        html = html.replace('</head>', NAV_CSS + '</head>', 1)

    # 3. Replace entire <header>…</header> block
    header_match = re.search(r'<header>.*?</header>', html, re.DOTALL)
    if header_match:
        extra = cfg.get('extra_nav', '')
        new_header = build_nav(cfg['active'], extra)
        html = html[:header_match.start()] + new_header + html[header_match.end():]
        print(f'✅ {fname}: header replaced')
    else:
        print(f'⚠️  {fname}: no <header> found')

    # 4. Fix old footer text
    html = html.replace('EduPath — A free curriculum reference for students and educators. Aligned to common US standards.',
                        'aceAcademy — Free grades 6–12 curriculum, aligned to Common Core, NGSS &amp; CSTA standards.')
    html = html.replace('EduPath', 'aceAcademy')

    p.write_text(html, encoding='utf-8')

print('\nDone.')
