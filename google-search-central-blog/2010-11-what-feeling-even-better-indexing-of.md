---
title: "What a feeling! Even better indexing of SWF content"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-11-what-feeling-even-better-indexing-of"
url: "https://developers.google.com/search/blog/2010/11/what-feeling-even-better-indexing-of"
canonical: "https://developers.google.com/search/blog/2010/11/what-feeling-even-better-indexing-of"
author: "Written by Jifeng Situ and Sverre Sundsdal, Software Engineers"
published: "2010-11-12T00:00:00+00:00"
updated: "2010-11-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:10:08+00:00"
status_code: 200
html_hash: "0afb9debc417cfb339ecfab2043da50913f0d73e32cbdcf8344c376979927d18"
clean_word_count: 435
clean_char_count: 2667
---
# What a feeling! Even better indexing of SWF content

We often get questions from webmasters about how we index content designed for Flash Player, so
we wanted to take a moment to update you on some of our latest progress.

About two years ago we announced that through a collaboration with Adobe we had
[significantly improved](/search/blog/2008/06/improved-flash-indexing)
Google's capability to index Flash technology based content. Last year we followed up with an
announcement that we had added
[external resource loading](/search/blog/2009/06/flash-indexing-with-external-resource)
to our SWF indexing capabilities. This work has allowed us to index all kinds of textual content
in SWF files, from Flash buttons and menus to self-contained Flash technology based websites.
Currently almost any text a user can see as they interact with a SWF file on your site can be
indexed by Googlebot and used to generate a snippet or match query terms in Google searches.
Additionally, Googlebot can also discover URLs in SWF files and follow those links, so if your
SWF content contains links to pages inside your website, Google may be able to crawl and index
those pages as well.

Last month we expanded our SWF indexing capabilities thanks to our continued collaboration with
Adobe and a new library that is more robust and compatible with features supported by Flash
Player 10.1. Additionally, thanks to improvements in the way we handle JavaScript, we are also now
significantly better at recognizing and indexing sites that use JavaScript to embed SWF content.
Finally, we have made improvements in our video indexing technology, resulting in better detection
of when a page has a video and better extraction of metadata such as alternate thumbnails from
Flash technology based videos. All in all, our SWF indexing technology now allows us to see
content from SWF files on hundreds of millions of pages across the web.

While we've made great progress indexing SWF content over the past few years, we're not done yet.
We are continuing to work on our ability to index deep linking (content within a Flash technology
based application that is linked to from the same application) as well as further improving
indexing of SWF files executed through JavaScript. You can help us improve these capabilities by
creating unique links for each page that is linked from within a single Flash object and by
submitting a [Sitemap](/search/docs/crawling-indexing/sitemaps/overview) through
[Google Webmaster Tools](https://search.google.com/search-console).

We're excited about the progress we've made so far and we look forward to keeping you updated
about further progress.
