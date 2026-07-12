---
title: "New reports for Special Announcements in Search Console"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2020-05-special-announcements-search-console"
url: "https://developers.google.com/search/blog/2020/05/special-announcements-search-console"
canonical: "https://developers.google.com/search/blog/2020/05/special-announcements-search-console"
author: "Daniel Waisberg, Moshe Samet"
published: "2020-05-05T00:00:00+00:00"
updated: "2020-05-05T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:36:54+00:00"
status_code: 200
html_hash: "4a2c5991428cd9c579d89dd59e65c8d3112a218a6e33f6746126dc4360525383"
clean_word_count: 441
clean_char_count: 3088
---
# New reports for Special Announcements in Search Console

Last month we introduced a new way for sites to
[highlight COVID-19 announcements](/search/blog/2020/04/highlight-covid-19-announcements-search)
on Google Search. At first, we're using this information to highlight announcements in Google
Search from health and government agency sites, to cover important updates like school closures
or stay-at-home directives.

Today we are announcing support for
[`SpecialAnnouncement`](/search/docs/appearance/structured-data/special-announcements)
in [Google Search Console](https://search.google.com/search-console), including new
reports to help you find any issues with your implementation and monitor how this rich result
type is performing. In addition we now also support the markup on the
[Rich Results Test](https://search.google.com/test/rich-results)
to review your existing URLs or debug your markup code before moving it to production.

## Special Announcements Enhancement report

A new report is now available in Search Console for sites that have implemented
`SpecialAnnouncement` structured data. The report allows you to see
errors, warnings, and valid pages for markup implemented on your site.

In addition, if you fix an issue, you can use the report to validate it, which will trigger a
process where Google recrawls your affected pages. Learn more about the
[Rich result status reports](https://support.google.com/webmasters/answer/7552505).

![Special Announcements Enhancement report](/static/search/blog/images/import/e262fb4bddc2f6da5b9c6a270fe20a49.png)

## Special Announcements appearance in Performance report

The Search Console Performance report now also allows you to see the performance of your
`SpecialAnnouncement` marked-up pages on Google Search. This means
that you can check the impressions, clicks and CTR results of your special announcement pages
and check their performance to understand how they are trending for any of the dimensions
available. Learn more about the
[Search appearance tab](https://support.google.com/webmasters/answer/7576553#by_search_appearance)
in the performance report.

![Special Announcements appearance in Performance report](/static/search/blog/images/import/9738e5cbb9c924e60839d6e9e6edc162.png)

## Special Announcements in Rich Results Test

After adding `SpecialAnnouncement` structured data to your pages, you
can test them using the [Rich Results Test tool](https://search.google.com/test/rich-results).
If you haven't published the markup on your site yet, you can also upload a piece of code to
check the markup. The test shows any errors or suggestions for your structured data.

![Special Announcements in Rich Results Test](/static/search/blog/images/import/10e186db47a98ba39ae97e50b6e1f262.png)

These new tools should make it easier to understand how your marked-up
`SpecialAnnouncement` pages perform on Search and to identify and fix
issues.

If you have any questions, check out the
[Google Webmasters community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)).
