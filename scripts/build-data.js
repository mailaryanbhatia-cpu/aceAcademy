/**
 * Rebuilds the 9 large "-data.js" files at the repo root from their
 * human-readable originals in data-source/.
 *
 * Why this exists (con #4, 2026-07-17): those 9 files were minified in
 * place on 2026-07-17 to cut total site size (~9.9MB -> ~8.98MB), which
 * meant the only copies left on disk were single-line and effectively
 * impossible to hand-edit. This script restores a real "source of truth":
 * data-source/*.js holds the readable originals (arrays/objects, one
 * entry per line), and this script regenerates the minified files that
 * pages actually <script src> load from them.
 *
 * Workflow: edit data-source/<file>.js like any normal file, then run
 * `npm run build:data` to regenerate the root-level minified copy before
 * committing. Never hand-edit the root-level minified files directly --
 * `npm run verify:data` (part of `npm test`) will catch drift between
 * data-source/ and the shipped files and fail CI if they diverge.
 *
 * Minification settings match the original 2026-07-17 minification pass
 * exactly: compress and mangle both OFF. This is deliberate, not an
 * oversight -- these files are loaded as classic (non-module) <script>
 * tags, and every one of them assigns to a top-level `const`/`let`
 * (WORKSHEETS, PRACTICE, CURRICULUM, TIPS, CHEAT_SHEETS, FORMULAS, etc.)
 * that OTHER <script> tags read as globals later in the page. Enabling
 * mangle would rename those top-level bindings and silently break every
 * page that depends on them; enabling compress risks other AST-level
 * rewrites with the same class of risk. Stripping whitespace/comments
 * only (what compress:false, mangle:false gives you) is the entire size
 * win worth having here -- these are data files, not logic, so there's no
 * dead-code-elimination or algebraic-simplification upside to chase.
 */
const fs = require('fs');
const path = require('path');
const { minify } = require('terser');

const root = path.join(__dirname, '..');
const sourceDir = path.join(root, 'data-source');

const FILES = [
  'curriculum-browser-data.js',
  'curriculum-data.js',
  'flashcards-data.js',
  'index-reference-data.js',
  'language-data.js',
  'practice-data.js',
  'tests-data.js',
  'tutor-kb-data.js',
  'worksheets-data.js',
];

async function buildOne(name) {
  const srcPath = path.join(sourceDir, name);
  const outPath = path.join(root, name);
  const code = fs.readFileSync(srcPath, 'utf-8');
  const result = await minify(code, { compress: false, mangle: false });
  if (!result.code) throw new Error(`terser produced no output for ${name}`);
  fs.writeFileSync(outPath, result.code);
  return { name, sourceBytes: code.length, outBytes: result.code.length };
}

async function main() {
  const checkOnly = process.argv.includes('--check');
  const results = [];
  for (const name of FILES) {
    const before = checkOnly ? fs.readFileSync(path.join(root, name), 'utf-8') : null;
    const r = await buildOne(name);
    results.push(r);
    if (checkOnly) {
      const after = fs.readFileSync(path.join(root, name), 'utf-8');
      if (before !== after) {
        console.error(`DRIFT DETECTED: ${name} differs from data-source/${name} after rebuild.`);
        console.error(`  This means someone edited the root-level ${name} directly, or edited`);
        console.error(`  data-source/${name} without running "npm run build:data" and committing`);
        console.error(`  the result. Fix: run "npm run build:data", review the diff, and commit`);
        console.error(`  both data-source/${name} and the regenerated ${name} together.`);
        // Restore the committed version so --check is non-destructive.
        fs.writeFileSync(path.join(root, name), before);
        process.exitCode = 1;
      }
    }
  }
  if (!checkOnly) {
    console.log('Rebuilt from data-source/:');
    for (const r of results) {
      console.log(`  ${r.name}: ${r.sourceBytes} -> ${r.outBytes} bytes`);
    }
  } else if (process.exitCode !== 1) {
    console.log('OK: all 9 data files match their data-source/ originals (no drift).');
  }
}

main();
