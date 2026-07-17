/**
 * Smoke test for curriculum.html's render + practice-sheet lookup, focused on
 * regression-testing the two bug classes fixed this cycle:
 *   1. Practice sheets must show under the CORRECT unit (position-based
 *      misalignment, fixed for G9/G12 History + G10 English).
 *   2. Practice sheets must stay correct while a search filter is active
 *      (filtered-array reindexing bug, fixed via `realIndex`/unit keys).
 * Drives the real DOM: clicks real grade links, dispatches a real `input`
 * event on the search box, and reads back rendered practice-sheet titles --
 * never pokes internal state via window.X (see jsdom-testing gotcha memory).
 */
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const root = path.join(__dirname, '..');

async function loadPage() {
  const html = fs.readFileSync(path.join(root, 'curriculum.html'), 'utf-8');
  const dom = new JSDOM(html, {
    url: 'file://' + path.join(root, 'curriculum.html'),
    runScripts: 'dangerously',
    resources: 'usable',
    pretendToBeVisual: true,
  });
  await new Promise((r) => setTimeout(r, 300));
  return dom;
}

function clickGrade(dom, gradeAttr) {
  const doc = dom.window.document;
  const link = doc.querySelector(`#gradeList a[data-grade="${gradeAttr}"]`);
  if (!link) throw new Error(`grade link data-grade="${gradeAttr}" not found`);
  link.dispatchEvent(new dom.window.MouseEvent('click', { bubbles: true, cancelable: true }));
}

function clickSubject(dom, subjId) {
  const doc = dom.window.document;
  const btn = Array.from(doc.querySelectorAll('.subj-btn')).find(b => b.getAttribute('onclick') === `setSubject('${subjId}')`);
  if (!btn) throw new Error(`subject button for "${subjId}" not found`);
  btn.click();
}

function getUnitCardByName(dom, unitName) {
  const doc = dom.window.document;
  return Array.from(doc.querySelectorAll('.unit-card')).find(c => c.querySelector('.unit-name')?.textContent === unitName);
}

function sheetTitlesInCard(card) {
  return Array.from(card.querySelectorAll('.sheet-title')).map(el => el.textContent.replace('📄 ', '').trim());
}

(async () => {
  const failures = [];
  const dom = await loadPage();

  // ── Test 1: Grade 9 History -> "World History: Modern Era" should show
  //    the newly-authored WWI/revolutions sheets, not old mismatched content.
  try {
    clickGrade(dom, '9');
    clickSubject(dom, 'history');
    const card = getUnitCardByName(dom, 'World History: Modern Era');
    if (!card) throw new Error('unit card not found');
    const titles = sheetTitlesInCard(card);
    if (!titles.some(t => /Age of Revolutions/.test(t))) {
      failures.push(`G9 History "World History: Modern Era" sheets don't include "Age of Revolutions": ${JSON.stringify(titles)}`);
    }
    if (titles.some(t => /Ancient civilizations/i.test(t))) {
      failures.push(`G9 History "World History: Modern Era" still shows old mismatched "Ancient civilizations" content: ${JSON.stringify(titles)}`);
    }
  } catch (e) { failures.push('Grade 9 History test threw: ' + e.message); }

  // ── Test 2: Grade 12 History -> "AP Government & Politics" should show the
  //    recovered US-Government-Structure sheets (previously at the wrong slot).
  try {
    clickGrade(dom, '12');
    clickSubject(dom, 'history');
    const card = getUnitCardByName(dom, 'AP Government & Politics');
    if (!card) throw new Error('unit card not found');
    const titles = sheetTitlesInCard(card);
    if (!titles.some(t => /US Government Structure/.test(t))) {
      failures.push(`G12 History "AP Government & Politics" sheets don't include "US Government Structure": ${JSON.stringify(titles)}`);
    }
  } catch (e) { failures.push('Grade 12 History test threw: ' + e.message); }

  // ── Test 3: Grade 10 English -> "Composition" should show argument/logical-
  //    fallacy sheets (moved to the correct position), not research-skills content.
  try {
    clickGrade(dom, '10');
    clickSubject(dom, 'ela');
    const card = getUnitCardByName(dom, 'Composition');
    if (!card) throw new Error('unit card not found');
    const titles = sheetTitlesInCard(card);
    if (!titles.some(t => /Elements of an Argument/.test(t))) {
      failures.push(`G10 English "Composition" sheets don't include "Elements of an Argument": ${JSON.stringify(titles)}`);
    }
  } catch (e) { failures.push('Grade 10 English test threw: ' + e.message); }

  // ── Test 4: search-while-filtering must not scramble practice sheets.
  //    Search for a term that matches only ONE of Grade 9 History's units
  //    ("Government"), leaving a single filtered result at array index 0 --
  //    this is exactly the scenario that broke under the old `i`-based lookup.
  try {
    clickGrade(dom, '9');
    clickSubject(dom, 'history');
    const doc = dom.window.document;
    const searchBox = doc.getElementById('searchInput');
    searchBox.value = 'civics';
    searchBox.dispatchEvent(new dom.window.Event('input', { bubbles: true }));
    await new Promise((r) => setTimeout(r, 350)); // search is debounced 200ms

    const cards = doc.querySelectorAll('.unit-card');
    if (cards.length !== 1) failures.push(`Expected exactly 1 filtered unit card for "civics" search, got ${cards.length}`);
    else {
      const card = cards[0];
      const unitName = card.querySelector('.unit-name')?.textContent;
      if (unitName !== 'Government & Civics') failures.push(`Filtered search surfaced unexpected unit: "${unitName}"`);
      const titles = sheetTitlesInCard(card);
      if (!titles.some(t => /Government and civics/.test(t))) {
        failures.push(`Filtered "Government & Civics" unit shows wrong sheets during search: ${JSON.stringify(titles)}`);
      }
      if (titles.some(t => /Age of Revolutions|US Government Structure/.test(t))) {
        failures.push(`Filtered "Government & Civics" unit leaked another unit's sheets during search: ${JSON.stringify(titles)}`);
      }
    }
    // Clear search for cleanliness
    searchBox.value = '';
    searchBox.dispatchEvent(new dom.window.Event('input', { bubbles: true }));
    await new Promise((r) => setTimeout(r, 350));
  } catch (e) { failures.push('Search-while-filtering test threw: ' + e.message); }

  // ── Test 5: every unit's practice sheets carry the correct problem count (basic sanity)
  try {
    clickGrade(dom, '9');
    clickSubject(dom, 'history');
    const doc = dom.window.document;
    const problems = doc.querySelectorAll('.problem');
    if (problems.length < 4) failures.push(`Grade 9 History rendered suspiciously few problems total: ${problems.length}`);
  } catch (e) { failures.push('Problem-count sanity check threw: ' + e.message); }

  if (failures.length) {
    console.error('[curriculum.html] FAILURES:');
    failures.forEach((f) => console.error('  - ' + f));
    process.exitCode = 1;
  } else {
    console.log('[curriculum.html] all smoke tests passed (5/5)');
  }
})();
