---
title: "Ahrefs Site Audit: 11 Useful Features You Might Have Missed"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "medium"
slug: "new-site-audit-features"
url: "https://ahrefs.com/blog/new-site-audit-features/"
canonical: "https://ahrefs.com/blog/new-site-audit-features/"
author: "Nick Churick"
published: "2019-05-09T17:04:29+00:00"
updated: "2023-01-30T22:22:21+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2023_aging"
  - "product_or_tool_content"
fetched_at: "2026-06-12T11:53:36+00:00"
status_code: 200
html_hash: "205fa19dda3b87914e62e6da47e078483cf340679f4abe995fbd4092afcf64f1"
clean_word_count: 1388
clean_char_count: 8168
---
# Ahrefs Site Audit: 11 Useful Features You Might Have Missed

In early 2018, we released Ahrefs’ [Site Audit tool](https://ahrefs.com/site-audit). Since then, we’ve added tons of new features that we never announced outside of our [private Facebook group](https://www.facebook.com/groups/ahrefsinsider/).

That’s why I’m writing this post. I want to let you know about all the new features that you might have missed. Features that make your [SEO audits](https://ahrefs.com/blog/technical-seo-audit/) more insightful and actionable than ever!

Here’s a quick overview of what we’re about to cover:

1. [Site structure](#site-structure)
2. [URL Info](#url-info)
3. [Segments](#segments)
4. [Presets for filters](#presets-for-filters)
5. [Data filters for the previous crawl](#data-filters-for-previous-crawl)
6. [“Show changes” switch in Data Explorer](#show-changes-switch)
7. [Improved outgoing links export](#improved-outgoing-links-export)
8. [Multiple seed sources](#multiple-seed-sources)
9. [Redirect chain issues](#redirect-chain-issues)
10. [Enhanced issue details and “How to fix” instructions](#enhanced-instructions)
11. [Hints for Data Explorer fields](#data-explorer-hints)

Let’s dive straight in.

## 1. Site structure

The Site Structure report is the latest addition to our Site Audit tool.

It shows the [subdomains and subfolders](https://ahrefs.com/blog/subdomain-vs-subfolder/) of your site in a tree view. But most importantly, this report displays the distribution of HTTP status codes, link depth, estimated organic traffic, referring domains and more for each subsection of your website.

You can use this report to find the subsections of your website which:

- Attract the most backlinks from unique websites (referring domains)
- Have the most broken and redirected pages
- Are underperforming in terms of organic traffic
- Are furthest from the homepage (or another seed page)
- Have the most or least indexable content

You can also toggle between the table view and chart view. The latter will come in handy for your client reports.

## 2. URL Info

Click on any URL in Site Audit to see *all* the data that our crawler collected for that URL.

This report is not limited to on-page data such as title, description, content length, indexability, [canonicalization](https://ahrefs.com/blog/canonicalization/), etc. It also gives you quick access to the URL’s inlinks (internal links to the page), internal outlinks, external outlinks, hreflang tags, duplicates, and so much more!

## 3. Segments

Segmentation was one of the most popular feature requests from our users, and I can see why.

Most website owners and SEOs want to isolate issues related to a specific section of a site, such as /blog, /store/, or perhaps a subdomain like es.ahrefs.com.

So we added the ability to configure a segment, save it, and then return to it at any time with just a few clicks.

To do this, hit *Segment > Configure segment*

Here’s a quick example:

Sidenote.

The segment is applied to **every** report in Site Audit.

If you manage a big website and did not know about this handy feature, go and segment your crawls right now. 😉

## 4. Presets for filters

A preset is a set of filters for Data Explorer. It allows you to focus in on a predetermined subset of URLs quickly.

We have added 40+ presets in Site Audit to save you time.

Now, it takes only a few seconds to apply a preset for:

- 3XX redirects
- 4XX broken URLs
- Non-indexable pages
- External URLs
- PDF files
- and more

You can combine these presets, edit them as you like, and even save your own.

Let us know in the comments if you come up with any useful and creative filter combinations!

## 5. Data filters for the previous crawl

Speaking of filters…

Have you noticed this small switch in the filters section?

You can use this to filter URLs based on their values from the previous crawl (as long as you have more than one crawl in your project).

How is this useful?

Imagine that you crawled a website with Site Audit and found a bunch of 404 URLs. You tasked your developers with fixing any broken internal links on your website by removing the links or redirecting the dead (404) URLs. And today, you want to check if there are any broken links left.

Here’s what you can do:

Run a new crawl and apply the following filters to see which URLs are still returning the 404 HTTP status code:

How cool is that!?

## 6. “Show changes” switch in Data Explorer

Since we touched on previous crawls, you’ll be glad to know that you can now see what changed between the previous and current crawl for any URL.

Just hit the “Show changes” button in the report.

You can see the change for every column in Data Explorer. And, as you know, the columns here are adjustable.

Here’s a quick use case:

Say you asked your co-worker to update some page descriptions. Now you want to see if they did it. Simply run a new crawl, go to Data Explorer, add the Description column to the table, and see if there is any change on the website.

This simple switch also allows you to track changes in the number of incoming or outgoing links, monitor the size of the page or resource, and many other things.

It’s super handy for client reports.

## 7. Improved outgoing links export

Customer feedback told us that the outgoing links export in Data Explorer was not well-formatted for further processing.

So we added specific exports for outgoing links where every outgoing link has a row of its own in the exported .csv file.

## 8. Multiple seed sources

Every crawl in Ahrefs Site Audit has a starting point or points that we call seeds. As our crawler finds links on seed pages, it follows them and crawls the linked pages.

You can tell our crawler where to start crawling your website from. The options include:

- the URL generated from the “Scope” field
- Sitemap(s)
- a custom list of URLs
- URLs with external backlinks according to Ahrefs

You can select just one seed or use many seeds when you set up a new crawl.

## 9. Redirect chain issues

Redirects are an integral part of many websites. Single 301 redirects are of no harm to your site performance.

However, redirect chains always require attention.

So we’ve added two new errors.

**Redirect chain**:

And **Redirect loop**:

It’s generally recommended to get rid of redirect chains on your site. However, as long as the number of redirects in the chain [is below five](https://support.google.com/webmasters/answer/6033086?hl=en), it’s not so critical.

Redirect loops, however, require immediate attention. They are like “traps” for crawlers and users alike.

In Site Audit, when you click through to the list of affected URLs, you’ll see that each of these reports gives you all the data you need about the redirect chain, including:

- the first redirecting URL
- the URLs in the chain, and
- the final destination URL

## 10. Enhanced issue details and “How to fix” instructions

We know that merely reporting SEO issues is not enough. It is equally important to explain how to fix these issues and why.

For that reason, we’ve improved our issue descriptions and “how to fix” instructions to make fixing issues easier than ever. And where short descriptions in the interface don’t go deep enough, we’ve added a link to a more detailed article in our Help section:

## 11. Hints for Data Explorer fields

In Data Explorer, you can view and filter for issues relating to **more than two-hundred data points**. Many of these fields are pretty straightforward, but we felt that some needed a better explanation.

So now, you can mouse-over any field to see an explanatory hint:

## Final thoughts

As you can see, we’re continually improving our tools.

If you have suggestions or feature requests for our Site Audit tool, you’re welcome to share them [here](https://ahrefs.canny.io/site-audit). Your feedback drives our product development.

Right now, we are working on a couple of major updates to our [Site Audit tool](https://ahrefs.com/site-audit). I won’t tell you what they are, but you’re going to love them, I promise! So stay tuned.

How do you like the new features? Let us know in the comments below!
