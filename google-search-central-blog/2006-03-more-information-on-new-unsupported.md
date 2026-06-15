---
title: "More information on the new \"unsupported file format\" error for Sitemaps"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-03-more-information-on-new-unsupported"
url: "https://developers.google.com/search/blog/2006/03/more-information-on-new-unsupported"
canonical: "https://developers.google.com/search/blog/2006/03/more-information-on-new-unsupported"
author: "Vanessa Fox"
published: "2006-03-20T00:00:00+00:00"
updated: "2006-03-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:45:00+00:00"
status_code: 200
html_hash: "936aa632642c396170df681f85dee6a5f5d74892273f71d3b7f44b0418b8f141"
clean_word_count: 241
clean_char_count: 1528
---
# More information on the new "unsupported file format" error for Sitemaps

As we told you a couple of days ago, we've recently
[enhanced the infrastructure](/search/blog/2006/03/improving-things-behind-scenes) that
processes Sitemaps. We've begun processing Sitemaps against stricter guidelines because we are
committed to interoperability with other tools that are using this
[protocol](/search/docs/crawling-indexing/sitemaps/build-sitemap#xml).
Because of this, some of you now see an "unsupported file format" error for Sitemaps that
previously had an "OK" status.

You'll see this error if the parser doesn't recognize a valid Sitemap file. Here are a few things
to check if you see this error:

- Confirm that the file uses the correct header.
  - For a Sitemap file, the header can look like this:

  ```
  <?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="https://www.google.com/schemas/sitemap/0.84">
  ```

  - For a Sitemap index file, the header can look like this:

  ```
  <?xml version="1.0" encoding="UTF-8"?>
    <sitemapindex xmlns="https://www.google.com/schemas/sitemap/0.84">
  ```
- Ensure the namespace in the header is
  `https://www.google.com/schemas/sitemap/0.84`. Note that this must end in 0.84. If
  it ends in .84, you'll see an error.
- Make sure each XML attribute is enclosed in either single quotes (`'`) or double
  quotes (`"`) and that those quotes are straight, not curly. If you use a word
  processing program, such as Microsoft Word, you may find that it inserts curly quotes.
