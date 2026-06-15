---
title: "An update to how we generate web page titles"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2021-08-update-to-generating-page-titles"
url: "https://developers.google.com/search/blog/2021/08/update-to-generating-page-titles"
canonical: "https://developers.google.com/search/blog/2021/08/update-to-generating-page-titles"
author: "Danny Sullivan, Search Liaison"
published: "2021-08-24T00:00:00+00:00"
updated: "2021-08-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:39:42+00:00"
status_code: 200
html_hash: "47cd846962c32a04bb8f5f10e88e9966d8bdaae251fa63507574230f7b53348a"
clean_word_count: 564
clean_char_count: 3408
---
# An update to how we generate web page titles

One of the primary ways people determine which search results might be relevant to their query is
by reviewing the titles of listed web pages. That's why Google Search works hard to provide the
best titles for documents in our results to connect searchers with the content that creators,
publishers, businesses, and others have produced.

## How titles are generated

Last week, we introduced a new system of generating titles for web pages. Before this, titles might
change based on the query issued. This generally will no longer happen with our new system. This
is because we think our new system is producing titles that work better for documents overall,
to describe what they are about, regardless of the particular query.

Also, while we've gone [beyond HTML
text to create titles](/search/docs/appearance/title-link) for [over
a decade](/search/blog/2012/01/better-page-titles-in-search-results), our new system is making even more use of such text. In particular, we are making
use of text that humans can visually see when they arrive at a web page. We consider the main
visual title or headline shown on a page, content that site owners often place within `<H1>`
tags or other header tags, and content that's large and prominent through the use of style treatments.

Other text contained in the page might be considered, as might be text within links that point at
pages.

## Why more than HTML title tags are used

Why not just always use the HTML title tag? For the same reasons
[we explained](/search/blog/2012/01/better-page-titles-in-search-results) when we began
going beyond the tag significantly back in 2012. HTML title tags don't always describe a page
well. In particular, title tags can sometimes be:

- Very long.
- "Stuffed" with keywords, because creators mistakenly think adding a bunch of words will
  increase the chances that a page will rank better.
- Lack title tags entirely or contain repetitive "boilerplate" language. For instance, home
  pages might simply be called "Home". In other cases, all pages in a site might be called
  "Untitled" or simply have the name of the site.

Overall, our update is designed to produce more readable and accessible titles for pages. In some
cases, we may add site names where that is seen as helpful. In other instances, when encountering
an extremely long title, we might select the most relevant portion rather than starting at the
beginning and truncating more useful parts.

## A focus on good HTML title tags remains valid

We'll soon be updating our long-standing [help
page about titles](/search/docs/appearance/title-link) to reflect this recent change. However, our main advice on that page to site
owners remains the same. Focus on creating great HTML title tags. Of all the ways we generate
titles, content from HTML title tags is still by far the most likely used, more than 80% of the time.

As with any system, the titles we generate won't always be perfect. We do welcome any feedback in
our [forums](https://support.google.com/webmasters/thread/122879386/your-feedback-on-titles-shown-in-search-results). We're
already making refinements to our new system based on feedback, and we'll keep working to make it even
better over time. Our testing shows the change we've introduced produces titles that are more
readable and preferred by searchers compared to our old system.
