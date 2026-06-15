---
title: "Introducing a new way for sites to highlight COVID-19 announcements on Google Search"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2020-04-highlight-covid-19-announcements-search"
url: "https://developers.google.com/search/blog/2020/04/highlight-covid-19-announcements-search"
canonical: "https://developers.google.com/search/blog/2020/04/highlight-covid-19-announcements-search"
author: "Lizzi Sassman, Danny Sullivan"
published: "2020-04-03T00:00:00+00:00"
updated: "2020-04-03T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:36:33+00:00"
status_code: 200
html_hash: "cf47e7748731561692d67b34492a9e440ed899f11529fafadc4e068158157d1a"
clean_word_count: 807
clean_char_count: 5657
---
# Introducing a new way for sites to highlight COVID-19 announcements on Google Search

Due to the COVID-19 outbreak, many organizations and groups are publishing important
coronavirus-related announcements that affect our everyday lives.

In response, we're introducing a new way for these special announcements to be highlighted on Google Search. Sites can
[add `SpecialAnnouncement` structured data](/search/docs/appearance/structured-data/special-announcements)
to their web pages or [submit
a COVID-19 announcement in Search Console](/search/docs/appearance/structured-data/special-announcements#using-search-console).

At first, we're using this information to highlight announcements in Google Search from health
and government agency sites, to cover important updates like school closures or stay-at-home
directives.

We are actively developing this feature, and we hope to expand it to include more sites. While
we might not immediately show announcements from other types of sites, seeing the markup will
help us better understand how to expand this feature.

**Please note**: beyond special announcements, there are a range of other options
that sites can use to highlight information such as canceled events or changes to business
hours. You can learn more about these at the end of this post.

## How COVID-19 announcements appear in Search

When `SpecialAnnouncement` structured data is added to a page, that
content can be eligible to appear with a COVID-19 announcement rich result, in addition to the
page's regular snippet description. A COVID-19 announcement rich result can contain a short
summary that can be expanded to view more. Please note that the format may change over
time, and you may not see results in Google Search right away.

![COVID-19 announcement in Google Search](/static/search/blog/images/import/9ed0241f779f44f6ab6085e3edb93ab3.png)

## How to implement your COVID-19 announcements

There are two ways that you can implement your COVID-19 announcements.

### Recommended: Add structured data to your web page

Structured data is a standardized format for providing information about a page and classifying
the page content. We recommend using this method because it is the easiest way for us to take
in this information, it enables reporting through
[Search Console](https://search.google.com/search-console/about) in the future, and
enables you to make updates. Learn how to
[add structured data to COVID-19 announcements](/search/docs/appearance/structured-data/special-announcements).

### Alternative: Submit announcements in Search Console

If you don't have the technical ability or support to implement structured data, you can
[submit a COVID-19 announcement in Search Console](/search/docs/appearance/structured-data/special-announcements#using-search-console).
This tool is still in beta testing, and you may see changes.

This method is not preferred and is intended only as a short-term solution. With structured
data, your announcement highlights can automatically update when your pages change. With the
tool, you'll have to manually update announcements. Also, announcements made this way cannot be
monitored through special reporting that will be made available through Search Console in the
future.

If you do need to submit this way, you'll need to first be
[verified in Search Console](https://support.google.com/webmasters/answer/9008080).
Then you can
[submit a COVID-19 announcement](https://search.google.com/search-console/special-announcement):

![Submit a COVID-19 announcement in Search Console](/static/search/blog/images/import/7d6d6467e9e2b00768e80032303df1ae.png)

## More COVID-19 resources for sites from Google Search

Beyond special announcements markup, there are other ways you can highlight other types of activities that may be impacted because of COVID-19:

- **Best practices for health and government sites**: If you are a representative of
  a health or government website, and you have important information about coronavirus for the
  general public,
  [here are some recommendations](/search/docs/advanced/guidelines/health-government-websites)
  for how to make this information more visible on Google Search.
- **Surface your common FAQs**: If your site has common FAQs,
  [adding FAQ markup](/search/docs/appearance/structured-data/faqpage)
  can help Google Search surface your answers.
- **Pausing your business online**: See our blog post on
  [how to pause your business online](/search/blog/2020/03/how-to-pause-your-business-online-in)
  in a way that minimizes impacts with Google Search.
- **Business hours and temporary closures**: Review the guidance from on how to
  [change your business hours or indicate temporary closures](https://support.google.com/business/answer/9773423)
  or how to
  [create COVID-19 posts](https://support.google.com/business/answer/7342169?p=covid_posts#covidpost).
- **Events**: If you hold events, look over the
  [new properties for marking them virtual, postponed, or canceled](/search/blog/2020/03/new-properties-virtual-or-canceled-events).
- **Knowledge Panels**: Understand how to
  [recommend changes to your Google knowledge panel](https://support.google.com/knowledgepanel/answer/7534842)
  (or
  [how to claim it](https://support.google.com/knowledgepanel/answer/7534902), if you haven't already).
- **Fix an overloaded server**: Learn how to
  [determine a server's bottleneck, quickly fix the
  bottleneck, improve server performance, and prevent regressions](https://web.dev/articles/overloaded-server).

If you have any questions or comments, please let us know
[on Twitter](https://twitter.com/googlesearchc).
