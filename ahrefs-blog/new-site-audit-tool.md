---
title: "This is the new Site Audit tool by Ahrefs"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "high"
slug: "new-site-audit-tool"
url: "https://ahrefs.com/blog/new-site-audit-tool/"
canonical: "https://ahrefs.com/blog/new-site-audit-tool/"
author: "Tim Soulo"
published: "2017-12-14T07:43:10+00:00"
updated: "2017-12-15T00:20:11+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "product_or_tool_content"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:53:41+00:00"
status_code: 200
html_hash: "2ba7c06d66259e3444c45386702feba04c045ea3d7def99b5b8f5e1a597b5c4a"
clean_word_count: 1376
clean_char_count: 7592
---
# This is the new Site Audit tool by Ahrefs

More than a year ago, we removed our old and outdated Site Audit tool from Ahrefs and announced that we were going to build a shiny new one from scratch.

We were hoping that we’d be able to deliver the new tool in 6-8 months. But in all honesty, we were a little over-ambitious with its functionality and encountered a few “bumps” along the way.

So, after a rather long wait, the new Site Audit tool is finally released!

Before I get into more detail with features and reports, let me share some of the things that make it so awesome:

**It is cloud-based** - You don’t need to install any software on your computer and you don’t need to own any servers or proxies to run it on a large website. Just click “Start crawl” and we’ll handle the rest.

**It is blazingly fast** - According to our backend team, our Site Audit tool can crawl faster than most websites can handle (which should not come as a surprise, considering that [Ahrefs has the second best crawler after Google](https://www.incapsula.com/blog/most-active-good-bots.html)). But you’re only allowed to increase the crawl speed if you verify the ownership of that website.

**It has 100+ pre-configured SEO issues** - And you have full control over them: modify them to your liking, remove those you don’t like and add any custom ones. This allows you to create a unique list of issues for every project (if needed).

**It has Ahrefs’ backlink and traffic metrics integrated** - No need to cross reference data between different tools. You’ll have all the SEO metrics that you care about in one place.

**It is visual** - Many of the aforementioned SEO issues are visualized with cool graphs and then grouped into reports, which makes the data much easier to grasp and explain to your clients. We have both: the graphs of the current snapshot of your website’s health, as well as your progress over time.

**It saves each crawl** - This way you can always go back and review previous crawls if needed. The option to compare crawls is in the pipeline already.

**It will support JavaScript Rendering** - This will be added in about ~2 weeks from now.

**It will support [Lighthouse](https://developers.google.com/web/tools/lighthouse/)** - This one is in the pipeline right after JavaScript rendering.

And now let’s take a closer look at the functionality of the new Site Audit tool.

## 1. Crawl settings / Scheduling

Upon starting a new project, you get full control over what we crawl and how fast we crawl it.

Here are some of the settings that you can configure:

- You can start crawling from: homepage, sitemaps, list of URLs having backlinks (as known by Ahrefs) or your custom list of URLs.
- You can specify crawl depth and the files and resources that you want us to crawl.
- You can include and exclude URLs and specify URL rewrite rules (using [regex](https://en.wikipedia.org/wiki/Regular_expression)).

And, finally, you can easily schedule subsequent crawls with very precise timing:

## 2. Real-time crawl log

It takes us just a few seconds to start crawling your website and we immediately show you a real-time Crawl log with the status of each item:

This is very handy; you won’t need to wait for the crawl to finish just to see that something went wrong.

For instance, you might overestimate what your server can handle and set up a crawl speed that is a tad too fast, which will result in most pages timing out. If that happens, you’ll see these “time outs” instantly in your crawl log and will be able to stop that crawl immediately and re-configure it.

## 3. Issues / Reports

In a similar fashion to the Crawl log, we start building all reports in real-time, using the data that we’ve collected so far:

As of today, Ahrefs’ Site Audit tool will monitor your website for the 100+ most common SEO issues.

And you can easily modify any of them, remove those you don’t agree with and add your own custom ones.

Many of these issues are grouped into cool visual Reports that are listed in the left-hand menu.

Everything in these reports is “clickable” - just click on the item that you would like to focus on and you’ll be redirected to the corresponding “view” in Data Explorer with a list of all affected pages.

You also get a handy “top level” filter that allows you to quickly rebuild any report for a specific subset of pages.

For example, you can look at all your **/blog/** pages without having to setup a new project:

## 4. Data Explorer

This is the heart and soul of Ahrefs’ Site Audit tool. We give you all the raw data that we have crawled, so that you can slice and dice it in any way you want (and export to CSV, if needed).

We save 150+ data points for each URL and you can build rather complex filtering logic with our “AND/OR” function and grouping support:

You can then save the whole thing as a custom issue and use it in other projects that you have in the Site Audit tool.

## 5. Progress graphs

The reason why you want to crawl your website for SEO issues is to get them fixed, right?

And the reason why you want to then re-crawl your website again is to see how many more issues are left and what your progress is, as compared to the previous crawl.

That’s why our new Site Audit tool has quite a few different graphs to illustrate your progress over time - both on project-level and for each individual issue.

## More updates are coming

As usual, the fact that we have released our Site Audit tool doesn’t mean that we have stopped working on it.

We have quite a few things in the pipeline for the next few months:

- **Description of each issue (+ how to fix)** - A lot of our customers are not very experienced in SEO, so we’ll gladly give them clues as to why each issue is important (or not) and how to fix it.
- **Schema.org & AMP support** - Even though these are not considered direct ranking factors, they may have a profound impact on your visibility in Google SERP, which makes them important to monitor.
- **Comparing crawls** - This one should be pretty dope. You’ll not only be able to easily see which pages were fixed since last crawl (and if any new ones are affected with that same issue), but we’ll also show you the exact changes: what Title your page used to have versus the current one, along with which outgoing links were removed from the page, which ones were added, and so on and so forth.
- **HTML data extraction** - We’re going to save the full HTML code of your pages so that you’ll be able to use regex to extract any data you may need. For example, if you decide to check which of your pages have the Facebook tracking pixel code installed, you won’t need to re-crawl your website - because all data is already there.
- **On-page report** - This one should be self explanatory. The plan is to try to aggregate all the useful data that we have on your page into a single actionable report.
- **Site structure visualisation** - It often helps a lot to see a “map” of how the pages of your website are all interlinked. Which is why we’ve planned it for our Site Audit.

So these are some of the things that we already know we need to add in order to make our Site Audit tool even more awesome.

But we’re always open to your feedback!

If you have any feature requests, please feel free to post them here: [**https://ahrefs.canny.io/site-audit**](https://ahrefs.canny.io/site-audit) (or upvote those that someone else has already posted).

We know that there are a lot of cool issues, graphs and reports that could be added to Site Audit and your input will help us prioritise our roadmap.
