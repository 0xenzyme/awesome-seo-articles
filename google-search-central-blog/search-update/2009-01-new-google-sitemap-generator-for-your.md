---
title: "A new Google Sitemap Generator for your website"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2009-01-new-google-sitemap-generator-for-your"
url: "https://developers.google.com/search/blog/2009/01/new-google-sitemap-generator-for-your"
canonical: "https://developers.google.com/search/blog/2009/01/new-google-sitemap-generator-for-your"
author: "John Mueller"
published: "2009-01-13T00:00:00+00:00"
updated: "2009-01-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:56:28+00:00"
status_code: 200
html_hash: "4780aa8d580b87c616ce7a14c0c85ac8ec2664c706ed2293dca777f8f1e013f7"
clean_word_count: 481
clean_char_count: 3175
---
# A new Google Sitemap Generator for your website

It's been well over three years since we initially announced the
[Python Sitemap generator](https://code.google.com/p/sitemap-generators/downloads/list)
in
[June 2005](https://googleblog.blogspot.com/2005/06/webmaster-friendly.html).
In this time, we've seen lots of people create great
[third-party sitemap generators](https://code.google.com/p/sitemap-generators/wiki/SitemapGenerators)
to help webmasters create better sitemap files. While most sitemap
generators either crawl websites or list the files on a server, we have created a different kind
of sitemap generator that uses several ways to find URLs on your website and then allows you to
automatically create and maintain different kinds of sitemap files.

![Google Sitemap Generator screenshot of the admin console](/static/search/blog/images/gsg-orig-admin-site-chrome-example.png)

## About Google Sitemap Generator

Our new open-source
[Google Sitemap Generator](https://code.google.com/p/googlesitemapgenerator/)
finds new and modified URLs based on your webserver's traffic, its log
files, or the files found on the server. By combining these methods, Google Sitemap Generator can
be very fast in finding these URLs and calculating relevant metadata, thereby making your sitemap
files as effective as possible. Once Google Sitemap Generator has collected the URLs, it can
create the following [sitemap files](/search/docs/crawling-indexing/sitemaps/overview) for you:

- XML sitemaps for Web Search according to
  the [sitemaps.org](https://www.sitemaps.org/) standard
- Mobile sitemaps for mobile-friendly websites
- Code Search sitemaps for source code that you make available to users

In addition, Google Sitemap Generator can send a
[ping to Google Blog Search](https://www.google.com/help/blogsearch/about_pinging)
for all of your new or modified URLs. You can optionally include the URLs of the sitemap files in
your robots.txt file as well as "ping" the other search engines that support the
[sitemaps.org](https://www.sitemaps.org/) standard.

Sending the URLs to the right sitemap files is simple thanks to the web-based administration
console. This console gives you access to various features that make administration a piece of
cake while maintaining a high level of security by default.

## Getting started

Google Sitemap Generator is a server plug-in that can be installed on both Linux/Apache and
Microsoft IIS Windows-based servers. As with other server-side plug-ins, you will need to have
administrative access to the server to install it. You can find detailed information for the
installation in the
[Google Sitemap Generator documentation](https://code.google.com/archive/p/googlesitemapgenerator/).

We're excited to release Google Sitemap Generator with the source code and hope that this will
encourage more web hosters to include this or similar tools in their hosting packages!

Do you have any questions? You can drop by our
[Help Group for Google Sitemap Generator](https://groups.google.com/group/google-sitemap-generator)
or ask general sitemaps question in our
[Webmaster Help Forum](https://support.google.com/webmasters).
