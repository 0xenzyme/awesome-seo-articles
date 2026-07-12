---
title: "New Location for the Google Crawlers' IP Range Files"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "low"
slug: "2026-03-crawler-ip-ranges"
url: "https://developers.google.com/search/blog/2026/03/crawler-ip-ranges"
canonical: "https://developers.google.com/search/blog/2026/03/crawler-ip-ranges"
author: "Gary"
published: "2026-03-31T00:00:00+00:00"
updated: "2026-03-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:46:08+00:00"
status_code: 200
html_hash: "6cd516dcd0a52e622b5596e38a6e16163673d6c8933b8eaacd7e183cd9551a81"
clean_word_count: 135
clean_char_count: 846
---
# New Location for the Google Crawlers' IP Range Files

Just a short note this time!

Currently, you find the JSON files listing Google's IP ranges under the
`/search/apis/ipranges/` directory on
`developers.google.com`. Since these ranges apply to more than
just Google Search crawlers, we're moving them to a more general location:
`developers.google.com/crawling/ipranges/`.

We've already
[updated our documentation](/crawling/docs/crawlers-fetchers/overview-google-crawlers)
to point to this new location. For the time being, the files will continue
to be available at the old `/search/` path as well to give
everyone time to update their systems. However, we encourage you to switch to
the new `/crawling/ipranges/` path as soon as possible. We will
eventually phase out the old locations and redirect them to the new ones
within 6 months.
