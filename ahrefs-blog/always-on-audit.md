---
title: "Automated Site Audit Tool by Ahrefs"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "low"
slug: "always-on-audit"
url: "https://ahrefs.com/blog/always-on-audit/"
canonical: "https://ahrefs.com/blog/always-on-audit/"
author: "Andrei Țiț"
published: "2024-11-27T13:45:01+00:00"
updated: "2026-04-07T12:36:12+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "product_or_tool_content"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:15:31+00:00"
status_code: 200
html_hash: "fc309b52187bacfe68b28193b64caabe547788cea2a2ed1cf5cd1af73ad0b7fe"
clean_word_count: 945
clean_char_count: 5921
---
# Always-on Audit (AOA): The Future Of Automated Website Monitoring

What if you had a system that worked around the clock to ensure your website’s SEO health stays in top shape?

Imagine a tool that automatically crawls your site 24/7, identifies critical issues as soon as they pop up, and sends real-time alerts for your most important pages – helping you fix problems *before* they impact your rankings.

Meet: **Always-on audit**.

## What is Always-on audit? (AOA)

**Always-on audit** is a new state for crawling your website in [Site Audit.](https://ahrefs.com/site-audit)

It’s designed to act as a real-time alerts system, a “safety net” for critical issues that might otherwise go unnoticed.

In short, it constantly crawls your website at a moderate speed to catch and report technical SEO issues for your most important pages as quickly as possible – unlike traditional crawlers which report them on a weekly or monthly basis.

## How does Always-on audit work?

Always-on audit constantly crawls new and known URLs — 24/7, at a moderate speed.

It’s designed to complement scheduled audits, helping you bridge the gap between them.

Scheduled audits are still your go-to for quickly gathering primary data about your website. Once done, AOA automatically kicks in, using that data to decide which pages to prioritize and recrawl.

That’s why when you stop an Always-on audit and start a new crawl, Site Audit will first run a quick normal crawl to index your website ***before*** switching to Always-on audit.

If new URLs are found on page, they will be extracted, batched up, and crawled later according to the existing crawl queue and their importance.

In fact, our [AhrefsSiteAudit](https://ahrefs.com/robot/site-audit) crawler uses several key metrics and signals to determine which pages to crawl and when, like:

- Organic traffic
- Internal and external inlinks
- URL depth
- Indexability status
- IndexNow signals

### IndexNow integration

Earlier this year, Ahrefs and [Yep](https://yep.com/) (our search engine) integrated with [IndexNow](https://ahrefs.com/index-now) – an Internet protocol that instantly notifies participating search engines when changes are made to your website.

![Ahrefs and IndexNow integration flow](https://ahrefs.com/blog/wp-content/uploads/2024/11/word-image-182809-3.jpg "Ahrefs and IndeNox integration flow")

This means that once a partner is pinged, all the information is shared with the other partners almost in real-time. This helps Ahrefs in two ways:

**1. Proactive crawling**: Always-on audits will use IndexNow signals to prioritize crawling important pages, so you can proactively detect critical SEO issues.

**2. Faster indexing**: All changes detected by our [Site Audit](https://ahrefs.com/site-audit) will notify the other participants automatically, ensuring your pages are indexed faster across multiple search engines *at the same time*.

NOTE: Auto-submit to IndexNow

The auto-submit to IndexNow function is available as a [project boost add-on](https://help.ahrefs.com/en/articles/10130957-what-are-project-boost-add-ons).

Otherwise, you can still manually submit pages to IndexNow by pasting the IndexNow API key – available under the project settings – into your website’s root directory.

### 24/7 alerts system

Did a page suddenly become non-indexable? Or a redirect break without warning?

Always-on audit keeps a constant watch, so you can catch critical SEO issues early on—with real-time alerts sent as they happen.

You’ll get an email if a new page is hit by an error-level issue. To avoid spam, alerts are grouped and sent every 30 minutes.

### Create customized alerts

Getting an email for each-and-every issue is counter-intuitive. You only want to receive those for what *you c*onsider critical for your own website.

Do you care only about indexability issues? No problem, enable only this category. Do you want to be instantly notified when a product page gets the “Out of stock” label on it? Just create a custom issue for that and enable it in the alert settings.

You’re in full control when it comes to setting up alerts in bulk, for the issues that matter.

But here’s more. The alert system allows you to customize the sensitivity level of alerts too, and how many it takes to trigger an alert.

### Crawl history changes

Always-on audit also enriches the current crawl history, allowing you to dive deep and analyze data with great granularity in [Site Audit](https://ahrefs.com/site-audit).

More specifically, you can track how your website has changed ***daily*** in terms of:

- # of pages added
- # of issues spotted and fixed
- The extent of changes undergone by a specific page

### Recrawl any page on demand

Ever wanted to see new issues for a page, without crawling your full website? Now you can. Just open the URL details panel of a page and hit **Recrawl.**

### Crawl credits usage

**Always-on audit** is available for all Lite and higher plans, with a crawl speed of 1 URL/minute.

You can benefit from increased crawl speed with the paid project boosts:

- 10 URLs/minute (with the Pro project boost)
- 30 URLs/minute (with the [Max project boost](https://help.ahrefs.com/en/articles/10130957-what-are-project-boost-add-ons))

At the moment, always-on audits **don’t** consume crawl credits.

NOTE

Scheduled audits still consume credits from your crawl credits allowance.

If you want to save up on crawl credits, you can always reduce the crawl speed from the project settings. Or as a last resort, put it on pause.

## What’s next?

With Always-on audit, [Patches,](https://ahrefs.com/patches/) and the [IndexNow integration](https://ahrefs.com/index-now/), Ahrefs is set to become the world’s first **fully automated site audit tool**.

–

Excited about Always-on audits? Upgrade your project to a [Pro or Max project boost](https://ahrefs.com/project-boosts) and catch SEO issues instantly.
