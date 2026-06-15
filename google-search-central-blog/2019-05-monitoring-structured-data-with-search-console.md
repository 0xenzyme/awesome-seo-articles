---
title: "Monitoring structured data with Search Console"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2019-05-monitoring-structured-data-with-search-console"
url: "https://developers.google.com/search/blog/2019/05/monitoring-structured-data-with-search-console"
canonical: "https://developers.google.com/search/blog/2019/05/monitoring-structured-data-with-search-console"
author: "Daniel Waisberg"
published: "2019-05-02T00:00:00+00:00"
updated: "2019-05-02T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:34:08+00:00"
status_code: 200
html_hash: "f223b9bd0c99e8644c9c4dddfe61165ce0c89913765a354bbb59d6618fe2edcb"
clean_word_count: 896
clean_char_count: 5629
---
# Monitoring structured data with Search Console

In our
[previous post](/search/blog/2019/04/enriching-search-results-structured-data)
in the structured data series, we discussed what structured data is and why you should add it to
your site. We are committed to structured data and continue to enhance related Search features and
improve our tools - that's why we have been
[creating solutions](/s/results/search/blog/?q=structured%20data)
to help webmasters and developers implement and diagnose structured data.

This post focuses on what you can do with Search Console to monitor and make the most out of
structured data for your site. In addition, we have some new features that will help you even
more. Below are the new additions, read on to learn more about them.

1. Unparsable structured data is a new report that aggregates structured data syntax errors.
2. New enhancement reports for
   [Sitelinks searchbox](/search/docs/appearance/structured-data/sitelinks-searchbox)
   and
   [Logo](/search/docs/appearance/structured-data/organization#logo).

## Monitoring overall structured data performance

Every time Search Console detects a new issue related to structured data on a website, we send an
email to account owners - but if an existing issue gets worse, it won't trigger an email, so it is
still important for you to check your account sporadically.

This is not something you need to do every day, but we recommend you check it once in a while to
make sure everything is working as intended. If your website development has defined cycles, it
might be a good practice to log in to Search Console after changes are made to the website to
monitor your performance.

If you'd like to have an overall idea of all the errors for a specific structured data feature in
your site, you can navigate to the Enhancements menu in the left sidebar and click a feature.
You'll find a summary of all errors and warnings, as well as the valid items.

As mentioned above, we added a new set of reports to help you understand more types of structured
data on your site:
[Sitelinks searchbox](/search/docs/appearance/structured-data/sitelinks-searchbox)
and
[Logo](/search/docs/appearance/structured-data/organization#logo). They are joining the existing set
of reports on Recipe, Event, Job Posting and others. You can read more about the reports in the
[Search Console Help Center](https://support.google.com/webmasters/answer/7552505).

Here's an example of an Enhancement report, note that you can only see enhancements that have been
detected in your pages. The report helps you with the following actions:

- Review the trends of errors, warnings and valid items: To view each status issue separately,
  click the colored boxes above the bar chart.
- Review warnings and errors per page: To see examples of pages which are currently affected by
  the issues, click a specific row below the bar chart.

![Enhancements report](/static/search/blog/images/import/a4355af8aeb7aafcc7933e54c92e54b7.png)

We are also happy to launch the Unparsable Structured Data report, which aggregates parsing issues
such as structured data syntax errors that prevented Google from identifying the feature type.
That is the reason these issues are aggregated here instead of the intended specific feature
report.

Check this report to see if Google was unable to parse any of the structured data you tried to add
to your site. Parsing issues could point you to lost opportunities for rich results for your site.
Below is a screenshot showing how the report looks like. You can
[access the report directly](https://search.google.com/search-console/unknown-type)
and read more about the report in
[our help center](https://support.google.com/webmasters/answer/9166415).

![Unparsable Structured Data report](/static/search/blog/images/import/f4c386792e12a7658e39ee445136899a.png)

## Testing structured data on a URL level

To make sure your pages were processed correctly and are eligible for rich results or as a way to
diagnose why some rich result are not surfacing for a specific URL, you can use the
[URL Inspection tool](https://search.google.com/search-console/inspect).
This tool helps you understand areas of improvement at a URL level and helps you get an idea on
where to focus.

When you paste a URL into the search box at the top of Search Console, you can find what's working
properly and warnings or errors related to your structured data in the enhancements section, as
seen below for Recipes.

![URL Inspection tool](/static/search/blog/images/import/3cd5180fbfcf116f1ed93b220ee1fad1.png)

In the screenshot above, there is an error related to Recipes. If you click Recipes, information
about the error displays, and you can click the little chart icon to the right of the error to
learn more about it.

Once you understand and fix the error, you can click Validate Fix (see screenshot below) so Google
can start validating whether the issue is indeed fixed. When you click the Validate Fix button,
Google runs several instantaneous tests. If your pages don't pass this test, Search Console
provides you with an immediate notification. Otherwise, Search Console reprocesses the rest of the
affected pages.

![Structured data error detail](/static/search/blog/images/import/99e3b7536859da26f39bc3414d0efc7f.png)

We would love to hear your feedback on how Search Console has helped you and how it can help you
even more with structured data. Send us feedback through
[Twitter](https://twitter.com/googlesearchc) or the
[Webmaster forum](https://support.google.com/webmasters/threads?thread_filter=(category:structured_data)).
