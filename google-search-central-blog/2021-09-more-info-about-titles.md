---
title: "More information on how Google generates titles for web page results"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2021-09-more-info-about-titles"
url: "https://developers.google.com/search/blog/2021/09/more-info-about-titles"
canonical: "https://developers.google.com/search/blog/2021/09/more-info-about-titles"
author: "Danny Sullivan, public liaison for Google Search"
published: "2021-09-17T00:00:00+00:00"
updated: "2021-09-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:39:45+00:00"
status_code: 200
html_hash: "4764a11ee0c33101744ce9ad543b5c5eaa914cb6a2c8ea177f44fe956583d193"
clean_word_count: 1039
clean_char_count: 6205
---
# More information on how Google generates titles for web page results

Last month, we shared about our new system for
[generating titles for web page
results](/search/blog/2021/08/update-to-generating-page-titles). Thanks to your feedback, which has been much appreciated, we've further refined
our titles system. Here's more about what we've been doing and some additional guidance for creators.

## Title elements are used the most

As we said in our [last post](/search/blog/2021/08/update-to-generating-page-titles),
our new system uses HTML title elements (sometimes called title tags) as the titles we show in
search results for the vast majority of web page results. Based on your
[feedback](https://support.google.com/webmasters/thread/122879386/your-feedback-on-titles-shown-in-search-results), we made changes to our system which means that title elements are now
used around 87% of the time, rather than around 80% before.

Why not use title elements 100% of the time? [Since
2012](/search/blog/2012/01/better-page-titles-in-search-results), we've used text beyond title elements in cases where our systems determine the title
element might not describe a page as well as it could. Some pages have empty titles. Some use the
same titles on every page regardless of the page's actual content. Some pages have no title
elements at all.

## Examples of going beyond title elements

Our new system is designed to address even more situations where going beyond the title element
might be helpful. Here are some examples of things it detects and adjusts for, which are based on
real issues we see across the trillions of pages we list.

### Half-empty titles

A half-empty title often occurs when large sites use templates to craft titles for their web pages,
and something is missing. The template might put a summary of the page first in the title, followed
by the site name. In half-empty titles, the summary is often missing, which produces titles like this:

> | Site Name

Our system is designed to detect half-empty titles and adjust by looking at information in header
elements or other large and prominent text on the page. This can produce a title in line with what
the site itself likely intended to happen, like this:

> Product Name | Site Name

### Obsolete titles

Obsolete titles often happen when the same page is used year-after-year for recurring information
but the title element didn't get updated to reflect the latest date. Consider a title element like
this:

> 2020 admissions criteria - University of Awesome

In this example, the title is for a page about getting admitted to a university. The page has a
large, visible headline that says "2021 admissions criteria" but for some reason, the title element
wasn't updated to the current date. Our system detects this inconsistency and uses the right date
from the headline in the title to say this:

> 2021 admissions criteria - University of Awesome

### Inaccurate titles

Sometimes titles aren't accurately reflecting what a page is about. For example, the page could
have dynamic content with a title element like:

> Giant stuffed animals, teddy bears, polar bears - Site Name

It's reasonable that people would expect to find these named products appearing on the page. But
this is a static title for a page with content that dynamically changes. Sometimes these products
might appear, but sometimes they don't.

Our system tries to understand if the title isn't accurately showing what a page is about. If so,
it might modify the title so that the use better knows what to expect, like this:

> Stuffed animals - Site Name

### Micro-boilerplate titles

Boilerplate titles are fairly easy to detect. We see the same title on all or nearly all the
pages within a site. Micro-boilerplate titles are where we see boilerplate title elements within
a subset of pages within a site. Our system detects and helps with these cases, just as we do with
boilerplate title elements overall.

Consider an online discussion forum about television shows. It might have areas for different shows,
and then for each show, it may have areas for threads for individual seasons. The micro-boilerplate
title elements appear on the season pages. The titles omit the season numbers, so it's not clear
which page is for what season. That produces duplicate titles like this:

> My so-called amazing TV show
>
> My so-called amazing TV show
>
> My so-called amazing TV show

Our system can detect the season number used in large, prominent headline text and insert those in
the title, so the titles are more helpful:

> Season 1 - My so-called amazing TV show
>
> Season 2 - My so-called amazing TV show
>
> Season 3 - My so-called amazing TV show

## Guidance for site owners

Our main advice to site owners about titles remains generally the same as on our
[help page](/search/docs/appearance/title-link) about the topic.
Focus on creating great HTML title elements. Those are by far what we use the most.

Beyond this, consider the examples in this post to understand if you might have similar patterns
that could cause our systems to look beyond your title elements. The changes we've made are
largely designed to help compensate for issues that creators might not realize their titles are
having. Making changes may help ensure your title element is again used. That's really our
preference, as well.

## Our work to improve titles will continue

No system for producing titles will be perfect. Using title elements 100% of the time has issues,
as illustrated above. But we also know our title system isn't perfect either. Your feedback has
been immensely helpful to improve our system. We welcome further feedback in our
[forum](https://support.google.com/webmasters/community), including
existing threads on this topic in [English](https://support.google.com/webmasters/thread/122879386/your-feedback-on-titles-shown-in-search-results) and [Japanese](https://support.google.com/webmasters/thread/125182163/%E6%A4%9C%E7%B4%A2%E7%B5%90%E6%9E%9C%E3%81%AB%E8%A1%A8%E7%A4%BA%E3%81%95%E3%82%8C%E3%82%8B%E3%82%BF%E3%82%A4%E3%83%88%E3%83%AB%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%83%95%E3%82%A3%E3%83%BC%E3%83%89%E3%83%90%E3%83%83%E3%82%AF).
