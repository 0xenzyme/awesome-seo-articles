"""Fetch new articles from ahrefs/semrush/google-search-central blogs, convert
to markdown with YAML frontmatter matching the existing corpus schema, drop
them into the correct category subdirectory, and append records to
metadata/index.jsonl + index.csv.

Read-only until --apply.

Usage:
    python -X utf8 scripts/fetch_new_articles.py                 # dry-run: show plan
    python -X utf8 scripts/fetch_new_articles.py --apply         # actually fetch
    python -X utf8 scripts/fetch_new_articles.py --apply --limit 3
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html as html_module
import io
import json
import re
import sys
import time
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_md
from readability import Document

REPO_ROOT = Path(__file__).resolve().parent.parent
JSONL_PATH = REPO_ROOT / "metadata" / "index.jsonl"
CSV_PATH = REPO_ROOT / "metadata" / "index.csv"
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)


# ---------------------------------------------------------------------------
# URL lists to fetch. Sourced from the check_new_articles.py probe on 2026-07-13.
# NEW = article not present in local corpus; kept published date for reference.
# ---------------------------------------------------------------------------

AHREFS_NEW = [
    "https://ahrefs.com/blog/taught-agent-to-refresh-data-content/",
    "https://ahrefs.com/blog/agent-a-for-seo/",
    "https://ahrefs.com/blog/retrieval-augmented-generation/",
    "https://ahrefs.com/blog/self-promotional-content-ai-seo-experiment/",
    "https://ahrefs.com/blog/ai-marketing-assistant/",
    "https://ahrefs.com/blog/marketing-trends/",
    "https://ahrefs.com/blog/new-features-may-2026/",
    "https://ahrefs.com/blog/what-is-an-ai-agent/",
    "https://ahrefs.com/blog/reddit-seo/",
    "https://ahrefs.com/blog/llmstxt-study/",
    "https://ahrefs.com/blog/average-organic-traffic-benchmarks/",
    "https://ahrefs.com/blog/what-is-a-good-ctr/",
    "https://ahrefs.com/blog/seo-content/",
    "https://ahrefs.com/blog/agentic-marketing/",
    # Historical backfill (4 older posts we somehow missed).
    "https://ahrefs.com/blog/how-do-search-engines-work/",
    "https://ahrefs.com/blog/what-is-soft-404/",
    "https://ahrefs.com/blog/bulk-pagespeed-insights-website-speed-test/",
    "https://ahrefs.com/blog/enterprise-seo-roi-calculator/",
]

SEMRUSH_NEW = [
    "https://www.semrush.com/blog/google-search-console-adds-social-and-video-reports/",
    "https://www.semrush.com/blog/how-ai-shapes-b2b-buying/",
    "https://www.semrush.com/blog/google-research-and-ai-spam-detection/",
    "https://www.semrush.com/blog/ai-overviews-commercial-search-study/",
    "https://www.semrush.com/blog/how-cardmarket-wins-search/",
    "https://www.semrush.com/blog/google-completes-spam-update-rollout/",
    "https://www.semrush.com/blog/ecommerce-ai-seo/",
    "https://www.semrush.com/blog/chatgpt-reasoning-ai-visibility/",
    "https://www.semrush.com/blog/how-i-rebuilt-our-content-update-pipeline/",
    "https://www.semrush.com/blog/google-launches-open-knowledge-format-for-ai-agents/",
    "https://www.semrush.com/blog/semrush-vs-semrush-for-enterprise/",
    "https://www.semrush.com/blog/category-entry-points-ai-search/",
    "https://www.semrush.com/blog/how-to-optimize-for-the-agentic-web/",
    "https://www.semrush.com/blog/ai-sentiment-analysis-marketers-guide/",
    "https://www.semrush.com/blog/ai-agent-bot-traffic/",
]

GSC_NEW = [
    "https://developers.google.com/search/blog/2026/07/search-console-social-video-platforms",
    "https://developers.google.com/search/blog/2026/07/search-central-live-deep-dive-europe-2026",
    "https://developers.google.com/search/blog/2026/06/scl-deep-dive-europe-2026",
]

# Category-alias table used by reorganize scripts (semrush-blog only).
SEMRUSH_BUCKET_ALIASES = {
    "news-research": "industry-news",
    "semrush-one": "semrush-product",
    "semrush-enterprise": "semrush-product",
}


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (name or "").strip().lower()).strip("-")
    return s or "uncategorized"


def source_from_url(url: str) -> str:
    if url.startswith("https://ahrefs.com/"):
        return "ahrefs-blog"
    if url.startswith("https://www.semrush.com/"):
        return "semrush-blog"
    if url.startswith("https://developers.google.com/"):
        return "google-search-central-blog"
    raise ValueError(f"unknown source for {url}")


def slug_from_url(url: str) -> str:
    src = source_from_url(url)
    if src == "google-search-central-blog":
        # https://developers.google.com/search/blog/2026/07/search-console-social-video-platforms
        m = re.match(r".*/search/blog/(\d{4})/(\d{2})/([^/?#]+)", url)
        if not m:
            raise ValueError(f"cannot parse gsc slug from {url}")
        year, month, name = m.groups()
        return f"{year}-{month}-{name}"
    # ahrefs / semrush: last path segment.
    m = re.match(r".*/blog/([^/?#]+)/?", url)
    if not m:
        raise ValueError(f"cannot parse slug from {url}")
    return m.group(1)


def http_get(url: str, timeout: int = 60, retries: int = 3) -> tuple[int, bytes]:
    last_exc: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.status, resp.read()
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            time.sleep(1.5 * attempt)
    raise last_exc if last_exc else RuntimeError("http_get failed")


def html_hash(html_bytes: bytes) -> str:
    return hashlib.sha256(html_bytes).hexdigest()


def parse_json_ld(soup: BeautifulSoup) -> list[dict]:
    out: list[dict] = []
    for tag in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(tag.string or tag.get_text() or "")
        except Exception:  # noqa: BLE001
            continue
        if isinstance(data, list):
            out.extend(x for x in data if isinstance(x, dict))
        elif isinstance(data, dict):
            if "@graph" in data and isinstance(data["@graph"], list):
                out.extend(x for x in data["@graph"] if isinstance(x, dict))
            else:
                out.append(data)
    return out


def find_article_node(json_ld: list[dict]) -> dict | None:
    for node in json_ld:
        t = node.get("@type", "")
        types = [t] if isinstance(t, str) else list(t)
        if any(x in {"BlogPosting", "Article", "NewsArticle"} for x in types):
            return node
    return None


def meta(soup: BeautifulSoup, prop: str, attr: str = "property") -> str:
    tag = soup.find("meta", attrs={attr: prop})
    if tag and tag.get("content"):
        return tag["content"].strip()
    return ""


def parse_iso(dt: str) -> str:
    """Normalize a datetime string to ISO with +00:00. Return '' if unparseable."""
    if not dt:
        return ""
    dt = dt.strip()
    # Common shapes: 2026-07-09T12:34:56+00:00, 2026-07-09, 2026-07-09T12:34:56Z
    try:
        d = datetime.fromisoformat(dt.replace("Z", "+00:00"))
    except ValueError:
        # Try YYYY-MM-DD only.
        try:
            d = datetime.strptime(dt[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except ValueError:
            return ""
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(timezone.utc).isoformat().replace("+00:00", "+00:00")


# ---------------------------------------------------------------------------
# Extraction per source
# ---------------------------------------------------------------------------


@dataclass
class Extracted:
    title: str
    author: str
    published: str  # ISO
    updated: str  # ISO
    categories: list[str]
    canonical: str
    body_html: str


def extract_ahrefs(soup: BeautifulSoup, url: str) -> Extracted:
    ld = parse_json_ld(soup)
    article = find_article_node(ld) or {}

    title = clean_title(
        article.get("headline") or meta(soup, "og:title") or (soup.title.string.strip() if soup.title else "")
    )
    author = ""
    a = article.get("author")
    if isinstance(a, dict):
        author = a.get("name", "")
    elif isinstance(a, list) and a:
        author = a[0].get("name", "") if isinstance(a[0], dict) else str(a[0])
    if not author:
        author = meta(soup, "author", attr="name")

    published = parse_iso(article.get("datePublished") or meta(soup, "article:published_time"))
    updated = parse_iso(article.get("dateModified") or meta(soup, "article:modified_time") or published)

    # Categories: Ahrefs adds article:section meta and rel=tag anchors.
    cats: list[str] = []
    for tag in soup.find_all("meta", attrs={"property": "article:section"}):
        if tag.get("content"):
            cats.append(html_module.unescape(tag["content"]).strip())
    if not cats:
        section = article.get("articleSection")
        if isinstance(section, str):
            cats = [html_module.unescape(section)]
        elif isinstance(section, list):
            cats = [html_module.unescape(s) for s in section if isinstance(s, str)]

    canonical = ""
    link = soup.find("link", rel="canonical")
    if link and link.get("href"):
        canonical = link["href"].strip()
    canonical = canonical or meta(soup, "og:url") or url

    # Body: prefer the main content div; fall back to readability.
    body_html = _body_html_readability(soup, url)

    return Extracted(
        title=title,
        author=author,
        published=published,
        updated=updated,
        categories=cats or ["Uncategorized"],
        canonical=canonical,
        body_html=body_html,
    )


def extract_semrush(soup: BeautifulSoup, url: str) -> Extracted:
    ld = parse_json_ld(soup)
    article = find_article_node(ld) or {}

    title = clean_title(
        article.get("headline") or meta(soup, "og:title") or (soup.title.string.strip() if soup.title else "")
    )
    author = ""
    a = article.get("author")
    if isinstance(a, dict):
        author = a.get("name", "")
    elif isinstance(a, list) and a:
        author = a[0].get("name", "") if isinstance(a[0], dict) else str(a[0])

    published = parse_iso(article.get("datePublished") or meta(soup, "article:published_time"))
    updated = parse_iso(article.get("dateModified") or meta(soup, "article:modified_time") or published)

    # Semrush ships its blog on Next.js. Category lives in __NEXT_DATA__ at
    # props.pageProps.page.category.name — JSON-LD doesn't carry it.
    cats: list[str] = []
    next_data = soup.find("script", id="__NEXT_DATA__")
    if next_data and next_data.string:
        try:
            data = json.loads(next_data.string)
            page = data.get("props", {}).get("pageProps", {}).get("page", {}) or {}
            cat = page.get("category") or {}
            name = cat.get("name")
            if name:
                cats.append(name)
            parent = cat.get("parent") or {}
            pname = parent.get("name")
            if pname and pname != name:
                cats.append(pname)
        except Exception:  # noqa: BLE001
            pass
    if not cats:
        section = article.get("articleSection")
        if isinstance(section, str):
            cats = [section]
        elif isinstance(section, list):
            cats = [s for s in section if isinstance(s, str)]

    canonical = ""
    link = soup.find("link", rel="canonical")
    if link and link.get("href"):
        canonical = link["href"].strip()
    canonical = canonical or meta(soup, "og:url") or url

    body_html = _body_html_readability(soup, url)

    return Extracted(
        title=title,
        author=author,
        published=published,
        updated=updated,
        categories=cats or ["Uncategorized"],
        canonical=canonical,
        body_html=body_html,
    )


def extract_gsc(soup: BeautifulSoup, url: str) -> Extracted:
    ld = parse_json_ld(soup)
    article = find_article_node(ld) or {}

    # Prefer og:title (clean), fall back to <title> which carries site suffixes.
    raw_title = meta(soup, "og:title") or article.get("headline") or (
        soup.title.string.strip() if soup.title else ""
    )
    title = clean_title(raw_title)
    # Strip trailing "| Google Search Central Blog | Google for Developers".
    for suffix in (
        " | Google Search Central Blog | Google for Developers",
        " | Google Search Central Blog",
        " | Google for Developers",
    ):
        if title.endswith(suffix):
            title = title[: -len(suffix)].rstrip()

    canonical = ""
    link = soup.find("link", rel="canonical")
    if link and link.get("href"):
        canonical = link["href"].strip()
    canonical = canonical or meta(soup, "og:url") or url

    body_html = _body_html_readability(soup, url)
    body_text = BeautifulSoup(body_html, "html.parser").get_text("\n", strip=True)

    # Published: JSON-LD first; otherwise scrape the leading date line.
    published = parse_iso(article.get("datePublished") or meta(soup, "article:published_time"))
    if not published:
        # Body typically starts with "Tuesday, July 7, 2026".
        m = re.search(
            r"\b(Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)day,\s+([A-Za-z]+)\s+(\d{1,2}),\s+(\d{4})\b",
            body_text,
        )
        if m:
            try:
                dt = datetime.strptime(f"{m.group(2)} {m.group(3)} {m.group(4)}", "%B %d %Y")
                published = dt.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "+00:00")
            except ValueError:
                published = ""
    updated = parse_iso(article.get("dateModified") or meta(soup, "article:modified_time") or published) or published

    # Author: JSON-LD first, then "Posted by <Name>" trailer.
    author = ""
    a = article.get("author")
    if isinstance(a, dict):
        author = a.get("name", "")
    elif isinstance(a, list) and a:
        author = a[0].get("name", "") if isinstance(a[0], dict) else ""
    if not author:
        # body_text is plaintext (readability output → get_text). Trailer
        # commonly looks like: "Posted by\nMoshe Samet\n, Product Manager …".
        m = re.search(r"Posted by\s+([^,]+?)(?:,|$)", body_text, re.S)
        if m:
            author = re.sub(r"\s+", " ", m.group(1)).strip()

    return Extracted(
        title=title,
        author=author,
        published=published,
        updated=updated,
        categories=["Google Search Central Blog"],
        canonical=canonical,
        body_html=body_html,
    )


def _body_html_readability(soup: BeautifulSoup, url: str) -> str:
    """Fallback body extractor using readability-lxml against the full HTML.

    WordPress lazy-loading strategy on Ahrefs (and many others) is:
      <img class="lazyload" src="data:image/svg..." data-src="REAL_URL">
      <noscript><img src="REAL_URL"></noscript>
    Naively unwrapping <noscript> or resolving data-src leaves us with TWO
    <img> siblings pointing at the same URL — hence duplicate output. So:
      1. For every <noscript> that contains <img>, drop the previous sibling
         image whose real URL matches. Then unwrap the <noscript>.
      2. Any leftover lazyload/data-svg <img>s (no matching noscript sibling)
         get their src rewritten to data-src.
    """
    working = BeautifulSoup(str(soup), "html.parser")

    def real_src(img) -> str:
        return (img.get("data-src") or img.get("src") or "").strip()

    for ns in working.find_all("noscript"):
        # Only handle <noscript> wrapping a single <img>.
        ns_imgs = ns.find_all("img")
        if not ns_imgs:
            ns.unwrap()
            continue
        target_srcs = {img.get("src", "").strip() for img in ns_imgs if img.get("src")}
        # Look at neighbouring imgs (before and after) with matching src.
        prev = ns.find_previous_sibling()
        while prev is not None and getattr(prev, "name", None) in ("br", None):
            prev = prev.find_previous_sibling()
        if prev is not None and getattr(prev, "name", None) == "img" and real_src(prev) in target_srcs:
            prev.decompose()
        nxt = ns.find_next_sibling()
        while nxt is not None and getattr(nxt, "name", None) in ("br", None):
            nxt = nxt.find_next_sibling()
        if nxt is not None and getattr(nxt, "name", None) == "img" and real_src(nxt) in target_srcs:
            nxt.decompose()
        ns.unwrap()

    # Rewrite any remaining lazyload placeholders.
    for img in working.find_all("img"):
        src = img.get("src", "")
        if src.startswith("data:image/svg") or "lazyload" in (img.get("class") or []):
            data_src = img.get("data-src")
            if data_src:
                img["src"] = data_src
            else:
                img.decompose()

    html = str(working)
    try:
        doc = Document(html)
        return doc.summary(html_partial=True)
    except Exception:  # noqa: BLE001
        body = working.find("body")
        return str(body) if body else ""


def clean_title(raw: str) -> str:
    """Decode HTML entities and normalize whitespace."""
    if not raw:
        return raw
    s = html_module.unescape(raw)
    s = s.replace("\xa0", " ")  # NBSP → space
    return re.sub(r"\s+", " ", s).strip()


EXTRACTORS = {
    "ahrefs-blog": extract_ahrefs,
    "semrush-blog": extract_semrush,
    "google-search-central-blog": extract_gsc,
}


# ---------------------------------------------------------------------------
# Category / bucket resolution
# ---------------------------------------------------------------------------


def bucket_for(source: str, categories: list[str], content_type: str) -> str:
    if source == "google-search-central-blog":
        return slugify(content_type)  # blog-article / short-announcement / ...
    first = (categories[0] if categories else "").strip()
    slug = slugify(first) or "uncategorized"
    if source == "semrush-blog":
        slug = SEMRUSH_BUCKET_ALIASES.get(slug, slug)
    return slug


def gsc_content_type(soup: BeautifulSoup, body_word_count: int) -> str:
    """Heuristic mirror of what the original preprocess pipeline seems to use:
    - short announcements are short (< ~250 words) and often list-like.
    - full posts are blog_article.
    We keep it simple: <= 250 words -> short_announcement, else blog_article.
    """
    if body_word_count <= 250:
        return "short_announcement"
    return "blog_article"


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------


def yaml_escape(s: str) -> str:
    # Double-quoted YAML: escape backslash and double-quote.
    return s.replace("\\", "\\\\").replace('"', '\\"')


def build_frontmatter(rec: dict) -> str:
    lines: list[str] = ["---"]
    scalar_order = [
        "title",
        "source",
        "content_type",
        "freshness_risk",
        "slug",
        "url",
        "canonical",
        "author",
        "published",
        "updated",
    ]
    for k in scalar_order:
        v = rec.get(k, "")
        if v == "":
            lines.append(f'{k}: ""')
        else:
            lines.append(f'{k}: "{yaml_escape(str(v))}"')
    # categories list
    cats = rec.get("categories") or []
    if cats:
        lines.append("categories:")
        for c in cats:
            lines.append(f'  - "{yaml_escape(c)}"')
    else:
        lines.append("categories: []")
    fr = rec.get("freshness_reasons") or []
    if fr:
        lines.append("freshness_reasons:")
        for r in fr:
            lines.append(f'  - "{yaml_escape(r)}"')
    else:
        lines.append("freshness_reasons: []")
    for k in ("fetched_at", "status_code", "html_hash", "clean_word_count", "clean_char_count"):
        v = rec.get(k, "")
        if isinstance(v, int):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f'{k}: "{yaml_escape(str(v))}"')
    lines.append("---")
    return "\n".join(lines) + "\n"


def clean_markdown(md_body: str) -> str:
    # Collapse >2 blank lines.
    md_body = re.sub(r"\n{3,}", "\n\n", md_body)
    return md_body.strip() + "\n"


# ---------------------------------------------------------------------------
# Main workflow
# ---------------------------------------------------------------------------


def load_existing_paths() -> set[str]:
    if not JSONL_PATH.exists():
        return set()
    out: set[str] = set()
    with JSONL_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            u = (r.get("url") or "").rstrip("/")
            if u:
                out.add(u)
            c = (r.get("canonical") or "").rstrip("/")
            if c:
                out.add(c)
    return out


def load_freshness_risk(source: str, published: str) -> str:
    if not published:
        return "unknown"
    try:
        year = int(published[:4])
    except ValueError:
        return "unknown"
    if year >= 2025:
        return "low"
    if year >= 2023:
        return "medium"
    return "historical"


def word_count(text: str) -> int:
    return len(re.findall(r"\w+", text))


def process_one(url: str, existing: set[str]) -> tuple[dict, str, Path] | None:
    if url.rstrip("/") in existing:
        print(f"  SKIP already in corpus: {url}")
        return None

    source = source_from_url(url)
    print(f"  fetch {source} {url}")
    status, body = http_get(url)
    hhash = html_hash(body)
    soup = BeautifulSoup(body, "html.parser")

    extract = EXTRACTORS[source]
    ex = extract(soup, url)

    md_body = clean_markdown(html_to_md(ex.body_html, heading_style="ATX", bullets="-"))
    clean_word_count = word_count(md_body)
    clean_char_count = len(md_body)

    slug = slug_from_url(url)

    if source == "google-search-central-blog":
        content_type = gsc_content_type(soup, clean_word_count)
    else:
        content_type = "blog_article"

    bucket = bucket_for(source, ex.categories, content_type)

    fetched_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "+00:00")

    frontmatter_rec = {
        "title": ex.title,
        "source": source,
        "content_type": content_type,
        "freshness_risk": load_freshness_risk(source, ex.published),
        "slug": slug,
        "url": url,
        "canonical": ex.canonical or url,
        "author": ex.author,
        "published": ex.published,
        "updated": ex.updated or ex.published,
        "categories": ex.categories,
        "freshness_reasons": [],
        "fetched_at": fetched_at,
        "status_code": status,
        "html_hash": hhash,
        "clean_word_count": clean_word_count,
        "clean_char_count": clean_char_count,
    }

    fm = build_frontmatter(frontmatter_rec)
    body_out = f"# {ex.title}\n\n{md_body}"
    file_content = fm + body_out

    rel_path = f"{source}/{bucket}/{slug}.md"
    dest = REPO_ROOT / rel_path

    # Metadata-record (superset of frontmatter, matches existing index.jsonl shape).
    meta_rec = {
        "author": ex.author,
        "body_word_count_estimate": clean_word_count,
        "canonical": ex.canonical or url,
        "categories": "|".join(ex.categories),
        "content_type": content_type,
        "fetched_at": fetched_at,
        "freshness_reasons": "",
        "freshness_risk": load_freshness_risk(source, ex.published),
        "frontmatter_char_count": len(fm),
        "frontmatter_word_count": word_count(fm),
        "heading": ex.title,
        "html_hash": hhash,
        "image_count": len(re.findall(r"!\[", md_body)),
        "link_count": len(re.findall(r"\]\(http", md_body)),
        "path": rel_path,
        "published": ex.published,
        "slug": slug,
        "source": source,
        "source_dir": source,
        "status_code": status,
        "title": ex.title,
        "updated": ex.updated or ex.published,
        "url": url,
        "warning_count": 0,
        "warnings": "",
    }

    return meta_rec, file_content, dest


def append_metadata(new_recs: list[dict]) -> None:
    if not new_recs:
        return
    with JSONL_PATH.open("a", encoding="utf-8", newline="\n") as f:
        for r in new_recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # CSV — append the same records, aligned on the existing header order.
    with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        header = next(csv.reader(f))
    with CSV_PATH.open("a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        for r in new_recs:
            writer.writerow([r.get(col, "") for col in header])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--limit", type=int, default=None, help="max articles to fetch (debug)")
    parser.add_argument(
        "--source",
        choices=("all", "ahrefs-blog", "semrush-blog", "google-search-central-blog"),
        default="all",
    )
    args = parser.parse_args()

    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")

    urls: list[str] = []
    if args.source in ("all", "ahrefs-blog"):
        urls.extend(AHREFS_NEW)
    if args.source in ("all", "semrush-blog"):
        urls.extend(SEMRUSH_NEW)
    if args.source in ("all", "google-search-central-blog"):
        urls.extend(GSC_NEW)

    if args.limit:
        urls = urls[: args.limit]

    print(f"Planned fetches: {len(urls)}")
    for u in urls:
        print(f"  - {u}")

    if not args.apply:
        print("\nDry-run. Re-run with --apply.")
        return 0

    existing = load_existing_paths()

    new_meta: list[dict] = []
    failures: list[tuple[str, str]] = []
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] {url}")
        try:
            result = process_one(url, existing)
        except Exception as exc:  # noqa: BLE001
            print(f"  FAILED: {exc}")
            failures.append((url, str(exc)))
            continue
        if not result:
            continue
        meta_rec, file_content, dest = result
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            print(f"  file already exists at {dest.relative_to(REPO_ROOT)}, skipping write")
            continue
        dest.write_text(file_content, encoding="utf-8", newline="\n")
        print(f"  wrote {dest.relative_to(REPO_ROOT)} ({meta_rec['body_word_count_estimate']} words)")
        new_meta.append(meta_rec)
        # Polite delay.
        time.sleep(0.7)

    if new_meta:
        print(f"\nAppending {len(new_meta)} records to metadata ...")
        append_metadata(new_meta)

    print(f"\nDone. Wrote {len(new_meta)} articles, {len(failures)} failures.")
    for u, err in failures:
        print(f"  FAIL {u}: {err}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
