from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIRS = [
    "ahrefs-blog",
    "semrush-blog",
    "google-search-central-blog",
]
OUT_DIR = ROOT / "metadata"
REPORT_DIR = ROOT / "reports"

REQUIRED_FIELDS = [
    "title",
    "source",
    "content_type",
    "freshness_risk",
    "slug",
    "url",
    "canonical",
    "fetched_at",
    "status_code",
    "html_hash",
    "clean_word_count",
    "clean_char_count",
]

RISKY_PATTERNS = {
    "local_windows_path": re.compile(r"\b[A-Z]:\\(?:Users|obsidian|project|work|tmp)\\", re.IGNORECASE),
    "obsidian_path": re.compile(r"\bD:\\obsidian\\daily\\data\b", re.IGNORECASE),
    "raw_archive_artifact": re.compile(r"\b(raw\.html|metadata\.json|manifest\.jsonl|data/raw)\b", re.IGNORECASE),
    "possible_credential": re.compile(
        r"(?i)\b(api[_-]?key|access[_-]?token|secret|password|authorization)\b\s*[:=]\s*['\"]?[a-z0-9][a-z0-9._~+/=-]{16,}",
    ),
    "bearer_token": re.compile(
        r"(?i)\bbearer\s+[a-z0-9._~+/=-]{24,}",
    ),
    "private_key_block": re.compile(
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
        re.IGNORECASE,
    ),
}


@dataclass
class Article:
    path: Path
    rel_path: str
    source_dir: str
    frontmatter: dict[str, Any]
    body: str
    warnings: list[str]


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "null":
        return None
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1].replace('\\"', '"')
    if value.isdigit():
        return int(value)
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str, list[str]]:
    warnings: list[str] = []
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return {}, text, ["missing_frontmatter"]

    normalized = text.replace("\r\n", "\n")
    parts = normalized.split("---\n", 2)
    if len(parts) < 3:
        return {}, text, ["unterminated_frontmatter"]

    raw_fm = parts[1]
    body = parts[2].lstrip("\n")
    data: dict[str, Any] = {}
    current_key: str | None = None

    for raw_line in raw_fm.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, []).append(parse_scalar(line[4:]))
            continue
        if ":" not in line:
            warnings.append(f"unparsed_frontmatter_line:{line[:40]}")
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        current_key = key
        if raw_value == "":
            data[key] = []
        else:
            data[key] = parse_scalar(raw_value)

    return data, body, warnings


