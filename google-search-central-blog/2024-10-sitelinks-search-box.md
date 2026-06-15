---
title: "Farewell, Sitelinks Search Box"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2024-10-sitelinks-search-box"
url: "https://developers.google.com/search/blog/2024/10/sitelinks-search-box"
canonical: "https://developers.google.com/search/blog/2024/10/sitelinks-search-box"
author: "John Mueller"
published: "2024-10-21T00:00:00+00:00"
updated: "2024-10-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:44:14+00:00"
status_code: 200
html_hash: "3dc91399382354208191117bb861738032daec992a90d24d6ced739cb71a38fd"
clean_word_count: 261
clean_char_count: 1746
---
# Farewell, Sitelinks Search Box

It's been over ten years since we initially announced the
[sitelinks search box in Google Search](/search/blog/2014/09/improved-sitelinks-search-box),
and over time, we've noticed that usage has dropped. With that, and to help simplify the search
results, we'll be removing this visual element starting on November 21, 2024.

![Search result showing a sitelinks search box](/static/search/blog/images/slsb-example-2024.png)

(Search result showing a sitelinks search box)

This change will apply globally across all search results, in all languages and countries.
This doesn't affect rankings or the [other sitelinks
visual element](/search/docs/appearance/sitelinks), and won't be listed in the Search status dashboard.
Once we stop showing sitelinks search box elements in Search, we'll remove the
[Search
Console rich results report](https://support.google.com/webmasters/answer/7552505) for it and stop highlighting the markup in the
[Rich Results Test](https://search.google.com/test/rich-results).

While you can remove
[sitelinks search box structured data](/search/docs/appearance/structured-data/sitelinks-searchbox)
from your site, there's no need to do so.
Unsupported structured data like this won't cause issues in Search, and won't trigger errors in
Search Console reports.
If you decide to remove sitelinks search box structured data, note that
[site names](/search/docs/appearance/site-names#add-structured-data) also uses a
variation of `WebSite` structured data, which continues to be supported.

If you have any questions, feel free to drop by our
[Search Central help community](https://goo.gle/sc-forum), or
ping us on [social media](https://www.linkedin.com/showcase/googlesearchcentral/).
