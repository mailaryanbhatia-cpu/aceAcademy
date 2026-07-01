#!/usr/bin/env python3
import pathlib, re

t = pathlib.Path('/sessions/admiring-stoic-pascal/mnt/outputs/tests.html').read_text(encoding='utf-8')

# Find Grade 10 block (between "10": and "11":)
g10_start = t.index('"10":')
g11_start = t.index('"11":')
g10block = t[g10_start:g11_start]

# Count Puritan occurrences before fix
before = g10block.count('Puritan')
print(f'Puritan occurrences in G10 block before: {before}')

# Replace the remaining "Which is NOT an example of Puritan literature?" question
old_q = ('"Which is NOT an example of Puritan literature?", '
         '"choices": ["Something that doesn\'t fit Puritan literature", '
         '"A classic example of Puritan literature", '
         '"A simple instance of Puritan literature", '
         '"A complex use of Puritan liter')
# Use regex to get the full object
pattern = r'"Which is NOT an example of Puritan literature\?"[^}]+"correct":\s*\d+[^}]*"exp":\s*"[^"]*"'
new_q = ('"Which is NOT an example of classical Greek literature?", '
         '"choices": ["A Renaissance-era Italian painting", '
         '"Homer\'s Iliad", '
         '"Sophocles\'s Antigone", '
         '"Plato\'s Republic"], '
         '"correct": 0, '
         '"exp": "The Renaissance painting is not ancient Greek literature. Homer, Sophocles, and Plato are all classical Greek literary figures."')

fixed_block, n = re.subn(pattern, new_q, g10block)
print(f'Replacements made: {n}')

after = fixed_block.count('Puritan')
print(f'Puritan occurrences in G10 block after: {after}')

t = t[:g10_start] + fixed_block + t[g11_start:]

# Verify the curriculum fix too
c = pathlib.Path('/sessions/admiring-stoic-pascal/mnt/outputs/curriculum.html').read_text(encoding='utf-8')
earth_check = "Earth's history and deep time" in c
print(f"\nCurriculum G8 Earth History check: {earth_check}")
if not earth_check:
    print("  Searching for actual text...")
    idx = c.find("Earth History & Space")
    print(f"  Found at {idx}: {c[idx:idx+200]}")

pathlib.Path('/sessions/admiring-stoic-pascal/mnt/outputs/tests.html').write_text(t, encoding='utf-8')
print('\nSaved tests.html')
