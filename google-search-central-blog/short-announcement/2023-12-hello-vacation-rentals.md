---
title: "Adding markup support for vacation rentals"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2023-12-hello-vacation-rentals"
url: "https://developers.google.com/search/blog/2023/12/hello-vacation-rentals"
canonical: "https://developers.google.com/search/blog/2023/12/hello-vacation-rentals"
author: "Troy Joseph, Google Search Software Engineer"
published: "2023-12-04T00:00:00+00:00"
updated: "2023-12-04T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:43:22+00:00"
status_code: 200
html_hash: "c9487f24ea7c3817e97e7839d47c1bdab31ac7b1aa071d9761286a622272d3c0"
clean_word_count: 338
clean_char_count: 2248
---
# Adding markup support for vacation rentals

Vacation rentals on Google make it easier for travelers to discover the best lodging options,
whether they're searching for a cozy cabin or a house that sleeps ten. Today, we're announcing a
new and simpler way for vacation rental integration partners to provide listing data to Google.

![An illustration of vacation rentals in Google Search](/static/search/docs/images/vacation-rental-rich-result.png)

Vacation rental partners can now implement [structured data markup](/search/docs/appearance/structured-data/vacation-rental)
in their site's pages to be eligible for this rich result. The existing
[feed method](https://support.google.com/hotelprices/answer/11949906) remains a good
option for large partners and those with many domains and brands. We recommend the markup option
for smaller partners including property managers who prefer a simpler setup and maintenance.

This feature is limited to sites that meet certain eligibility criteria and additional
[steps are required](https://support.google.com/hotelprices/answer/11946837) to
complete the integration. To learn more about how to list your vacation rentals on Google, visit
the [integration starter guide](https://support.google.com/hotelprices/answer/12568039).

## New vacation rental rich result report in Search Console

To help you monitor and verify your markup, we're also starting to support vacation rental
listing structured data in a new [vacation rental rich result report](https://support.google.com/webmasters/answer/7552505)
in Search Console. This report will help you monitor and fix the validity of your vacation rental
structured data.

![Vacation rental rich result report in Search Console](/static/search/blog/images/vacation-rental-rich-results-report.png)

## Support in the Rich Results Test

You can test your structured data using the [Rich Results Test](https://search.google.com/test/rich-results)
by submitting the URL of a page or a code snippet. Using the tool, you can immediately confirm
whether or not your markup is valid without waiting for the rich result report to be updated.

![Vacation rental markup in the Rich Results Test](/static/search/blog/images/vacation-rental-rich-results-test.png)
