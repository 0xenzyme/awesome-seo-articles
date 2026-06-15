---
title: "Update on the Autocomplete API"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-07-update-on-autocomplete-api"
url: "https://developers.google.com/search/blog/2015/07/update-on-autocomplete-api"
canonical: "https://developers.google.com/search/blog/2015/07/update-on-autocomplete-api"
author: "Peter Chiu on behalf of the Autocomplete team"
published: "2015-07-24T00:00:00+00:00"
updated: "2015-07-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:27:09+00:00"
status_code: 200
html_hash: "349584df22cd44ade5b761dbf80e51d31d82b804b5db8dad90d01a3a3a66a574"
clean_word_count: 375
clean_char_count: 2387
---
# Update on the Autocomplete API

Google Search provides an autocomplete service that attempts to predict a query before a user
finishes typing. For years, a number of developers have integrated the results of autocomplete
within their own services using a non-official, non-published API that also had no restrictions on
it. Developers who discovered the autocomplete API were then able to incorporate autocomplete
services, independent of Google Search.

There have been multiple times in which the developer community's reverse-engineering of a Google
service via an unpublished API has led to great things. The Google Maps API, for example, became a
formal supported API months after seeing what creative engineers could do combining map data with
other data sources. We currently support
[more than 80 APIs](/apis-explorer) that
developers can use to integrate Google services and data into their applications.

However, there are some times when using an unsupported, unpublished API also carries the risk
that the API will stop being be available. This is one of those situations.

We built autocomplete as a complement to Search, and never intended that it would exist
disconnected from the purpose of anticipating user search queries. Over time we've realized that
while we can conceive of uses for an autocomplete data feed outside of search results that may be
valuable, overall the content of our automatic completions are optimized and intended to be used
in conjunction with web search results, and outside of the context of a web search don't provide a
meaningful user benefit.

In the interest of maintaining the integrity of autocomplete as part of Search, we will be
restricting unauthorized access to the unpublished autocomplete API as of August 10th, 2015. We
want to ensure that users experience autocomplete as it was designed to be used—as a service
closely tied to Search. We believe this provides the best user experience for both services.

For publishers and developers who still want to use the autocomplete service for their site, we
have an alternative. Google Custom Search Engine allows sites to maintain autocomplete
functionality in connection with Search functionality. Any partner already using Google CSE will
be unaffected by this change. For others, if you want autocomplete functionality after August
10th, 2015, please see our CSE sign-up page.
