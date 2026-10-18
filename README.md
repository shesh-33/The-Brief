# The Brief — iPhone home-screen web app

A lightweight, installable Progressive Web App for five economics stories each day.

## Features
- One story card at a time, with summary, "why it matters", image (optional), and original source link.
- Swipe **left** to mark read and dismiss; swipe **right** to save for later. Buttons provide equivalent accessible controls.
- Progress and bookmarks retained locally on the device.
- Five-story daily JSON import; or experimental copy-and-paste text import from a ChatGPT briefing.
- Optional JSON feed URL with refresh upon opening.
- Works offline after initial successful visit (but the feed and external sources require internet).
- Installs through Safari > Share > Add to Home Screen when hosted at HTTPS.

## Get it online using GitHub Pages
1. From your Mac, create a **public** GitHub repository, e.g. `the-brief`. Do **not** upload private keys or sensitive data.
2. Upload **all files in this folder** to the repository root (`index.html`, `app.js`, `sw.js`, icons, manifest, and optionally `daily.json`).
3. In repository Settings > Pages, choose Deploy from a branch, branch `main`, folder `/ (root)`, and save.
4. Wait for GitHub to show the Pages URL, typically `https://USERNAME.github.io/the-brief/`.
5. Open that URL in Safari on your iPhone, tap Share, then **Add to Home Screen**.
6. Open Settings inside the app to import the day's five stories. If you host `daily.json`, configure your Pages URL plus `daily.json` as the feed URL.

If editing the repo on your Mac and previewing locally, run `python3 -m http.server 8000` from this folder, then visit `http://localhost:8000`. Service workers require a secure context, which localhost supports for desktop testing.

## Daily updating
The scheduled ChatGPT task is not directly connected to external app state. This app **does not automatically receive** your ChatGPT news briefings. The simplest reliable path is to paste the briefing or edit `daily.json` and publish it. For later automation, arrange for an external script or workflow to create exactly five verified articles daily and commit a new `daily.json` to your GitHub Pages repository. Don't put an OpenAI API key in any web page or GitHub repository file. Use GitHub Actions Secrets or a server-side secret manager.

### JSON schema
```
{
  "date": "2026-10-19",
  "stories": [
    {"id":"item-1","category":"Macroeconomics","headline":"...","summary":"...","why":"...","source":"...","url":"https://...","image":"https://..."},
    {"id":"item-2","category":"Development economics","headline":"...","summary":"...","why":"...","source":"...","url":"https://..."},
    {"id":"item-3","category":"World affairs","headline":"...","summary":"...","why":"...","source":"...","url":"https://..."},
    {"id":"item-4","category":"AI and technology","headline":"...","summary":"...","why":"...","source":"...","url":"https://..."},
    {"id":"item-5","category":"Econometrics","headline":"...","summary":"...","why":"...","source":"...","url":"https://..."}
  ]
}
```
Images are optional. Use licensed or publisher-permitted image URLs; absent images show a visual placeholder. The supplied edition is **illustrative sample content**, not a continuously updated verified news feed.

## Limitations
- Saved state does not sync across devices and may be lost when local site data is cleared.
- Native interactive iPhone Home Screen widgets are not possible with a standalone PWA; the app icon opens the full interface.
- Copying a rich ChatGPT reply into plain text may omit or mangle images and citations. JSON imports are most reliable.
- On iOS, the browser may sometimes evict cached files; opening online restores them.
