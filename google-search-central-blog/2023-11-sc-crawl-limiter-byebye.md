---
title: "Upcoming deprecation of Crawl Rate Limiter Tool in Search Console"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2023-11-sc-crawl-limiter-byebye"
url: "https://developers.google.com/search/blog/2023/11/sc-crawl-limiter-byebye"
canonical: "https://developers.google.com/search/blog/2023/11/sc-crawl-limiter-byebye"
author: "Gary Illyes, Nir Kalush"
published: "2023-11-24T00:00:00+00:00"
updated: "2023-11-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:43:13+00:00"
status_code: 200
html_hash: "a0905be6069efb86e98f93198d3d63208db61bfb3cfdba2c4e55d0a9086a546a"
clean_word_count: 355
clean_char_count: 2247
---
# Upcoming deprecation of Crawl Rate Limiter Tool in Search Console

The crawl rate limiter tool in Search Console is being deprecated on Jan 8th, 2024. This tool has
been
[available for over a decade](/search/blog/2008/12/more-control-of-googlebots-crawl-rate),
but with the improvements we've made to our crawling logic and other tools available to
publishers, its usefulness has dissipated.

Googlebot reacts to how the site–or more specifically the server handling the site–
responds to Googlebot's HTTP requests. For example, if the server persistently returns HTTP
`500` status codes for a range of URLs, Googlebot will automatically, and almost
immediately slow down crawling. Similarly, Googlebot slows down automatically if the response time
for requests gets significantly longer. If you do experience unusually heavy crawling that your
site can't manage on its own, refer to this
[help article](/search/docs/crawling-indexing/reduce-crawl-rate).

In contrast, the rate limiter tool had a much slower effect; in fact it may have taken over a day
for the new limits to be applied on crawling. Fortunately though, site owners rarely had to resort
to using the tool, and those who have, in many cases set the crawling speed to the bare minimum.
With the deprecation of the crawl limiter tool, we're also setting the minimum crawling speed to a
lower rate, comparable to the old crawl rate limits. This means that we effectively continue
honoring the settings that some site owners have set in the past if the Search interest is low,
and our crawlers don't waste the site's bandwidth.

Because of the advances in the automated crawl rate handling, and in the spirit of keeping things
simple for users, we'll be deprecating this tool in Search Console. We are keeping the Googlebot
[report form](/search/docs/crawling-indexing/reduce-crawl-rate) for reporting unusual
Googlebot activities and for emergency cases, but keep in mind that the fastest way to reduce
crawl rate is to instruct Googlebot through server responses as detailed in
[our documentation](/search/docs/crawling-indexing/reduce-crawl-rate).

If you have questions or comments, write in our
[Google Search Central Community](https://support.google.com/webmasters/community).
