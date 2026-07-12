---
title: "Getting your site ready for mobile-first indexing"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2017-12-getting-your-site-ready-for-mobile"
url: "https://developers.google.com/search/blog/2017/12/getting-your-site-ready-for-mobile"
canonical: "https://developers.google.com/search/blog/2017/12/getting-your-site-ready-for-mobile"
author: "Gary Illyes"
published: "2017-12-18T00:00:00+00:00"
updated: "2017-12-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:31:14+00:00"
status_code: 200
html_hash: "530fe96b72bcf4692ecca973c4571bc9f8d7c8ccb72e537dd27af52766d60d3d"
clean_word_count: 618
clean_char_count: 4180
---
# Getting your site ready for mobile-first indexing

When we [announced](/search/blog/2016/11/mobile-first-indexing) almost a year ago that
we're experimenting with mobile-first indexing, we said we'd update publishers about our progress,
something that we've done the past few months through public talks in
[office hours](/search/events/join-office-hours) and at conferences like
[Pubcon](https://www.google.com/search?q=mobile+first+indexing+pubcon).

To recap, currently our crawling, indexing, and ranking systems typically look at the desktop
version of a page's content, which may cause issues for mobile searchers when that version is
vastly different from the mobile version. Mobile-first indexing means that we'll use the mobile
version of the content for indexing and ranking, to better help our—primarily mobile—users
find what they're looking for. Webmasters will see significantly increased crawling by
[Smartphone Googlebot](/search/docs/crawling-indexing/overview-google-crawlers), and
the snippets in the results, as well as the content on the
[Google cache pages](https://support.google.com/websearch/answer/1687222),
will be from the mobile version of the pages.

[As we said](/search/blog/2016/11/mobile-first-indexing), sites that make use of
[responsive web design](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#responsive-design)
and correctly implement
[dynamic serving](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
(that include all of the desktop content and markup) generally don't have to do anything. Here are
some extra tips that help ensure a site is ready for mobile-first indexing:

- Make sure the mobile version of the site also has the important, high-quality content. This
  includes text, images (with `alt` attributes), and videos - in the usual crawlable
  and indexable formats.
- Structured data is important for indexing and search features that users love: it should be
  both on the mobile and desktop version of the site. Ensure URLs within the structured data are
  updated to the mobile version on the mobile pages.
- Metadata should be present on both versions of the site. It provides hints about the content on
  a page for indexing and serving. For example, make sure that titles and meta descriptions are
  equivalent across both versions of all pages on the site.
- No changes are necessary for interlinking with separate mobile URLs (m.-dot sites). For
  [sites using separate mobile URLs](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#separate-urls),
  keep the existing `link` `rel=canonical` and `link`
  `rel=alternate` elements between these versions.
- Check hreflang links on separate mobile URLs. When using
  [`link` `rel=hreflang`](/search/docs/specialty/international/localized-versions)
  tags for
  [internationalization](/search/docs/specialty/international/managing-multi-regional-sites),
  link between mobile and desktop URLs separately. Your mobile URLs' hreflang should point to the
  other language/region versions on other mobile URLs, and similarly link desktop with other
  desktop URLs using `hreflang` `link` elements there.
- Ensure the servers hosting the site have enough capacity to handle potentially increased
  [crawl rate](/search/blog/2017/01/what-crawl-budget-means-for-googlebot). This
  doesn't affect sites that use responsive web design and dynamic serving, only sites where the
  mobile version is on a separate host, such as m.example.com.

We will be evaluating sites independently on their readiness for mobile-first indexing based on
the above criteria and transitioning them when ready. This process has already started for a
handful of sites and is closely being monitored by the search team.

We continue to be cautious with rolling out mobile-first indexing. We believe taking this slowly
will help site owners get their sites ready for mobile users, and because of that, we currently
don't have a timeline for when it's going to be completed. If you have any questions, drop by our
[Webmaster forums](https://support.google.com/webmasters/go/community)
or our [public events](/search/events).
