---
title: "To infinity and beyond? No!"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-08-to-infinity-and-beyond-no"
url: "https://developers.google.com/search/blog/2008/08/to-infinity-and-beyond-no"
canonical: "https://developers.google.com/search/blog/2008/08/to-infinity-and-beyond-no"
author: "Written by Torrey Hoffman, Webmaster Tools team"
published: "2008-08-05T00:00:00+00:00"
updated: "2008-08-05T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:53:58+00:00"
status_code: 200
html_hash: "7f8e819d05adf166970a4eb7dcbe612dbea4b50e683f9c3ec1d9317c143935bf"
clean_word_count: 458
clean_char_count: 2850
---
# To infinity and beyond? No!

When Googlebot crawls the web, it often finds what we call an "infinite space". These are very
large numbers of links that usually provide little or no new content for Googlebot to index. If
this happens on your site, crawling those URLs may use unnecessary bandwidth, and could result in
Googlebot failing to completely index the real content on your site.

Recently, we started notifying site owners when we discover this problem on their web sites. Like
most messages we send, you'll find them in
[Webmaster Tools](https://search.google.com/search-console)
in the Message Center. You'll probably want to know right away if Googlebot has this
problem—or other problems—crawling your sites. So verify your site with Webmaster
Tools, and check the Message Center every now and then.

![webmaster tools message informing the owner of a site about an infinite space](/static/search/blog/images/import/551feac03a9f6df6d50c1138bfb44b5c.png)

## Examples of an infinite space

The classic example of an "infinite space" is a calendar with a "Next Month" link. It may be
possible to keep following those "Next Month" links forever! Of course, that's not what you want
Googlebot to do. Googlebot is smart enough to figure out some of those on its own, but there are
a lot of ways to create an infinite space and we may not detect all of them.

![example calendar page showing no event for a specific day](/static/search/blog/images/import/9806fcd08a5fe2ea61a695cafd36c269.png)

Another common scenario is websites which provide for filtering a set of search results in many
ways. A shopping site might allow for finding clothing items by filtering on category, price,
color, brand, style, etc. The number of possible combinations of filters can grow exponentially.
This can produce thousands of URLs, all finding some subset of the items sold. This may be
convenient for your users, but is not so helpful for the Googlebot, which just wants to find
everything&mdashl;once!

## Correcting infinite space issues

Our
[Webmaster Tools Help article](https://www.google.com/support/webmasters/bin/answer.py?answer=76401)
describes more ways infinite spaces can arise, and provides recommendations on how to avoid the
problem. One fix is to eliminate whole categories of dynamically generated links using your
robots.txt file.
[The Help Center has lots of information on how to use robots.txt](/search/docs/crawling-indexing/robots/intro).
If you do that,
[don't forget to verify that Googlebot can find all your content](https://www.google.com/webmasters/tools/robots-testing-tool)
some other way. Another option is to block those problematic links with a `nofollow`
link attribute. If you'd like
[more information on `nofollow` links](/search/docs/advanced/guidelines/qualify-outbound-links),
check out the Webmaster Help Center.
