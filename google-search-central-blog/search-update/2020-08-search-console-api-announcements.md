---
title: "Search Console API announcements"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2020-08-search-console-api-announcements"
url: "https://developers.google.com/search/blog/2020/08/search-console-api-announcements"
canonical: "https://developers.google.com/search/blog/2020/08/search-console-api-announcements"
author: "Nati Yosephian, Search Console Software Engineer"
published: "2020-08-06T00:00:00+00:00"
updated: "2020-08-06T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:37:31+00:00"
status_code: 200
html_hash: "218cfe320953357436cf61d2d97d7305b608e05cbf0e93cff9b5c84f7240186b"
clean_word_count: 596
clean_char_count: 3706
---
# Search Console API announcements

Over the past year, we have been working to upgrade the infrastructure of the
[Search Console API](/webmaster-tools), and we are happy to let you know that we're
almost there. You might have already noticed some minor changes, but in general, our goal was to
make the migration as invisible as possible. This change will help Google to improve the
performance of the API as demand grows.

Note that **if you're not querying the API yourself you don't need to take action**.
If you are querying the API for your own data or if you maintain a tool which uses that data
(for example, a WordPress plugin), read on. Below is a summary of the changes:

1. **Changes on Google Cloud Platform dashboard**: you'll see is a drop in the old
   API usage report and an increase in the new one.
2. **API key restriction changes**: if you have previously set API key
   restrictions, you might need to change them.
3. **Discovery document changes**: if you're querying the API using a third-party
   API library or querying the
   [Webmasters Discovery Document](https://www.googleapis.com/discovery/v1/apis/webmasters/v3/rest)
   directly, you will need to update it by the end of the year.

Please note that other than these changes, the **API is backward compatible** and
there are currently no changes in scope or functionality.

## Google Cloud Platform (GCP) changes

In the
[Google Cloud Console dashboards](https://cloud.google.com/monitoring/charts/dashboards),
you will notice a traffic drop for the legacy API and an increase in calls to the new one. This
is the same API, just under the new name.

![Search Console API changes in Google Cloud Console](/static/search/blog/images/import/bf8e53f15fe1c0a8b91a79948c4d163e.jpg)

You can monitor your API usage on the
[new Google Search Console API page](https://console.cloud.google.com/apis/api/searchconsole.googleapis.com/overview).

## API key restriction changes

As mentioned in the introduction, these instructions are important only if you query the data
yourself or provide a tool that does that for your users.

To check if you have an API restriction active on your API key, follow
[these steps](https://cloud.google.com/docs/authentication/api-keys#adding_api_restrictions)
in the [credentials page](https://console.cloud.google.com/apis/credentials)
and make sure the Search Console API is not restricted. If you have added an API restriction for
your API keys **you will need to take action by August 31**.

In order to allow your API calls to be migrated automatically to the new API infrastructure, you
need to make sure the Google Search Console API is not restricted.

- If your API restrictions are set to "Don't restrict key" you're all set.
- If your API restrictions are set to "Restrict key",  **the Search Console API should be
  checked as shown in the image below**.

![Google Search Console API restrictions setting](/static/search/blog/images/import/44efcb3a3364ea8e409ac3171ed1d8d1.png)

## Discovery document changes

If you're querying the Search Console API using an
[external API library](/api-client-library), or
querying the
[Webmasters API discovery document](https://www.googleapis.com/discovery/v1/apis/webmasters/v3/rest)
directly **you will need to take action** as we'll drop the support in the
Webmasters discovery document. Our current plan is to support it until December 31, 2020 - but
**we'll provide more details and guidance in the coming months**.

If you have any questions, you can ask in the
[help community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console))
or the Google Webmasters [Twitter handle](https://twitter.com/googlesearchc).
