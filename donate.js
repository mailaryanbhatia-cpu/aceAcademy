// ── aceAcademy Donate Link (site-wide, injected into the top nav) ──────────
// Self-contained: finds the page's nav bar and inserts a bold white
// "Donate" link next to the profile pill (or sign-in link, if present),
// pointing to a PayPal donation page where visitors can enter any amount
// and pay via PayPal balance or debit/credit card as a guest.
(function(){
  if (window.__AceDonateInit) return; // guard against double-injection
  window.__AceDonateInit = true;

  var PAYPAL_URL = 'https://www.paypal.com/donate?business=' +
    encodeURIComponent('jagasia.deepti@gmail.com') +
    '&currency_code=USD&no_recurring=0';

  function inject(){
    if (document.getElementById('ace-donate-link')) return;

    var nav = document.querySelector('nav') || document.querySelector('.nav') || document.querySelector('header');
    if (!nav) return;

    var link = document.createElement('a');
    link.id = 'ace-donate-link';
    link.href = PAYPAL_URL;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    link.title = 'Support aceAcademy — donate any amount via PayPal or card';
    link.textContent = 'Donate';
    link.style.cssText = [
      'color:#ffffff',
      'font-weight:900',
      'font-size:1.05rem',
      'letter-spacing:.02em',
      'text-decoration:none',
      'white-space:nowrap',
      'flex-shrink:0',
      'padding:4px 10px',
      'border-radius:8px',
      'transition:opacity .15s,transform .15s',
      'position:relative',
      'z-index:100'
    ].join(';');
    link.onmouseenter = function(){ this.style.opacity = '.8'; this.style.transform = 'scale(1.05)'; };
    link.onmouseleave = function(){ this.style.opacity = '1'; this.style.transform = 'scale(1)'; };

    // Prefer sitting immediately to the left of the profile pill (nav-profile.js)
    // or a login/sign-in link, if either is present on this page.
    var profilePill = document.getElementById('ace-nav-profile');
    var signInLink = nav.querySelector('a[href*="login.html"], a[href*="/login"]');
    var anchor = profilePill || signInLink;

    if (anchor && anchor.parentNode === nav) {
      nav.insertBefore(link, anchor);
    } else if (anchor) {
      anchor.parentNode.insertBefore(link, anchor);
    } else {
      // No profile pill or sign-in link found on this page — just push it to the far right.
      link.style.marginLeft = 'auto';
      nav.appendChild(link);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inject);
  } else {
    inject();
  }
})();
