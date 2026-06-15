---
title: "Using the lastmod attribute"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-04-using-lastmod-attribute"
url: "https://developers.google.com/search/blog/2006/04/using-lastmod-attribute"
canonical: "https://developers.google.com/search/blog/2006/04/using-lastmod-attribute"
author: "Vanessa Fox"
published: "2006-04-14T00:00:00+00:00"
updated: "2006-04-14T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:45:23+00:00"
status_code: 200
html_hash: "a2f0b58b21106a8dfdf77541666b4f04084e9994121178b3d914f768fee8f7bd"
clean_word_count: 131
clean_char_count: 825
---
# Using the lastmod attribute

With our
[recent infrastructure changes](/search/blog/2006/03/improving-things-behind-scenes),
we've made some minor changes in how we process the
[lastmod attribute](/search/docs/crawling-indexing/sitemaps/build-sitemap#general-guidelines).
If you omit the time portion, it defaults to midnight UTC (00:00:00Z). If you specify a time, but
omit the timezone, you'll get an invalid date error. You'll also get an invalid date error if you
specify an invalid date or time (like February 80th) or the date isn't in the correct format.
You'll no longer see errors associated with future dates.

Dates must use
[W3C Datetime encoding](https://www.w3.org/TR/NOTE-datetime),
although you can omit the time portion. For instance, the following are both valid:

- 2005-02-21
- 2005-02-21T18:00:15+00:00
