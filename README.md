# Awesome SEO Articles

Markdown corpus of public SEO and digital marketing articles, with source metadata and generated indexes. The snapshot dated 2026-10-12 contains 4272 articles. Current counts live in [`metadata/source-summary.json`](metadata/source-summary.json).

| Source | Directory | Articles | Words |
| --- | --- | ---: | ---: |
| Ahrefs Blog | `ahrefs-blog/` | 1194 | 2,900,308 |
| Semrush Blog | `semrush-blog/` | 1423 | 3,961,550 |
| Google Search Central Blog | `google-search-central-blog/` | 1655 | 615,042 |

Each article is cleaned Markdown plus YAML frontmatter: title, source, original URL, canonical URL, author, dates, fetch time, content hash, content type, freshness, and cleaned word and character counts.

## Layout

Articles sit in category subdirectories. Files placed directly in a source directory are skipped by the indexer, including `google-search-central-blog/INDEX-BY-YEAR.md`.

Ahrefs categories: `affiliate-marketing`, `ahrefs-insights`, `ai-search`, `content-marketing`, `data-studies`, `enterprise-seo`, `general-marketing`, `general-seo`, `keyword-research`, `link-building`, `local-seo`, `on-page-seo`, `paid-marketing`, `product-blog`, `technical-seo`, `uncategorized`, `video-marketing`.

Semrush categories: `ai`, `analytics`, `competitor-intelligence-research`, `content`, `ecommerce`, `frequently-asked-questions`, `general-marketing`, `general-seo`, `industry-news`, `keyword-research`, `link-building`, `local-seo`, `on-page-seo`, `original-research-studies`, `paid-advertising`, `semrush`, `semrush-product`, `social-media`, `technical-seo`, `uncategorized`, `video-marketing`.

Google Search Central is grouped by content type: `blog-article`, `event`, `search-update`, `short-announcement`.

## Frontmatter

Required on every article:

`title`, `source`, `content_type`, `freshness_risk`, `slug`, `url`, `canonical`, `fetched_at`, `status_code`, `html_hash`, `clean_word_count`, `clean_char_count`

`source` is the directory name (`ahrefs-blog`, `semrush-blog`, or `google-search-central-blog`).

`content_type` values in this snapshot: `blog_article`, `landing_page`, `product_blog`, `seo_guide`, `event`, `search_update`, `short_announcement`, `faq_short`, `product_or_tool`, `research_study`.

`freshness_risk` values: `low`, `medium`, `high`, `historical`, `unknown`.

Optional fields used throughout the corpus: `author`, `published`, `updated`, `categories`, `freshness_reasons`.

## Indexes

Regenerate after adding or editing articles:

```powershell
python -X utf8 scripts/preprocess_public_repo.py
```

Outputs:

- `metadata/index.csv`
- `metadata/index.jsonl`
- `metadata/source-summary.json`
- `reports/publication-audit.md`

The preprocessor does not modify article files. It rebuilds the indexes, source summary, duplicate-canonical report, and public-release notes.

Check the tree without rewriting those files:

```powershell
python -X utf8 scripts/validate_corpus.py
```

The publication audit currently lists 7 duplicate canonical URL groups. Validation reports them and still passes. Missing frontmatter, risky local paths or secrets, and an index that does not match the files fail the check.

## Scripts

Python 3.12. Fetching new pages needs the packages in `requirements.txt`. Discovery, preprocessing, and validation use the standard library.

```powershell
python -X utf8 scripts/check_new_articles.py
python -m pip install -r requirements.txt
python -X utf8 scripts/fetch_new_articles.py
python -X utf8 scripts/fetch_new_articles.py --apply
```

`check_new_articles.py` reads upstream sitemaps and the Search Central feed and prints URLs that are not in the local index. `fetch_new_articles.py` is a dry run until `--apply`. URLs to fetch are the lists at the top of that script. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Third-party text

The article files are copyrighted by Ahrefs, Semrush, and Google. This repository does not grant a license to republish them. Original scripts, tests, and project docs are MIT. Read [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md) before redistributing any part of the tree.

Prefer `metadata/` when the goal is discovery or citation. Each row includes the original URL.

## Citation

GitHub can cite this dataset from [CITATION.cff](CITATION.cff). Cite the repository version and the original article URL in the file you used.
