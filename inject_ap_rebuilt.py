#!/usr/bin/env python3
"""
Inject fully rebuilt AP worksheet data into worksheets.html.
New structure: math(4u), science(7u), ela(2u), history(9u),
               cs(2u), arts(5u), languages(8u), capstone(2u)
Removes old 'health' subject entirely.
"""
import sys, json, re
sys.path.insert(0, '/sessions/admiring-stoic-pascal/mnt/outputs')

from ap_rebuild_math    import AP_MATH
from ap_rebuild_science import AP_SCIENCE
from ap_rebuild_ela     import AP_ELA
from ap_rebuild_history import AP_HISTORY
from ap_rebuild_arts    import AP_ARTS
from ap_rebuild_langs   import AP_LANGS
from ap_rebuild_cap     import AP_CAP

# Reuse existing AP_CS (already matches curriculum)
from ap_data_hist_cs_health import AP_CS

WORKSHEETS_PATH = '/sessions/admiring-stoic-pascal/mnt/outputs/worksheets.html'

# ── serialisers ──────────────────────────────────────────────────────────────

def js_str(s):
    return json.dumps(str(s), ensure_ascii=False)

def build_problems(problems):
    parts = []
    for p in problems:
        parts.append(
            '{q:'  + js_str(p['q'])    +
            ',ex:' + js_str(p['ex'])   +
            ',a:'  + js_str(p['a'])    +
            ',diff:'+ js_str(p['diff']) + '}'
        )
    return '[' + ','.join(parts) + ']'

def build_topic(topic):
    return ('{title:' + js_str(topic['title']) +
            ',problems:' + build_problems(topic['problems']) + '}')

def build_unit(unit):
    return '[' + ','.join(build_topic(t) for t in unit) + ']'

def build_subject(units):
    return '[' + ','.join(build_unit(u) for u in units) + ']'

def build_ap_block():
    subjects = {
        'math':      AP_MATH,
        'science':   AP_SCIENCE,
        'ela':       AP_ELA,
        'history':   AP_HISTORY,
        'cs':        AP_CS,
        'arts':      AP_ARTS,
        'languages': AP_LANGS,
        'capstone':  AP_CAP,
    }
    inner = ','.join(
        f'"{key}":{build_subject(val)}'
        for key, val in subjects.items()
    )
    return f'"ap":{{{inner}}}'

# ── bracket-depth parser ─────────────────────────────────────────────────────

def find_bracket_end(text, start):
    open_ch  = text[start]
    close_ch = ']' if open_ch == '[' else '}'
    depth = 0
    i = start
    in_str = False
    escape = False
    while i < len(text):
        ch = text[i]
        if escape:
            escape = False
        elif ch == '\\' and in_str:
            escape = True
        elif ch == '"' and not escape:
            in_str = not in_str
        elif not in_str:
            if ch == open_ch:
                depth += 1
            elif ch == close_ch:
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return -1

def find_ap_span(text):
    """Return (span_start, span_end) of the entire "ap":{...} entry."""
    ws_match = re.search(r'\bWORKSHEETS\s*=\s*\{', text)
    if not ws_match:
        print("ERROR: WORKSHEETS not found"); return None, None

    ws_start = ws_match.end() - 1          # the opening {
    ws_end   = find_bracket_end(text, ws_start)

    block        = text[ws_start:ws_end + 1]
    ap_match     = re.search(r'["\']ap["\']\s*:\s*\{', block)
    if not ap_match:
        print("ERROR: 'ap' key not found"); return None, None

    ap_key_local  = ap_match.start()
    ap_brace_local = ap_match.end() - 1        # the { of ap's value
    ap_brace_abs  = ws_start + ap_brace_local
    ap_end_abs    = find_bracket_end(text, ap_brace_abs)

    span_start = ws_start + ap_key_local
    span_end   = ap_end_abs                   # inclusive
    return span_start, span_end

# ── main ─────────────────────────────────────────────────────────────────────

def count_topics(subject_data):
    return sum(len(unit) for unit in subject_data)

def main():
    with open(WORKSHEETS_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    ap_start, ap_end = find_ap_span(html)
    if ap_start is None:
        sys.exit(1)

    print(f"Found AP block at chars {ap_start}–{ap_end}")
    print(f"Old snippet: {html[ap_start:ap_start+60]}...")

    new_ap   = build_ap_block()
    new_html = html[:ap_start] + new_ap + html[ap_end + 1:]

    # ── topic-count report ──
    subjects = {
        'math':      AP_MATH,
        'science':   AP_SCIENCE,
        'ela':       AP_ELA,
        'history':   AP_HISTORY,
        'cs':        AP_CS,
        'arts':      AP_ARTS,
        'languages': AP_LANGS,
        'capstone':  AP_CAP,
    }
    total = 0
    for name, data in subjects.items():
        n = count_topics(data)
        total += n
        print(f"  {name:12s}: {len(data):2d} units, {n:3d} topics")
    print(f"  {'TOTAL':12s}: {total:3d} topics")

    # ── JS syntax check (write to temp file to avoid arg-list limits) ──
    import subprocess, tempfile, os
    js_check = f'var WORKSHEETS={{{new_ap}}}'
    with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as tf:
        tf.write(js_check)
        tmp_path = tf.name
    result = subprocess.run(['node', '--check', tmp_path], capture_output=True, text=True)
    os.unlink(tmp_path)
    if result.returncode != 0:
        print("JS SYNTAX ERROR:", result.stderr[:400])
        sys.exit(1)
    print("JS syntax: OK")

    with open(WORKSHEETS_PATH, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print("worksheets.html updated successfully!")
    print(f"New file size: {len(new_html):,} bytes")

if __name__ == '__main__':
    main()
