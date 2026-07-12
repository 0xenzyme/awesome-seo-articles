---
title: "Multiple Sitemaps in the same directory"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-10-multiple-sitemaps-in-same-directory"
url: "https://developers.google.com/search/blog/2006/10/multiple-sitemaps-in-same-directory"
canonical: "https://developers.google.com/search/blog/2006/10/multiple-sitemaps-in-same-directory"
author: null
published: "2006-10-09T00:00:00+00:00"
updated: "2006-10-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:46:45+00:00"
status_code: 200
html_hash: "71df22f71b8f59101b14937686939ca80c1971d989ea90885f98d8e92b13e8fd"
clean_word_count: 587
clean_char_count: 3697
---
# Multiple Sitemaps in the same directory

We've gotten a few questions about whether you can put multiple
[Sitemaps](/search/docs/crawling-indexing/sitemaps/overview) in the same directory.
Yes, you can!

You might want to have multiple Sitemap files in a single directory for a number of reasons. For
instance, if you have an auction site, you might want to have a daily Sitemap with new auction
offers and a weekly Sitemap with less time-sensitive URLs. Or you could generate a new Sitemap
every day with new offers, so that the list of Sitemaps grows over time. Either of these
solutions works just fine.

Or, here's another sample scenario: Suppose you're a provider that supports multiple web shops,
and they share a similar URL structure differentiated by a parameter. For example:

```
  https://example.com/stores/home?id=1
  https://example.com/stores/home?id=2
  https://example.com/stores/home?id=3
```

Since they're all in the same directory, it's fine by our rules to put the URLs for all of the
stores into a single Sitemap, under https://example.com/ or https://example.com/stores/. However,
some webmasters may prefer to have separate Sitemaps for each store, such as:

```
  https://example.com/stores/store1_sitemap.xml
  https://example.com/stores/store2_sitemap.xml
  https://example.com/stores/store3_sitemap.xml
```

As long as all URLs listed in the Sitemap are at the same location as the Sitemap or in a sub
directory (in the above example https://example.com/stores/ or perhaps
https://example.com/stores/catalog) it's fine for multiple Sitemaps to live in the same directory
(as many as you want!). The important thing is that Sitemaps not contain URLs from parent
directories or completely different directories—if that happens, we can't be sure that the
submitter controls the URL's directory, so we can't trust the metadata.

The above Sitemaps could also be collected into a single
[Sitemap index file](/search/docs/crawling-indexing/sitemaps/large-sitemaps) and
easily be submitted via Google Webmaster Tools. For example, you could create
https://example.com/stores/sitemap\_index.xml as follows:

```
<?xml version='1.0' encoding='utf-8'?>
<sitemapindex xmlns="https://www.google.com/schemas/sitemap/0.84">
  <sitemap>
    <loc>https://example.com/stores/store1_sitemap.xml</loc>
    <lastmod>2006-10-01T18:23:17+00:00</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/stores/store2_sitemap.xml</loc>
    <lastmod>2006-10-01</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/stores/store3_sitemap.xml</loc>
    <lastmod>2006-10-05</lastmod>
  </sitemap>
</sitemapindex>
```

Then simply [add](/search/docs/crawling-indexing/sitemaps/overview) the index file to your
account, and you'll be able to see any
[errors](https://support.google.com/webmasters/answer/7451001?topic=8497)
for each of the child Sitemaps.

If each store includes more than 50,000 URLs (the maximum number for a single Sitemap), you would
need to have multiple Sitemaps for each store. In that case, you may want to create a Sitemap
index file for each store that lists the Sitemaps for that store. For instance:

```
  https://example.com/stores/store1_sitemapindex.xml
  https://example.com/stores/store2_sitemapindex.xml
  https://example.com/stores/store3_sitemapindex.xml
```

Since Sitemap index files can't contain other index files, you would need to submit each Sitemap
index file to your account separately.

Whether you list all URLs in a single Sitemap or in multiple Sitemaps (in the same directory of
different directories) is simply based on what's easiest for you to maintain. We treat the URLs
equally for each of these methods of organization.
