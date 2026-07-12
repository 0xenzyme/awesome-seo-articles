---
title: "The new evergreen Googlebot"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2019-05-the-new-evergreen-googlebot"
url: "https://developers.google.com/search/blog/2019/05/the-new-evergreen-googlebot"
canonical: "https://developers.google.com/search/blog/2019/05/the-new-evergreen-googlebot"
author: "Martin Splitt"
published: "2019-05-07T00:00:00+00:00"
updated: "2019-05-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:34:19+00:00"
status_code: 200
html_hash: "56e3b64b110ef250c0d9ac3c0125aa13e18831e9416d08bc27c335d6cdaf3e15"
clean_word_count: 223
clean_char_count: 1563
---
# The new evergreen Googlebot

Googlebot is the crawler that visits web pages to include them within Google Search index. The
number one question we got from the community at events and social media was if we could make
Googlebot evergreen with the latest Chromium. Today, we are happy to announce that Googlebot now
runs the latest Chromium rendering engine (74 at the time of this post) when rendering pages for
Search. Moving forward, Googlebot will regularly update its rendering engine to ensure support for
latest web platform features.

## What that means for you

Compared to the previous version, Googlebot now supports 1000+ new features, like:

- ES6 and newer JavaScript features
- [IntersectionObserver for lazy-loading](/web/fundamentals/performance/lazy-loading-guidance/images-and-video#lazy_loading_images)
- [Web Components v1 APIs](/web/fundamentals/web-components)

You should check if you're transpiling or use polyfills specifically for Googlebot and if so,
evaluate if this is still necessary. There are still some limitations, so check our
[troubleshooter for JavaScript-related issues](/search/docs/crawling-indexing/javascript/fix-search-javascript)
and the
[video series on JavaScript SEO](https://www.youtube.com/watch?v=wSwzfEn5-6A&list=PLKoqnv2vTMUPOalM1zuWDP9OQl851WMM9).

Any thoughts on this? Talk to us on
[Twitter](https://twitter.com/googlesearchc), the
[webmaster forums](https://support.google.com/webmasters/community/?gpf=%23!forum%2Fwebmasters),
or join us for the [online office hours](/search/events/join-office-hours).
