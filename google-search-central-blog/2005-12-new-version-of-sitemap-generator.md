---
title: "New version of Sitemap Generator"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2005-12-new-version-of-sitemap-generator"
url: "https://developers.google.com/search/blog/2005/12/new-version-of-sitemap-generator"
canonical: "https://developers.google.com/search/blog/2005/12/new-version-of-sitemap-generator"
author: "Vanessa Fox"
published: "2005-12-07T00:00:00+00:00"
updated: "2005-12-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:44:23+00:00"
status_code: 200
html_hash: "f33dde57b9629d39efe2c4e3fdc29f7285cf0659474b3b4eb766522fb3e0caf5"
clean_word_count: 109
clean_char_count: 682
---
# New version of Sitemap Generator

We recently
[uploaded a new version](https://sourceforge.net/project/showfiles.php?group_id=137793&package_id=153422)
(v1.4) of the
[Sitemap Generator](/search/docs/crawling-indexing/sitemaps/overview) tool.

This version has the same features as the last one, but fixes a subtle bug in writing GZip
compressed Sitemap files. The old version stored more path information than it needed to when it
created GZip files, and this was a point of concern for some webmasters.

The bug was found, and the bugfix suggested, by members of the
[Sitemaps community](https://support.google.com/webmasters/community).
Thanks for bringing it to our attention.
