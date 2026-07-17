// ── AcerAcademy Study Coins ─────────────────────────────────────
window.AceCoins = (function(){
  var KEY = 'ace_coins';
  var LOG_KEY = 'ace_coin_log';

  function getBalance(){ return parseInt(localStorage.getItem(KEY)||'0'); }
  function setBalance(n){ localStorage.setItem(KEY, String(Math.max(0,n))); }

  function log(amount, reason){
    var logs = JSON.parse(localStorage.getItem(LOG_KEY)||'[]');
    logs.unshift({ amount:amount, reason:reason, date:new Date().toISOString() });
    if (logs.length > 100) logs = logs.slice(0,100);
    localStorage.setItem(LOG_KEY, JSON.stringify(logs));
  }

  function earn(amount, reason){
    setBalance(getBalance() + amount);
    log(amount, reason);
    updateBadge();
    if (window.AceSound) window.AceSound.coin();
    showFloater('+'+amount+' 🪙');
  }

  function spend(amount, reason){
    if (getBalance() < amount) return false;
    setBalance(getBalance() - amount);
    log(-amount, reason);
    updateBadge();
    return true;
  }

  function updateBadge(){
    var b = document.getElementById('ace-coin-badge');
    if (b) b.textContent = '🪙 ' + getBalance().toLocaleString();
  }

  function showFloater(text){
    var el = document.createElement('div');
    el.style.cssText = 'position:fixed;bottom:80px;right:22px;background:linear-gradient(135deg,#f59e0b,#fbbf24);color:#1c1917;font-weight:800;font-size:.9rem;padding:7px 14px;border-radius:99px;z-index:99998;pointer-events:none;animation:ace-coin-pop .6s ease forwards';
    el.textContent = text;
    var st = document.createElement('style');
    st.textContent = '@keyframes ace-coin-pop{0%{opacity:0;transform:translateY(10px) scale(.8)}40%{opacity:1;transform:translateY(-8px) scale(1.1)}100%{opacity:0;transform:translateY(-24px) scale(1)}}';
    document.head.appendChild(st);
    document.body.appendChild(el);
    setTimeout(function(){ el.remove(); }, 1000);
  }

  function injectBadge(){
    if (document.getElementById('ace-coin-badge')) return;
    var badge = document.createElement('div');
    badge.id = 'ace-coin-badge';
    badge.title = 'Study Coins — earned by studying!';
    badge.style.cssText = 'position:fixed;bottom:62px;right:18px;z-index:9998;background:linear-gradient(135deg,#f59e0b,#fbbf24);color:#1c1917;font-size:.78rem;font-weight:800;padding:5px 12px;border-radius:999px;box-shadow:0 3px 12px rgba(245,158,11,.4);cursor:pointer;user-select:none;';
    badge.textContent = '🪙 ' + getBalance().toLocaleString();
    badge.onclick = showCoinLog;
    document.body.appendChild(badge);
  }

  function showCoinLog(){
    var logs = JSON.parse(localStorage.getItem(LOG_KEY)||'[]');
    var overlay = document.createElement('div');
    overlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:99998;backdrop-filter:blur(3px)';
    var panel = document.createElement('div');
    panel.style.cssText = 'position:fixed;bottom:110px;right:18px;background:#0f172a;border:1px solid #334155;border-radius:18px;padding:18px 20px;z-index:99999;min-width:250px;max-width:300px;box-shadow:0 12px 40px rgba(0,0,0,.5);max-height:400px;overflow-y:auto';
    var rows = logs.slice(0,20).map(function(l){
      var sign = l.amount > 0 ? '+' : '';
      var col  = l.amount > 0 ? '#fbbf24' : '#ef4444';
      return '<div style="display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid #1e293b;font-size:.78rem">'
        +'<span style="color:#94a3b8">'+l.reason+'</span>'
        +'<span style="font-weight:700;color:'+col+'">'+sign+l.amount+' 🪙</span>'
        +'</div>';
    }).join('') || '<div style="color:#475569;text-align:center;padding:12px">No activity yet</div>';

    panel.innerHTML = '<div style="font-weight:800;font-size:.95rem;color:#fbbf24;margin-bottom:10px">🪙 '+getBalance().toLocaleString()+' Coins</div>' + rows
      + '<button onclick="this.parentNode.remove();document.querySelector(\'.ace-coin-overlay\').remove();" style="margin-top:12px;width:100%;background:#1e293b;color:#94a3b8;border:none;padding:7px;border-radius:8px;cursor:pointer;font-size:.8rem">Close</button>';

    overlay.className = 'ace-coin-overlay';
    overlay.onclick = function(){ overlay.remove(); panel.remove(); };
    document.body.appendChild(overlay);
    document.body.appendChild(panel);
  }

  // ── Daily login reward ─────────────────────────────────────
  (function dailyReward(){
    var lastCoin = localStorage.getItem('ace_last_coin_date');
    var today = new Date().toISOString().split('T')[0];
    if (lastCoin !== today){
      localStorage.setItem('ace_last_coin_date', today);
      setTimeout(function(){ earn(5, 'Daily login'); }, 1500);
    }
  })();

  if (document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', injectBadge);
  } else {
    injectBadge();
  }

  return {
    earn: earn,
    spend: spend,
    getBalance: getBalance,
    updateBadge: updateBadge
  };
})();
