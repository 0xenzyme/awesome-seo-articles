---
title: "An update to the Webmaster Tools API"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2014-09-an-update-to-webmaster-tools-api"
url: "https://developers.google.com/search/blog/2014/09/an-update-to-webmaster-tools-api"
canonical: "https://developers.google.com/search/blog/2014/09/an-update-to-webmaster-tools-api"
author: "John Mueller"
published: "2014-09-11T00:00:00+00:00"
updated: "2014-09-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:25:22+00:00"
status_code: 200
html_hash: "b13bd8a92007f718087c440b2a425e180dbd3fc1264a6b98048a7238fb5a837b"
clean_word_count: 218
clean_char_count: 1365
---
# An update to the Webmaster Tools API

Over the summer the Webmaster Tools team has been cooking up an update to the
[Webmaster Tools API](/webmaster-tools). The new API is consistent
with other Google APIs, makes it easier to authenticate for apps or web-services, and provides
access to some of the main features of Webmaster Tools.

If you've used other Google APIs, getting started with the new Webmaster Tools API will be easy!
We have examples for
[Python](/webmaster-tools/v3/quickstart/quickstart-python),
[Java](/webmaster-tools/v3/quickstart/quickstart-java), as well as
[OACurl](/webmaster-tools/v3/quickstart/quickstart-oacurl) (for fans
of command lines).

This API allows you to:

- list, add, or remove sites from your account (you can currently have up to 500 sites in your
  account)
- list, add, or remove sitemaps for your websites
- get warning, error, and indexed counts for individual sitemaps
- get a time-series of all kinds of crawl errors for your site
- list crawl error samples for specific types of errors
- mark individual crawl errors as "fixed" (this doesn't change how they're processed, but can help
  simplify the UI for you)

We'd love to see what you're building with our APIs! Should you have any questions about the usage
of the API, you can post in our
[help forum](https://support.google.com/webmasters/community) as well.
