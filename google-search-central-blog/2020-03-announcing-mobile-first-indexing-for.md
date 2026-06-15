---
title: "Announcing mobile first indexing for the whole web"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2020-03-announcing-mobile-first-indexing-for"
url: "https://developers.google.com/search/blog/2020/03/announcing-mobile-first-indexing-for"
canonical: "https://developers.google.com/search/blog/2020/03/announcing-mobile-first-indexing-for"
author: "John Mueller"
published: "2020-03-05T00:00:00+00:00"
updated: "2020-03-05T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:36:14+00:00"
status_code: 200
html_hash: "3fb0ed49f2d0956ef01f28116816ee8bed027c574248c13f76ae7efe83a00d4c"
clean_word_count: 534
clean_char_count: 3604
---
# Announcing mobile first indexing for the whole web

It's been a few years now that Google started working on
[mobile-first indexing](/search/blog/2016/11/mobile-first-indexing) - Google's
crawling of the web using a smartphone Googlebot. From our analysis, most sites shown
in search results are good to go for mobile-first indexing, and 70% of those shown in our search
results have already shifted over. To simplify, we'll be switching to mobile-first indexing for
all websites starting September 2020. In the meantime, we'll continue moving sites to
mobile-first indexing when our systems recognize that they're ready.

When we switch a domain to mobile-first indexing, it will see an increase in Googlebot's
crawling, while we update our index to your site's mobile version. Depending on the domain, this
change can take some time. Afterwards, we'll still occasionally crawl with the traditional
desktop Googlebot, but most crawling for Search will be done with our
[mobile smartphone user-agent](/search/docs/crawling-indexing/overview-google-crawlers).
The exact user-agent name used will
[match the Chromium version used for rendering](/search/blog/2019/10/updating-user-agent-of-googlebot).

In
[Search Console](https://search.google.com/search-console/about), there are multiple
ways to check for mobile-first indexing. The status is shown on the
[settings page](https://search.google.com/search-console/settings), as well as in the
[URL Inspection Tool](https://support.google.com/webmasters/answer/9012289), when
checking a specific URL with regards to its most recent crawling.

Our guidance on
[making all websites work well for mobile-first indexing](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
continues to be relevant, for new and existing sites. In particular, we recommend making sure
that the content shown is the same (including text,
[images](/search/docs/appearance/google-images),
[videos](/search/docs/appearance/video), links), and that meta data
([titles](/search/docs/appearance/title-link) and [descriptions](/search/docs/appearance/snippet),
[robots `meta` tags](/search/docs/crawling-indexing/robots-meta-tag)) and all
[structured data](/search/docs/appearance/structured-data/search-gallery)
is the same. It's good to double-check these when a website is launched or significantly
redesigned. In the
[URL Testing Tools](https://support.google.com/webmasters/answer/9012289)
you can easily check both desktop and mobile versions directly. If you use other tools to
analyze your website, such as crawlers or monitoring tools, use a mobile user-agent if you want
to match what Google Search sees.

While we continue to support
[various ways of making mobile websites](/search/mobile-sites/mobile-seo), we recommend
[responsive web design](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#responsive-design)
for new websites. We suggest not using separate mobile URLs (often called "m-dot") because of
issues and confusion we've seen over the years, both from search engines and users.

Mobile-first indexing has come a long way. It's great to see how the web has evolved from desktop
to mobile, and how webmasters have helped to allow crawling and indexing to match how users
interact with the web! We appreciate all your work over the years, which has helped to make this
transition fairly smooth. We'll continue to monitor and evaluate these changes carefully. If you
have any questions, please drop by our
[Webmaster forums](https://support.google.com/webmasters/go/community) or our
[public events](/search/events).
