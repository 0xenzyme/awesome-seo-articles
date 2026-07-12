---
title: "App Indexing updates"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-04-app-indexing-updates"
url: "https://developers.google.com/search/blog/2014/04/app-indexing-updates"
canonical: "https://developers.google.com/search/blog/2014/04/app-indexing-updates"
author: "Michael Xu"
published: "2014-04-03T00:00:00+00:00"
updated: "2014-04-03T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:24:21+00:00"
status_code: 200
html_hash: "3f6804bfe264f39ca3a86f4991889bf27915821938e350b2e59f804932795616"
clean_word_count: 369
clean_char_count: 2392
---
# App Indexing updates

In October, we announced guidelines for
[App Indexing](/search/blog/2013/10/indexing-apps-just-like-websites)
for deep linking directly from Google Search results to your Android app. Thanks to all of you
that have expressed interest. We've just enabled
[20+ additional applications](https://insidesearch.blogspot.com/2014/04/accessing-your-app-content-in-google.html)
that users will soon see app deep links for in Search Results, and starting today we're making app
deep links to English content available globally.

![](/static/search/blog/images/import/5f7a5a75ced316567c77d13c12c0b2f8.png)

We're continuing to onboard more publishers in all languages. If you haven't added deep link
support to your Android app or specified these links on your website or in your Sitemaps, please
do so and then notify us by filling out this
[form](https://firebase.google.com/docs/app-indexing/).

Here are some best practices to consider when adding deep links to your sitemap or website:

- App deep links should only be included for
  [canonical](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  web URLs.
- Remember to specify an app deep link for your home page.
- Not all website URLs in a Sitemap need to have a corresponding app deep link. Do not include app
  deep links that aren't supported by your app.
- If you are a news site and use
  [News Sitemaps](/search/docs/crawling-indexing/sitemaps/news-sitemap), be sure to include your
  deep link annotations in the News Sitemaps, as well as your general Sitemaps.
- Don't provide annotations for deep links that execute native ARM code. This enables app indexing
  to work for all platforms.

When Google indexes content from your app, your app will need to make HTTP requests that it
usually makes under normal operation. These requests will appear to your servers as originating
from Googlebot. Therefore, your server's robots.txt file must be configured properly to allow
these requests.

Finally, please make sure the back button behavior of your app leads directly back to the search
results page.

For more details on implementation, visit our
[updated developer guidelines](https://firebase.google.com/docs/app-indexing/). And, as always, you
can ask questions on the
[mobile section of our webmaster forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:mobile_web)).
