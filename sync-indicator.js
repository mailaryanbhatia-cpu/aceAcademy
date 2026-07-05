/**
 * sync-indicator.js
 * Shows a small sync status dot in the nav. Green = synced, yellow = syncing, grey = offline.
 */
(function(){
  var DOT_ID = '_ace_sync_dot';

  function injectDot(){
    if(document.getElementById(DOT_ID)) return;
    // Find nav or body
    var nav = document.querySelector('nav') || document.body;
    var dot = document.createElement('div');
    dot.id = DOT_ID;
    dot.title = 'Sync status';
    dot.style.cssText = [
      'position:fixed',
      'bottom:14px',
      'right:14px',
      'width:10px',
      'height:10px',
      'border-radius:50%',
      'background:#334155',
      'z-index:9000',
      'transition:background .4s, box-shadow .4s',
      'cursor:default',
      'box-shadow:0 0 0 2px rgba(255,255,255,.08)'
    ].join(';');
    document.body.appendChild(dot);
    return dot;
  }

  function setStatus(state){
    var dot = document.getElementById(DOT_ID) || injectDot();
    if(!dot) return;
    var map = {
      synced:  { bg:'#10b981', shadow:'0 0 0 3px rgba(16,185,129,.3)',  title:'Synced ✓' },
      syncing: { bg:'#f59e0b', shadow:'0 0 0 3px rgba(245,158,11,.3)',  title:'Syncing…' },
      offline: { bg:'#64748b', shadow:'0 0 0 2px rgba(255,255,255,.08)',title:'Offline — changes saved locally' },
      error:   { bg:'#ef4444', shadow:'0 0 0 3px rgba(239,68,68,.3)',   title:'Sync error' }
    };
    var s = map[state] || map.offline;
    dot.style.background  = s.bg;
    dot.style.boxShadow   = s.shadow;
    dot.title = s.title;
  }

  function refreshStatus(){
    if(typeof aceFirestore === 'undefined'){ setStatus('offline'); return; }
    var st = aceFirestore.status();
    if(!navigator.onLine){ setStatus('offline'); return; }
    if(!st.synced){ setStatus('offline'); return; }
    if(st.dirty > 0 || st.pending > 0){ setStatus('syncing'); return; }
    setStatus('synced');
  }

  document.addEventListener('DOMContentLoaded', function(){
    injectDot();
    refreshStatus();
    // Poll every 3s
    setInterval(refreshStatus, 3000);
    // React to sync events
    window.addEventListener('ace-sync-updated', function(){ setStatus('synced'); });
    window.addEventListener('offline', function(){ setStatus('offline'); });
    window.addEventListener('online',  function(){ setStatus('syncing'); setTimeout(refreshStatus, 3000); });
  });
})();
