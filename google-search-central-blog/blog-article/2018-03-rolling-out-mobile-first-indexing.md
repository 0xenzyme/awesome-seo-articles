---
title: "Rolling out mobile-first indexing"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2018-03-rolling-out-mobile-first-indexing"
url: "https://developers.google.com/search/blog/2018/03/rolling-out-mobile-first-indexing"
canonical: "https://developers.google.com/search/blog/2018/03/rolling-out-mobile-first-indexing"
author: "Fan Zhang"
published: "2018-03-26T00:00:00+00:00"
updated: "2018-03-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2018_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:32:00+00:00"
status_code: 200
html_hash: "a922a383783606475620c912f9a776baa00d3e5b09cf7173b13400707ba0ccdf"
clean_word_count: 574
clean_char_count: 3881
---
# Rolling out mobile-first indexing

Today we're announcing that [after a year and
a half](/search/blog/2016/11/mobile-first-indexing) of careful experimentation and testing, we've started migrating sites that follow the
[best practices](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) for mobile-first indexing.

To recap, our crawling, indexing, and ranking systems have typically used the desktop version of
a page's content, which may cause issues for mobile searchers when that version is vastly
different from the mobile version. Mobile-first indexing means that we'll use the mobile version
of the page for indexing and ranking, to better help our – primarily mobile – users find what
they're looking for.

We continue to have one single index that we use for serving search results. We do not have a
"mobile-first index" that's separate from our main index. Historically, the desktop version was
indexed, but increasingly, we will be using the mobile versions of content.

We are notifying sites that are
[migrating to mobile-first indexing](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) via
[Search Console](https://search.google.com/search-console). Site owners will see
significantly increased crawl rate from the
[Smartphone Googlebot](/search/docs/crawling-indexing/overview-google-crawlers).
Additionally, Google will show the mobile version of pages in Search results and
[Google cached pages](https://support.google.com/websearch/answer/1687222).

![the message sent to site owners when mobile-first indexing is enabled for their sites](/static/search/blog/images/import/4a410be1a89754ebd72b67c916d1ea66.png)

To understand more about how we determine the mobile content from a site, see
[our documentation](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing). It covers how sites
using responsive web design or dynamic serving are generally set for mobile-first indexing. For
sites that have AMP and non-AMP pages, Google will prefer to index the mobile version of the
non-AMP page.

Sites that are not in this initial wave don't need to panic. Mobile-first indexing is about how
we gather content, not about how content is ranked. Content gathered by mobile-first indexing has
no ranking advantage over mobile content that's not yet gathered this way or desktop content.
Moreover, if you only have desktop content, you will continue to be represented in our index.

Having said that, we continue to encourage webmasters to make their content mobile-friendly. We
do evaluate all content in our index—whether it is desktop or mobile—to determine how
mobile-friendly it is. [Since 2015](/search/blog/2015/04/rolling-out-mobile-friendly-update),
this measure can help mobile-friendly content perform better for those who are searching on mobile.
Related, we [recently announced](/search/blog/2018/01/using-page-speed-in-mobile-search)
that beginning in July 2018, content that is slow-loading may perform less well for both desktop
and mobile searchers.

To recap:

- Mobile-indexing is rolling out more broadly. Being indexed this way has no ranking advantage and
  operates independently from our mobile-friendly assessment.
- Having mobile-friendly content is still helpful for those looking at ways to perform better in
  mobile search results.
- Having fast-loading content is still helpful for those looking at ways to perform better for
  mobile and desktop users.
- As always, ranking uses many factors. We may show content to users that's not mobile-friendly or
  that is slow loading if our many other signals determine it is the most relevant content to show.

We'll continue to monitor and evaluate this change carefully. If you have any questions, please drop by our
[Webmaster forums](https://support.google.com/webmasters/go/community) or our
[public events](/search/events).
