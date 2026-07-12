---
title: "Google, duplicate content caused by URL parameters, and you"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-09-google-duplicate-content-caused-by-url"
url: "https://developers.google.com/search/blog/2007/09/google-duplicate-content-caused-by-url"
canonical: "https://developers.google.com/search/blog/2007/09/google-duplicate-content-caused-by-url"
author: "Maile Ohye"
published: "2007-09-12T00:00:00+00:00"
updated: "2007-09-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:50:10+00:00"
status_code: 200
html_hash: "5c9e68959a77760a5c386071ee6e7052a449cfe8e4c64d3d330318f043ac8b91"
clean_word_count: 624
clean_char_count: 4080
---
# Google, duplicate content caused by URL parameters, and you

## How can URL parameters, like session IDs or tracking IDs, cause duplicate content?

When user and/or tracking information is stored through URL parameters, duplicate content can
arise because the same page is accessible through numerous URLs. It's what Adam Lasnik referred
to in
"[Deftly Dealing with Duplicate Content](/search/blog/2006/12/deftly-dealing-with-duplicate-content)"
as "store items shown (and—worse yet—linked) via multiple distinct URLs." In the
example below, URL parameters create three URLs which access the same product page.

![example of 3 urls displaying the same content](/static/search/blog/images/import/989a49635c351c2be8cbe7b09df77a43.jpg)

## Why should you care?

When search engines crawl identical content through varied URLs, there may be several negative
effects:

1. Having multiple URLs can dilute link popularity. For example, in the diagram above, rather than
   50 links to your intended display URL, the 50 links may be divided three ways among the three
   distinct URLs.
2. Search results may display user-unfriendly URLs (long URLs with tracking IDs, session IDs)
   - Decreases chances of user selecting the listing
   - Offsets branding efforts

## How we help users and webmasters with duplicate content

We've designed algorithms to help prevent duplicate content from negatively affecting webmasters
and the user experience.

1. When we detect duplicate content, such as through variations caused by URL parameters, we group
   the duplicate URLs into one cluster.
2. We select what we think is the "best" URL to represent the cluster in search results.
3. We then consolidate properties of the URLs in the cluster, such as link popularity, to the
   representative URL.

Consolidating properties from duplicates into one representative URL often provides users with
more accurate search results.

## If you find you have duplicate content as mentioned above, can you help search engines understand your site?

First, no worries, there are many sites on the web that utilize URL parameters and for valid
reasons. But yes, you can help reduce potential problems for search engines by:

- Removing unnecessary URL parameters—keep the URL as clean as possible.
- Submitting a [Sitemap](/search/docs/crawling-indexing/sitemaps/overview)
  with the canonical (that is, representative) version of each URL. While we can't guarantee that
  our algorithms will display the Sitemap's URL in search results, it's helpful to indicate the
  canonical preference.

## How can you design your site to reduce duplicate content?

Because of the way Google handles duplicate content, webmasters need not be overly concerned with
the loss of link popularity or loss of PageRank due to duplication. However, to reduce duplicate
content more broadly, we suggest:

1. When tracking visitor information, use `301` redirects to redirect URLs with parameters such as
   `affiliateID`, `trackingID`, etc. to the canonical version.
2. Use a cookie to set the `affiliateID` and `trackingID` values.

If you follow this guideline, your webserver logs could appear as:

```
127.0.0.1 - - [19/Jun/2007:14:40:45 -0700] "GET /product.php?category=gummy-candy&item=swedish-fish&affiliateid=ABCD HTTP/1.1" 301 -
127.0.0.1 - - [19/Jun/2007:14:40:45 -0700] "GET /product.php?item=swedish-fish HTTP/1.1" 200 74
```

And the session file storing the raw cookie information may look like:

```
category|s:11:"gummy-candy";affiliateid|s:4:"ABCD";
```

Please be aware that if your site uses cookies, your content (such as product pages) should remain
accessible with cookies disabled.

## How can we better assist you in the future?

We recently published ideas from
[SMX Advanced](/search/blog/2007/06/duplicate-content-summit-at-smx)
on how search engines can help webmasters with duplicate content. If you have an opinion on the
topic, please join our conversation in the
[Webmaster Help Group](https://groups.google.com/group/Google_Webmaster_Help-Requests/topics)
(we've already started the thread).
