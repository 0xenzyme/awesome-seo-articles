---
title: "Focusing on the new Search Console"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2019-01-focusing-on-new-search-console"
url: "https://developers.google.com/search/blog/2019/01/focusing-on-new-search-console"
canonical: "https://developers.google.com/search/blog/2019/01/focusing-on-new-search-console"
author: "Hillel Maoz"
published: "2019-01-25T00:00:00+00:00"
updated: "2019-01-25T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:33:33+00:00"
status_code: 200
html_hash: "315b1d4732cb4771f4ad48ed2cc057548767cdae2789b3180df85fd9c5ccab0c"
clean_word_count: 1048
clean_char_count: 6364
---
# Focusing on the new Search Console

Over the last year, the
[new Search Console](https://support.google.com/webmasters/answer/7451491)
has been
[growing](/search/blog/2018/01/introducing-new-search-console) and
[growing](/search/blog/2018/09/the-new-search-console-is-graduating),
with the goal of making it easier for site owners to focus on the important tasks. For us, focus
means being able to put in all our work into the new Search Console, being committed to the users,
and with that, being able to turn off some of the older, perhaps already-improved, aspects of the
old Search Console. This gives us space to further build out the new Search Console, adding and
improving features over time.

Here are some of the upcoming
[changes in Search Console](https://support.google.com/webmasters/answer/9073702)
that we're planning on making towards end of March, 2019:

## Crawl errors in the new Index Coverage report

One of the more common pieces of feedback we received was that the list of crawl errors in Search
Console was not actionable when it came to setting priorities (it's normal that Google crawls URLs
which don't exist, it's not something that needs to be fixed on the website). By changing the
focus on issues and patterns used for site indexing, we believe that site owners will be able to
find and fix issues much faster (and when issues are fixed, you can request reprocessing quickly
too). With this, we're going to remove the old Crawl Errors report - for desktop, smartphone, and
site-wide errors. We'll continue to improve the way issues are recognized and flagged, so if
there's something that would help you, please submit feedback in the tools.

Along with the Crawl Errors report, we're also deprecating the crawl errors API that's based on
the same internal systems. At the moment, we don't have a replacement for this API. We'll inform
API users of this change directly.

## Sitemaps data in Index Coverage

As we move forward with the new Search Console, we're turning the old sitemaps report off. The new
sitemaps report has most of the functionality of the old report, and we're aiming to bring the
rest of the information - specifically for images and video - to the new reports over time.
Moreover, to track URLs submitted in sitemap files, within the Index Coverage report you can
select and filter using your sitemap files. This makes it easier to focus on URLs that you care
about.

## Using the URL inspection tool to fetch as Google

The new
[URL inspection tool](https://support.google.com/webmasters/answer/9012289)
offers many ways to check and review URLs on your website. It provides both a look into the
current indexing, as well as a live check of URLs that you've recently changed. In the meantime,
this tool shows even more information on URLs, such as the HTTP headers, page resource, the
JavaScript console log, and a screenshot of the page. From there, you can also submit pages for
re-processing, to have them added or updated in our search results as quickly as possible.

## User-management is now in settings

We've improved the user management interface and decreased clutter from the tool by merging it
with the Settings section of the new Search Console. This replaces the
[user-management features](https://support.google.com/webmasters/answer/2453966)
in the old Search Console.

## Structured data dashboard to dedicated reports per vertical

To help you implement Rich Results for you site, we added several reports to the new Search
Console last year. These include Jobs, Recipes, Events and Q&A.; We are committed to keep
adding reports like these to the new Search Console. When Google encounters a syntax error parsing
structured data on a page, it will also be reported in aggregate to make sure you don't miss
anything critical.

Other Structured Data types that are not supported with Rich Results features, will not be
reported in Search Console anymore. We hope this reduces distraction from non-critical issues, and
help you to focus on fixing problems which could be visible in Search.

## Letting go of some old features

With the focus on features that we believe are critical to site owners, we've had to make a hard
decision to drop some features in Search Console. In particular:

HTML suggestions - finding short and duplicated titles can be useful for site owners, but Google's
algorithms have gotten
[better at showing and improving titles](/search/docs/advanced/appearance/good-titles-snippets)
over the years. We still believe this is something useful for sites to look into, and there are
some really good tools that help you to
[crawl your website to extract titles and descriptions](https://www.google.com/search?q=crawl+website+for+titles+and+descriptions)
too.

Property Sets - while they're loved by some site owners, the small number of users makes it hard
to justify maintaining this feature. However, we did learn that users need a more comprehensive
view of their website and so we will soon add the option of managing a search console account over
an entire domain (regardless of schema type and sub-domains). Stay tuned!

Android Apps - most of the relevant functionality has been moved to the
[Firebase console](https://console.firebase.google.com/)
over the years.

Blocked resources - we added this functionality to help sites with unblocking of CSS and
JavaScript files for mobile-friendliness several years back. In the meantime, these issues have
gotten much fewer, the usage of this tool has dropped significantly, and you're able to find
blocked resources directly in the
[URL inspection tool](https://support.google.com/webmasters/answer/9012289).

## Please send us feedback!

We realize some of these changes will affect your work-flows, so we want to let you know about
them as early as possible. Please send us your feedback directly in the new Search Console, if
there are aspects which are unclear, or which would ideally be different for your use-case. For
more detailed feedback, please use our
[help forums](https://support.google.com/webmasters/go/community),
you can include screenshots and ideas. In the long run, we believe the new Search Console will
make things much easier, help you focus on the issues affecting your site, and the opportunities
available to your site, with regards to Search.

We're looking forward to an exciting year!
