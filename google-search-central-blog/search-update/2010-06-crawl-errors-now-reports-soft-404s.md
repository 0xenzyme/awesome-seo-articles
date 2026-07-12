---
title: "Crawl Errors now reports soft 404s"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2010-06-crawl-errors-now-reports-soft-404s"
url: "https://developers.google.com/search/blog/2010/06/crawl-errors-now-reports-soft-404s"
canonical: "https://developers.google.com/search/blog/2010/06/crawl-errors-now-reports-soft-404s"
author: "Jonathan Simon"
published: "2010-06-07T00:00:00+00:00"
updated: "2010-06-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:07:00+00:00"
status_code: 200
html_hash: "e19d699fa39b0e78491914e126508fa201d1a87a335e5c82e89061573abce3eb"
clean_word_count: 378
clean_char_count: 2342
---
# Crawl Errors now reports soft 404s

Today we're releasing a feature to help you discover if your site serves undesirable
`soft` or `crypto` `404`s. A `soft 404` occurs
when a webserver responds with a `200 OK`
[HTTP response code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
for a page that doesn't exist rather than the appropriate `404 Not Found`.
`Soft 404`s can limit a site's crawl coverage by search engines because these duplicate
URLs may be crawled instead of pages with unique content.

The web is infinite, but the time search engines spend crawling your site is limited. Properly
reporting non-existent pages with a `404` or `410` response code can improve
the crawl coverage of your site's best content. Additionally, `soft 404`s can
potentially be confusing for your site's visitors as described in our past blog post,
[Farewell to `soft 404` pages](/search/blog/2008/08/farewell-to-soft-404s).

You can find the new `soft 404` reporting feature under the Crawl errors section in
[Webmaster Tools](https://search.google.com/search-console).

![soft 404 errors in the crawl error feature in webmaster tools](/static/search/blog/images/import/19c645520ae91827ff095e50ae170637.png)

Here's a list of steps to correct `soft 404` errors to help both Google and your users:

1. Check whether you have `soft 404` errors listed in Webmaster Tools
2. For the `soft 404` errors, determine whether the URL:

1. Contains the correct content and properly returns a `200` response (not actually a
   `soft 404`)
2. Should `301` redirect to a more accurate URL
3. Doesn't exist and should return a `404` or `410` response

3. Confirm that you've configured the proper HTTP Response by using
   [Fetch as Googlebot](/search/blog/2009/10/fetch-as-googlebot-and-malware-details)
   in Webmaster Tools
4. If you now return `404` errors, you may want to customize your `404` page to aid
   your users. Our
   [custom `404` widget](/search/docs/crawling-indexing/http-network-errors#pagegone)
   can help.

We hope that you're now better enabled to find and correct `soft 404` errors on your
site. If you have feedback or questions about the new `soft 404` error reporting
feature or any other Webmaster Tools feature, please share your thoughts with us in the
[Webmaster Help Forum](https://support.google.com/webmasters/community).
