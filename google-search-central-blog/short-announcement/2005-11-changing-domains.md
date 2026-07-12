---
title: "Changing domains"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2005-11-changing-domains"
url: "https://developers.google.com/search/blog/2005/11/changing-domains"
canonical: "https://developers.google.com/search/blog/2005/11/changing-domains"
author: "Vanessa Fox"
published: "2005-11-11T00:00:00+00:00"
updated: "2005-11-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:44:02+00:00"
status_code: 200
html_hash: "fd999da8b0f88fc55fdf7fa865c201742513fd0b56aa01a40d3fd113bbce3de4"
clean_word_count: 179
clean_char_count: 990
---
# Changing domains

From our
[Google Group](https://support.google.com/webmasters/community):

**I've moved my site to a new domain. Can I submit a Sitemap to tell you to index the new
site rather than the old site?**

Submitting a Sitemap for the new site is a great first step, because that helps us learn about
the new pages right away. Make sure you place the new Sitemap in the root directory of the new
site as the Sitemap must be located on the same domain as the site URLs contained in it.

Another important thing to do is redirect visitors from the old site to the new one. Put a
`301` (permanent) redirect on every page of the old site to point to the corresponding
page on the new site.

You can find out more about `301` HTTP redirects from
[RFC-2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.2)
and you can learn more about how to make the site move a smooth one from our
[Google Help Center](/search/docs/crawling-indexing/site-move-with-url-changes).