def load_articles() -> list[Article]:
    articles: list[Article] = []
    for source_dir in SOURCE_DIRS:
        folder = ROOT / source_dir
        for path in sorted(folder.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            fm, body, warnings = parse_frontmatter(text)
            for field in REQUIRED_FIELDS:
                if field not in fm:
                    warnings.append(f"missing_field:{field}")
            if fm.get("source") and fm.get("source") != source_dir:
                warnings.append("source_mismatch")
            rel_path = path.relative_to(ROOT).as_posix()
            articles.append(
                Article(
                    path=path,
                    rel_path=rel_path,
                    source_dir=source_dir,
                    frontmatter=fm,
                    body=body,
                    warnings=warnings,
                )
            )
    return articles


def first_heading(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def count_images(body: str) -> int:
    return len(re.findall(r"!\[[^\]]*\]\([^)]+\)", body))


def count_links(body: str) -> int:
    return len(re.findall(r"(?<!!)\[[^\]]+\]\([^)]+\)", body))


def scan_risky_text(article: Article) -> list[str]:
    haystack = "\n".join(
        [
            json.dumps(article.frontmatter, ensure_ascii=False, sort_keys=True),
            article.body,
        ]
    )
    hits = []
    for name, pattern in RISKY_PATTERNS.items():
        if pattern.search(haystack):
            hits.append(name)
    return hits


def article_row(article: Article) -> dict[str, Any]:
    fm = article.frontmatter
    body_words = len(re.findall(r"\b[\w'-]+\b", article.body))
    risk_hits = scan_risky_text(article)
    warnings = [*article.warnings, *[f"risk_hit:{hit}" for hit in risk_hits]]
    return {
        "path": article.rel_path,
        "source_dir": article.source_dir,
        "source": fm.get("source"),
        "title": fm.get("title"),
        "heading": first_heading(article.body),
        "slug": fm.get("slug"),
        "url": fm.get("url"),
        "canonical": fm.get("canonical"),
        "author": fm.get("author"),
        "published": fm.get("published"),
        "updated": fm.get("updated"),
        "fetched_at": fm.get("fetched_at"),
        "content_type": fm.get("content_type"),
        "freshness_risk": fm.get("freshness_risk"),
        "categories": "|".join(fm.get("categories") or []),
        "freshness_reasons": "|".join(fm.get("freshness_reasons") or []),
        "status_code": fm.get("status_code"),
        "html_hash": fm.get("html_hash"),
        "frontmatter_word_count": fm.get("clean_word_count"),
        "frontmatter_char_count": fm.get("clean_char_count"),
        "body_word_count_estimate": body_words,
        "image_count": count_images(article.body),
        "link_count": count_links(article.body),
        "warning_count": len(warnings),
        "warnings": "|".join(warnings),
    }


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def source_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_articles": len(rows),
        "sources": {},
    }
    by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_source[row["source_dir"]].append(row)

    for source, source_rows in sorted(by_source.items()):
        warning_rows = [r for r in source_rows if r["warning_count"]]
        word_counts = [
            int(r["frontmatter_word_count"])
            for r in source_rows
            if isinstance(r["frontmatter_word_count"], int)
        ]
        summary["sources"][source] = {
            "articles": len(source_rows),
            "warnings": len(warning_rows),
            "content_types": dict(Counter(r["content_type"] for r in source_rows)),
            "freshness_risks": dict(Counter(r["freshness_risk"] for r in source_rows)),
            "min_words": min(word_counts) if word_counts else None,
            "max_words": max(word_counts) if word_counts else None,
            "total_words": sum(word_counts),
        }
    return summary


def duplicate_canonicals(rows: list[dict[str, Any]]) -> list[tuple[str, list[str]]]:
    grouped: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        canonical = row.get("canonical")
        if canonical:
            grouped[str(canonical)].append(str(row["path"]))
    return sorted(
        [(canonical, paths) for canonical, paths in grouped.items() if len(paths) > 1],
        key=lambda item: (-len(item[1]), item[0]),
    )


def write_report(path: Path, rows: list[dict[str, Any]], summary: dict[str, Any]) -> None:
    warnings = [row for row in rows if row["warning_count"]]
    duplicate_groups = duplicate_canonicals(rows)
    risky_by_name = Counter()
    for row in rows:
        for warning in str(row["warnings"]).split("|"):
            if warning.startswith("risk_hit:"):
                risky_by_name[warning.removeprefix("risk_hit:")] += 1

    lines = [
        "# Publication Audit",
        "",
        f"Generated: {summary['generated_at']}",
        f"Total Markdown articles: {summary['total_articles']}",
        "",
        "## Source Inventory",
        "",
        "| Source | Articles | Warning rows | Total words | Content types | Freshness risks |",
        "| --- | ---: | ---: | ---: | --- | --- |",
    ]
    for source, item in summary["sources"].items():
        lines.append(
            "| {source} | {articles} | {warnings} | {total_words} | {content_types} | {freshness_risks} |".format(
                source=source,
                articles=item["articles"],
                warnings=item["warnings"],
                total_words=item["total_words"],
                content_types=", ".join(f"{k}: {v}" for k, v in sorted(item["content_types"].items())),
                freshness_risks=", ".join(f"{k}: {v}" for k, v in sorted(item["freshness_risks"].items())),
            )
        )

    lines.extend(
        [
            "",
            "## Public Release Notes",
            "",
            "- This repository currently contains full article text from third-party sources.",
            "- Ahrefs and Semrush content should be treated as copyrighted third-party material unless explicit redistribution permission is confirmed.",
            "- Google Search Central content may have separate licensing and attribution requirements; verify source terms before public release.",
            "- The generated metadata files are safer to publish than the full article corpus if the goal is discovery, indexing, or research references.",
            "",
            "## Risk Scan",
            "",
            f"- Rows with any warnings: {len(warnings)}",
            f"- Duplicate canonical URL groups: {len(duplicate_groups)}",
        ]
    )
    if risky_by_name:
        lines.append("- Risk pattern hits: " + ", ".join(f"{k}: {v}" for k, v in sorted(risky_by_name.items())))
    else:
        lines.append("- Risk pattern hits: 0")

    lines.extend(["", "## Duplicate Canonicals", ""])
    if duplicate_groups:
        for canonical, paths in duplicate_groups[:50]:
            lines.append(f"- {canonical} ({len(paths)} files): " + ", ".join(paths[:5]))
    else:
        lines.append("- None detected.")

    lines.extend(["", "## Warning Samples", ""])
    if warnings:
        for row in warnings[:100]:
            lines.append(f"- `{row['path']}`: {row['warnings']}")
    else:
        lines.append("- None.")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    articles = load_articles()
    rows = [article_row(article) for article in articles]

    OUT_DIR.mkdir(exist_ok=True)
    REPORT_DIR.mkdir(exist_ok=True)

    write_csv(OUT_DIR / "index.csv", rows)
    write_jsonl(OUT_DIR / "index.jsonl", rows)
    summary = source_summary(rows)
    (OUT_DIR / "source-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_report(REPORT_DIR / "publication-audit.md", rows, summary)

    print(f"Processed {len(rows)} markdown articles")
    print(f"Wrote {OUT_DIR / 'index.csv'}")
    print(f"Wrote {REPORT_DIR / 'publication-audit.md'}")


if __name__ == "__main__":
    main()
