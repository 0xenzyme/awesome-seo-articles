---
title: "Deeper Integration of Search Console in Google Analytics"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2016-05-deeper-integration-of-search-console-in"
url: "https://developers.google.com/search/blog/2016/05/deeper-integration-of-search-console-in"
canonical: "https://developers.google.com/search/blog/2016/05/deeper-integration-of-search-console-in"
author: "Daniel Waisberg"
published: "2016-05-12T00:00:00+00:00"
updated: "2016-05-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2016_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:28:44+00:00"
status_code: 200
html_hash: "3624641a14d94d51af98f7f529fb3258265fd2a16da767a76831ecb6452c9f3a"
clean_word_count: 652
clean_char_count: 4308
---
# Deeper Integration of Search Console in Google Analytics

*Cross-posted from the
[Google Analytics Blog](https://analytics.blogspot.com/2016/05/deeper-integration-of-search-console-in.html).*

Google Analytics helps brands optimize their websites and marketing efforts for all sources of
traffic, and Search Console is where website owners manage how they appear in Google organic
search results. Today, we are introducing the ability to display Search Console metrics alongside
Google Analytics metrics, in the same reports, side by side—giving you a full view of how
your site shows up and performs in organic search results.

For years, users of both Search Console and Google Analytics have been able to link the two
properties
([instructions](https://support.google.com/analytics/answer/1308621))
and see Search Console statistics in Google Analytics, in isolation. But to gain a fuller picture
of your website's performance in organic Search, it's beneficial to see how visitors reached your
site and what they did once they got there.

With this update, you'll be able to see your Search Console metrics and your Google Analytics
metrics in the same reports, in parallel. By combining data from both sources at the landing page
level, we're able to show you a full range of Acquisition, Behavior and Conversion metrics for
your organic search traffic. This feature out is rolling out over the coming few weeks, so not
everyone will see it immediately.

![New Search Console reports combine Search Console and Google Analytics metrics](/static/search/blog/images/import/21e958f7f2139f3a82edc1be67b8627e.png)

## New Insights

The new reports allow you to examine your organic Search data end-to-end and discover unique and
actionable insights. Your Acquisition metrics from Search Console, such as impressions and average
position, are now available in relation to your Behavior and Conversion metrics from Google
Analytics, like bounce rate and pages per session.

Below are some new capabilities resulting from this improved integration:

- Find landing pages that are attracting many users through Google organic Search (for example, high
  impressions and high click through rate) but where users are not engaging with the website. In
  this case, you should consider improving your landing pages.
- Find landing pages that have high site engagement but are not successfully attracting users from
  Google organic Search (for example, have low click through rate). In this case, you might benefit from
  [improving titles and descriptions shown in Search](/search/docs/appearance/title-link).
- Learn which queries are ranking well for each organic landing page.
- Segment organic performance by device category (desktop, tablet, mobile) in the new Devices
  report.

![New Landing Page report showing Search Console and Google Analytics metrics](/static/search/blog/images/import/38b87e6c4dc3dd25211f95dba6e0d5e0.png)

## Additional Information

Each of these new reports will display how your organic Search traffic performs. As data is joined
at the landing page level, Landing Pages, Countries and Devices will show both Search Console and
Google Analytics data, while the Queries report will only show Search Console data for individual
queries. The same search queries will display in Google Analytics as you see in Search Console
today.

As mentioned in our
[Search Console Help Center](https://support.google.com/webmasters/answer/6155685),
some data may not be displayed, to protect user privacy. For example, Search Console may not track
some infrequent queries, and will not display those that include personal or sensitive
information.

Also, while the data is displayed in parallel, not all Google Analytics features are available for
Search Console data—including segmentation. Any segment that is applied to the new combined
reports will only apply to Google Analytics data. You may also see that clicks from Search Console
may differ from total sessions in Google Analytics.

To experience the new combined reports from Search Console and Google Analytics,
[make sure your properties are linked](https://support.google.com/analytics/answer/1308621),
and then navigate to the new section "Search Console", which should appear under the "Acquisition"
menu item in Google Analytics.
