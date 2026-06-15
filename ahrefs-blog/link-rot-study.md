---
title: "At Least 66.5% of Links to Sites in the Last 9 Years Are Dead (Ahrefs Study on Link Rot)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "link-rot-study"
url: "https://ahrefs.com/blog/link-rot-study/"
canonical: "https://ahrefs.com/blog/link-rot-study/"
author: "Patrick Stox"
published: "2022-04-29T06:40:30+00:00"
updated: "2024-02-02T17:07:46+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:45:42+00:00"
status_code: 200
html_hash: "21464650fd6dc9360dabc8ecc63761223411f9e70b74bf6b4adc917d211c05a5"
clean_word_count: 1972
clean_char_count: 11068
---
# At Least 66.5% of Links to Sites in the Last 9 Years Are Dead (Ahrefs Study on Link Rot)

Link rot is when links stop pointing to their intended file, web page, or server. The links are dead. Link rot happens as pages on the internet are removed, redirected, or updated causing the links on these pages to go to broken pages or pages whose content has been altered.

Since January 2013, 66.5% of the links pointing to the 2,062,173 websites we sampled have rotted. We found another 6.45% with temporary errors. We don’t know if they’re still there or not.

This is even more complicated when it comes to SEO. Another 1.55% have other issues that prevent the links from being counted for the purposes of ranking.

That means a total of 74.5% of the links in our study are considered lost, with at least 66.5% being rotted.

