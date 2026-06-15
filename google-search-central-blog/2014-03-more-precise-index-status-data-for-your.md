---
title: "More Precise Index Status Data for Your Site Variations"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-03-more-precise-index-status-data-for-your"
url: "https://developers.google.com/search/blog/2014/03/more-precise-index-status-data-for-your"
canonical: "https://developers.google.com/search/blog/2014/03/more-precise-index-status-data-for-your"
author: "Zineb Ait Bahajji"
published: "2014-03-31T00:00:00+00:00"
updated: "2014-03-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:24:02+00:00"
status_code: 200
html_hash: "8bf8e302dfc999d72266cdf7d8d53ddf7f94f2878ef1065ccd14d8fb153662e9"
clean_word_count: 583
clean_char_count: 3740
---
# More Precise Index Status Data for Your Site Variations

The Google Webmaster Tools
[Index Status](https://support.google.com/webmasters/answer/2642366)
feature reports how many pages on your site are indexed by Google. In the past, we didn't show
index status data for HTTPS websites independently, but rather we included everything in the
HTTP site's report. In the last months, we've heard from you that you'd like to use Webmaster
Tools to track your indexed URLs for sections of your website, including the parts that use
HTTPS.

We've seen that nearly 10% of all URLs already use a secure connection to transfer data via
[HTTPS](https://en.wikipedia.org/wiki/HTTP_Secure), and we hope to see
more webmasters move their websites from HTTP to HTTPS in the future. We're happy to announce a
refinement in the way your site's index status data is displayed in Webmaster Tools: the Index
Status feature now tracks your site's indexed URLs for each protocol (HTTP and HTTPS) as well as
for verified subdirectories.

This makes it easy for you to monitor different sections of your site. For example, the following
URLs each show their own data in Webmaster Tools Index Status report, provided they are verified
separately:

|  |  |
| --- | --- |
| HTTP | HTTPS |
| https://www.example.com/ | https://www.example.com/ |
| https://example.com | https://example.com |
| https://www.example.com/folder/ | https://www.example.com/folder/ |
| https://example.com/folder/ | https://example.com/folder/ |

The refined data will be visible for webmasters whose site's URLs are on HTTPS or who have
subdirectories verified, such as `https://example.com/folder/`. Data for
subdirectories will be included in the higher-level verified sites on the same hostname and
protocol.

If you have a website on HTTPS or if some of your content is indexed under different
subdomains, you will see a change in the corresponding Index Status reports. The screenshots
below illustrate the changes that you may see on your HTTP and HTTPS sites' Index Status graphs
for instance:

![HTTP site's Index Status showing drop](/static/search/blog/images/import/04d8f3f32775d1ee1721879d0fafaca9.png)
![HTTPS site's Index Status showing increase](/static/search/blog/images/import/d02a61836b8de31083bb6da246b99ef0.png)

An "Update" annotation has been added to the Index Status graph for March 9th, showing when we
started collecting this data. This change does not affect the way we index your URLs, nor does
it have an impact on the overall number of URLs indexed on your domain. It is a change that
only affects the reporting of data in Webmaster Tools user interface.

In order to see your data correctly, you will need to
[verify](https://support.google.com/webmasters/topic/4564314)
all existing variants of your site (www., non-www., HTTPS, subdirectories, subdomains) in
Google Webmaster Tools. We recommend that your preferred domains and
[canonical URLs](/search/docs/crawling-indexing/consolidate-duplicate-urls) are
configured accordingly.

Note that if you wish to
[submit a Sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap), you will need to do
so for the preferred variant of your website, using the corresponding URLs.
[Robots.txt](/search/docs/crawling-indexing/robots/intro) files are also read separately for
each protocol and hostname.

We hope that you'll find this update useful, and that it'll help you monitor, identify and fix
indexing problems with your website. You can find additional details in our Index Status
[Help Center article](https://support.google.com/webmasters/answer/2642366).
As usual, if you have any questions, don't hesitate to ask in our webmaster
[Help Forum](https://support.google.com/webmasters/community/).
