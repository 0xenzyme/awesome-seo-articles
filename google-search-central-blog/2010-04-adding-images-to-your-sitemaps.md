---
title: "Adding Images to your Sitemaps"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2010-04-adding-images-to-your-sitemaps"
url: "https://developers.google.com/search/blog/2010/04/adding-images-to-your-sitemaps"
canonical: "https://developers.google.com/search/blog/2010/04/adding-images-to-your-sitemaps"
author: "Alkis Evlogimenos, Software Engineer"
published: "2010-04-07T00:00:00+00:00"
updated: "2010-04-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:05:37+00:00"
status_code: 200
html_hash: "01ab4a237d65f51a978c1f10f65add23220b34cb8b19849a53796ca62440aca0"
clean_word_count: 273
clean_char_count: 1751
---
# Adding Images to your Sitemaps

Sitemaps are an invaluable resource for search engines. They can highlight the important content
on a site and allow crawlers to quickly discover it. Images are an important element of many sites
and search engines could equally benefit from knowing which images you consider important. This is
particularly true for images that are only accessible via JavaScript forms, or for pages that
contain many images but only some of which are integral to the page content.

Now you can use a Sitemaps extension to provide Google with exactly this information. For each URL
you list in your Sitemap, you can add additional information about important images that exist on
that page. You don't need to create a new Sitemap, you can just add information on images to the
Sitemap you already use.

Adding images to your Sitemaps is easy. Simply follow the instructions in
[our documentation](/search/docs/crawling-indexing/sitemaps/image-sitemaps) or refer to the
example below:

```
<?xml version="1.0" encoding="UTF-8"?>
  <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
             xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
    <url>
      <loc>https://example.com/sample.html</loc>
      <image:image>
        <image:loc>https://example.com/image.jpg</image:loc>
      </image:image>
    </url>
  </urlset>
```

We index billions of images and see hundreds of millions of image-related queries each day. To
take advantage of that traffic most effectively, take a moment to update your Sitemap file with
information on the images from your site. Let us know in the
[Sitemaps forum](https://support.google.com/webmasters/community/label?lid=401d0e67c19e20e9&hl=en)
if you have any questions.
