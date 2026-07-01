#!/usr/bin/env python3
"""Fix the drawing canvas in worksheets.html — three targeted patches."""
import pathlib, re

p = pathlib.Path('/sessions/admiring-stoic-pascal/mnt/outputs/worksheets.html')
html = p.read_text(encoding='utf-8')

# ── PATCH 1: Call initVisibleCanvases after innerHTML is set ──────────────────
# Find the line right after wrap.innerHTML = `...`; and add a rAF call
old_after = "  document.getElementById('printBtn').classList.add('visible');\n}"
new_after = """  document.getElementById('printBtn').classList.add('visible');
  // Init canvases after layout settles
  requestAnimationFrame(() => requestAnimationFrame(initVisibleCanvases));
}"""

assert old_after in html, "Patch 1 anchor not found!"
html = html.replace(old_after, new_after, 1)
print("✅ Patch 1: initVisibleCanvases called after render")

# ── PATCH 2: Replace the broken drawing JS with a robust version ──────────────
# Find and remove the old drawing JS block
old_js_start = '// ══════════════════════════════════════════════════════════════\n//  DRAWING CANVAS ENGINE'
old_js_end   = '_canvasObserver.observe(document.body, { childList: true, subtree: true, attributes: true });\nsetTimeout(initVisibleCanvases, 300);'

js_start_idx = html.find(old_js_start)
js_end_idx   = html.find(old_js_end)
assert js_start_idx != -1, "Drawing JS start not found"
assert js_end_idx   != -1, "Drawing JS end not found"

old_js = html[js_start_idx : js_end_idx + len(old_js_end)]

