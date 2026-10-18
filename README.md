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

## NEW: Automatic daily updates with GitHub Actions

The downloaded upgrade includes `.github/workflows/daily-brief.yml` and `generate_daily.py`. **Upload the new files, including the hidden `.github` directory, to the root of your existing repository.** You do not need a new repository. `app.js` now automatically fetches `daily.json` from the same website when opened. New data appears automatically after the workflow publishes; your existing Home Screen icon keeps working.

### One-time setup on GitHub
1. Create an OpenAI API key at https://platform.openai.com/api-keys and add API billing/usage limits if needed. **The API is a separately billed product; a ChatGPT subscription does not cover it.**
2. In your GitHub repository, select **Settings → Secrets and variables → Actions → New repository secret**. Name it exactly `OPENAI_API_KEY`, and paste the API key into the value field. **Never put the key in a public file or share it in chat.**
3. Under **Settings → Actions → General → Workflow permissions**, select **Read and write permissions** if your repository's policy requires it. Save. The workflow also declares `contents: write`.
4. In the **Actions** tab, select **Publish daily economics briefing → Run workflow** to test it. When the run succeeds, the repository's `daily.json` will change. Check that it contains five verifiable links.
5. Open the iPhone app online. It automatically loads `daily.json`. In app Settings, use **Refresh now** if needed. An existing custom feed URL overrides the default; clear it and save to restore the default feed URL, or use your Pages URL plus `/daily.json`.

The workflow starts at **7:40 AM America/Chicago** to aim for an edition around 8:00 AM, but **GitHub Actions scheduled jobs are not guaranteed to start precisely on time**. On failure, the previously published file remains available; inspect the Actions log. Scheduled workflows in public repositories may be disabled after 60 days of no activity. The workflow must be present on the default branch. Source checking is model-based and not a substitute for editorial fact-checking.

**This is a separate daily AI-generated briefing.** ChatGPT's built-in scheduled task cannot directly publish its response to GitHub or supply the API key to this job. The content can be similar but will not be exactly the same. It uses OpenAI API web search, which has usage charges. The image field remains blank deliberately: automatically hotlinking publisher images without permission is unreliable and can violate image reuse terms; the app displays its visual fallback.

To disable automated updates, disable the workflow under GitHub Actions. Your existing ChatGPT scheduled task is unaffected.
