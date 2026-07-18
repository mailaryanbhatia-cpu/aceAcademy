/**
 * Site-wide load-time error check (con #5, 2026-07-17): loads every HTML
 * page on the site in jsdom and fails if ANY page throws an uncaught JS
 * error during its initial script execution.
 *
 * Why this exists: this codebase has had the SAME bug recur at least 3
 * times across its history -- a function/variable used at page-load time
 * (not inside a click handler) that's declared in a LATER <script> tag
 * than the one that calls it. Function/const/let declarations only hoist
 * within their own <script> block, not across tags, so the call throws a
 * ReferenceError, which silently kills every remaining line in that
 * script block. The getTipBtn bug (fixed 2026-07-17) is the most recent
 * instance: it broke the homepage's Daily Challenge sidebar, hero
 * greeting, and stats widget all at once, with no visible error unless
 * you opened devtools.
 *
 * Rather than trying to statically analyze declaration order across
 * <script> tags (fragile -- would need a real scope-aware JS parser to do
 * correctly) or forcing every page onto a single monolithic <script> tag
 * (a much bigger, riskier rewrite with its own collision risks), this
 * takes the pragmatic route: actually execute every page and check
 * whether it throws. This catches this bug class regardless of its exact
 * cause (script order, a typo'd identifier, a removed function nobody
 * updated the caller for, etc.) and covers all pages on the site, not
 * just the handful with bespoke jsdom test files in tests/.
 *
 * IMPORTANT jsdom gotcha #1: attaching a `window.addEventListener('error',
 * ...)` AFTER `JSDOM.fromURL(...)`/`new JSDOM(...)` resolves is too late to
 * catch errors thrown during the page's initial *synchronous* script
 * execution -- by the time control returns to your code, every
 * non-deferred <script> tag has already run. (tests/*.test.js use that
 * pattern safely because they're only checking for errors during a later
 * async step, e.g. after a lazy-loaded data file resolves -- not during
 * initial load.) Fixed here by passing a `VirtualConsole` and listening for
 * its 'jsdomError' event, registered before the DOM is even constructed, so
 * nothing can be missed.
 *
 * IMPORTANT jsdom gotcha #2 (the one that cost the most time to track down):
 * several tool-hub pages (aptools/assignment/ela/history/notetaker/
 * organizer/quizzes/tools/completion.html) use `<iframe src="child.html"
 * onload="hideLoader()">`, where hideLoader() is declared further down in
 * the SAME <script> tag. This is 100% safe in a real browser: an iframe's
 * onload only fires after its sub-document finishes loading, which is
 * always asynchronous (goes through the network/task-queue stack, even for
 * a cached same-origin fetch) -- so by the time onload can possibly fire,
 * the parent page's own <script> tags (including the one hoisting
 * hideLoader) have already finished their synchronous run. jsdom, however,
 * doesn't reliably preserve that ordering guarantee when it actually loads
 * and executes a same-origin iframe's HTML/JS -- it can fire the onload
 * before the parent's trailing <script> tag runs, producing a
 * "hideLoader is not defined" error that would never happen in production.
 * Rather than chase jsdom's iframe-timing semantics (or worse, leave 9
 * known-noisy pages permanently on an exceptions list, which would hide
 * REAL future regressions on those same pages), this loads each page from
 * an in-memory HTML string with every <iframe src="*.html"> rewritten to
 * `about:blank` first. Nested iframe content isn't this check's concern
 * anyway -- each iframe target gets checked on its own, in the same run,
 * as its own top-level page.
 */
const fs = require('fs');
const path = require('path');
const http = require('http');
const { JSDOM, VirtualConsole } = require('jsdom');

const root = path.join(__dirname, '..');
const PORT = 8931;

// A real (local-only) HTTP server so relative <script src>/<link> resource
// resolution behaves exactly like a real page load, just against this
// checkout's files instead of the deployed site.
function startServer() {
  const server = http.createServer((req, res) => {
    const urlPath = decodeURIComponent(req.url.split('?')[0]);
    const filePath = path.join(root, urlPath === '/' ? '/index.html' : urlPath);
    fs.readFile(filePath, (err, data) => {
      if (err) { res.writeHead(404); res.end(); return; }
      res.writeHead(200);
      res.end(data);
    });
  });
  return new Promise((resolve) => server.listen(PORT, () => resolve(server)));
}

