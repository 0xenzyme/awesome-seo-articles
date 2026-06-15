---
title: "What Crawl Budget Means for Googlebot"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2017-01-what-crawl-budget-means-for-googlebot"
url: "https://developers.google.com/search/blog/2017/01/what-crawl-budget-means-for-googlebot"
canonical: "https://developers.google.com/search/blog/2017/01/what-crawl-budget-means-for-googlebot"
author: "Gary Illyes"
published: "2017-01-16T00:00:00+00:00"
updated: "2017-01-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:30:03+00:00"
status_code: 200
html_hash: "a371a7367157020b5432d0a2db39e9da832ee184da49f031784818f44d43daac"
clean_word_count: 921
clean_char_count: 5749
---
# What Crawl Budget Means for Googlebot

Recently, we've heard a number of definitions for "crawl budget", however we don't have a single
term that would describe everything that "crawl budget" stands for externally. With this post
we'll clarify what we actually have and what it means for Googlebot.

First, we'd like to emphasize that crawl budget, as described below, is not something most
publishers have to worry about. If new pages tend to be crawled the same day they're published,
crawl budget is not something webmasters need to focus on. Likewise, if a site has fewer than a
few thousand URLs, most of the time it will be crawled efficiently.

Prioritizing what to crawl, when, and how much resource the server hosting the site can allocate
to crawling is more important for bigger sites, or those that auto-generate pages based on URL
parameters, for example.

## Crawl rate limit

Googlebot is designed to be a good citizen of the web. Crawling is its main priority, while making
sure it doesn't degrade the experience of users visiting the site. We call this the "crawl rate
limit," which limits the maximum fetching rate for a given site.

Simply put, this represents the number of simultaneous parallel connections Googlebot may use to
crawl the site, as well as the time it has to wait between the fetches. The crawl rate can go up
and down based on a couple of factors:

- **Crawl health**: If the site responds really quickly for a while, the limit goes up,
  meaning more connections can be used to crawl. If the site slows down or responds with server
  errors, the limit goes down and Googlebot crawls less.
- [**Limit set in
  Search Console**](https://support.google.com/webmasters/answer/48620): Website owners can reduce Googlebot's crawling of their site. Note
  that setting higher limits doesn't automatically increase crawling.

## Crawl demand

Even if the crawl rate limit isn't reached, if there's no demand from indexing, there will be low
activity from Googlebot. The two factors that play a significant role in determining crawl demand
are:

- **Popularity**: URLs that are more popular on the Internet tend to be crawled more often to
  keep them fresher in our index.
- **Staleness**: Our systems attempt to prevent URLs from becoming stale in the index.

Additionally, site-wide events like site moves may trigger an increase in crawl demand in order to
reindex the content under the new URLs.

Taking crawl rate and crawl demand together we define crawl budget as the number of URLs Googlebot
can and wants to crawl.

## Factors affecting crawl budget

According to our analysis, having many low-value-add URLs can negatively affect a site's crawling
and indexing. We found that the low-value-add URLs fall into these categories, in order of
significance:

- [Faceted navigation](/search/blog/2014/02/faceted-navigation-best-and-5-of-worst) and
  [session identifiers](/search/blog/2007/09/google-duplicate-content-caused-by-url)
- [On-site duplicate content](/search/blog/2007/09/google-duplicate-content-caused-by-url)
- [Soft error pages](/search/blog/2010/06/crawl-errors-now-reports-soft-404s)
- Hacked pages
- [Infinite spaces](/search/blog/2008/08/to-infinity-and-beyond-no) and proxies
- Low quality and spam content

Wasting server resources on pages like these will drain crawl activity from pages that do actually
have value, which may cause a significant delay in discovering great content on a site.

## Top questions

Crawling is the entry point for sites into Google's search results. Efficient crawling of a
website helps with its indexing in Google Search.

### Does site speed affect my crawl budget? How about errors?

Making a site faster improves the users' experience while also increasing crawl rate. For
Googlebot, a speedy site is a sign of healthy servers, so it can get more content over the
same number of connections. On the flip side, a significant number of 5xx errors or
connection timeouts signal the opposite, and crawling slows down.

We recommend paying attention to the
[Crawl Errors report in Search Console](https://support.google.com/webmasters/answer/35120)
and keeping the number of server errors low.

### Is crawling a ranking factor?

An increased crawl rate will not necessarily lead to better positions in Search results.
Google uses hundreds of signals to rank the results, and while crawling is necessary for
being in the results, it's not a ranking signal.

### Do alternate URLs and embedded content count in the crawl budget?

Generally, any URL that Googlebot crawls will count towards a site's crawl budget.
Alternate URLs, like AMP or hreflang, as well as embedded content, such as CSS and
JavaScript, including AJAX
(like [XHR](https://en.wikipedia.org/wiki/XMLHttpRequest))
calls, may have to be crawled and will consume a site's crawl budget. Similarly, long
redirect chains may have a negative effect on crawling.

### Can I control Googlebot with the `crawl-delay` rule?

The non-standard `crawl-delay` robots.txt rule is not processed by Googlebot.

### Does the `nofollow` rule affect crawl budget?

It depends. Any URL that is crawled affects crawl budget, so even if your page marks a URL
as `nofollow` it can still be crawled if another page on your site, or any page on the web,
doesn't label the link as nofollow.

### Do URLs I disallowed through robots.txt affect my crawl budget in any way?

No, disallowed URLs do not affect the crawl budget.

For information on how to optimize crawling of your site, take a look at our blogpost on
[optimizing crawling](/search/blog/2009/08/optimize-your-crawling-indexing)
from 2009 that is still applicable. If you have questions, ask in the
[forums](https://support.google.com/webmasters/community/)!
