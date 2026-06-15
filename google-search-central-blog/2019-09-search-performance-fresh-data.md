---
title: "Fresher data in your site's Search Performance report"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2019-09-search-performance-fresh-data"
url: "https://developers.google.com/search/blog/2019/09/search-performance-fresh-data"
canonical: "https://developers.google.com/search/blog/2019/09/search-performance-fresh-data"
author: "Ziv Hodak"
published: "2019-09-23T00:00:00+00:00"
updated: "2019-09-23T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:35:09+00:00"
status_code: 200
html_hash: "17aeb442905914e50bae0e59b10067f768fa7856a16d595753795433022104f2"
clean_word_count: 541
clean_char_count: 3493
---
# Fresher data in your site's Search Performance report

We analyzed our user feedback, and today would like to announce a new improvement to the report
based on  **users' #1 feature request**—improved data freshness!

The [Performance report](https://support.google.com/webmasters/answer/7576553)
helps webmasters and site owners better understand how their site performs on Google search, and
answer questions such as:

- General stats: How much traffic did my site get from Search and Discover?
- Search queries: What are my site's top and trending search queries?
- Top content: What are my site's most successful pages on Google search?
- Site's audiences: From which countries? From which devices—is it mostly mobile?
- Formats: What search formats does my site get (AMP, recipes, etc.)?

With the new fresh data, users can now see data as recent as less than a day old—a
significant improvement compared to the previous few days.

We hope this improved data freshness allows you to better monitor and track your site's
performance and addresses some important needs such as:

- Seeing your weekend performance on Monday morning - no need to wait until Wednesday.
- Checking on your site's stats first thing in the morning after, or even during, important days
  such as holidays, global events, and shopping days.
- Checking if your site's traffic rebounds soon after fixing an important technical issue.

![Fresh Data in Search Performance report](/static/search/blog/images/import/6df3320acfe64b4c69eed1084cd51767.png)

In addition, we updated the report to clearly communicate the data timezone (Pacific time zone).
This is useful when you'd like to interpret the data compared to your local time zone or integrate
it with other sources such as Google Analytics.

![Performance report date picker](/static/search/blog/images/import/4063cc035ad593d9fbb44e108671a7fd.png)

Each fresh data point will be replaced with the final data point after a few days. It is expected
that from time to time the fresh data might change a bit before being finalized.

The Search Analytics
[API](/webmaster-tools/search-console-api-original/v3/searchanalytics/query)
does not support fresh data yet. In addition, fresh data is not available on the Discover
performance report. As a result, properties that are eligible for Discover performance report will
not see fresh data in their Overview report. We hope to address these items in the future.

## Exporting performance data over time

We also heard your feedback about wanting a simple way to explore and export your performance
over time. Starting today, this is possible. Simply choose 'dates' in the table below the graph,
select the desired time frame, and explore the data in Search Console or export the chart. We
hope that this new feature will help you further explore your performance trends and changes
over time.

![Performance report now with 'dates' table](/static/search/blog/images/import/0e7807b320b8c5aeac34b1c63d53411b.png)

## In conclusion

We hope that this new fresh data will help you better monitor your site's performance and
identify trends, patterns and interesting changes much closer to when they happen. In addition,
we hope that the new date table dimension will assist you in exploring performance trends and
changes over time. If you have any questions or concerns, please reach out on the
[Webmaster Help Forum](https://support.google.com/webmasters/community) or on
[Twitter](https://twitter.com/googlesearchc).
