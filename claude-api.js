/**
 * claude-api.js  —  aceAcademy AI helper (Gemini-backed)
 *
 * Priority:
 *   1. Firebase Cloud Function (aiChat) — no student key needed, server-side key
 *   2. Direct Gemini API — student's own key stored in localStorage (fallback only)
 *
 * Usage:
 *   await aceAI.call(userPrompt, systemPrompt, maxTokens)  → string
 *   await aceAI.stream(userPrompt, systemPrompt, maxTokens, onChunk)  → void
 *   await aceAI.run(asyncFn)  → catches NO_KEY, prompts, retries
 *
 * (File name kept as claude-api.js for compatibility with existing <script>
 * tags/history; the actual provider is now Google Gemini, not Anthropic.)
 */
(function(){
  'use strict';

  const KEY_LS   = 'ace_gemini_key';
  const MODEL    = 'gemini-3.5-flash';
  const ENDPOINT = `https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent`;

  // ── Key management ──────────────────────────────────────────────────────────
  function getKey()   { return localStorage.getItem(KEY_LS) || ''; }
  function hasKey()   { return !!getKey(); }
  function setKey(k)  { localStorage.setItem(KEY_LS, k); }
  function clearKey() { localStorage.removeItem(KEY_LS); }

  // ── Check if Firebase callable functions are available ──────────────────────
  function getCallableFn() {
    try {
      if (typeof firebase !== 'undefined' && firebase.functions) {
        return firebase.functions().httpsCallable('aiChat');
      }
    } catch(e) {}
    return null;
  }

  function toGeminiBody(userPrompt, systemPrompt, maxTokens) {
    return {
      contents: [{ role: 'user', parts: [{ text: userPrompt }] }],
      ...(systemPrompt ? { systemInstruction: { parts: [{ text: systemPrompt }] } } : {}),
      generationConfig: { maxOutputTokens: maxTokens || 800 }
    };
  }

  function extractText(json) {
    return json.candidates?.[0]?.content?.parts?.map(p => p.text).join('') ?? '';
  }

  // ── Core: call via Cloud Function (preferred) ───────────────────────────────
  async function callViaFunction(userPrompt, systemPrompt, maxTokens) {
    const fn = getCallableFn();
    if (!fn) throw { code: 'NO_FUNCTION' };
    const messages = [{ role: 'user', content: userPrompt }];
    const result = await fn({ messages, system: systemPrompt, maxTokens });
    return result.data.content;
  }

  // ── Core: call direct (fallback — student's own Gemini key) ─────────────────
  async function callDirect(userPrompt, systemPrompt, maxTokens) {
    const key = getKey();
    if (!key) throw { code: 'NO_KEY' };
    const resp = await fetch(ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'x-goog-api-key': key },
      body: JSON.stringify(toGeminiBody(userPrompt, systemPrompt, maxTokens))
    });
    if (!resp.ok) {
      const e = await resp.json().catch(() => ({}));
      throw new Error(e.error?.message || 'API error ' + resp.status);
    }
    return extractText(await resp.json());
  }

  // ── Public: call (function first, direct fallback) ──────────────────────────
  async function call(userPrompt, systemPrompt, maxTokens) {
    try {
      return await callViaFunction(userPrompt, systemPrompt, maxTokens);
    } catch(e) {
      if (e && e.code === 'NO_FUNCTION') {
        return await callDirect(userPrompt, systemPrompt, maxTokens);
      }
      throw e;
    }
  }

  // ── Public: stream — the Cloud Function only returns whole text (no true
  // token streaming), so callers built around a streaming interface just get
  // the full response delivered as one "chunk". ───────────────────────────────
  async function stream(userPrompt, systemPrompt, maxTokens, onChunk) {
    const text = await call(userPrompt, systemPrompt, maxTokens);
    onChunk(text, text);
  }

  // ── Key prompt modal ────────────────────────────────────────────────────────
  function promptKey(onSuccess) {
    const existing = document.getElementById('_aceKeyModal');
    if (existing) existing.remove();
    const el = document.createElement('div');
    el.id = '_aceKeyModal';
    el.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:99999;display:flex;align-items:center;justify-content:center;padding:20px';
    el.innerHTML = `
      <div style="background:#0d1526;border:1.5px solid rgba(99,102,241,.5);border-radius:16px;padding:28px;max-width:440px;width:100%;box-shadow:0 20px 60px rgba(0,0,0,.5)">
        <div style="font-size:1.1rem;font-weight:800;color:#e2e8f0;margin-bottom:6px">✦ Gemini API Key</div>
        <div style="font-size:.82rem;color:#94a3b8;margin-bottom:18px;line-height:1.6">
          Enter your Gemini API key to enable AI features. It's stored only on this device.<br>
          <a href="https://aistudio.google.com/apikey" target="_blank" style="color:#818cf8">Get a free key →</a>
        </div>
        <input id="_aceKeyInput" type="password" placeholder="Paste your Gemini API key" style="width:100%;box-sizing:border-box;background:#060b18;border:1.5px solid #1e293b;border-radius:10px;padding:12px 14px;color:#e2e8f0;font-size:.88rem;margin-bottom:14px;outline:none"/>
        <div id="_aceKeyErr" style="color:#f87171;font-size:.8rem;margin-bottom:10px;display:none"></div>
        <div style="display:flex;gap:10px">
          <button id="_aceKeySave" style="flex:1;background:linear-gradient(135deg,#6366f1,#8b5cf6);border:none;border-radius:10px;padding:12px;color:#fff;font-weight:800;cursor:pointer;font-size:.88rem">Save Key</button>
          <button id="_aceKeyCancel" style="background:#1e293b;border:none;border-radius:10px;padding:12px 18px;color:#94a3b8;cursor:pointer;font-size:.88rem">Cancel</button>
        </div>
      </div>`;
    document.body.appendChild(el);
    const inp = document.getElementById('_aceKeyInput');
    inp.focus();
    document.getElementById('_aceKeyCancel').onclick = () => el.remove();
    document.getElementById('_aceKeySave').onclick = () => {
      const k = inp.value.trim();
      if (k.length < 10) {
        const err = document.getElementById('_aceKeyErr');
        err.style.display = '';
        err.textContent = 'That doesn\'t look like a valid key.';
        return;
      }
      setKey(k);
      el.remove();
      if (onSuccess) onSuccess();
    };
    inp.addEventListener('keydown', e => { if(e.key==='Enter') document.getElementById('_aceKeySave').click(); });
  }

  // ── run(): wrap fn, catch NO_KEY, prompt, retry ──────────────────────────────
  async function run(fn) {
    try {
      return await fn();
    } catch(e) {
      if (e && e.code === 'NO_KEY') {
        return new Promise((resolve, reject) => {
          promptKey(async () => {
            try { resolve(await fn()); }
            catch(e2) { reject(e2); }
          });
        });
      }
      throw e;
    }
  }

  // ── Status badge (shows in tools) ───────────────────────────────────────────
  function badge() {
    const fn = getCallableFn();
    if (fn) return '<span style="font-size:.7rem;color:#10b981;border:1px solid rgba(16,185,129,.4);padding:2px 8px;border-radius:20px;font-weight:700">✓ AI Ready</span>';
    if (hasKey()) return '<span style="font-size:.7rem;color:#6366f1;border:1px solid rgba(99,102,241,.4);padding:2px 8px;border-radius:20px;font-weight:700">Gemini AI</span>';
    return '<span style="font-size:.7rem;color:#f59e0b;border:1px solid rgba(245,158,11,.4);padding:2px 8px;border-radius:20px;font-weight:700">Set API Key</span>';
  }

  window.aceAI = { call, stream, badge, promptKey, run, hasKey, getKey, setKey, clearKey };
})();
