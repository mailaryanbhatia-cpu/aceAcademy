// theme.js — AcerAcademy dark theme
(function(){
  function applyTheme(t){
    document.documentElement.setAttribute('data-theme',t);
    localStorage.setItem('color-theme',t);
    var btn=document.getElementById('themeToggle')||document.getElementById('themeToggleBtn');
    if(btn) btn.textContent=t==='dark'?'☀️':'🌙';
  }
  applyTheme(localStorage.getItem('color-theme')||'dark');
  window.toggleTheme=function(){
    applyTheme(document.documentElement.getAttribute('data-theme')==='dark'?'light':'dark');
  };
})();
