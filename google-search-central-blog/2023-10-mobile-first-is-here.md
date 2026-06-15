---
title: "Mobile-first indexing has landed - thanks for all your support"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2023-10-mobile-first-is-here"
url: "https://developers.google.com/search/blog/2023/10/mobile-first-is-here"
canonical: "https://developers.google.com/search/blog/2023/10/mobile-first-is-here"
author: "John Mueller, Nir Kalush"
published: "2023-10-31T00:00:00+00:00"
updated: "2023-10-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
fetched_at: "2026-06-14T13:42:55+00:00"
status_code: 200
html_hash: "655cc5913d9e8a919b0ef99ccd7c460b5917f3a7737b71ae508984eb24297516"
clean_word_count: 477
clean_char_count: 3002
---
# Mobile-first indexing has landed - thanks for all your support

It's been a long road, getting from there to here.
We're delighted to announce that the trek to Mobile First Indexing is now complete.

![Googlebot and Crawley celebrating with a red mobile phone](/static/search/blog/images/2023-mfi-googlebot.png)

Google Search started focusing more and more on mobile devices starting in 2015, with the [mobile friendly update](/search/blog/2015/04/rolling-out-mobile-friendly-update).
Then, in 2016, we [started mobile-first crawling and indexing](/search/blog/2016/11/mobile-first-indexing).
This allowed Google Search to index the content that users would see, when they access the website on their mobile phone.
Crawling and indexing as a smartphone was a big change for Google's infrastructure, but also a change for the public web: a mobile web page now needed to be as complete as the corresponding desktop version.

Over the years, mobile web traffic has continued to grow; in some regions, people almost exclusively use their phone to access the internet.
Thank you — site-owners, SEOs, web-developers, designers, and everyone who works on websites — for helping to make the mobile web a success!

## Next steps

We currently know of a very small set of sites which do not work on mobile devices at all.
The error types we've seen there are primarily that the page shows errors to all mobile users, that the mobile version of the site is blocked with robots.txt while the desktop version is allowed for crawling, or that all pages on the mobile site redirect to the homepage.
These are issues that Google can't resolve.
We'll continue to try to crawl these sites with our legacy desktop Googlebot crawler for the time being, and will re-evaluate the list a few times a year.
For more information, check out our [mobile indexing best practices](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing).

Additionally, we'll continue to reduce our crawling with legacy desktop Googlebot as much as possible.
This helps to save resources for site-owners, and for us.

## Search Console changes

With the move to Mobile First Indexing behind us, we're also turning off the indexing crawler information in the [settings page](https://search.google.com/search-console/settings) in [Search Console](https://search.google.com/search-console/).
This information is no longer needed since all websites that work on mobile devices are now being primarily crawled with our mobile crawler.
The [crawl stats report](https://support.google.com/webmasters/answer/9679690) shows how your site is currently being crawled, if you're curious.

![section of a screenshot from Search Console crawl stats, showing the Googlebot type](/static/search/blog/images/2023-mfi-sc.png)

It has been an honor to work together with so many site-owners on this transition, your work on making the web accessible to everyone - and to every crawler - who uses mobile devices is greatly appreciated.
Thank you.
