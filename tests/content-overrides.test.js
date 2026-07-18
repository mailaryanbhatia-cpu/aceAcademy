/**
 * Smoke test for the hybrid content-management override system (con #4
 * follow-up, 2026-07-19): content-overrides.js + curriculum.html's render()
 * merging in an admin-added unit title/topics/extra-practice-sheets.
 *
 * Bypasses the real Firestore network call (unreachable in this offline
 * test) by directly populating window._contentOverrides -- the same shape
 * content-overrides.js would populate it with after a real fetch -- and
 * driving the UI via the real setGrade()/setSubject() functions (per the
 * jsdom-testing gotcha in memory: assigning window.currentGrade directly
 * silently no-ops against the page's top-level `let currentGrade`).
 */
const path = require('path');
const http = require('http');
const fs = require('fs');
const { JSDOM } = require('jsdom');

const root = path.join(__dirname, '..');
const PORT = 8953;

function startServer() {
  const server = http.createServer((req, res) => {
    const urlPath = req.url.split('?')[0];
    const filePath = path.join(root, decodeURIComponent(urlPath === '/' ? '/index.html' : urlPath));
    fs.readFile(filePath, (err, data) => {
      if (err) { res.writeHead(404); res.end(); return; }
      res.writeHead(200);
      res.end(data);
    });
  });
  return new Promise((resolve) => server.listen(PORT, () => resolve(server)));
}

(async () => {
  const failures = [];
  const server = await startServer();

  try {
    const dom = await JSDOM.fromURL(`http://localhost:${PORT}/curriculum.html`, {
      runScripts: 'dangerously',
      resources: 'usable',
      pretendToBeVisual: true,
    });
    const { window } = dom;
    await new Promise((r) => setTimeout(r, 300));

    const UNIT_KEY = 'k-math-counting-and-number-sense';
    window._contentOverrides[UNIT_KEY] = {
      unit: 'OVERRIDDEN TITLE FOR TESTING',
      topics: ['Custom topic one', 'Custom topic two'],
      extraPracticeSheets: [{ title: 'Admin Added Sheet', problems: [{ q: '1+1=?', a: '2' }] }],
    };
    window.setGrade('k');
    window.setSubject('math');
    await new Promise((r) => setTimeout(r, 100));

    const html = window.document.getElementById('mainContent').innerHTML;

    if (!html.includes('OVERRIDDEN TITLE FOR TESTING')) {
      failures.push('Overridden unit title did not render');
    }
    if (!html.includes('Custom topic one') || !html.includes('Custom topic two')) {
      failures.push('Overridden topics list did not render');
    }
    if (!html.includes('Admin Added Sheet')) {
      failures.push('Admin-added extra practice sheet did not render');
    }
    if (html.includes('Counting &amp; Number Sense') || html.includes('Counting & Number Sense')) {
      failures.push('Original (pre-override) unit title still rendered alongside the override');
    }

    // 2nd check: a unit with NO override should render completely normally
    // (this system should be a no-op for the other 300+ units).
    window._contentOverrides = {};
    window.setGrade('k');
    window.setSubject('math');
    await new Promise((r) => setTimeout(r, 100));
    const html2 = window.document.getElementById('mainContent').innerHTML;
    if (!html2.includes('Counting') || !html2.includes('Number Sense')) {
      failures.push('Unit rendered incorrectly once overrides were cleared -- original content should come back');
    }
  } catch (e) {
    failures.push('Test threw: ' + e.message);
  } finally {
    server.close();
  }

  if (failures.length) {
    console.error('[content-overrides] FAILURES:');
    failures.forEach((f) => console.error('  - ' + f));
    process.exitCode = 1;
  } else {
    console.log('[content-overrides] all smoke tests passed');
  }
})();
