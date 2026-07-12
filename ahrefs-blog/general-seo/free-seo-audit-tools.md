---
title: "The Only 2 Free SEO Audit Tools You Need"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "free-seo-audit-tools"
url: "https://ahrefs.com/blog/free-seo-audit-tools/"
canonical: "https://ahrefs.com/blog/free-seo-audit-tools/"
author: "Mateusz Makosiewicz"
published: "2022-10-28T06:00:00+00:00"
updated: "2023-08-15T10:11:21+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2023_aging"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:31:51+00:00"
status_code: 200
html_hash: "6b45d4e0681ba530a43c34a0ff9d52eda7e51c69cf5665f6282df5170911b692"
clean_word_count: 1704
clean_char_count: 10312
---
# The Only 2 Free SEO Audit Tools You Need

An SEO audit is where you find opportunities to improve a site’s search performance.

To find all of these opportunities, you need to look in different places: content, links, technical issues, and more.

This is something Google Search Console and [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) are designed for. And if you use both of them for what they are best at, you can do a comprehensive SEO audit without spending a dime on tools. Let’s do a quick overview of them.

## 1. [Google Search Console](https://search.google.com/search-console/about)

Google Search Console (GSC) is a unique and probably irreplaceable tool in any SEO toolbox because it offers the most accurate data when it comes to Google’s search-related products, e.g., organic traffic data, click-through rates, index coverage, etc.

