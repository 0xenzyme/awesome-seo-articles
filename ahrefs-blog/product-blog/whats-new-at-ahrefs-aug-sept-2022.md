---
title: "What’s new at Ahrefs? (Aug & Sept 2022)"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "high"
slug: "whats-new-at-ahrefs-aug-sept-2022"
url: "https://ahrefs.com/blog/whats-new-at-ahrefs-aug-sept-2022/"
canonical: "https://ahrefs.com/blog/whats-new-at-ahrefs-aug-sept-2022/"
author: "Rebekah Bek"
published: "2022-10-12T14:33:53+00:00"
updated: "2022-11-03T04:20:25+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2022_old"
  - "product_or_tool_content"
  - "title_year_2022_before_2026"
fetched_at: "2026-06-12T12:17:35+00:00"
status_code: 200
html_hash: "85e00fafa2f1d90a104fa99428e86772d5b4d5dfeaa3b6b74035a5e8d5b20aa6"
clean_word_count: 1082
clean_char_count: 6299
---
# What’s new at Ahrefs? (Aug & Sept 2022)

We have lots to talk about today: new reports, new features, and exciting things like the new Ahrefs API v3 for Enterprise plans.

Use the sidebar to jump to updates for a specific tool.

## 1. Site Explorer

#### **Organic keywords history chart in Overview 2.0**

This new chart shows you the organic keywords ranking history for your target.

Since it shares the same settings as the Performance chart, changing filters by adding competitors or comparing by year changes the data in both charts.

To collapse either chart, click on the caret in the upper right.

![Filters for organic keywords history chart in Overview 2.0](https://ahrefs.com/blog/wp-content/uploads/2022/10/okchart1.jpg)

To filter for keywords ranking in specific position groups, click on these position buckets.

Finally, the chart used to reset whenever you entered a new target.

We’ve changed this so that the last selected metrics, timeframe, and granularity are saved per user. Now, even after you enter a new target, the same settings will apply by default.

#### **Calendar report for Pages**

Back in July, we announced the new [Calendar report for Positions](https://ahrefs.com/blog/whats-new-at-ahrefs-july-2022/).

Following that, the Calendar report for Pages is now live. It’s based on the Top pages report, and shows both you new pages that started ranking for at least one keyword in the top 100, as well as lost pages that lost all their keyword rankings.

In the example below, on the 22nd of July, the Ahrefs blog saw 10 new pages enter the top 100 search results and 2 pages that lost all their keyword rankings.

To select several dates at once, just click and drag on the calendar itself.

You’ll find a breakdown of all movements below.

We’ve also made the Positions Calendar report available to all plans. Now, Lite plans can view data in the Positions tab for the last 7 days.

#### **Internal backlinks report**

The new Internal backlinks report is similar to the legacy report, but has many more useful filters – take “Target HTTP code” for example. This status code filter makes it easy to find and clean up broken or redirected pages without having to run a crawl.

## 2. Site Explorer & Keywords Explorer

#### **Filter for keywords with a local pack in the SERP**

We’ve added a handy new local pack filter in both Site Explorer and Keywords Explorer reports.

A good way to use this in Site Explorer is to see your competitors’ local pack rankings.

Just go to the organic keywords report with their domain set as the target. Then, click on the SERP features filter and select Local Pack to find out where they’re ranking for in local SERPs.

And now, you have a list of keywords to go after.

In Keywords Explorer, you could enter seeds like “dentist” and “dental”.

Then head to the Matching terms report and select Local Pack in the SERP features filter. And there’s your list of keywords to target.

#### **Copy URLs in SERP overview widgets**

Now, you can select positions in the SERP overview widgets in Site Explorer and Keywords Explorer and either click on **Copy** to copy the URLs, or **Open in** to open up to ten URLs directly in Link Intersect or Content Gap.

## 3. Site Audit

#### **Links report in predefined issues**

We’ve added a new tab with a links report to a bunch of predefined issues in Site Audit. You’ll see it whenever you click on a predefined issue where we’ve made tabs available.

Previously, you’d see a list of pages where an issue happened. The problem with this was that many issues are related to links, not pages.

Now, you can just switch to the links tab and quickly see a list of the links related to the issue. This is a much more efficient way to make changes quickly.

#### **Bulk export of issues**

Up until very recently, you could only export Site Audit issues one by one. This was not super fun to do.

We’ve now made bulk export of all issues in Site Audit possible. Just click on Export all issues on your crawl overview, All issues and Bulk export pages to start preparing a zip archive with .csv files for all issues in the background.

Once it’s ready, you can download it from the export tray in the header.

Bulk export is available for all paid plans.

#### **HTTP authentication in Site Audit**

The new HTTP authentication feature in Site Audit lets you crawl staging and restricted websites protected by basic or digest HTTP authentication.

You’ll find it on the Scope page when creating a new project and in an existing project’s Project settings. If at least one of the seed URLs entered returns a 401 status code, you’ll see a “Website requires HTTP authentication” message.

If you enter your credentials, we’ll use them to recheck seed URLs, verify ownership, and crawl the website.

This feature is available for Advanced plans and higher.

## 4. General

#### **Tags filter in GDS Rank Tracker connector**

Our Rank Tracker connector for Google Data Studio now supports the tags filter. It expects a comma-separated list of tags and affects all the charts and reports in the data source.

Read more in our [GDS documentation](https://docs.ahrefs.com/docs/data-studio/reference/rank-tracker-configuration).

#### **API v3 for Enterprise plans**

Ahrefs’ new API v3 lets Enterprise plan users pull data from Site Explorer’s Overview, Backlinks, Referring domains, Organic keywords, Top pages, and Paid pages reports. More Site Explorer reports and other tools are coming soon.

If you already have an active API v2 subscription, it’ll still work as before.

Read more about API units consumption in our [API documentation](https://docs.ahrefs.com/docs/api/).

#### **Audit log for Enterprise plans**

If you’re the workspace owner or an admin of an Enterprise account, you can now access the new Audit log from Account Settings.

This log shows you all reports consumption in the workspace for the last 90 days.

#### **Admin view settings for workspace owners and admins**

We’ve also added Admin view settings to the Dashboard.

Now, workspace owners and admins can view all projects and folders, including the ones that aren’t shared with them. The Projects section in Account Settings that used to list all projects is now discontinued.

—

That’s all for this month. Enjoy!
