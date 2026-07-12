---
title: "Best Practices for News coverage with Search"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2020-02-best-practices-for-news-coverage-with"
url: "https://developers.google.com/search/blog/2020/02/best-practices-for-news-coverage-with"
canonical: "https://developers.google.com/search/blog/2020/02/best-practices-for-news-coverage-with"
author: "Patrick Kettner"
published: "2020-02-28T00:00:00+00:00"
updated: "2020-02-28T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:36:02+00:00"
status_code: 200
html_hash: "634e3deb5caf4788099039bb0d806ee9bd95bb02e94b25b613e2fbef6cad46b6"
clean_word_count: 656
clean_char_count: 4166
---
# Best Practices for News coverage with Search

Having up-to-date information during large, public events is critical, as the landscape changes by
the minute. This guide highlights some tools that news publishers can use to create a data rich
and engaging experience for their users.

## Add Article structured data to AMP pages

Adding Article structured data to your news, blog, and sports article AMP pages can make the
content eligible for an enhanced appearance in Google Search results. Enhanced features may
include placement in the Top stories carousel, host carousel, and Visual stories. Learn how to
[mark up your article](/search/docs/appearance/structured-data/article).

You can now test and validate your
[AMP article markup](/search/docs/appearance/structured-data/article#amp-sd)
in the
[Rich Results Test](https://search.google.com/test/rich-results?e=SuitSdEmbeddedContent)
tool. Enter your page's URL or a code snippet, and the Rich Result Test shows the AMP Articles
that were found on the page (as well as other rich result types), and any errors or suggestions
for your AMP Articles. You can also save the test history and share the test results.

We also recommend that you
[provide a publication date](/search/docs/appearance/publication-dates)
so that Google can expose this information in Search results, if this information is considered to
be useful to the user.

## Mark up your live-streaming video content

If you are live-streaming a video during an event, you can be eligible for a LIVE badge by
[marking your video with BroadcastEvent](/search/docs/appearance/structured-data/video#livestream-guidelines).
We strongly recommend that you use the Indexing API to ensure that your live-streaming video
content gets crawled and indexed in a timely way. The Indexing API allows any site owner to
directly notify Google when certain types of pages are added or removed. This allows Google to
schedule pages for a fresh crawl, which can lead to more relevant user traffic as your content
is updated. For websites with many short-lived pages like livestream videos, the Indexing API
keeps content fresh in search results. Learn how to
[get started with the Indexing API](/search/apis/indexing-api/v3/quickstart).

## For AMP pages: Update the cache and use components

Use the following to ensure your AMP content is published and up-to-date the moment news breaks.

### Update the cache

When people click an AMP page, the Google AMP Cache automatically requests updates to serve
fresh content for the next person once the content has been cached. However, if you want to
force an update to the cache in response to a change in the content on the origin domain, you
can send an [update request to the Google AMP Cache](/amp/cache/update-cache).
This is useful if your pages are changing in response to a live news event.

### Use news-related AMP components

- [`<amp-live-list> </amp-live-list>`](https://amp.dev/documentation/components/amp-live-list/):
  Add live content to your article and have it updated based on a source document. This is a
  great choice if you just want content to reload easily, without having to set up or configure
  additional services on your backend.
  [Learn how to implement
  `<amp-live-list></amp-live-list>`](https://amp.dev/documentation/examples/news-publishing/live_blog/?format=websites).
- [`<amp-script></amp-script>`](https://amp.dev/documentation/components/amp-script/):
  Run your own JavaScript inside of AMP pages. This flexibility means that anything you are
  publishing on your desktop or non-AMP mobile pages, you can bring over to AMP.
  `<amp-script></amp-script>`
  supports Websockets, interactive SVGs, and more. This allows you to create engaging news pages
  like election coverage maps, live graphs and polls etc. As a newer feature, the AMP team is
  actively soliciting feedback on it. If for some reason it doesn't work for your use case,
  [let us know](https://github.com/ampproject/amphtml/issues/new/choose).

If you have any questions, let us know through [the forum](https://support.google.com/webmasters/community)
or [on Twitter](https://twitter.com/googlesearchc).
