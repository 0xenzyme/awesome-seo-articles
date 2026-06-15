---
title: "Flash support in Instant Previews"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-05-flash-support-in-instant-previews"
url: "https://developers.google.com/search/blog/2011/05/flash-support-in-instant-previews"
canonical: "https://developers.google.com/search/blog/2011/05/flash-support-in-instant-previews"
author: "Raj Krishnan"
published: "2011-05-06T00:00:00+00:00"
updated: "2011-05-06T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:12:55+00:00"
status_code: 200
html_hash: "dcdbb05fb6b66a69df141c935171b0d483f3f4ff119a84ab94e92742cba58bf5"
clean_word_count: 393
clean_char_count: 2514
---
# Flash support in Instant Previews

With
[Instant Previews](/search/blog/2010/11/instant-previews), users can see a snapshot of
a search result before clicking on it. We've made a number of
[improvements](https://googleblog.blogspot.com/2011/04/this-week-in-search-41511)
to the feature since its introduction last November, and if you own a site, one of the most
relevant changes for you is that Instant Previews now supports Flash.

![An Instant Preview with rich content rendered](/static/search/blog/images/import/3e278bcb151afc8f28db8d475cfe9a8e.png)

In most cases, when the preview for a page is generated through our regular crawl, we will now
render a snapshot of any Flash components on the page. This will replace the "puzzle piece" icon
that previously appeared to indicate Flash components, and should improve the accuracy of the
previews.

However, for pages that are fetched on demand by the "Google Web Preview" user-agent, we will
generate a preview without Flash in order to minimize latency. In these cases the preview will
appear as if the page were visited by someone using a browser without Flash enabled, and
"Install Flash" messages may appear in the preview, depending on how your website handles users
without Flash.

To improve your previews for these on-demand renders, here are some guidelines for using Flash on
your site:

- **Make sure that your site has a reasonable, seamless experience for visitors without Flash.**
  This may involve creating HTML-only equivalents for your Flash-based content that will
  automatically be shown to visitors who can't view Flash. Providing a good experience for this
  case will improve your preview and make your visitors happier.
- If Flash components are rendering but appear as loading screens instead of actual content,
  **try reducing the loading time for the component**. This makes it more likely we'll render
  it properly.
- If you have Flash videos on your site, **consider
  [submitting a Video Sitemap](/search/docs/crawling-indexing/sitemaps/video-sitemaps)**
  which helps us to generate thumbnails for your videos in Instant Previews.
- If most of the page is rendering properly but you still see puzzle pieces appearing for some
  smaller components, these may be fixed in future crawls of your page.

If you have additional questions, you can post them in our
[Webmaster Help Forum](https://support.google.com/webmasters/community).

As always, we'll keep you updated as we continue to make improvements to Instant Previews.
