---
title: "Video Sitemaps and mRSS vs. Facebook Share and RDFa"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-12-video-sitemaps-mrss-vs-facebook-share"
url: "https://developers.google.com/search/blog/2010/12/video-sitemaps-mrss-vs-facebook-share"
canonical: "https://developers.google.com/search/blog/2010/12/video-sitemaps-mrss-vs-facebook-share"
author: "Maile Ohye"
published: "2010-12-23T00:00:00+00:00"
updated: "2010-12-23T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:10:42+00:00"
status_code: 200
html_hash: "4e1320c94d9ac806258adcceea66298c64e7f69186a2618b9427dcb274fee60f"
clean_word_count: 390
clean_char_count: 2806
---
# Video Sitemaps and mRSS vs. Facebook Share and RDFa

What are the benefits of submitting feeds like
[Video Sitemaps](/search/docs/crawling-indexing/sitemaps/video-sitemaps) and
[mRSS](/search/docs/crawling-indexing/sitemaps/video-sitemaps#sitemap_alternatives)
vs. the benefits of
[Facebook Share and RDFa](/search/blog/2009/09/supporting-facebook-share-and-rdfa-for)?
Is one better than the other? Let's start the discussion.

## Functionality of feeds vs. on-page markup

Google accepts information from both video feeds, such as Video Sitemaps and mRSS, as well as
on-page markup, such as Facebook Share and RDFa. We recommend that you use both!

If you have limited resources, however, here's a chart explaining the pros and cons of each
method. The key differentiators include:

- While both feeds and on-page markup give search engines metadata, Video Sitemaps/mRSS also help
  with crawl discovery. We may find a new URL through your feed that we wouldn't have easily
  discovered otherwise.
- Using Video Sitemaps/mRSS requires that the search engine support these formats and not all
  engines do. Because on-page markup is just that—on the page—crawlers can gather the
  metadata through organic means as they index the URL. No feed support is required.

|  |  |  |
| --- | --- | --- |
|  | **Feeds (Video Sitemaps and mRSS)** | **On-page markup (Facebook Share and RDFa)** |
| Accepted by Google | **&check;** | **&check;** |
| Helps search engines discover new URLs with videos (improves discovery and coverage) | **&check;** |  |
| Provides structured metadata (for example, video title and description) | **&check;** | **&check;** |
| Allows search engines without sitemap/mRSS support to still obtain metadata information (allows organic gathering of metadata) |  | **&check;** |
| Incorporates additional metadata like "duration" | **&check;** |  |

If you're further wondering about the benefits of specific feeds (Video Sitemaps vs. mRSS), we can
help with clarification there, too. First of all, you can use either. We're indifferent about it.
:) One benefit of Video Sitemaps is that, because it's a format we're
actively enhancing, we can quickly extend it to allow for more specifications.

*All this said, if you're going to start from scratch, Video Sitemaps is our recommended start.*

|  |  |  |
| --- | --- | --- |
|  | **Video Sitemaps** | **mRSS** |
| Accepted by Google | **&check;** | **&check;** |
| Been around for a long, long time and pretty widely accepted |  | **&check;** |
| Extremely quick for Google Video Search team to extend | **&check;** |  |

"Starving" to start conversation about feeds or on-page markup? Join us in the
[Sitemaps section](https://support.google.com/webmasters/community/label?lid=401d0e67c19e20e9&hl=en)
of the Webmaster discussion forum.
