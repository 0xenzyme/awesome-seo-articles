---
title: "The Rich Results Test is out of beta"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2020-07-rich-results-test-out-of-beta"
url: "https://developers.google.com/search/blog/2020/07/rich-results-test-out-of-beta"
canonical: "https://developers.google.com/search/blog/2020/07/rich-results-test-out-of-beta"
author: null
published: "2020-07-07T00:00:00+00:00"
updated: "2020-07-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:37:04+00:00"
status_code: 200
html_hash: "8e61f5a9160d2879cc2b3dbc379f9882c0ac70b323e0c28a652fe705e20f7474"
clean_word_count: 386
clean_char_count: 2470
---
# The Rich Results Test is out of beta

Today we are announcing that the
[Rich Results Test](https://search.google.com/test/rich-results)
fully supports all Google Search rich result features - it's out of beta. In addition, we are
preparing to deprecate the Structured Data Testing Tool - it will still be available for the
time being, but going forward we strongly recommend you use the Rich Results Test to test and
validate your structured data.

Rich results are experiences on Google Search that go beyond the standard blue link. They're powered by
[structured data](/search/docs/appearance/structured-data/intro-structured-data) and can
include carousels, images, or other non-textual elements. Over the last couple years we've
developed the Rich Results Test to help you test your structured data and preview your rich results.

Here are some reasons the new tool will serve you better:

- It shows which Search feature enhancements are valid for the markup you are providing
- It handles dynamically loaded structured data markup more effectively
- It renders both mobile and desktop versions of a result
- It is fully aligned with Search Console reports

You can use the Rich Results Test to test a code snippet or a URL to a page. The test returns
errors and warnings we detect on your page. Note that errors disqualify your page from showing
up as a rich result. While warnings might limit the appearance, your page is still eligible for
showing up as a rich result. For example, if there was a warning for a missing image property,
that page could still appear as a rich result, just without an image.

Here are some examples of what you'll see when using the tool.

![valid structured data on Rich Results Test](/static/search/blog/images/import/fc7217406295798b3dceca0cfbcc7222.jpg)
![code explorer showing error on Rich Results Test](/static/search/blog/images/import/8ef46cf2f497dd7077c705e002163c4a.jpg)
![search preview on Rich Results Test](/static/search/blog/images/import/bf2dfef0b7b5edbb2396bff8f304bf4f.jpg)

Learn more about the
[Rich Results Test](https://support.google.com/webmasters/answer/7445569), and let us know if you have any feedback either through the
[help community](https://support.google.com/webmasters/threads?thread_filter=(category%3Astructured_data)&max_results=20)
or
[Twitter](https://twitter.com/googlesearchc).

*Posted by [Moshe Samet](https://www.linkedin.com/in/moshe-samet-5465326/), Search Console Product Manager*
