"""Probe upstream sitemaps / feeds to find articles published after our
latest local record — read-only, prints a report, does not modify the repo.

Sources:
- ahrefs-blog:        https://ahrefs.com/blog/sitemap_index.xml  (Yoast)
- semrush-blog:       https://www.semrush.com/blog/sitemap/     (single sitemap)
- google-search-central-blog: https://developers.google.com/search/blog/feed.xml (RSS)

For each source we compute:
- local_latest_published: latest published-date we already have on disk
- upstream_new: entries from upstream whose URL is NOT in our metadata

Usage:
    python -X utf8 scripts/check_new_articles.py
"""

from __future__ import annotations

import io
import json
import re
import sys
import urllib.request
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET

REPO_ROOT = Path(__file__).resolve().parent.parent
JSONL_PATH = REPO_ROOT / "metadata" / "index.jsonl"

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) awesome-seo-articles-check/1.0"


def http_get(url: str, timeout: int = 60, retries: int = 3) -> bytes:
    last_exc: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            if attempt < retries:
                print(f"    retry {attempt}/{retries - 1} for {url}: {exc}")
    raise last_exc if last_exc else RuntimeError("http_get failed")


def parse_xml(data: bytes) -> ET.Element:
    return ET.fromstring(data)


def strip_ns(tag: str) -> str:
    return tag.split("}", 1)[-1] if "}" in tag else tag


def urls_from_sitemap(sitemap_url: str) -> list[tuple[str, str]]:
    """Return (url, lastmod) tuples from a sitemap or sitemap index (recursively).

    A sitemap index nests <sitemap><loc>...</loc><lastmod>...</lastmod></sitemap>;
    a urlset holds <url><loc>...</loc><lastmod>...</lastmod></url>. We
    auto-detect and recurse.
    """
    print(f"  fetching {sitemap_url}")
    data = http_get(sitemap_url)
    root = parse_xml(data)
    root_tag = strip_ns(root.tag)
    if root_tag == "sitemapindex":
        results: list[tuple[str, str]] = []
        for sm in root:
            loc = None
            for child in sm:
                if strip_ns(child.tag) == "loc":
                    loc = (child.text or "").strip()
            if loc:
                try:
                    results.extend(urls_from_sitemap(loc))
                except Exception as exc:  # noqa: BLE001
                    print(f"    WARN fetching {loc}: {exc}")
        return results
    if root_tag == "urlset":
        out: list[tuple[str, str]] = []
        for url in root:
            loc = ""
            lastmod = ""
            for child in url:
                t = strip_ns(child.tag)
                if t == "loc":
                    loc = (child.text or "").strip()
                elif t == "lastmod":
                    lastmod = (child.text or "").strip()
            if loc:
                out.append((loc, lastmod))
        return out
    print(f"  WARN unexpected root <{root_tag}> at {sitemap_url}")
    return []


def urls_from_rss(feed_url: str) -> list[tuple[str, str]]:
    """Return (link, pubDate as YYYY-MM-DD) tuples from an RSS feed."""
    print(f"  fetching {feed_url}")
    data = http_get(feed_url)
    root = parse_xml(data)
    # rss/channel/item
    items = []
    for channel in root:
        if strip_ns(channel.tag) != "channel":
            continue
        for item in channel:
            if strip_ns(item.tag) != "item":
                continue
            link = ""
            pubdate = ""
            for child in item:
                t = strip_ns(child.tag)
                if t == "link":
                    link = (child.text or "").strip()
                elif t == "pubDate":
                    raw = (child.text or "").strip()
                    # Format: "Tue, 07 Jul 2026 00:00:00 +0000"
                    try:
                        pubdate = datetime.strptime(
                            raw, "%a, %d %b %Y %H:%M:%S %z"
                        ).strftime("%Y-%m-%d")
                    except ValueError:
                        pubdate = raw[:10]
            if link:
                items.append((link, pubdate))
    return items


