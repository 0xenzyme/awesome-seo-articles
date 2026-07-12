---
title: "Improved Search Queries stats for separate mobile sites"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2014-01-improved-search-queries-stats"
url: "https://developers.google.com/search/blog/2014/01/improved-search-queries-stats"
canonical: "https://developers.google.com/search/blog/2014/01/improved-search-queries-stats"
author: "Maile Ohye"
published: "2014-01-07T00:00:00+00:00"
updated: "2014-01-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:23:35+00:00"
status_code: 200
html_hash: "46631a8004c3e52805960bff6ed20b6a717a880cd2cae50c4ae7595d26e0a4e7"
clean_word_count: 341
clean_char_count: 2332
---
# Improved Search Queries stats for separate mobile sites

Search Queries in
[Webmaster Tools](https://search.google.com/search-console) just
became more cohesive for those who manage a mobile site on a separate URL from desktop, such as
mobile on m.example.com and desktop on www. In
[Search Queries](https://support.google.com/webmasters/answer/35252),
when you view your m. site\* and set Filters to "Mobile," from Dec 31, 2013 onwards, you'll now
see:

- Queries where your m. pages appeared in search results for mobile browsers
- Queries where Google applied
  [Skip Redirect](/search/blog/2011/12/introducing-smartphone-googlebot-mobile). This
  means that, while search results displayed the desktop URL, the user was automatically directed
  to the corresponding m. version of the URL (thus saving the user from latency of a server-side
  redirect).

![Skip Redirect information (impressions, clicks, etc.) calculated with mobile site.](/static/search/blog/images/archived_1_Screen_Shot_2014-01-06_at_9.25.26_PM.png)

Prior to this Search Queries improvement, Webmaster Tools reported Skip Redirect impressions with
the desktop URL. Now we've consolidated information when Skip Redirect is triggered, so that
impressions, clicks, and CTR are calculated solely with the verified m. site, making your mobile
statistics more understandable.

## Best practices if you have a separate m. site

Here are a few search-friendly recommendations for those publishing content on a separate m. site:

- Follow our advice on
  [Building Smartphone-Optimized Websites](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
- On the desktop page, add a special link `rel="alternate"` tag pointing to the
  corresponding mobile URL. This helps Googlebot discover the location of your site's mobile
  pages.
- On the mobile page, add a link
  [`rel="canonical"`](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  tag pointing to the corresponding desktop URL.
- Use the `HTTP Vary: User-Agent` header if your servers automatically redirect users
  based on their user agent/device.
- Verify ownership of both the desktop (www) and mobile (m.) sites in Webmaster Tools for improved
  communication and troubleshooting information specific to each site.

Be sure you've verified ownership for your mobile site!
