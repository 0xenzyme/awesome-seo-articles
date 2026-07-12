---
title: "When your site changes"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2005-10-when-your-site-changes"
url: "https://developers.google.com/search/blog/2005/10/when-your-site-changes"
canonical: "https://developers.google.com/search/blog/2005/10/when-your-site-changes"
author: "Vanessa Fox"
published: "2005-10-26T00:00:00+00:00"
updated: "2005-10-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:44:00+00:00"
status_code: 200
html_hash: "7feb812cf331e631dd9cfba7439be64d31a9a1007eb6ba50f2bff05bce0412cc"
clean_word_count: 300
clean_char_count: 1820
---
# When your site changes

Here's another question we've gotten. If you have a question about Sitemaps, let us know by
posting in the
[Sitemaps Google Group](https://support.google.com/webmasters/community).

## I've submitted a Sitemap for my site. What should I do when my site changes?

If you add pages to your site, you can let us know in several different ways:

- **Resubmit your Sitemap:** You can add the URLs to your existing Sitemap and then
  resubmit it either by using your Google Account or by
  [sending us a ping (HTTP request)](/search/docs/crawling-indexing/sitemaps/overview#ping).
- **Create a new Sitemap:** You can create a new Sitemap with only the new URLs and
  [submit](/search/docs/crawling-indexing/sitemaps/build-sitemap#addsitemap) that
  separately using your Google Account.
- **Use a Sitemap index file:** You can create a new Sitemap with only the new URLs
  and then list both the original Sitemap and the new Sitemap in a
  [Sitemap index file](/search/docs/crawling-indexing/sitemaps/overview#sitemapFileRequirements).
  Then, you can simply submit the Sitemap index file. If you often add pages to your site, you
  can periodically create a new Sitemap with new URLs, add the new Sitemap to the Sitemap index
  file, and resubmit the Sitemap index file.

Note that if you ping us to let us know about changes to your Sitemap, make sure that you submit
that Sitemap using your Google Account at least once. The **Last Submitted** date
shown in your Google Sitemaps Account lists the date you last submitted the Sitemap manually,
but if you receive a status `200 (OK)` from the ping, we received it successfully.

If you've deleted pages from your site, you can delete those pages from your Sitemap and then
resubmit it (either manually through your Google Account or by pinging us).
