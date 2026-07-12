---
title: "What’s new at Ahrefs? (Nov 2022)"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "high"
slug: "whats-new-at-ahrefs-nov-2022"
url: "https://ahrefs.com/blog/whats-new-at-ahrefs-nov-2022/"
canonical: "https://ahrefs.com/blog/whats-new-at-ahrefs-nov-2022/"
author: "Rebekah Bek"
published: "2022-12-14T11:37:41+00:00"
updated: "2023-02-09T04:44:20+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2023_aging"
  - "product_or_tool_content"
  - "title_year_2022_before_2026"
fetched_at: "2026-06-12T12:18:50+00:00"
status_code: 200
html_hash: "fc3188e22a0a2bb63122a9ade541cac3763fc7e14e21071b7327029dff1e9283"
clean_word_count: 854
clean_char_count: 5246
---
# What’s new at Ahrefs? (Nov 2022)

This month we’re introducing the new Organic competitors report, new video SERP features filters, HTML code comparison in Site Audit, and more.

Let’s get right into it.

## 1. Site Explorer

#### **Organic competitors report (beta)**

This report shows you who your organic competitors are and how everyone matches up against each other based on organic traffic, organic traffic value, and number of organic pages.

Look at the competitive map for a visual competitor gap analysis. The bigger the size of the circle, the more pages a competitor has. In “Compare mode”, previous values are displayed as dotted circles.

![Organic competitors report – Visual analysis](https://ahrefs.com/blog/wp-content/uploads/2022/12/Organic_competitors__iherb_com_.jpg)

Then scroll down to the data table below, which shows you competitive metrics.

Look at the Competitor’s keywords column to see the keywords you’re not ranking for and find missed keyword opportunities. Or, open the nested Pages table to get an idea of pages worth creating to build topical authority.

Use the date pickers to compare changes between specific dates.

This report replaces our Competing domains and Competing pages reports. While the report is in beta, we’re working on fine-tuning the UI and improving data and filtering.

#### **Broken backlinks report**

This report shows all backlinks pointing to broken pages on your target.

We’ve added new filters to give you more flexibility over the data. For example, you can apply the filter – Target page URL **doesn’t contain** /blog –  to see all broken backlinks pointing to pages on our site except for our blog.

This report is available for Standard plan users and higher.

## 2. Keywords Explorer

#### **SERP comparison and SERP similarity score**

Last month, we introduced the SERP comparison feature in Site Explorer. It’s now been added to Keywords Explorer as well, and upgraded with a new SERP similarity score.

Just scroll down to the SERP overview to compare two SERPs side by side. You can compare a keyword by date…

…or compare SERPs for two entirely different keywords.

We’ve also introduced a new SERP similarity score that shows you how similar two SERPs are on a 100-point scale. A higher value shows more similarity. This score takes into account both the number of results in common and their relative positions.

For example, let’s say I’m comparing the keywords “how to start a blog” versus “how to blog”.

Without looking at the SERPs, my guess would be that “how to blog” would be about writing blog posts. But it has a similarity score of 70% with “how to start a blog”, where all posts are about how to actually create a blog.

Since both intent and the search results for these two keywords are pretty much the same, you probably wouldn’t need to create separate blog posts on both.

## 3. Cross-tool updates

#### **Video SERP features filters**

We’ve added two new video SERP features filters in Site Explorer, Keywords Explorer, and Rank Tracker.

Selecting “Video preview” lets you filter for videos that show up in SERPs as search results that look like this:

…while selecting “Videos” lets you find blocks of multiple videos that show up in SERPs that look like this:

## 4. Site Audit

#### **HTML code and text comparison**

Easily spot technical issues by comparing raw and rendered HTML code between Site Audit crawls.

Go to any crawl in Site Audit and click on HTML source in URL details. Then select HTML or text and hit “Compare with” to see all changes highlighted.

You can also track changes in the content extracted from the page and see when certain keywords have been added or removed.

## 5. General

#### **Updates for Site Explorer connector for GDS**

You can now add URL rating, the UR history chart, and the Keywords by top position chart to your reports in Google Data Studio. We’ve also added history grouping, which can be applied to any historical chart.

Find the [Site Explorer report template here](https://datastudio.google.com/u/0/reporting/54258fc6-9ef0-4718-98df-1a4c4aa87ece/page/p_1bfyh3p8oc).

#### **UR and Keywords Explorer metrics in API v3**

We’ve added two endpoints to Site Explorer:

- [URL rating](https://docs.ahrefs.com/docs/api/site-explorer/operations/list-all-backlinks) to the backlinks endpoint, so backlinks data now includes the referring page’s UR;
- [UR history](https://docs.ahrefs.com/docs/api/site-explorer/operations/get-a-url-rating-history) to pull the corresponding SE Overview chart.

And three endpoints to Keywords Explorer:

- [Keyword metrics](https://docs.ahrefs.com/docs/api/keywords-explorer/operations/get-a-overview) for a single keyword or a list of keywords
- [Volume history](https://docs.ahrefs.com/docs/api/keywords-explorer/operations/get-a-volume-history) for a single keyword
- [Volume by country](https://docs.ahrefs.com/docs/api/keywords-explorer/operations/get-a-volume-by-country) for a single keyword.

For convenience, look for the API button in SE Overview, SE Backlinks, or KE Overview to copy an API query and pull the report with all current filters applied.

API v3 is currently available for Enterprise customers only.

—

That’s all for this month. Enjoy!
