---
title: "Real-world data in PageSpeed Insights"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2018-01-real-world-data-in-pagespeed-insights"
url: "https://developers.google.com/search/blog/2018/01/real-world-data-in-pagespeed-insights"
canonical: "https://developers.google.com/search/blog/2018/01/real-world-data-in-pagespeed-insights"
author: "Mushan Yang (杨沐杉)"
published: "2018-01-10T00:00:00+00:00"
updated: "2018-01-10T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2018_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:31:42+00:00"
status_code: 200
html_hash: "47550ff4fc4ba095d928bc6fec5f200811004c0020e647e6af9531f7ad7cfdb7"
clean_word_count: 406
clean_char_count: 2608
---
# Real-world data in PageSpeed Insights

[PageSpeed Insights](https://pagespeed.web.dev/)
provides information about how well a page adheres to a set of best practices. In the past, these
recommendations were presented without the context of how fast the page performed in the real
world, which made it hard to understand when it was appropriate to apply these optimizations.
Today, we're announcing that PageSpeed Insights will use data from the
[Chrome User Experience Report](https://blog.chromium.org/2017/10/introducing-chrome-user-experience-report.html)
to make better recommendations for developers and the optimization score has been tuned to be more
aligned with the real-world data.

The PSI report now has several different elements:

- The Speed score categorizes a page as being Fast, Average, or Slow. This is determined by
  looking at the median value of two metrics: First Contentful Paint
  ([FCP](/web/updates/2017/06/user-centric-performance-metrics))
  and DOM Content Loaded
  ([DCL](/web/fundamentals/performance/critical-rendering-path/measure-crp)).
  If both metrics are in the top one-third of their category, the page is considered fast.
- The Optimization score categorizes a page as being Good, Medium, or Low by estimating its
  performance headroom. The calculation assumes that a developer wants to keep the same appearance
  and functionality of the page.
- The Page Load Distributions section presents how this page's FCP and DCL events are distributed
  in the data set. These events are categorized as Fast (top third), Average (middle third), and
  Slow (bottom third) by comparing to all events in the Chrome User Experience Report.
- The Page Stats section describes the round trips required to load the page's
  [render-blocking resources](/web/fundamentals/performance/critical-rendering-path),
  the total bytes used by the page, and how it compares to the median number of round trips and
  bytes used in the dataset. It can indicate if the page might be faster if the developer modifies
  the appearance and functionality of the page.
- Optimization Suggestions is a list of
  [best practices](/speed/docs/insights/rules)
  that could be applied to this page. If the page is fast, these suggestions are hidden by default, as the page is already in the top third of all pages in the data set.

For more details on these changes, see
[About PageSpeed Insights](/speed/docs/insights/about).
As always, if you have any questions or feedback, please visit our
[forums](https://groups.google.com/forum/)
and please remember to include the URL that is being evaluated.
