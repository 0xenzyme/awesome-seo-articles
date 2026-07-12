---
title: "Grok in Brand Radar, higher API limits, and more (April 2026)"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "low"
slug: "new-features-apr-2026"
url: "https://ahrefs.com/blog/new-features-apr-2026/"
canonical: "https://ahrefs.com/blog/new-features-apr-2026/"
author: "Andrei Țiț"
published: "2026-05-25T15:45:18+00:00"
updated: "2026-06-05T22:00:47+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "product_or_tool_content"
fetched_at: "2026-06-12T11:51:56+00:00"
status_code: 200
html_hash: "b3525636752bc6ea09ae497fd2c89cd3a7ed5710e04aed05d8f6a8eaa793f47f"
clean_word_count: 781
clean_char_count: 4919
---
# Grok in Brand Radar, higher API limits, and more (April 2026)

We’ve got 8 updates this month covering Brand Radar, Site Explorer, Keywords Explorer, GSC Insights, Social Media Manager, and the API.

Let’s dive in.

## Brand Radar

### Grok

Grok is now available in Brand Radar for both Ahrefs prompts and custom prompts. It’s included in the All Indexes add-on, or available separately at $199 per month. For custom queries, you don’t need an add-on, just monthly checks.

![Grok in Ahrefs Brand Radar](https://ahrefs.com/blog/wp-content/uploads/2026/05/1.jpg)

### Cited pages report: new columns and tabs

Cited domains is no longer a separate report. It’s now an **All domains** tab sitting alongside Yours, Competitors, and Other. URL filters have moved from the table header into a filter bar below the tabs.

The biggest structural change comes from the citation funnel: **Cited in** shows the total responses where the domain was cited, and **Found in** shows the total responses where the page was found, cited or not.

We also show **Found but not cited** brand mentions so you can be aware of and fill AI citation gaps.

### Citations chart: Found in and Position modes

The chart now has two modes:

**(1) Found in** plots two lines per page: solid for total responses where the page was found, dashed for responses where it was cited.

**(2) Position** plots each page’s average citation position over time, with line thickness reflecting how many citations back the average. This helps monitor how AI citations change over time, instead of comparing snapshots side by side.

## Site Explorer

### Organic positions report

The new report shows every ranking URL for your organic keywords. It’s similar to Positions in Calendar, but Calendar only shows positions with daily movements, while this report shows all of them.

### Crawled pages report

The new report shows all pages on a site crawled by [Ahrefs bot](https://ahrefs.com/seo/glossary/ahrefsbot), sorted by the most recent crawl attempt. Useful for spotting crawl issues, finding new competitor pages before they rank, and auditing what’s actually being discovered versus ignored.

## Keywords Explorer

### Historical search volume for keyword lists

Keywords Explorer now has a graph showing historical total search volume across multiple keywords or a saved keyword list. Track seasonality or watch demand shift across a niche over time.

## GSC reports

### New filters in the Keywords report

The Keywords report has two new filters:  (1) **word count** works the same way as in other Ahrefs tools. (2) **Rank Tracker status** replaces the old “Not tracked only” filter and lets you view both tracked and non-tracked keywords. Checking GSC metrics for your tracked terms takes one click instead of a workaround.

### GSC Insights in Portfolios

GSC Insights are now visible in Portfolios, so if you manage multiple GSC properties (country-specific sites, different brands, or sections of one domain) you can track their combined performance from a single dashboard.

## Social Media Manager

### Overview report redesign

The Overview report is now a full snapshot of your social media health:

1. **Quick stats** at the top: Posts Published, New Followers, Total Engagement, and Average Engagement Rate, each with period-over-period deltas and date range filtering
2. **Connected channels**: follower counts, growth deltas, and connection and token status per channel
3. **Upcoming posts**: your next 5 scheduled posts, inline
4. **Top posts by views**: shows which content is getting the most attention

## API

### Higher limits across all self-serve plans

By popular request, API units and rows-per-request are going up across every self-serve plan:

### Brand Radar API: entity support

Brand Radar API endpoints now support **entities**, both brand variations and brand websites, matching what’s already available in the UI.

To handle the more complex input, POST versions of the existing GET endpoints are available, accepting input as a JSON object in the request body instead of URL parameters.

### Brand Radar API: report management endpoints

New endpoints let you manage Brand Radar reports end to end: a GET to list existing reports with metadata, a POST to create a new report and configure its tracking platforms and schedule, and a PATCH to update tracking settings on existing reports.

[Read API docs →](https://docs.ahrefs.com/en/api/reference/management)

### Looker connector for Brand Radar

A new **Looker connector for Brand Radar** is live, providing history charts for AI mentions, impressions, and AI Share of Voice, plus distributions of those metrics across brands and platforms.

---

That’s all for this month. Check out our [full changelog](https://ahrefs.com/blog/new-features/) for the rest of the smaller updates, or leave any feature requests on our [Canny board](https://ahrefs.canny.io/). Enjoy!
