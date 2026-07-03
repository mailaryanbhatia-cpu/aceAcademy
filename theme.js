// theme.js — shared dark/light mode for aceAcademy
(function(){
  function applyTheme(t){
    document.documentElement.setAttribute('data-theme', t);
    localStorage.setItem('color-theme', t);
    const btn = document.getElementById('themeToggle');
    if(btn) btn.textContent = t === 'dark' ? '☀️' : '🌙';
  }
  const saved = localStorage.getItem('color-theme');
  const preferred = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  applyTheme(saved || preferred);
  window.toggleTheme = function(){
    const current = document.documentElement.getAttribute('data-theme');
    applyTheme(current === 'dark' ? 'light' : 'dark');
  };
  window.addEventListener('DOMContentLoaded', function(){
    const t = localStorage.getItem('color-theme') || preferred;
    applyTheme(t);
    const btn = document.getElementById('themeToggle');
    if(btn) btn.textContent = t === 'dark' ? '☀️' : '🌙';
  });
})();
