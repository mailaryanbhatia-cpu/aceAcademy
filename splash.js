(function(){
  // Only show on PWA standalone mode or first load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', showSplash);
  } else {
    showSplash();
  }

  function showSplash(){
    // Only show in standalone PWA mode
    var isStandalone = window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone;
    if (!isStandalone) return;

    // Skip if already shown this session
    if (sessionStorage.getItem('ace_splash_shown')) return;
    sessionStorage.setItem('ace_splash_shown', '1');

    var style = document.createElement('style');
    style.textContent = [
      '#ace-splash{position:fixed;inset:0;z-index:999999;background:#0b1120;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0;animation:none;pointer-events:all}',
      '#ace-splash.fade-out{animation:ace-sp-fade .5s ease forwards}',
      '@keyframes ace-sp-fade{to{opacity:0;pointer-events:none}}',
      '@keyframes ace-sp-logo-in{from{opacity:0;transform:scale(.7)}to{opacity:1;transform:scale(1)}}',
      '@keyframes ace-sp-text-in{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}',
      '@keyframes ace-sp-dot{0%,80%,100%{transform:scale(.6);opacity:.4}40%{transform:scale(1);opacity:1}}',
      '.ace-sp-logo{width:96px;height:96px;border-radius:22px;animation:ace-sp-logo-in .55s cubic-bezier(.34,1.56,.64,1)}',
      '.ace-sp-name{font-family:-apple-system,BlinkMacSystemFont,"Inter",sans-serif;font-size:1.8rem;font-weight:900;color:#e2e8f0;margin-top:18px;letter-spacing:-.02em;animation:ace-sp-text-in .5s .2s ease both}',
      '.ace-sp-sub{font-family:-apple-system,BlinkMacSystemFont,"Inter",sans-serif;font-size:.85rem;color:#475569;margin-top:5px;animation:ace-sp-text-in .5s .35s ease both}',
      '.ace-sp-dots{display:flex;gap:7px;margin-top:36px;animation:ace-sp-text-in .5s .5s ease both}',
      '.ace-sp-dot{width:8px;height:8px;border-radius:50%;background:#6366f1}',
      '.ace-sp-dot:nth-child(1){animation:ace-sp-dot 1.2s .0s infinite ease-in-out}',
      '.ace-sp-dot:nth-child(2){animation:ace-sp-dot 1.2s .2s infinite ease-in-out}',
      '.ace-sp-dot:nth-child(3){animation:ace-sp-dot 1.2s .4s infinite ease-in-out}'
    ].join('');
    document.head.appendChild(style);

    var splash = document.createElement('div');
    splash.id = 'ace-splash';
    splash.innerHTML = [
      '<img class="ace-sp-logo" src="/icons/icon-192.png" alt="aceAcademy"/>',
      '<div class="ace-sp-name">aceAcademy</div>',
      '<div class="ace-sp-sub">Your AP Study Platform</div>',
      '<div class="ace-sp-dots">',
      '  <div class="ace-sp-dot"></div>',
      '  <div class="ace-sp-dot"></div>',
      '  <div class="ace-sp-dot"></div>',
      '</div>'
    ].join('');
    document.body.insertBefore(splash, document.body.firstChild);

    // Fade out after 1.8s
    setTimeout(function(){
      splash.classList.add('fade-out');
      setTimeout(function(){ splash.remove(); }, 500);
    }, 1800);
  }
})();
