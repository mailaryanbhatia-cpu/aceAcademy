#!/bin/bash
# ─────────────────────────────────────────────────────
#  aceAcademy — Deploy to GitHub Pages
#  Double-click this file to publish your site live.
# ─────────────────────────────────────────────────────

GITHUB_TOKEN="YOUR_TOKEN_HERE"
GITHUB_USER="mailaryanbhatia-cpu"
REPO_NAME="aceAcademy"

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║   aceAcademy — GitHub Pages Deployer    ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# ── Step 1: Create the GitHub repo ───────────────────
echo "→ Creating GitHub repository..."
RESPONSE=$(curl -s -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d "{\"name\":\"$REPO_NAME\",\"description\":\"Khan Academy-style curriculum for grades 6-12 with full practice problems\",\"private\":false,\"auto_init\":false}")

REPO_URL=$(echo "$RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('html_url',''))" 2>/dev/null)

if [ -z "$REPO_URL" ]; then
  # Repo might already exist — check
  EXISTS=$(curl -s -o /dev/null -w "%{http_code}" \
    -H "Authorization: token $GITHUB_TOKEN" \
    https://api.github.com/repos/$GITHUB_USER/$REPO_NAME)
  if [ "$EXISTS" = "200" ]; then
    echo "   Repository already exists — continuing."
    REPO_URL="https://github.com/$GITHUB_USER/$REPO_NAME"
  else
    echo "✗ Failed to create repository. Response:"
    echo "$RESPONSE"
    read -p "Press Enter to exit..."
    exit 1
  fi
else
  echo "   ✓ Repository created: $REPO_URL"
fi

# ── Step 2: Configure git ─────────────────────────────
echo ""
echo "→ Configuring git..."
git config --global user.email "jagasia.deepti@gmail.com" 2>/dev/null
git config --global user.name "$GITHUB_USER" 2>/dev/null

# ── Step 3: Init repo and commit ─────────────────────
echo "→ Initializing git repository..."
if [ -d ".git" ]; then
  rm -rf .git
fi
git init -b main
git add *.html *.js *.css *.py *.command 2>/dev/null || true
git add . 2>/dev/null || true
git commit -m "Update — aceAcademy full curriculum sync"

# ── Step 4: Push to GitHub ────────────────────────────
echo ""
echo "→ Pushing to GitHub (this may take 30-60 seconds for the large file)..."
REMOTE_URL="https://$GITHUB_USER:$GITHUB_TOKEN@github.com/$GITHUB_USER/$REPO_NAME.git"
git remote add origin "$REMOTE_URL"
git push -u origin main

if [ $? -ne 0 ]; then
  echo ""
  echo "✗ Push failed. Trying force push..."
  git push -u origin main --force
fi

# ── Step 5: Enable GitHub Pages ───────────────────────
echo ""
echo "→ Enabling GitHub Pages..."
sleep 3
curl -s -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/$GITHUB_USER/$REPO_NAME/pages \
  -d '{"source":{"branch":"main","path":"/"}}' > /dev/null

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║  ✓ DONE! Your site will be live in ~60 seconds at:      ║"
echo "║                                                          ║"
echo "║  https://mailaryanbhatia-cpu.github.io/aceAcademy       ║"
echo "║                                                          ║"
echo "║  GitHub repo: https://github.com/mailaryanbhatia-cpu/aceAcademy ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Open the GitHub repo in browser
open "https://github.com/$GITHUB_USER/$REPO_NAME"

echo "Opening your repo in the browser..."
echo ""
read -p "Press Enter to close this window..."
