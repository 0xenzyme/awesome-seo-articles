import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from preprocess_public_repo import Article, duplicate_canonicals, parse_frontmatter, scan_risky_text


SAMPLE = """---
title: "Hello"
source: ahrefs-blog
content_type: "blog_article"
categories:
  - "General SEO"
  - "AI"
clean_word_count: 12
---
# Hello

Body text.
"""


class FrontmatterTests(unittest.TestCase):
    def test_parses_scalars_and_lists(self) -> None:
        data, body, warnings = parse_frontmatter(SAMPLE)
        self.assertEqual(warnings, [])
        self.assertEqual(data["title"], "Hello")
        self.assertEqual(data["source"], "ahrefs-blog")
        self.assertEqual(data["clean_word_count"], 12)
        self.assertEqual(data["categories"], ["General SEO", "AI"])
        self.assertTrue(body.startswith("# Hello"))

    def test_missing_frontmatter(self) -> None:
        data, body, warnings = parse_frontmatter("# No frontmatter\n")
        self.assertEqual(data, {})
        self.assertEqual(warnings, ["missing_frontmatter"])
        self.assertIn("No frontmatter", body)

    def test_duplicate_canonicals(self) -> None:
        groups = duplicate_canonicals(
            [
                {"canonical": "https://example.com/a", "path": "a.md"},
                {"canonical": "https://example.com/a", "path": "b.md"},
                {"canonical": "https://example.com/c", "path": "c.md"},
            ]
        )
        self.assertEqual(groups, [("https://example.com/a", ["a.md", "b.md"])])

    def test_risky_windows_path(self) -> None:
        article = Article(
            path=Path("x.md"),
            rel_path="x.md",
            source_dir="ahrefs-blog",
            frontmatter={},
            body=r"cached at D:\Users\secret\notes",
            warnings=[],
        )
        self.assertIn("local_windows_path", scan_risky_text(article))


if __name__ == "__main__":
    unittest.main()
