---
title: "Introducing smartphone Googlebot-Mobile"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-12-introducing-smartphone-googlebot-mobile"
url: "https://developers.google.com/search/blog/2011/12/introducing-smartphone-googlebot-mobile"
canonical: "https://developers.google.com/search/blog/2011/12/introducing-smartphone-googlebot-mobile"
author: "Yoshikiyo Kato, Software Engineer"
published: "2011-12-15T00:00:00+00:00"
updated: "2011-12-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:16:49+00:00"
status_code: 200
html_hash: "95ccdb1af1ecf7e5b477e13ad4788371f30754e3875b3a3ba9b8a3206741baf9"
clean_word_count: 557
clean_char_count: 3633
---
# Introducing smartphone Googlebot-Mobile

With the number of smartphone users rapidly rising, we're seeing more and more websites providing
content specifically designed to be browsed on smartphones. Today we are happy to announce that
`Googlebot-Mobile` now crawls with a smartphone user-agent in addition to its previous
feature phone user-agents. This is to increase our coverage of smartphone content and to provide a
better search experience for smartphone users.

Here are the main user-agent strings that Googlebot-Mobile now uses:

- **Feature phones Googlebot-Mobile:**

- `SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101
  (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1; +https://www.google.com/bot.html)`
- `DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1;
  +https://www.google.com/bot.html)`

- **Smartphone Googlebot-Mobile:**

- ~~`Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9
  (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7 (compatible;
  Googlebot-Mobile/2.1; +https://www.google.com/bot.html)`~~
- ~~Update October 2013: `Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X)
  AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25
  (compatible; Googlebot-Mobile/2.1; +https://www.google.com/bot.html)`~~
- **Update August 2015**: `Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS
  X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4
  (compatible; Googlebot/2.1; +https://www.google.com/bot.html)`

The content crawled by smartphone Googlebot-Mobile will be used primarily to improve the user
experience on mobile search. For example, the new crawler may discover content specifically
optimized to be browsed on smartphones as well as smartphone-specific redirects.

One new feature we're also launching that uses these signals is
*Skip Redirect for Smartphone-Optimized Pages*. When we discover a URL in our search
results that redirects smartphone users to another URL serving smartphone-optimized content, we
change the link target shown in the search results to point directly to the final destination URL.
This removes the extra latency the redirect introduces leading to a saving of 0.5-1 seconds on
average when visiting landing page for such search results.

**Update 9 August 2013**: If a site uses separate URLs to serve desktop and
smartphone users, and if we discover accurate
[`rel-alternate-media` annotations](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#annotation-in-sitemaps)
linking the desktop and smartphone pages, our algorithms may change the link target shown in the
search results to point directly to the smartphone page.

Since all Googlebot-Mobile user-agents identify themselves as a specific kind of mobile, please
**treat each Googlebot-Mobile request as you would a human user with the same phone
user-agent**. This, and other guidelines are described in our
[previous blog post](/search/blog/2011/02/making-websites-mobile-friendly)
and they still apply, except for those referring to smartphones which we are updating today. If
your site has treated Googlebot-Mobile specially based on the fact that it only crawls with
feature phone user-agents, we strongly recommend reviewing this policy and serving the
appropriate content based on the Googlebot-Mobile's user-agent, so that both your feature phone
and smartphone content will be indexed properly.

If you have more questions, please ask on our
[Webmaster Help forums](https://support.google.com/webmasters/community).
