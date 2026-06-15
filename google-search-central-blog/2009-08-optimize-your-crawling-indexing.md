---
title: "Optimize your crawling and indexing"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-08-optimize-your-crawling-indexing"
url: "https://developers.google.com/search/blog/2009/08/optimize-your-crawling-indexing"
canonical: "https://developers.google.com/search/blog/2009/08/optimize-your-crawling-indexing"
author: "Susan Moskwa"
published: "2009-08-10T00:00:00+00:00"
updated: "2009-08-10T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:59:55+00:00"
status_code: 200
html_hash: "372b9723ec231ed6de2c51844ee98859fc93e3f1930f6fdff20af5acd81a786a"
clean_word_count: 671
clean_char_count: 4135
---
# Optimize your crawling and indexing

Many questions about website architecture, crawling and indexing, and even ranking issues can be
boiled down to one central issue:
**How easy is it for search engines to crawl your site?**
We've spoken on this topic at a number of recent events, and below you'll find our presentation
and some key takeaways on this topic.

[The Internet is a *big*place](https://googleblog.blogspot.com/2008/07/we-knew-web-was-big.html);
new content is being created all the time. Google has a finite number of resources, so when faced
with the nearly-infinite quantity of content that's available online, Googlebot is only able to
find and crawl a percentage of that content. Then, of the content we've crawled, we're only able
to index a portion.

URLs are like the bridges between your website and a search engine's crawler: crawlers need to be
able to find and cross those bridges (that is, find and crawl your URLs) in order to get to your
site's content. If your URLs are complicated or redundant, crawlers are going to spend time
tracing and retracing their steps; if your URLs are organized and lead directly to distinct
content, crawlers can spend their time accessing your content rather than crawling through empty
pages, or crawling the same content over and over via different URLs.

In the slides above you can see some examples of what *not* to do—real-life examples
(though names have been changed to protect the innocent) of homegrown URL hacks and encodings,
parameters masquerading as part of the URL path, infinite crawl spaces, and more. You'll also
find some recommendations for straightening out that labyrinth of URLs and helping crawlers find
more of your content faster, including:

- **Remove user-specific details from URLs.** URL parameters that don't change the
  content of the page—like session IDs or sort order—can be removed from the URL and put into a
  cookie. By putting this information in a cookie and
  [`301` redirecting](/search/docs/crawling-indexing/301-redirects)
  to a "clean" URL, you retain the information and reduce the number of URLs pointing to that same
  content.
- **Rein in infinite spaces.** Do you have a calendar that links to an infinite
  number of past or future dates (each with their own unique URL)? Do you have paginated data
  that returns a
  [status code of `200`](/search/docs/crawling-indexing/http-network-errors)
  when you add `&page=3563` to the URL, even if there aren't that many pages of
  data? If so, you have an
  [infinite crawl space](/search/blog/2008/08/to-infinity-and-beyond-no) on your
  website, and crawlers could be wasting their (and your!) bandwidth trying to crawl it all.
  Consider
  [these tips](https://www.google.com/support/webmasters/bin/answer.py?answer=76401)
  for reining in infinite spaces.
- **Disallow actions Googlebot can't perform.** Using your
  [robots.txt file](/search/docs/crawling-indexing/robots/intro), you can disallow crawling of
  login pages, contact forms, shopping carts, and other pages whose sole functionality is
  something that a crawler can't perform. (Crawlers are notoriously cheap and shy, so they don't
  usually "Add to cart" or "Contact us.") This lets crawlers spend more of their time crawling
  content that they can actually do something with.
- **One man, one vote. One URL, one set of content.** In an ideal world, there's a
  one-to-one pairing between URL and content: each URL leads to a unique piece of content, and
  each piece of content can only be accessed via one URL. The closer you can get to this ideal,
  the more streamlined your site will be for crawling and indexing. If your CMS or current site
  setup makes this difficult, you can
  [use the `rel="canonical"` element](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  to indicate the preferred URL for a particular piece of content.

If you have further questions about optimizing your site for crawling and indexing, check out some
of our [previous writing](/search/help/crawling-index-faq) on the subject, or stop by
our
[Help Forum](https://support.google.com/webmasters/community).
