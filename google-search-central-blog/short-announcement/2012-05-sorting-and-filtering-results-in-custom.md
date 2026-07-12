---
title: "Sorting and Filtering Results in Custom Search"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2012-05-sorting-and-filtering-results-in-custom"
url: "https://developers.google.com/search/blog/2012/05/sorting-and-filtering-results-in-custom"
canonical: "https://developers.google.com/search/blog/2012/05/sorting-and-filtering-results-in-custom"
author: "Roger Wang"
published: "2012-05-08T00:00:00+00:00"
updated: "2012-05-08T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:19:09+00:00"
status_code: 200
html_hash: "e4efa0828190ff5813f9d68a1b7a75e6e5040287907727f2a42d9c00735cca74"
clean_word_count: 328
clean_char_count: 2206
---
# Sorting and Filtering Results in Custom Search

*(Cross-posted on the
[Custom Search Blog](https://googlecustomsearch.blogspot.com/2012/05/sorting-and-filtering-results-in-custom.html))*

Using [Custom Search Engine](https://www.google.com/cse/) (CSE),
you can create rich search experiences that make it easier for visitors to find the information
they're looking for on your site. Today we're announcing two improvements to sorting and filtering
of search results in CSE.

First, CSE now supports UI-based
[results sorting](https://support.google.com/customsearch/bin/answer.py?answer=2549537),
which you can enable in the Basics tab of the CSE control panel. Once you've updated the CSE
element code on your site, a "sort by" picker will become visible at the top of the results
section.

![New feature in the Custom Search Engine UI for sorting results](/static/search/blog/images/import/cfbed4d2c0c2dc4b262317a1623b304c.png)

By default CSE supports sorting by date and relevance. In the control panel, you can specify
additional "sort by" keys that are based on the structure of your site's content, giving users
more options to find the results that are most relevant to them. For example, if you've marked up
pages for [product rich snippets](/search/docs/appearance/structured-data/product), you
could enable sorting based on price as shown in this screenshot:

![Sorting is supported by several verticals](/static/search/blog/images/import/f049ec37381e88477c05022b60a2f25b.png)

Second, we're introducing compact queries for
[filtering by attribute](/custom-search/docs/structured_search#filter_by_attribute).
Currently you can issue a query like
`[more:pagemap:product-description:search more:pagemap:product-description:engine]`
which will only show pages with a `product-description` attribute that contains both
`search` and `engine`.

With a compact query, you can issue the same request as
`[more:p:product-description:search*engine]`

We hope these new features help you create richer and more useful search experiences for your
visitors. As always, if you have any questions or feedback please let us know via our
[Help Forum](https://support.google.com/programmable-search/community).
