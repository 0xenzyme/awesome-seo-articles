---
title: "Structured Data dashboard: new markup error reports for easier debugging"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2013-12-structured-data-dashboard-new-markup_12"
url: "https://developers.google.com/search/blog/2013/12/structured-data-dashboard-new-markup_12"
canonical: "https://developers.google.com/search/blog/2013/12/structured-data-dashboard-new-markup_12"
author: "Mariya Moeva"
published: "2013-12-12T00:00:00+00:00"
updated: "2013-12-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2013_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:23:20+00:00"
status_code: 200
html_hash: "8fe0c0ac574a330d31661e4e226e29f71d42c96f5f05e8a503663090677e5064"
clean_word_count: 575
clean_char_count: 3640
---
# Structured Data dashboard: new markup error reports for easier debugging

Since we
[launched the Structured Data dashboard](/search/blog/2012/07/introducing-structured-data-dashboard)
last year, it has quickly become one of the most popular features in Webmaster Tools. We've been
working to expand it and make it even easier to debug issues so that you can see how Google
understands the marked-up content on your site.

Starting today, you can see items with errors in the Structured Data dashboard. This new feature
is a result of a collaboration with webmasters, whom we invited in June to>register as early
testers of markup error reporting in Webmaster Tools. We've incorporated their feedback to improve
the functionality of the Structured Data dashboard.

An "item" here represents one top-level structured data element (nested items are not counted)
tagged in the HTML code. They are grouped by data type and ordered by number of errors:

![Structured data errors view in Webmaster Tools](/static/search/blog/images/import/77243324a5a7b0bace61978a048a8a42.png)

We've added a separate scale for the errors on the right side of the graph in the dashboard, so
you can compare items and errors over time. This can be useful to spot connections between changes
you may have made on your site and markup errors that are appearing (or disappearing!).

Our data pipelines have also been updated for more comprehensive reporting, so you may initially
see fewer data points in the chronological graph.

## How to debug markup implementation errors

1. To investigate an issue with a specific content type, click on it and we'll show you the markup
   errors we've found for that type. You can see all of them at once, or filter by error type using
   the tabs at the top:
![Over-time trend of Structured Data errors in Search Console](/static/search/blog/images/import/c59b94c7e8a6fe79b0a845d23dc7f403.png)2. Check to see if the markup meets the
   [implementation guidelines for each content type](/search/docs/appearance/structured-data/intro-structured-data).
   In our example case (events markup), some of the items are missing a `startDate` or
   `name` property. We also surface missing properties for nested content types (for
   example, a review item inside a product item)—in this case, this is the
   `lowprice` property.
3. Click on URLs in the table to see details about what markup we've detected when we crawled the
   page last and what's missing. You'll can also use the "Test live data" button to test your
   markup in the
   [Structured Data Testing Tool](https://www.google.com/webmasters/tools/richsnippets).
   Often when checking a bunch of URLs, you're likely to spot a common issue that you can solve
   with a single change (for example, by adjusting a setting or template in your content management
   system).
![A detailed description of a Structured data error shown in Webmaster tools](/static/search/blog/images/import/68e526978b0cae0e00136c8f5f8b5d47.png)4. Fix the issues and test the new implementation in the
   [Structured Data Testing Tool](https://www.google.com/webmasters/tools/richsnippets).
   After the pages are recrawled and reprocessed, the changes will be reflected in the Structured
   Data dashboard.

We hope this new feature helps you manage the structured data markup on your site better. We will
continue to add more error types in the coming months. Meanwhile, we look forward to your comments
and questions here or in the dedicated Structured Data section of the
[Webmaster Help forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:structured_data)).
