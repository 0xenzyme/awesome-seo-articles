---
title: "Bye Bye Preferred Domain setting"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2019-06-bye-bye-preferred-domain-setting"
url: "https://developers.google.com/search/blog/2019/06/bye-bye-preferred-domain-setting"
canonical: "https://developers.google.com/search/blog/2019/06/bye-bye-preferred-domain-setting"
author: "Daniel Waisberg"
published: "2019-06-18T00:00:00+00:00"
updated: "2019-06-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:34:25+00:00"
status_code: 200
html_hash: "ce33aa328cf854701e6380d99e18425c4f4c70f3649b165c141f2ad02b873ab9"
clean_word_count: 232
clean_char_count: 1480
---
# Bye Bye Preferred Domain setting

As we progress with
[the migration](/search/blog/2018/01/introducing-new-search-console)
to the new Search Console experience, we will be saying farewell to one of our settings: preferred
domain.

![the Search Console preferred domain setting](/static/search/blog/images/import/0b1b7af2db53ef376cc98a549b00e7d9.png)

It's common for a website to have the same content on multiple URLs. For example, it might have
the same content on `https://example.com/` as on
`https://www.example.com/index.html`. To make things easier, when our
systems recognize that, we'll pick one URL as the "canonical" for Search. You can still tell us
your preference in multiple ways if there's something specific you want us to pick (see
paragraph below). But if you don't have a preference, we'll choose the best option we find. Note
that with the deprecation we will no longer use any existing Search Console preferred domain
configuration.

You can find detailed explanations on how to tell us your preference in the
[Consolidate duplicate URLs](/search/docs/crawling-indexing/consolidate-duplicate-urls)
help center article. Here are some of the options available to you:

1. Use `rel="canonical"` link tag on HTML pages
2. Use `rel="canonical"` HTTP header
3. Use a sitemap
4. Use `301` redirects for retired URLs

Send us any feedback either through
[Twitter](https://twitter.com/googlesearchc) or
[our forum](https://support.google.com/webmasters/community).
