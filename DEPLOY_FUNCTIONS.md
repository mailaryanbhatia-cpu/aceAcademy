# Deploy Firebase Cloud Functions (one-time setup)

This removes the need for students to enter their own Claude API key.

## Prerequisites
```bash
npm install -g firebase-tools
firebase login
```

## 1. Set your Anthropic API key as a secret
```bash
cd /path/to/aceAcademy
firebase functions:secrets:set ANTHROPIC_KEY
# paste your sk-ant-... key when prompted
```

## 2. Install function dependencies
```bash
cd functions
npm install
cd ..
```

## 3. Deploy
```bash
firebase deploy --only functions
```

That's it. The `claudeChat` Cloud Function will handle all AI calls server-side.
Students will automatically use the function (no key prompt) once they're signed in.

## How it works
- `claude-api.js` checks for Firebase callable functions first
- If available (and student is signed in), routes through Cloud Function
- Falls back to direct API + student's own key if not available
- Cloud Function enforces auth, rate-limits via Firebase, and caps tokens at 1500
