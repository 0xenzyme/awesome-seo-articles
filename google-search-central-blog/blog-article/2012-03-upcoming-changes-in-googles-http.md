---
title: "Upcoming changes in Google's HTTP Referrer"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-03-upcoming-changes-in-googles-http"
url: "https://developers.google.com/search/blog/2012/03/upcoming-changes-in-googles-http"
canonical: "https://developers.google.com/search/blog/2012/03/upcoming-changes-in-googles-http"
author: "John Mueller"
published: "2012-03-19T00:00:00+00:00"
updated: "2012-03-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:18:30+00:00"
status_code: 200
html_hash: "e1a2763bae2e0cb5d1609b576f4bd6d2b531c4d588d1bc28151ea53ab763f76b"
clean_word_count: 380
clean_char_count: 2440
---
# Upcoming changes in Google's HTTP Referrer

Protecting users' privacy is a priority for us and it's helped drive
[recent](https://googleblog.blogspot.com/2011/10/making-search-more-secure.html)
[changes](https://insidesearch.blogspot.com/2012/03/bringing-more-secure-search-around.html).
Helping users save time is also very important; it's explicitly mentioned as a part of
[our philosophy](https://www.google.com/about/company/tenthings).
Today, we're happy to announce that Google Web Search will soon be using a
[new proposal](https://wiki.whatwg.org/wiki/Meta_referrer) to
reduce latency when a user of Google's SSL-search clicks on a search result with a modern browser
such as Chrome.

Starting in April, for browsers with the appropriate support, we will be using the "referrer" meta
tag to automatically simplify the
[referring URL](https://en.wikipedia.org/wiki/HTTP_referer) that
is sent by the browser when visiting a page linked from an organic search result. This results in
a faster time to result and more streamlined experience for the user.

What does this mean for sites that receive clicks from Google search results? You may start to see
[`origin`](https://tools.ietf.org/html/rfc6454)
referrers—Google's home pages (see the
[meta referrer specification](https://wiki.whatwg.org/wiki/Meta_referrer)
for further detail)—as a source of organic SSL search traffic. This change will only
affect the subset of SSL search referrers which already didn't include the query terms. Non-HTTPS
referrals will continue to behave as they do today. Again, the primary motivation for this change
is to remove an unneeded redirect so that signed-in users reach their destination faster.

Website analytics programs can detect these organic search requests by detecting bare Google host
names using SSL (like "https://www.google.co.uk/"). Webmasters will continue see the same data in
[Webmasters Tools](https://search.google.com/search-console)
just as before, you'll receive an aggregated list of the
[top search queries](https://support.google.com/webmasters/answer/7576553#zippy=%2Cqueries)
that drove traffic to their site.

We will continue to look into further improvements to how search query data is surfaced through
Webmaster Tools. If you have questions, feedback or suggestions, please let us know through the
[Webmaster Tools Help Forum](https://groups.google.com/a/googleproductforums.com/forum/#!categories/webmasters).
