---
title: "Improving things behind the scenes"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-03-improving-things-behind-scenes"
url: "https://developers.google.com/search/blog/2006/03/improving-things-behind-scenes"
canonical: "https://developers.google.com/search/blog/2006/03/improving-things-behind-scenes"
author: "Vanessa Fox"
published: "2006-03-15T00:00:00+00:00"
updated: "2006-03-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:44:58+00:00"
status_code: 200
html_hash: "241a5ecb6132c4a29bd19ba19a9d693ee4a45227000b618cecd69973f6143d1a"
clean_word_count: 285
clean_char_count: 1734
---
# Improving things behind the scenes

We've just made some enhancements to the infrastructure that processes Sitemaps. You shouldn't
notice many changes, although you may see new and more
[detailed error messages](https://support.google.com/webmasters/answer/7451001)
for your Sitemaps. If you see a different error message than you've seen before, you can click on
it to view more information about it.

This change may cause some Sitemaps that used to have a status of OK to display an error message.
This is because we've enhanced our reporting to provide error information that wasn't available
to you before. For instance, if you see an "Invalid file format" error, make sure that you've
declared the namespace in your Sitemap file correctly and that the
[header matches the examples we provide](/search/docs/crawling-indexing/sitemaps/build-sitemap#xml)
in our documentation.

As part of this change, you can no longer list
[Sitemap index files](/search/docs/crawling-indexing/sitemaps/large-sitemaps)
within Sitemap index files. Each Sitemap index file can list only Sitemaps. Remember that you can
list up to 1,000 Sitemaps in each Sitemap index file. If you have more than 1,000 Sitemaps for a
site, you can submit multiple Sitemap index files.

We've also changed the verification
[error message](/search/blog/2006/03/if-you-see-we-couldnt-find-your)
we talked about in a recent blog post. If you request verification and we receive a status other
than `200` or `404` when we try to access a non-existent file on your site,
you'll now see an "HTTP error".

We expect this change to be a smooth one, but please let us know in our
[Google Group](https://support.google.com/webmasters/community)
if you experience any trouble.
