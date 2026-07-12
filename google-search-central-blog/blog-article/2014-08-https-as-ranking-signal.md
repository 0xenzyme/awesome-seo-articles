---
title: "HTTPS as a ranking signal"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-08-https-as-ranking-signal"
url: "https://developers.google.com/search/blog/2014/08/https-as-ranking-signal"
canonical: "https://developers.google.com/search/blog/2014/08/https-as-ranking-signal"
author: "Zineb Ait Bahajji, Gary Illyes"
published: "2014-08-07T00:00:00+00:00"
updated: "2014-08-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:25:16+00:00"
status_code: 200
html_hash: "f2f8624357c81da9cc41a30e224d784f0c0b12b71dcac4ba70b6c696e8401f88"
clean_word_count: 534
clean_char_count: 3319
---
# HTTPS as a ranking signal

Security is a top priority for Google. We invest a lot in making sure that our services use
industry-leading security, like
[strong HTTPS encryption by default](https://googleonlinesecurity.blogspot.com/2011/11/protecting-data-for-long-term-with.html).
That means that people using Search, Gmail and Google Drive, for example, automatically have a
secure connection to Google.

Beyond our own stuff, we're also working to make the Internet safer more broadly. A big part of
that is making sure that websites people access from Google are secure. For instance, we have
created resources to help webmasters
[prevent and fix security breaches](/web/fundamentals/security/hacked)
on their sites.

We want to go even further. At [Google I/O](https://events.google.com/io)
a few months ago, we called for
["HTTPS everywhere"](https://www.youtube.com/watch?v=cBhZ6S0PFCY) on
the web.

We've also seen more and more webmasters adopting
[HTTPS](https://en.wikipedia.org/wiki/HTTP_Secure)
(also known as HTTP over
[TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security),
or Transport Layer Security), on their website, which is encouraging.

For these reasons, over the past few months we've been running tests taking into account whether
sites use secure, encrypted connections as a signal in our search ranking algorithms. We've seen
positive results, so we're starting to use HTTPS as a ranking signal. For now it's only a very
lightweight signal—affecting fewer than 1% of global queries, and carrying less weight than
other signals such as
[high-quality content](/search/docs/fundamentals/seo-starter-guide)
—while we give webmasters time to switch to HTTPS. But over time, we may decide to
strengthen it, because we'd like to encourage all website owners to switch from HTTP to HTTPS
to keep everyone safe on the web.

![An image of a lock that conveys that moving from HTTP to HTTPS keeps everyone safe on the web](/static/search/blog/images/security.png)

In the coming weeks, we'll publish detailed best practices (it's in our
[documentation](/search/docs/advanced/security/https) now) to make TLS adoption easier,
and to avoid common mistakes. Here are some basic tips to get started:

- Decide the kind of certificate you need: single, multi-domain, or wildcard certificate
- Use 2048-bit key certificates
- Use relative URLs for resources that reside on the same secure domain
- Use protocol relative URLs for all other domains
- Check out our
  [Site move article](/search/docs/crawling-indexing/site-move-with-url-changes)
  for more guidelines on how to change your website's address
- Don't block your HTTPS site from crawling using robots.txt
- Allow indexing of your pages by search engines where possible. Avoid the `noindex`
  robots `meta` tag.

If your website is already serving on HTTPS, you can test its security level and configuration
with the
[Qualys Lab tool](https://www.ssllabs.com/ssltest/). If you are
concerned about TLS and your site's performance, have a look at
[Is TLS fast yet?](https://istlsfastyet.com/). And of course, if you
have any questions or concerns, please you can post in our
[Webmaster Help Forums](https://support.google.com/webmasters/community).

We hope to see more websites using HTTPS in the future. Let's all make the web more secure!
