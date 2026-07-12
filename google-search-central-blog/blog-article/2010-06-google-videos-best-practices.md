---
title: "Google Videos best practices"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-06-google-videos-best-practices"
url: "https://developers.google.com/search/blog/2010/06/google-videos-best-practices"
canonical: "https://developers.google.com/search/blog/2010/06/google-videos-best-practices"
author: "Nelson Lee, Product Manager, Video Search"
published: "2010-06-12T00:00:00+00:00"
updated: "2010-06-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:07:07+00:00"
status_code: 200
html_hash: "869c8864c6a53f93cea6681a740a679ea42a324c155e8172661398e2f75baf4d"
clean_word_count: 426
clean_char_count: 2740
---
# Google Videos best practices

We'd like to highlight three [best practices](/search/docs/appearance/video)
that address some of the most common problems found when crawling and indexing video content.
These best practices include ensuring your video URLs are crawlable, stating what countries your
videos may be played in, and that if your videos are removed, you clearly indicate this state to
search engines.

## Best Practice 1: Verify your video URLs are crawlable: check your robots.txt

Sometimes publishers unknowingly include video URLs in their Sitemap that are
[robots.txt](/search/docs/crawling-indexing/robots/intro) disallowed. Please make sure your
robots.txt file isn't blocking any of the URLs specified in your Sitemap. This includes URLs for
the:

- Playpage
- Content and player
- Thumbnail

## Best Practice 2: Tell us what countries the video may be played in

Is your video only available in some locales? The optional attribute "restriction" has recently
been added (see our documentation about
[video best practices](/search/docs/appearance/video)), which you can use to
tell us whether the video can only be played in certain territories. Using this tag, you have the
option of either including a list of all countries where it can be played, or just telling us the
countries where it can't be played. If your videos can be played everywhere, then you don't need
to include this.

## Best Practice 3: Indicate clearly when videos are removed—protect the user experience

Sometimes publishers take videos down but don't signal to search engines that they've done so.
This can result in the search engine's index not accurately reflecting content of the web. Then
when users click on a search result, they're taken to a page either indicating that the video
doesn't exist, or to a different video. Users find this experience dissatisfying. Although we have
mechanisms to detect when search results are no longer available, we strongly encourage following
community standards.

To signal that a video has been removed:

1. **Return a `404 (Not found)` HTTP response code**, you can still return a helpful page to be
   displayed to your users. Check out these
   [guidelines for creating useful `404` pages](/search/docs/crawling-indexing/troubleshoot-crawling-errors#soft-404-errors).
2. **Indicate expiration dates** for each video listed in a Video Sitemap (use the
   `<video:expiration_date>` element) or mRSS feed (`<dcterms:valid>`
   tag) submitted to Google.

For more information on Google Videos please visit our
[Help Center](/search/docs/appearance/video), and to post questions and search
answers check out our
[Help Forum](https://support.google.com/webmasters/community/thread?tid=5216d9b9a700866a).
