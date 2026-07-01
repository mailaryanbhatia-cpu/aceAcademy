#!/usr/bin/env python3
"""Inject missing tests into tests.html to match curriculum structure."""
import sys, json, re
sys.path.insert(0, '/sessions/admiring-stoic-pascal/mnt/outputs')

from gen_missing_tests_1 import (
    G12_HISTORY_U4, AP_SCIENCE_U5, AP_SCIENCE_U6, AP_SCIENCE_U7
)
from gen_missing_tests_2 import (
    AP_HISTORY_U5, AP_HISTORY_U6, AP_HISTORY_U7, AP_HISTORY_U8, AP_HISTORY_U9
)
from gen_missing_tests_3 import (
    AP_ARTS_U1, AP_ARTS_U2, AP_ARTS_U3, AP_ARTS_U4, AP_ARTS_U5,
    AP_LANGS_U1, AP_LANGS_U2, AP_LANGS_U3, AP_LANGS_U4, AP_LANGS_U5,
    AP_LANGS_U6, AP_LANGS_U7, AP_LANGS_U8,
    AP_CAPSTONE_U1, AP_CAPSTONE_U2
)

TESTS_PATH = '/sessions/admiring-stoic-pascal/mnt/outputs/tests.html'

def find_end(text, start):
    depth=0; i=start; in_str=False; esc=False
    while i < len(text):
        c=text[i]
        if esc: esc=False
        elif c=='\\' and in_str: esc=True
        elif c=='"' and not esc: in_str=not in_str
        elif not in_str:
            if c=='{': depth+=1
            elif c=='}':
                depth-=1
                if depth==0: return i
        i+=1
    return -1

with open(TESTS_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# Parse TESTS object
start = html.index('const TESTS = ') + len('const TESTS = ')
end = find_end(html, start)
tests = json.loads(html[start:end+1])

print("Before injection:")
for grade, subjects in tests.items():
    counts = {s: len(u) for s, u in subjects.items()}
    print(f"  Grade {grade}: {counts}")

# ── Grade 12: add history unit 4 ─────────────────────────────────────────────
tests['12']['history'].append(G12_HISTORY_U4)

# ── AP Science: add units 5, 6, 7 ────────────────────────────────────────────
tests['ap']['science'].append(AP_SCIENCE_U5)
tests['ap']['science'].append(AP_SCIENCE_U6)
tests['ap']['science'].append(AP_SCIENCE_U7)

# ── AP History: add units 5-9 ─────────────────────────────────────────────────
tests['ap']['history'].append(AP_HISTORY_U5)
tests['ap']['history'].append(AP_HISTORY_U6)
tests['ap']['history'].append(AP_HISTORY_U7)
tests['ap']['history'].append(AP_HISTORY_U8)
tests['ap']['history'].append(AP_HISTORY_U9)

# ── AP Arts: new subject ──────────────────────────────────────────────────────
tests['ap']['arts'] = [AP_ARTS_U1, AP_ARTS_U2, AP_ARTS_U3, AP_ARTS_U4, AP_ARTS_U5]

# ── AP Languages: new subject ─────────────────────────────────────────────────
tests['ap']['languages'] = [
    AP_LANGS_U1, AP_LANGS_U2, AP_LANGS_U3, AP_LANGS_U4,
    AP_LANGS_U5, AP_LANGS_U6, AP_LANGS_U7, AP_LANGS_U8
]

# ── AP Capstone: new subject ──────────────────────────────────────────────────
tests['ap']['capstone'] = [AP_CAPSTONE_U1, AP_CAPSTONE_U2]

print("\nAfter injection:")
for grade, subjects in tests.items():
    counts = {s: len(u) for s, u in subjects.items()}
    print(f"  Grade {grade}: {counts}")

# Serialize and inject
new_tests_json = json.dumps(tests, ensure_ascii=False, separators=(',', ':'))
new_html = html[:start] + new_tests_json + html[end+1:]

with open(TESTS_PATH, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"\ntests.html updated. New size: {len(new_html):,} bytes")
