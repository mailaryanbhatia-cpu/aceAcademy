/**
 * Smoke test for tutor.html's non-AI (canned/rule-based) chat tutor.
 *
 * Drives the page exactly like a user would -- sets the real #inputBox
 * textarea value and clicks the real send button -- rather than poking
 * internal state via window.X, per the jsdom-testing gotcha documented in
 * memory (top-level `let`/`const` in a classic <script> tag do NOT become
 * window properties, so window.X = ... silently no-ops and produces a
 * false-positive pass).
 */
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const root = path.join(__dirname, '..');

async function loadPage() {
  const html = fs.readFileSync(path.join(root, 'tutor.html'), 'utf-8');
  const dom = new JSDOM(html, {
    url: 'file://' + path.join(root, 'tutor.html'),
    runScripts: 'dangerously',
    resources: 'usable',
    pretendToBeVisual: true,
  });
  // Let the inline <script> tags finish executing AND window.onload's delayed
  // welcome-message sequence (400ms + 900ms of setTimeouts) fully complete --
  // otherwise the welcome message can land in the middle of a test question's
  // exchange and get mistaken for the actual reply.
  await new Promise((r) => setTimeout(r, 1700));
  return dom;
}

async function ask(dom, text) {
  const doc = dom.window.document;
  const input = doc.getElementById('inputBox');
  const sendBtn = doc.querySelector('.send-btn');
  if (!input || !sendBtn) throw new Error('inputBox or send button not found');

  const before = doc.getElementById('messages').children.length;
  input.value = text;
  sendBtn.click();
  // sendMessage() awaits a 350-700ms artificial "typing" delay before rendering.
  await new Promise((r) => setTimeout(r, 900));
  const msgs = doc.getElementById('messages');
  const after = msgs.children.length;
  if (after <= before) throw new Error(`No new message rendered after asking "${text}"`);
  const acerMsgs = Array.from(msgs.children).filter((el) => el.classList.contains('acer') && el.id !== 'typ');
  const lastBubble = acerMsgs[acerMsgs.length - 1].querySelector('.bubble');
  return lastBubble ? lastBubble.textContent : '';
}

(async () => {
  const failures = [];
  const dom = await loadPage();

  // 1. Greeting chip should produce a response containing "photosynthesis".
  try {
    const reply = await ask(dom, 'What is photosynthesis and how does it work?');
    if (!/photosynthes/i.test(reply)) failures.push(`Photosynthesis question got an unrelated reply: "${reply.slice(0, 120)}..."`);
  } catch (e) { failures.push('Photosynthesis question threw: ' + e.message); }

  // 2. A simple linear equation should be solved (guided/direct math mode).
  try {
    const reply = await ask(dom, '3x + 5 = 20');
    // 3x + 5 = 20  =>  x = 5
    if (!/\b5\b/.test(reply)) failures.push(`Equation 3x+5=20 reply didn't mention the answer (5): "${reply.slice(0, 200)}..."`);
  } catch (e) { failures.push('Equation question threw: ' + e.message); }

  // 3. A greeting should get a greeting-shaped reply, not a fallback/empty one.
  try {
    const reply = await ask(dom, 'hi there');
    if (!reply || reply.trim().length < 5) failures.push(`Greeting got a suspiciously short/empty reply: "${reply}"`);
  } catch (e) { failures.push('Greeting threw: ' + e.message); }

  // 4. Grade switch should not throw and should produce an acknowledgement message.
  try {
    const doc = dom.window.document;
    const before = doc.getElementById('messages').children.length;
    const sel = doc.getElementById('gradeSelect');
    sel.value = '9';
    sel.dispatchEvent(new dom.window.Event('change', { bubbles: true }));
    await new Promise((r) => setTimeout(r, 100));
    const after = doc.getElementById('messages').children.length;
    if (after <= before) failures.push('Switching grade did not add an acknowledgement message');
  } catch (e) { failures.push('Grade switch threw: ' + e.message); }

  if (failures.length) {
    console.error('[tutor.html] FAILURES:');
    failures.forEach((f) => console.error('  - ' + f));
    process.exitCode = 1;
  } else {
    console.log('[tutor.html] all smoke tests passed (4/4)');
  }
})();
