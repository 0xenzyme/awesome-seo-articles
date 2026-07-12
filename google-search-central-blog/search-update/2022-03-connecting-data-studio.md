---
title: "Connecting Search Console to Data Studio"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2022-03-connecting-data-studio"
url: "https://developers.google.com/search/blog/2022/03/connecting-data-studio"
canonical: "https://developers.google.com/search/blog/2022/03/connecting-data-studio"
author: "Daniel Waisberg"
published: "2022-03-08T00:00:00+00:00"
updated: "2022-03-08T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:40:09+00:00"
status_code: 200
html_hash: "4d1c59579e99a72e8aa29858aa3a83c1c1d8194e824b5bd7e23089e91857ad19"
clean_word_count: 808
clean_char_count: 5199
---
# Connecting Search Console to Data Studio

[Google Search Console](https://goo.gle/searchconsole) gives you insight into your website performance in Google Search,
but understanding your data can be a challenge. If you set up a custom dashboard with data visualizations that work for **you**, it might help you
make better decisions that are supported by data. This post is the first in a series of posts that will focus on exporting, enhancing, and visualizing
Search Console data using [Google Data Studio](https://support.google.com/datastudio/answer/6283323).

In today’s post, we’ll discuss how to bring your Search Console data into Google Data Studio. We’ll show an example where we download Search Console data
into Google Sheets, enhance the data with geographical regions, and connect the spreadsheet to Data Studio.

In future posts, we’ll discuss how to create data visualizations to help you monitor and analyze your data.

## Prepare the data and connect to Data Studio

In order to import Search Console data into Data Studio, there are two roads you can take:

- If you are happy to see the same data as you see in Search Console, you should use the Google Data Studio data connector. This option is straightforward:
  visit the [connector gallery](https://datastudio.google.com/data), choose Search Console, and find the property you’d like to connect.
  You can find a guide to the connector in the [Data Studio Help Center](https://support.google.com/datastudio/answer/7314895).
- If you’d like to enhance the data provided by Search Console (for example, clustering countries into regions), you should first export the data from the web
  interface or through the API. Then, you can manipulate the data with Google Sheets or BigQuery and connect it to Data Studio.

In this post we’ll discuss the second option, since it requires more steps and offers more customization opportunities. There are three main steps you need to take:

1. Export Search Console data.
2. Add your own data on top of it.
3. Import it into Data Studio.

### Export Search Console data

In order to export your data, visit the Search Console [Performance report](https://search.google.com/search-console/performance/search-analytics),
choose a date range, click **Export**, and choose Google Sheets. This will create a new spreadsheet, which we’ll enhance in the next step. You can also use
the [Search Analytics API](/webmaster-tools/v1/searchanalytics/query) for a more automated solution, but that's
out of scope for this post.

![Search Console Performance report export options](/static/search/blog/images/search-console-data-export.png "Search Console Performance report export options")

You can read more about the dimensions and metrics that will be available to you in the [Performance
report help documentation](https://support.google.com/webmasters/answer/7576553#dimensions).

### Enhance Search Console data

To show how to enhance your Search Console data, we’ll use a neat Google Sheets function, [IMPORTDATA](https://support.google.com/docs/answer/3093335),
which can import data from a URL. In our example, we’re importing the
[ISO 3166 countries by region](https://gist.githubusercontent.com/richjenks/15b75f1960bc3321e295/raw/62749882ed0e9dffa3edd7a9a44a7be59df8402c/countries.md) table.

Add a new sheet to the data you exported from Search Console and enter the following code to the first cell:

```
=IMPORTDATA("https://gist.githubusercontent.com/richjenks/15b75f1960bc3321e295/raw/62749882ed0e9dffa3edd7a9a44a7be59df8402c/countries.md", "|")
```

In the Search Console sheet, create a column for **Region** and use the `VLOOKUP`
function to match the regions to the countries.

Here is a [sample sheet](https://docs.google.com/spreadsheets/d/1WoyovWWCLq9uaYfnsICL4uMQMApaoNhjMf8U4nl0ZHQ/) showing how the final table would look.

*Embedded: Table showing Search Console data enhanced with country regions*

Even though we’re using an example to enhance the geographical data, you can use the same process to add any type of information. For example, if you have a query classification,
you could use that to group queries into categories.

### Connect Google Sheets to Data Studio

Finally, connect your Google Sheets to Data Studio. To do this, visit the [connector gallery](https://datastudio.google.com/data),
choose Google Sheets, and find your newly created spreadsheet; but make sure to choose the right sheet.

Once the data is in Data Studio, the visualization work begins...

## Next

In the next post in this series, [Monitoring Search traffic (and more!) with Data Studio](/search/blog/2022/03/monitoring-dashboard), we’ll discuss different types of dashboards and provide step-by-step examples for you to follow along.

As always, let us know if you have any questions through the [Google
Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)) or the [Data Studio Community](https://support.google.com/datastudio/threads?thread_filter=(category:connect_to_data)).
Also, if you’re on Twitter, make sure to [follow us](https://twitter.com/googlesearchc); we’ll announce future posts over there - *stay tuned!*
