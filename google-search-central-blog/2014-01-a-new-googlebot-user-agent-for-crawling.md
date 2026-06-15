---
title: "A new Googlebot user-agent for crawling smartphone content"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-01-a-new-googlebot-user-agent-for-crawling"
url: "https://developers.google.com/search/blog/2014/01/a-new-googlebot-user-agent-for-crawling"
canonical: "https://developers.google.com/search/blog/2014/01/a-new-googlebot-user-agent-for-crawling"
author: "Zhijian He, Smartphone search engineer"
published: "2014-01-23T00:00:00+00:00"
updated: "2014-01-23T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:23:26+00:00"
status_code: 200
html_hash: "a493b8d7e03c780579b6a56567916450bad8ad25f8ba39cef8f5f0a50633dfbd"
clean_word_count: 619
clean_char_count: 4194
---
# A new Googlebot user-agent for crawling smartphone content

Over the years, Google has used different crawlers to crawl and index content for feature phones
and smartphones. These mobile-specific crawlers have all been referred to as Googlebot-Mobile.
However, feature phones and smartphones have considerably different device capabilities, and we've
seen cases where a webmaster inadvertently blocked smartphone crawling or indexing when they
really meant to block just feature phone crawling or indexing. This ambiguity made it impossible
for Google to index smartphone content of some sites, or for Google to recognize that these sites
are smartphone-optimized.

## A new Googlebot for smartphones

To clarify the situation and to give webmasters greater control, we'll be retiring
"Googlebot-Mobile" for smartphones as a user agent starting in 3-4 weeks' time. From then on, the
user agent for smartphones will identify itself simply as "Googlebot" but will still list
mobile elsewhere in the `user-agent` string. Here are the
new and old `user-agent`s:

The new Googlebot for smartphones `user-agent`

:

```
Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4
(KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4
(compatible;  Googlebot /2.1; +https://www.google.com/bot.html)
```

*(updated August 2015)*

```
Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26
(KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25
(compatible; Googlebot/2.1; +https://www.google.com/bot.html)
```

The Googlebot-Mobile for smartphones `user-agent` we will be retiring soon:

```
Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26
(KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25
(compatible; Googlebot-Mobile/2.1; +https://www.google.com/bot.html)
```

This change affects only Googlebot-Mobile for smartphones. The user agent of the regular Googlebot
does not change, and the remaining two Googlebot-Mobile crawlers will continue to refer to feature
phone devices in their `user-agent` strings; for reference, these are:

Regular Googlebot `user-agent`:

```
 Mozilla/5.0 (compatible; Googlebot/2.1; +https://www.google.com/bot.html)
```

The two Googlebot-Mobile user-agents for feature phones:

- ```
  SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1
      UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0
      (compatible; Googlebot-Mobile/2.1; +https://www.google.com/bot.html)
  ```
- ```
  DoCoMo/2.0 N905i(c100;TB;W24H16)
      (compatible; Googlebot-Mobile/2.1; +https://www.google.com/bot.html)
  ```

You can test your site using the
[Fetch as Google feature in Webmaster Tools](https://support.google.com/webmasters/answer/158587),
and you can see a full list of our
[existing crawlers in the Help Center](/search/docs/crawling-indexing/overview-google-crawlers).

## Crawling and indexing

Please note this important implication of the `user-agent` update: **The new
Googlebot for smartphones crawler will follow robots.txt, robots `meta` tag, and HTTP header
rules for `Googlebot` instead of `Googlebot-Mobile`**. For
example, when the new crawler is deployed, this robots.txt rule will block all crawling by
the new `Googlebot` for smartphones `user-agent`, and also the regular
`Googlebot`:

```
User-agent: Googlebot
Disallow: /
```

This robots.txt rule will block crawling by Google's feature phone crawlers:

```
User-agent: Googlebot-Mobile
Disallow: /
```

Based on our internal analyses, this update affects less than 0.001% of URLs while giving
webmasters greater control over the crawling and indexing of their content. As always, if you have
any questions, you can:

- Read our
  [recommendations for building smartphone-optimized sites](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
- Learn more about
  [controlling Googlebot crawling and indexing](/search/docs/crawling-indexing)
- Ask in our
  [Webmaster help forums](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:crawling_indexing_ranking))
  or visit one of our
  [Webmaster Central office hours hangouts](/search/events#sign-up-for-online-seo-office-hours).
