---
title: "More time, tools, and details on the page experience update"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2021-04-more-details-page-experience"
url: "https://developers.google.com/search/blog/2021/04/more-details-page-experience"
canonical: "https://developers.google.com/search/blog/2021/04/more-details-page-experience"
author: "Jeffrey\n    Jose"
published: "2021-04-19T00:00:00+00:00"
updated: "2021-04-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:38:47+00:00"
status_code: 200
html_hash: "00406ac03c82ed0b914f7249783346d9ada5fc29cd1d93dea010961712cf733b"
clean_word_count: 1280
clean_char_count: 8139
---
# More time, tools, and details on the page experience update

Last November we [announced](/search/blog/2020/11/timing-for-page-experience) that the
page experience ranking change will go live on Google Search this year, in what we're calling the
"page experience update". To help publishers and site owners improve their page experience and
prepare, today we're announcing a few key updates:

1. [Gradual rollout starting in mid-June this year](#gradual-rollout)
2. [Details on what will be included in the update](#details)
3. [A new Page Experience report in Search Console](#new-report)
4. [Support for signed exchanges for all content on Google Search](#sxg)

## Gradual rollout starting in mid-June this year

We'll begin using page experience as part of our ranking systems beginning in mid-June 2021.
However, page experience won't play its full role as part of those systems until the end of
August. You can think of it as if you're adding a flavoring to a food you're preparing. Rather
than add the flavor all at once into the mix, we'll be slowly adding it all over this time period.

As we have said before, while this update is designed to highlight pages that offer great user
experiences, page experience remains one of many factors our systems take into account. Given
this, sites generally should not expect drastic changes. In addition, because we're doing this as
a gradual rollout, we will be able to monitor for any unexpected or unintended issues.

We hope that this adjusted roll-out schedule will help you continue to make refinements to your
website with page experience in mind. Ahead of this change, we've been gathering feedback to
ensure that we're providing helpful guidance and [answering
questions](https://support.google.com/webmasters/thread/104436075) that site owners may have about how to improve page experience for their users.

## Details on what will be included in the update

As previously [announced](/search/blog/2020/05/evaluating-page-experience#page-experience-and-the-mobile-top-stories-feature),
the page experience update will consider several [page
experience signals](/search/docs/appearance/page-experience#signals), including the three [Core
Web Vitals metrics](https://web.dev/articles/vitals): [LCP](https://web.dev/articles/lcp),
[FID](https://web.dev/articles/fid), and [CLS](https://web.dev/articles/cls)
(as well as [Chrome's recent fix to
CLS](https://web.dev/articles/evolving-cls)). In addition, the Top Stories carousel feature on Google Search will be updated to
include all news content, as long as it meets the [Google
News policies](https://support.google.com/news/publisher-center/answer/6204050). This means that using the AMP format is no longer required and that
any page, irrespective of its Core Web Vitals score or page experience status, will be eligible to
appear in the Top Stories carousel.

We're also bringing similar updates to the Google News app, a key destination for users around
the world to get a comprehensive view of the important news of the day. As part of the page
experience update, we're expanding the usage of non-AMP content to power the core experience
on [news.google.com](https://news.google.com/) and in the Google News app.

Additionally, we will no longer show the AMP badge icon to indicate AMP content. You can expect
this change to come to our products as the page experience update begins to roll out in mid-June.
We'll continue to test other ways to help identify content with a great page experience, and we'll
keep you updated when there is more to share.

If you're looking for more details, take a look at the
[Core Web Vitals
and Page Experience FAQs](https://support.google.com/webmasters/thread/104436075)
that we published on the Search Central forums recently. If you're an AMP publisher, the AMP team
has built an [AMP
page experience guide](https://blog.amp.dev/2020/10/13/meet-amps-page-experience-guide/) that offers tailored advice on how to make your AMP pages perform at
their best.

## A new Page Experience report in Search Console

To provide you with more actionable insights, we're introducing the
[Page Experience
report](https://support.google.com/webmasters/answer/10218333). This report combines the existing Core Web Vitals report with other components of
the page experience signals, such as HTTPS security, absence of intrusive interstitials, and mobile friendliness.

The Page Experience report offers valuable metrics, such as the percentage of URLs with good page
experience and search impressions over time, enabling you to quickly evaluate performance. You can
also dig into the components of page experience signal to gain additional insights on opportunities
for improvement.

![Page experience report in Search Console](/static/search/blog/images/page-experience-report.png)

In addition to launching the Page Experience report, we've also updated the
[Search Performance
report](https://support.google.com/webmasters/answer/7576553) to allow you to filter pages with good page experience, which helps you keep track of how
these pages compare to other pages on the same site.

## Support for signed exchanges for all content on Google Search

Today we're also announcing the general availability of [signed
exchanges (SXG) on Google Search](/search/docs/appearance/signed-exchange) for all web pages. Google Search previously only
[supported](https://blog.amp.dev/2019/05/22/privacy-preserving-instant-loading-for-all-web-content/)
SXG built with the AMP framework.

SXG allows Google Search to leverage the privacy-preserving prefetching technique in
[compatible
browsers](https://web.dev/articles/signed-exchanges#browser-compatibility), which can lead to improved page experience. This technique enables Google Search
to load key resources of a page (HTML, JavaScript, CSS) ahead of navigation, which makes it
possible for the browser to display pages faster.

Nikkei, a large publication based in Japan, has been testing SXG on [Nikkei
Style](https://style.nikkei.com) and saw a 300ms reduction in Largest Contentful Paint (LCP). They also saw
12% more user engagement and an improvement of 9% in pageviews per session on Android Chrome where
this test was implemented. To implement SXG on their site, Nikkei chose
[`nginx-sxg-module`](https://github.com/google/nginx-sxg-module), an
open source extension for NGINX servers.

For more information on SXG tooling, see [Signed
Exchanges (SXGs)](https://web.dev/articles/signed-exchanges#tooling). For instructions on setting up SXG, see
[How to set up signed
exchanges using Web Packager](https://web.dev/articles/signed-exchanges-webpackager).

## Building a better web, together

Our vision for page experience is to build a web ecosystem that users love—together. We're hard
at work to make sure that you have the right tools and resources available before the ranking
rollout starting in mid-June 2021.

We hope the updates that we shared today will make it easier for you to build great websites.
If you have questions or feedback, please visit our [help
forums](https://support.google.com/webmasters/community/), check out the [FAQs](https://support.google.com/webmasters/thread/104436075)
that we published recently, or let us know through [Twitter](https://twitter.com/googlesearchc).

---

## Updates

- **Update on August 4, 2021**:
  [Clarified that Safe Browsing isn't used as a ranking signal](/search/blog/2021/08/simplifying-the-page-experience-report).
  Safe Browsing systems continue to play an important role to keep users of Google Search safe,
  and any flags will continue to be surfaced in Search Console outside of Page Experience
  report.
- **Update on June 15, 2021**: The page experience update is rolling out to all users globally.
  It will be complete by the end of August 2021.
- **Update on January 31, 2024**:
  [Interaction to Next Paint (INP) will replace FID](https://web.dev/blog/inp-cwv-march-12)
  as a part of Core Web Vitals on March 12, 2024.
- **Update on March 12, 2024**:
  [Interaction to Next Paint (INP) has replaced FID](https://web.dev/blog/inp-cwv-launch)
  as a part of Core Web Vitals.
