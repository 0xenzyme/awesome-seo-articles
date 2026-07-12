---
title: "App deep linking with goo.gl"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-05-app-deep-linking-with-googl"
url: "https://developers.google.com/search/blog/2015/05/app-deep-linking-with-googl"
canonical: "https://developers.google.com/search/blog/2015/05/app-deep-linking-with-googl"
author: "Fabian Schlup, Software Engineer"
published: "2015-05-27T00:00:00+00:00"
updated: "2015-05-27T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:26:46+00:00"
status_code: 200
html_hash: "84692fdfc78fd198a7ea3e962e04a2f687ac70523b83a9ed43541fb5b4665e3b"
clean_word_count: 432
clean_char_count: 2581
---
# App deep linking with goo.gl

Starting now, goo.gl short links function as a single link you can use to all your
content—whether that content is in your Android app, iOS app, or website. Once you've taken
the necessary steps to set up
[App Indexing for Android and iOS](https://firebase.google.com/docs/app-indexing/),
goo.gl URLs will send users straight to the right page in your app if they have it installed, and
everyone else to your website. This will provide additional opportunities for your app users to
re-engage with your app.

This feature works for both new short URLs and retroactively, so any existing goo.gl short links
to your content will now also direct users to your app.

![](/static/search/blog/images/import/485076b48fd01ceb895200d8bbf95bda.png)

## Share links that 'do the right thing'

You can also make full use of this feature by integrating the
[URL Shortener API](/url-shortener)
into your app's share flow, so users can share links that automatically redirect to your native
app cross-platform. This will also allow others to embed links in their websites and apps which
deep link directly to your app.

Take Google Maps as an example. With the new cross-platform goo.gl links, the Maps share button
generates one link that provides the best possible sharing experience for everyone. When opened,
the link auto-detects the user's platform and if they have Maps installed. If the user has the app
installed, the short link opens the content directly in the Android or iOS Maps app. If the user
doesn't have the app installed or is on desktop, the short link opens the page on the Maps
website.

Try it out for yourself! Don't forget to use a phone with the Google Maps app installed:
[https://goo.gl/maps/xlWFj](https://www.google.com/maps?q=Google+Bldg+41,+1600+Amphitheatre+Pkwy,+Mountain+View,+CA+94043&ftid=0x808fba02f3d60bc5:0x6bc3b76cb42de9de).

## How to set it up

To set up app deep linking on goo.gl:

1. Complete the necessary steps to participate in App Indexing for Android and iOS on the
   [App Indexing site](https://firebase.google.com/docs/app-indexing/). Note that goo.gl deep
   links are open to all iOS developers, unlike deep links from Search currently. After this step,
   existing goo.gl short links will start deep linking to your app.
2. Optionally integrate the
   [URL Shortener API](/url-shortener)
   with your app's share flow, your email campaigns, etc. to programmatically generate links that
   will deep link directly back to your app.

We hope you enjoy this new functionality and happy cross-platform sharing!