NEW_JS = r"""// ══════════════════════════════════════════════════════════════
//  DRAWING CANVAS ENGINE  (robust v2)
// ══════════════════════════════════════════════════════════════
const _canvasState = {};

function getState(id) {
  if (!_canvasState[id]) {
    _canvasState[id] = { tool:'pen', color:'#1e293b', size:2, drawing:false, history:[], lastX:0, lastY:0 };
  }
  return _canvasState[id];
}

function initCanvas(id) {
  const cv = document.getElementById('canvas-' + id);
  if (!cv) return false;

  const rect = cv.getBoundingClientRect();
  const w = rect.width > 0 ? rect.width : (cv.parentElement ? cv.parentElement.getBoundingClientRect().width : 0);
  if (w === 0) return false;  // not laid out yet — will retry

  const dpr = window.devicePixelRatio || 1;
  const h = 220;

  // Only resize if dimensions changed or never set
  if (cv.dataset.initW === String(Math.round(w))) return true;
  cv.dataset.initW = String(Math.round(w));

  cv.width  = Math.round(w * dpr);
  cv.height = Math.round(h * dpr);
  cv.style.width  = w + 'px';
  cv.style.height = h + 'px';

  const ctx = cv.getContext('2d');
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.scale(dpr, dpr);

  // Lined-paper background
  drawBackground(ctx, w, h);
  saveHistory(id, cv);
  return true;
}

function drawBackground(ctx, w, h) {
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, w, h);
  ctx.strokeStyle = '#e2e8f0';
  ctx.lineWidth = 1;
  for (let y = 30; y < h; y += 30) {
    ctx.beginPath();
    ctx.moveTo(12, y);
    ctx.lineTo(w - 4, y);
    ctx.stroke();
  }
  // Left margin line
  ctx.strokeStyle = '#fca5a5';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(36, 0);
  ctx.lineTo(36, h);
  ctx.stroke();
}

function saveHistory(id, cv) {
  if (!cv) cv = document.getElementById('canvas-' + id);
  if (!cv) return;
  const st = getState(id);
  try {
    st.history.push(cv.toDataURL());
    if (st.history.length > 25) st.history.shift();
  } catch(e) {}
}

function getPos(e, cv) {
  const rect = cv.getBoundingClientRect();
  const src = e.touches ? e.touches[0] : e;
  return {
    x: (src.clientX - rect.left),
    y: (src.clientY - rect.top)
  };
}

function startDraw(e, id) {
  e.preventDefault();
  if (!initCanvas(id)) return;
  const cv = document.getElementById('canvas-' + id);
  const st = getState(id);
  st.drawing = true;
  const pos = getPos(e, cv);
  st.lastX = pos.x;
  st.lastY = pos.y;
  // Draw a dot on single tap/click
  const ctx = cv.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  if (st.tool === 'eraser') {
    ctx.globalCompositeOperation = 'source-over';
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(pos.x, pos.y, st.size * 3, 0, Math.PI * 2);
    ctx.fill();
  } else {
    ctx.globalCompositeOperation = 'source-over';
    ctx.fillStyle = st.color;
    ctx.beginPath();
    ctx.arc(pos.x, pos.y, st.size / 2, 0, Math.PI * 2);
    ctx.fill();
  }
}

function draw(e, id) {
  e.preventDefault();
  const st = getState(id);
  if (!st.drawing) return;
  const cv = document.getElementById('canvas-' + id);
  if (!cv) return;
  const ctx = cv.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const pos = getPos(e, cv);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.lineWidth   = st.tool === 'eraser' ? st.size * 6 : st.size;
  ctx.lineCap     = 'round';
  ctx.lineJoin    = 'round';
  ctx.strokeStyle = st.tool === 'eraser' ? '#ffffff' : st.color;
  ctx.globalCompositeOperation = st.tool === 'eraser' ? 'source-over' : 'source-over';
  if (st.tool === 'eraser') ctx.strokeStyle = '#ffffff';
  ctx.beginPath();
  ctx.moveTo(st.lastX, st.lastY);
  ctx.lineTo(pos.x, pos.y);
  ctx.stroke();
  st.lastX = pos.x;
  st.lastY = pos.y;
}

function endDraw(id) {
  const st = getState(id);
  if (!st.drawing) return;
  st.drawing = false;
  saveHistory(id);
}

function setTool(id, tool) {
  getState(id).tool = tool;
  const penBtn   = document.getElementById('pen-' + id);
  const eraseBtn = document.getElementById('erase-' + id);
  if (penBtn)   penBtn.classList.toggle('active',   tool === 'pen');
  if (eraseBtn) eraseBtn.classList.toggle('active', tool === 'eraser');
}

function setColor(id, color, el) {
  const st = getState(id);
  st.color = color;
  const tb = document.getElementById('tb-' + id);
  if (tb) tb.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('active'));
  if (el) el.classList.add('active');
  if (st.tool === 'eraser') setTool(id, 'pen');
}

function setSize(id, size, el) {
  getState(id).size = size;
  const tb = document.getElementById('tb-' + id);
  if (tb) tb.querySelectorAll('.size-btn').forEach(s => s.classList.remove('active'));
  if (el) el.classList.add('active');
}

function clearCanvas(id) {
  const cv = document.getElementById('canvas-' + id);
  if (!cv) return;
  const ctx = cv.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  const w = cv.offsetWidth || 600;
  const h = 220;
  drawBackground(ctx, w, h);
  saveHistory(id, cv);
}

function undoCanvas(id) {
  const st = getState(id);
  if (st.history.length <= 1) return;
  st.history.pop();
  const prev = st.history[st.history.length - 1];
  const cv = document.getElementById('canvas-' + id);
  if (!cv) return;
  const ctx = cv.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const img = new Image();
  img.onload = () => {
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, cv.width, cv.height);
    ctx.drawImage(img, 0, 0, cv.offsetWidth, 220);
  };
  img.src = prev;
}

function initVisibleCanvases() {
  document.querySelectorAll('.draw-canvas').forEach(cv => {
    const id = cv.id.replace('canvas-', '');
    initCanvas(id);
  });
}

// Re-init on resize
window.addEventListener('resize', () => {
  document.querySelectorAll('.draw-canvas').forEach(cv => {
    const id = cv.id.replace('canvas-', '');
    delete cv.dataset.initW;  // force reinit
    initCanvas(id);
  });
});"""

html = html.replace(old_js, NEW_JS)
print("✅ Patch 2: Drawing JS replaced with robust v2")

# ── PATCH 3: Fix canvas CSS height to match new 220px ────────────────────────
html = html.replace('.draw-canvas{display:block;width:100%;height:200px}',
                    '.draw-canvas{display:block;width:100%;height:220px}')
print("✅ Patch 3: Canvas CSS height updated to 220px")

p.write_text(html, encoding='utf-8')
print(f"✅ Saved — {p.stat().st_size // 1024} KB")

# Quick sanity checks
checks = [
    ("initVisibleCanvases called after render",   "requestAnimationFrame(() => requestAnimationFrame(initVisibleCanvases));" in html),
    ("robust v2 JS present",                       "DRAWING CANVAS ENGINE  (robust v2)" in html),
    ("drawBackground function exists",             "function drawBackground" in html),
    ("setTransform used instead of scale",         "setTransform(dpr" in html),
    ("no old broken observer",                     "_canvasObserver" not in html),
    ("canvas 220px height",                        "height:220px" in html),
]
print()
for label, result in checks:
    print(f"{'✅' if result else '❌'} {label}")
