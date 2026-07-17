/**
 * Smoke test for essaygrader.html's rule-based scoring engine (gradeEssay()).
 * Drives the real DOM: fills #essayText, clicks the real "Quick Grade"
 * button, then reads back the rendered score/rubric/feedback.
 */
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const root = path.join(__dirname, '..');

const STRONG_ESSAY = `
Standardized testing should be reduced in importance for college admissions because it fails to measure a student's true potential and disadvantages low-income students. This essay will argue that holistic admissions, which weigh grades, essays, and extracurriculars more heavily than test scores, produce fairer outcomes.

First, standardized tests correlate strongly with family income. According to research, students from wealthy families can afford test preparation courses and private tutors, artificially inflating their scores relative to their actual academic ability. For example, students in top income brackets score, on average, hundreds of points higher on the SAT than students from low-income families, even when their high school grades are comparable.

Furthermore, test scores measure a narrow set of skills rather than the broader qualities that predict college success. Studies show that high school GPA is a better predictor of college graduation rates than SAT scores. However, some critics argue that grades vary too much in rigor between schools to be compared fairly. Nevertheless, a combination of GPA, coursework rigor, and personal essays provides a more complete picture than a single test score.

In conclusion, colleges should deemphasize standardized testing in favor of a holistic review process. This would create a fairer admissions system that evaluates the whole student rather than their performance on a single Saturday morning exam.
`.trim();

async function loadPage() {
  const html = fs.readFileSync(path.join(root, 'essaygrader.html'), 'utf-8');
  const dom = new JSDOM(html, {
    url: 'https://academyacer.com/essaygrader.html',
    runScripts: 'dangerously',
    resources: 'usable',
    pretendToBeVisual: true,
  });
  // jsdom doesn't implement scrollIntoView (not a site bug -- a jsdom gap);
  // gradeEssay() calls it on the results panel after rendering.
  dom.window.HTMLElement.prototype.scrollIntoView = () => {};
  await new Promise((r) => setTimeout(r, 300));
  return dom;
}

(async () => {
  const failures = [];
  const dom = await loadPage();
  const doc = dom.window.document;

  try {
    doc.getElementById('essayText').value = STRONG_ESSAY;
    const gradeBtn = doc.querySelector('.ace-btn[onclick="gradeEssay()"]');
    if (!gradeBtn) throw new Error('Quick Grade button not found');
    gradeBtn.click();

    const resultsDisplay = doc.getElementById('results').style.display;
    if (resultsDisplay !== 'block') failures.push('Results panel did not become visible after grading');

    const totalText = doc.getElementById('totalScore').textContent;
    const m = totalText.match(/(\d+)\s*\/\s*100/);
    if (!m) failures.push(`totalScore text didn't match "N / 100" pattern: "${totalText}"`);
    else {
      const score = parseInt(m[1], 10);
      // This essay has a thesis, evidence phrases, 4 paragraphs, transitions,
      // a counterargument ("However, some critics argue"), and a conclusion --
      // it should score reasonably well, not near-zero.
      if (score < 60) failures.push(`Well-formed essay scored unexpectedly low: ${score}/100`);
      if (score > 100) failures.push(`Score exceeds 100: ${score}`);
    }

    const letter = doc.getElementById('letterGrade').textContent;
    if (!/^[A-F][+-]?$/.test(letter)) failures.push(`letterGrade isn't a valid letter grade: "${letter}"`);

    const rubricHtml = doc.getElementById('rubricGrid').innerHTML;
    if (!rubricHtml || !rubricHtml.includes('Thesis') || !rubricHtml.includes('Evidence')) {
      failures.push('rubricGrid missing expected category labels (Thesis/Evidence)');
    }

    const feedbackHtml = doc.getElementById('feedbackContent').innerHTML;
    if (!feedbackHtml || feedbackHtml.trim().length < 50) {
      failures.push('feedbackContent looks empty/too short after grading');
    }
  } catch (e) {
    failures.push('Grading a well-formed essay threw: ' + e.message);
  }

  // Weak essay (short, no thesis/evidence/transitions) should score notably lower.
  try {
    doc.getElementById('essayText').value = 'I think testing is bad. It is not fair. Some people do better than others. That is why we should not use tests. '.repeat(3);
    doc.querySelector('.ace-btn[onclick="gradeEssay()"]').click();
    const weakScore = parseInt(doc.getElementById('totalScore').textContent.match(/(\d+)/)[1], 10);
    if (weakScore >= 60) failures.push(`Weak/repetitive essay scored surprisingly high: ${weakScore}/100`);
  } catch (e) {
    failures.push('Grading a weak essay threw: ' + e.message);
  }

  if (failures.length) {
    console.error('[essaygrader.html] FAILURES:');
    failures.forEach((f) => console.error('  - ' + f));
    process.exitCode = 1;
  } else {
    console.log('[essaygrader.html] all smoke tests passed');
  }
})();
