#!/usr/bin/env python3
"""
Inject full AP worksheet data (119 topics across 6 subjects) into worksheets.html.
Imports all three data files and rebuilds the WORKSHEETS["ap"] section.
"""
import sys, json, re
sys.path.insert(0, '/sessions/admiring-stoic-pascal/mnt/outputs')

from ap_data_math import AP_MATH
from ap_data_sci_ela import AP_SCIENCE, AP_ELA
from ap_data_hist_cs_health import AP_HISTORY, AP_CS, AP_HEALTH

WORKSHEETS_PATH = '/sessions/admiring-stoic-pascal/mnt/outputs/worksheets.html'

def js_string(s):
    return json.dumps(s, ensure_ascii=False)

def build_problems(problems):
    parts = []
    for p in problems:
        parts.append(
            '{q:' + js_string(p['q']) +
            ',ex:' + js_string(p['ex']) +
            ',a:' + js_string(p['a']) +
            ',diff:' + js_string(p['diff']) + '}'
        )
    return '[' + ','.join(parts) + ']'

def build_topic(topic):
    return ('{title:' + js_string(topic['title']) +
            ',problems:' + build_problems(topic['problems']) + '}')

def build_unit(unit):
    return '[' + ','.join(build_topic(t) for t in unit) + ']'

def build_subject(units):
    return '[' + ','.join(build_unit(u) for u in units) + ']'

def build_ap_block():
    return (
        '"ap":{'
        '"math":' + build_subject(AP_MATH) + ','
        '"science":' + build_subject(AP_SCIENCE) + ','
        '"ela":' + build_subject(AP_ELA) + ','
        '"history":' + build_subject(AP_HISTORY) + ','
        '"cs":' + build_subject(AP_CS) + ','
        '"health":' + build_subject(AP_HEALTH) +
        '}'
    )

def find_bracket_end(text, start):
    """Find the closing bracket/brace matching the one at text[start]."""
    open_ch = text[start]
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

def find_ap_key(text):
    """Find the start of the "ap":{ or 'ap':{ entry inside WORKSHEETS."""
    # Look for the WORKSHEETS object
    ws_match = re.search(r'\bWORKSHEETS\s*=\s*\{', text)
    if not ws_match:
        print("ERROR: WORKSHEETS not found")
        return None, None, None

    ws_start = ws_match.end() - 1  # points to the '{'
    ws_end = find_bracket_end(text, ws_start)

    # Search for "ap": inside that block
    block = text[ws_start:ws_end+1]
    ap_match = re.search(r'["\']ap["\']\s*:\s*\{', block)
    if not ap_match:
        print("ERROR: 'ap' key not found inside WORKSHEETS")
        return None, None, None

    ap_key_local_start = ap_match.start()  # where "ap": starts
    ap_brace_local = ap_match.end() - 1     # points to the '{' of ap's value
    ap_brace_abs = ws_start + ap_brace_local
    ap_end_abs = find_bracket_end(text, ap_brace_abs)

    # The full "ap":{...} span
    ap_span_start = ws_start + ap_key_local_start
    ap_span_end = ap_end_abs  # inclusive

    return ap_span_start, ap_span_end, ap_match.group(0)

def main():
    with open(WORKSHEETS_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    ap_start, ap_end, matched = find_ap_key(html)
    if ap_start is None:
        sys.exit(1)

    print(f"Found AP block at chars {ap_start}–{ap_end}")
    print(f"Replacing: {html[ap_start:ap_start+40]}...")

    new_ap = build_ap_block()
    new_html = html[:ap_start] + new_ap + html[ap_end+1:]

    # Quick sanity: count topics
    total = (len(AP_MATH) * len(AP_MATH[0]) +
             len(AP_SCIENCE) * len(AP_SCIENCE[0]) +
             len(AP_ELA) * len(AP_ELA[0]) +
             len(AP_HISTORY) * len(AP_HISTORY[0]) +
             len(AP_CS) * len(AP_CS[0]) +
             len(AP_HEALTH) * len(AP_HEALTH[0]))
    print(f"Total AP topics: {total}")

    with open(WORKSHEETS_PATH, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print("worksheets.html updated successfully!")

if __name__ == '__main__':
    main()
