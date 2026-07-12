---
title: "Better details about when Googlebot last visited a page"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-09-better-details-about-when-googlebot"
url: "https://developers.google.com/search/blog/2006/09/better-details-about-when-googlebot"
canonical: "https://developers.google.com/search/blog/2006/09/better-details-about-when-googlebot"
author: null
published: "2006-09-05T00:00:00+00:00"
updated: "2006-09-05T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:46:22+00:00"
status_code: 200
html_hash: "6fe27d325150661e5480f2248c4b1c14efd91a3bef53f4f80aa90be891a5613f"
clean_word_count: 387
clean_char_count: 2291
---
# Better details about when Googlebot last visited a page

Most people know that Googlebot downloads pages from web servers to crawl the web. Not as many
people know that if Googlebot accesses a page and gets a
`304 (Not-Modified)`
response to a `If-Modified-Since` qualified request, Googlebot doesn't download the
contents of that page. This reduces the bandwidth consumed on your web server.

When you look at Google's cache of a page (for instance, by using the
[`cache:` operator](/search/docs/monitor-debug/search-operators/web-search-cache)
or clicking the Cached link under a URL in the search results), you can see the date that
Googlebot retrieved that page. Previously, the date we listed for the page's cache was the date
that we last successfully fetched the content of the page. This meant that even if we visited a
page very recently, the cache date might be quite a bit older if the page hadn't changed since the
previous visit. This made it difficult for webmasters to use the cache date we display to
determine Googlebot's most recent visit. Consider the following example:

1. Googlebot crawls a page on April 12, 2006.
2. Our cached version of that page notes that "This is Google's cache of
   `https://www.example.com/` as retrieved on April 12, 2006 20:02:06 GMT."
3. Periodically, Googlebot checks to see if that page has changed, and each time, receives a
   `Not-Modified` response. For instance, on August 27, 2006, Googlebot checks the page,
   receives a `Not-Modified` response, and therefore, doesn't download the contents of
   the page.
4. On August 28, 2006, our cached version of the page still shows the April 12, 2006 date—the
   date we last downloaded the page's contents, even though Googlebot last visited the day
   before.

We've recently changed the date we show for the cached page to reflect when Googlebot last
*accessed* it (whether the page had changed or not).
This should make it easier for you to determine the most recent date Googlebot visited the
page. For instance, in the above example, the cached version of the page would now say "This is
Google's cache of `https://www.example.com/` as retrieved on August 27, 2006 13:13:37
GMT."

Note that this change will be reflected for individual pages as we update those pages in our
index.
