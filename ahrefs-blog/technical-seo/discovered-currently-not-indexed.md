---
title: "How to Fix \"Discovered - currently not indexed\""
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "discovered-currently-not-indexed"
url: "https://ahrefs.com/blog/discovered-currently-not-indexed/"
canonical: "https://ahrefs.com/blog/discovered-currently-not-indexed/"
author: "Dino Kukic"
published: "2022-09-20T06:00:00+00:00"
updated: "2024-10-04T15:11:27+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T11:27:22+00:00"
status_code: 200
html_hash: "8fc7a52679b5cf21d382197c2284e9dc09b2d90ecf08dbd483680af18a9a1079"
clean_word_count: 1862
clean_char_count: 11357
---
# How to Fix “Discovered - currently not indexed”

“Discovered - currently not indexed” means Google knows about the URL but hasn’t yet crawled or indexed it.

Follow this five-step process to diagnose and fix the issue.

## 1. Request indexing

If you only see a few pages with the “Discovered - currently not indexed” issue, try requesting indexing via Google Search Console (GSC). To do that, click “URL inspection” on the menu and enter the page’s URL. If it’s not currently indexed, hit the “Request indexing” button.

If all is good, you should see a message that the URL was added to the priority crawl queue.

!["Indexing requested" notice in Google Search Console

Sidenote.

There is a limit on how many URLs you can submit. While this is not defined in the docs, you can typically submit 10–15 URLs daily.

If this doesn’t work, there’s almost always an underlying issue you need to diagnose and fix before requesting indexing for a second time. So keep reading.

Did you know?

There’s a way to send Google batch indexing requests (i.e., multiple URLs at once). Learn more in [our guide to Google’s Indexing API](https://ahrefs.com/blog/google-search-console-url-inspection-api/).

## 2. Check for crawl budget issues

[Crawl budget](https://ahrefs.com/blog/crawl-budget/) is how fast and how many pages a search engine wants to crawl on your site. If your crawlable URLs exceed your crawl budget, you may see the “Discovered - currently not indexed” warning.

According to Google’s Gary Illyes, [90% of sites don’t need to worry about it](https://search-off-the-record.libsyn.com/should-i-worry-about-crawl-budget). However, although issues with crawl budgets tend to affect larger sites, specific technical setups, problems, and mistakes can lead to issues on smaller sites.

Let’s look at a few things that can lead to crawl budget issues and how to improve them.

### Do you serve content from subdomains?

Let’s say your main website is on *example.com,* but you have assets on a subdomain such as *cdn.example.com*. In this case, the asset subdomain may be considered part of your main website and [grouped together for the crawl budget](https://www.seroundtable.com/google-subdomains-crawl-budget-31186.html).

Consider serving assets from a CDN URL with a separate crawl budget to solve this.

### Do you have unnecessary redirects?

Typically, when we decide to remove a page from the website, we add a [redirect](https://ahrefs.com/blog/redirects-for-seo/) to another relevant page. However, this isn’t always necessary. Unless the page has backlinks or traffic, it’s better to remove or replace internal links to the deleted page and return a 404.

Here’s a flowchart explaining the process:

![How to fix unnecessary redirects

You can find redirected URLs with internal and external links free of charge with an [Ahrefs Webmaster Tools (AWT)](https://ahrefs.com/webmaster-tools) account. Here’s the process:

1. Crawl your website with Ahrefs’ [Site Audit](https://ahrefs.com/site-audit)
2. Go to the latest crawl
3. Go to the **Redirects** report
4. Click on the number of internal URL redirects
5. Add columns for “No. of all inlinks” and “No. of referring domains”

![Redirects with internal links and backlinks, via Ahrefs' Site Audit

### Do you have duplicate content?

Duplicate content is when you have near or exact copies of pages accessible at multiple URLs. Examples include:

- The same pages are accessible at www and non-www versions of your site, as well as HTTPS and HTTP.
- Development or staging instances.
- Empty product or category pages with boilerplate content.

The way you solve duplicate content issues depends on your circumstances.

**Learn more:**[*Duplicate Content: Why It Happens and How to Fix It*](https://ahrefs.com/blog/duplicate-content/)

### Have you used internal nofollow links?

[Nofollow links](https://ahrefs.com/blog/nofollow-links/) won’t prevent the page from being indexed. However, using them internally tells search engines a page is not important.

Here’s how to find pages with nofollowed internal links for free using [AWT](https://ahrefs.com/webmaster-tools):

1. Crawl your site with [Site Audit](https://ahrefs.com/site-audit)
2. Go to the **Links** report
3. Click the “Issues” tab
4. Look for the “​​Page has nofollow incoming internal links only” and “Page has nofollow and dofollow incoming internal links” warnings and notices

![Finding nofollowed internal links with Ahrefs' Site Audit

If the page is important, replace the nofollow links with followed ones.

### Do you have orphan pages?

If the only way to discover your new page is from the sitemap and it has no internal links, Google may consider it unimportant.

I’ll discuss this in more detail below when talking about internal linking.

## 3. Check for content quality issues

Google doesn’t index everything it discovers. It [prioritizes high-quality, unique, and compelling content](https://twitter.com/JohnMu/status/1240620876845981698). As Google hasn’t yet crawled pages with this warning, it can’t know whether the content is low quality or not. However, it may have an idea based on similar pages that it’s already crawled—which is why it may have “deprioritized” crawling.

Here are a few types of content Google is unlikely to index:

- **Machine-translated content** – The translations will be far from perfect if you use Google’s Translate API or similar to localize content. In which case, it’s not particularly useful to searchers.
- **Spun content** – This is where you use software to rewrite content. The result is almost always low-quality, plagiarized content.
- **AI-generated content** – [AI writing tools](https://ahrefs.com/blog/ai-writing-tools/) are gaining popularity, but they rarely create useful content without human involvement.
- **Thin content** – These are pages without much unique content.

If any of these apply to your content, use the flowchart below to fix the issue:

![How to solve content quality issues

In short, if you have thin content, merge it with other thin content to create something useful or delete it. Otherwise, improve the content. If the resulting content isn’t made for organic search, [noindex](https://ahrefs.com/seo/glossary/noindex-tag) it so search engines can prioritize crawling more important pages.

## 4. Check that content is internally linked

Internal links are links from one page on your website to another. Google often sees URLs without any or many internal links as unimportant and may not index them. You can check if a URL has internal links for free with [AWT](https://ahrefs.com/webmaster-tools). Here’s how:

1. Crawl your site with [Site Audit](https://ahrefs.com/site-audit)
2. Go to the **Page Explorer** tool
3. Filter for “All pages” under “Content”
4. Add a column for the “No. of all inlinks”

![Finding the number of internal links to pages on a website, via Ahrefs' Site Audit

If you selected backlinks and/or sitemaps as URL sources when setting up your project, you may also be able to find some orphan pages. Just go to the **Links** report, click the “Issues” tab, and look for the “Orphan page (has no incoming internal links)” error.

![Finding orphan pages with Ahrefs' Site Audit

Recommendation

Finding all the orphan pages on your website may not be possible with a crawling tool like [Site Audit](https://ahrefs.com/site-audit). This is because orphan pages have no internal links to crawl. You’ll have to check server logs for a complete picture. Learn how in [our guide to finding orphan pages](https://ahrefs.com/blog/orphan-pages/).

You can also use Ahrefs to find internal linking opportunities between two existing pages. Here’s how:

1. Go to the **Internal link opportunities** report in [Site Audit](https://ahrefs.com/site-audit)
2. Enter a keyword related to the page you want to add internal links to
3. Choose “Keyword” as the search mode

For example, let’s say Ahrefs wrote a post about keyword research. Entering “keyword research” finds pages on your site that mention that keyword and shows you the context. You can then add internal contextual links where relevant.

Alternatively, you can search within the page text using **Page Explorer** to find potential pages to link from when you are publishing a new page.

![Searching for contextual internal link opportunities using the Page Explorer in Ahrefs' Site Audit

However, none of these tactics can replace a good website structure with logical internal linking. That’s something every site should prioritize. However, if you’re facing issues, one way is to “hack” your crawl depth and ensure all your internal pages are linked from an HTML sitemap.

An HTML sitemap is an HTML page that gives users a better picture of your website structure and an easier way to navigate. Unlike XML sitemaps, which are made to be parsed by different systems, HTML sitemaps are made for users. While they’re sometimes considered a thing of the past, [they are still relevant](https://www.searchenginejournal.com/html-sitemap-importance/325405/).

If you have a big website, you may want to consider splitting it into a logical structure, as you don’t want tens of thousands of URLs linked to from a single page. [Check out how LinkedIn does it for inspiration.](https://www.linkedin.com/directory/people)

Recommendation

Ensure you use proper <a> tags for the internal links instead of using JavaScript functions such as onClick() to lead the user to another page. If you’re using Jamstack or a JS framework, check how it, or some of its libraries, handles internal links. They need to be rendered as <a> tags.

## 5. Check backlinks

Backlinks are one of the signals Google uses to decide whether a page is likely to be valuable and worthy of crawling. If your page has no or few [high-quality backlinks](https://ahrefs.com/blog/high-quality-backlinks/), it may be one of the reasons Google has “deprioritized” crawling.

Getting more backlinks is probably the hardest of all the listed, but it does pay off. Even one valuable link can help Google discover your content and index it faster.

You can see how many backlinks any page on your website has for free with [AWT](https://ahrefs.com/webmaster-tools).

If you want to check a specific page, paste it into Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer) and check the **Overview** report.

![Checking backlinks to a page in Ahrefs' Site Explorer

If you want to see which pages do or don’t have many backlinks, enter your domain into [Site Explorer](https://ahrefs.com/site-explorer) and check the **Best by links** report.

![Finding the most linked pages on a website using the Best by links report in Ahrefs' Site Explorer

If an important page has few or no backlinks, consider trying to build more.

Further reading

- [Link Building for SEO: The Beginner’s Guide](https://ahrefs.com/seo/link-building)
- [How to Get Backlinks: 15 Proven Tactics](https://ahrefs.com/blog/how-to-get-backlinks/)
- [9 Easy Link Building Strategies](https://ahrefs.com/blog/link-building-strategies/)

## Keep learning

- [Google’s New Search Console URL Inspection API: What It Is & How to Use It](https://ahrefs.com/blog/google-search-console-url-inspection-api/)
- [How to Fix “indexed, though blocked by robots.txt” in GSC](https://ahrefs.com/blog/indexed-though-blocked-by-robots-txt/)
