---
title: "Introducing Video Sitemaps"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2007-12-introducing-video-sitemaps"
url: "https://developers.google.com/search/blog/2007/12/introducing-video-sitemaps"
canonical: "https://developers.google.com/search/blog/2007/12/introducing-video-sitemaps"
author: "John Fisher-Ogden, Software Engineer, and Amy Wu, Associate Product Manager"
published: "2007-12-17T00:00:00+00:00"
updated: "2007-12-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:51:04+00:00"
status_code: 200
html_hash: "7231ae226d15aeac685029bb275a0b4f1fcfc77a0b132c672e6d935486404b64"
clean_word_count: 239
clean_char_count: 1663
---
# Introducing Video Sitemaps

In our effort to help users search all the world's public videos, the Google Video team joined the
Sitemaps folks to introduce Video Sitemaps—an extension of the
[Sitemap Protocol](https://sitemaps.org/protocol.html) that
helps make your videos more searchable via
[Google Video Search](https://video.google.com/). By submitting
this video-specific Sitemap in addition to your standard Sitemap, you can specify all the video
files on your site, along with relevant metadata. Here's an example:

```
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9"
           xmlns:video="https://www.google.com/schemas/sitemap-video/1.0">
  <url>
    <loc>https://www.example.com/videos/some_video_landing_page.html</loc>
    <video:video>
      <video:content_loc>https://www.example.com/video123.flv</video:content_loc>
      <video:player_loc allow_embed="yes">
        https://www.example.com/videoplayer.swf?video=123
      </video:player_loc>
      <video:title>My funny video</video:title>
      <video:thumbnail_loc>https://www.example.com/thumbs/123.jpg</video:thumbnail_loc>
    </video:video>
  </url>
  <url>
    <loc>https://www.example.com/videos/some_other_video_landing_page.html</loc>
    <video:video>
      <video:content_loc>https://www.example.com/videos/video1.mpg</video:content_loc>
      <video:description>A really awesome video</video:description>
    </video:video>
  </url>
</urlset>
```

To get started,
[create a Video Sitemap](/search/docs/crawling-indexing/sitemaps/video-sitemaps),
sign into
[Google Webmaster Tools](https://search.google.com/search-console),
and add the Video Sitemap to your account.
