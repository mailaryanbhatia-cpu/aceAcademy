#!/usr/bin/env python3
"""Inject a floating notes widget into all aceAcademy HTML pages."""
import pathlib, re

WIDGET = r"""
<!-- ══ FLOATING NOTES WIDGET ══════════════════════════════════════════ -->
<style>
#notesBtn{position:fixed;bottom:24px;right:24px;width:52px;height:52px;border-radius:50%;
  background:var(--accent,#6c63ff);color:#fff;border:none;font-size:1.4rem;cursor:pointer;
  box-shadow:0 4px 18px rgba(0,0,0,.25);z-index:9998;display:flex;align-items:center;
  justify-content:center;transition:transform .15s,box-shadow .15s;}
#notesBtn:hover{transform:scale(1.1);box-shadow:0 6px 24px rgba(0,0,0,.35);}
#notesBtn .badge{position:absolute;top:-4px;right:-4px;background:#f06;color:#fff;
  font-size:.6rem;font-weight:700;padding:2px 5px;border-radius:10px;display:none;}
#notesPanel{position:fixed;bottom:88px;right:24px;width:360px;max-height:520px;
  background:#fff;border-radius:16px;box-shadow:0 8px 40px rgba(0,0,0,.22);
  z-index:9999;display:flex;flex-direction:column;opacity:0;pointer-events:none;
  transform:translateY(16px);transition:opacity .2s,transform .2s;overflow:hidden;}
#notesPanel.open{opacity:1;pointer-events:auto;transform:translateY(0);}
.np-head{background:var(--accent,#6c63ff);color:#fff;padding:12px 16px;
  display:flex;align-items:center;justify-content:space-between;flex-shrink:0;}
.np-head h3{margin:0;font-size:1rem;font-weight:700;letter-spacing:.02em;}
.np-head-btns{display:flex;gap:8px;align-items:center;}
.np-icon-btn{background:rgba(255,255,255,.2);border:none;color:#fff;border-radius:8px;
  padding:4px 8px;font-size:.8rem;cursor:pointer;transition:background .15s;}
.np-icon-btn:hover{background:rgba(255,255,255,.35);}
.np-tabs{display:flex;gap:0;overflow-x:auto;border-bottom:1px solid #eee;flex-shrink:0;
  scrollbar-width:none;}
.np-tabs::-webkit-scrollbar{display:none;}
.np-tab{padding:8px 14px;font-size:.75rem;font-weight:600;border:none;background:none;
  cursor:pointer;color:#888;white-space:nowrap;border-bottom:2px solid transparent;transition:color .15s;}
.np-tab.active{color:var(--accent,#6c63ff);border-bottom-color:var(--accent,#6c63ff);}
.np-body{flex:1;display:flex;flex-direction:column;min-height:0;}
.np-textarea{flex:1;width:100%;border:none;outline:none;resize:none;
  padding:14px 16px;font-size:.88rem;font-family:inherit;line-height:1.6;
  color:#333;background:#fafafa;min-height:240px;}
.np-footer{display:flex;align-items:center;justify-content:space-between;
  padding:8px 12px;border-top:1px solid #eee;background:#fff;flex-shrink:0;}
.np-wordcount{font-size:.72rem;color:#aaa;}
.np-foot-btns{display:flex;gap:6px;}
.np-foot-btn{font-size:.72rem;padding:4px 10px;border:1px solid #ddd;border-radius:8px;
  background:#fff;cursor:pointer;color:#555;transition:all .15s;}
.np-foot-btn:hover{background:#f5f5ff;border-color:var(--accent,#6c63ff);color:var(--accent,#6c63ff);}
.np-foot-btn.danger:hover{background:#fff0f0;border-color:#f06;color:#f06;}
@media(max-width:420px){
  #notesPanel{width:calc(100vw - 32px);right:16px;}
  #notesBtn{bottom:16px;right:16px;}
}
</style>

<button id="notesBtn" onclick="toggleNotes()" title="Notes">
  📝<span class="badge" id="notesBadge">!</span>
</button>

<div id="notesPanel">
  <div class="np-head">
    <h3>📝 My Notes</h3>
    <div class="np-head-btns">
      <button class="np-icon-btn" onclick="downloadNotes()" title="Download all notes">⬇ Save</button>
      <button class="np-icon-btn" onclick="toggleNotes()" title="Close">✕</button>
    </div>
  </div>
  <div class="np-tabs" id="notesTabs"></div>
  <div class="np-body">
    <textarea class="np-textarea" id="notesTA"
      placeholder="Start typing your notes here…&#10;&#10;💡 Tips:&#10;• Use *asterisks* for key terms&#10;• Jot formulas, vocab, or reminders&#10;• Notes are saved automatically"
      oninput="saveNote();updateWordCount();updateBadge()"></textarea>
  </div>
  <div class="np-footer">
    <span class="np-wordcount" id="npWordCount">0 words</span>
    <div class="np-foot-btns">
      <button class="np-foot-btn" onclick="copyNotes()">📋 Copy</button>
      <button class="np-foot-btn danger" onclick="clearNote()">🗑 Clear</button>
    </div>
  </div>
</div>

<script>
(function(){
  const NOTE_TABS = [
    {key:'general',   label:'📓 General'},
    {key:'math',      label:'➕ Math'},
    {key:'science',   label:'🔬 Science'},
    {key:'ela',       label:'📖 ELA'},
    {key:'history',   label:'🌍 History'},
    {key:'cs',        label:'💻 CS'},
    {key:'health',    label:'❤️ Health'},
    {key:'languages', label:'🌏 Languages'},
  ];
  let activeTab = 'general';

  function noteKey(k){ return 'aceNotes_' + k; }

  function loadNote(k){
    try{ return localStorage.getItem(noteKey(k)) || ''; }catch(e){ return ''; }
  }
  function saveNote(){
    try{ localStorage.setItem(noteKey(activeTab), document.getElementById('notesTA').value); }catch(e){}
  }
  window.saveNote = saveNote;

  function buildTabs(){
    const container = document.getElementById('notesTabs');
    container.innerHTML = NOTE_TABS.map(t=>
      `<button class="np-tab${t.key===activeTab?' active':''}" onclick="switchTab('${t.key}')">${t.label}</button>`
    ).join('');
  }

  window.switchTab = function(k){
    saveNote();
    activeTab = k;
    buildTabs();
    const ta = document.getElementById('notesTA');
    ta.value = loadNote(k);
    ta.focus();
    updateWordCount();
    updateBadge();
  };

  window.toggleNotes = function(){
    const p = document.getElementById('notesPanel');
    p.classList.toggle('open');
    if(p.classList.contains('open')){
      document.getElementById('notesTA').value = loadNote(activeTab);
      updateWordCount();
      updateBadge();
      document.getElementById('notesTA').focus();
    }
  };

  window.updateWordCount = function(){
    const v = (document.getElementById('notesTA')?.value||'').trim();
    const words = v ? v.split(/\s+/).length : 0;
    const el = document.getElementById('npWordCount');
    if(el) el.textContent = words + (words===1?' word':' words');
  };

  window.updateBadge = function(){
    // Show badge if any tab has content
    const hasNotes = NOTE_TABS.some(t=> loadNote(t.key).trim().length > 0);
    const b = document.getElementById('notesBadge');
    if(b) b.style.display = hasNotes ? 'block' : 'none';
  };

  window.clearNote = function(){
    if(!confirm('Clear notes for this tab?')) return;
    try{ localStorage.removeItem(noteKey(activeTab)); }catch(e){}
    document.getElementById('notesTA').value = '';
    updateWordCount();
    updateBadge();
  };

  window.copyNotes = function(){
    const ta = document.getElementById('notesTA');
    if(!ta || !ta.value.trim()){ alert('No notes to copy!'); return; }
    navigator.clipboard.writeText(ta.value).then(()=>{
      const btn = event.target;
      const orig = btn.textContent;
      btn.textContent = '✅ Copied!';
      setTimeout(()=>{ btn.textContent = orig; }, 1500);
    }).catch(()=>{
      ta.select();
      document.execCommand('copy');
    });
  };

  window.downloadNotes = function(){
    const allNotes = NOTE_TABS
      .map(t=>{ const c=loadNote(t.key).trim(); return c ? `=== ${t.label} ===\n${c}` : ''; })
      .filter(Boolean).join('\n\n');
    if(!allNotes){ alert('No notes to save!'); return; }
    const blob = new Blob([allNotes], {type:'text/plain'});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'aceAcademy-notes.txt';
    a.click();
    URL.revokeObjectURL(a.href);
  };

  // Init
  buildTabs();
  updateBadge();

  // Close panel when clicking outside
  document.addEventListener('click', function(e){
    const p = document.getElementById('notesPanel');
    const b = document.getElementById('notesBtn');
    if(p && p.classList.contains('open') && !p.contains(e.target) && !b.contains(e.target)){
      p.classList.remove('open');
    }
  });
})();
</script>
<!-- ══ END NOTES WIDGET ════════════════════════════════════════════════ -->
"""

pages = [
    'index.html','curriculum.html','worksheets.html',
    'tests.html','tutor.html','language.html'
]
base = pathlib.Path('/sessions/admiring-stoic-pascal/mnt/outputs')

for name in pages:
    p = base / name
    if not p.exists():
        print(f'SKIP (not found): {name}')
        continue
    html = p.read_text(encoding='utf-8')
    if '<!-- ══ FLOATING NOTES WIDGET' in html:
        print(f'Already has widget: {name}')
        continue
    html = html.replace('</body>', WIDGET + '\n</body>', 1)
    p.write_text(html, encoding='utf-8')
    print(f'Injected: {name}')

print('\nDone.')
