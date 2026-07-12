---
title: "Video Sitemaps: Understanding location tags"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2010-08-video-sitemaps-understanding-location"
url: "https://developers.google.com/search/blog/2010/08/video-sitemaps-understanding-location"
canonical: "https://developers.google.com/search/blog/2010/08/video-sitemaps-understanding-location"
author: "Nelson Lee, Product Manager, Video Search"
published: "2010-08-16T00:00:00+00:00"
updated: "2010-08-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:08:13+00:00"
status_code: 200
html_hash: "5003f994e10eb6b4eacd3ed786dbde2dafbc3122db810e45af9103408540a1d7"
clean_word_count: 344
clean_char_count: 2220
---
# Video Sitemaps: Understanding location tags

If you want to add video information to a Sitemap or mRSS feed you must specify the location of
the video. This means you must include one of two tags, either the
`video:player_loc` or `video:content_loc`. In the case of an mRSS feed,
these equivalent tags are `media:player` or `media:content`, respectively.
We need this information to verify that there is actually a live video on your landing page and
to extract metadata and signals from the video bytes for ranking. If one of these tags is not
included we will not be able to verify the video and your Sitemap/mRSS feed will not be crawled.
To reduce confusion, here is some more detail about these elements.

## Video Locations Defined

- **Player Location/URL:** the player (for example, .swf) URL with corresponding arguments that
  load and play the actual video.
- **Content Location/URL:** the actual raw video bytes (for example, .flv, .avi) containing the
  video content.

## The Requirements

One of either the player `video:player_loc` or content `video:content_loc`
location is required. However, we strongly suggest you provide both, as they each serve distinct
purposes: player location is primarily used to help verify that a video exists on the page, and
content location helps us extract more signals and metadata to accurately rank your videos.

## URL extensions at a glance

|  |  |  |
| --- | --- | --- |
| **Sitemap:** | **mRSS:** | **Contents:** |
| `<loc>` | `<link />` | The playpage URL |
| `<video:player_loc>` | `<media:player>`(url attribute) | The SWF URL |
| `<video:content_loc>` | `<media:content>` (url attribute) | The FLV or other raw video URL |

Note, that all URLs should be unique (every URL in your entire Video Sitemap and mRSS feed should
be unique).

If you would like to better ensure that only Googlebot accesses your content, you can perform a
[reverse DNS lookup](/search/docs/crawling-indexing/verifying-googlebot).

For more information on Google Videos please visit our
[Help Center](/search/docs/appearance/video),
and to post questions and search for answers check out our
[Help Forum](https://support.google.com/webmasters/community/thread?tid=5216d9b9a700866a).
