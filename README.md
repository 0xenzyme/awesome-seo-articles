# Awesome SEO Articles

This repository is a Markdown corpus of SEO and digital marketing articles collected from public web sources.

## Current Corpus

- `ahrefs-blog/`
- `semrush-blog/`
- `google-search-central-blog/`

Each article file contains YAML-style frontmatter with source metadata, original URL, canonical URL, dates, fetch timestamp, hash, content type, freshness risk, and cleaned word/character counts.

## Public Release Caution

This repository currently includes full article text from third-party sources. Before publishing it as a public GitHub repository, verify redistribution rights for each source:

- Ahrefs and Semrush articles should be treated as copyrighted third-party material unless explicit permission is confirmed.
- Google Search Central content may have separate licensing and attribution requirements.
- If redistribution is not confirmed, prefer publishing metadata indexes and source links instead of full article bodies.

## Preprocessing

Run:

```powershell
python -X utf8 scripts/preprocess_public_repo.py
```

Generated outputs:

- `metadata/index.csv`
- `metadata/index.jsonl`
- `metadata/source-summary.json`
- `reports/publication-audit.md`

The preprocessing script is read-only with respect to article files. It builds indexes, source summaries, duplicate canonical checks, and public-release risk notes.

