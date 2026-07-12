---
title: "Supporting AVIF in Google Search"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2024-08-happy-avifriday"
url: "https://developers.google.com/search/blog/2024/08/happy-avifriday"
canonical: "https://developers.google.com/search/blog/2024/08/happy-avifriday"
author: "John Mueller"
published: "2024-08-30T00:00:00+00:00"
updated: "2024-08-30T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:44:01+00:00"
status_code: 200
html_hash: "a7ccd7f82ae626b662e42236bdd547b94486f41adf1fef649c7072f05436bf36"
clean_word_count: 272
clean_char_count: 1731
---
# Supporting AVIF in Google Search

Over the recent years, AVIF has become one of the most commonly used image formats on the web.
We're happy to announce that AVIF is now a [supported file type](/search/docs/crawling-indexing/indexable-file-types)
in Google Search, for Google Images as well as any place that uses images in Google Search. You
don't need to do anything special to have your AVIF files indexed by Google.

![Googlebot and Crawley checking to see if they are AVIF compatible](/search/blog/images/googlebot-crawley-binoculars.avif)

[AVIF](https://en.wikipedia.org/wiki/AVIF) is an open image file
format based on the AV1 video compression standard. It's supported by all major web browsers, and
images in AVIF image file format are supported by a variety of services and platforms on the web,
including [WordPress](https://make.wordpress.org/core/2024/02/23/wordpress-6-5-adds-avif-support/),
[Joomla](https://issues.joomla.org/tracker/joomla-cms/41381),
and [CloudFlare](https://blog.cloudflare.com/generate-avif-images-with-image-resizing/).
It's not recommended to blindly make sweeping changes to images across a website: take the time
you need to evaluate which format works best for your specific needs. If you do choose to change
image file formats for some of your images, and if this results in changes to filenames or
extensions, make sure to set up [server-side redirects](/search/docs/crawling-indexing/301-redirects#serverside).

If you're curious about other aspects involved with optimizing SEO for your site's images, check
out our [guide to Image SEO](/search/docs/appearance/google-images). If you have more
questions, let us know in the [Search Central help community](https://goo.gle/sc-forum).
