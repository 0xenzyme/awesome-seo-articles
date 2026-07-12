---
title: "Resolving issues listed in the Errors tab"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-04-resolving-issues-listed-in-errors-tab"
url: "https://developers.google.com/search/blog/2006/04/resolving-issues-listed-in-errors-tab"
canonical: "https://developers.google.com/search/blog/2006/04/resolving-issues-listed-in-errors-tab"
author: "Vanessa Fox"
published: "2006-04-11T00:00:00+00:00"
updated: "2006-04-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:45:16+00:00"
status_code: 200
html_hash: "3fd6b57db3016b68716d4ab92cefe4d525e76ae02152eb992d1d842b9934128f"
clean_word_count: 145
clean_char_count: 814
---
# Resolving issues listed in the Errors tab

Another question from our mailbag:

**Under the Errors tab, I see a URL listed with a
[`404` error](https://support.google.com/webmasters/answer/9679690).
That page doesn't exist on my site and I don't link to it. Why does this show up?** The Errors tab lists both errors we encountered following links in your Sitemap and
errors we had following links during our regular discovery crawl. If we tried to follow the link
from the Sitemap, the URL lists "Sitemap" beside it. If it doesn't list "Sitemap", then we tried
to follow that link from a web page (either on your site or another site). You might double-check
your site and make sure that none of the internal links are pointing to that URL. If they aren't,
then this URL is probably linked from an external page.
