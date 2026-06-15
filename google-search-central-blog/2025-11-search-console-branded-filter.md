---
title: "Introducing the branded queries filter in Search Console"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "low"
slug: "2025-11-search-console-branded-filter"
url: "https://developers.google.com/search/blog/2025/11/search-console-branded-filter"
canonical: "https://developers.google.com/search/blog/2025/11/search-console-branded-filter"
author: "Michael Huzman, Software Engineer, Search Console"
published: "2025-11-20T00:00:00+00:00"
updated: "2025-11-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:45:47+00:00"
status_code: 200
html_hash: "6607b0cc8eb8e2a866073ba65571022bbcff0c42ecf29575bc93722c6d5b4c23"
clean_word_count: 681
clean_char_count: 4477
---
# Introducing the branded queries filter in Search Console

Following the [Query groups](/search/blog/2025/10/search-console-query-groups) launch
last month, we're happy to announce we're providing an additional tool to analyze the performance
of your website by query type in the [Search Console Performance Report](https://support.google.com/webmasters/answer/7576553):
the branded queries filter. This new feature is designed to help analyze the queries driving traffic
to your site by automatically differentiating between branded and non-branded queries.

## What is a branded query?

A branded query is a query that includes your brand name (for example, Google), variations or
misspellings of the brand name (for example, Gogle), and brand-related products or services:
(for example, Gmail).

Differentiating between traffic from people who are already familiar with your brand and people who
aren't is not always straightforward. Focusing on branded queries and non-branded queries separately
can help you better understand traffic patterns. Branded queries typically lead to higher-ranking pages
from your site and result in higher click-through rates, whereas non-branded queries offer organic growth,
as they show how new users find your content without any initial intent to go to your site.

## How does the branded queries filter work?

The new filter is accessible within the [Search results Performance report](https://support.google.com/webmasters/answer/7576553)
and lets you segment your query data into two distinct views:

1. **Branded:** Shows performance data for queries that include your brand name
   or closely associated products (for example, Gmail for google.com).
2. **Non-branded:** Shows performance data for all other queries.

You can apply this filter across all search types (web, image, video, and news) in the search
results performance report. When applied, you will be able to see metrics—such as impressions,
clicks, average position, and CTR—limited specifically to the selected group.

![Search Console branded queries filter](/static/search/blog/images/search-console-branded-queries-filter.png)

Additionally, we have added a new card to the [Insights report](https://support.google.com/webmasters/answer/16308503)
that shows the breakdown of total clicks for branded versus non-branded traffic, helping you measure
brand recognition and compare the volume of traffic from people already familiar with your brand to
the volume of traffic from those who didn't explicitly intend to visit your site.

![Search Console Insights branded traffic card](/static/search/blog/images/insights-branded-traffic-card.png)

## How are branded queries identified?

The classification of branded versus non-branded is **NOT** based on a regular expression
method of including or excluding keywords, which is already available in the "Filter by query"
section. It is determined by an internal, AI-assisted system. It includes your website brand name
in all languages, typos, and also queries that don't include the brand name but refer to a unique
product or service of the site.

Due to the dynamic and contextual nature of brand classification, some queries may occasionally be
misidentified. This filter is designed to make it easier for you to segment and analyze your data
within Search Console; it has no effect on how Google Search ranking works.

## Rollout and availability

The branded queries filter will be **rolling out gradually over the coming weeks**.
If you cannot see this option in your reports, it might be due to one of the following reasons:

- This is only available for top level properties (and not for URL path properties such as
  `https://example.com/path` or subdomain properties such as `developers.google.com`).
- This is only available for sites with a sufficient volume of queries and impressions for our
  signals.

We encourage you to dive into the Performance report, explore this new segmentation, and gain a
clearer view on your site's performance. Since this is a new kind of analysis in Search Console,
your feedback is extremely welcome. You can provide feedback through the thumbs up and thumbs down
available in the cards and, if needed, using the Submit feedback link. You can share your comments
on [LinkedIn](https://www.linkedin.com/showcase/googlesearchcentral/)
or post in the [Google Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)).
