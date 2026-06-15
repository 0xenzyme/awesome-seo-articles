---
title: "Bulk data export: a new and powerful way to access your Search Console data"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2023-02-bulk-data-export"
url: "https://developers.google.com/search/blog/2023/02/bulk-data-export"
canonical: "https://developers.google.com/search/blog/2023/02/bulk-data-export"
author: "Daniel Waisberg"
published: "2023-02-21T00:00:00+00:00"
updated: "2023-02-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:41:29+00:00"
status_code: 200
html_hash: "1e8f5232fe2854e87725453dfa036d5aabf21d154a5b60ded630bc0a3c129015"
clean_word_count: 832
clean_char_count: 5323
---
# Bulk data export: a new and powerful way to access your Search Console data

Today, we're announcing [bulk
data export](https://support.google.com/webmasters/answer/12918484), a new feature that allows you to export data from Search Console to
[Google BigQuery](https://cloud.google.com/bigquery) on an ongoing basis.
(*Note that the rollout will take approximately one week, so you may not have access right away.*)

You can configure an export in Search Console to get a daily data dump into your BigQuery project.
The data includes all your performance data, apart from anonymized queries, which are filtered out
for privacy reasons; in other words, the bulk data export is not affected by the
[daily data row limit](/search/blog/2022/10/performance-data-deep-dive#daily-data-row-limit).
This means you can explore your data to its maximum potential, joining it with other sources of data
and using advanced analysis and visualization techniques.

This data export could be particularly helpful for large websites with tens of thousands of pages, or those receiving
traffic from tens of thousands of queries a day (or both!). Small and medium sites already have access to all their
data through the user interface, the [Looker Studio connector](/search/blog/2022/03/monitoring-dashboard)
(formerly known as Data Studio) or the [Search Analytics API](https://developers.google.com/webmaster-tools/v1/searchanalytics/query).

## Setting up a new bulk data export

To configure a new report, you'll need to prepare your BigQuery account to receive the data and set up
your details in the Search Console settings. Check the Help Center for a
[step-by-step guide](https://support.google.com/webmasters/answer/12917675),
but in general, the process is divided into two stages:

1. **Prepare your Cloud project** ([inside Google Cloud Console](https://console.cloud.google.com/)):
   this includes enabling the BigQuery API for your project and giving permission to your Search Console service account.
2. **Set export destination** ([inside Search Console](https://search.google.com/search-console/settings/bulk-data-export)):
   this includes providing your Google Cloud project ID, and choosing a dataset location. Note that only property owners can set up a bulk data export.

![Search Console bulk data export settings page](/static/search/blog/images/search-console-bulk-data-export.png)

Once you submit the information to Search Console, it'll simulate an export. If the export succeeds, we'll inform all property owners via email and your
ongoing exports will start within 48 hours. If the export simulation fails, you'll receive an immediate alert on the issue detected; here's a list of
[possible export errors](https://support.google.com/webmasters/answer/12919198).

## Data available on bulk data exports

Once the bulk data export is set up successfully, you can log in to your BigQuery account and start querying the data.

You can find detailed [table guidelines and references](https://support.google.com/webmasters/answer/12917991) in the help center;
also check the explanation on the difference between [aggregating
data by property vs by page](https://support.google.com/webmasters/answer/7576553#urlorsite), as it'll help you understand the data better. Here is a quick description of the three tables that will be available to you:

- `searchdata_site_impression`: This table contains data aggregated by property, including query, country, type, and device.
- `searchdata_url_impression`: This table contains data aggregated by URL, which enables a more detailed view of queries and rich results.
- `ExportLog`: This table is a record of what data was saved for that day. Failed exports are not recorded here.

![Bulk data export table shown in the BigQuery interface](/static/search/blog/images/bulk-data-export-bigquery-table.png)

If you need a little help to start querying the data, check the [sample queries](https://support.google.com/webmasters/answer/12917174)
published in the help center, they can be handy to get up and running. Here's one example, where we pull the total query by URL combinations for pages with at least
100 FAQ rich result impressions over the last two weeks.

```
SELECT
  url,
  query,
  sum(impressions) AS impressions,
  sum(clicks) AS clicks,
  sum(clicks) / sum(impressions) AS ctr,
  /* Added one below, because position is zero-based */
  ((sum(sum_position) / sum(impressions)) + 1.0) AS avg_position
/* Remember to update the table name to your table */
FROM searchconsole.searchdata_url_impression
WHERE search_type = 'WEB'
  AND is_tpf_faq = true
  AND data_date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 14 day) AND CURRENT_DATE()
  AND clicks > 100
GROUP BY 1,2
ORDER BY clicks
LIMIT 1000
```

We hope that by making more Google Search data available, website owners and SEOs will be able to find more content opportunities by analyzing long tail queries.
It'll also make it easier to join page-level information from internal systems to Search results in a more effective and comprehensive way.

And as always, if you have any questions or concerns, please reach out to us via the [Google
Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)) or on [Twitter](https://twitter.com/googlesearchc).
