"""Reorganize google-search-central-blog into subdirs by content_type
and emit a year-based index file for browsing by publish year.

- Buckets: content_type slug (short-announcement / blog-article /
  search-update / event / uncategorized).
- Also writes ``google-search-central-blog/INDEX-BY-YEAR.md``: grouped by
  publish year descending, each entry ``- YYYY-MM-DD [title](path)``.
- Uses ``git mv`` and rewrites ``metadata/index.jsonl`` + ``index.csv``
  ``path`` fields.

Usage:
    python -X utf8 scripts/reorganize_gsc.py           # dry-run
    python -X utf8 scripts/reorganize_gsc.py --apply
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JSONL_PATH = REPO_ROOT / "metadata" / "index.jsonl"
CSV_PATH = REPO_ROOT / "metadata" / "index.csv"
SOURCE_DIR = "google-search-central-blog"
UNCATEGORIZED = "uncategorized"


def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    return s or UNCATEGORIZED


def bucket_for(rec: dict) -> str:
    ct = (rec.get("content_type") or "").strip()
    return slugify(ct) if ct else UNCATEGORIZED


def load_records() -> list[dict]:
    with JSONL_PATH.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def build_plan(records: list[dict]) -> tuple[dict[str, str], Counter]:
    plan: dict[str, str] = {}
    counter: Counter = Counter()
    for rec in records:
        if rec.get("source_dir") != SOURCE_DIR:
            continue
        old = rec["path"]
        assert old.startswith(f"{SOURCE_DIR}/"), old
        filename = old[len(SOURCE_DIR) + 1 :]
        if "/" in filename:
            # Already nested — idempotent skip.
            continue
        bucket = bucket_for(rec)
        new = f"{SOURCE_DIR}/{bucket}/{filename}"
        plan[old] = new
        counter[bucket] += 1
    return plan, counter


def git_mv(old: str, new: str) -> None:
    (REPO_ROOT / new).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "mv", old, new], cwd=REPO_ROOT, check=True)


def rewrite_jsonl(plan: dict[str, str]) -> None:
    records = load_records()
    for rec in records:
        if rec.get("path") in plan:
            rec["path"] = plan[rec["path"]]
    tmp = JSONL_PATH.with_suffix(".jsonl.tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    tmp.replace(JSONL_PATH)


def rewrite_csv(plan: dict[str, str]) -> None:
    with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        return
    path_idx = rows[0].index("path")
    for row in rows[1:]:
        if row and row[path_idx] in plan:
            row[path_idx] = plan[row[path_idx]]
    tmp = CSV_PATH.with_suffix(".csv.tmp")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f, lineterminator="\n").writerows(rows)
    tmp.replace(CSV_PATH)


def write_year_index(records: list[dict]) -> Path:
    """Emit INDEX-BY-YEAR.md grouped by publish year, newest first."""
    by_year: dict[str, list[dict]] = defaultdict(list)
    for rec in records:
        if rec.get("source_dir") != SOURCE_DIR:
            continue
        pub = (rec.get("published") or "")[:10]  # YYYY-MM-DD
        year = pub[:4] or "unknown"
        by_year[year].append(
            {
                "date": pub or "unknown",
                "title": rec.get("title") or rec.get("heading") or rec.get("slug") or "",
                # Path is post-move (rewrite_jsonl updated it before we run this).
                "path": rec.get("path", ""),
            }
        )

    lines: list[str] = []
    lines.append("# Google Search Central Blog — Index by Year")
    lines.append("")
    total = sum(len(v) for v in by_year.values())
    lines.append(f"Total: {total} posts across {len(by_year)} years.")
    lines.append("")
    for year in sorted(by_year, reverse=True):
        entries = sorted(by_year[year], key=lambda r: r["date"], reverse=True)
        lines.append(f"## {year} ({len(entries)})")
        lines.append("")
        for e in entries:
            # Relative path from the index file (which lives inside SOURCE_DIR).
            rel = e["path"]
            if rel.startswith(f"{SOURCE_DIR}/"):
                rel = rel[len(SOURCE_DIR) + 1 :]
            # Escape ] and | in titles to avoid breaking Markdown.
            title = e["title"].replace("|", "\\|").replace("]", "\\]")
            lines.append(f"- {e['date']} — [{title}]({rel})")
        lines.append("")

    out = REPO_ROOT / SOURCE_DIR / "INDEX-BY-YEAR.md"
    out.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")

    records = load_records()
    plan, counter = build_plan(records)

    print(f"Source: {SOURCE_DIR}")
    print(f"Total files to move: {len(plan)}")
    print(f"Buckets: {len(counter)}")
    print()
    print(f"{'count':>6}  bucket")
    print(f"{'-----':>6}  ------")
    for bucket, n in counter.most_common():
        print(f"{n:>6}  {bucket}")
    print()

    # Sanity: files on disk vs plan.
    disk_files = {
        f"{SOURCE_DIR}/{p.name}"
        for p in (REPO_ROOT / SOURCE_DIR).iterdir()
        if p.is_file() and p.suffix == ".md"
    }
    orphans = disk_files - set(plan)
    if orphans:
        print(f"WARNING: {len(orphans)} .md file(s) on disk without a plan entry:")
        for o in sorted(orphans)[:5]:
            print(f"  - {o}")
        print()

    missing = [p for p in plan if not (REPO_ROOT / p).is_file()]
    if missing:
        print(f"WARNING: {len(missing)} metadata paths missing on disk.")
        print()

    # Collision guard.
    seen: dict[str, str] = {}
    for old, new in plan.items():
        if new in seen:
            print(f"ERROR collision: {new} <- {seen[new]} & {old}")
            return 2
        seen[new] = old

    if not args.apply:
        print("Dry-run only. Re-run with --apply to execute.")
        return 0

    missing_set = set(missing)
    exe = {k: v for k, v in plan.items() if k not in missing_set}
    print(f"Moving {len(exe)} files with git mv ...")
    for i, (old, new) in enumerate(exe.items(), 1):
        git_mv(old, new)
        if i % 200 == 0:
            print(f"  moved {i}/{len(exe)}")
    print("Move complete.")

    print("Rewriting metadata/index.jsonl ...")
    rewrite_jsonl(exe)
    print("Rewriting metadata/index.csv ...")
    rewrite_csv(exe)

    # Year index — read the freshly-updated metadata so paths are post-move.
    print("Writing INDEX-BY-YEAR.md ...")
    updated = load_records()
    idx = write_year_index(updated)
    print(f"Wrote {idx.relative_to(REPO_ROOT)}")
    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
