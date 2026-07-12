---
title: "A new way to enable video key moments in Search"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2021-07-new-way-key-moments"
url: "https://developers.google.com/search/blog/2021/07/new-way-key-moments"
canonical: "https://developers.google.com/search/blog/2021/07/new-way-key-moments"
author: "Danielle Marshak"
published: "2021-07-19T00:00:00+00:00"
updated: "2021-07-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:39:34+00:00"
status_code: 200
html_hash: "43bb6cce555c9e218fad6386f8a018acda82085cf52baa994133f6a7728e23d0"
clean_word_count: 424
clean_char_count: 2702
---
# A new way to enable video key moments in Search

Since [video key moments](/search/docs/appearance/video#key-moments) first
launched in 2019, we've continued to expand and improve the feature. We've evolved the design and
brought key moments to more videos, including mobile and desktop, across all regions where Google
Search is available. Key moments are helping more people connect directly with the most relevant
segments of videos, and navigate them like chapters in a book.

Today, we're launching a new way for you to enable key moments for videos on your site, without
the effort of manually labeling each segment. All you have to do is tell Google the URL pattern
for skipping to a specific timestamp within your video. Google will then use AI to identify key
moments in the video, and display links directly to those moments in Search results.

![key moments in Google Search](/static/search/blog/images/key-moments-example1.png)
![key moments in Google Search](/static/search/blog/images/key-moments-example2.png)

We first [announced](/search/blog/2021/05/search-io-2021) the [`SeekToAction`](/search/docs/appearance/structured-data/video#seek)
beta test during Google I/O, and as of today we're moving the feature out of beta and supporting
this markup for any site with videos. Here are a few tips to keep in mind when implementing this
markup:

- Your URLs must have the ability to deep link into some point other than the start point in the
  video. For example, `https://www.example.com/example?t=30` starts 30 seconds into a
  video.
- Use [`SeekToAction` markup](/search/docs/appearance/structured-data/video#seek) on every
  video page where you'd like Google to automatically identify key moments, and follow our
  additional [guidelines](/search/docs/appearance/structured-data/video#clip-guidelines). Here's a
  detailed [example](/search/docs/appearance/structured-data/video#seektoaction).
- To automatically identify key moments in your video, Google must be able to [fetch
  your video content files](/search/docs/appearance/video#allow-fetch).

Note that `SeekToAction` markup applies only to videos embedded on your own site. If
you post videos on third-party platforms where you don't control the schema.org markup, you can
reach out to those platforms to see if this markup is supported.

We hope you'll find `SeekToAction` markup an easier, more efficient way to enable key
moments and help people engage more deeply with your videos. If you have any questions, post them in the [forum](https://support.google.com/webmasters/community),
connect with [@googlesearchc on Twitter](https://twitter.com/googlesearchc), or file
feedback directly on our documentation pages.
