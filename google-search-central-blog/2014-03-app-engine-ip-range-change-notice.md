---
title: "App Engine IP Range Change Notice"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2014-03-app-engine-ip-range-change-notice"
url: "https://developers.google.com/search/blog/2014/03/app-engine-ip-range-change-notice"
canonical: "https://developers.google.com/search/blog/2014/03/app-engine-ip-range-change-notice"
author: "the Google App Engine Team"
published: "2014-03-18T00:00:00+00:00"
updated: "2014-03-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:23:53+00:00"
status_code: 200
html_hash: "cfd425ded685f72fd3b1d97a26e5d751caa39e100ac813c620c420346a65261a"
clean_word_count: 196
clean_char_count: 1281
---
# App Engine IP Range Change Notice

Google uses a wide range of IP addresses for its different services, and the addresses may change
without notification.
[Google App Engine](https://cloud.google.com/products/app-engine/)
is a Platform as a Service offering which hosts a wide variety of 3rd party applications. This
post announces changes in the IP address range and headers used by the Google App Engine
`URLFetch` (outbound HTTP) and outbound sockets APIs.

While we recommend that App Engine IP ranges not be used to filter inbound requests, we are aware
that some services have created filters that rely on specific addresses. Google App Engine will be
changing its IP range beginning this month. Please see
[these instructions](/appengine/kb/general#static-ip)
to determine App Engine's IP range.

Additionally, the HTTP
[`User-Agent` header string](/appengine/docs/python/urlfetch#Python_Request_headers)
that historically allowed identification of individual App Engine applications should no longer
be relied on to identify the application. With the introduction of outbound
[sockets for App Engine](/appengine/docs/java/sockets),
applications may now make HTTP requests without using the `URLFetch` API, and those
requests may set a `User-Agent` of their own choosing.
