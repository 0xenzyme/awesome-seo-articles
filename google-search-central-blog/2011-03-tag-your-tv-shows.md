---
title: "Tag Your TV Shows!"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2011-03-tag-your-tv-shows"
url: "https://developers.google.com/search/blog/2011/03/tag-your-tv-shows"
canonical: "https://developers.google.com/search/blog/2011/03/tag-your-tv-shows"
author: "Written by Jeff Posnick, Video Search Team"
published: "2011-03-24T00:00:00+00:00"
updated: "2011-03-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:12:02+00:00"
status_code: 200
html_hash: "4504330cbb99633cd2f576163e1b1d134f6499fe42cf0974e034faff560f9df9"
clean_word_count: 277
clean_char_count: 1854
---
# Tag Your TV Shows!

If your website is the authoritative source for the video of a particular TV show, make sure we
know about it! Hopefully, you already submit
[Video Sitemaps](/search/docs/crawling-indexing/sitemaps/video-sitemaps)
or
[mRSS feeds](/search/docs/crawling-indexing/sitemaps/video-sitemaps#sitemap_alternatives)
to inform us about video content on your website. We now support
[additional fields](/search/docs/crawling-indexing/sitemaps/video-sitemaps)
in both video Sitemaps and mRSS feeds where you can specify metadata specific to television or
episodic content. This includes the series' title, the season and episode numbers for the video in
question, the premiere date, as well as other additional information. The metadata from your video
feed helps us provide more detailed, relevant results to users wanting to view your show.

Here's an example Video Sitemap entry that includes all the required and some optional TV metadata in the
`>video:tvshow>` element:

```
<video:video>
<video:title>The Sample Show, Season 1, Episode 2</video:title>
<!-- other required root level video tags omitted -->
  <video:tvshow>
    <video:show_title>The Sample Show</video:show_title>;
    <video:video_type>full</video:video_type>
    <video:episode_title>A Sample Episode Title</video:episode_title>
    <video:season_number>1</video:season_number>
    <video:episode_number>2</video:episode_number>
  </video:tvshow>
</video:video>
```

The
[full documentation](/search/docs/crawling-indexing/sitemaps/video-sitemaps)
for the tags for both mRSS and Video Sitemaps can be found in our Webmaster Tools Help Center.
As always, if you have any questions about Video Sitemaps or mRSS feeds, reach out to us in the
[Sitemaps section](https://support.google.com/webmasters/community/label?lid=401d0e67c19e20e9&hl=en)
of the Webmaster Help Forum.
