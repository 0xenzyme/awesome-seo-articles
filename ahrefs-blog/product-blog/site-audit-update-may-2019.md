---
title: "What's new in Ahrefs' Site Audit tool (May 2019)"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "high"
slug: "site-audit-update-may-2019"
url: "https://ahrefs.com/blog/site-audit-update-may-2019/"
canonical: "https://ahrefs.com/blog/site-audit-update-may-2019/"
author: "Nick Churick"
published: "2019-05-23T08:08:01+00:00"
updated: "2019-06-03T15:04:30+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "product_or_tool_content"
  - "time_sensitive_title"
  - "title_year_2019_before_2026"
fetched_at: "2026-06-12T12:10:11+00:00"
status_code: 200
html_hash: "e520eb40da9ed775557f2ed9319aa2b2e79e72c4ea236051fd940994368d87d2"
clean_word_count: 543
clean_char_count: 3230
---
# What’s new in Ahrefs’ Site Audit tool (May 2019)

Earlier this month, we published [a blog post](https://ahrefs.com/blog/new-site-audit-features/) showcasing all the new features added to Ahrefs’ Site Audit tool in the past 12 months. Today we have even more improvements to announce!

There are no revolutionary new features this time around. Think of these more as minor yet notable upgrades that make Site Audit just that little bit better, again.

## 1. Faster data retrieval

We made a few essential changes to the way we store and process your crawl data.

What’s in it for you?

All reports and all filtered tables (segments, presets, affected URLs) in your new projects will load much faster, which saves time.

## 2. Revised crawl comparison

As you know, Site Audit compares the current and previous crawl to highlight recent website changes. Those changes are shown as green and red numbers in the various reports and in Data Explorer (with “Show changes” switch turned on).

Before today, Site Audit did this even if the previous crawl was incomplete—which gave you pointless data.

Now, Site Audit only compares the current crawl to the previous “**Completed**” one.

To find out which crawl was used for comparison, check the crawl settings panel or hover over any number that shows a change.

![previous-crawl-1](https://ahrefs.com/blog/wp-content/uploads/2019/05/previous-crawl-1.png)

## 3. Revisited crawl statuses

We have generally improved the way we assign statuses to crawls. The most significant changes affect “Stopped” and “Completed” statuses.

The crawls that reached *the maximum allowable depth*, *the maximum number of internal URLs*, or *the maximum duration time* used to have the “**Stopped**” status.

Now these crawls will be labeled as “**Completed**” as they actually have the expected output, limited to the crawl settings.

Only the crawls stopped manually will have the “**Stopped**” status in the project history.

## 4. One crawl per project

Until recently, you could have two crawls running for the same project at the same time. This had no practical value and just consumed your monthly credits.

From today, a new crawl won’t start if there is already a crawl in progress.

The scheduled crawl will be skipped if the previous crawl (whether manual or scheduled) is still running. Site Audit will continue to try to run the next scheduled crawl on the expected date.

## 5. “Skipped” crawls

Now, whenever a *scheduled* crawl cannot be started, its status will show as “**Skipped**” in the crawl history report.

Scheduled crawls will be skipped if you have no Site Audit credits left, or when there is already a crawl in progress for the project.

You can click on the crawl in the project history to learn why it was skipped.

## 6. Improved error reporting

If there’s ever an issue with a crawl, we show the cause of that issue when you open the crawl.

But we realized that some of those messages left a lot to be desired—so we improved them.

## Over to you

How do you like these improvements?

Please let us know if you have any questions or feedback. Don’t forget that you can submit and upvote feature requests for Site Audit [here](https://ahrefs.canny.io/site-audit) 😉
