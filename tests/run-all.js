/**
 * Runs every jsdom smoke test in this directory in a separate process (so a
 * crash in one test file can't take down the others or leak jsdom window
 * state between suites) and aggregates pass/fail across all of them.
 */
const { execFileSync } = require('child_process');
const path = require('path');

const tests = [
  'curriculum.test.js',
  'tutor.test.js',
  'essaygrader.test.js',
  'xp-system.test.js',
];

let anyFailed = false;

for (const t of tests) {
  console.log(`\n--- running ${t} ---`);
  try {
    const out = execFileSync(process.execPath, [path.join(__dirname, t)], { encoding: 'utf-8' });
    process.stdout.write(out);
  } catch (e) {
    anyFailed = true;
    if (e.stdout) process.stdout.write(e.stdout);
    if (e.stderr) process.stderr.write(e.stderr);
    console.error(`--- ${t} exited with a failure ---`);
  }
}

console.log('\n' + (anyFailed ? 'One or more functional test suites FAILED.' : 'All functional test suites passed.'));
process.exit(anyFailed ? 1 : 0);
