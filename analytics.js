/**
 * AcerAcademy — Tool analytics tracker
 * Auto-tracks page visits. Reads tool name from <title>.
 * Data stored in localStorage under 'ace_analytics' (per-device; this key
 * already syncs to each signed-in user's own Firestore doc via
 * firestore.js's 'ace_' prefix rule, but that's per-user, not a site-wide
 * total).
 *
 * Site-wide aggregate counts (added 2026-07-19, part of the con-4 backend
 * work): also increments a shared analyticsSummary/{date} Firestore doc so
 * admin.html can show real cross-visitor totals. Deliberately NOT built on
 * Cloud Functions (those require enabling the Blaze/pay-as-you-go plan --
 * the same billing friction that caused the Gemini AI wiring to get rolled
 * back) -- instead this writes directly from the browser using
 * FieldValue.increment(), which is safe to call from many clients
 * concurrently without read-modify-write races. Per firestore.rules, this
 * write requires being signed in (so a script can't anonymously spam-
 * inflate counters or run up read/write costs) -- anonymous/signed-out
 * visits aren't reflected in the site-wide totals, only in each user's own
 * local/synced history.
 */
(function(){
  const LS_KEY = 'ace_analytics';

  function getData(){ return JSON.parse(localStorage.getItem(LS_KEY)||'{}'); }
  function setData(d){ localStorage.setItem(LS_KEY, JSON.stringify(d)); }

  function track(toolName){
    if(!toolName || toolName==='AcerAcademy') return;
    const d = getData();
    if(!d[toolName]) d[toolName] = {visits:0, lastVisit:null, firstVisit:null};
    d[toolName].visits++;
    const now = new Date().toISOString();
    d[toolName].lastVisit = now;
    if(!d[toolName].firstVisit) d[toolName].firstVisit = now;
    setData(d);
  }

  // Derive tool name from page title: "Essay Grader — AcerAcademy" → "Essay Grader"
  function getToolName(){
    const title = document.title || '';
    return title.replace(/\s*[—\-–]\s*AcerAcademy.*$/i,'').trim() || null;
  }

  // Top N tools sorted by visits
  function topTools(n){
    const d = getData();
    return Object.entries(d)
      .map(([name,v])=>({name,...v}))
      .sort((a,b)=>b.visits-a.visits)
      .slice(0, n||10);
  }

  // All tools visited in the last N days
  function recentTools(days){
    const cutoff = new Date(Date.now() - (days||30)*24*60*60*1000).toISOString();
    const d = getData();
    return Object.entries(d)
      .filter(([,v])=>v.lastVisit > cutoff)
      .map(([name,v])=>({name,...v}))
      .sort((a,b)=>b.visits-a.visits);
  }

  // Total visits across all tools
  function totalVisits(){
    return Object.values(getData()).reduce((s,v)=>s+v.visits,0);
  }

  // Firestore field names can't safely contain '.', '/', '[', ']', '*', or
  // '~' -- strip anything outside a safe set rather than risk a rejected
  // write for an unusual page title.
  function safeFieldName(name){
    return name.replace(/[.\/\[\]*~]/g, '_').slice(0, 200);
  }

  // Best-effort site-wide counter increment. Silently does nothing if
  // Firebase isn't loaded on this page, or the visitor isn't signed in --
  // see the file header for why signed-in-only is the deliberate tradeoff.
  // Guards against double-incrementing if both the immediate call and the
  // delayed retry (below) each find a signed-in user for this same page load.
  let _siteWideCountPushed = false;
  function pushSiteWideCount(toolName){
    if (_siteWideCountPushed) return;
    try {
      if (typeof firebase === 'undefined' || !firebase.firestore || !firebase.auth) return;
      const user = firebase.auth().currentUser;
      if (!user) return;
      _siteWideCountPushed = true;
      const today = new Date().toISOString().slice(0, 10);
      const field = safeFieldName(toolName);
      const update = { updatedAt: firebase.firestore.FieldValue.serverTimestamp() };
      update[field] = firebase.firestore.FieldValue.increment(1);
      firebase.firestore().collection('analyticsSummary').doc(today).set(update, { merge: true })
        .catch(err => console.warn('[analytics] site-wide count failed:', err.message));
    } catch (e) {
      console.warn('[analytics] site-wide count failed:', e.message);
    }
  }

  // Auto-track on page load
  document.addEventListener('DOMContentLoaded', ()=>{
    const tool = getToolName();
    if(tool) {
      track(tool);
      // Firebase auth state may not be resolved yet at DOMContentLoaded on
      // pages that load the SDK late/async -- try now, and again shortly
      // after, rather than requiring every page to fire a dedicated ready
      // event just for this.
      pushSiteWideCount(tool);
      setTimeout(() => pushSiteWideCount(tool), 1500);
    }
  });

  // ── Basic in-house error monitoring (added 2026-07-19) ──────────────
  // Deliberately NOT a third-party service (e.g. Sentry) -- wiring one in
  // would mean creating a new external account, which isn't something to
  // do on someone else's behalf. Instead: real page errors get written to
  // the same free-tier Firestore project everything else here already
  // uses, viewable in admin.html's Errors tab.
  //
  // Capped at MAX_ERRORS_PER_LOAD per page load so a page stuck in an
  // error loop (e.g. a bug that throws on every animation frame) can't
  // burn through the Firestore free-tier write quota by itself.
  const MAX_ERRORS_PER_LOAD = 3;
  let _errorsLogged = 0;

  function pushErrorLog(message, extra){
    try {
      if (_errorsLogged >= MAX_ERRORS_PER_LOAD) return;
      if (typeof firebase === 'undefined' || !firebase.firestore || !firebase.auth) return;
      const user = firebase.auth().currentUser;
      if (!user) return; // same signed-in-including-anonymous gate as pushSiteWideCount
      _errorsLogged++;
      const entry = Object.assign({
        message: String(message || '').slice(0, 500),
        page: getToolName() || document.title || location.pathname,
        url: location.pathname,
        userAgent: navigator.userAgent.slice(0, 200),
        createdAt: firebase.firestore.FieldValue.serverTimestamp(),
      }, extra || {});
      firebase.firestore().collection('errorLogs').add(entry)
        .catch(err => console.warn('[analytics] error log write failed:', err.message));
    } catch (e) {
      console.warn('[analytics] error log write failed:', e.message);
    }
  }

  window.addEventListener('error', (e) => {
    pushErrorLog(e.message, { source: e.filename ? e.filename.split('/').pop() : '', line: e.lineno });
  });
  window.addEventListener('unhandledrejection', (e) => {
    const reason = e.reason && e.reason.message ? e.reason.message : String(e.reason);
    pushErrorLog('Unhandled promise rejection: ' + reason, { source: 'promise' });
  });

  window.aceAnalytics = { track, getData, topTools, recentTools, totalVisits, getToolName };
})();
