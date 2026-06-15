---
title: "How we use spam reports"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-09-how-we-use-spam-reports"
url: "https://developers.google.com/search/blog/2007/09/how-we-use-spam-reports"
canonical: "https://developers.google.com/search/blog/2007/09/how-we-use-spam-reports"
author: "Jianfei Zhu, WebSpam Group"
published: "2007-09-01"
updated: "2007-09-01"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:50:12+00:00"
status_code: 200
html_hash: "e7d2ec78e9212c29e73d41a46228b9237c0e076d2ed13f3abd8f1d4bff325170"
clean_word_count: 640
clean_char_count: 4083
---
# How we use spam reports

2007-09-01

[Google Webmaster Tools](https://search.google.com/search-console)
not only help us communicate with webmasters, but also provide a channel for you to
[inform us about spam sites](/search/docs/advanced/guidelines/report-spam) you find
online. Thanks to you, we've received many spam reports that have helped us improve search quality
by showing more relevant, useful sites in our results.

It's easy to submit a spam report via either of two channels, authenticated and unauthenticated.
We give a higher priority to the reports that are submitted through an
[authenticated channel such as Webmaster Tools](/search/docs/advanced/guidelines/report-spam "authenticated channel such as Webmaster Tools").
Or you can
[submit unauthenticated reports](/search/docs/advanced/guidelines/report-spam "submit unauthenticated reports").
Since the unauthenticated reports are reported anonymously, we may give it lower priority to
process.

Here's how a spam report submitted from Webmaster Tools is processed:

## We evaluate the spam report

We take spam reports very seriously, and we have dedicated staff to timely process reports. We
primarily evaluate spam reports in reference to our
[webmaster guidelines](/search/docs/essentials "webmaster guidelines"). We
determine whether we agree or disagree with the user's report.

A spam site commonly uses illicit techniques to mislead search engines to (mis)lead users to
certain websites. The Webmaster Guidelines cover most (but not all) common forms of behavior that
we consider deceptive or manipulative. We suggest you review our webmaster guidelines listed in
our [Webmaster Help Center](/search). These will help you create a search-engine
friendly website without spam.

There are cases where we disagree with the spam report's evaluation, and those reports are then
disregarded. The confirmed reports are forwarded to our engineering teams.

## We take action on confirmed spam reports

We take action on many confirmed spam sites, either manually and/or algorithmically. Furthermore,
the extent of our action is dependent on the severity of the violation—a confirmed spam
report doesn't necessarily mean the entire site will be removed from the index.

### Taking action on spam by improving our algorithms

It's most efficient for us to combat spam through our algorithms. We use spam reports about one
site to create algorithmic improvements detecting spam in all sites similar to the report. We
then extensively test our changes before we push our new code into production. This engineering
process takes time. When people ask the question "Why haven't you penalized the spam site I've
reported?", if we confirmed their spam report, then it's likely that we're working, or will be
working, on an algorithmic solution.

### Taking manual action on a spam site

We may also take manual action on confirmed spam sites. This process is obviously much faster,
but it's not as robust a method to improve our search quality as the algorithmic approach.

## We can contact webmasters to correct their site

If we believe that a reported spam site is in violation of the webmaster guidelines but is
otherwise legitimate, we may try to contact the webmaster to correct their site. We contact
webmasters [via email](/search/blog/2007/08/update-on-penalty-notifications "via email") and,
if they have a
[verified site](https://www.google.com/support/webmasters/bin/topic.py?topic=8472)
in Webmaster Tools, we can also send them a note through the
[Message Center](https://www.google.com/support/webmasters/bin/answer.py?answer=61504&hl=en).

Our goal is to deliver the most relevant results to users. We hope that our users and webmasters
keep reporting spam sites, as it helps us to improve our algorithms and improve search quality.
If you have questions about what's spam, visit our Help Center or post your question in our
[discussion group](https://support.google.com/webmasters/community).
And, of course, if you find a spam site,
[please let us know](/search/docs/advanced/guidelines/report-spam)!
