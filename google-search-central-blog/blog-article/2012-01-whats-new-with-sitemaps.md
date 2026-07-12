---
title: "What's new with Sitemaps"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-01-whats-new-with-sitemaps"
url: "https://developers.google.com/search/blog/2012/01/whats-new-with-sitemaps"
canonical: "https://developers.google.com/search/blog/2012/01/whats-new-with-sitemaps"
author: "Kamila Primke"
published: "2012-01-26T00:00:00+00:00"
updated: "2012-01-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:17:34+00:00"
status_code: 200
html_hash: "8ec42fdf76c7a79038e480f33b2e6328d2d32e46326f852420bc0a863dfc19d8"
clean_word_count: 422
clean_char_count: 2553
---
# What's new with Sitemaps

Sitemaps are a way to tell Google about pages on your site. Webmaster Tools' Sitemaps feature
gives you feedback on your submitted Sitemaps, such as how many Sitemap URLs have been indexed,
or whether your Sitemaps have any errors. Recently, we've added even more information! Let's check
it out:

![View of the Stemaps report in Webmaster Tools](/static/search/blog/images/import/afcc9a962ac21af854966f3299d51193.png)

The Sitemaps page displays details based on content-type. Now statistics from Web, Videos, Images
and News are featured prominently. This lets you see how many items of each type were submitted
(if any), and for some content types, we also show how many items have been indexed. With these
enhancements, the new Sitemaps page replaces the Video Sitemaps Labs feature, which will be
retired.

Another improvement is the ability to test a Sitemap. Unlike an actual submission, testing does
not submit your Sitemap to Google as it only checks it for errors. Testing requires a live fetch
by Googlebot and usually takes a few seconds to complete. Note that the initial testing is not
exhaustive and may not detect all issues; for example, errors that can only be identified once the
URLs are downloaded are not be caught by the test.

In addition to on-the-spot testing, we've got a new way of displaying errors which better exposes
what types of issues a Sitemap contains. Instead of repeating the same kind of error many times
for one Sitemap, errors and warnings are now grouped, and a few examples are given. Likewise, for
Sitemap index files, we've aggregated errors and warnings from the child Sitemaps that the Sitemap
index encloses. No longer will you need to click through each child Sitemap one by one.

Finally, we've changed the way the "Delete" button works. Now, it removes the Sitemap from
Webmaster Tools, both from your account and the accounts of the other owners of the site. Be aware
that a Sitemap may still be read or processed by Google even if you delete it from Webmaster
Tools. For example if you reference a Sitemap in your robots.txt file search engines may still
attempt to process the Sitemap. To truly prevent a Sitemap from being processed, remove the file
from your server or block it via robots.txt.

For more information on Sitemaps in Webmaster Tools and how Sitemaps work, visit our
[documentation about sitemaps](/search/docs/crawling-indexing/sitemaps/overview). If you have
any questions, go to
[Webmaster Help Forum](https://support.google.com/webmasters/community).
