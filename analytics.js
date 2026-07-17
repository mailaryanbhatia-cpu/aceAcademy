/**
 * AcerAcademy — Tool analytics tracker
 * Auto-tracks page visits. Reads tool name from <title>.
 * Data stored in localStorage under 'ace_analytics'.
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

  // Auto-track on page load
  document.addEventListener('DOMContentLoaded', ()=>{
    const tool = getToolName();
    if(tool) track(tool);
  });

  window.aceAnalytics = { track, getData, topTools, recentTools, totalVisits, getToolName };
})();
