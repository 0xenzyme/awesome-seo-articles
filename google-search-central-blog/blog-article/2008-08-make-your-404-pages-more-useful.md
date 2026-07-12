---
title: "Make your 404 pages more useful"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-08-make-your-404-pages-more-useful"
url: "https://developers.google.com/search/blog/2008/08/make-your-404-pages-more-useful"
canonical: "https://developers.google.com/search/blog/2008/08/make-your-404-pages-more-useful"
author: "Written by Sahala Swenson, Webmaster Tools team"
published: "2008-08-19T00:00:00+00:00"
updated: "2008-08-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:53:50+00:00"
status_code: 200
html_hash: "36b3a3485dd2b5d3d68fff5b986ba7ba598a8969ed88a7c0f0d204572cfc475e"
clean_word_count: 476
clean_char_count: 2977
---
# Make your 404 pages more useful

Your visitors may stumble into a
[`404` "Not found"](https://google.com/not-very+found)
page on your website for a variety of reasons:

- A mistyped URL, or a copy-and-paste mistake
- Broken or truncated links on web pages or in an email message
- Moved or deleted content

Confronted by a `404` page, they may then attempt to manually correct the URL, click
the back button, or even navigate away from your site. As hinted in an
[earlier post](/search/blog/2008/08/farewell-to-soft-404s)
for
["`404` week at Webmaster Central"](/search/blog/2008/08/its-404-week-at-webmaster-central),
there are various ways to help your visitors get out of the dead-end situation. In our quest to
make `404` pages more useful, we've just added a section in
[Webmaster Tools](https://search.google.com/search-console)
called "Enhance `404` pages". If you've created a
[custom `404` page](/search/docs/crawling-indexing/http-network-errors#pagegone)
this allows you to embed a widget in your `404` page that helps your visitors find what
they're looking for by providing suggestions based on the incorrect URL.

![custom 404 page widget generator in webmaster tools](/static/search/blog/images/import/325c0f47da567284a78bb687a02a4626.png)

Example: Jamie receives the link `www.example.com/activities/adventurecruise.html`
in an email message. Because of formatting due to a bad email client, the URL is truncated to
`www.example.com/activities/adventur`. As a result it returns a `404` page.
With the `404` widget added, however, she could instead see the following:

![example page where the custom 404 widget generates useful suggestions for the user](/static/search/blog/images/import/6df0b767a53aa02372183fccc4c356d5.png)

In addition to attempting to correct the URL, the `404` widget also suggests the
following, if available:

- a link to the parent subdirectory
- a sitemap webpage
- site search query suggestions and search box

How do you add the widget? Visit the "Enhance `404` pages" section in Webmaster Tools,
which allows you to generate a JavaScript snippet. You can then copy and paste this into your
custom `404` page's code. As always, don't forget to
[return a proper `404` code](/search/blog/2008/08/farewell-to-soft-404s).

Can you change the way it looks? Sure. We leave the HTML unstyled initially, but you can edit the
CSS block that we've included. For more information, check out our
[guide on how to customize the look of your `404` widget](https://www.google.com/support/webmasters/bin/answer.py?answer=100044&hl=en).

This feature is currently experimental—we might not provide corrections and suggestions for
your site but we'll be working to improve the coverage. In the meantime, let us know what you
think in the comments below or in our
[group discussion](https://groups.google.com/group/Google_Webmaster_Help-Indexing/browse_thread/thread/8043e56a67baa401).
Thanks for helping us make the Internet a more friendly place!
