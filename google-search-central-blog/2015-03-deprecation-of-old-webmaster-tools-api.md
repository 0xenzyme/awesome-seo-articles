---
title: "Deprecation of the old Webmaster Tools API"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2015-03-deprecation-of-old-webmaster-tools-api"
url: "https://developers.google.com/search/blog/2015/03/deprecation-of-old-webmaster-tools-api"
canonical: "https://developers.google.com/search/blog/2015/03/deprecation-of-old-webmaster-tools-api"
author: "John Mueller"
published: "2015-03-12T00:00:00+00:00"
updated: "2015-03-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:26:14+00:00"
status_code: 200
html_hash: "5f44e4359eb7bef06d3ad675359a136ba0bd0edf1a86fdcc5db6e50b72eec890"
clean_word_count: 195
clean_char_count: 1363
---
# Deprecation of the old Webmaster Tools API

Last fall we announced the
[new Webmaster Tools API](/search/blog/2014/09/an-update-to-webmaster-tools-api), which
helps you to automate a number of important aspects using code. With the
[pending shutdown of `ClientLogin`](https://googledevelopers.blogspot.com/2015/02/reminder-clientlogin-shutdown-scheduled.html),
we're going to turn down the
[old Webmaster Tools API](/search/blog/2008/06/get-cooking-with-webmaster-tools-api) on
April 20, 2015.

If you're still using the old API, getting started with the new one is fairly easy. The new API
covers everything from the old version except for messages and keywords. We have examples in
[Python](/webmaster-tools/v3/quickstart/quickstart-python),
[Java](/webmaster-tools/v3/quickstart/quickstart-java), as well as
[OACurl](/webmaster-tools/v3/quickstart/quickstart-oacurl)
(for command-line fans and quick testing). Additionally, there's the
[Site Verification API](/site-verification)
to add sites programmatically to your account. The
[Python search query data download](/search/blog/2011/12/download-search-queries-data-using)
will continue to be available for the moment, and replaced by an API in the upcoming quarters.

As always, should you have any questions, you can post in our
[Webmaster Help Forum](https://support.google.com/webmasters/go/community).
