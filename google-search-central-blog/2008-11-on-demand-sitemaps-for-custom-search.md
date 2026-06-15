---
title: "On-Demand Sitemaps for Custom Search"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-11-on-demand-sitemaps-for-custom-search"
url: "https://developers.google.com/search/blog/2008/11/on-demand-sitemaps-for-custom-search"
canonical: "https://developers.google.com/search/blog/2008/11/on-demand-sitemaps-for-custom-search"
author: "Written by Rajat Mukherjee, Group Product Manager, Search"
published: "2008-11-13T00:00:00+00:00"
updated: "2008-11-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:55:46+00:00"
status_code: 200
html_hash: "86928c56911bcd203c2398f56ade8cfcf7e1e1a013b5d05662b762fa48df021c"
clean_word_count: 554
clean_char_count: 3531
---
# On-Demand Sitemaps for Custom Search

Since we
[launched enhanced indexing](/search/blog/2008/05/sitemaps-offer-better-coverage-for-your)
with the
[Custom Search platform](https://www.google.com/cse)
earlier this year, webmasters who submit
[Sitemaps](/search/docs/crawling-indexing/sitemaps/overview) to Webmaster Tools get special
treatment: Custom Search recognizes the submitted Sitemaps and indexes URLs from these Sitemaps
into a separate index for higher quality Custom Search results. We analyze your Custom Search
Engines (CSEs), pick up the appropriate Sitemaps, and figure out which URLs are relevant for your
engines for enhanced indexing. You get the *dual benefit* of better discovery for Google.com
and more comprehensive coverage in your own CSEs.

Today, we're taking another step towards improving your experience with Google webmaster services
with the launch of
[On-Demand Indexing](https://googlecustomsearch.blogspot.com/2008/11/on-demand-indexing-for-fast-moving-web.html)
in Custom Search. With On-Demand Indexing, you can now tell us about the pages on your websites
that are new, or that are important and have changed, and Custom Search will instantly schedule
them for crawl, and index and serve them in your CSEs usually within 24 hours, often much faster.

How do you tell us about these URLs? You guessed it... provide a Sitemap to Webmaster Tools,
like you always do, and tell Custom Search about it. Just go to the
[CSE control panel](https://www.google.com/coop/manage/cse/),
click on the Indexing tab, select your On-Demand Sitemap, and click the "Index Now" button. You
can tell us which of these URLs are most important to you via the `priority` and
`lastmod` attributes that you provide in your Sitemap. Each CSE has a number of pages
allocated within the On-Demand Index, and with these attributes, you can us which are most
important for indexing. If you need greater
[allocation](https://www.google.com/support/customsearch/bin/topic.py?topic=16792)
in the On-Demand index, as well as more customization controls,
[Google Site Search](https://www.google.com/sitesearch)
provides a range of options.

![Sitemaps submission in Webmaster Tools](/static/search/blog/images/import/fb6e32b95c3a1906ea43343b8fa3b9a0.png)

Some important points to remember:

1. You only need to submit your Sitemaps once in Webmaster Tools. Custom Search will automatically
   list the Sitemaps submitted via Webmaster Tools and you can decide which Sitemap to select for
   On-Demand Indexing.
2. Your Sitemap needs to be for a website
   [verified in Webmaster Tools](https://support.google.com/webmasters/answer/34592),
   so that we can verify ownership of the right URLs.
3. In order for us to index these additional pages, our crawlers must be able to crawl them. You
   can use "Webmaster Tools > Crawl Errors
   >
   [URLs restricted by robots.txt](https://www.google.com/support/webmasters/bin/answer.py?answer=35235)"
   or check your robots.txt file to ensure that you're not
   [blocking us from crawling](/search/docs/crawling-indexing/robots/intro) these pages.
4. Submitting pages for On-Demand Indexing will not make them appear any faster in the main Google
   index, or impact ranking on Google.com.

We hope you'll use this feature to inform us regularly of the most important changes on your
sites, so we can respond quickly and get those pages indexed in your CSE. As always, we're always
listening for your
[feedback on Custom Search](https://groups.google.com/group/google-custom-search).
