---
title: "Welcoming the new Search Console URL Inspection API"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2022-01-url-inspection-api"
url: "https://developers.google.com/search/blog/2022/01/url-inspection-api"
canonical: "https://developers.google.com/search/blog/2022/01/url-inspection-api"
author: "Daniel Waisberg"
published: "2022-01-31T00:00:00+00:00"
updated: "2022-01-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:40:07+00:00"
status_code: 200
html_hash: "76b6c2bb07da1ca66e6813cd02797bc1e71f484d53b20cf9745fe7a1a78f7484"
clean_word_count: 628
clean_char_count: 4784
---
# Welcoming the new Search Console URL Inspection API

Today we’re launching the new Google Search Console [URL Inspection API](/webmaster-tools/v1/urlInspection.index/inspect),
which gives programmatic access to URL-level data for properties you manage in Search Console.

The [Search Console APIs](/webmaster-tools) are a way to access data outside of Search Console, through external applications and products.
Developers and SEO tools already use the APIs to build custom solutions to view, add, or remove properties and sitemaps, and to run advanced queries on Search performance data.

With the new URL Inspection API, we're providing a new tool for developers to debug and optimize their pages. You can request the data Search Console has about the indexed version of a URL;
the API will return the indexed information currently available in the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289).

## Using the new API

In order to learn how to use the new API, check the [API developer documentation](/webmaster-tools/v1/urlInspection.index/inspect).
The request parameters include the URL you’d like to inspect and the URL of the property as defined in Search Console.

The response includes analysis results containing information from Search Console, including index status, AMP, rich results, and mobile usability. For more details, read the
[list of parameters](/webmaster-tools/v1/urlInspection.index/UrlInspectionResult) and the
[Indexed URL results explanation](https://support.google.com/webmasters/answer/9012289#indexed_inspection).

Once you make the API call, you will get a response with all relevant results, or an error message if the request fails. If a specific analysis result is missing from the response,
it means the analysis was not available for the URL inspected. Here's an example of the response you’ll get from the API.

```
  {
  "inspectionResult": {
    "inspectionResultLink": "https://search.google.com/search-console/inspect?resource_id=https://developers.google.com/search/&id=odaUL5Dqq3q8n0EicQzawg&utm_medium=link",
    "indexStatusResult": {
      "verdict": "PASS",
      "coverageState": "Indexed, not submitted in sitemap",
      "robotsTxtState": "ALLOWED",
      "indexingState": "INDEXING_ALLOWED",
      "lastCrawlTime": "2022-01-31T08:39:51Z",
      "pageFetchState": "SUCCESSFUL",
      "googleCanonical": "https://developers.google.com/search/help/site-appearance-faq",
      "userCanonical": "https://developers.google.com/search/help/site-appearance-faq",
      "referringUrls": [
        "https://developers.google.com/search/updates",
        "https://developers.google.com/search/help/crawling-index-faq"
      ],
      "crawledAs": "MOBILE"
    },
    "mobileUsabilityResult": {
      "verdict": "PASS"
    },
    "richResultsResult": {
      "verdict": "PASS",
      "detectedItems": [
        {
          "richResultType": "Breadcrumbs",
          "items": [
            {
              "name": "Unnamed item"
            }
          ]
        },
        {
          "richResultType": "FAQ",
          "items": [
            {
              "name": "Unnamed item"
            }
          ]
        }
      ]
    }
```

## Potential use cases

While building the new API, we consulted various SEOs and publishers with regards to how they would use the API to create solutions with this data. Here are some of the use cases that stand out:

- *SEO tools and agencies* can provide ongoing monitoring for important pages and single page debugging options. For example, checking if there are differences between user-declared
  and Google-selected canonicals, or debugging structured data issues from a group of pages.
- *CMS and plugin developers* can add page or template-level insights and ongoing checks for existing pages. For example, monitoring changes over time for key pages
  to diagnose issues and help prioritize fixes.

## Usage limits

You can find a more detailed description of Search Console [APIs usage limits](/webmaster-tools/limits)
in the developer documentation. Specifically with regards to the URL Inspection API, the quota is enforced per Search Console
[website property](https://support.google.com/webmasters/answer/34592) (calls querying the same site):

- 2,000 queries per day
- 600 queries per minute

## Feedback

We believe the new API will bring new opportunities to the ecosystem to innovate with Google Search data; we’re always excited to see the solutions developers and SEOs build around the
Search Console APIs.

If you have any questions or feedback, reach out to us [on Twitter](https://twitter.com/googlesearchc), or post a question in the
[Search Central community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)).
