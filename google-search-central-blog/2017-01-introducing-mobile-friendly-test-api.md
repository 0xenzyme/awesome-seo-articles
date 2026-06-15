---
title: "Introducing the Mobile-Friendly Test API"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2017-01-introducing-mobile-friendly-test-api"
url: "https://developers.google.com/search/blog/2017/01/introducing-mobile-friendly-test-api"
canonical: "https://developers.google.com/search/blog/2017/01/introducing-mobile-friendly-test-api"
author: "John Mueller"
published: "2017-01-31T00:00:00+00:00"
updated: "2017-01-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:29:58+00:00"
status_code: 200
html_hash: "9d110e8b4800e374cc5a5e61aef9dcf0e93874f8dd4d8492994e95c2bfb5cae3"
clean_word_count: 218
clean_char_count: 1403
---
# Introducing the Mobile-Friendly Test API

With so many users on mobile devices, having a mobile-friendly web is important to us all. The
[Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
is a great way to check individual pages manually. We're happy to announce that this test is now
available via API as well.

The
[Mobile-Friendly Test API](/webmaster-tools/search-console-api)
lets you test URLs using automated tools. For example, you could use it to monitor important pages
in your website in order to prevent accidental regressions in templates that you use. The
[API method](/webmaster-tools/search-console-api/reference/rest/v1/urlTestingTools.mobileFriendlyTest/run)
runs all tests, and returns the same information - including a list of the blocked URLs - as the
manual test. The documentation includes simple samples to help get you started quickly.

![](/static/search/blog/images/import/26374334ddd97424a137974fef057931.png)

We hope this API makes it easier to check your pages for mobile-friendliness and to get any such
issues resolved faster. We'd love to hear how you use the API—you can post in our
[forum](https://support.google.com/webmasters/go/community), and you
can link to any code or implementation that you've set up! As always, if you have any questions,
you can drop by our
[webmaster help forum](https://support.google.com/webmasters/go/community).
