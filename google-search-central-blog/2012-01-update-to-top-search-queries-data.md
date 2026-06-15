---
title: "Update to Top Search Queries data"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2012-01-update-to-top-search-queries-data"
url: "https://developers.google.com/search/blog/2012/01/update-to-top-search-queries-data"
canonical: "https://developers.google.com/search/blog/2012/01/update-to-top-search-queries-data"
author: "Chris Anderson, Susan Moskwa"
published: "2012-01-25T00:00:00+00:00"
updated: "2012-01-25T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:17:29+00:00"
status_code: 200
html_hash: "879f7f02872cc880a9fea7ad0a28708c76494e5d7efdb23b989ab1242debb4d5"
clean_word_count: 295
clean_char_count: 1798
---
# Update to Top Search Queries data

Starting today, we're updating our Top Search Queries feature to make it better match expectations
about search engine rankings. Previously we reported the average position of all URLs from your
site for a given query. As of today, we'll instead average only the top position that a URL from
your site appeared in.

## An example

Let's say Nick searched for "bacon" and URLs from your site appeared in positions 3, 6, and 12.
Jane also searched for "bacon" and URLs from your site appeared in positions 5 and 9. Previously,
we would have averaged all these positions together and shown an Average Position of 7. Going
forward, we'll only average the highest position your site appeared in for each search (3 for
Nick's search and 5 for Jane's search), for an Average Position of 4.

We anticipate that this new method of calculation will more accurately match your expectations
about how a link's position in Google Search results should be reported.

## How will this affect my Top Search Queries data?

This change will affect your Top Search Queries data going forward.
**Historical data will not change.** Note that the change in calculation means that the Average
Position metric will usually stay the same or decrease, as we will no longer be averaging in
lower-ranking URLs.

[Check out the updated Top Search Queries data](https://google.com/webmasters/tools/home)
in the Your site on the web section of Webmaster Tools. And remember, you can also
[download Top Search Queries data programmatically](/search/blog/2011/12/download-search-queries-data-using)!

We look forward to providing you a more representative picture of your Google Search data. Let us
know what you think in our
[Webmaster Forum](https://support.google.com/webmasters/community).
