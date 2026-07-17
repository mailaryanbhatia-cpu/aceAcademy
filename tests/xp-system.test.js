/**
 * Smoke test for xp-system.js (window.AceXP). Unlike tutor.html/curriculum.html,
 * this file's public API is genuinely attached to `window.AceXP` as real object
 * methods (not top-level `let`/`const` bindings) -- so calling them directly is
 * safe and isn't subject to the jsdom window.X gotcha documented in memory.
 */
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const root = path.join(__dirname, '..');

function freshWindow() {
  const dom = new JSDOM('<!doctype html><html><body></body></html>', {
    url: 'https://academyacer.com/tools.html',
    runScripts: 'dangerously',
  });
  const code = fs.readFileSync(path.join(root, 'xp-system.js'), 'utf-8');
  dom.window.eval(code);
  return dom;
}

(async () => {
  const failures = [];

  // ── Test 1: fresh state starts at 0 XP / level 1 / 0-day streak ──
  try {
    const dom = freshWindow();
    const { AceXP } = dom.window;
    if (typeof AceXP !== 'object') throw new Error('window.AceXP was not created');
    if (AceXP.getTotalXP() !== 0) failures.push(`Fresh state getTotalXP() should be 0, got ${AceXP.getTotalXP()}`);
    const lv = AceXP.getLevel();
    if (lv.level !== 1) failures.push(`Fresh state level should be 1, got ${lv.level}`);
    if (lv.xpForNextLevel !== 100) failures.push(`Level 1 should need 100 XP to level up, got ${lv.xpForNextLevel}`);
  } catch (e) { failures.push('Fresh-state test threw: ' + e.message); }

  // ── Test 2: recordActivity accumulates XP correctly ──
  try {
    const dom = freshWindow();
    const { AceXP } = dom.window;
    const result = AceXP.recordActivity(40, 'Test activity');
    if (AceXP.getTotalXP() !== 40) failures.push(`After +40 XP, getTotalXP() should be 40, got ${AceXP.getTotalXP()}`);
    if (result.total !== 40) failures.push(`recordActivity() return value total should be 40, got ${result.total}`);
    AceXP.recordActivity(70, 'Another activity');
    if (AceXP.getTotalXP() !== 110) failures.push(`After +40 then +70, total should be 110, got ${AceXP.getTotalXP()}`);
  } catch (e) { failures.push('XP accumulation test threw: ' + e.message); }

  // ── Test 3: level-up threshold math (100 XP -> level 2, 250 -> level 3) ──
  try {
    const dom = freshWindow();
    const { AceXP } = dom.window;
    AceXP.recordActivity(100, 'reach level 2');
    let lv = AceXP.getLevel();
    if (lv.level !== 2) failures.push(`100 total XP should be level 2, got level ${lv.level}`);
    AceXP.recordActivity(150, 'reach level 3'); // 100 + 150 = 250, level 2 needs 150 more (100-250), level 3 starts at 250
    lv = AceXP.getLevel();
    if (lv.level !== 3) failures.push(`250 total XP should be level 3, got level ${lv.level}`);
    if (lv.xpIntoLevel !== 0) failures.push(`At exactly 250 XP, xpIntoLevel should be 0, got ${lv.xpIntoLevel}`);
  } catch (e) { failures.push('Level-up threshold test threw: ' + e.message); }

  // ── Test 4: streak starts at 1 after first activity of the day, stays 1 on a second activity same day ──
  try {
    const dom = freshWindow();
    const { AceXP } = dom.window;
    const r1 = AceXP.recordActivity(10, 'day 1 activity A');
    if (r1.streak.current !== 1) failures.push(`First-ever activity should set streak to 1, got ${r1.streak.current}`);
    const r2 = AceXP.recordActivity(10, 'day 1 activity B'); // same day, should NOT double-increment
    if (r2.streak.current !== 1) failures.push(`Second activity same day should keep streak at 1, got ${r2.streak.current}`);
    const st = AceXP.getStreak();
    if (st.current !== 1 || st.longest !== 1) failures.push(`getStreak() mismatch after same-day activities: ${JSON.stringify(st)}`);
  } catch (e) { failures.push('Streak same-day test threw: ' + e.message); }

  // ── Test 5: getHistory() returns an array and doesn't throw on a fresh window ──
  try {
    const dom = freshWindow();
    const { AceXP } = dom.window;
    const hist = AceXP.getHistory();
    if (!Array.isArray(hist)) failures.push(`getHistory() should return an array, got ${typeof hist}`);
    AceXP.recordActivity(5, 'log check');
    const hist2 = AceXP.getHistory();
    if (hist2.length !== 1) failures.push(`After one activity, history should have 1 entry, got ${hist2.length}`);
  } catch (e) { failures.push('History test threw: ' + e.message); }

  if (failures.length) {
    console.error('[xp-system.js] FAILURES:');
    failures.forEach((f) => console.error('  - ' + f));
    process.exitCode = 1;
  } else {
    console.log('[xp-system.js] all smoke tests passed (5/5)');
  }
})();