def load_local() -> dict[str, dict]:
    """source_dir -> {'urls': set, 'latest_pub': str}."""
    out: dict[str, dict] = defaultdict(lambda: {"urls": set(), "latest_pub": ""})
    with JSONL_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            s = r.get("source_dir")
            if not s:
                continue
            for key in ("url", "canonical"):
                u = (r.get(key) or "").strip()
                if u:
                    # Normalize by stripping trailing slash.
                    out[s]["urls"].add(u.rstrip("/"))
            pub = (r.get("published") or "")[:10]
            if pub and pub > out[s]["latest_pub"]:
                out[s]["latest_pub"] = pub
    return out


def is_blog_article_url(source: str, url: str) -> bool:
    """Filter sitemap entries down to real blog posts."""
    if source == "ahrefs-blog":
        # Only /blog/<slug>/ — exclude author pages, category pages, /page/, /author/.
        if not url.startswith("https://ahrefs.com/blog/"):
            return False
        if "?" in url or "#" in url:
            return False
        tail = url[len("https://ahrefs.com/blog/") :].rstrip("/")
        if not tail or "/" in tail:
            return False
        if re.match(r"^(page|category|author|tag)", tail):
            return False
        return True
    if source == "semrush-blog":
        if not url.startswith("https://www.semrush.com/blog/"):
            return False
        tail = url[len("https://www.semrush.com/blog/") :].rstrip("/")
        if not tail or "/" in tail:
            return False
        return True
    if source == "google-search-central-blog":
        return url.startswith("https://developers.google.com/search/blog/")
    return False


def check_source(source: str, entries: list[tuple[str, str]], local: dict) -> None:
    filtered = [(u, m) for u, m in entries if is_blog_article_url(source, u)]
    known = local["urls"]
    new_entries: list[tuple[str, str]] = []
    updated_entries: list[tuple[str, str]] = []  # known URL but recent lastmod
    for url, lastmod in filtered:
        norm = url.rstrip("/")
        if norm not in known:
            new_entries.append((url, lastmod))
        else:
            # Existing article — flag if lastmod > local_latest_pub (rough proxy).
            if lastmod and lastmod[:10] > local["latest_pub"]:
                updated_entries.append((url, lastmod))

    print()
    print(f"### {source}")
    print(f"  local latest_published: {local['latest_pub'] or '(none)'}")
    print(f"  upstream entries (post-filter): {len(filtered)}")
    print(f"  local known URLs: {len(known)}")
    print(f"  NEW (not in local): {len(new_entries)}")
    print(f"  UPDATED (known URL, upstream lastmod > local latest): {len(updated_entries)}")

    if new_entries:
        # Sort by lastmod desc when available.
        new_entries.sort(key=lambda t: t[1] or "", reverse=True)
        print("  new sample (up to 30):")
        for url, lastmod in new_entries[:30]:
            print(f"    {lastmod[:10] or '----------':10s}  {url}")
        if len(new_entries) > 30:
            print(f"    ... and {len(new_entries) - 30} more")

    if updated_entries:
        updated_entries.sort(key=lambda t: t[1] or "", reverse=True)
        print("  updated sample (up to 10):")
        for url, lastmod in updated_entries[:10]:
            print(f"    {lastmod[:10] or '----------':10s}  {url}")
        if len(updated_entries) > 10:
            print(f"    ... and {len(updated_entries) - 10} more")


def main() -> int:
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")

    local = load_local()

    print("=== ahrefs-blog ===")
    ahrefs_entries = urls_from_sitemap("https://ahrefs.com/blog/sitemap_index.xml")
    check_source("ahrefs-blog", ahrefs_entries, local["ahrefs-blog"])

    print()
    print("=== semrush-blog ===")
    semrush_entries = urls_from_sitemap("https://www.semrush.com/blog/sitemap/")
    check_source("semrush-blog", semrush_entries, local["semrush-blog"])

    print()
    print("=== google-search-central-blog ===")
    gsc_entries = urls_from_rss("https://developers.google.com/search/blog/feed.xml")
    check_source(
        "google-search-central-blog", gsc_entries, local["google-search-central-blog"]
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
