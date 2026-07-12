---
title: "Updates to Search Console's API"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2020-12-search-console-api-updates"
url: "https://developers.google.com/search/blog/2020/12/search-console-api-updates"
canonical: "https://developers.google.com/search/blog/2020/12/search-console-api-updates"
author: "Nati Yosephian, Gilad Amar, and Michael Huzman, Search Console team"
published: "2020-12-09T00:00:00+00:00"
updated: "2020-12-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:38:07+00:00"
status_code: 200
html_hash: "651a47aa056c4eefc96ea4ad6e32c97aee339446304aed4cacec8fe2ae42cd69"
clean_word_count: 576
clean_char_count: 3941
---
# Updates to Search Console's API

A few months ago we announced an [API infrastructure upgrade](/search/blog/2020/08/search-console-api-announcements)
to improve the performance of the [Search Console API](/webmaster-tools) as demand grows. Today we're happy to announce
some more updates coming your way:

- Addition of fresh data and news filter in the Search Console API
- Domain property support in the Sitemaps API
- Guidelines on how to [migrate the Discovery doc](/search/blog/2020/08/search-console-api-announcements#discovery-document-changes)

If you make your own calls to the API, read on.

## Fresh data and news filter in the Search Console API

The [Performance report](https://support.google.com/webmasters/answer/7576553) already supports fresh data that is less than a day old. You can now access this data through the API by passing the request parameter
`dataState` with value set to `all`. The data you get for this value will also include fresh data that is not yet final. If you wish to get only final data,
you can either pass this parameter with value set to `final` or not pass it at all and you will get only final data by default.

A few months ago, we added a [News tab on Search filter](https://twitter.com/googlesearchc/status/1285559587576467456) to the
Performance report. This information is now also available in the API, and you can access it by setting the value of `searchType`
parameter in the request to `news`.

## Domain property support in the Sitemaps API

The Sitemaps API now supports domain properties, as other Search Console APIs already do. You can query, add, and delete your sitemaps on
[domain properties](https://support.google.com/webmasters/answer/34592#domain_property), for example:

`GET https://www.googleapis.com/webmasters/v3/sites/sc-domain:example.com/sitemaps`

## Discovery doc migration

We'll drop the support in the Webmasters discovery document. If you're querying the Search Console API using an [external API library](/api-client-library), or querying
the [Webmasters API discovery document](https://www.googleapis.com/discovery/v1/apis/webmasters/v3/rest) directly, you will
need to update your API calls to include the following changes.

### API library changes

For updates on the API library changes, refer to the [Java](/webmaster-tools/search-console-api-original/v3/quickstart/quickstart-java) and
[Python](/webmaster-tools/search-console-api-original/v3/quickstart/quickstart-python) quickstart guides,
for an updated API usage guide.

#### Java

For all Webmasters service-related imports, change the `webmasters` package to the `searchconsole.v1` package,
and the service name, `Webmasters`, to `SearchConsole`. Examples:

- Importing the API service:

  `import com.google.api.services.webmasters.Webmasters;`

  `import com.google.api.services.searchconsole.v1.SearchConsole;`
- Importing a response object:

  `import com.google.api.services.webmasters.model.WmxSite;`

  `import com.google.api.services.searchconsole.v1.model.WmxSite;`

Note that besides the service object, other API objects are exactly the same as before, only the **package** changes.

#### Python

When building the Webmasters service object, make the following change:

`webmasters_service = build('webmasters', 'v3', http=http)`

`webmasters_service = build('searchconsole', 'v1', http=http)`

Again, there's no change in how objects behave.

### Direct discovery document query

The discovery document querying changes include:

- URL change

  `https://www.googleapis.com/discovery/v1/apis/webmasters/v3/rest`

  `https://searchconsole.googleapis.com/$discovery/rest`
- Content change
  - The `name` field changed from `webmasters` to `searchconsole`.
  - The `version` field changed from `v3` to `v1`.

If you have any questions, you can ask in the [Search
Central community](https://support.google.com/webmasters/community) or [on Twitter](https://twitter.com/googlesearchc).
