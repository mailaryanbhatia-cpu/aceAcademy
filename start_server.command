#!/bin/bash
# ─────────────────────────────────────────────
#  EduCurriculum — Local Dev Server
#  Double-click this file to start the server,
#  then open http://localhost:8000 in your browser
# ─────────────────────────────────────────────

# Get the directory where this script lives
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo ""
echo "╔══════════════════════════════════════╗"
echo "║   EduCurriculum Local Server         ║"
echo "║   http://localhost:8000              ║"
echo "╚══════════════════════════════════════╝"
echo ""
echo "Opening browser..."
sleep 1
open "http://localhost:8000"

echo "Server running. Press Ctrl+C to stop."
echo ""

# Start server (Python 3 built into macOS)
python3 -m http.server 8000
