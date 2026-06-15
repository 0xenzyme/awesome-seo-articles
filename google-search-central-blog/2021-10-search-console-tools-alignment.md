---
title: "Aligning Search Console testing tools and the URL Inspection tool"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2021-10-search-console-tools-alignment"
url: "https://developers.google.com/search/blog/2021/10/search-console-tools-alignment"
canonical: "https://developers.google.com/search/blog/2021/10/search-console-tools-alignment"
author: "Amir Taboul, Search Console Software Engineer"
published: "2021-10-11T00:00:00+00:00"
updated: "2021-10-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:39:49+00:00"
status_code: 200
html_hash: "6d1aa3ff592fd86dd218f255e656ccdb5a31cbb08733c5624409fc181813ce78"
clean_word_count: 275
clean_char_count: 1785
---
# Aligning Search Console testing tools and the URL Inspection tool

In order to help users find and fix issues in web pages, the Search Console team provides three public standalone tools to website owners and SEOs, specifically for
[AMP](https://search.google.com/test/amp), [Mobile Friendly](https://goo.gle/mobilefriendly), and [Rich Results](https://goo.gle/richresults).

These tools are internally powered by the same engine as Search Console’s [URL Inspection tool](https://support.google.com/webmasters/answer/9012289),
which has evolved throughout the years. While the engine is the same, the UI of the tools has advanced separately. Today, we’re making changes in their designs and
improving features to be fully aligned with the URL Inspection tool.

The changes include standardization of previous features, plus new features that you may be familiar with from the URL Inspection tool. Specifically, from now on the
following fields will be reported both on public testing and URL inspection tools.

- **Page availability** - Whether Google was able to crawl the page, when it was crawled, or any obstacles that it encountered when crawling the URL.
- **HTTP headers** - The HTTP header response returned from the inspected URL.
- **Page screenshot** - The rendered page as seen by Google.
- **Paired AMP inspection**, Inspect both canonical and AMP URL.

![New Rich Results test](/static/search/blog/images/rich-results-test.png "New Rich Results test")

If you have any questions or feedback, click the **send feedback** button available on Google Search Console, reach out to us [on
Twitter](https://twitter.com/googlesearchc), or post a question in the [Search Central community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)).
