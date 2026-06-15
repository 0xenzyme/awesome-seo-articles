---
title: "An Update on Sitemaps at Google"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-06-update-on-sitemaps-at-google"
url: "https://developers.google.com/search/blog/2009/06/update-on-sitemaps-at-google"
canonical: "https://developers.google.com/search/blog/2009/06/update-on-sitemaps-at-google"
author: "John Mueller"
published: "2009-06-11T00:00:00+00:00"
updated: "2009-06-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T12:59:00+00:00"
status_code: 200
html_hash: "b0e06a54249f252929eef487caa6f1c2e97af84be722b78a67b6dc0cce581a25"
clean_word_count: 436
clean_char_count: 2784
---
# An Update on Sitemaps at Google

Did you know that the number of website hosts that have been submitting Sitemap files has almost
tripled over the last year? It's no wonder: the secret is out - as a
[recent research study](/search/blog/2009/04/research-study-of-sitemaps)
showed, Sitemaps helps search engines to find new and changed content faster. Using Sitemaps
doesn't guarantee that your site will be crawled and indexed completely, but it certainly helps
us understand your website better.

Together with the
[Webmaster Tools design update](/search/blog/2009/06/out-with-old-in-with-new),
we've been working on Sitemaps as well:

- Google and the other search engines which are a part of
  [Sitemaps.org](https://www.sitemaps.org/index.html)
  now support up to 50,000 child Sitemaps for
  [Sitemap index files](https://www.sitemaps.org/index.html)
  (instead of the previous 1,000). This allows large sites to submit a theoretical maximum of
  2.5 billion URLs with a single Sitemap Index URL (oh, and if you need more, you can always
  submit multiple Sitemap index files).
- The
  [Webmaster Tools design update](/search/blog/2009/04/spring-time-design-refresh)
  now shows you all Sitemap files that were submitted for your verified website. This is
  particularly useful if you have multiple owners verified in Webmaster Tools or if you are
  submitting some Sitemap files via
  [HTTP ping](https://www.google.com/support/webmasters/bin/answer.py?answer=34609)
  or through your [robots.txt](/search/docs/crawling-indexing/sitemaps/overview)
  file.
- The
  [indexed URL count](/search/blog/2009/03/using-stats-from-site-and-sitemap)
  in Webmaster Tools for your Sitemap files is now even more precise.
- For the XML developers out there, we've updated the
  [XSD schemas](https://www.sitemaps.org/schemas/sitemap/0.9/)
  to allow Sitemap extensions. The new schema helps webmasters to create better Sitemaps by
  verifying more features. By validating Sitemap files with the new schema, you can be more
  confident that the Sitemap files are correct.
- Do I need to mention that Sitemap file processing is much faster than ever before? We've
  drastically reduced the average time from submitting a Sitemap file to processing it and
  showing some initial data in Webmaster Tools.

For more information about using Sitemaps, make sure to check out our blog post about
[frequently asked questions on Sitemaps](/search/blog/2008/01/sitemaps-faqs)
and our
[Help Center](/search/docs/crawling-indexing/sitemaps/overview). If you have any questions that
aren't covered here, don't forget to
[search our Help Forum](https://support.google.com/webmasters/community)
and start a thread in the
[Sitemaps section](https://support.google.com/webmasters/community/)
for more help.