If you don’t already have GSC set up, all you need to do is [sign in](https://search.google.com/search-console/about) with your Google account, verify the ownership of the site you want to audit, and wait for the data to come in. By the way, we also recommend submitting a sitemap via GSC as soon as possible (this helps Google discover and index your pages quicker).

GSC allows you to monitor the entire website (left) or just parts of it (right).

### How it helps

Here’s a list of SEO checks best done with GSC.

#### Checking organic traffic (from Google)

Arguably the most common use case for GSC and one of the reasons why it’s unique—getting organic traffic, impressions, and click-through rates straight from Google.

With the Performance tools in GSC, you can check for things like click trends over longer periods (up to 16 months) or pages with high rankings but low click-through rates.

#### Checking for manual actions

When Google thinks a page or an entire website is trying to manipulate search rankings, it can issue a so-called [manual action](https://support.google.com/webmasters/answer/9044175?hl=en). This can result in lower rankings or even exclusion from Google’s index.

Google uses GSC to communicate an eventual manual action. If your website has one, you will find it there, along with directions on how to fix the problem.

#### Checking for crawlability issues

Crawlability is a search engine’s ability to access content on a page. If a page can’t be accessed by [Googlebot](https://ahrefs.com/blog/googlebot/), searchers won’t find it on the SERPs.

The **Crawl Stats** report in GSC is helpful for detecting potential problems with crawling your website by Google. For instance, server 5XX errors, page timeouts, or unavailable [robots.txt files](https://ahrefs.com/blog/robots-txt/).

Google recommends this report for advanced users with sites bigger than 1,000 pages. However, pretty much every potential error here, including sudden drops in crawl rate, can also affect smaller sites.

#### Making sure your website is mobile-friendly

Mobile-friendliness is part of Google’s [Page Experience signals](https://developers.google.com/search/docs/appearance/page-experience) (has an impact on rankings). Google doesn’t want to rank high pages that are slow or hard to navigate on mobile devices, as too many people surf the web and look for local businesses using their phones ([stats from Google](https://www.thinkwithgoogle.com/marketing-strategies/app-and-mobile/mobile-web-traffic-statistics/)).

GSC automatically monitors your entire website for mobile usability. If there’s any action needed, you’ll see what needs fixing and where.

#### Core Web Vitals

Another part of the Page Experience signals. [Core Web Vitals (CWV)](https://ahrefs.com/blog/core-web-vitals/) is a set of metrics for a page’s load time, interactivity, and stability of the content as it loads.

You can also have CWV set up in [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools). And in case the **CWV** report shows a “not enough data” message, you can look at Ahrefs’ page speed metrics to spot slow pages.

All the above reports are sitewide. But if at any point you want to audit just one page from your website, you can use the URL Inspection tool.

## 2. [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools)

Ahrefs Webmaster Tools (AWT) is a tool that monitors the SEO health and SEO performance of your website.

Compared to GSC, it monitors more SEO issues (explains how to fix them too) and offers more data on backlinks and keywords. You can think of it as a tool that fills the gaps of GSC.

To set up AWT, [create a free account](https://ahrefs.com/webmaster-tools). Then add and verify your websites so that the tool can start to crawl them. You will be able to use your GSC account to verify if you like.

Sidenote.

AWT is free for an unlimited number of verified projects, up to 5,000 pages in total. If you need more, consider a premium [Ahrefs subscription](https://ahrefs.com/pricing) with access to additional SEO tools.

### How it helps

The tool consists of three main tools: Dashboard, [Site Explorer](https://ahrefs.com/site-explorer), and [Site Audit](https://ahrefs.com/site-audit). Most of your SEO audit will be done in Site Audit and some in Site Explorer. Let’s look at some details.

#### Site Audit (for technical and on-page SEO issues)

If you know what types of SEO issues you’re looking for after the crawl is done, you can head straight to the **All issues** report in Site Audit. You can edit the importance of the issues and use “Importance” as the filter.

For each issue, you can view details with tips on how to fix it.

Otherwise, you may want to start auditing with the **Indexability** report. It’s a fundamental report because, without indexing, pages are invisible to search engines and can’t bring in any search traffic. If there are any [canonicalization](https://ahrefs.com/blog/canonicalization/) issues or misplaced [“noindex” tags](https://ahrefs.com/blog/meta-robots/), this report will let you know.

Click on the category of issues to view affected pages.

In the **Internal pages** report, you will be able to spot any broken pages with 4XX or 5XX [response codes](https://ahrefs.com/blog/http-status-codes/). For instance, non-existing pages with the 404 code. Then you can view the number of referring domains to those pages by adding a column to the report.

This report allows you also to spot pages that are using HTTP protocol instead of HTTPS. (HTTPS is a small ranking signal, as part of the Page Experience signals.)

On the left, we can see the distribution of pages with errors. On the right, we can see the distribution of pages with HTTPS and HTTP protocols.

Any issues with links on your website will be shown in the **Links** report. For instance, [orphan pages](https://ahrefs.com/blog/orphan-pages/), dead-end pages, or pages with links to broken external pages.

Click on the corresponding card to see all broken internal or external pages. Graphs offer an at-a-glance overview of link distribution.

For low-hanging, on-page optimization opportunities, go to the **Content** report. Some issues may directly hinder your ability to rank, such as title tag issues.

The reports mentioned above are examples of **13 predefined reports available in** **AWT****.** You may find other reports helpful too, such as reports made for images, localization issues, or a special cluster report showing sets of pages with duplicate content. What’s more, you can create your own reports with four Site Audit tools:

- Page Explorer
- Link Explorer
- Internal Link Opportunities
- Structure Explorer

Once you’re done with fixing issues reported in [Site Audit](https://ahrefs.com/site-audit), you can schedule regular site crawls.

AWT will email you when the crawl is done so you can check for improvements, new issues, or just the general [SEO health score](https://ahrefs.com/blog/seo-score/). The tool will also keep a history of site crawls for three months.

#### Site Explorer (for checking keywords, traffic, and backlinks)

Unlike GSC, AWT has no limits on the number of reported organic keywords and backlinks.

With the **Organic keywords** report, you can see keywords where you already rank. And based on provided [SEO metrics](https://ahrefs.com/blog/ahrefs-seo-metrics/)—e.g., position, Keyword Difficulty (KD), volume—you can identify [content that could need an update](/blog/republishing-content/) or an opportunity to [take over a featured snippet](https://ahrefs.com/blog/featured-snippets/).

To see low-hanging featured snippet opportunities, you can use these filters in the **Organic keywords** report.

With the **Backlinks** report, you can see all backlinks pointing from *specific pages* (GSC shows just domains) to your website. The data comes with some handy SEO metrics, such as Domain Rating (DR) and organic traffic to the page. (You can also sort and filter through those metrics.)

Some other things you can do with AWT for your audit:

- See how fast you’re acquiring backlinks and keywords
- Assess the [quality of your backlinks](https://ahrefs.com/blog/what-are-backlinks/#what-makes-a-good-backlink)
- See which pages have a chance of moving from the second to the first SERP
- Discover traffic drops that coincided with Google’s core updates
- Look past GSC’s 16-month organic traffic limit
- Spot negative SEO attacks (through spammy anchors or sudden spikes in referring domains)
- Use SEO data to [evaluate your website’s worth](https://ahrefs.com/blog/how-much-is-my-website-worth/)

## Final thoughts

SEO audits can be overwhelming, so it’s good to start with a game plan. We recommend our [SEO audit checklist](https://ahrefs.com/blog/seo-audit/), where we’ve pinpointed 14 places you should look for impactful SEO issues. You will be able to do 13 of the 14 points with just GSC and AWT.

Feel free to play around with both tools and come up with your own game plan. You can learn more about the tools in the following:

- [How to Use Google Search Console to Improve SEO (Beginner’s Guide)](https://ahrefs.com/blog/google-search-console/)
- [GSC Getting Started Guide](https://support.google.com/webmasters/answer/9128669?hl=en&ref_topic=9128571)
- [AWT Overview Video](https://www.youtube.com/watch?v=ipTk-qGrNlc&t=1s)

Got questions? Ping me [on Twitter](https://twitter.com/m_makosiewicz).
