---
title: "Video mode now only shows pages where video is the main content"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2023-12-video-is-the-main-content"
url: "https://developers.google.com/search/blog/2023/12/video-is-the-main-content"
canonical: "https://developers.google.com/search/blog/2023/12/video-is-the-main-content"
author: "Cory Benavente"
published: "2023-12-04T00:00:00+00:00"
updated: "2023-12-04T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
fetched_at: "2026-06-14T13:43:25+00:00"
status_code: 200
html_hash: "07c3bd0a6f51f833c63e1740028631421da6d5a66e7eaea82630894dc0544726"
clean_word_count: 528
clean_char_count: 3124
---
# Video mode now only shows pages where video is the main content

[Earlier this year](/search/blog/2023/04/simplifying-video), we made a change to only
show video thumbnails next to results on the main Google Search results page when the video is
the main content of a page. Today, we're extending this change to search results in Video mode to
better connect users with the video content they're looking for (rather than having to comb
through a page to find that video). This change will start rolling out today, and it could take
up to a week to complete.

![Video mode in Google Search results](/static/search/blog/images/video-mode-on-google.png "Video mode in Google Search results")

With this update, clicking a result in Video mode will only take users to a page where the video
is the main content. Here's an example of a page where the video is the main content of the page:
the video is above the fold, it's prominent, and the main purpose of the page is to watch that
video.

![a web page where the video is the main content on the page](/static/search/docs/images/dedicated-video-page.png "A web page where the video is the main content on the page")

Here are some examples of page types where the video is supplementary to the textual content, and
not the primary focus of the page:

- A blog post where the video is complementary to the text rather than the primary content of
  the page
- A product details page with a complementary video
- A video category page that lists multiple videos of equal prominence

As the update rolls out, you'll see the impact of this change in your Search Console
[video indexing report](https://support.google.com/webmasters/answer/9495631).
Videos that aren't the main content of the page will appear as "No video indexed" in Search
Console. We're also adding a new reason to the report to explain why these videos are not indexed:
"Video is not the main content of the page", which simplifies the report by replacing the
following issues:

- Invalid video URL
- Unsupported video format
- Unknown video format
- Inline data URLs cannot be used for video URLs
- Video outside the viewport
- Video too small
- Video too tall

![Video indexing report in Search Console, with a callout for the new issue: Video is not the main content of the page](/static/search/blog/images/video-is-main-content-search-console.png)

Since these videos will no longer be shown in Video mode, you can expect to see a decrease in
the number of pages with indexed videos. This decrease will also appear in the number of video
impressions in the [performance report](https://support.google.com/webmasters/answer/7576553),
[video indexing report](https://support.google.com/webmasters/answer/9495631), and
the [video rich results report](https://support.google.com/webmasters/answer/7552505)
in Search Console.

To learn more about video indexing best practices, check out the [video best practices guide](/search/docs/appearance/video).
For questions, feel free to post in our [Search Central help community](https://goo.gle/sc-forum),
where you can join a discussion with like-minded experts.
