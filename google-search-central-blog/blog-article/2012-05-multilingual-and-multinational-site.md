---
title: "Multilingual and multinational site annotations in Sitemaps"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-05-multilingual-and-multinational-site"
url: "https://developers.google.com/search/blog/2012/05/multilingual-and-multinational-site"
canonical: "https://developers.google.com/search/blog/2012/05/multilingual-and-multinational-site"
author: "Pierre Far"
published: "2012-05-24T00:00:00+00:00"
updated: "2012-05-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:19:02+00:00"
status_code: 200
html_hash: "cc1e434c9ffc3355a727978c4f36e008829302f54d35a9f43ec9798b390a1c1c"
clean_word_count: 381
clean_char_count: 2564
---
# Multilingual and multinational site annotations in Sitemaps

In December 2011 we
[announced](/search/blog/2011/12/new-markup-for-multilingual-content) annotations
for sites that target users in many languages and, optionally, countries. These annotations define
a cluster of equivalent pages that target users around the world, and were implemented using
[`rel-alternate-hreflang` `link` elements](/search/docs/specialty/international/localized-versions)
in the HTML of each page in the cluster.

Based on webmaster feedback and other considerations, today we're adding support for specifying
the `rel-alternate-hreflang` annotations in
[sitemaps](/search/docs/crawling-indexing/sitemaps/overview).
Using sitemaps instead of HTML link elements offers many advantages including smaller page size
and easier deployment for some websites.

To see how this works, let's take a simple example: We wish to specify that for the URL
https://www.example.com/en, targeting English language users, the equivalent URL targeting German
language speakers https://www.example.com/de. Up till now, the only way to add such annotation is
to use a link element, either as an HTTP header or as HTML elements on both URLs like this:

```
<link rel="alternate" hreflang="en" href="https://www.example.com/en" >
<link rel="alternate" hreflang="de" href="https://www.example.com/de" >
```

As of today, you can alternately use the following equivalent markup in sitemaps:

```
<url>
  <loc>https://www.example.com/en</loc>
  <xhtml:link
    rel="alternate"
    hreflang="de"
    href="https://www.example.com/de" />
  <xhtml:link
    rel="alternate"
    hreflang="en"
    href="https://www.example.com/en" />
</url>
<url>
  <loc>https://www.example.com/de</loc>
  <xhtml:link
    rel="alternate"
    hreflang="de"
    href="https://www.example.com/de" />
  <xhtml:link
    rel="alternate"
    hreflang="en"
    href="https://www.example.com/en" />
</url>
```

Briefly, the new sitemaps tags shown in bold function in the same way as the HTML link tags, with
both using the same attributes. The full technical details of how the annotations are implemented
in sitemaps, including how to implement the xhtml namespace for the link tag, are in our
[new Help Center article](/search/docs/specialty/international/localized-versions).

A more detailed example can be found in our new Help Center article, and if you need more help,
please ask in our brand new
[internationalization help forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:international_seo)).
