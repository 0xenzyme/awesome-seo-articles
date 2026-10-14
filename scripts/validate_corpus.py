"""Check corpus frontmatter and index coverage without rewriting files.

Duplicate canonical URLs are printed and do not fail the run. Missing required
fields, source mismatches, risky text, and index drift do.

Usage:
    python -X utf8 scripts/validate_corpus.py
"""

from __future__ import annotations

import csv
import io
import json
import sys
from pathlib import Path

from preprocess_public_repo import (
    duplicate_canonicals,
    load_articles,
    scan_risky_text,
)

ROOT = Path(__file__).resolve().parents[1]
JSONL_PATH = ROOT / "metadata" / "index.jsonl"
CSV_PATH = ROOT / "metadata" / "index.csv"
COMPARE_FIELDS = ("canonical", "html_hash", "content_type", "freshness_risk")


def _text(value: object) -> str:
    if value is None:
        return ""
    return str(value)


def load_jsonl() -> dict[str, dict]:
    rows: dict[str, dict] = {}
    with JSONL_PATH.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            path = row.get("path")
            if not path:
                raise ValueError(f"metadata/index.jsonl:{line_number} missing path")
            if path in rows:
                raise ValueError(f"metadata/index.jsonl duplicate path: {path}")
            rows[path] = row
    return rows


def load_csv_paths() -> set[str]:
    with CSV_PATH.open(encoding="utf-8", newline="") as handle:
        return {row["path"] for row in csv.DictReader(handle)}


def collect_problems() -> tuple[list[str], list[tuple[str, list[str]]]]:
    articles = load_articles()
    problems: list[str] = []
    if not articles:
        problems.append("no article files found")

    for article in articles:
        for warning in article.warnings:
            problems.append(f"{article.rel_path}: {warning}")
        for hit in scan_risky_text(article):
            problems.append(f"{article.rel_path}: risk_hit:{hit}")

    rows = [
        {"canonical": article.frontmatter.get("canonical"), "path": article.rel_path}
        for article in articles
    ]
    duplicates = duplicate_canonicals(rows)

    if not JSONL_PATH.exists():
        problems.append("missing metadata/index.jsonl")
        return problems, duplicates
    if not CSV_PATH.exists():
        problems.append("missing metadata/index.csv")
        return problems, duplicates

    indexed = load_jsonl()
    csv_paths = load_csv_paths()
    on_disk = {article.rel_path: article for article in articles}

    for path in sorted(set(on_disk) - set(indexed)):
        problems.append(f"index missing article: {path}")
    for path in sorted(set(indexed) - set(on_disk)):
        problems.append(f"index has unknown path: {path}")
    if csv_paths != set(indexed):
        problems.append("metadata/index.csv paths differ from metadata/index.jsonl")

    for path in sorted(set(on_disk) & set(indexed)):
        frontmatter = on_disk[path].frontmatter
        row = indexed[path]
        for field in COMPARE_FIELDS:
            disk_value = _text(frontmatter.get(field))
            index_value = _text(row.get(field))
            if disk_value != index_value:
                problems.append(
                    f"{path}: {field} differs (file {disk_value!r}, index {index_value!r})"
                )

    return problems, duplicates


def main() -> int:
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")

    problems, duplicates = collect_problems()
    print(f"duplicate canonical groups: {len(duplicates)} (reported, not failing)")
    for canonical, paths in duplicates:
        print(f"  {canonical}: {', '.join(paths)}")

    if problems:
        print(f"{len(problems)} problem(s):")
        for problem in problems[:100]:
            print(f"  {problem}")
        if len(problems) > 100:
            print(f"  ... and {len(problems) - 100} more")
        return 1

    print("corpus ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
