---
title: "Monitoring Search traffic (and more!) with Data Studio"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2022-03-monitoring-dashboard"
url: "https://developers.google.com/search/blog/2022/03/monitoring-dashboard"
canonical: "https://developers.google.com/search/blog/2022/03/monitoring-dashboard"
author: "Daniel Waisberg"
published: "2022-03-30T00:00:00+00:00"
updated: "2022-03-30T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:40:13+00:00"
status_code: 200
html_hash: "dff8b53ba7d6000a214460c59d0372144c1a21d563bbbf623e0da4f42d9d5c73"
clean_word_count: 1314
clean_char_count: 8331
---
# Monitoring Search traffic (and more!) with Data Studio

This article shows how to create a monitoring dashboard for your Search traffic on Data Studio. While Search Console provides
out-of-the-box charts and filtering capabilities, Data Studio allows you to customize your own charts and view them side
by side with other data, such as Google Ads, Analytics, YouTube, BigQuery, and others. If you missed our previous article
in this series, check it out at [Connecting Search Console to Data Studio](/search/blog/2022/03/connecting-data-studio).

Before we dive into dashboarding, we have some good news for Data Studio users: *as of today, the Search Console connector includes
data for Discover and Google News traffic, similar to the data [recently
added](/search/blog/2021/10/search-analytics-discover-gnews) to the API*.

In today's post, we're sharing a dashboard for you to use with your own data; it makes it easy to toggle between different Search Console properties,
data types, devices, and more. You can link your own data to
[this template](https://datastudio.google.com/reporting/7300a2df-97a2-408a-b10c-43acd2270fe6/page/6zXD/preview) to monitor
your site's Google Search traffic.

Keep reading to learn more about the dashboard.

## How and why you should use a dashboard

When you build a dashboard, you should always start by defining its purpose,
and the majority of cases can be classified as one of three options:

- **Monitoring performance**. Quickly discover a change in the data, for example monitoring URL clicks and click-through rate (CTR)
  for important pages on your site.
- **Data exploration**. Uncover insights from data, for example analyzing search performance patterns across different countries,
  devices, or website sections.
- **Informing the world**. Publishing interesting trends and patterns, for example sharing aggregate data segmented by industry.

Today we'll discuss a monitoring performance dashboard, which should help you find out issues as they happen. Usually, this kind
of dashboard uses simple visualizations such as line or bar charts, and tables — those are quick to interpret. Then, if an issue
is discovered, the SEO or analyst can proceed to a deeper data exploration (this will be covered in the next post).

## Search traffic monitoring dashboard

As mentioned, this post provides
[a template](https://datastudio.google.com/reporting/7300a2df-97a2-408a-b10c-43acd2270fe6/page/6zXD/preview)
to monitor Google Search performance. In this section, we discuss how to get your Search data into Data Studio, what functionality
and data the dashboard provides, and why we made some of the design decisions.

### Set up a Search Console connector

Sign in to [Data Studio](https://datastudio.google.com/), create a
[Search Console data source](https://support.google.com/datastudio/answer/7314895), and choose the
**URL Impression** table, which includes data for web, image, video, news, discover, and googleNews on a URL level basis.
The **Property Parameter** you choose here will be the default one in your report, but you'll have access to the others
through a filter, more about it later in the post. To learn more about the data visit the
[Performance report help pages](https://support.google.com/webmasters/topic/9384513).

![Creating a Search Console data connector](/static/search/blog/images/search-console-data-studio.png "Creating a Search Console data connector")

### Control the data using filters and dates

The header of the report includes several options for you to filter the data in the charts:

1. Use the [data control](https://support.google.com/datastudio/answer/7415591) to change between
   the Search Console properties you have access to.
2. Choose the date range you'd like to see in the report. By default you'll see the last 28 days compared to the previous 28 days.
3. Create filters to drill down on your data:
   - **Page**. Use this to include or exclude one or more pages from your website. Tip: you can
     [use regular expressions](/search/blog/2021/06/regex-negative-match) similar to the way you use it in Search Console.
   - **Type**. Use this to choose among the different data types (including Discover and Google News). You can only choose one at a time.
   - **Country**. Use this to include or exclude one or more countries.
   - **Device**. Use this to choose one or more device categories.

![Options available to control the data in the dashboard](/static/search/blog/images/search-console-dashboard-filters.png "Options available to control the data in the dashboard")

### Monitor clicks and CTR over time

A line chart is the most effective visualization to show how metrics change over time. In this case, we chose to look at both
Clicks and Site CTR. In the line chart image, weekends and weekdays have very different patterns (one of the reasons it's
important to always use a multiple of 7 in your line charts date range) — *keep your eyes on days that break that pattern!*

Note that this image is for a website that is work oriented, hence the traffic is high on weekdays and low on weekends.
It might look very different for your site.

![Line charts showing clicks and CTR trends over time](/static/search/blog/images/search-console-line-chart.png "Line charts showing clicks and CTR trends over time")

We have not included Google Analytics data in this report, but it might be interesting to include a chart showing how many conversions the
website got from organic Google Search. Learn how to [connect
Google Analytics](https://support.google.com/datastudio/answer/6370352) to Data Studio; this would help closing the loop.

### Drill down into specific URLs (or website sections)

When you analyze trends and patterns, charts will be more helpful to you, but if you want to go deeper, it's more effective to analyze particular
URLs (or groups of them) using a table. For example:

- Use the page filter to include only specific sections of your website.
- Use the country filter to check how different pages perform in countries you care about.
- Use the type filter to analyze URL-level performance for each of the data types.

![Table showing URL drill down](/static/search/blog/images/search-console-drill-down.png "Table showing URL drill down")

## Bonus tips

### Tip #1: Make your dashboard mobile-friendly

Most dashboards don't need to be mobile friendly as people use them on their computer. But a monitoring dashboard can be often
used while commuting to work, so it might be important for it to be mobile-friendly.

In order to create a good mobile experience for a monitoring dashboard, set "Display mode" to "Fit to width" (found under
[report and page layout](https://support.google.com/datastudio/answer/7355651)) — this will adjust the
dashboard width to the screen size. If you choose this option, make sure to check how the report looks on different screen sizes.

### Tip #2: Shorten URL strings

If your report includes a single domain with no subdomains, you might consider removing the domain name from your report
to make the tables less cluttered. For example, if you're building a report for `example.com/cool-dashboards/search`,
you'd see only `/cool-dashboards/search`. To do so, you can create a
[calculated field](https://support.google.com/datastudio/answer/6299685) to remove the domain name
from the URL using a regular expression. For example, for a `.com` domain name you
could use the following expression:

```
REGEXP_EXTRACT(Landing Page, ".*\\.com/(.*)$")
```

## Next: An advanced chart for optimizing your Search efforts

In the next post, [Optimizing website performance with a Search Console bubble chart](/search/blog/2022/04/performance-optimization-bubble-chart), we'll discuss an advanced chart that may help you understand where to focus your attention when it comes to
optimizing your Search efforts.

As always, let us know if you have any questions through the [Google
Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)) or the [Data
Studio Community](https://support.google.com/datastudio/threads?thread_filter=(category:connect_to_data)). Also, if you're on Twitter, make sure to [follow us](https://twitter.com/googlesearchc);
we'll announce future posts over there.

*Happy dashboarding!*
