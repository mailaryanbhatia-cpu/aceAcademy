# AcerAcademy

A free, static K-12 and AP study platform: curriculum browsers, quizzes, worksheets,
flashcards, an AI-style tutor, an essay grader, and 40+ other study tools, all
served from GitHub Pages at [academyacer.com](https://academyacer.com).

## Stack

Plain HTML/CSS/JS -- no build step, no framework, no server. Pages are served
directly by GitHub Pages. The only "backend" is Firebase (Spark/free tier):

- **Firebase Auth** -- Google sign-in for real accounts, plus a silent
  anonymous identity for signed-out visitors (`firebase-auth.js`).
- **Firestore** -- per-user cross-device sync of XP/streaks/quiz history
  (`firestore.js`), a hybrid content-management system for editing curriculum
  units without a redeploy (`admin.html` + `content-overrides.js`), and a
  site-wide analytics counter (`analytics.js`).
- **firestore.rules** -- the real security enforcement (client-side checks in
  `admin.html` are UI-only). Deployed manually via the Firebase Console --
  see the comments at the top of the file for the collections it covers.

Deliberately built without Cloud Functions, since enabling them requires
Firebase's paid Blaze plan regardless of usage -- everything here runs on the
free Spark tier. (`DEPLOY_FUNCTIONS.md` documents an optional Cloud
Functions-based path for wiring in a real AI model later, if that tradeoff is
ever worth it -- the site currently ships with canned/scripted responses in
the tutor and essay grader instead.)

## Repo layout

- `*.html` -- one file per tool/page (134 of them). Shared chrome lives in
  `ace-shared.css` / `ace-theme.css` / `theme.js` / `auth-guard.js`.
- `*-data.js` at the repo root -- shipped (minified) data files the pages
  actually load.
- `data-source/` -- the hand-editable originals of the 9 largest data files.
  Tracked via **Git LFS** (see `.gitattributes`) so their size doesn't bloat
  the main repo. Run `npm run build:data` after editing anything in here to
  regenerate the minified root-level copies, and `npm run verify:data` to
  confirm they haven't drifted apart.
- `scripts/` -- `site-audit.js` (syntax/link audit), `check-page-errors.js`
  (catches load-time JS errors across every page), `build-data.js`.
- `tests/` -- jsdom-based functional smoke tests (`run-all.js` runs all of
  them).

## Running tests locally

```bash
npm install
npm test
```

This runs the full CI suite: site audit, functional smoke tests, the
data-source/shipped-data drift check, and the page-load error check. CI
(`.github/workflows/site-audit.yml`) runs the same on every push/PR to
`main`.

## Deployment

Push to `main` -- GitHub Pages auto-builds and deploys (~1-2 min, plus up to
~10 min for the CDN cache to catch up). There is no separate deploy step.

Firestore rules are **not** auto-deployed -- after editing `firestore.rules`,
paste the new contents into Firebase Console -> Firestore Database -> Rules
-> Publish.
