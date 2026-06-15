---
title: "Using stats from site: and Sitemap details"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2009-03-using-stats-from-site-and-sitemap"
url: "https://developers.google.com/search/blog/2009/03/using-stats-from-site-and-sitemap"
canonical: "https://developers.google.com/search/blog/2009/03/using-stats-from-site-and-sitemap"
author: "Charlene Perez"
published: "2009-03-05T00:00:00+00:00"
updated: "2009-03-05T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T12:57:26+00:00"
status_code: 200
html_hash: "820fabbdd140d63645ca57942c270cba753db5000833c31756fb140aec20a671"
clean_word_count: 302
clean_char_count: 1891
---
# Using stats from site: and Sitemap details

Every now and then in the webmaster blogosphere and forums, this issue comes up: when a webmaster
performs a `site:example.com` query on their website, the number of indexed results
differs from what is displayed in their Sitemaps report in Webmaster Tools. Such a discrepancy
may smell like a bug, but it's actually by design. Your Sitemap report only reflects the URLs
you've submitted in your Sitemap file. The `site` operator, on the other hand, takes
into account whatever Google has crawled, which may include URLs not included in your Sitemap,
such as newly added URLs or other URLs discovered via links.

Think of the `site operator` as a quick diagnosis of the general health of your site in
Google's index. `site` operator results can show you:

- a rough estimate of how many pages have been indexed
- one indication of if your site has been
  [hacked](/search/blog/2008/04/my-sites-been-hacked-now-what)
- if you have duplicate titles or snippets

Here is an example query using the `site` operator:

![search result page for a site: query](/static/search/blog/images/archived_1_Picture_3.png)

Your Sitemap report provides more granular statistics about the URLs you submitted, such as the
number of indexed URLs vs. the number submitted for crawling, and Sitemap-specific warnings or
errors that may have occurred when Google tried to access your URLs.

![Sitemap report in webmaster tools](/static/search/blog/images/archived_Picture_2.png)

You can check out our Help Center for more on the
[site: operator](/search/docs/monitor-debug/search-operators/all-search-site)
and
[Sitemaps](/search/docs/crawling-indexing/sitemaps/overview). If you have further questions or
issues, please post to our
[Webmaster Help Forum](https://support.google.com/webmasters/community),
where experienced webmasters and Googlers are happy to help.
