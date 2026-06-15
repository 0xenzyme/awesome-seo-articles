---
title: "Minor cleaning up in the Search Console API"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2019-08-minor-cleaning-up-in-search-console-api"
url: "https://developers.google.com/search/blog/2019/08/minor-cleaning-up-in-search-console-api"
canonical: "https://developers.google.com/search/blog/2019/08/minor-cleaning-up-in-search-console-api"
author: "Ziv Hodak"
published: "2019-08-26T00:00:00+00:00"
updated: "2019-08-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:34:45+00:00"
status_code: 200
html_hash: "b6c8e6eecb546aaa7a94a15db91196aa21550f2e22487566daad01c43d51342e"
clean_word_count: 164
clean_char_count: 1052
---
# Minor cleaning up in the Search Console API

With the move to the
[new Search Console](https://support.google.com/webmasters/answer/7451491),
we've decided to clean up some parts of the Search Console API as well. In the
[Search Analytics API](/webmaster-tools/search-console-api-original/v3/searchanalytics),
going forward we'll no longer support these Android app search appearance types:

- Is Install
- Is App Universal
- Is Opened

Since these appearance types are no longer used in the UI, they haven't been populated with data
recently. Going forward, we won't be showing these types at all through the API.

Additionally, for the
[Sitemaps API](/webmaster-tools/search-console-api-original/v3/sitemaps),
we're no longer populating data on indexing status of submitted sitemap files in the "Indexed"
field.

We're still committed to the Search Console API. In particular, we're working on updating the
Search Console API to the new Search Console. We don't have any specific timeframes to share at
the moment, but stay tuned to find out more!
