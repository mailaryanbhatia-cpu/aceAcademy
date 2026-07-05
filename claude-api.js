/**
 * aceAcademy — Claude API helper
 * Browser-direct calls using anthropic-dangerous-allow-browser header.
 * Key stored in localStorage under 'ace_claude_key'.
 */
(function(){
  const KEY_LS = 'ace_claude_key';
  const MODEL   = 'claude-haiku-4-5-20251001';
  const ENDPOINT = 'https://api.anthropic.com/v1/messages';

  async function call(userPrompt, systemPrompt='You are a helpful academic assistant.', maxTokens=1200){
    const key = localStorage.getItem(KEY_LS);
    if(!key) throw new Error('NO_KEY');

    const body = {
      model: MODEL,
      max_tokens: maxTokens,
      system: systemPrompt,
      messages: [{role:'user', content: userPrompt}]
    };

    const res = await fetch(ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': key,
        'anthropic-version': '2023-06-01',
        'anthropic-dangerous-allow-browser': 'true'
      },
      body: JSON.stringify(body)
    });

    if(!res.ok){
      const err = await res.json().catch(()=>({error:{message:'API error '+res.status}}));
      throw new Error(err?.error?.message || 'API error '+res.status);
    }
    const data = await res.json();
    return data.content?.[0]?.text || '';
  }

  // Streaming version — calls onChunk(text) repeatedly, returns full text
  async function stream(userPrompt, systemPrompt, maxTokens, onChunk){
    const key = localStorage.getItem(KEY_LS);
    if(!key) throw new Error('NO_KEY');

    const body = {
      model: MODEL,
      max_tokens: maxTokens || 1200,
      stream: true,
      system: systemPrompt || 'You are a helpful academic assistant.',
      messages: [{role:'user', content: userPrompt}]
    };

    const res = await fetch(ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': key,
        'anthropic-version': '2023-06-01',
        'anthropic-dangerous-allow-browser': 'true'
      },
      body: JSON.stringify(body)
    });

    if(!res.ok){
      const err = await res.json().catch(()=>({error:{message:'API error '+res.status}}));
      throw new Error(err?.error?.message || 'API error '+res.status);
    }

    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let full = '';
    while(true){
      const {done, value} = await reader.read();
      if(done) break;
      const chunk = decoder.decode(value);
      const lines = chunk.split('\n').filter(l=>l.startsWith('data: '));
      for(const line of lines){
        const data = line.slice(6);
        if(data==='[DONE]') break;
        try{
          const j = JSON.parse(data);
          if(j.type==='content_block_delta' && j.delta?.text){
            full += j.delta.text;
            if(onChunk) onChunk(j.delta.text, full);
          }
        }catch(e){}
      }
    }
    return full;
  }

  // Show the standard "AI powered by Claude" badge on a container
  function badge(containerEl){
    if(!containerEl) return;
    const d = document.createElement('div');
    d.className = 'ace-ai-badge';
    d.innerHTML = '✦ Powered by Claude AI';
    d.style.cssText = 'display:inline-flex;align-items:center;gap:5px;font-size:.72rem;font-weight:700;color:var(--accent);opacity:.8;margin-top:6px;';
    containerEl.appendChild(d);
  }

  // Show the API key prompt if key is missing
  function promptKey(onSuccess){
    let modal = document.getElementById('_aceApiModal');
    if(!modal){
      modal = document.createElement('div');
      modal.id = '_aceApiModal';
      modal.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.8);z-index:99999;display:flex;align-items:center;justify-content:center;backdrop-filter:blur(6px)';
      modal.innerHTML = `
        <div style="background:#0d1526;border:1.5px solid #2d3748;border-radius:20px;padding:28px;max-width:480px;width:92%;box-shadow:0 30px 80px rgba(0,0,0,.6)">
          <h3 style="margin:0 0 8px;font-size:1.1rem;font-weight:800;color:#e2e8f0">🤖 Enable AI Features</h3>
          <p style="font-size:.85rem;color:#94a3b8;margin:0 0 16px;line-height:1.6">Enter your Anthropic API key to unlock AI-powered grading, thesis generation, and debate feedback. Your key is stored only in your browser.</p>
          <a href="https://console.anthropic.com/settings/keys" target="_blank" style="font-size:.78rem;color:#818cf8;margin-bottom:14px;display:block">→ Get a free API key at console.anthropic.com</a>
          <input id="_aceApiKeyInput" type="password" placeholder="sk-ant-..." style="width:100%;padding:10px 14px;background:#111827;border:1.5px solid #374151;border-radius:10px;color:#e2e8f0;font-size:.9rem;box-sizing:border-box;margin-bottom:14px;font-family:inherit">
          <div style="display:flex;gap:10px;justify-content:flex-end">
            <button onclick="document.getElementById('_aceApiModal').remove()" style="background:#1e293b;border:none;color:#94a3b8;padding:9px 18px;border-radius:99px;cursor:pointer;font-size:.88rem">Cancel</button>
            <button onclick="window.aceAI._saveKey()" style="background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;border:none;padding:9px 22px;border-radius:99px;font-weight:700;cursor:pointer;font-size:.88rem">Save Key</button>
          </div>
        </div>`;
      document.body.appendChild(modal);
      document.getElementById('_aceApiKeyInput').focus();
      document.getElementById('_aceApiKeyInput').addEventListener('keydown', e=>{ if(e.key==='Enter') window.aceAI._saveKey(); });
    }
    window.aceAI._onKeySuccess = onSuccess;
  }

  function _saveKey(){
    const val = document.getElementById('_aceApiKeyInput')?.value?.trim();
    if(!val || !val.startsWith('sk-ant')){
      alert('Please enter a valid Anthropic API key (starts with sk-ant-)');
      return;
    }
    localStorage.setItem(KEY_LS, val);
    document.getElementById('_aceApiModal')?.remove();
    if(window.aceAI._onKeySuccess) window.aceAI._onKeySuccess();
  }

  // Convenience: run fn, catch NO_KEY and prompt, then retry
  async function run(fn){
    try { return await fn(); }
    catch(e){
      if(e.message==='NO_KEY'){
        return new Promise(resolve => {
          promptKey(async ()=>{ resolve(await fn()); });
        });
      }
      throw e;
    }
  }

  window.aceAI = { call, stream, badge, promptKey, _saveKey, run,
    hasKey: ()=>!!localStorage.getItem(KEY_LS),
    getKey: ()=>localStorage.getItem(KEY_LS),
    setKey: k=>localStorage.setItem(KEY_LS, k),
    clearKey: ()=>localStorage.removeItem(KEY_LS)
  };
})();
