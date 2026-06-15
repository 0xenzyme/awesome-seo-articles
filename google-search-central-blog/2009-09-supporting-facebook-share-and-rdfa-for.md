---
title: "Supporting Facebook Share and RDFa for videos"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-09-supporting-facebook-share-and-rdfa-for"
url: "https://developers.google.com/search/blog/2009/09/supporting-facebook-share-and-rdfa-for"
canonical: "https://developers.google.com/search/blog/2009/09/supporting-facebook-share-and-rdfa-for"
author: "Michael Cohen, Product Manager, Video Search Team"
published: "2009-09-14T00:00:00+00:00"
updated: "2009-09-14T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:00:50+00:00"
status_code: 200
html_hash: "109ab21edeef3c92c2a7c46ffa4aac7cb381f3260dc31646cc8357ac5d947ea6"
clean_word_count: 471
clean_char_count: 3269
---
# Supporting Facebook Share and RDFa for videos

Have you ever wondered how to increase the chances of your videos appearing in Google's results?
Over the last year, the Video Search team has been working hard to improve our index of video
on the Web. Today, we're beginning the first in a series of posts to explain some best practices
for sites hosting video content.

We
[previously](https://googlevideo.blogspot.com/2009/01/calling-video-publishers.html)
talked about the importance of
[submitting a Video Sitemap or mRSS feed](/search/docs/crawling-indexing/sitemaps/video-sitemaps)
to Google and following Google's
[webmaster guidelines](/search/docs/essentials).
However, we wanted to offer webmasters an additional tool, so today we're taking a page from the
[rich snippets](/search/blog/2009/05/introducing-rich-snippets) playbook and
announcing support for [Facebook Share](https://www.facebook.com/share_partners.php)
and [Yahoo! SearchMonkey RDFa](https://developer.search.yahoo.com/help/objects/video).
Both of these markup formats allow you to specify information essential to video indexing, such
as a video's title and description, within the HTML of a video page. While we've become smarter
at discovering this information on our own, we'd certainly appreciate some hints directly from
webmasters. Also, to maximize the chances that we find the markup on your video pages, you
should make sure it appears in the HTML without the execution of JavaScript or Flash.

So, check out Facebook Share and RDFa and help Google find your videos!

Facebook Share:

```
<meta name="title" content="Baroo? - cute puppies" />
<meta name="description" content="The cutest canine head tilts on the Internet!" />
<link rel="image_src" href="https://example.com/thumbnail_preview.jpg" />
<link rel="video_src" href="https://example.com/video_object.swf?id=12345" />
<meta name="video_height" content="296" />
<meta name="video_width" content="512" />
<meta name="video_type" content="application/x-shockwave-flash" />
```

RDFa (Yahoo! SearchMonkey):

```
<object width="512" height="296" rel="media:video"
           resource="https://example.com/video_object.swf?id=12345"
           xmlns:media="https://search.yahoo.com/searchmonkey/media/"
           xmlns:dc="https://purl.org/dc/terms/">
  <param name="movie" value="https://example.com/video_object.swf?id=12345" />
  <embed src="https://example.com/video_object.swf?id=12345"
            type="application/x-shockwave-flash" width="512" height="296">
  </embed>
  <a rel="media:thumbnail" href="https://example.com/thumbnail_preview.jpg" />
  <a rel="dc:license" href="https://example.com/terms_of_service.html" />
  <span property="dc:description" content="Cute Overload defines Baroo? as: Dogspeak for
    'Whut the...?' Frequently accompanied by the Canine Tilt and/or wrinkled brow for enhanced
    effect." />
  <span property="media:title" content="Baroo? - cute puppies" />
  <span property="media:width" content="512" />
  <span property="media:height" content="296" />
  <span property="media:type" content="application/x-shockwave-flash" />
  <span property="media:region" content="us" />
  <span property="media:region" content="uk" />
  <span property="media:duration" content="63" />
</object>
```
