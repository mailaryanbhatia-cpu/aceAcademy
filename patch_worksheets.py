#!/usr/bin/env python3
import pathlib, re

p = pathlib.Path('/sessions/admiring-stoic-pascal/mnt/outputs/worksheets.html')
html = p.read_text(encoding='utf-8')

# ── 1. Replace CSS ────────────────────────────────────────────────────────────
old_css = """.work-area{margin-top:14px;border-top:1px dashed var(--border);padding-top:14px}
.work-lines{display:flex;flex-direction:column;gap:10px;margin-top:8px}
.work-line{border-bottom:1px solid #e5e7eb;height:28px;width:100%}"""

new_css = """.work-area{margin-top:16px;border-top:1px dashed var(--border);padding-top:12px}
.canvas-toolbar{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:8px;padding:6px 8px;background:#f8fafc;border:1px solid var(--border);border-radius:8px}
.tool-btn{width:30px;height:30px;border:1px solid var(--border);border-radius:6px;background:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:.9rem;transition:all .15s}
.tool-btn:hover,.tool-btn.active{background:var(--accent);border-color:var(--accent);color:#fff}
.tool-btn.active{box-shadow:0 0 0 2px #93c5fd}
.color-swatch{width:22px;height:22px;border-radius:4px;border:2px solid transparent;cursor:pointer;transition:border-color .1s;flex-shrink:0}
.color-swatch.active{border-color:#1e293b;transform:scale(1.2)}
.size-btn{width:26px;height:26px;border:1px solid var(--border);border-radius:5px;background:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s}
.size-btn.active{background:var(--accent);border-color:var(--accent)}
.canvas-wrap{position:relative;border:1px solid #d1d5db;border-radius:8px;background:#fff;overflow:hidden;cursor:crosshair;touch-action:none}
.draw-canvas{display:block;width:100%;height:200px}
.canvas-actions{display:flex;gap:6px;margin-top:6px;justify-content:flex-end}
.ca-btn{padding:4px 12px;font-size:.75rem;border:1px solid var(--border);border-radius:6px;background:#fff;cursor:pointer;font-weight:600;color:var(--muted);transition:all .15s}
.ca-btn:hover{border-color:var(--accent);color:var(--accent)}
.ca-btn.danger:hover{border-color:#ef4444;color:#ef4444}"""

assert old_css in html, "CSS block not found!"
html = html.replace(old_css, new_css)
print("✅ CSS replaced")

# ── 2. Replace the work-area HTML generation in JS ────────────────────────────
old_html = """<div class="work-area">
            <div style="font-size:.75rem;color:var(--muted);font-weight:600;letter-spacing:.05em">WORK SPACE</div>
            <div class="work-lines">${'<div class="work-line"></div>'.repeat(4)}</div>
          </div>"""

new_html = """<div class="work-area">
            <div style="font-size:.72rem;color:var(--muted);font-weight:700;letter-spacing:.08em;margin-bottom:6px">✏️ WORK SPACE</div>
            <div class="canvas-toolbar" id="tb-${i}">
              <span style="font-size:.7rem;color:var(--muted);font-weight:600">Tool:</span>
              <button class="tool-btn active" id="pen-${i}" title="Pen" onclick="setTool('${i}','pen')">🖊</button>
              <button class="tool-btn" id="erase-${i}" title="Eraser" onclick="setTool('${i}','eraser')">⬜</button>
              <div style="width:1px;height:22px;background:var(--border);margin:0 2px"></div>
              <span style="font-size:.7rem;color:var(--muted);font-weight:600">Color:</span>
              <div class="color-swatch active" style="background:#1e293b" onclick="setColor('${i}','#1e293b',this)" title="Black"></div>
              <div class="color-swatch" style="background:#2563eb" onclick="setColor('${i}','#2563eb',this)" title="Blue"></div>
              <div class="color-swatch" style="background:#dc2626" onclick="setColor('${i}','#dc2626',this)" title="Red"></div>
              <div class="color-swatch" style="background:#16a34a" onclick="setColor('${i}','#16a34a',this)" title="Green"></div>
              <div class="color-swatch" style="background:#9333ea" onclick="setColor('${i}','#9333ea',this)" title="Purple"></div>
              <div style="width:1px;height:22px;background:var(--border);margin:0 2px"></div>
              <span style="font-size:.7rem;color:var(--muted);font-weight:600">Size:</span>
              <button class="size-btn active" id="sz-${i}-2" onclick="setSize('${i}',2,this)" title="Thin">•</button>
              <button class="size-btn" id="sz-${i}-5" onclick="setSize('${i}',5,this)" title="Medium">●</button>
              <button class="size-btn" id="sz-${i}-10" onclick="setSize('${i}',10,this)" title="Thick">⬤</button>
              <div style="flex:1"></div>
              <button class="tool-btn" title="Undo" onclick="undoCanvas('${i}')">↩</button>
            </div>
            <div class="canvas-wrap">
              <canvas class="draw-canvas" id="canvas-${i}" onmousedown="startDraw(event,'${i}')" onmousemove="draw(event,'${i}')" onmouseup="endDraw('${i}')" onmouseleave="endDraw('${i}')" ontouchstart="startDraw(event,'${i}')" ontouchmove="draw(event,'${i}')" ontouchend="endDraw('${i}')"></canvas>
            </div>
            <div class="canvas-actions">
              <button class="ca-btn danger" onclick="clearCanvas('${i}')">🗑 Clear</button>
            </div>
          </div>"""

assert old_html in html, "HTML work-area block not found!"
html = html.replace(old_html, new_html)
print("✅ Work-area HTML replaced")

