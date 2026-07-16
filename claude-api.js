/**
 * claude-api.js  —  aceAcademy AI helper
 *
 * Priority:
 *   1. Firebase Cloud Function (claudeChat) — no student key needed, server-side key
 *   2. Direct Anthropic API  — student's own key stored in localStorage
 *
 * Usage:
 *   await aceAI.call(userPrompt, systemPrompt, maxTokens)  → string
 *   await aceAI.stream(userPrompt, systemPrompt, maxTokens, onChunk)  → void
 *   await aceAI.run(asyncFn)  → catches NO_KEY, prompts, retries
 */
(function(){
  'use strict';

  const KEY_LS   = 'ace_claude_key';
  const MODEL    = 'claude-haiku-4-5-20251001';
  const ENDPOINT = 'https://api.anthropic.com/v1/messages';

  // ── Key management ──────────────────────────────────────────────────────────
  function getKey()   { return localStorage.getItem(KEY_LS) || ''; }
  function hasKey()   { return !!getKey(); }
  function setKey(k)  { localStorage.setItem(KEY_LS, k); }
  function clearKey() { localStorage.removeItem(KEY_LS); }

  // ── Check if Firebase callable functions are available ──────────────────────
  function getCallableFn() {
    try {
      if (typeof firebase !== 'undefined' && firebase.functions) {
        return firebase.functions().httpsCallable('claudeChat');
      }
    } catch(e) {}
    return null;
  }

  // ── Core: call via Cloud Function (preferred) ───────────────────────────────
  async function callViaFunction(userPrompt, systemPrompt, maxTokens) {
    const fn = getCallableFn();
    if (!fn) throw { code: 'NO_FUNCTION' };
    const messages = [{ role: 'user', content: userPrompt }];
    const result = await fn({ messages, system: systemPrompt, maxTokens });
    return result.data.content;
  }

  // ── Core: call direct (fallback) ────────────────────────────────────────────
  async function callDirect(userPrompt, systemPrompt, maxTokens) {
    const key = getKey();
    if (!key) throw { code: 'NO_KEY' };
    const body = {
      model: MODEL,
      max_tokens: maxTokens || 800,
      messages: [{ role: 'user', content: userPrompt }],
      ...(systemPrompt ? { system: systemPrompt } : {})
    };
    const resp = await fetch(ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': key,
        'anthropic-version': '2023-06-01',
        'anthropic-dangerous-allow-browser': 'true'
      },
      body: JSON.stringify(body)
    });
    if (!resp.ok) {
      const e = await resp.json().catch(() => ({}));
      throw new Error(e.error?.message || 'API error ' + resp.status);
    }
    const json = await resp.json();
    return json.content?.[0]?.text ?? '';
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

  // ── Public: stream (direct only — Cloud Functions don't stream yet) ─────────
  async function stream(userPrompt, systemPrompt, maxTokens, onChunk) {
    // Try function first (non-streaming), then fall through to streaming direct
    try {
      const fn = getCallableFn();
      if (fn) {
        // Use function but simulate chunk delivery
        const text = await callViaFunction(userPrompt, systemPrompt, maxTokens);
        onChunk(text, text);
        return;
      }
    } catch(e) { /* fall through */ }

    // Direct streaming
    const key = getKey();
    if (!key) throw { code: 'NO_KEY' };
    const body = {
      model: MODEL,
      max_tokens: maxTokens || 800,
      stream: true,
      messages: [{ role: 'user', content: userPrompt }],
      ...(systemPrompt ? { system: systemPrompt } : {})
    };
    const resp = await fetch(ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': key,
        'anthropic-version': '2023-06-01',
        'anthropic-dangerous-allow-browser': 'true'
      },
      body: JSON.stringify(body)
    });
    if (!resp.ok) throw new Error('Stream error ' + resp.status);
    const reader = resp.body.getReader();
    const dec    = new TextDecoder();
    let full = '';
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      const lines = dec.decode(value).split('\n');
      for (const line of lines) {
        if (!line.startsWith('data:')) continue;
        try {
          const evt = JSON.parse(line.slice(5).trim());
          if (evt.type === 'content_block_delta' && evt.delta?.text) {
            full += evt.delta.text;
            onChunk(evt.delta.text, full);
          }
        } catch(_) {}
      }
    }
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
        <div style="font-size:1.1rem;font-weight:800;color:#e2e8f0;margin-bottom:6px">✦ Claude API Key</div>
        <div style="font-size:.82rem;color:#94a3b8;margin-bottom:18px;line-height:1.6">
          Enter your Anthropic API key to enable AI features. It's stored only on this device.<br>
          <a href="https://console.anthropic.com/keys" target="_blank" style="color:#818cf8">Get a free key →</a>
        </div>
        <input id="_aceKeyInput" type="password" placeholder="sk-ant-..." style="width:100%;box-sizing:border-box;background:#060b18;border:1.5px solid #1e293b;border-radius:10px;padding:12px 14px;color:#e2e8f0;font-size:.88rem;margin-bottom:14px;outline:none"/>
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
      if (!k.startsWith('sk-ant-')) {
        const err = document.getElementById('_aceKeyErr');
        err.style.display = '';
        err.textContent = 'Key must start with sk-ant-';
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
    if (hasKey()) return '<span style="font-size:.7rem;color:#6366f1;border:1px solid rgba(99,102,241,.4);padding:2px 8px;border-radius:20px;font-weight:700">Claude AI</span>';
    return '<span style="font-size:.7rem;color:#f59e0b;border:1px solid rgba(245,158,11,.4);padding:2px 8px;border-radius:20px;font-weight:700">Set API Key</span>';
  }

  window.aceAI = { call, stream, badge, promptKey, run, hasKey, getKey, setKey, clearKey };
})();