Often, the links that no longer work are important. Check out [this example](https://perma.cc/0gwuqRxEJJW?type=image) of a website that was referenced in a U.S. Supreme Court case. Someone bought the domain and used it to make a statement.

In a [previous study](https://harvardlawreview.org/2014/03/perma-scoping-and-addressing-the-problem-of-link-and-reference-rot-in-legal-citations/) of legal journals and citations from 2014, 70% of the links within the journals and 50% of the URLs from U.S. Supreme Court decisions did not contain the originally cited material.

[Another study](https://link.springer.com/chapter/10.1007/978-3-642-33290-6_14) from 2012 found that 30% of social media links were dead within two years.

Most of the previous studies are fairly small and contain older parts of the web. I assume a lot more of the older web is already gone, if not most of it. For example, most sites stopped using extensions like .html on URLs many years ago in favor of clean URLs. Most sites have also moved from [HTTP to HTTPs](https://ahrefs.com/blog/what-is-https/).

Considering the above, we decided to do the largest link rot study ever. And it’s one of the only ones that cover the more recent version of the web.

Let’s dig into the data.

## About the data

Ahrefs has been crawling the web since 2010. But for the purpose of this study, we’re only looking at the data from January 2013.

You can use the **Backlinks** report in Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer) to check the data for your own site. For Ahrefs, 26.9 million out of 174.3 million links have been lost. Just compare the numbers with the “Lost” filter applied vs. the numbers with the “All” filter applied.

There are a few cases we tag as lost that we don’t count as link rot. I’ll cover that below.

As I mentioned in the intro, at least 66.5% of links to the sampled websites have rotted in the last nine years.

The web is complex and messy, and some things change faster than others. I wanted to see how many sites have link rot—and what percentage of their links experience link rot. A huge thanks to our data scientist Loveme Felicilda for pulling this data! This is the distribution for the percentage of link rot by domain across the dataset.

There are a lot of small sites that don’t have much link rot. If we take out the smallest sites and only look at those with more than 10 live links, you’ll see that larger sites seem to have quite a bit of link rot.

As I mentioned in the intro, the number of links we consider lost when it comes to SEO is even higher—percentage-wise, it’s 74.5%. I also wanted to see the distribution for these across the dataset.

There are a lot of small sites that don’t have many lost links. If we take out the smallest sites and only look at those with more than 10 live links, you’ll see that larger sites seem to have lost quite a lot of their links.

Links can be lost for many reasons. We classify lost links in different ways at Ahrefs. Here are the most common reasons that links are lost:

- Dropped (47.7%)
- Link removed (34.2%)
- Crawl error (6.45%)
- 301/302 (5.99%)
- Not found (4.11%)
- Not canonical (0.82%)
- Noindex (0.73%)
- Broken redirect (0%)

Let’s look at each of those and why they happen.

### 47.7% of links are from dropped pages

These pages are removed from our index for various reasons.

Pages may be dropped because they can’t be crawled or indexed. In some cases, a domain may not exist anymore.

### 34.2% of links are removed

In this case, the pages still exist; they just no longer link to you.

It could be that someone removed the link during a content refresh, replaced your link with a different one, or removed the link due to company policies. Another possibility is that a competitor decided to no longer link to you.

### 6.45% of lost links are from crawl errors

When we encounter an error while trying to crawl a page, it will be put into this bucket.

If the page is accessible when it’s crawled again and the link is still there, it will be counted as live. If the page continues to “error,” we may drop it from the index.

We chose to not count crawl errors in the total for link rot. It’s likely that a portion of these links no longer exists, but others still do.

### 5.99% of links are lost due to redirected pages

The page containing the link has been redirected somewhere else.

Pages change locations for all kinds of reasons. Commonly, this is the result of some kind of [website migration](https://ahrefs.com/blog/website-migration/).

### 4.11% of links are pages that are not found

In this case, the linking page has been deleted. The content, including the link, is missing.

Occasionally, these pages may become live again or be redirected; in such situations, they will be added back or placed in the redirect bucket.

### 0.82% of links are lost because the page they were on is no longer canonical

The canonical specified by the page has changed.

The linking page has a [“rel=canonical” tag](https://ahrefs.com/blog/canonical-tags/) to some other location. It could be a change from [HTTP to HTTPs](https://ahrefs.com/blog/website-migration/) or some kind of standardization involving [trailing slashes](https://ahrefs.com/blog/trailing-slash/) or [parameters](https://ahrefs.com/blog/url-parameters/). This is usually nothing to be worried about. The page is simply changing how it wants to be indexed. These links have just shifted locations, going from one page to another.

### 0.73% of links are lost because their pages are marked “noindex”

The linking page is marked “noindex,” so we don’t count the links from it.

We did not count pages marked as noindex in the numbers for link rot. The link technically exists, but the page it’s on won’t be found in search engines and won’t pass any value.

### A small number of links are lost due to broken redirects

In this case, we saw multiple redirects in a chain before. Now one of those redirects is broken. The link is, thus, kind of disconnected from the target.

This happens if:

- **The redirect chain is broken** – If any of the pages in the redirect chain fails to respond, it gets reported as a lost link.
- **The redirect no longer exists (or is changed)** – Let’s say you had a link from Site A → Site B, but the link was first redirected through one or more other URLs (e.g., Site A → Site C → Site B). If the linking site swapped this link out so that it linked directly (rather than going through a redirect chain), it would be reported as a lost link. The same applies if the final URL of the redirect is changed to redirect elsewhere.

## What can you do about link rot?

A lot of the links you obtain may be lost over time. One way you can possibly get some of them back is with [link reclamation](https://ahrefs.com/blog/link-reclamation/).

In many cases, your old URLs have links from other websites. If they’re not [redirected](https://ahrefs.com/blog/301-redirects/) to the current pages, then those links are lost and no longer count for your pages. It’s not too late to do these redirects, and you can quickly reclaim any lost value. Think of this as the fastest link building you will ever do.

Here’s how to find those opportunities:

- Paste your domain into [Site Explorer](https://ahrefs.com/site-explorer) (also accessible for free in [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools))
- Go to the **Best by links** report
- Add a “404 not found” HTTP response filter

I usually sort this by “Referring domains.”

You can even use link rot to your advantage. Broken link building is a tactic that involves finding resources in your niche that are no longer live, then reaching out to site owners and letting them know about a resource you have that can replace the broken link.

Want to know how to do this for your site? Our head of content, [Joshua Hardwick](https://ahrefs.com/blog/author/joshua-hardwick/), has you covered with a process-oriented guide to [broken link building](https://ahrefs.com/blog/broken-link-building/).

Another way to help with link rot is to fix broken links on your own website. These are easily identified in the [Site Audit](https://ahrefs.com/site-audit) **Links** report. Just remove the links or update the reference to a relevant page that exists.

You may also want to fix broken links from your site that point to other sites. I have trouble arguing for this for SEO and, generally, will deem it as a website health and maintenance task that is of pretty low priority.

However, you can argue that clicking these links is bad for user experience. Accordingly, you can prioritize the links that are more often clicked.

The list of broken links to external pages can also be found in the **Links** report. If you see zero broken external links as I do, it’s probably because you didn’t enable “Check HTTP status of external links” in your [Site Audit](https://ahrefs.com/site-audit) crawl settings.

## Final thoughts

Some companies and technologies have tried to help with link rot. Many of these solutions don’t really solve the problem of broken links or a changing web. Instead, they rely on archiving what was on the web so it can still be seen. For example, the [Internet Archive](https://archive.org/) has a [Chrome extension](https://chrome.google.com/webstore/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak?hl=en-US) that will show archives of pages if they’re broken.

Similarly, the CDN Cloudflare has an [Always Online option](https://blog.cloudflare.com/cloudflares-always-online-and-the-internet-archive-team-up-to-fight-origin-errors/) that will first look for its own archived copy of a page that’s offline. But if that doesn’t exist, it will pull the most recent version from the Internet Archive.

If you use Brave browser, a broken page will have a message that lets you check for an archived version at archive.org.

The Law Library of Congress implemented an [external archiving solution](https://digital.gov/2016/04/13/law-library-of-congress-implements-solution-for-link-and-reference-rot/) for the problem of link and reference rot in its legal research reports.

As always, message me [on Twitter](https://twitter.com/patrickstox) if you have any questions.
