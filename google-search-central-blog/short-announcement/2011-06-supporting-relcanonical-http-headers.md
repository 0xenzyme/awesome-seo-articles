---
title: "Protecting your site with Gruyere"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2011-06-supporting-relcanonical-http-headers"
url: "https://developers.google.com/search/blog/2011/06/supporting-relcanonical-http-headers"
canonical: "https://developers.google.com/search/blog/2011/06/supporting-relcanonical-http-headers"
author: "Pierre Far"
published: "2011-06-17T00:00:00+00:00"
updated: "2011-06-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:13:52+00:00"
status_code: 200
html_hash: "30ff95d5d714a3f3605998c9080b6561ab7d2ebe84f9035c7fd210bd88b0a013"
clean_word_count: 321
clean_char_count: 2061
---
# Protecting your site with Gruyere

Based on your feedback, we’re happy to announce that Google web search now supports
[`link` `rel="canonical"` relationships](/search/docs/crawling-indexing/consolidate-duplicate-urls)
specified in HTTP headers as per the syntax described in
[section 5 of IETF RFC 5988](https://tools.ietf.org/html/rfc5988#section-5).
Webmasters can use `rel="canonical"` HTTP headers to signal the canonical URL for both
HTML documents and other types of content such as PDF files.

To see the `rel="canonical"` HTTP header in action, let’s look at the scenario of a
website offering a white paper both as an HTML page and as a downloadable PDF alternative, under
these two URLs:

- https://www.example.com/white-paper.html
- https://www.example.com/white-paper.pdf

In this case, the webmaster can signal to Google that the canonical URL for the PDF download is
the HTML document by using a `rel="canonical"` HTTP header when the PDF file is
requested; for example:

```
GET /white-paper.pdf HTTP/1.1
Host: www.example.com
(...rest of HTTP request headers...)

HTTP/1.1 200 OK
Content-Type: application/pdf
Link: <https://www.example.com/white-paper.html>; rel="canonical"
Content-Length: 785710
(... rest of HTTP response headers...)
```

Another common situation in which `rel="canonical"` HTTP headers may help is when a
website serves the same file from multiple URLs (for example when using a content distribution
network) and the webmaster wishes to signal to Google the preferred URL.

We currently support these link header elements for web search only. As we see how webmasters are
using these elements, we're hoping to add support for them in our other properties. For more
information, please see our Help Center articles about
[canonicalization](/search/docs/crawling-indexing/consolidate-duplicate-urls) and the
[`rel="canonical"` element](/search/docs/crawling-indexing/consolidate-duplicate-urls).
If you have any questions, please ask in our
[Webmaster Help Forum](https://www.google.com/support/forum/p/Webmasters?hl=en).
