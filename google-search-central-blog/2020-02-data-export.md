---
title: "More and better data export in Search Console"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2020-02-data-export"
url: "https://developers.google.com/search/blog/2020/02/data-export"
canonical: "https://developers.google.com/search/blog/2020/02/data-export"
author: "Daniel Waisberg"
published: "2020-02-26T00:00:00+00:00"
updated: "2020-02-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:36:04+00:00"
status_code: 200
html_hash: "cfc3cbb13ec0cfc5e9024bf5977252a805230281002fe59f317cfcd364ca76ac"
clean_word_count: 864
clean_char_count: 5395
---
# More and better data export in Search Console

We have heard users ask for better download capabilities in Search Console loud and clear - so
we're happy to let you know that more and better data is available to export.

You'll now be able to download the complete information you see in almost all Search Console
reports (instead of just specific table views). We believe that this data will be much easier
to read outside SC and store it for your future reference (if needed). You'll find a section
at the end of this post describing other ways to use your Search Console data outside the tool.

## Enhancement reports and more

When exporting data from a report, for example AMP status, you'll now be able to export the data
behind the charts, not only the details table (as previously). This means that in addition to
the list of issues and their affected pages, you'll also see a daily breakdown of your pages,
their status, and impressions received by them on Google Search results. If you are exporting
data from a specific drill-down view, you can see the details describing this view in the
exported file.

If you choose Google Sheets or Excel (new!) you'll get a spreadsheet with two tabs, and if you
choose to download as csv, you'll get a zip file with two csv files.

Here is a
[sample
dataset](https://docs.google.com/spreadsheets/d/1aZD7eAqjiIYAPc8PewVsJZnrErvOI5CFXu9x9fubiNY/) downloaded from the AMP status report. We changed the titles of the spreadsheet to
be descriptive for this post, but the original title includes the domain name, the report, and the date of the export.

![AMP report export sample](/static/search/blog/images/import/f14dc9670dc3e558faf7959126075ad7.png)

## Performance report

When it comes to Performance data, we have two improvements:

1. You can now download the content of all tabs with one click. This means that you'll now get the
   data on Queries, Pages, Countries, Devices, Search appearances and Dates, all together. The
   download output is the same as explained above, Google sheets or Excel spreadsheet with
   multiple tabs and csv files compressed in a zip file.
2. Along with the performance data, you'll have an extra tab (or csv file) called "Filters", which
   shows which filters were applied when the data was exported.

Here is a
[sample dataset](https://docs.google.com/spreadsheets/d/1A37a2Pf5mIRY7WvDIFOCWlCrOjsD0ZMzE2FL-6RxmNg/)
downloaded from the Performance report.

![Performance on Search export sample](/static/search/blog/images/import/7b0156bffe78c685db50d04bc1705f00.png)

## Additional ways to use Search Console data outside the tool

Since we're talking about exporting data, we thought we'd take the opportunity to talk about
other ways you can currently use Search Console data outside the tool. You might want to do this
if you have a specific use case that is important to your company, such as joining the data with
another dataset, performing an advanced analysis, or visualizing the data in a different way.
There are two options, depending on the data you want and your technical level.

### Search Console API

If you have a technical background, or a developer in your company can help you, you might
consider using the
[Search Console API](/webmaster-tools) to view, add, or
remove properties and sitemaps, and to run advanced queries for Google Search results data.

We have plenty of documentation on the subject, but here are some links that might be useful to
you if you're starting now:

1. The [Overview and prerequisites
   guide](/webmaster-tools/v1/prereqs) walks you through the things you should do before writing your first client
   application. You'll also find more advanced guides in the sidebar of this section, for example
   a guide on how to
   [query all your
   search data](/webmaster-tools/v1/how-tos/all-your-data).
2. The [reference section](/webmaster-tools/v1/api_reference_index)
   provides details on query parameters, usage limits and errors returned by the API.
3. The [API samples](/webmaster-tools/v1/libraries) provides
   links to sample code for several programming languages, a great way to get up and running.

### Google Data Studio

[Google Data Studio](https://marketingplatform.google.com/about/data-studio/)
is a dashboarding solution that helps you unify data from different data sources, explore it, and
tell impactful data stories. The tool provides a
[Search Console connector](https://support.google.com/datastudio/answer/7314895)
to import various metrics and dimensions into your dashboard. This can be valuable if you'd like
to see Search Console data side-by-side with data from other tools.

If you'd like to give it a try, you can use
[this template](https://datastudio.google.com/c/reporting/0B_U5RNpwhcE6QXg4SXFBVGUwMjg/page/6zXD/preview)
to visualize your data - click "use template" at the top right corner of the page
to connect to your data. To learn more about how to use the report and which insights you might
find in it, check this
[step-by-step guide](https://online-behavior.com/analytics/search-console-data-studio).
If you just want to play with it, here's a report based on that template with sample data.

Let us know on [Twitter](https://twitter.com/googlesearchc)
if you have interesting use cases or comments about the new download capabilities, or about using
Search Console data in general. And enjoy the enhanced data!
