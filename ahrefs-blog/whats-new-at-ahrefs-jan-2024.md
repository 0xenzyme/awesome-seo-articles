---
title: "What’s new at Ahrefs? (Jan 2024)"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "high"
slug: "whats-new-at-ahrefs-jan-2024"
url: "https://ahrefs.com/blog/whats-new-at-ahrefs-jan-2024/"
canonical: "https://ahrefs.com/blog/whats-new-at-ahrefs-jan-2024/"
author: "Rebekah Bek"
published: "2024-02-07T09:07:19+00:00"
updated: "2024-02-08T02:32:36+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2024_watch"
  - "product_or_tool_content"
  - "title_year_2024_before_2026"
fetched_at: "2026-06-12T12:18:09+00:00"
status_code: 200
html_hash: "550fd6a42e1215cbd96cfc713ab6ca7e4e52ebc664288c6be7575da9874288f9"
clean_word_count: 787
clean_char_count: 4847
---
# What’s new at Ahrefs? (Jan 2024)

This month we’re introducing a new AI feature to identify search intent, the “best links” filter in Overview 2.0, mobile usability issues in Site Audit and more.

Let’s get right into it.

## Site Explorer

**“Best links” filter in Overview 2.0**

The Best links filter is now also in Overview 2.0. Using the filter here affects all backlink-related counts and historical charts, which lets you filter out link noise from all widgets.

For example, here we’re looking at the referring domains graph for a few competing pages on wireless earphones.

![Referring domains graph on Overview 2.0](https://ahrefs.com/blog/wp-content/uploads/2024/01/image10-2.png)

Let’s hit the best links filter and select Show best links only, then Show results.

Applying the filter affects the graph like so. With the filter applied, the top two results have even swapped places towards the end of 2023.

This helps paint an even clearer picture of the performance over time when it comes to so-called “good links”. Remember that you can always input your own custom settings by opening the filter itself and hitting “Configure best links filter”.

**Site structure report available for Lite plan users**

All Lite plan users, both legacy and new, can now access the Site structure report for domain- and subdomain-level metrics.

Site Structure shows you the structure of a website in a tree format, along with metrics for each path level – without having to run a crawl. This helps you understand different sections of a website and how they contribute to its SEO.

**Deprecated legacy reports**

We’ve deprecated a bunch of legacy backlink reports:

- Backlinks
- Broken backlinks
- Referring domains
- New & Lost Anchors
- Internal backlinks
- Best by links
- Best by links’ growth
- Linked domains
- Outgoing anchors

All reports already have a replacement in Site Explorer 2.0.

## Cross-tool update

**Identify search intent with AI**

We’ve added a new AI feature that identifies keyword search intent in the SERP overview widget in Site Explorer, Keywords Explorer and Rank Tracker.

Instead of categorizing search intent into traditional models like informational, navigational or transactional, this classification is more granular – it tells you in simple terms what people searching for a keyword might want to find. This gives you multiple paths or content angles that you can use to rank.

Just look for the “Identify intents” button to get started.

For example, if we identify search intent for the query “best microwave”, we’d see that people searching for this keyword could be looking for product reviews and recommendations of the best-performing microwave ovens, or information on the most reliable microwave brands.

**New SERP feature: Discussions and forums**

Our SERP overview widgets now show a new SERP feature: Discussions and forums.

We take rankings in this feature into account when calculating organic traffic – traffic is distributed equally between all URLs.

## Rank Tracker

**New filters in GSC keywords report**

In the GSC keywords report, you can now filter by clicks, impressions, CTR, and position.

We’ve also added a “URLs” column which shows you the number of pages ranking for a keyword. Just click on a number to open a nested table and see all URLs.

## Site Audit

**Mobile usability issues**

Site Audit now reports problems with mobile usability on your site. The five issues we report on are:

- Viewport not set
- Content not sized correctly
- Font size too small
- Tap targets are too small or too close together
- If a document uses plugins

To find these issues, you’ll need to:

1. Connect to PageSpeed Insights API
2. Select the mobile user agent in your crawl settings
3. Run a new crawl

## General

**Enable two-factor authentication**

You can now enable two-factor authentication, or 2FA, from Account settings > My account. This lets you improve account security with time-based passwords via mobile apps like Google Authenticator.

If you’re a workspace owner or admin, you can also make 2FA mandatory for all workspace members from Account Settings > Members.

Note that 2FA is tied to an account rather than a workspace. So if you’re a member of multiple workspaces and one requires 2FA, you’ll need to perform 2FA every time you sign in.

**New APIv3 endpoint: Anchors**

You can now fetch anchor texts at scale with the new APIv3 endpoint for our Anchors report in Site Explorer.

[Read API documentation](https://docs.ahrefs.com/docs/api/site-explorer%2Foperations%2Flist-anchors)

As always, use the API button in the report to generate sample requests.

–

That’s all for this month. Check out [the Ahrefs changelog](https://ahrefs.com/blog/new-features/) for more updates, and leave any feature requests [on our Canny](https://ahrefs.canny.io/). Enjoy!
