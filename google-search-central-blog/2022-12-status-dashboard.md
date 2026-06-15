---
title: "Introducing the Google Search Status Dashboard"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2022-12-status-dashboard"
url: "https://developers.google.com/search/blog/2022/12/status-dashboard"
canonical: "https://developers.google.com/search/blog/2022/12/status-dashboard"
author: "Gary Illyes"
published: "2022-12-14T00:00:00+00:00"
updated: "2022-12-14T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:41:20+00:00"
status_code: 200
html_hash: "7da6589e979610dcc6cc8d08be89818c56a3698d375fc14d74dd70c59affcf88"
clean_word_count: 538
clean_char_count: 3489
---
# Introducing the Google Search Status Dashboard

As we head into 2023, we want to introduce another tool for the public to understand the most
current status of systems which impact Search—crawling, indexing, and serving. While system
disruptions are extremely rare, we want to be transparent when they do happen. In the past, we've
worked with our
[Site Reliability Engineers (SRE)](https://sre.google/) to
externalize these disruptions on our
[Google Search Central Twitter](https://twitter.com/googlesearchc)
account. Today, we're introducing the
[Google Search Status Dashboard](https://status.search.google.com/)
to communicate the status of Search going forward.

Over the past couple years we've been working with our SREs on improved ways to make information
about major incidents generally accessible and useful. The goal was to make reporting issues
quick, accurate, and easy. As a result, we have launched a new
[status dashboard](https://status.search.google.com/) and
simplified the process of communicating during incidents.

This dashboard reports widespread issues occurring in the last 7 days, with some details and the
current status of the incident. A widespread issue means there's a systemic problem with a
[Search system](/search/docs/advanced/guidelines/how-search-works) affecting a large
number of sites or Search users. Typically these kinds of issues are very visible externally, and
internally the
[SREs' monitoring and alerting mechanisms](https://sre.google/sre-book/monitoring-distributed-systems/)
are working behind the scenes to flag the issues.

![The Google Search Status dashboard showing no ongoing incidents](/static/search/blog/images/searchstatusdashboard.png)

The dashboard has a number of features that you might already be aware of from other Google status
dashboards, such as an
[RSS feed](https://status.search.google.com/en/feed.atom)
you can subscribe to and
[view of historical data](https://status.search.google.com/summary).

### How we communicate incidents and updates

Once we confirm with SREs that there's an ongoing, widespread issue in Search, we aim to post an
incident on the dashboard within an hour, and consecutive updates to the incident within 12 hours.
Unlike with a traditional automated dashboard, our global staff reports these updates. The start
time of the incident is generally when we managed to confirm the issue.

Outside of the traditional status update you might see, we will also try to provide more
information that might resolve the solution. For example, in the hypothetical scenario that the
nameserver handling domain name resolution for millions of sites refuses Googlebot's connection
requests, we may post an update saying that changing nameservers may mitigate the issue sites are
experiencing. Of course with any issue, we will keep posting updates to the incident—with
mitigation possibilities when available—until the incident is resolved.

We consider an incident resolved when our engineers have made changes that will end the impact on
the system. While this means that the system itself is now healthy, sites may experience effects
for some time until they're reprocessed, depending on the type of incident.

If you want to learn more about the dashboard, we have a
[dedicated page for the Search Status dashboard](/search/help/status-dashboard)
on Google Search Central. If you want to leave some feedback about the dashboard, tweet at us
[@googlesearchc](https://twitter.com/googlesearchc).
