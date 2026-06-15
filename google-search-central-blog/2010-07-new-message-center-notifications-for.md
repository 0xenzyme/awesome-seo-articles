---
title: "New Message Center notifications for detecting an increase in Crawl Errors"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2010-07-new-message-center-notifications-for"
url: "https://developers.google.com/search/blog/2010/07/new-message-center-notifications-for"
canonical: "https://developers.google.com/search/blog/2010/07/new-message-center-notifications-for"
author: "Jonathan Simon"
published: "2010-07-26T00:00:00+00:00"
updated: "2010-07-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:07:51+00:00"
status_code: 200
html_hash: "31751fe11ad3374255e18b292a802707334081d015a58339159641c6edc17c3f"
clean_word_count: 275
clean_char_count: 1765
---
# New Message Center notifications for detecting an increase in Crawl Errors

When Googlebot crawls your site, it's expected that most URLs will return a `200`
response code, some a `404` response, some will be disallowed by robots.txt, etc.
Whenever we're unable to reach your content, we show this information in the
[Crawl errors](https://support.google.com/webmasters/answer/9679690)
section of Webmaster Tools (even though it might be intentional and not actually an error).
Continuing with our effort to provide useful and actionable information to webmasters, we're now
sending **SiteNotice** messages when we detect a significant increase in the number of crawl
errors impacting a specific site. These notifications are meant to alert you of potential
crawl-related issues and provide a sample set of URLs for diagnosing and fixing them.

A SiteNotice for a spike in the number of unreachable URLs, for example, will look like this:

![example sitenotice message in webmaster tools](/static/search/blog/images/import/42176d9367607a46ab5e758dd5836254.png)

We hope you find SiteNotices helpful for discovering and dealing with issues that, if left
unattended, could negatively affect your crawl coverage. You'll only receive these notifications
if you've verified your site in Webmaster Tools and we detect significant changes to the number of
crawl errors we encounter on your site. And if you don't want to miss out on any these important
messages, you can use the
[email forwarding feature](https://www.google.com/support/webmasters/bin/answer.py?answer=140528)
to receive these alerts in your inbox.

If you have any questions, please post them in our
[Webmaster Help Forum](https://support.google.com/webmasters/community)
or leave your comments below.
