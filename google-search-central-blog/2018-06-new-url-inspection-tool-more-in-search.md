---
title: "New URL inspection tool and more in Search Console"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2018-06-new-url-inspection-tool-more-in-search"
url: "https://developers.google.com/search/blog/2018/06/new-url-inspection-tool-more-in-search"
canonical: "https://developers.google.com/search/blog/2018/06/new-url-inspection-tool-more-in-search"
author: "Roman Kecher and Sion Schori - Search Console engineers"
published: "2018-06-25T00:00:00+00:00"
updated: "2018-06-25T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2018_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:32:30+00:00"
status_code: 200
html_hash: "93ae5e36836586410fbf6647e359670e137ce2fb9dc45ee88ea2f4d4faf771a7"
clean_word_count: 618
clean_char_count: 3952
---
# New URL inspection tool and more in Search Console

A few months ago, we introduced the
[new Search Console](/search/blog/2018/01/introducing-new-search-console). Here are
some updates on how it's progressing.

## Welcome "URL inspection" tool

One of our most common user requests in Search Console is for more details on how Google Search
sees a specific URL. We listened, and today we've started launching a new tool,
[URL inspection](https://support.google.com/webmasters/answer/9012289),
to provide these details so Search becomes more transparent. The URL Inspection tool provides
detailed
[crawl, index, and serving information](https://support.google.com/webmasters/answer/70897)
about your pages, directly from the Google index.

Enter a URL that you own to learn the last crawl date and status, any crawling or indexing errors,
and the canonical URL for that page. If the page was successfully indexed, you can see information
and status about any enhancements we found on the page, such as linked AMP version or rich results
like Recipes and Jobs.

![URL is indexed with valid AMP enhancement](/static/search/blog/images/import/1872f42d62e2252bb0239bb68f378edc.png)

URL is indexed with valid AMP enhancement

If a page isn't indexed, you can learn why. The new report includes information about
[`noindex` robots `meta` tags](/search/docs/crawling-indexing/block-indexing) and Google's
canonical URL for the page.

![URL is not indexed due to noindex meta tag in the HTML](/static/search/blog/images/import/0734c771b5baf466eca8f6e3ce8c74eb.png)

URL is not indexed due to `noindex` `meta` tag in the HTML

A single click can take you to the issue report showing all other pages affected by the same issue
to help you track down and fix common bugs.

We hope that the URL Inspection tool will help you debug issues with new or existing pages in the
Google index. We began rolling it out today; it will become available to all users in the coming
weeks.

## More exciting updates

In addition to the launch of URL inspection, we have a few more features and reports we recently
launched to the new Search Console:

- **16 months of traffic data**: The
  [Search Analytics API](/webmaster-tools/search-console-api-original/v3/searchanalytics)
  now returns 16 months of data, just like the
  [Performance report](https://support.google.com/webmasters/answer/7576553).
- **Recipe report**: The
  [Recipe report](https://support.google.com/webmasters/answer/7552505)
  help you fix structured data issues affecting recipes rich results. Use our
  [task-oriented interface](/search/blog/2018/01/introducing-new-search-console) to
  test and validate your fixes; we will keep you informed on your progress using messages.
- **New Search Appearance filters in Search Analytics**: The
  [performance](https://support.google.com/webmasters/answer/7576553)
  report now gives you more visibility on new search appearance results, including
  [Web Light](https://support.google.com/webmasters/answer/6211428)
  and
  [Google Play Instant](https://developer.android.com/topic/google-play-instant/)
  results.

## Thank you for your feedback

We are constantly reading your feedback, conducting surveys, and monitoring usage statistics of
the new Search Console. We are happy to see so many of you using the new
[issue validation flow](/search/blog/2018/01/introducing-new-search-console#enhance)
in Index Coverage and the AMP report. We notice that issues tend to get fixed quicker when you use
these tools. We also see that you appreciate the updates on the validation process that we provide
by email or on the validation details page.

We want to thank everyone who provided feedback: it has helped us improve our flows and fix bugs
on our side.

## More to come

The new Search Console is still beta, but it's adding features and reports every month. Please
keep sharing your feedback through the various channels and let us know how we're doing.
