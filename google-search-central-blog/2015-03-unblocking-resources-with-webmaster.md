---
title: "Unblocking resources with Webmaster Tools"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2015-03-unblocking-resources-with-webmaster"
url: "https://developers.google.com/search/blog/2015/03/unblocking-resources-with-webmaster"
canonical: "https://developers.google.com/search/blog/2015/03/unblocking-resources-with-webmaster"
author: "John Mueller"
published: "2015-03-11T00:00:00+00:00"
updated: "2015-03-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:26:27+00:00"
status_code: 200
html_hash: "31b145c19575d2884723b79b2b86c0ffc98e7e27d1a0c13a67c64ac984e63d86"
clean_word_count: 319
clean_char_count: 2000
---
# Unblocking resources with Webmaster Tools

Webmasters often use linked images, CSS, and JavaScript files in web pages to make them pretty and
functional. If these resources are blocked from crawling, then Googlebot can't use them when it
renders those pages for Search. Google Webmaster Tools now includes a
[Blocked Resources Report](https://support.google.com/webmasters/answer/6153277)
to help you find and resolve these kinds of issues.

![](/static/search/blog/images/import/87911a257f9d81fa1e41495abcca717b.png)

This report starts with the names of the hosts from which your site is using blocked resources
such as JavaScript, CSS, and images. Clicking on the rows gives you the list of blocked resources
and then the pages that embed them, guiding you through the steps to diagnose and resolve how
we're able to crawl and index the page's content.

An update to
[Fetch and Render](https://support.google.com/webmasters/answer/6066467)
shows how these blocked resources matter. When you request a URL be fetched and rendered, it now
shows screenshots rendered both as Googlebot and as a typical user. This makes it easier to
recognize the issues that significantly influence why your pages are seen differently by
Googlebot.

Webmaster Tools attempts to show you only the hosts that you might have influence over, so at the
moment, we won't show hosts that are used by many different sites (such as popular analytics
services). Because it can be time-consuming (usually not for technical reasons!) to update all
robots.txt files, we recommend starting with the resources that make the most important visual
difference when blocked. Our
[Help Center article](https://support.google.com/webmasters/answer/6153277)
has more information on the steps involved.

We hope this new feature makes it easier for you to spot and then unblock resources used by your
website! Should you have any questions, you can drop by our
[webmaster help forums](https://support.google.com/webmasters/go/community).
