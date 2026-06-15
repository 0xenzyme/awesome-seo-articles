---
title: "Sitemaps: One file, many content types"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-06-sitemaps-one-file-many-content-types"
url: "https://developers.google.com/search/blog/2010/06/sitemaps-one-file-many-content-types"
canonical: "https://developers.google.com/search/blog/2010/06/sitemaps-one-file-many-content-types"
author: "Jonathan Simon"
published: "2010-06-29T00:00:00+00:00"
updated: "2010-06-29T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:07:22+00:00"
status_code: 200
html_hash: "84a51ab59e99e663e866ef64b046f11e8f3d259aafb09aaa4ddb494315a60fdf"
clean_word_count: 376
clean_char_count: 2557
---
# Sitemaps: One file, many content types

Have you ever wanted to submit your various content types (video, images, etc.) in one
[Sitemap](/search/docs/crawling-indexing/sitemaps/overview)?
Now you can! If your site contains videos, images, mobile URLs, code or geo information, you can
now create—and submit—a Sitemap with all the information.

Site owners have been leveraging Sitemaps to let Google know about their sites' content since
Sitemaps were first introduced in 2005. Since that time additional
[specialized Sitemap formats](/search/docs/crawling-indexing/sitemaps/overview)
have been introduced to better accommodate video, images, mobile, code or geographic content.
With the increasing number of specialized formats, we'd like to make it easier for you by
supporting Sitemaps that can include multiple content types in the same file.

The structure of a Sitemap with multiple content types is similar to a standard Sitemap, with the
additional ability to contain URLs referencing different content types. Here's an example of a
Sitemap that contains a reference to a standard web page for Web search, image content for Image
search and a video reference to be included in Video search:

```
<?xml version='1.0' encoding='utf-8'?>
  <urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9"
             xmlns:image="https://www.google.com/schemas/sitemap-image/1.1"
             xmlns:video="https://www.google.com/schemas/sitemap-video/1.1">
  <url>
    <loc>https://example.com/foo.html</loc>
    <image:image>
      <image:loc>https://example.com/image.jpg</image:loc>
    </image:image>
    <video:video>
      <video:content_loc>https://example.com/videoABC.flv</video:content_loc>
      <video:title>Grilling tofu for summer</video:title>
    </video:video>
  </url>
</urlset>
```

Here's an example of what you'll see in
[Webmaster Tools](https://search.google.com/search-console)
when a Sitemap containing multiple content types is submitted:

![sitemap feature in webmaster tools identifies multiple sitemap extensions for a single sitemap](/static/search/blog/images/import/4107cdcc02ced5dafebac7eff424e84e.png)

We hope the capability to include multiple content types in one Sitemap simplifies your Sitemap
submission. The rest of the
[Sitemap rules](/search/docs/crawling-indexing/sitemaps/build-sitemap),
like 50,000 max URLs in one file and the 10MB uncompressed file size limit, still apply. If you
have questions or other feedback, please visit the
[Webmaster Help Forum](https://support.google.com/webmasters/community).
