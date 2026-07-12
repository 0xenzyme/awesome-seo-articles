---
title: "New reports for review snippets in Search Console"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2020-02-review-snippets"
url: "https://developers.google.com/search/blog/2020/02/review-snippets"
canonical: "https://developers.google.com/search/blog/2020/02/review-snippets"
author: "Tomer Hodadi and Yuval Kurtser, Search Console engineering team"
published: "2020-02-10T00:00:00+00:00"
updated: "2020-02-10T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:36:09+00:00"
status_code: 200
html_hash: "85fc5c249c067b78b17777a439c7b9fc725e985603f635ceba3ede49b58c0af3"
clean_word_count: 581
clean_char_count: 3830
---
# New reports for review snippets in Search Console

A [review snippet](/search/docs/appearance/structured-data/review-snippet)
is a short excerpt of a review or a rating from a website, usually an average of the combined
rating scores from many reviewers. This is one of the most used structured data types on the
web, used by millions of web sites for many content types such as
[Book](https://schema.org/Book),
[Movie](https://schema.org/Movie),
[Event](https://schema.org/Event),
[Product](https://schema.org/Product) and more.

When Google finds valid reviews or ratings markup, we may show a rich result that includes stars
and other summary info. This rich result can appear directly on search results or as part of
a Google Knowledge panel, as shown in the screenshots below.

Today we are announcing support for review snippets in
[Google Search Console](https://search.google.com/search-console), including new
reports to help you find any issues with your implementation and monitor how this rich result
type is improving your performance. You can also use the
[Rich Results Test](https://search.google.com/test/rich-results)
to review your existing URLs or debug your markup code before moving it to production.

![Review snippets in Google Search results](/static/search/blog/images/import/b2a668d1a7ead99e4356d5de8cc4d60f.png)

## Review snippet Enhancement report

To help site owners make the most of their reviews, a new review snippet report is now available
in Search Console for sites that have implemented reviews or ratings
[structured data](/search/docs/appearance/structured-data/review-snippet#structured-data-type-definitions).
The report allows you to see errors, warnings, and valid pages for markup implemented on your site.

In addition, if you fix an issue, you can use the report to validate it, which will trigger a
process where Google recrawls your affected pages. The report is covering all the content
types currently supported as review snippets. Learn more about the
[Rich result status reports](https://support.google.com/webmasters/answer/7552505).

![Review snippet Enhancement report in Search Console](/static/search/blog/images/import/f31479e47cebca8a3379d2835a170b74.png)

## Review snippet appearance in the Performance report

The Search Console
[Performance report](https://support.google.com/webmasters/answer/7576553)
now allows you to see the performance of your review or rating marked-up pages on Google Search
and Discover using the new "Review snippet" search appearance filter.

![Review snippet appearance in the Performance report in Search Console](/static/search/blog/images/import/f577e1261db545f9908aedba43127b08.png)

This means that you can check the impressions, clicks and CTR results of your review snippet
pages and check their performance to understand how they are trending for any of the dimensions
available. For example you can
[filter your data](https://support.google.com/webmasters/answer/7576553#filteringdata)
to see which queries, pages, countries and devices are bringing your review snippets traffic.

## Review snippet in the Rich Results Test

![Review snippet in the Rich Results Test](/static/search/blog/images/import/43f0a9c498836df46d36dbcb7c699b97.png)

After adding review snippets structured data to your pages, you can test them using the
[Rich Results Test](https://search.google.com/test/rich-results). You can test
a code snippet or submit a URL of a page. The test shows any errors or suggestions for your structured data.

These new tools should make it easier to understand how your marked-up review snippet pages
perform on Search and to identify and fix review issues.

If you have any questions, check out the
[Google Webmasters community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)).
