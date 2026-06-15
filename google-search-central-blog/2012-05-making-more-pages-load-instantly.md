---
title: "Making more pages load instantly"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2012-05-making-more-pages-load-instantly"
url: "https://developers.google.com/search/blog/2012/05/making-more-pages-load-instantly"
canonical: "https://developers.google.com/search/blog/2012/05/making-more-pages-load-instantly"
author: "Ziga Mahkovec"
published: "2012-05-17T00:00:00+00:00"
updated: "2012-05-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:19:00+00:00"
status_code: 200
html_hash: "33acfd5ce729d0bb9e0cc06c4c6ee9b981c6282c4402c523d2f52c606ac66132"
clean_word_count: 307
clean_char_count: 1898
---
# Making more pages load instantly

At Google we're obsessed with speed. We've long known that even seemingly minor speed increases
can have
[surprisingly large impacts](https://googleresearch.blogspot.com/2009/06/speed-matters.html)
on user engagement and happiness. About a year ago we
[rolled out Instant Pages](/search/blog/2011/06/announcing-instant-pages) in pursuit of
that goal. Instant Pages makes use of prerendering technology in Chrome to make your site appear
to load instantly in some cases, with no need for any extra work on your part. Here's a video of
it in action:

We've been closely watching performance and listening to webmaster feedback. Since Instant Pages
rolled out we've saved more than a thousand years of ours users' time. We're very happy with the
results so far, and we'll be gradually increasing how often we trigger the feature.

In the vast majority of cases, webmasters don't have to do anything for their sites to work
correctly with prerendering. As we mentioned in our
[initial announcement of Instant Pages](/search/blog/2011/06/announcing-instant-pages),
search traffic will be measured in Webmaster Tools just like before this feature: only results the
user visits will be counted. If your site keeps track of pageviews on its own, you might be
interested in the
[Page Visibility API](/chrome/whitepapers/pagevisibility), which
allows you to detect when prerendering is occurring and factor those out of your statistics. If
you use an ads or analytics package, check with them to see if their solution is already
prerender-aware; if it is, in many cases you won't need to make any changes at all. If you're
interested in triggering Chrome's prerendering within your own site, see the
[Prerendering in Chrome](/chrome/whitepapers/prerender) article.

Instant Pages means that users arrive at your site happier and more engaged, which is great for
everyone.