function listHtmlFiles(dir, base = dir) {
  let out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === 'node_modules' || entry.name === 'data-source' || entry.name.startsWith('.')) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out = out.concat(listHtmlFiles(full, base));
    else if (entry.name.endsWith('.html')) out.push(path.relative(base, full));
  }
  return out;
}

// Neutralize nested iframe loading (see gotcha #2 above) -- only touches the
// src attribute value, not onload or anything else, so the parent page's own
// code under test is completely unmodified.
function neutralizeIframes(html) {
  return html.replace(
    /(<iframe\b[^>]*\bsrc\s*=\s*)(["'])(?!about:blank)([^"']*\.html[^"']*)\2/gi,
    '$1$2about:blank$2'
  );
}

// Errors that occur only because this sandboxed/offline test environment
// can't reach external CDNs (Google Fonts, Firebase, cdnjs, etc.) or hit a
// jsdom API gap (matchMedia, canvas 2D context, Notification -- all real,
// standard browser APIs that jsdom simply doesn't implement). These occur
// identically on every page regardless of this codebase's own code and are
// not the script-order/undefined-symbol bug class this check exists to
// catch.
const REALLY_BENIGN = [
  /firebase/i,
  /Not implemented/i,
  /^Could not load (style|link|script):/i,
  /window\.matchMedia is not a function/,
  /Cannot read properties of null \(reading '(clearRect|scale|getImageData|fillStyle)'\)/,
  /Cannot set properties of null \(setting '(fillStyle|innerHTML)'\)/,
  /Notification is not defined/,
  /^Could not parse CSS stylesheet$/,
];

async function checkPage(relPath) {
  const jsdomErrors = [];
  const virtualConsole = new VirtualConsole();
  virtualConsole.on('jsdomError', (err) => {
    const msg = err && err.message ? err.message : String(err);
    if (!REALLY_BENIGN.some((p) => p.test(msg))) jsdomErrors.push(msg);
  });

  const absPath = path.join(root, relPath);
  let html = fs.readFileSync(absPath, 'utf-8');
  html = neutralizeIframes(html);

  let dom;
  try {
    dom = new JSDOM(html, {
      url: `http://localhost:${PORT}/${relPath}`,
      runScripts: 'dangerously',
      resources: 'usable',
      pretendToBeVisual: true,
      virtualConsole,
    });
    // let a short async settle so setTimeout(0)/microtask-queued code (like
    // the lazy-load .then() chains) gets a chance to run and surface errors too
    await new Promise((r) => setTimeout(r, 250));
  } catch (e) {
    if (!REALLY_BENIGN.some((p) => p.test(e.message))) jsdomErrors.push('threw during load: ' + e.message);
  } finally {
    if (dom) dom.window.close();
  }
  return jsdomErrors;
}

async function main() {
  const server = await startServer();
  const pages = listHtmlFiles(root).sort();
  const only = process.argv[2]; // optional: check a single page, for fast iteration
  const targets = only ? pages.filter((p) => p === only) : pages;
  const failures = {};

  for (const p of targets) {
    const errs = await checkPage(p);
    if (errs.length) failures[p] = errs;
  }
  server.close();

  const failedPages = Object.keys(failures);
  if (failedPages.length) {
    console.error(`\n${failedPages.length}/${targets.length} page(s) threw an uncaught JS error during initial load:\n`);
    for (const p of failedPages) {
      console.error(`  ${p}:`);
      for (const e of failures[p]) console.error(`    - ${e}`);
    }
    console.error('\nThis is almost always a function/variable referenced before it exists --');
    console.error('most often because it\'s declared in a LATER <script> tag than the one that');
    console.error('calls it (declarations only hoist within their own <script> block, not across');
    console.error('tags). Move the missing declaration earlier: into the SAME <script> block as');
    console.error('its first caller, physically before that call.');
    process.exitCode = 1;
  } else {
    console.log(`OK: all ${targets.length} page(s) loaded with zero uncaught JS errors.`);
  }
}

main();