# ── 3. Inject drawing JS before closing </script> ─────────────────────────────
drawing_js = """
// ══════════════════════════════════════════════════════════════
//  DRAWING CANVAS ENGINE
// ══════════════════════════════════════════════════════════════
const _canvas = {};  // per-problem state

function getState(id) {
  if (!_canvas[id]) {
    _canvas[id] = { tool:'pen', color:'#1e293b', size:2, drawing:false, history:[] };
  }
  return _canvas[id];
}

function initCanvas(id) {
  const cv = document.getElementById('canvas-' + id);
  if (!cv || cv.dataset.init) return;
  cv.dataset.init = '1';
  // Set physical pixel size
  const w = cv.offsetWidth || cv.parentElement.offsetWidth || 600;
  cv.width  = w * window.devicePixelRatio;
  cv.height = 200 * window.devicePixelRatio;
  cv.style.height = '200px';
  const ctx = cv.getContext('2d');
  ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  // Lined-paper background
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, w, 200);
  ctx.strokeStyle = '#e5e7eb';
  ctx.lineWidth = 1;
  for (let y = 28; y < 200; y += 28) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
  }
  saveHistory(id);
}

function saveHistory(id) {
  const cv = document.getElementById('canvas-' + id);
  if (!cv) return;
  const st = getState(id);
  st.history.push(cv.toDataURL());
  if (st.history.length > 20) st.history.shift();
}

function getPos(e, cv) {
  const rect = cv.getBoundingClientRect();
  const src = e.touches ? e.touches[0] : e;
  return { x: src.clientX - rect.left, y: src.clientY - rect.top };
}

function startDraw(e, id) {
  e.preventDefault();
  initCanvas(id);
  const st = getState(id);
  st.drawing = true;
  const cv = document.getElementById('canvas-' + id);
  const ctx = cv.getContext('2d');
  const pos = getPos(e, cv);
  ctx.beginPath();
  ctx.moveTo(pos.x, pos.y);
  st.lastX = pos.x; st.lastY = pos.y;
}

function draw(e, id) {
  e.preventDefault();
  const st = getState(id);
  if (!st.drawing) return;
  const cv = document.getElementById('canvas-' + id);
  const ctx = cv.getContext('2d');
  const pos = getPos(e, cv);
  ctx.lineWidth   = st.tool === 'eraser' ? st.size * 5 : st.size;
  ctx.lineCap     = 'round';
  ctx.lineJoin    = 'round';
  ctx.strokeStyle = st.tool === 'eraser' ? '#ffffff' : st.color;
  ctx.globalCompositeOperation = st.tool === 'eraser' ? 'destination-out' : 'source-over';
  ctx.beginPath();
  ctx.moveTo(st.lastX, st.lastY);
  ctx.lineTo(pos.x, pos.y);
  ctx.stroke();
  st.lastX = pos.x; st.lastY = pos.y;
}

function endDraw(id) {
  const st = getState(id);
  if (!st.drawing) return;
  st.drawing = false;
  const cv = document.getElementById('canvas-' + id);
  const ctx = cv.getContext('2d');
  ctx.globalCompositeOperation = 'source-over';
  saveHistory(id);
}

function setTool(id, tool) {
  getState(id).tool = tool;
  document.getElementById('pen-' + id).classList.toggle('active', tool === 'pen');
  document.getElementById('erase-' + id).classList.toggle('active', tool === 'eraser');
}

function setColor(id, color, el) {
  getState(id).color = color;
  const tb = document.getElementById('tb-' + id);
  tb.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('active'));
  el.classList.add('active');
  // Auto-switch to pen if on eraser
  if (getState(id).tool === 'eraser') setTool(id, 'pen');
}

function setSize(id, size, el) {
  getState(id).size = size;
  const tb = document.getElementById('tb-' + id);
  tb.querySelectorAll('.size-btn').forEach(s => s.classList.remove('active'));
  el.classList.add('active');
}

function clearCanvas(id) {
  const cv = document.getElementById('canvas-' + id);
  if (!cv) return;
  const ctx = cv.getContext('2d');
  const w = cv.offsetWidth || 600;
  ctx.globalCompositeOperation = 'source-over';
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, w, 200);
  ctx.strokeStyle = '#e5e7eb';
  ctx.lineWidth = 1;
  for (let y = 28; y < 200; y += 28) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
  }
  saveHistory(id);
}

function undoCanvas(id) {
  const st = getState(id);
  if (st.history.length <= 1) return;
  st.history.pop();
  const prev = st.history[st.history.length - 1];
  const cv = document.getElementById('canvas-' + id);
  const ctx = cv.getContext('2d');
  const img = new Image();
  img.onload = () => {
    ctx.globalCompositeOperation = 'source-over';
    ctx.clearRect(0, 0, cv.width, cv.height);
    ctx.drawImage(img, 0, 0, cv.offsetWidth, 200);
  };
  img.src = prev;
}

// Init all visible canvases on render; re-init on scroll into view
function initVisibleCanvases() {
  document.querySelectorAll('.draw-canvas').forEach(cv => {
    if (!cv.dataset.init && cv.offsetParent !== null) {
      initCanvas(cv.id.replace('canvas-', ''));
    }
  });
}
// Watch for new canvases appearing (when units open)
const _canvasObserver = new MutationObserver(initVisibleCanvases);
_canvasObserver.observe(document.body, { childList: true, subtree: true, attributes: true });
setTimeout(initVisibleCanvases, 300);
"""

last_script = html.rfind('</script>')
assert last_script != -1, "</script> not found"
html = html[:last_script] + drawing_js + '\n' + html[last_script:]
print("✅ Drawing JS injected")

p.write_text(html, encoding='utf-8')
print(f"✅ Saved — {p.stat().st_size // 1024} KB")
