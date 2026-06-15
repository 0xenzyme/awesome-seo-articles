---
title: "Announcing the new Search Console Video index report"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2022-07-video-indexing-report"
url: "https://developers.google.com/search/blog/2022/07/video-indexing-report"
canonical: "https://developers.google.com/search/blog/2022/07/video-indexing-report"
author: "Danielle Marshak, Moshe Samet"
published: "2022-07-11T00:00:00+00:00"
updated: "2022-07-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:40:44+00:00"
status_code: 200
html_hash: "e37dcabd6fb8294e2d7f1d8ffd81b2436687930d40e7aecd7fcf25a862c8eae3"
clean_word_count: 527
clean_char_count: 3231
---
# Announcing the new Search Console Video index report

Video creation and consumption on the web continues to grow, and Google Search indexes videos from millions of different sites,
so people can easily discover and watch this content. To help you understand the performance of your videos on Google, and
identify possible areas of improvement, Search Console is launching a new report called
[Video indexing](https://support.google.com/webmasters/answer/9495631).
We will roll out this change gradually over the next few months, so you might not see any changes for now.

## Video Indexing Report

If Google detects videos on your site, the Video indexing report will appear on the left navigation
bar in the coverage section. If Google has not detected a video on your website, you will not see
the report.

The report shows the status of video indexing on your site. It helps you answer the following questions:

- In how many pages has Google identified a video?
- Which videos were indexed successfully?
- What are the issues preventing videos from being indexed?

In addition, if you fix an existing issue, you can use the report to validate the fix and track how
your fixed video pages are updated in the Google index.

![The new Video indexing report on Search Console](/static/search/blog/images/video-indexing-report.png "The new Video indexing report on Search Console")

Please note that this report is different from the Video [Rich results report](https://support.google.com/webmasters/answer/7552505).
The report discussed in today’s post is about video indexing, regardless of any video structured
data, and therefore it does not show the validity of [Video structured data](/search/docs/appearance/structured-data/video)
items. The Video Rich results report is unchanged and continues to show which Video structured data
items are valid or invalid on your site.

## Inspecting a specific video page

In addition to the new report, we also enhanced the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289)
to allow you to check the video indexing status of a specific page. When inspecting a page, if Google
detected a video in it, you will see the following in the results:

- Details such as the video URL and the thumbnail URL.
- The page status showing whether the video was indexed or not.
- List of issues preventing the video from being indexed.

This does not apply to live inspection, which does not show video indexing status and will only indicate
if a video was detected on the page being inspected.

![The new Video page indexing section in the URL inspection tool](/static/search/blog/images/video-url-inspection.png "The new Video page indexing section in the URL inspection tool")

We hope the new tools will make it easier to understand how your videos perform on Search and to identify
and fix issues. To learn more about video indexing best practices, check out the
[video best practices guide](/search/docs/appearance/video).

If you have any questions or concerns, please reach out to us via the [Google Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console))
or on [Twitter](https://twitter.com/googlesearchc).
