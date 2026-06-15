---
title: "Vehicle listing structured data for car dealerships"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2023-10-vehicle-listings-structured-data"
url: "https://developers.google.com/search/blog/2023/10/vehicle-listings-structured-data"
canonical: "https://developers.google.com/search/blog/2023/10/vehicle-listings-structured-data"
author: "Daniel Yosef and Alexander Ikonomidis, Google Search software engineers"
published: "2023-10-16T00:00:00+00:00"
updated: "2023-10-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:43:02+00:00"
status_code: 200
html_hash: "1af1eecec1ffacb23b0c8d5ac8d642ccd47a03f96cd0e7ff9461a172ef14dc2b"
clean_word_count: 399
clean_char_count: 2645
---
# Vehicle listing structured data for car dealerships

Vehicle listings on Google allows car dealerships to show their for-sale inventory on Google Search and other
Google surfaces. It is currently available in the US and US territories. Today, we're announcing
a new and simpler way to provide for-sale vehicle inventory data to Google.

![Image showing how vehicle listing rich results can be shown on Google Search](/static/search/blog/images/vehicle-listing-rich-resut.png)

Now, car dealerships of all sizes can be eligible for vehicle listings on Google by using the
[vehicle listing markup](/search/docs/appearance/structured-data/vehicle-listing). The existing
[feed method](https://developers.google.com/vehicle-listings/reference/feed-specification)
remains a good option for car dealerships that are comfortable with creating and maintaining feed files.
We recommend using the markup for those who haven't yet signed up for vehicle listings on Google and prefer
a simpler setup via markup.

You can implement vehicle listing markup on your car details pages to provide basic car information along with
their availability. See our [documentation](/search/docs/appearance/structured-data/vehicle-listing)
for more details.

We're also making it easier to monitor and fix the structured data needed for this feature using the Search Console
reports and tools.

## Rich result reports in Search Console

To help you monitor markup issues, we are also beginning to support vehicle listing structured data in a new
[Rich result report](https://support.google.com/webmasters/answer/7552505)
in Search Console that shows valid and invalid items for pages with structured data.

![Screenshot of the new Vehicle listings rich result report in Search Console](/static/search/blog/images/vehicle-listings-status-report.png)

## Rich Results Test

You can also test your structured data using the [Rich Results Test](https://search.google.com/test/rich-results)
by submitting the URL of a page or a code snippet. Using the tool, you can confirm whether or not your markup
is valid instantly without waiting for Rich result reports to be updated.

![Screenshot of the new Vehicle listings validation in the rich results test](/static/search/blog/images/vehicle-listing-rich-resut-test.png)

We hope these additions will make it easier for car dealerships to connect with potential customers on Search. If you have any
questions or concerns, please reach out to us via the [Google Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category%3Astructured_data))
or on [Twitter](https://twitter.com/googlesearchc).
