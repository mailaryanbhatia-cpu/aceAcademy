#!/usr/bin/env python3
"""Fix <nav class="topnav"> pages and add a professional landing hero to index.html."""
import pathlib, re

base = pathlib.Path('/sessions/admiring-stoic-pascal/mnt/outputs')

NAV_CSS = '''<style id="ace-nav-css">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
body { font-family: 'Inter', 'Segoe UI', system-ui, sans-serif; -webkit-font-smoothing: antialiased; }
nav.topnav {
  background: #0f172a !important;
  border-bottom: none !important;
  box-shadow: 0 2px 16px rgba(0,0,0,.3) !important;
  padding: 0 20px !important;
  height: 60px !important;
  display: flex !important;
  align-items: center !important;
  gap: 2px !important;
  position: sticky !important;
  top: 0 !important;
  z-index: 500 !important;
  overflow-x: auto !important;
}
nav.topnav::-webkit-scrollbar { display: none; }
nav.topnav .logo, nav.topnav a.logo {
  font-size: 1.1rem !important; font-weight: 800 !important;
  color: #fff !important; text-decoration: none !important;
  margin-right: 10px !important; white-space: nowrap !important; flex-shrink: 0 !important;
  display: flex !important; align-items: center !important; gap: 6px !important;
}
nav.topnav .logo span, nav.topnav a.logo span { color: #818cf8 !important; }
nav.topnav a.nav-link, nav.topnav a.back-link {
  display: inline-flex !important; align-items: center !important; gap: 3px !important;
  text-decoration: none !important; padding: 6px 9px !important;
  border-radius: 7px !important; font-size: 0.76rem !important;
  font-weight: 600 !important; white-space: nowrap !important;
  color: #94a3b8 !important; transition: background .15s, color .15s !important;
  font-family: inherit !important;
}
nav.topnav a.nav-link:hover, nav.topnav a.back-link:hover {
  background: rgba(255,255,255,.1) !important; color: #fff !important;
}
nav.topnav a.nav-link.active {
  background: rgba(99,102,241,.25) !important; color: #a5b4fc !important;
}
nav.topnav .spacer, nav.topnav h1.nav-title {
  flex: 1 !important; color: #94a3b8 !important;
  font-size: 0.8rem !important; font-weight: 500 !important;
}
nav.topnav input, nav.topnav select {
  background: #1e293b !important; border: 1px solid #334155 !important;
  color: #e2e8f0 !important; border-radius: 6px !important;
  padding: 5px 10px !important; font-size: 0.78rem !important;
  font-family: inherit !important; outline: none !important;
}
/* General polish */
:root {
  --bg:#f1f5f9; --surface:#fff; --border:#e2e8f0; --text:#0f172a;
  --muted:#64748b; --accent:#4f46e5; --accent-light:#eef2ff;
  --shadow-sm:0 1px 3px rgba(0,0,0,.07),0 1px 2px rgba(0,0,0,.04);
  --shadow:0 4px 12px rgba(0,0,0,.08),0 2px 4px rgba(0,0,0,.04);
  --radius:10px;
}
body { background: var(--bg); color: var(--text); }
.problem-card, .unit-card, .stat-card, .goal-item {
  box-shadow: var(--shadow-sm) !important; border-radius: 10px !important;
}
.problem-card:hover, .unit-card:hover { box-shadow: var(--shadow) !important; }
.unit-num { background:#eef2ff !important; color:#4f46e5 !important; border:none !important; }
footer { background:#0f172a !important; color:#94a3b8 !important; border-top:none !important; }
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:#cbd5e1;border-radius:10px}
::-webkit-scrollbar-thumb:hover{background:#94a3b8}
</style>
'''

TOPNAV_PAGES = {
    'worksheets.html': 'worksheets.html',
    'tests.html':      'tests.html',
    'language.html':   'language.html',
    'tutor.html':      'tutor.html',
}

for fname, active in TOPNAV_PAGES.items():
    p = base / fname
    html = p.read_text(encoding='utf-8')

    # Inject CSS if not already there
    if 'ace-nav-css' not in html:
        html = html.replace('</head>', NAV_CSS + '</head>', 1)

    # Fix title
    titles = {
        'worksheets.html': 'aceAcademy — Worksheets',
        'tests.html':      'aceAcademy — Tests',
        'language.html':   'aceAcademy — Languages',
        'tutor.html':      'aceAcademy — AI Tutor',
    }
    html = re.sub(r'<title>[^<]*</title>', f'<title>{titles[fname]}</title>', html)

    # Fix footer
    html = html.replace('EduPath', 'aceAcademy')

    p.write_text(html, encoding='utf-8')
    print(f'✅ {fname}')

print('\nAll topnav pages updated.')
