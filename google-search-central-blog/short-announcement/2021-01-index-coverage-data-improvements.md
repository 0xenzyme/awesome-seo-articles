---
title: "Index Coverage Data Improvements"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2021-01-index-coverage-data-improvements"
url: "https://developers.google.com/search/blog/2021/01/index-coverage-data-improvements"
canonical: "https://developers.google.com/search/blog/2021/01/index-coverage-data-improvements"
author: "Tal Yadid, Software Engineer, Search Console"
published: "2021-01-11T00:00:00+00:00"
updated: "2021-01-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:38:13+00:00"
status_code: 200
html_hash: "02024754d78f4037c4d53e338fddd9b0c9213557c20e16f4782fb6fb15ee86a9"
clean_word_count: 289
clean_char_count: 1842
---
# Index Coverage Data Improvements

Helping people understand how Google crawls and indexes their sites has been one of the main objectives of Search Console since its
[early days](/search/blog/2005/11/more-stats). When we launched the
[new Search Console](/search/blog/2018/01/introducing-new-search-console), we also introduced the
[Index Coverage report](https://support.google.com/webmasters/answer/7440203), which shows the indexing state of URLs
that Google has visited, or tried to visit, in your property.

Based on the feedback we got from the community, today we are rolling out significant improvements to this report so you’re better informed on issues
that might prevent Google from crawling and indexing your pages. The change is focused on providing a more accurate state to existing issues,
which should help you solve them more easily. The list of changes include:

- Removal of the generic "crawl anomaly" issue type - all crawls errors should now be mapped to an issue with a finer resolution.
- Pages that were submitted but blocked by robots.txt and got indexed are now reported as "indexed but blocked" (warning) instead of "submitted but blocked" (error)
- Addition of a new issue: "[indexed without content](https://support.google.com/webmasters/answer/7440203#indexed_no_content)" (warning)
- `Soft 404` reporting is now more accurate

The changes above are now reflected in the index coverage report so you may see new types of issues or changes in counts of issues. We hope that
this change will help you better understand how [we crawl and index](https://www.google.com/search/howsearchworks/crawling-indexing/) your site.

Please share your feedback about the report through the [Search Central Help Community](https://support.google.com/webmasters/community)
or via [Twitter](https://twitter.com/googlesearchc).
