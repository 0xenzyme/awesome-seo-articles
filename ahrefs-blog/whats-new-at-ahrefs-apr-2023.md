---
title: "What’s new at Ahrefs? (April 2023)"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "high"
slug: "whats-new-at-ahrefs-apr-2023"
url: "https://ahrefs.com/blog/whats-new-at-ahrefs-apr-2023/"
canonical: "https://ahrefs.com/blog/whats-new-at-ahrefs-apr-2023/"
author: "Rebekah Bek"
published: "2023-05-10T12:31:46+00:00"
updated: "2023-05-15T10:39:24+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2023_aging"
  - "product_or_tool_content"
  - "title_year_2023_before_2026"
fetched_at: "2026-06-12T12:17:24+00:00"
status_code: 200
html_hash: "dae98146072dec02d0088baf04787a4ba51b501d70e158f0b11f5922c0e2b98b"
clean_word_count: 860
clean_char_count: 4827
---
# What’s new at Ahrefs? (April 2023)

This month we’re introducing a bunch of new features: we now store robots.txt and sitemaps in Site Audit, there’s a new target filter in Keyword Ideas reports, use cases are now shown in Content Explorer, and lots more.

Let’s get right into it.

## 1. Site Explorer

**Nested keywords table in Top Pages 2.0**

You can now click on the numbers in the keywords column to open a table that shows all the keywords that a page is ranking for.

![Nested keywords table in Top Pages 2.0](https://ahrefs.com/blog/wp-content/uploads/2023/05/1.jpg)

If you’re in All countries mode, the country with the most keywords will be selected automatically.

In “compare” mode, the number of keywords in the nested table may exceed the number of keywords in the main table. That’s because the main table shows current keywords, while the nested table also contains lost ones.

## 2. Cross-tool updates

**HTTP status codes in SERP overview tables**

We now show HTTP status codes that don’t return a 200 response code in SERP overview tables in Site Explorer and Keywords Explorer.

This can impact things like word count. For example, when you see that a page returns a 302 response code, you might also notice that the word count of that page is shown as 0 since we couldn’t successfully crawl the page.

## 3. Keywords Explorer

**Target filter in Keyword Ideas reports**

Use this new Target filter in Keyword Ideas reports to dig into what positions a target URL is ranking for. You can choose to see all keywords, keywords that the target ranks for, or keywords that the target doesn’t rank for in the top 100 positions.

For example, if I wanted to make a big push on topics about blogging on the Ahrefs blog, I’d start my search in Keywords Explorer by searching for “blog” and “blogging”, go to the matching terms report and select Questions to find some informational topics.

Next, I’d set a target filter for ahrefs.com/blog and set it to path mode. In the results, we don’t have any pages ranking in the top 100 for topics like “how to start a blog” or “how to use pinterest for blogging” – so these might be good topics worth going after. On the other hand, a topic like “how to write a blog” is something we’ve already covered that might be worth an update.

## 4. Site Audit

**Storing robots.txt and sitemaps**

We’ve started storing robots.txt and sitemaps for each Site Audit crawl, so you’ll now see them in Page Explorer and Link Explorer. Just click on any page and go to View source to view its contents, then use the “Compare with” dropdown to compare changes between crawls.

We also now tell you which sitemap each URL and link is found in. For example, this “Referenced in sitemaps” field in Page Explorer points to each URL’s sitemap.

You can also click in to URL details to see the same “Present in sitemap” field with a link to the sitemap itself.

We’ve also added a bunch of new sitemap-related issues to Site Audit, which you’ll find under this new Sitemaps issues category. This brings the total number of pre-defined issues we detect in Site Audit to over 140.

Here’s the full list:

- Sitemap has syntax error
- Sitemap is not accessible
- Sitemap larger 50MB
- Sitemap with over 50K URLs
- Sitemap in the wrong format
- Sitemap includes URLs out of its scope
- Indexable page not in sitemap
- Page in multiple sitemaps

## 5. Content Explorer

**Use cases and predefined filters**

We’ve added a new tab to the entry page that shows you useful ways to search in the tool. Click on each use case to apply that set of filters.

For example, enter “parenting” in the search box and click on “low competition topics” to see the results load with some pre-defined filters to help you identify low competition topics.

## 6. General

**Keyword lists > Dashboard**

Good news: we’re working on bringing the keyword lists in Keywords Explorer to your Dashboard to make everything more organized and easy to access.

For now, you’ll be prompted to select a location when you create a new keyword list. For existing lists, the location will default to the United States if no location is stored or detected.

**Keyword database updates**

We now show around 5.6B keywords with complete trends from Sept 2015 to Jan 2023. We’ve also added over ~419K new keywords this month.

**New user joined your workspace notification**

To improve account security, we’ve enabled a new email notification that lets you know when a new user accepts an invitation to join a workspace. Both the inviter and the workspace owner get an email.

—

That’s all for this month. If you have any feature requests, you can leave them [on our Canny](https://ahrefs.canny.io/) or in our subscribers-only [Ahrefs Insider community](https://community.ahrefs.com/home), which we’ve just relaunched. Enjoy!
