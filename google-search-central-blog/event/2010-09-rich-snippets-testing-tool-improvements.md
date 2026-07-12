---
title: "Rich snippets: testing tool improvements, breadcrumbs, and events"
source: google-search-central-blog
content_type: "event"
freshness_risk: "historical"
slug: "2010-09-rich-snippets-testing-tool-improvements"
url: "https://developers.google.com/search/blog/2010/09/rich-snippets-testing-tool-improvements"
canonical: "https://developers.google.com/search/blog/2010/09/rich-snippets-testing-tool-improvements"
author: "Pravir Gupta"
published: "2010-09-02T00:00:00+00:00"
updated: "2010-09-02T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:08:53+00:00"
status_code: 200
html_hash: "00e8e646a595c355b913e8770bd601296a97c796a02ce5d439e4ecee130ac01f"
clean_word_count: 577
clean_char_count: 3827
---
# Rich snippets: testing tool improvements, breadcrumbs, and events

Since the initial roll-out of
[rich snippets](/search/docs/appearance/enriched-search-results)
in 2009, webmasters have shown a great deal of interest in adding markup to their web pages to
improve their listings in search results. When webmasters add markup using
[microdata](/search/docs/appearance/structured-data/intro-structured-data),
[microformats](/search/docs/appearance/structured-data/intro-structured-data), or
[RDFa](/search/docs/appearance/structured-data/intro-structured-data), Google
is able to understand the content on web pages and show search result snippets that better convey
the information on the page. Thanks to steady adoption by webmasters, we now see more than twice
as many searches with rich snippets in the results in the US, and a four-fold increase globally,
compared to one year ago. Here are three recent product updates.

## Testing tool improvements

Despite the healthy adoption rate by webmasters so far, implementing the rich snippets markup
correctly can still be a major challenge. To help address this, we've added new error messages to the
[rich snippets testing tool](https://www.google.com/webmasters/tools/richsnippets)
to help you better identify and fix any problems with the markup.

![view of the rich snippets testing tool](/static/search/blog/images/import/2ef387df73c540511fc9e39c64466eb0.png)

If you've added markup in the past but haven't seen rich snippets appear for your site, we
encourage you to take a few minutes to try testing the markup again on the updated testing tool.

## Rich snippets markup for breadcrumbs

Last year, Google announced a modification to search results to
[begin
showing site hierarchies](https://googleblog.blogspot.com/2009/11/new-site-hierarchies-display-in-search.html) (typically referred to as "breadcrumbs") rather than standard URLs
in cases where it helped users to better understand a website:

![result showing breadcrumb navigation for the page](/static/search/blog/images/import/a4364c8c80d62f3ec323c45da78ce1df.png)

We are now adding support for a
[Breadcrumbs](/search/docs/appearance/structured-data/breadcrumb)
markup format that allows webmasters to explicitly identify the breadcrumb hierarchy on their pages.

If the breadcrumbs UI is already showing for your site, we'll continue to show it even if you don't
do the markup, so don't worry about any existing UI disappearing. Note that this new format is
experimental. Based on feedback and on other available standards, this format may be modified or
replaced in the future. As with other rich snippet types, while markup helps us to better understand
the content on your site, it does not guarantee that the breadcrumbs UI will be shown for your web
pages in search results.

## Events

In January, we added support for
[rich snippets for events](/search/blog/2010/01/introducing-new-rich-snippets-format).
If a web page containing events listings showed up in search results, up to three links to specific
events could be shown in the search result snippet.

This works well for general queries like
[concerts in seattle](https://www.google.com/search?q=concerts+in+seattle),
but we also wanted to improve the search experience when searching for a specific event. We will
now show rich snippets when pages containing a single event show up in search results. Single
event rich snippets now contain the date and location of the event:

![result showing the date and time of the event, powered by structured data](/static/search/blog/images/import/d5e0ff0088d9bf047082f51bd673c714.png)

For instructions on adding events markup, refer to the
[events page](/search/docs/appearance/structured-data/event) in the
[rich snippets documentation](/search/docs/appearance/structured-data/search-gallery).
