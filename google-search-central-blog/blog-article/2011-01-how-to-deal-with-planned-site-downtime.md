---
title: "How to deal with planned site downtime"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-01-how-to-deal-with-planned-site-downtime"
url: "https://developers.google.com/search/blog/2011/01/how-to-deal-with-planned-site-downtime"
canonical: "https://developers.google.com/search/blog/2011/01/how-to-deal-with-planned-site-downtime"
author: "Kaspar Szymanski"
published: "2011-01-25T00:00:00+00:00"
updated: "2011-01-25T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:10:50+00:00"
status_code: 200
html_hash: "315233692f5a191bcb6f4135578d29f34639cf980e683799cc934b74e14437b7"
clean_word_count: 465
clean_char_count: 2833
---
# How to deal with planned site downtime

Once in a while we get asked whether a site's visibility in Google's search results can be impacted
in a negative way if it's unavailable when Googlebot tries to crawl it. Sometimes downtime is
unavoidable: a site owner might decide to take a site down due to ongoing site maintenance, or
legal or cultural requirements. Outages that are not clearly marked as such can negatively affect
a site's reputation. While we cannot guarantee any crawling, indexing or ranking, there are
methods to deal with planned website downtime in a way that will generally not negatively affect
your site's visibility in the search results.

For example, instead of returning an HTTP result code
[`404 (Not Found)`](https://en.wikipedia.org/wiki/HTTP_404)
or showing an error page with the status code `200 (OK)` when a page is requested,
it's better to return a `503` HTTP result code (Service Unavailable) which tells search
engine crawlers that the downtime is temporary. Moreover, it allows site owners to provide
visitors and bots with an estimated time when the site will be up and running again. If known, the
length of the downtime in seconds or the estimated date and time when the downtime will be
complete can be specified in an optional
[`Retry-After` header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37),
which Googlebot may use to determine when to recrawl the URL.

Returning a `503` HTTP result code can be a great solution for a number of other
situations. We encounter a lot of problems with sites that return `200 (OK)` result
codes for server errors, downtime, bandwidth-overruns or for temporary placeholder pages
("Under Construction"). The `503` HTTP result code is the site owner's solution of
choice for all these situations. As for planned server downtime like hardware maintenance, it's a
good idea to have a separate server available to actually return the `503` HTTP result
code. It is important, however, to not treat `503` as a permanent solution: lasting
`503` HTTP result codes can eventually be seen as a sign that the server is now
permanently unavailable and can result in us removing URLs from Google's index.

If you set up a `503 (Service Unavailable)` response, the header information might look
like this when using PHP:

```
header('HTTP/1.1 503 Service Temporarily Unavailable');
header('Retry-After: Sat, 8 Oct 2011 18:27:00 GMT');
```

Similar to how you can
[make `404` pages more useful to users](/search/docs/crawling-indexing/http-network-errors#pagegone),
it's also a good idea to provide a customized `503` message explaining the situation to
users and letting them know when the site will be available again. For further information
regarding HTTP result codes, please see
[RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10).
