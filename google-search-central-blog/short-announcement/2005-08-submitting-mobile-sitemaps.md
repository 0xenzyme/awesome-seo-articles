---
title: "Submitting mobile Sitemaps"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2005-08-submitting-mobile-sitemaps"
url: "https://developers.google.com/search/blog/2005/08/submitting-mobile-sitemaps"
canonical: "https://developers.google.com/search/blog/2005/08/submitting-mobile-sitemaps"
author: "Vanessa Fox"
published: "2005-08-31T00:00:00+00:00"
updated: "2005-08-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:43:32+00:00"
status_code: 200
html_hash: "17fc43270d074a21c4432ace0a0f07d6833d0a32b88ef106e31a4d8458ba90c0"
clean_word_count: 318
clean_char_count: 2011
---
# Submitting mobile Sitemaps

If you've created and submitted Sitemaps for your non-mobile pages, or just want to submit a
mobile Sitemap for the first time, here are a few helpful tips to help you get started:

## Identify your mobile Sitemaps content

- If you have content other than XHTML mobile profile, WML, and cHTML, you should create a
  separate non-mobile Sitemap for those and submit it using the Add a Sitemap page.
- If your site serves multiple mobile markup languages, you should create a separate mobile
  Sitemap for each markup language.
- If you have URLs that serve multiple markup languages, you should include those URLs in each
  mobile Sitemap that applies. For instance, if you have a URL that serves both XHTML and WML
  content, include that URL in two mobile Sitemaps, one for each markup language.
- If you have a large site and use Sitemap index files to manage a large number of mobile
  Sitemaps, make sure that each Sitemap index file only includes mobile Sitemaps for one markup
  language.

## Create your mobile Sitemaps

- You can [create mobile Sitemaps](/search/docs/crawling-indexing/sitemaps/overview) in
  the same way as other Sitemaps. The only format not supported is OAI-PMH.
- If you are submitting a syndication feed, and the URLs listed in that feed serve multiple markup
  languages, decide which markup language fits best. You can't submit the syndication feed
  multiple times, each for a different markup language, since each Sitemap (within the same
  directory) must have a unique name.

## Submit your mobile Sitemaps

- Once you've created your Sitemap, log in to your Google Account and
  [submit it](/search/docs/crawling-indexing/sitemaps/build-sitemap#addsitemap) using
  the
  [Add a Mobile Sitemap page](https://support.google.com/webmasters/answer/7451001).
- Specify the markup language that the URLs listed in the mobile Sitemap serve.
- Once you've submitted the mobile Sitemap it will be listed on your My Sitemaps page as a
  "Mobile" type.
