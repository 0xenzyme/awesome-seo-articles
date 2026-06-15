---
title: "Indexing HTTPS pages by default"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-12-indexing-https-pages-by-default"
url: "https://developers.google.com/search/blog/2015/12/indexing-https-pages-by-default"
canonical: "https://developers.google.com/search/blog/2015/12/indexing-https-pages-by-default"
author: "Zineb Ait Bahajji"
published: "2015-12-17T00:00:00+00:00"
updated: "2015-12-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:28:01+00:00"
status_code: 200
html_hash: "1f25d833a1351156a65e203aad4f2aade0953b152d852db0554e449c5599681b"
clean_word_count: 409
clean_char_count: 2559
---
# Indexing HTTPS pages by default

At Google, user security has always been a top priority. Over the years, we've worked hard to
promote a more secure web and to provide a better browsing experience for users.
[Gmail](https://gmailblog.blogspot.com/2014/03/staying-at-forefront-of-email-security.html),
[Google Search](https://googleblog.blogspot.com/2011/10/making-search-more-secure.html),
and YouTube have had secure connections for some time, and we also started giving a slight
[ranking boost to HTTPS URLs](/search/blog/2014/08/https-as-ranking-signal) in search
results last year. Browsing the web should be a private experience between the user and the
website, and must not be subject to
[eavesdropping](https://en.wikipedia.org/wiki/Eavesdropping),
[man-in-the-middle attacks](https://en.wikipedia.org/wiki/Man-in-the-middle_attack),
or data modification. This is why we've been strongly promoting
[HTTPS everywhere](https://www.youtube.com/watch?v=cBhZ6S0PFCY).

As a natural continuation of this, today we'd like to announce that we're adjusting our indexing
system to look for more HTTPS pages. Specifically, we'll start crawling HTTPS equivalents of HTTP
pages, even when the former are not linked to from any page. When two URLs from the same domain
appear to have the same content but are served over different protocol schemes, we'll typically
choose to index the HTTPS URL if:

- It doesn't contain insecure dependencies.
- It isn't blocked from crawling by robots.txt.
- It doesn't redirect users to or through an insecure HTTP page.
- It doesn't have a `rel="canonical"` link to the HTTP page.
- It doesn't contain a `noindex` robots `meta` tag.
- It doesn't have on-host outlinks to HTTP URLs.
- The sitemaps lists the HTTPS URL, or doesn't list the HTTP version of the URL
- The server has a valid TLS certificate.

Although our systems prefer the HTTPS version by default, you can also make this clearer for other
search engines by redirecting your HTTP site to your HTTPS version and by implementing the
[HSTS header](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)
on your server.

We're excited about taking another step forward in making the web more secure. By showing users
HTTPS pages in our search results, we're hoping to decrease the risk for users to browse a website
over an insecure connection and making themselves vulnerable to content injection attacks. As
usual, if you have any questions or comments, please let us know in our
[webmaster help forums](https://support.google.com/webmasters/go/community).
