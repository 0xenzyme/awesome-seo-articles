---
title: "Introducing Sitemaps for Google News"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-11-introducing-sitemaps-for-google-news"
url: "https://developers.google.com/search/blog/2006/11/introducing-sitemaps-for-google-news"
canonical: "https://developers.google.com/search/blog/2006/11/introducing-sitemaps-for-google-news"
author: null
published: "2006-11-20T00:00:00+00:00"
updated: "2006-11-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:46:55+00:00"
status_code: 200
html_hash: "f2a32b29aa2b8d93324bb6eba385dfb40671e0224dfb40a3ac2be7a65fd1b261"
clean_word_count: 377
clean_char_count: 2361
---
# Introducing Sitemaps for Google News

Good news for webmasters of English-language news sites: If your site is currently included in
[Google News](https://news.google.com/), you can now create News
Sitemaps that tell us exactly which articles to crawl for inclusion in Google News. In addition,
you can access crawl errors, which tell you if there were any problems crawling the articles in
your News Sitemaps, or, for that matter, any articles on your site that Google News reaches
through its normal crawl.

Freshness is important for news, so we recrawl all News Sitemaps frequently. The
[News Sitemaps XML definition](/search/docs/crawling-indexing/sitemaps/news-sitemap)
lets you specify a publication date and time for each article to help us process fresh articles in
timely fashion. You can also specify keywords for each article to inform the placement of the
articles into sections on Google News.

If your English-language news site is currently included in Google News, the news features are
automatically enabled in Webmaster Tools; just add the site to your account. Here's how the new
summary page will look:

![webmaster tools summary page](/static/search/blog/images/import/915248b6bb7fa6ae132c02fe0775f279.jpg)

The presence of the **News crawl** link on the left indicates that the news features are
enabled. A few things to note:

- You will only have the news features enabled if your site is currently included in Google News.
  If it's not, you can
  [request inclusion](https://www.google.com/support/news_pub/bin/answer.py?answer=40787).
- In most cases, you should
  [add the site](https://support.google.com/webmasters/answer/34592)
  for the **hostname** under which you publish your articles. For example, if you publish your
  articles at URLs such as `https://www.example.com/business/article123.html`, you
  should add the site `https://www.example.com/`. Exception: If your site is within a
  hosting site, you should add the site for your **home page**, for example,
  `https://members.tripod.com/mynewssite/`. If you publish articles under multiple
  hostnames, you should add a site for each of them.
- You must
  [verify your site](https://support.google.com/webmasters/answer/34592)
  to enable the news features.

We'll be working to make the news features available to publishers in more languages as soon as
possible.
