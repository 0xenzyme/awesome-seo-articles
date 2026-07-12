---
title: "Page layout algorithm improvement"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2012-01-page-layout-algorithm-improvement"
url: "https://developers.google.com/search/blog/2012/01/page-layout-algorithm-improvement"
canonical: "https://developers.google.com/search/blog/2012/01/page-layout-algorithm-improvement"
author: "Matt Cutts"
published: "2012-01-19T00:00:00+00:00"
updated: "2012-01-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:17:26+00:00"
status_code: 200
html_hash: "ec4bdc86867e89518909056664c3db0aa8987b7365c52224554a96262b525d7d"
clean_word_count: 546
clean_char_count: 3248
---
# Page layout algorithm improvement

In our ongoing effort to help you find more high-quality websites in search results, today we're
launching an algorithmic change that looks at the layout of a webpage and the amount of content
you see on the page once you click on a result.

As
[we've mentioned previously](https://searchengineland.com/google-may-penalize-ad-heavy-pages-100601),
we've heard complaints from users that if they click on a result and it's difficult to find the
actual content, they aren't happy with the experience. Rather than scrolling down the page past a
slew of ads, users want to see content right away. So sites that don't have much content
"above-the-fold" can be affected by this change. If you click on a website and the part of the
website you see first either doesn't have a lot of visible content above-the-fold or dedicates a
large fraction of the site's initial screen real estate to ads, that's not a very good user
experience. Such sites may not rank as highly going forward.

We understand that placing ads above-the-fold is quite common for many websites; these ads often
perform well and help publishers monetize online content. This algorithmic change does not affect
sites who place ads above-the-fold to a normal degree, but affects sites that go much further to
load the top of the page with ads to an excessive degree or that make it hard to find the actual
original content on the page. This new algorithmic improvement tends to impact sites where there
is only a small amount of visible content above-the-fold or relevant content is persistently
pushed down by large blocks of ads.

This algorithmic change noticeably affects less than 1% of searches globally. That means that in
less than one in 100 searches, a typical user might notice a reordering of results on the search
page. If you believe that your website has been affected by the page layout algorithm change,
consider how your web pages use the area above-the-fold and whether the content on the page is
obscured or otherwise hard for users to discern quickly. You can use our
[Browser Size](https://browsersize.googlelabs.com/) tool, among
[many others](https://chrome.google.com/webstore/search/screen%20resolution),
to see how your website would look under different screen resolutions.

If you decide to update your page layout, the page layout algorithm will automatically reflect the
changes as we re-crawl and process enough pages from your site to assess the changes. How long
that takes will depend on several factors, including the number of pages on your site and how
efficiently Googlebot can crawl the content. On a typical website, it can take several weeks for
Googlebot to crawl and process enough pages to reflect layout changes on the site.

Overall, our advice for publishers
[continues to be to focus on delivering the best possible user experience](https://www.youtube.com/watch?feature=player_detailpage&v=R7Yv6DzHBvE#t=1186s)
on your websites and not to focus on specific algorithm tweaks. This change is just one of the
over 500 improvements we expect to roll out to search this year. As always, please post your
feedback and questions in our
[Webmaster Help forum](https://support.google.com/webmasters/community).
