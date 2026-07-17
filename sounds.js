// ── AcerAcademy Sound Engine ────────────────────────────────────
// Uses Web Audio API — no files needed, all synthesized
window.AceSound = (function(){
  var ctx = null;
  var enabled = localStorage.getItem('ace_sounds') !== 'off';

  function getCtx(){
    if (!ctx) ctx = new (window.AudioContext || window.webkitAudioContext)();
    return ctx;
  }

  function tone(freq, type, duration, volume, delay){
    if (!enabled) return;
    try {
      var c = getCtx();
      var o = c.createOscillator();
      var g = c.createGain();
      o.connect(g); g.connect(c.destination);
      o.type = type || 'sine';
      o.frequency.setValueAtTime(freq, c.currentTime + (delay||0));
      g.gain.setValueAtTime(volume||0.3, c.currentTime + (delay||0));
      g.gain.exponentialRampToValueAtTime(0.001, c.currentTime + (delay||0) + duration);
      o.start(c.currentTime + (delay||0));
      o.stop(c.currentTime + (delay||0) + duration);
    } catch(e){}
  }

  return {
    toggle: function(){
      enabled = !enabled;
      localStorage.setItem('ace_sounds', enabled ? 'on' : 'off');
      return enabled;
    },
    isEnabled: function(){ return enabled; },

    // Card correct (Good/Easy)
    correct: function(){
      tone(523, 'sine', 0.12, 0.2);
      tone(659, 'sine', 0.12, 0.18, 0.1);
    },

    // Card wrong (Again)
    wrong: function(){
      tone(220, 'sawtooth', 0.15, 0.15);
      tone(180, 'sawtooth', 0.15, 0.12, 0.12);
    },

    // Card flip
    flip: function(){
      tone(440, 'sine', 0.08, 0.1);
    },

    // Session complete
    sessionDone: function(){
      var notes = [523,659,784,1047];
      notes.forEach(function(f,i){ tone(f,'sine',0.18,0.22,i*0.1); });
    },

    // Streak milestone (every 10 days)
    streakMilestone: function(){
      var melody = [523,587,659,698,784,880,988,1047];
      melody.forEach(function(f,i){ tone(f,'sine',0.2,0.25,i*0.08); });
      // Harmony
      setTimeout(function(){
        tone(659,'triangle',0.4,0.15);
        tone(784,'triangle',0.4,0.15);
      }, 200);
    },

    // Badge earned — fanfare
    badgeEarned: function(){
      // Triumphant ascending fanfare
      var fanfare = [392,523,659,784,659,784,1047];
      var times   = [0, 0.12, 0.24, 0.36, 0.52, 0.6, 0.72];
      fanfare.forEach(function(f,i){
        tone(f,'triangle',0.25,0.28,times[i]);
      });
      // Background chord swell
      setTimeout(function(){
        tone(523,'sine',0.6,0.12);
        tone(659,'sine',0.6,0.10);
        tone(784,'sine',0.6,0.10);
      }, 500);
    },

    // Coin earned
    coin: function(){
      tone(880,'sine',0.06,0.2);
      tone(1100,'sine',0.08,0.18,0.05);
    },

    // Goal completed
    goalDone: function(){
      var notes = [523,659,784,1047];
      notes.forEach(function(f,i){ tone(f,'sine',0.22,0.2,i*0.09); });
    }
  };
})();
