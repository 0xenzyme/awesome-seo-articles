---
title: "How to Submit Your Website to Google"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "submit-website-to-google"
url: "https://ahrefs.com/blog/submit-website-to-google/"
canonical: "https://ahrefs.com/blog/submit-website-to-google/"
author: "Joshua Hardwick"
published: "2021-04-20T16:00:46+00:00"
updated: "2024-03-18T13:28:18+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T12:11:22+00:00"
status_code: 200
html_hash: "1507d9b5c146191dc327ddae925ec2c9e62949496f2c8b80b032c767b0915c0e"
clean_word_count: 2100
clean_char_count: 12739
---
# How to Submit Your Website to Google

If you want search engine users to be able to find your website, it needs to be indexed.

But how do you submit your website to Google in 2021? And do you even need to?

In this guide, you’ll learn:

- [How to submit your website to Google](#submitting-your-website)
- [How to submit URLs to Google](#submitting-urls)
- [If and why you need to submit your website to Google](#importance)
- [How long it takes for Google to index your website](#how-long-indexing-takes)
- [Why Google might not be indexing your website](#troubleshooting)

## How to submit your website to Google

There are two ways to submit your website to Google. You can either submit an updated sitemap in Google Search Console or submit the sitemap URL using Google’s “ping” service. Both options are completely free and only take a second.

### Finding your sitemap

Both submission methods require your sitemap URL. The way you find or create this depends on your website platform.

**If you use WordPress**, install a [free SEO plugin](https://ahrefs.com/blog/best-seo-plugins-for-wordpress/) like [Yoast](https://wordpress.org/plugins/wordpress-seo/), [Rank Math](https://wordpress.org/plugins/seo-by-rank-math/), or [The SEO Framework](https://wordpress.org/plugins/autodescription/). All three of these create sitemaps for you. It will be here: `yourwebsite.com/sitemap_index.xml`

**If you use Wix, Squarespace, or Shopify**, your sitemap is here: `yourwebsite.com/sitemap.xml` .

**If you use a different platform or CMS**, chances are it creates a sitemap for you. The most likely locations for this are:

`yourwebsite.com/sitemap.xml`

`yourwebsite.com/sitemap_index.xml`

`yourwebsite.com/sitemap1.xml`

If it’s not there, see if the location is listed at yourwebsite.com/robots.txt.

**If you don’t use a platform or CMS**, you’ll need to [create a sitemap manually](https://ahrefs.com/blog/how-to-create-a-sitemap/). However, it’s worth checking the URLs above first, as you may already have one.

### Submitting your sitemap

You have two options here.

#### Option 1. Submit your sitemap in Google Search Console

1. Log in to [Google Search Console](https://search.google.com/search-console/about)
2. Go to the right property
3. Click “Sitemaps” on the left menu
4. Paste in your sitemap URL
5. Click “Submit”

This is arguably the best method because Google Search Console alerts you to sitemap errors in the future. It also provides insights into your site’s health, including why certain pages may not be indexed.

#### Option 2. Submit your sitemap by pinging Google

Google operates a “ping” service where you can request a fresh crawl of your sitemap. Just type this into your browser, replacing the end part with your sitemap URL:

`http://www.google.com/ping?sitemap=<complete_url_of_sitemap>`

For example, if your sitemap is located at yourwebsite.com/sitemap.xml, you’d navigate to:

`http://www.google.com/ping?sitemap=https://yourwebsite.com/sitemap.xml`

You should then see the “sitemap notification received” page.

Google [says](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap) you should only use this service with new or updated sitemaps. Don’t repeatedly submit or ping unchanged sitemaps multiple times.

## How to submit URLs to Google

Generally speaking, there’s no need to submit each new page to Google. As long as the new URLs are in a sitemap that you already submitted to Google, they’ll be discovered eventually. However, there are two ways you can potentially speed up this process.

#### Option 1. Ping Google

Make sure the new pages are in your sitemap, then use the instructions in the previous section to ping Google and prompt them to re-check your sitemap. This isn’t totally necessary if you’re using WordPress with Yoast, Rank Math, or The SEO Framework because these plugins [all](https://wordpress.org/support/topic/google-sitemap-ping/) [ping](https://rankmath.com/kb/configure-sitemaps/#ping-search-engines) [Google](https://wordpress.org/support/topic/how-to-verify-sitemap-ping-to-google/) automatically.

#### Option 2. Use Google’s URL Inspection Tool

It’s possible to add URLs to Google even if they’re not in your sitemap (although they should be) using the [URL Inspection Tool](https://support.google.com/webmasters/answer/9012289?hl=en) in Google Search Console.

1. Log in to [Google Search Console](https://search.google.com/search-console/about)
2. Go to the right property
3. Click “URL Inspection” on the left menu
4. Paste in the URL of your new page
5. Hit return
6. Click “Request indexing”

If you only have one or two new pages, there’s no harm doing this. Some people believe that it speeds up indexing. If you have lots of new pages to submit to Google, don’t use this process. It’s inefficient, and you’ll be there all day. Use the first option instead.

## Do I need to submit my website to Google?

Kind of.

Google will usually find and index any valuable pages eventually, even if you don’t submit them. But there are still benefits to submitting your website to Google.

Before we talk about these benefits, we should discuss how Google finds and indexes content.

### How Google finds and indexes your content

Google finds and indexes content in four main steps.

Sidenote.

 These are somewhat oversimplified as Google is a complex beast.

#### Step 1. Discover

Discovery is where Google learns that your website exists. Google finds most websites and pages from sitemaps or [backlinks](https://ahrefs.com/blog/what-are-backlinks/) from known pages.

#### Step 2. Crawl

Crawling is where a computer program (spider) called [Googlebot](https://ahrefs.com/blog/googlebot/) visits and downloads your pages.

#### Step 3. Process

Processing is where key information is extracted from the crawled pages and prepared for indexing.

#### Step 4. Index

Indexing is where processed information from crawled pages is added to a big database called the search index. This is essentially a digital library of trillions of web pages from which Google pulls search results.

**Recommended reading:** *[How Do Search Engines Work and Why Should You Care?](https://ahrefs.com/seo/how-do-search-engines-work)*

### Why submitting to Google is important

Each of the four steps above happens in order. It’s a journey. By submitting your website to Google, you can potentially speed up the first part of the process: Discovery.

Like any journey, the sooner you set off, the sooner you can arrive at your destination. In this case: indexing.

But there are a few other reasons why submitting a sitemap is important.

#### 1. It tells Google which pages are important

Sitemaps don’t always include every page on your website. They only list important pages and exclude unimportant or duplicate pages. This helps to combat issues like the indexing of the wrong version of a page due to [duplicate content](https://ahrefs.com/blog/duplicate-content/) issues.

#### 2. It tells Google about new pages

Many CMS’ add new pages to your sitemap and some ping Google automatically. This saves time having to submit every new page manually.

#### 3. It tells Google about orphan pages

Orphan pages are pages without [internal links](https://ahrefs.com/blog/internal-links-for-seo/) from other pages on your website. Google can’t discover these pages through crawling unless they have backlinks from known pages on other sites. Submitting a sitemap partially solves this problem as orphan pages are usually included in sitemaps—at least those generated by a CMS.

## How long does it take for Google to index content?

Google [says](https://developers.google.com/search/docs/advanced/crawling/ask-google-to-recrawl) that crawling can take anywhere from a few days to a few weeks. (Remember that crawling is almost always a prerequisite to indexing.)

In my experience, unless you have a large website, it rarely takes more than a week or two.

But don’t worry if it takes a bit longer; it’s perfectly normal.

## Why isn’t Google indexing my website?

Google won’t always index all of the URLs you submit. Although there are many reasons this can happen, here are a few of the most common:

### 1. You’ve blocked crawling

[Robots.txt](https://ahrefs.com/blog/robots-txt/) is a text file that tells Google which URLs they can and can’t crawl.

For example, this robots.txt file blocks Google from crawling all pages on the website:

```
User-agent: Googlebot
Disallow: /
```

Google will sometimes index URLs even if they can’t crawl them, but it’s quite rare. Preventing crawling also stops Google from obtaining much information about the page in question, so it probably won’t rank even if it’s indexed.

This is another reason to sign up and submit your website through Google Search Console. It actually tells you if pages are excluded from indexing due to crawl blocks in the **Coverage** report.

Here’s how to get to it:

1. Log in to [Google Search Console](https://search.google.com/search-console/about)
2. Choose the correct property
3. Click “Coverage” on the left menu

From here, toggle the “Excluded” tab only and check for these three issues:

- Blocked by robots.txt
- Submitted URL blocked by robots.txt
- [Indexed, though blocked by robots.txt](https://ahrefs.com/blog/indexed-though-blocked-by-robots-txt/)

### 2. You’ve noindexed important pages

If there’s a [meta robots tag or x-robots-header](https://ahrefs.com/blog/meta-robots/) on your page with “noindex” in the content attribute, Google won’t index it.

If Google has crawled your website already, you can check for pages excluded because of noindexing in the **Coverage** report. Just toggle the “Error” and “Excluded” tabs, then check for these two issues:

- Submitted URL marked ‘noindex’
- Excluded by ‘noindex’ tag

If Google hasn’t crawled your website yet, or you just want to keep an eye out for rogue “noindex tags” in the future, sign up for [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) (AWT) and run a free website crawl using [Site Audit](https://ahrefs.com/site-audit). This checks your site for 100+ common SEO issues, including noindexed pages.

### 3. You have low-value pages

Google is unlikely to index pages that don’t hold much value for searchers. In [a tweet from 2018](https://twitter.com/JohnMu/status/948544364090970112), Google’s John Mueller suggests that your website and content should be “awesome and inspiring” for it to be indexed.

If you’ve ruled out technical issues that would prevent indexing, it’s worth asking yourself if that page is truly valuable. If the answer is no, that’s probably why it’s not indexed.

If you feel that the page is low-value and you’re concerned you might have other similar pages, run a free website crawl using [Site Audit](https://ahrefs.com/site-audit) in [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools). This flags up two issues often associated with low-value content:

1. Pages with low word counts
2. Pages that are exact or near-duplicates

You can see the number of URLs with low word counts in the **All issues** report.

Although content doesn’t need to be lengthy to be valuable, pages with super low word counts often aren’t that valuable for search engine users. So it’s worth reviewing these pages manually and making them more useful where necessary.

You can see pages that are exact or near duplicates in the **Duplicate Content** report:

Here’s a good example of two low-value pages that are near-duplicates:

These are empty category pages on an e-commerce site. Because neither of them features any products, they’re not helpful for searchers. They should either be removed or improved.

**Recommended reading:** *[10 Ways to Get Google to Index Your Site](https://ahrefs.com/blog/google-index/)*

## Final thoughts

Even if your site is indexed in Google, it doesn’t necessarily mean that you’ll [rank on the first page of Google](https://ahrefs.com/blog/how-to-get-on-the-first-page-of-google/) for your target keywords. Indexing means you’re in the race, not that you’ll win.

This is where SEO comes in. [SEO](https://ahrefs.com/blog/what-is-seo/) is the practice of optimizing your website to increase its traffic from a search engine’s organic results. In this case: Google.

**If you want to learn more about SEO**, read our [beginner’s guide to SEO](https://ahrefs.com/seo) or [watch this free training course](https://ahrefs.com/academy/seo-training-course).

**If you want to submit your website to other search engines**, read [our full guide to submitting to search engines](https://ahrefs.com/blog/submit-website-to-search-engines/).

**Got questions?** Ping me [on Twitter](https://twitter.com/joshuachardwick?lang=en).
