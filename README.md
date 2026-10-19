# The Brief — free manual ChatGPT import

## Install this update in your existing GitHub Pages app

1. Unzip the download on your Mac.
2. Open the existing GitHub repository for The Brief, and upload these files at the **repository root**: `index.html`, `app.js`, `sw.js`, `manifest.webmanifest`, `icon-192.png`, and `icon-512.png`. Replace existing versions.
3. Delete `.github/workflows/daily-brief.yml` or disable its scheduled workflow under GitHub **Actions** if you previously uploaded it. It is unnecessary and will fail without an API key. You can also delete `generate_daily.py`.
4. Give GitHub Pages a moment to publish. On your iPhone, close and reopen The Brief. If the older version persists, open the GitHub Pages URL in Safari and refresh it before returning to the Home Screen app.

## Import your five daily stories

1. Open the ChatGPT daily briefing and tap **Copy** on the complete response. Include the numbered story headlines.
2. Open **The Brief** on your iPhone, tap **Settings**, paste in **Import today's edition**, then tap **Import briefing**.
3. Tap **Today**. You'll see the five stories as cards. Swipe left or press Done reading to dismiss; swipe right or press Save to bookmark.

No API key, subscription, secrets, server, or extra app needed. The content and reading state remain in that device's local storage.

**Important limitations:** Rich embedded citation widgets from ChatGPT may not become regular URLs when copied. The importer preserves normal Markdown or bare HTTPS links but cannot reconstruct missing source URLs. Photos embedded in ChatGPT responses are not reliably copyable and will appear as visual placeholders unless you import an image URL through JSON. Text import is heuristic—review imported cards, especially headlines and summaries. The hosted `daily.json` feed is now **off by default** to protect manual imports.

## Formatting tip

If copying a highly formatted ChatGPT briefing doesn't work, ask ChatGPT to reformat today's five stories as a plain Markdown list numbered 1–5, including a two-paragraph summary, a `Why it matters` section, and normal Markdown links to sources. Copy that and import it.
