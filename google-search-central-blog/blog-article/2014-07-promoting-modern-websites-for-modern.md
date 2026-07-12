---
title: "Promoting modern websites for modern devices in Google search results"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-07-promoting-modern-websites-for-modern"
url: "https://developers.google.com/search/blog/2014/07/promoting-modern-websites-for-modern"
canonical: "https://developers.google.com/search/blog/2014/07/promoting-modern-websites-for-modern"
author: "Pierre Far"
published: "2014-07-15T00:00:00+00:00"
updated: "2014-07-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:25:07+00:00"
status_code: 200
html_hash: "720977df954e317ff77038ee1d4e596b3bbb2e9080068961665443e84b208cfc"
clean_word_count: 356
clean_char_count: 2338
---
# Promoting modern websites for modern devices in Google search results

A common annoyance for web users is when websites require browser technologies that are not
supported by their device. When users access such pages, they may see nothing but a blank space or
miss out a large portion of the page's contents.

Starting today in our English search results in the US, we will indicate to searchers when our
algorithms detect pages that may not work on their devices. For example, Adobe Flash is not
supported on iOS devices or on Android versions 4.1 and higher, and a page whose contents are
mostly Flash may be noted like this:

![](/static/search/blog/images/import/970164be6d4109aa22ba68217b2426c6.png)

## Developing modern multi-device websites

Fortunately, making websites that work on all modern devices is not that hard: websites can use
HTML5 since it is universally supported, sometimes exclusively, by all devices. To help webmasters
build websites that work on all types of devices regardless of the type of content they wish to
serve, we recently
[announced](https://googledevelopers.blogspot.com/2014/06/web-fundamentals-and-web-starter-kit.html)
two resources:

- [Web Fundamentals](/web/fundamentals): a curated source for
  modern best practices.
- [Web Starter Kit](https://github.com/google/web-starter-kit/):
  a starter framework supporting the Web Fundamentals best practices out of the box.

By following the best practices described in Web Fundamentals you can build a
[responsive web design](/web/fundamentals/layouts), which has long been
[Google's recommendation](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
for search-friendly sites. Be sure not to block crawling of any Googlebot of the page assets
(CSS, JavaScript, and images) using robots.txt or otherwise. Being able to access these external
files fully helps our algorithms detect your site's responsive web design configuration and treat
it appropriately. You can use the
[Fetch and render as Google](https://support.google.com/webmasters/answer/158587)
feature in Webmaster Tools to test how our indexing algorithms see your site.

As always, if you need more help you can ask a question in
[our webmaster forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:crawling_indexing_ranking)).
