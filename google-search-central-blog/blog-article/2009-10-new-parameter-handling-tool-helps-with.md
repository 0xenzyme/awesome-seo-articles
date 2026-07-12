---
title: "New parameter handling tool helps with duplicate content issues"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-10-new-parameter-handling-tool-helps-with"
url: "https://developers.google.com/search/blog/2009/10/new-parameter-handling-tool-helps-with"
canonical: "https://developers.google.com/search/blog/2009/10/new-parameter-handling-tool-helps-with"
author: "Tanya Gupta and Ningning Zhu, Software Engineers"
published: "2009-10-05T00:00:00+00:00"
updated: "2009-10-05T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:01:33+00:00"
status_code: 200
html_hash: "ce41d43801b11b9abd943486e9e45683459b9b90380f86a3b93e39ae8a5c68bf"
clean_word_count: 483
clean_char_count: 3068
---
# New parameter handling tool helps with duplicate content issues

Duplicate content has been a hot topic among webmasters and our blog for over three years. One of
our [first posts](/search/blog/2006/12/deftly-dealing-with-duplicate-content) on the
subject came out in December of '06, and our
[most recent post](/search/blog/2009/09/duplicate-content-and-multiple-site) was last
week. Over the past three years, we've been providing tools and tips to help webmasters control
which URLs we crawl and index, including a) use of `301` redirects, b)
[www vs. non-www preferred domain setting](https://www.google.com/support/webmasters/bin/answer.py?answer=44231),
c) [change of address option](/search/blog/2009/06/out-with-old-in-with-new), and d)
[`rel="canonical"`](/search/blog/2009/02/specify-your-canonical).

We're happy to announce another feature to assist with managing duplicate content: parameter
handling. Parameter handling allows you to view which parameters Google believes should be ignored
or not ignored at crawl time, and to overwrite our suggestions if necessary.

![Screenshot of the URL parameter tool at its launch](/static/search/blog/images/oldurlparam.png)

The URL Parameters tool in 2009

Let's take our old example of a
[site selling Swedish fish](/static/search/blog/images/swedish-fish.jpg). Imagine that your
preferred version of the URL and its content looks like this:

```
https://www.example.com/product.php?item=swedish-fish
```

However, you may also serve the same content on different URLs depending on how the user navigates
around your site, or your content management system may embed parameters such as <
code>sessionid:

```
https://www.example.com/product.php?item=swedish-fish&category=gummy-candy
https://www.example.com/product.php?item=swedish-fish&trackingid=1234&sessionid=5678
```

With the "Parameter Handling" setting, you can now provide suggestions to our crawler to ignore
the parameters *category, trackingid*, and *sessionid*. If we take your suggestion into
account, the net result will be a more efficient crawl of your site, and fewer duplicate URLs.

Since we launched the feature, here are some popular questions that have come up:

## Are the suggestions provided a hint or a command?

Your suggestions are considered hints. We'll do our best to take them into account; however, there
may be cases when the provided suggestions may do more harm than good for a site.

## When do I use parameter handling vs `rel="canonical"`?

`rel="canonical"` is a great tool to manage duplicate content issues, and has had huge
adoption. The differences between the two options are:

- `rel="canonical"` has to be put on each page, whereas parameter handling is set at
  the host level
- `rel="canonical"` is respected by many search engines, whereas parameter handling
  suggestions are only provided to Google

Use which option works best for you; it's fine to use both if you want to be very thorough.

As always,
[your feedback](https://support.google.com/webmasters/community)
on our new feature is appreciated.
