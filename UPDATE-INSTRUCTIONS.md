# The Brief — Archive + pictures + formatting (v6)

Replace **index.html**, **app.js**, and **sw.js** in the root of your existing GitHub Pages repository with the three files supplied in this ZIP. Keep your existing icons, manifest, and other files; do NOT upload a new repository or use an API key.

## What's new
- Archive tab automatically retains full imported editions, and lets you search or reopen older days.
- Settings > Export backup produces a JSON file containing archived editions and reading states. Restore backup imports it. iPhone browser data is not permanent; export backups periodically.
- Every article has an **Add picture** button. Paste a direct public HTTPS image URL ending in jpg/png/webp if possible. You can change it or clear it later. ChatGPT's Copy action does not generally include image URLs, and the app cannot legally or reliably scrape publisher photos on its own. If the image host blocks hotlinking, the article's visual fallback stays.
- More spacious article typography, better headings and tables, and optional KaTeX equation rendering when the CDN loads. All raw article text continues to be stored unmodified and the full-original comparison remains.

## Deploy
1. Upload these three files to the top level of your existing GitHub repository and commit.
2. Confirm the Pages deployment finishes.
3. Close the Home Screen app and reopen it. If it looks old, visit the GitHub Pages URL in Safari and reload.
4. Import a briefing normally, then open Archive and try Add picture on an article.

**Important:** The app preserves only text actually delivered by ChatGPT's Copy action. Equation typesetting relies on an external CDN and may fall back to readable plain text offline. Pictures must be added manually with URLs; copyrighted press imagery should only be embedded where permitted.
