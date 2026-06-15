---
title: "Using Sitemap Index Files"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2005-08-using-sitemap-index-files"
url: "https://developers.google.com/search/blog/2005/08/using-sitemap-index-files"
canonical: "https://developers.google.com/search/blog/2005/08/using-sitemap-index-files"
author: "Vanessa Fox"
published: "2005-08-18T00:00:00+00:00"
updated: "2005-08-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:43:34+00:00"
status_code: 200
html_hash: "be7d8a604a05de65d91792d3714d1aebf6764d2d14ae4c15d3d9f05e957f0dd7"
clean_word_count: 554
clean_char_count: 3307
---
# Using Sitemap Index Files

Several of you have asked us, should I submit Sitemaps or Sitemap *indexes* for my site?

If you have a small site, you probably don't need to use a Sitemap index file—you can just
list all of your URLs in one Sitemap.

If you have a larger site, you may want or need to have multiple Sitemaps for your site. In that
case, you can make submitting and tracking easier by listing the Sitemaps in a
[Sitemap index file.](/search/docs/crawling-indexing/sitemaps/large-sitemaps)

You must use multiple Sitemaps for your site when:

- You have more than 50,000 URLs to list. That's the maximum that one Sitemap can include.
- A single Sitemap would be larger than 10MB, uncompressed. That's the maximum size for a Sitemap.

You may want to use multiple Sitemaps for other reasons, to make organization easier. For instance
if:

- You want to store all of your archived URLs in one Sitemap and all of your URLs that change
  frequently in another. This way, when you add new URLs to the Sitemap, you'll have a smaller and
  more manageable file to work with.
- You manage multiple sites that are in subfolders. You might want to create a Sitemap for each
  site and then create a Sitemap index file that lists them in the root. Remember, this method
  works only with subfolders. For example, this Sitemap index file:

  ```
  www.example.com/sitemap_index.xml
  ```

  could list the following Sitemaps:

  ```
  www.example.com/site1/sitemap.xml
  www.example.com/sitemap2/sitemap.xml
  ```

  However, that Sitemap index file could not list the following Sitemaps:

  ```
  site1.example.com/sitemap.xml
  site2.example.com/sitemap.xml
  ```

## Creating an index of Sitemap index files

You can also have an index of Sitemap index files. A Sitemap index file can be a maximum of 10MB
as well, so if you have a really large site, you may have to use this additional organization step
to keep the file sizes to a manageable level. We have a size limitation for Sitemaps and Sitemap
indexes so that when we download the files, we don't overwhelm your bandwidth.

## Compressing your Sitemap index file

Speaking of being considerate of your bandwidth, if you can, you should compress your Sitemaps and
your Sitemap indexes using
[gzip](https://www.google.com/search?q=gz+file). If you're not
familiar with gzip, keep watching this blog. We're putting together some helpful instructions.

If you compress your Sitemap index file, you'll probably want to give it an `.xml.gz`
extension. If you don't compress your Sitemap index file, you'll probably want to give it an
`.xml` extension.

## Submitting your Sitemap index file

So, you've got some individual Sitemaps that you've listed in a Sitemap index file. What now? Just
Sign into Google Sitemaps and submit the
[Sitemap index file](/search/docs/crawling-indexing/sitemaps/build-sitemap). You don't
need to submit individual Sitemaps that are included in the index. Once we've processed your
Sitemap index file, we'll let you know if we found errors in the Sitemap index itself, or in any
of the individual Sitemaps.

If you make changes to a Sitemap included in a Sitemap index file you've submitted, just change
the `lastmod` date for that Sitemap in your index. During this beta period, you can
resubmit the Sitemap index file.
