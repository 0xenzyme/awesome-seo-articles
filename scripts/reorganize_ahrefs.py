"""Reorganize a blog corpus into subdirectories by primary category.

Behavior:
- Reads metadata/index.jsonl to determine each file's primary category
  (first token of ``categories`` split by ``|``). Empty / ``[|]`` categories
  fall into ``uncategorized``.
- In dry-run mode (default): prints the planned bucket distribution and
  any warnings (missing files, filename collisions).
- With --apply: moves files via ``git mv`` (so history is preserved) and
  rewrites the ``path`` field in both ``index.jsonl`` and ``index.csv``.

Usage:
    python -X utf8 scripts/reorganize_ahrefs.py --source ahrefs-blog          # dry-run
    python -X utf8 scripts/reorganize_ahrefs.py --source ahrefs-blog --apply
    python -X utf8 scripts/reorganize_ahrefs.py --source semrush-blog --apply
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JSONL_PATH = REPO_ROOT / "metadata" / "index.jsonl"
CSV_PATH = REPO_ROOT / "metadata" / "index.csv"
UNCATEGORIZED = "uncategorized"

# Per-source bucket aliases: map raw slug -> unified slug. Used to fold
# semantically equivalent (or product-family) buckets into one directory.
BUCKET_ALIASES: dict[str, dict[str, str]] = {
    "semrush-blog": {
        "news-research": "industry-news",     # 1 stray record folded in
        "semrush-one": "semrush-product",     # product-line umbrella
        "semrush-enterprise": "semrush-product",
    },
}


def slugify(name: str) -> str:
    """Convert a category label like ``General SEO`` to ``general-seo``."""
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s or UNCATEGORIZED


def primary_category(raw: str, source_dir: str = "") -> str:
    """Return the primary bucket slug for a ``categories`` field."""
    if not raw:
        return UNCATEGORIZED
    first = raw.split("|", 1)[0].strip()
    # Guard against garbage like ``[|]`` -> first token = ``[``.
    if not first or first in {"[", "]", "[]"}:
        return UNCATEGORIZED
    slug = slugify(first)
    aliases = BUCKET_ALIASES.get(source_dir, {})
    return aliases.get(slug, slug)


def load_records() -> list[dict]:
    with JSONL_PATH.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def build_plan(records: list[dict], source_dir: str) -> tuple[dict[str, str], Counter]:
    """Return (old_path -> new_path map, bucket counter)."""
    plan: dict[str, str] = {}
    counter: Counter = Counter()
    for rec in records:
        if rec.get("source_dir") != source_dir:
            continue
        old_path = rec["path"]  # e.g. <source_dir>/foo.md
        assert old_path.startswith(f"{source_dir}/"), old_path
        filename = old_path[len(source_dir) + 1 :]
        # Skip already-nested files (idempotent).
        if "/" in filename:
            continue
        bucket = primary_category(rec.get("categories", ""), source_dir)
        new_path = f"{source_dir}/{bucket}/{filename}"
        plan[old_path] = new_path
        counter[bucket] += 1
    return plan, counter


def detect_collisions(plan: dict[str, str]) -> list[str]:
    seen: dict[str, str] = {}
    problems: list[str] = []
    for old, new in plan.items():
        if new in seen:
            problems.append(f"COLLISION: {new} <- {seen[new]} AND {old}")
        else:
            seen[new] = old
    return problems


def check_files_exist(plan: dict[str, str]) -> list[str]:
    missing = []
    for old in plan:
        if not (REPO_ROOT / old).is_file():
            missing.append(old)
    return missing


def git_mv(old: str, new: str) -> None:
    dest = REPO_ROOT / new
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["git", "mv", old, new],
        cwd=REPO_ROOT,
        check=True,
    )


def rewrite_jsonl(plan: dict[str, str]) -> None:
    records = load_records()
    for rec in records:
        old = rec.get("path")
        if old in plan:
            rec["path"] = plan[old]
    tmp = JSONL_PATH.with_suffix(".jsonl.tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    tmp.replace(JSONL_PATH)


def rewrite_csv(plan: dict[str, str]) -> None:
    # Read with utf-8-sig in case of BOM; write plain utf-8, LF.
    with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        return
    header = rows[0]
    path_idx = header.index("path")
    for row in rows[1:]:
        if row and row[path_idx] in plan:
            row[path_idx] = plan[row[path_idx]]
    tmp = CSV_PATH.with_suffix(".csv.tmp")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(rows)
    tmp.replace(CSV_PATH)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        default="ahrefs-blog",
        help="Source blog directory to reorganize (default: ahrefs-blog).",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually move files and rewrite metadata (default: dry-run).",
    )
    args = parser.parse_args()

    # Force UTF-8 stdout on Windows.
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")

    source_dir = args.source
    records = load_records()
    plan, counter = build_plan(records, source_dir)

    print(f"Source: {source_dir}")
    print(f"Total files to move: {len(plan)}")
    print(f"Buckets: {len(counter)}")
    print()
    print(f"{'count':>6}  bucket")
    print(f"{'-----':>6}  ------")
    for bucket, n in counter.most_common():
        print(f"{n:>6}  {bucket}")
    print()

    missing = check_files_exist(plan)
    if missing:
        print(f"WARNING: {len(missing)} file(s) referenced in metadata are missing on disk:")
        for m in missing[:10]:
            print(f"  - {m}")
        if len(missing) > 10:
            print(f"  ... and {len(missing) - 10} more")
        print()

    collisions = detect_collisions(plan)
    if collisions:
        print(f"ERROR: {len(collisions)} collision(s):")
        for c in collisions[:10]:
            print(f"  {c}")
        return 2

    # Also flag any on-disk .md files NOT covered by the plan.
    disk_files = {
        f"{source_dir}/{p.name}"
        for p in (REPO_ROOT / source_dir).iterdir()
        if p.is_file() and p.suffix == ".md"
    }
    orphans = disk_files - set(plan)
    if orphans:
        print(f"WARNING: {len(orphans)} .md file(s) on disk without metadata entry:")
        for o in sorted(orphans)[:10]:
            print(f"  - {o}")
        if len(orphans) > 10:
            print(f"  ... and {len(orphans) - 10} more")
        print()

    if not args.apply:
        print("Dry-run only. Re-run with --apply to execute.")
        return 0

    # Skip missing files from the actual move plan.
    missing_set = set(missing)
    executable_plan = {k: v for k, v in plan.items() if k not in missing_set}

    print(f"Moving {len(executable_plan)} files with git mv ...")
    for i, (old, new) in enumerate(executable_plan.items(), 1):
        git_mv(old, new)
        if i % 100 == 0:
            print(f"  moved {i}/{len(executable_plan)}")
    print("Move complete.")

    print("Rewriting metadata/index.jsonl ...")
    rewrite_jsonl(executable_plan)
    print("Rewriting metadata/index.csv ...")
    rewrite_csv(executable_plan)
    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
