---
title: "More control of Googlebot's crawl rate"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2008-12-more-control-of-googlebots-crawl-rate"
url: "https://developers.google.com/search/blog/2008/12/more-control-of-googlebots-crawl-rate"
canonical: "https://developers.google.com/search/blog/2008/12/more-control-of-googlebots-crawl-rate"
author: "Written By Pooja Shah, Software Engineer, Webmaster Tools Team"
published: "2008-12-04T00:00:00+00:00"
updated: "2008-12-04T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:56:05+00:00"
status_code: 200
html_hash: "10ebb940c1c17c96c5db8fca02ef788ad3a813a4b06cf42e66865e01d89fe50e"
clean_word_count: 416
clean_char_count: 2563
---
# More control of Googlebot's crawl rate

We've upgraded the crawl rate setting in
[Webmaster Tools](https://search.google.com/search-console)
so that webmasters experiencing problems with Googlebot can now provide us more specific
information. Crawl rate for your site determines the time used by Googlebot to crawl your site on
each visit. Our goal is to thoroughly crawl your site (so your pages can be indexed and returned
in search results!) without creating a noticeable impact on your server's bandwidth. While most
webmasters are fine using the default crawl setting (that is, no changes needed, more on that
below), some webmasters may have more specific needs.

[Googlebot](/search/docs/crawling-indexing/googlebot) employs sophisticated
algorithms that determine how much to crawl each site it visits. For a vast majority of sites,
it's probably best to choose the "Let Google determine my crawl rate" option, which is the
default. However, if you're an advanced user or if you're facing bandwidth issues with your
server, you can customize your crawl rate to the speed most optimal for your web server(s). The
custom crawl rate option allows you to provide Googlebot insight to the maximum number of
requests per second and the number of seconds between requests that you feel are best for your
environment.

![crawl rate feature in webmaster tools](/static/search/blog/images/archived_crawl-rate.png)

Googlebot determines the range of crawl rate values you'll have available in Webmaster Tools. This
is based on our understanding of your server's capabilities. This range may vary from one site to
another and across time based on several factors. Setting the crawl rate to a lower-than-default
value may affect the coverage and freshness of your site in Google's search results. However,
setting it to higher value than the default won't improve your coverage or ranking. If you do set
a custom crawl rate, the new rate will be in effect for 90 days after which it resets to Google's
recommended value.

You may use this setting only for root level sites and sites not hosted on a large domain like
blogspot.com (we have special settings assigned for them). To check the crawl rate setting, sign
in to
[Webmaster Tools](https://search.google.com/search-console)
and visit the Settings tab. If you have additional questions, visit the
[Webmaster Help Center](https://support.google.com/webmasters)
to learn more about how Google crawls your site or post your questions in the
[Webmaster Help Forum](https://support.google.com/webmasters/community).
