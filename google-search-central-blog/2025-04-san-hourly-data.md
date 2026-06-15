---
title: "The Search Analytics API now supports hourly data"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "2025-04-san-hourly-data"
url: "https://developers.google.com/search/blog/2025/04/san-hourly-data"
canonical: "https://developers.google.com/search/blog/2025/04/san-hourly-data"
author: "Tali Pruss, Daniel Waisberg"
published: "2025-04-09T00:00:00+00:00"
updated: "2025-04-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "news_or_research"
fetched_at: "2026-06-14T13:45:04+00:00"
status_code: 200
html_hash: "3e9670c83fe8d777711cec2018a7247b0928d1bef4b73554fd89e0151f4d106a"
clean_word_count: 482
clean_char_count: 3520
---
# The Search Analytics API now supports hourly data

A few months ago, we announced an improved way to view
[recent performance data in Search Console](/search/blog/2024/12/recent-data-search-console).
The "24 hours" view includes data from the last available 24 hours and appears with a delay of
only a few hours. This view can help you find information about which pages and queries are
performing in this recent timeframe and how content you recently published is picking up.

Today, we're adding support for hourly data to the
[Search Analytics API](/webmaster-tools/v1/searchanalytics/query),
we heard ecosystem requests to make this data more accessible loud and clear. As a result, we're
adding hourly data to the API and with a wider scope than the product interface: while the product
displays hourly data only for the past 24 hours, the API will return data for up to 10 days with
an hourly breakdown. This will allow developers to create solutions to show not only hourly data
for the latest day, but also to compare the most recent day to the same day in the previous week,
which can be useful when analyzing patterns for the days of the week.

## How to pull hourly data from the Search Analytics API

In order to make hourly data available in the Search Analytics API, we're introducing 2 changes to
the [API request body](/webmaster-tools/v1/searchanalytics/query#request-body):

- New `ApiDimension` named `HOUR` for you to group the response by
  hour.
- New `dataState` value named `HOURLY_ALL`, which should be used when
  grouping by HOUR. This will indicate that hourly data might be partial.

In the following section we provide a sample API request and a sample response for reference.

### Sample API request

```
{
  "startDate": "2025-04-07",
  "endDate": "2025-04-07",
  "dataState": "HOURLY_ALL",
  "dimensions": [
    "HOUR"
  ]
}
```

### Sample API response

```
{
  "rows": [
    {
      "keys": [
        "2025-04-07T00:00:00-07:00"
      ],
      "clicks": 17610,
      "impressions": 1571473,
      "ctr": 0.011206046810858348,
      "position": 10.073871456906991
    },
    {
      "keys": [
        "2025-04-07T01:00:00-07:00"
      ],
      "clicks": 18289,
      "impressions": 1662252,
      "ctr": 0.011002543537321658,
      "position": 9.5440029550272758
    },
    {
      "keys": [
        "2025-04-07T02:00:00-07:00"
      ],
      "clicks": 18548,
      "impressions": 1652038,
      "ctr": 0.011227344649457216,
      "position": 9.81503633693656
    },
    {
      "keys": [
        "2025-04-07T03:00:00-07:00"
      ],
      "clicks": 18931,
      "impressions": 1592716,
      "ctr": 0.01188598595104212,
      "position": 9.4956935197486558
    },
    {
      "keys": [
        "2025-04-07T04:00:00-07:00"
      ],
      "clicks": 20519,
      "impressions": 1595636,
      "ctr": 0.012859449147549943,
      "position": 9.4670100198290843
    },
    …
  ],
  "responseAggregationType": "byProperty"
}
```

We hope that this new data will help you better monitor your recently published content in a more
effective way and help you take action in a timely manner. We would love to hear your thoughts on
how this new view works for you and to hear any suggestions on how to make it even better. If you
have any feedback, questions, or comments, you can find us on
[LinkedIn](https://www.linkedin.com/showcase/googlesearchcentral/)
or post in the [Google Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)).
