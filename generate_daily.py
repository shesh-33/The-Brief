"""Generate the public five-story daily.json for the Brief PWA.
Requires OPENAI_API_KEY in environment. Never commit the key.
"""
import json
import os
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
DAY = datetime.now(ZoneInfo('America/Chicago')).date().isoformat()
OUTPUT = ROOT / 'daily.json'
MODEL = os.environ.get('BRIEF_MODEL', 'gpt-5-mini')

INSTRUCTIONS = '''You are an unusually careful economics news editor writing for an economics/mathematics undergraduate preparing for graduate work. Use web search to verify current reporting, exact publication dates, and live source links. Produce EXACTLY five distinct news stories and research analyses, covering a balanced sample of economics and economic research, U.S. policy, global affairs, finance, AI, econometrics, development economics, and occasional JEP research. Prioritize substantial developments during the previous 48 hours; include one particularly worthwhile scholarly paper when available, noting its publication date. Do not invent studies or claims. Never repeat a story merely to fill space. Each item needs: id (1..5 as strings), category, headline, summary (110-160 words with concrete details and appropriate caveats), why (45-90 words explaining economic mechanisms and, where useful, an econometric identification question), source (publisher name), url (DIRECT article/report/paper HTTPs URL, not a homepage), image (empty string). Five unique source links, no speculative unverified figures. Dates refer to America/Chicago. Do not use fake or stock photo URLs. Respond with ONLY a JSON object with top-level date in YYYY-MM-DD and stories array. No markdown, footnotes, citations markup, or extra fields. If a claim cannot be verified, omit it. For research articles, distinguish publication from coverage date.'''


def clean_text(v, limit):
    return re.sub(r'\s+', ' ', str(v)).strip()[:limit]


def validate(payload):
    if not isinstance(payload, dict) or payload.get('date') != DAY:
        raise ValueError('Unexpected date in generated edition')
    raw = payload.get('stories')
    if not isinstance(raw, list) or len(raw) != 5:
        raise ValueError('Edition must contain exactly five stories')
    urls = set()
    result = []
    for idx, s in enumerate(raw, 1):
        if not isinstance(s, dict):
            raise ValueError('Invalid story')
        url = str(s.get('url', '')).strip()
        parsed = urlparse(url)
        if parsed.scheme != 'https' or not parsed.netloc or parsed.hostname in ('example.com', 'localhost'):
            raise ValueError(f'Invalid source URL for story {idx}: {url}')
        if url in urls:
            raise ValueError('Duplicate source URL')
        urls.add(url)
        item = {'id': str(idx)}
        for key, limit in [('category', 80), ('headline', 220), ('summary', 3000), ('why', 1600), ('source', 100)]:
            item[key] = clean_text(s.get(key, ''), limit)
            if len(item[key]) < 5:
                raise ValueError(f'Missing {key} for story {idx}')
        item['url'] = url
        item['image'] = ''  # Image URLs require independent reuse permission.
        result.append(item)
    return {'date': DAY, 'stories': result}


def main():
    if not os.environ.get('OPENAI_API_KEY'):
        raise RuntimeError('OPENAI_API_KEY must be set as a GitHub Actions secret')
    client = OpenAI()
    response = client.responses.create(
        model=MODEL,
        tools=[{'type': 'web_search'}],
        instructions=INSTRUCTIONS,
        input=f'Prepare the 8 AM daily brief for {DAY} (America/Chicago). Verify the five source article URLs with web search before using them. Output JSON only.',
    )
    text = response.output_text.strip()
    if text.startswith('```'):
        text = re.sub(r'^```(?:json)?\s*|\s*```$', '', text).strip()
    payload = validate(json.loads(text))
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Created {OUTPUT} for {DAY} with five articles')


if __name__ == '__main__':
    main()
