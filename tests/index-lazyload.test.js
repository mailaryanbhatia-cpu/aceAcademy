/**
 * Smoke test for index.html's lazy-loaded practice-data.js (con #3 fix,
 * 2026-07-17): the homepage no longer blocks its initial render on the
 * 1.4MB practice-problem bank -- it's injected dynamically after first
 * paint, and render()/dcSidebarInit()/openQuiz() wait for it (with a
 * self-healing guard on render() specifically, since grade/subject links
 * can be clicked before the lazy load finishes).
 *
 * Requires a real HTTP server (not file:// or a fake https:// origin) so
 * that BOTH the dynamically-injected <script src="practice-data.js"> and
 * localStorage work correctly -- see the jsdom-testing gotcha in memory:
 * file:// is an opaque origin (blocks localStorage), and a fake https://
 * origin can't resolve relative script fetches without a real network.
 */
const path = require('path');
const http = require('http');
const fs = require('fs');
const { JSDOM } = require('jsdom');

const root = path.join(__dirname, '..');
const PORT = 8919;

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
    const dom = await JSDOM.fromURL(`http://localhost:${PORT}/index.html`, {
      runScripts: 'dangerously',
      resources: 'usable',
      pretendToBeVisual: true,
    });
    const errors = [];
    dom.window.addEventListener('error', (e) => {
      const msg = e.error ? e.error.message : e.message;
      // firebase failing to load is expected in this offline test env (no CDN access) -- unrelated to this fix.
      if (!/firebase/i.test(msg)) errors.push(msg);
    });
    const doc = dom.window.document;

    // 1. Immediately after load, the static parts of the page (hero, tool
    //    grid, nav) should already be present -- proving the lazy-loaded
    //    practice data isn't blocking the rest of the page.
    await new Promise((r) => setTimeout(r, 30));
    if (!doc.body.innerHTML || doc.body.innerHTML.length < 1000) {
      failures.push('Page body looks empty shortly after load -- lazy-load may be blocking initial render');
    }
    if (errors.length) {
      failures.push('Unexpected error(s) before practice-data.js finished loading: ' + errors.join('; '));
    }

    // 2. After the lazy load resolves, the Daily Challenge selects and the
    //    curriculum-browser's practice-sheet-bearing unit cards should populate.
    await new Promise((r) => setTimeout(r, 1500));
    const gradeOptions = doc.getElementById('dc-sel-grade')?.options.length || 0;
    if (gradeOptions === 0) {
      failures.push('dc-sel-grade never populated after the lazy load should have finished');
    }
    if (!doc.querySelector('.unit-card')) {
      failures.push('No .unit-card rendered after the lazy load should have finished (render() never ran?)');
    }
    if (errors.length) {
      failures.push('Unexpected error(s) after practice-data.js loaded: ' + errors.join('; '));
    }
  } catch (e) {
    failures.push('Test threw: ' + e.message);
  } finally {
    server.close();
  }

  if (failures.length) {
    console.error('[index.html lazy-load] FAILURES:');
    failures.forEach((f) => console.error('  - ' + f));
    process.exitCode = 1;
  } else {
    console.log('[index.html lazy-load] all smoke tests passed');
  }
})();
