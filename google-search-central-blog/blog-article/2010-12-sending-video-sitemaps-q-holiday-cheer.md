---
title: "Sending Video Sitemaps Q'n'A holiday cheer"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-12-sending-video-sitemaps-q-holiday-cheer"
url: "https://developers.google.com/search/blog/2010/12/sending-video-sitemaps-q-holiday-cheer"
canonical: "https://developers.google.com/search/blog/2010/12/sending-video-sitemaps-q-holiday-cheer"
author: "Maile Ohye"
published: "2010-12-25T00:00:00+00:00"
updated: "2010-12-25T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:10:34+00:00"
status_code: 200
html_hash: "6c1d08a76e85488e699bb8c6c2dc6ca529c3da0167b2625b0f64d34c3fa889d9"
clean_word_count: 948
clean_char_count: 5866
---
# Sending Video Sitemaps Q'n'A holiday cheer

To the fabulous, savvy audience that attended our
[Video Sitemap webinar](https://www.youtube.com/watch?v=kks0wPkX12I)
several months ago, please accept our re-gift: a summary of your questions from the
[Video Sitemaps](/search/docs/crawling-indexing/sitemaps/video-sitemaps) Q&A!

To those who were unable to attend the webinar, please enjoy our gift of the summarized Q&A
—it's like new!

Either way, happy holidays from all of us on the Webmaster Central Team. :)

*Our entire webinar covers the basics of Video Sitemaps and best practices—nearly
everything you'd need to know when submitting a video feed.*

1. *Can the source/content of the video (perhaps a third-party vendor) be hosted on another
   site? For example, can I host my videos on YouTube and still be eligible for Video Search
   traffic?*

   Yes, you can use a third party to host videos. Only the play page--the URL within the
   `<loc>` tag--needs to be on your site.
   `<video:content_loc>` and `<video:player_loc>` can list
   URLs on a different site or subdomain.

   For example, here's a snippet from a valid
   Video Sitemap that shows content hosted on a different subdomain from the play page:

   ```
   <url>
     <loc>https://www.example.com/videos/some_video_landing_page.html</loc>
     <video:video>
       <video:thumbnail_loc>https://www.example.com/thumbs/123.jpg</video:thumbnail_loc>
       <video:title>Grilling steaks for summer</video:title>
       <video:description>Alkis shows you how to get perfectly done steaks every time</video:description>
       <video:content_loc>https://video-hoster.example.com/video123.flv</video:content_loc>
       <video:player_loc allow_embed="yes" autoplay="ap=1">https://www.example.com/videoplayer.swf?video=123</video:player_loc>
     </video:video>
   </url>
   ```
2. *If I'm using YouTube to host my videos, can Google verify that I'm the legitimate owner?*

   Currently, there doesn't exist functionality that allows you, as the uploader, to verify that
   you're the owner of a video. The issue of authorship is a hard problem on the web, not just
   for videos, but nearly all types of content.
3. *Because Google owns YouTube, should users who embed YouTube videos still submit Video
   Sitemaps or is it unnecessary?*

   Google treats YouTube as just another source for video content—though you don't need to
   submit a Video Sitemap if you only want your YouTube-hosted videos indexed. If, however,
   you're using YouTube as a online video platform (that is, with play pages on your own site),
   then we do recommend Sitemap submission.
4. *How long does it take for Google to accept and verify a Video Sitemap?*

   Video Sitemap submission is a two-part process:

   1. We fetch the Sitemap and parse it for syntax errors. This happens within minutes.
   2. We fetch the assets referenced in the Sitemap, perform checks, validate metadata, do
      more cool stuff, and last, index the video. This step can require varied amounts of time
      depending on your site and our system load.
5. *What tags and
   [categories](/search/docs/appearance/video)
   are most important in Video Sitemaps or mRSS? Should I create my own categories or is there
   a list that I should conform to?*

   Currently, the most important metadata to include is title and description—both are
   required. The category tag is optional, and there isn't a list from which to select.
6. *Do I have to use [HTML5](https://www.html5rocks.com/) to
   use Video Sitemaps?

   Does HTML5 help with discovery?

   Or, if my site is HTML5 compliant, do I still need to submit a Video Sitemap?*

   None of the Video Search principles change with HTML5. We still recommend using a Video
   Sitemap regardless of the markup on your site. HTML5 can be helpful, though, because tags
   like `<video>` make it easier for our systems to verify that video exists on
   the page.
7. *If I use an [iframe](/search/docs/appearance/video) rather than
   embedding my videos, can Google still find it?*

   We do not recommend using iframes to embed video content on your pages.
8. *Can I have multiple videos on one URL?*

   You can. We've found, however, that users may not consider it the best experience. When users
   click on a video search result, they most often don't like being forced to locate the correct
   video among multiple videos on the resulting page.
9. *Do I need to specifically create a
   [robots.txt](/search/docs/crawling-indexing/robots/intro)
   file that allows Googlebot, or do I just need to make sure Googlebot isn't blocked?*

   Just make sure that Googlebot isn't blocked.
10. *I provided a thumbnail, but it's not being used. Does Google create their own thumbnails
    from my videos?*

    We try to use the [thumbnail you provide](/search/docs/appearance/video)
    if it's valid. If not, we'll try to generate a thumbnail ourselves. We recommend that you
    provide thumbnails that are at least 120x90 pixels. We also accept many thumbnail formats,
    such as PNG and JPEG.
11. *Any video filesize limitations?*

    At this time, there aren't video filesize limitations on content submitted through Video
    Sitemaps.
12. *Is there any way to indicate a transcript or closed captioning for a video?*

    Currently there isn't, but perhaps down the road.
13. *What if I'm using Lightbox or a popup to display a video; can it still be indexed?*

    Depends on the use case and how it's rendered, but if indexing by search engines is important
    to you, it's not the safest method. In the
    [documentation](/search/docs/appearance/video), we explain that "When
    designing your site, it's important to configure your video pages without any overly complex
    JavaScript or Flash setup." Most often, for bots, simpler is safer.

Have a safe and happy holiday!
