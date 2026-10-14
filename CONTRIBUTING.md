# Contributing

Issues and pull requests are welcome for corpus corrections, metadata bugs, and script fixes.

## What belongs here

Add a public article from one of the existing sources:

- Ahrefs Blog
- Semrush Blog
- Google Search Central Blog

Keep the cleaned Markdown and the frontmatter schema already used in the corpus. Record the source URL. Do not add private notes, credentials, or local filesystem paths.

## Add articles

From the repository root, with Python 3.12:

```powershell
python -X utf8 scripts/check_new_articles.py
python -m pip install -r requirements.txt
python -X utf8 scripts/fetch_new_articles.py
python -X utf8 scripts/fetch_new_articles.py --apply
python -X utf8 scripts/preprocess_public_repo.py
python -X utf8 scripts/validate_corpus.py
```

`check_new_articles.py` only prints what is new upstream. Copy URLs you intend to fetch into the `AHREFS_NEW`, `SEMRUSH_NEW`, or `GSC_NEW` list in `scripts/fetch_new_articles.py`. The fetch command is a dry run until you pass `--apply`. Use `--source` and `--limit` to narrow a run.

After fetching, regenerate the indexes. `validate_corpus.py` checks required frontmatter, risky path or secret patterns, and whether `metadata/index.jsonl` still matches the article files. It prints duplicate canonical URLs and does not fail on the known duplicates.

## Frontmatter

Required fields:

`title`, `source`, `content_type`, `freshness_risk`, `slug`, `url`, `canonical`, `fetched_at`, `status_code`, `html_hash`, `clean_word_count`, `clean_char_count`

`source` must match the top-level directory name.

Reuse these `content_type` values when they fit: `blog_article`, `landing_page`, `product_blog`, `seo_guide`, `event`, `search_update`, `short_announcement`, `faq_short`, `product_or_tool`, `research_study`.

Reuse these `freshness_risk` values: `low`, `medium`, `high`, `historical`, `unknown`.

## Layout

Put each file in the category directory that matches its topic. Do not add article files directly under `ahrefs-blog/`, `semrush-blog/`, or `google-search-central-blog/`. `google-search-central-blog/INDEX-BY-YEAR.md` is an index and is skipped by the preprocessor.

## Checks

```powershell
python -m compileall -q scripts tests
python -m unittest discover -s tests -v
python -X utf8 scripts/validate_corpus.py
```

The same checks run in GitHub Actions on push and pull request. That workflow does not install fetch dependencies and does not download articles.

## Licensing

Scripts, tests, and the project docs listed in `LICENSE` are MIT. Article Markdown is not relicensed by this repository. Read `NOTICE.md` before adding or requesting a new source.
