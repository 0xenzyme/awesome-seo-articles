---
title: "Farewell to soft 404s"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2008-08-farewell-to-soft-404s"
url: "https://developers.google.com/search/blog/2008/08/farewell-to-soft-404s"
canonical: "https://developers.google.com/search/blog/2008/08/farewell-to-soft-404s"
author: "Maile Ohye"
published: "2008-08-12T00:00:00+00:00"
updated: "2008-08-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:53:39+00:00"
status_code: 200
html_hash: "920d0bca9c363c06c1a4702012d72c2b0c07b03da485f5861a94c1e96047ccc6"
clean_word_count: 297
clean_char_count: 1869
---
# Farewell to soft 404s

We see two kinds of
[`404` ("File not found") responses](/search/docs/crawling-indexing/http-network-errors)
on the web: "hard `404` error" and "soft `404` error." We discourage the use
of so-called `soft 404` because they can be a confusing experience for users and search
engines. Instead of returning a `404` response code for a non-existent URL, websites
that serve `soft 404` errors *return a `200` response code*. The
content of the `200` response is often the home page of the site, or an error page.

How does a `soft 404` look to the user? Here's a mockup of a `soft 404`:
This site returns a `200` response code and the site's home page for URLs that don't
exist.

![a user confused by a soft 404](/static/search/blog/images/import/d7ee5595d67cc4369244bade38b53e40.png)

As exemplified above, `soft 404` errors are confusing for users, and furthermore search
engines may spend much of their time crawling and indexing non-existent, often duplicative URLs
on your site. This can negatively impact your site's crawl coverage—because of the time Googlebot
spends on non-existent pages, your unique URLs may not be discovered as quickly or visited as
frequently.

## What should you do instead of returning a `soft 404`?

It's much better to *return a `404` response code and clearly explain to users that
the file wasn't found*. This makes search engines and many users happy.

![example of a 404 response header](/static/search/blog/images/import/e2bc59570529ef251f4c327aae2a34bf.png)
![example error message returned to the user explaining that the content is not found](/static/search/blog/images/import/7ffcd978d0497f3ee6021e60557a305d.png)

Can your webserver return `404`, but send a helpful "Not found" message to the user? Of
course! More info as
"[`404` week](/search/blog/2008/08/its-404-week-at-webmaster-central)"
continues!
