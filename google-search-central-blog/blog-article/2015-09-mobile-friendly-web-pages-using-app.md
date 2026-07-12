---
title: "Mobile-friendly web pages using app banners"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-09-mobile-friendly-web-pages-using-app"
url: "https://developers.google.com/search/blog/2015/09/mobile-friendly-web-pages-using-app"
canonical: "https://developers.google.com/search/blog/2015/09/mobile-friendly-web-pages-using-app"
author: "Daniel Bathgate, Software Engineer, Google Search."
published: "2015-09-01T00:00:00+00:00"
updated: "2015-09-01T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:27:31+00:00"
status_code: 200
html_hash: "1c2c64545dc56956ebf0c3b5d02b9e7b7e14a6ecceec67c57d3cbf092cdba277"
clean_word_count: 406
clean_char_count: 2762
---
# Mobile-friendly web pages using app banners

When it comes to search on mobile devices, users should get the most relevant answers, no matter
if the answer lives in an app or a web page. We've recently made it easier for users to
[find and discover apps](https://insidesearch.blogspot.com/2015/06/find-app-content-straight-from-google.html)
and
[mobile-friendly web pages](/search/blog/2015/02/finding-more-mobile-friendly-search).
However, sometimes a user may tap on a search result on a mobile device and see an app install
interstitial that hides a significant amount of content and prompts the user to install an app.
Our analysis shows that it is not a good search experience and can be frustrating for users
because they are expecting to see the content of the web page.

Starting today, we'll be updating the
[Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
to indicate that sites should avoid showing app install interstitials that hide a significant
amount of content on the transition from the search result page. The
[Mobile Usability report](https://search.google.com/search-console/mobile-usability)
in Search Console will show webmasters the number of pages across their site that have this issue.

After November 1, mobile web pages that show an app install interstitial that hides a significant
amount of content on the transition from the search result page will no longer be considered
mobile-friendly. This does not affect other types of interstitials. As an alternative to app
install interstitials, browsers provide ways to promote an app that are more user-friendly.

![App install interstitials that hide a significant amount of content provide a bad search experience](/static/search/blog/images/import/e0ddf74816f07e73c6177f4a6ab3b00d.png)
![App install banners are less intrusive and preferred](/static/search/blog/images/import/50976d07e96179a59b54609c476dff2e.png)

App install banners are supported by Safari (as
[Smart Banners](https://developer.apple.com/library/mac/documentation/AppleApplications/Reference/SafariWebContent/PromotingAppswithAppBanners/PromotingAppswithAppBanners))
and Chrome (as
[Native App Install Banners](/web/updates/2015/03/increasing-engagement-with-app-install-banners-in-chrome-for-android#native)).
Banners provide a consistent user interface for promoting an app and provide the user with the
ability to control their browsing experience. Webmasters can also use their own implementations
of app install banners as long as they don't block searchers from viewing the page's content.

If you have any questions, we're always happy to chat in the
[Webmaster Central Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:crawling_indexing_ranking)).
