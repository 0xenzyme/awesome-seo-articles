---
title: "Introducing the Structured Data Dashboard"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2012-07-introducing-structured-data-dashboard"
url: "https://developers.google.com/search/blog/2012/07/introducing-structured-data-dashboard"
canonical: "https://developers.google.com/search/blog/2012/07/introducing-structured-data-dashboard"
author: "Andrei Pascovici"
published: "2012-08-01T00:00:00+00:00"
updated: "2012-08-01T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:19:33+00:00"
status_code: 200
html_hash: "bdef8b486c3504bca56b38b8f9a26516e8e9833fe7327e20c596f0a9be060ff7"
clean_word_count: 407
clean_char_count: 2774
---
# Introducing the Structured Data Dashboard

Structured data is becoming an increasingly important part of the web ecosystem. Google makes use
of structured data in a number of ways including
[rich snippets](/search/docs/appearance/structured-data/intro-structured-data)
which allow websites to highlight specific types of content in search results. Websites
participate by marking up their content using industry-standard formats and schemas.

To provide webmasters with greater visibility into the structured data that Google knows about for
their website, we're introducing today a new feature in Webmaster Tools - the Structured Data
Dashboard. The Structured Data Dashboard has three views: site, item type and page-level.

## Site-level view

At the top level, the Structured Data Dashboard, which is under Optimization, aggregates this data
(by root item type and vocabulary schema). Root item type means an item that is not an attribute
of another on the same page. For example, the site below has about 2 million Schema.Org
annotations for `Books`
("<https://schema.org/Book>").

![the Structured Data Dashboard in Webmaster Tools](/static/search/blog/images/import/aa1596c06b185056e37e21efa116987d.png)

## Itemtype-level view

It also provides per-page details for each item type, as seen below:

![Structured data Itemtype-level view in webmaster tools](/static/search/blog/images/import/1cb514fb89eeb37e53c5c9276388a98f.png)

Google parses and stores a fixed number of pages for each site and item type. They are stored in
decreasing order by the time in which they were crawled. We also keep all their structured data
markup. For certain
[item types](/search/docs/appearance/structured-data/intro-structured-data)
we also provide specialized preview columns as seen in this example below (for example,
`Name` is specific to schema.org
[`Product`](https://schema.org/Product)).

![Structured data Itemtype-level view in webmaster tools for product annotations](/static/search/blog/images/import/82014d85ce0726587d29346f2de77b97.png)

The default sort order is such that it would facilitate inspection of the most recently added Structured Data.

## Page-level view

Last but not least, we have a details page showing all attributes of every item type on the given
page (as well as a link to the
[Rich Snippet testing tool](https://www.google.com/webmasters/tools/richsnippets)
for the page in question).

![Structured data page level view in webmaster tools](/static/search/blog/images/import/c4588731005b1bd83372c0ad55c626bd.png)

Webmasters can use the Structured Data Dashboard to verify that Google is picking up new markup,
as well as to detect problems with existing markup, for example monitor potential changes in
instance counts during site redesigns.
