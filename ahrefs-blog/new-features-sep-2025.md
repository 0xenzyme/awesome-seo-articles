---
title: "Entities & Topics in Brand Radar, Ahrefs Connect, and more (September 2025)"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "medium"
slug: "new-features-sep-2025"
url: "https://ahrefs.com/blog/new-features-sep-2025/"
canonical: "https://ahrefs.com/blog/new-features-sep-2025/"
author: "Rebekah Bek"
published: "2025-10-14T00:55:46+00:00"
updated: "2025-10-14T00:57:18+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "product_or_tool_content"
  - "title_year_2025_before_2026"
fetched_at: "2026-06-12T11:52:58+00:00"
status_code: 200
html_hash: "8a129eadc1334712fcd3d7b238e8ac492806e92462ac2e1707728049490bee2a"
clean_word_count: 954
clean_char_count: 5924
---
# Entities & Topics in Brand Radar, Ahrefs Connect, and more (September 2025)

We’ve got 18 updates this month – from big improvements in tracking your brand in AI, to the launch of Ahrefs Connect for integrations.

Let’s dive in.

## Brand Radar

**Entities**
 You can now group multiple variations of a brand or competitor name into one entity. Any response that matches a term in the group gets counted. That means no more chasing every typo, spelling, or alternate phrasing – just a cleaner, consolidated view of your brand footprint.

![](https://ahrefs.com/blog/wp-content/uploads/2025/10/image8.png)

**Saved reports**
 Reports for your brand, competitors, and market can now be saved directly in Brand Radar. Access control is built in: keep them private, or share them with your team.

**Topics**
 Brand Radar now has a Topics report and Overview widget. Queries are grouped by parent topics from Keywords Explorer, helping you:

- Uncover new angles where your brand is (or isn’t) visible in AI
- Prioritize which queries to optimize for first
- Slice results with the new filter to focus where it matters most

**Filter builder**
 Think of this as the new Market Scope filter from v1. It lets you exclude responses from Overview charts, giving you more control over what’s shown and how you analyze coverage.

**Cited Domains & Pages improvements**
 Both reports now have their own dedicated filters so you can refine by domain names and page URLs directly, instead of just removing responses. Plus, the Cited Domains report has a new column showing the total number of cited pages per domain, making it easier to spot where coverage is concentrated.

**Export upgrades**
 Sharing data is easier too:

- Export directly to Google Sheets
- Download any Brand Radar chart as a CSV

**Brand Radar API**
 The first endpoint is live: AI responses. It includes the same columns and filters you’re used to in-app, now accessible via API. Handy for dashboards, pipelines, and custom reporting.

 [Read API docs →](https://docs.ahrefs.com/docs/api/brand-radar/operations)

**AWT access**
 The Brand Radar add-on is now available to Ahrefs Webmaster Tools users, even without a paid subscription. You’ll need an AWT account to get started. (Note: Search Demand and Web Visibility indexes are excluded for free users.)

## Report Builder

Add Brand Radar 2.0 Mentions charts for all platforms into your custom reports. Perfect for slipping AI visibility data into your monthly SEO reports for clients or stakeholders.

## Web Analytics

**Funnels comparison**
 Compare funnels across dates using the date picker. Exports in comparison mode include both current and previous periods. You can also export tracked events directly, which makes it easier to analyze them outside Ahrefs.

**Possible 404 report**
 Flags pages that get visits but contain “404” or “not found” in the title. This often happens when AI chatbots hallucinate URLs – now you can catch and fix them before they cause issues.

## Site Explorer

**SERP features history**
 A new chart in Overview shows the number of positions your site holds in SERP features over time. Like in Rank Tracker, you’ll see:

- Owned features – where your pages actually rank
- Total features – out of 19 possible types

The chart is interactive too: click on features, drag across a time period, and it’ll open Organic Keywords with the right filters already applied.

**404 not found in Outgoing Links**
 There’s a new status code filter in the Outgoing Links report that lets you find broken outgoing links directly. This fully replaces the old Broken Links report, which has been removed.

## Keywords Explorer

**Competitors map**
 Traffic Share reports now include a competitors map – a visual way to see who’s winning your keywords by traffic and traffic value. Bubble size shows coverage: pages for domains, and ranking keywords for pages.

**Historical traffic share**
 Also in Traffic Share reports, a new trend chart shows how traffic distribution has shifted over time. Click any point on the chart to zoom in, then pick pages to plot directly and track competitive changes in detail.

**Exclude keywords filter**
 You can now exclude keywords that are already in a list or project from keyword ideas reports. This helps keep results focused on fresh opportunities instead of cluttered with duplicates.

## Rank Tracker

**User notes**
 User notes in Rank Tracker and GSC charts are now shared across the entire workspace. If a project is shared, everyone in it can see the notes. Members with editing rights can edit any note, while guests can only view. Notes can’t be made private.

## Batch Analysis

Batch Analysis 2.0 is now the default. It’s faster, more powerful, and supports up to 1,000 URLs (vs 200 before). You’ll see:

- Backlink counts
- Referring domains
- Outlink data

The tool also gives more accurate link counts than the old version. We’ve added these new fields to the batch-analysis API v3 endpoint.

[Read API docs →](https://docs.ahrefs.com/docs/api/batch-analysis/operations)

## Ahrefs Connect

**Launch of Ahrefs Connect**
 Big news: we’ve launched Ahrefs Connect, our new system for third-party integrations built on API v3. Ahrefs Connect lets your favorite tools plug into your Ahrefs account with OAuth, so they can pull data like:

- Competitive intelligence
- Site Audit reports
- Organic search and backlinks data

We’ve also added extra API units to Lite, Standard, and Advanced plans to support Ahrefs Connect. Direct API v3 access and new app activations remain Enterprise-only.

 [Read docs for details →](https://docs.ahrefs.com/docs/connect/overview)

⚠️ Reminder: API v2 and all legacy integrations stop working on November 1, 2025.

–

That’s all for this month. Check out our [changelog](https://ahrefs.com/changelog) for more updates, or leave any feature requests on our [Canny board](https://ahrefs.canny.io/). Enjoy!
