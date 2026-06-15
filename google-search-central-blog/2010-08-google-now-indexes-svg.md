---
title: "Google now indexes SVG"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2010-08-google-now-indexes-svg"
url: "https://developers.google.com/search/blog/2010/08/google-now-indexes-svg"
canonical: "https://developers.google.com/search/blog/2010/08/google-now-indexes-svg"
author: "Bogdan Stanescu and John Sarapata, Software Engineers"
published: "2010-09-01T00:00:00+00:00"
updated: "2010-09-01T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:08:00+00:00"
status_code: 200
html_hash: "042a72657ac6906460d40de8d4418c9b66a208f0d74f6bf1efd438dccf8c9a0f"
clean_word_count: 197
clean_char_count: 1161
---
# Google now indexes SVG

You can now use Google search to find SVG documents.
[SVG](https://www.w3.org/Graphics/SVG/)
is an open, XML-based format for vector graphics with support for interactive elements. We're big
fans of open standards, and our mission is to organize the world's information, so indexing SVG
is a natural step.

We index SVG content whether it is in a standalone file or embedded directly in HTML. The web is
big, so it may take some time before we crawl and index most SVG files, but as of today you may
start seeing them in your search results. If you want to see it yourself, try searching for
[sitemap site:fastsvg.com](https://www.google.com/search?q=sitemap+site%3Afastsvg.com)
or
[HideShow site:svg-whiz.com](https://www.google.com/search?q=HideShow+site%3Asvg-whiz.com).

If you host SVG files and you wish to exclude them from Google's search results, you can use the
[`X-Robots-Tag: noindex` rule in the HTTP header](https://googleblog.blogspot.com/2007/07/robots-exclusion-protocol-now-with-even.html).

Check out Webmaster Central for a full list of
[file types we support](/search/docs/crawling-indexing/indexable-file-types).
