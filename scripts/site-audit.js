#!/usr/bin/env node
/**
 * site-audit.js — aceAcademy CI health check
 *
 * Runs the same checks that have been done manually by hand throughout this
 * project's history before every commit:
 *   1. Every inline <script> tag on every .html page must be valid JS
 *      (catches the "embedded </script> text truncates the real script tag"
 *      class of bug found in annotatedbib/cornellnotes/labreport/timeline.html,
 *      and the "orphaned function fragment" bug found in curriculum.html).
 *   2. Every internal href="*.html" link must point to a file that exists.
 *
 * Exits non-zero (failing CI) if any problems are found.
 */

const fs = require('fs');
const path = require('path');
const os = require('os');
const { execSync } = require('child_process');

const root = process.cwd();
const htmlFiles = fs.readdirSync(root).filter(f => f.endsWith('.html'));

let failures = 0;

// ── 1. Inline <script> syntax check ─────────────────────────────────────────
const scriptRe = /<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g;
for (const file of htmlFiles) {
  const html = fs.readFileSync(path.join(root, file), 'utf-8');
  let m;
  let i = 0;
  scriptRe.lastIndex = 0;
  while ((m = scriptRe.exec(html)) !== null) {
    const code = m[1];
    if (code.trim()) {
      const tmp = path.join(os.tmpdir(), `audit_${file.replace(/[^a-z0-9.]/gi, '_')}_${i}.js`);
      fs.writeFileSync(tmp, code);
      try {
        execSync(`node --check "${tmp}"`, { stdio: 'pipe' });
      } catch (e) {
        console.error(`[SYNTAX ERROR] ${file} (inline script #${i}):\n${(e.stderr || '').toString().trim()}`);
        failures++;
      } finally {
        fs.unlinkSync(tmp);
      }
    }
    i++;
  }
}

// ── 2. Broken internal link check ───────────────────────────────────────────
const htmlSet = new Set(htmlFiles);
const hrefRe = /href=["']([a-zA-Z0-9_\-]+\.html)["']/g;
for (const file of htmlFiles) {
  const html = fs.readFileSync(path.join(root, file), 'utf-8');
  let m;
  hrefRe.lastIndex = 0;
  while ((m = hrefRe.exec(html)) !== null) {
    if (!htmlSet.has(m[1])) {
      console.error(`[BROKEN LINK] ${file} links to missing file: ${m[1]}`);
      failures++;
    }
  }
}

console.log(`\nChecked ${htmlFiles.length} HTML files.`);
if (failures > 0) {
  console.error(`\n${failures} problem(s) found.`);
  process.exit(1);
} else {
  console.log('All checks passed.');
  process.exit(0);
}
