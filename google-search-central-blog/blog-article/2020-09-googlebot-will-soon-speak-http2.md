---
title: "Googlebot will soon speak HTTP/2"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2020-09-googlebot-will-soon-speak-http2"
url: "https://developers.google.com/search/blog/2020/09/googlebot-will-soon-speak-http2"
canonical: "https://developers.google.com/search/blog/2020/09/googlebot-will-soon-speak-http2"
author: "Gary Illyes"
published: "2020-09-17T00:00:00+00:00"
updated: "2020-09-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:37:35+00:00"
status_code: 200
html_hash: "d8d43be721142b55f0f521a40341bd412243bcb0e11c2ab21fdcee62e2446529"
clean_word_count: 1142
clean_char_count: 6762
---
# Googlebot will soon speak HTTP/2

Starting November 2020, Googlebot will start crawling some sites over HTTP/2.

Ever since mainstream browsers started supporting the next major revision of HTTP,
[HTTP/2 or h2](https://en.wikipedia.org/wiki/HTTP/2) for short, web professionals
[asked us](https://support.google.com/webmasters/thread/3884161) whether
Googlebot can crawl over the upgraded, more modern version of the protocol.

Today we're announcing that starting mid November 2020, Googlebot will support crawling over
HTTP/2 for select sites.

## What is HTTP/2

As we said, it's the next [major version of HTTP](https://tools.ietf.org/html/rfc7540), the
protocol the internet primarily uses for transferring data. HTTP/2 is much more robust, efficient,
and faster than its predecessor, due to its architecture and the features it implements for clients
(for example, your browser) and servers. If you want to read more about it, we have a long article on the
[HTTP/2 topic](/web/fundamentals/performance/http2).

## Why we're making this change

In general, we expect this change to make crawling more efficient in terms of server resource usage. With h2,
Googlebot is able to open a single TCP connection to the server and efficiently transfer multiple files over
it in parallel, instead of requiring multiple connections. The fewer connections open, the fewer resources the
server and Googlebot have to spend on crawling.

## How it works

In the first phase, we'll crawl a small number of sites over h2, and we'll ramp up gradually to more sites that
may benefit from the initially supported features, like request multiplexing.

Googlebot decides which site to crawl over h2 based on whether the site supports h2, and whether the site and
Googlebot would benefit from crawling over HTTP/2. If your server supports h2 and Googlebot already crawls a
lot from your site, you may be already eligible for the connection upgrade, and you don't have to do anything.

If your server still only talks HTTP/1.1, that's also fine. There's no explicit drawback for crawling over this
protocol; crawling will remain the same, quality and quantity wise.

## How to opt out

Our preliminary tests showed no issues or negative impact on indexing, but we understand that, for various reasons,
you may want to opt your site out from crawling over HTTP/2. You can do that by instructing the server to respond
with a [421 HTTP status code](https://tools.ietf.org/html/rfc7540#section-9.1.2) when Googlebot attempts
to crawl your site over h2. If that's not feasible at the moment, you can
[send a message to the Googlebot team](https://www.google.com/webmasters/tools/googlebot-report)
(however, this solution is temporary).

If you have more questions about Googlebot and HTTP/2, check the
[questions we thought you might ask](#questions). If you can't find your question, write to
us on [Twitter](https://twitter.com/googlesearchc) and in the
[help forums](https://support.google.com/websearch/community).

## Questions that we thought you might ask

### Why are you upgrading Googlebot now?

The software we use to enable Googlebot to crawl over h2 has matured enough that it can be used in production.

### Do I need to upgrade my server ASAP?

It's really up to you. However, we will only switch to crawling over h2 sites that support it and will
clearly benefit from it. If there's no clear benefit for crawling over h2, Googlebot will still continue
to crawl over h1.

### How do I test if my site supports h2?

[Cloudflare](https://blog.cloudflare.com/tools-for-debugging-testing-and-using-http-2/) has a
blog post with a plethora of different methods to test whether a site supports h2, check it out!

### How do I upgrade my site to h2?

This really depends on your server. We recommend talking to your server administrator or hosting provider.

### How do I convince Googlebot to talk h2 with my site?

You can't. If the site supports h2, it is eligible for being crawled over h2, but only if that would be
beneficial for the site and Googlebot. If crawling over h2 would not result in noticeable resource savings
for example, we would simply continue to crawl the site over HTTP/1.1.

### Why are you not crawling every h2-enabled site over h2?

In our evaluations we found little to no benefit for certain sites (for example, those with very low qps)
when crawling over h2. Therefore we have decided to switch crawling to h2 only when there's clear benefit
for the site. We'll continue to evaluate the performance gains and may change our criteria for switching
in the future.

### How do I know if my site is crawled over h2?

When a site becomes eligible for crawling over h2, the owners of that site registered in Search Console will
get a message saying that some of the crawling traffic may be over h2 going forward. You can also check
in your server logs (for example, in the access.log file if your site runs on Apache).

### Which h2 features are supported by Googlebot?

Googlebot supports most of the features introduced by h2. Some features like server push, which may be
beneficial for rendering, are still being evaluated.

### Does Googlebot support plaintext HTTP/2 (h2c)?

No. Your website must use HTTPS and support HTTP/2 in order to be eligible for crawling over HTTP/2. This
is equivalent to how modern browsers handle it.

### Is Googlebot going to use the ALPN extension to decide which protocol version to use for crawling?

Application-layer protocol negotiation (ALPN) will only be used for sites that are opted in to crawling
over h2, and the only accepted protocol for responses will be h2. If the server responds during the
TLS handshake with a protocol version other than h2, Googlebot will back off and come back later on HTTP/1.1.

### How will different h2 features help with crawling?

Some of the many, but most prominent benefits of h2 include:

- **Multiplexing and concurrency**: Fewer TCP connections open means fewer resources spent.
- **Header compression**: Drastically reduced HTTP header sizes will save resources.
- **Server push**: This feature is not yet enabled; it's still in the evaluation phase.
  It may be beneficial for rendering, but we don't have anything specific to say about it at this point.

If you want to know more about specific h2 features and their relation to crawling, ask us on
[Twitter](https://twitter.com/googlesearchc).

### Will Googlebot crawl more or faster over h2?

The primary benefit of h2 is resource savings, both on the server side, and on Googlebot side. Whether we crawl
using h1 or h2 does not affect how your site is indexed, and hence it does not affect how much we plan to
crawl from your site.

### Is there any ranking benefit for a site in being crawled over h2?

No.
