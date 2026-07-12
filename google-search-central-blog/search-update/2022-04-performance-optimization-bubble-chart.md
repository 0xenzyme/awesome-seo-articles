---
title: "Optimizing website performance with a Search Console bubble chart"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2022-04-performance-optimization-bubble-chart"
url: "https://developers.google.com/search/blog/2022/04/performance-optimization-bubble-chart"
canonical: "https://developers.google.com/search/blog/2022/04/performance-optimization-bubble-chart"
author: "Daniel Waisberg"
published: "2022-04-06T00:00:00+00:00"
updated: "2022-04-06T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:40:24+00:00"
status_code: 200
html_hash: "216ad1fe8b44d176df84b0f8791b7229c19379d1c1480c7bbd184692f35ff0d1"
clean_word_count: 1481
clean_char_count: 9576
---
# Optimizing website performance with a Search Console bubble chart

Analyzing Search performance data is always a challenge, but even more so when you have plenty of long-tail queries,
which are harder to visualize and understand. In this post, we'll provide tips to help you uncover opportunities to
optimize your site's Google Search performance.

If you haven't read our recent posts on [connecting Search Console to Data Studio](/search/blog/2022/03/connecting-data-studio)
and [monitoring Search traffic with Data Studio](/search/blog/2022/03/monitoring-dashboard),
consider checking them out to understand more about what you can do with Search Console in Data Studio.

Today we'll discuss a [bubble chart](https://support.google.com/datastudio/answer/7207785)
that can help you understand which queries are performing well for your site, and which could be improved. We'll first
explain the main elements in the chart, describing specific settings and how they influence the data. Then we'll provide
some pointers on what to look for when analyzing the data.

