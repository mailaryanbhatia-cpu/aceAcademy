(function(){
  function inject(){
    var name   = localStorage.getItem('ace_profile_name') || '';
    var avatar = localStorage.getItem('ace_avatar') || '';
    var streak = JSON.parse(localStorage.getItem('ace_login_streak') || '{"count":0}');
    var badges = JSON.parse(localStorage.getItem('ace_badges') || '[]');
    var topBadge = '';
    ['diamond','gold','silver','bronze'].forEach(function(id){
      if(!topBadge && badges.includes(id))
        topBadge = {diamond:'💎',gold:'🥇',silver:'🥈',bronze:'🥉'}[id];
    });

    var initials = name
      ? name.split(' ').map(function(w){ return w[0]; }).join('').slice(0,2).toUpperCase()
      : '🎓';
    var label = name ? (name.split(' ')[0].slice(0,12)) : 'Profile';

    // Build the pill
    var pill = document.createElement('a');
    pill.href = '/aceAcademy/profile.html';
    pill.title = 'My Profile';
    pill.style.cssText = [
      'display:inline-flex','align-items:center','gap:7px',
      'background:#1e293b','border:1px solid #334155',
      'border-radius:99px','padding:4px 12px 4px 4px',
      'text-decoration:none','color:#e2e8f0',
      'font-size:.8rem','font-weight:700',
      'transition:border-color .2s',
      'flex-shrink:0','white-space:nowrap',
      'position:relative','z-index:100'
    ].join(';');
    pill.onmouseenter = function(){ this.style.borderColor='#6366f1'; };
    pill.onmouseleave = function(){ this.style.borderColor='#334155'; };

    // Avatar circle
    var av = document.createElement('div');
    av.style.cssText = 'width:26px;height:26px;border-radius:50%;background:linear-gradient(135deg,#6366f1,#8b5cf6);display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:900;color:#fff;overflow:hidden;flex-shrink:0';
    if (avatar) {
      var img = document.createElement('img');
      img.src = avatar;
      img.style.cssText = 'width:100%;height:100%;object-fit:cover;border-radius:50%';
      av.appendChild(img);
    } else {
      av.textContent = initials;
    }

    // Name + badge
    var txt = document.createElement('span');
    txt.textContent = label + (topBadge ? ' ' + topBadge : '');

    pill.appendChild(av);
    pill.appendChild(txt);

    // Try to find a nav to append to
    var nav = document.querySelector('nav') || document.querySelector('.nav') || document.querySelector('header');
    if (!nav) return;

    // Avoid duplicate
    if (document.getElementById('ace-nav-profile')) return;
    pill.id = 'ace-nav-profile';

    // Position: append to nav, floated right via flex
    pill.style.marginLeft = 'auto';

    // Check if there's already a theme toggle or other buttons at the end
    // Insert before the last button/element if possible, otherwise just append
    var themeBtn = nav.querySelector('#themeToggle, #themeToggleBtn, [onclick="toggleTheme()"]');
    if (themeBtn) {
      // insert before theme toggle
      themeBtn.parentNode.insertBefore(pill, themeBtn);
    } else {
      nav.appendChild(pill);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inject);
  } else {
    inject();
  }
})();