Starting with the good news: you don't need to build the chart from scratch, you can use
[this template](https://datastudio.google.com/reporting/1e5b5f6a-38d7-4547-a54b-69594681a09b/page/xFbeC/preview), connect to your data,
and tweak any settings you want.

*Without further ado...*

![Data Studio report showing a bubble chart with Search Console data](/static/search/blog/images/search-performance-analysis.png "Data Studio report showing a bubble chart with Search Console data")

## Understanding the chart

A **bubble chart** is a great visualization when you have multiple metrics and dimensions because it enables you to see
relationships and patterns in your data more effectively. In the example shown here, you can see traffic attributes
(click-through rate (CTR), [average position](https://support.google.com/webmasters/answer/7042828#position))
and volume (total [clicks](https://support.google.com/webmasters/answer/7042828#click)) for different dimensions (query, device) at the same time.

We'll go through some of the chart elements to clarify what it shows, and what it doesn't.

### Data source

For this chart, we're using the **Site Impression** table available through the [Search Console data source](https://support.google.com/datastudio/answer/7314895), which includes [Search
performance data](https://support.google.com/webmasters/answer/7576553) aggregated by site and queries.

### Filters and data controls

In order to make it easy for you to control your data effectively, we included five customization options in the chart:

1. **[Data control](https://support.google.com/datastudio/answer/7415591)**: Choose the Search Console
   property you'd like to analyze.
2. **Date range**: Choose the date range you'd like to see in the report; by default you'll see the last 28 days.
3. **Query**: Include or exclude queries to focus on. You can [use regular
   expressions](/search/blog/2021/06/regex-negative-match) similar to the way you use them in Search Console.
4. **Country**: Include or exclude countries.
5. **Device**: Include or exclude device categories.

### Axes

The axes in the chart are **Average position** (y-axis) and **Site CTR** (x-axis), but we made three significant transformations
to make the chart more insightful:

- **Reverse y-axis direction**: Since the y-axis shows average position, inverting it means that 1 is at the top.
  For most business charts, the best position is in the top right corner, so it is more intuitive to invert the y-axis
  when using it to display average position.
- **Log scale**: A [logarithmic scale](https://en.wikipedia.org/wiki/Logarithmic_scale) is
  "a way of displaying numerical data over a very wide range of values in a compact way (...) moving a unit of distance along
  the scale means the number has been multiplied by 10". Using log scale for both axes enables you to have a better understanding
  of queries that are in the extremities of the chart (very low CTR, average position, or both).
- **[Reference lines](https://support.google.com/datastudio/answer/9921462)**: The reference line
  is very helpful to highlight values that are above or below a certain threshold. Looking at the average, median, or a certain
  percentile can call attention to deviations from the pattern.

### Bubbles

Each bubble in the chart represents a single query, and in order to make the chart more useful, we used two
[style properties](https://support.google.com/datastudio/answer/7207785#style-properties):

- **Size**: Using the number of clicks as the bubble size helps you see in a glance which queries are driving the bulk
  of the traffic — the larger the bubble the more traffic the query generates.
- **Color**: Using the device category as the bubble color helps you understand the differences between mobile and desktop
  Search performance. You can use any dimension as the color, but as the number of values increases, the harder it is to
  recognize patterns.

## Analyzing the data

The goal of this visualization is to help surface query optimization opportunities. The chart shows query performance, where
the y-axis represents **average position**, the x-axis represents **CTR**, the bubble size represents total number of
**clicks**, and the bubble color represents **device category**.

The red reference lines show the average for each of the axes, which split the chart into quadrants, showing four types of
query performance. Your quadrants are likely to look different than the one shared in this post; they'll depend on how your
site queries are distributed.

![chart showing four types of query performance](/static/search/blog/images/query-performance-types.png "chart showing four types of query performance")

In general, the chart will show four groups you can analyze to help you decide where to invest your time when optimizing your query performance.

1. **Top position, high CTR**: There's not much you need to do for those; you're doing a great job already.
2. **Low position, high CTR**: Those queries seem relevant to users; they get a high CTR even when ranking lower
   than the average query on your website. They could represent a significant contribution if their position goes up —
   *invest in optimizing them!*
3. **Low position, low CTR**: When looking at queries with low CTR (this and the next bullet), it's especially interesting to look
   at the bubble sizes to understand which queries have a low CTR but are still driving significant traffic. While the queries in this
   quadrant might seem unworthy of your effort, they can be divided into two main groups:
   - *Related queries*: If the query in question is important to you, it's a good start to have it appearing in Search already.
     Prioritize these queries over queries that are not appearing in Search results at all, as they'll be easier to optimize.
   - *Unrelated queries*: If the query is unrelated to your site, maybe it's a good opportunity to fine-tune your content to
     focus on queries that will bring relevant traffic.
4. **Top position, low CTR**: Those queries might have a low CTR for various reasons. You should check
   the largest bubbles to find signs of the following:
   - Your competitors may have structured data markup and are showing up with rich results, which might attract users to click
     their results instead of yours. Consider [enabling Search result
     features for your site](/search/docs/appearance/search-result-features).
   - You may have optimized, or be "accidentally" ranking, for a query that users are not interested in relation to your site.
   - Users may have already found the information they needed, for example your company's opening hours, address, or phone number.

## Optimizing your website performance

Once you find queries that are worth the time and effort, make sure to optimize for them with the help of the
[SEO starter guide](/search/docs/fundamentals/seo-starter-guide). Here are some tips:

- Ensure that your [`title`](/search/docs/appearance/title-link#page-titles) elements,
  [description `meta` tags](/search/docs/appearance/snippet#meta-descriptions), and `alt` attributes are descriptive, specific, and accurate.
- Use heading elements to emphasize important text and help create a hierarchical structure for your content, making it easier
  for users and search engines to navigate through your document.
- Add [structured data markup](/search/docs/appearance/structured-data/intro-structured-data) to describe your content to search engines and be eligible to display your content in useful
  (and eye-catching) ways in search results.
- Think about the words that a user might search for to find a piece of your content. You can use the
  [Keyword Planner](https://ads.google.com/home/tools/keyword-planner/) provided by Google Ads to
  help you discover new keyword variations and see the approximate search volume for each keyword. You can also use
  [Google Trends](https://trends.google.com/trends/) to find ideas from rising topics and queries
  related to your website.

## Feedback

As always, let us know if you have any questions through the [Google
Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)) or the [Data Studio Community](https://support.google.com/datastudio/threads?thread_filter=(category:connect_to_data)).
Also, if you're on Twitter, make sure to [follow us](https://twitter.com/googlesearchc), as we'll announce future posts over there.
