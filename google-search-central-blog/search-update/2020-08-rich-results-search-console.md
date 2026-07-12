---
title: "Rich Results and Search Console Webmaster Conference Lightning Talk"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2020-08-rich-results-search-console"
url: "https://developers.google.com/search/blog/2020/08/rich-results-search-console"
canonical: "https://developers.google.com/search/blog/2020/08/rich-results-search-console"
author: "Daniel Waisberg"
published: "2020-08-11T00:00:00+00:00"
updated: "2020-08-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:37:28+00:00"
status_code: 200
html_hash: "9172d3f4e2f8ffdba1285850896048c39dfcf14eaffefdd7a5044b79632a1190"
clean_word_count: 1156
clean_char_count: 7457
---
# Rich Results and Search Console Webmaster Conference Lightning Talk

A few weeks ago we held another
[Webmaster Conference Lightning Talk](https://www.youtube.com/playlist?list=PLKoqnv2vTMUNf6w9wUu7RgxHkaTrq2Zpf),
this time about [Rich Results and Search Console](https://www.youtube.com/watch?v=B4MlM1sJ5ZE).
During the talk we hosted a live chat and a lot of viewers asked questions - we tried to answer
all we could, but our typing skills didn't match the challenge...so we thought we'd follow up on
the questions posed in this blog post.

If you missed the video, you can watch it below: it discusses how to get started with rich
results and use Search Console to optimize your search appearance in Google Search.

## Rich Results and Search Console FAQs

### Will a site rank higher against competitors if it implements structured data?

[Structured data](/search/docs/appearance/structured-data/intro-structured-data)
by itself is not a generic ranking factor. However, it can help Google to understand what
the page is about, which can make it easier for us to show it where relevant and make it
eligible for additional search experiences.

### Which structured data would you recommend to use in Ecommerce category pages?

You don't need to mark up the products on a category page, a Product
should only be marked up when they are the primary element on a page.

### How much content should be included in my structured data? Can there be too much?

There is no limit to how much structured data you can implement on
your pages, but make sure you're sticking to the
[general guidelines](/search/docs/appearance/structured-data/sd-policies).
For example the markup should always be visible to users and representative of the main
content of the page.

### What exactly are FAQ clicks and impressions based on?

A [Frequently Asked Question (FAQ) page](/search/docs/appearance/structured-data/faqpage)
contains a list of questions and answers pertaining to a particular topic. Properly marked
up FAQ pages may be eligible to have a rich result on Search and an Action on the Google
Assistant, which can help site owners reach the right users. These rich results include
snippets with frequently asked questions, allowing users to expand and collapse answers to
them. Every time such a result appears in Search results for a user it will be counted as
an impression on Search Console, and if the user clicks to visit the website it will be
counted as a click. Clicks to expand and collapse the search result will not be counted as
clicks on Search Console as they do not lead the user to the website. You can check
impressions and clicks on your FAQ rich results using the 'Search appearance' tab in the
[Search Performance report](https://support.google.com/webmasters/answer/7576553).

### Will Google show rich results for reviews made by the review host site?

Reviews must not be written or provided by the business or content
provider. According to our
[review snippets guidelines](/search/docs/appearance/structured-data/review-snippet#guidelines):
"Ratings must be sourced directly from users" - publishing reviews written by the business
itself are against the guidelines and might trigger a
[Manual Action](https://support.google.com/webmasters/answer/9044175#spammy-structured-markup).

### There are schema types that are not used by Google, why should we use them?

Google supports a number of
[schema types](/search/docs/appearance/structured-data/search-gallery),
but other search engines can use different types to surface rich results, so you might
want to implement it for them.

### Why do rich results that previously appeared in Search sometimes disappear?

The Google algorithm tailors search results to create what it thinks
is the best search experience for each user, depending on many variables, including search
history, location, and device type. In some cases, it may determine that one feature is
more appropriate than another, or even that a plain blue link is best. Check the
[Rich Results Status report](https://support.google.com/webmasters/answer/7552505).
If you don't see a drop in the number of valid items, or a spike in errors, your
implementation should be fine.

### How can I verify my dynamically generated structured data?

The safest way to check your structured data implementation is to
[inspect the URL](https://support.google.com/webmasters/answer/9012289) on
Search Console. This will provide information about Google's indexed version of a specific
page. You can also use the [Rich Results Test](https://goo.gle/richresults)
public tool to get a verdict. If you don't see the structured data through those tools,
your markup is not valid.

### How can I add structured data in WordPress?

There are a number of
[WordPress plugins](https://wordpress.org/plugins/search/structured+data/)
available that could help with adding structured data. Also check your theme settings, it
might also support some types of markup.

### With the deprecation of the Structured Data Testing Tool, will the Rich Results Test support structured data that is not supported by Google Search?

The [Rich Results Test](https://goo.gle/richresults)
supports all structured data that triggers a rich result on Google Search, and as Google
creates new experiences for more structured data types we'll add support for them in this
test. While we prepare to deprecate the Structured Data Testing Tool, we'll be
investigating how a generic tool can be supported outside of Google.

## Stay Tuned!

If you missed our previous lightning talks, check the
[WMConf Lightning Talk playlist](https://www.youtube.com/playlist?list=PLKoqnv2vTMUNf6w9wUu7RgxHkaTrq2Zpf).
Also make sure to [subscribe to our YouTube channel](https://www.youtube.com/channel/UCWf2ZlNsCGDS89VBF_awNvA?sub_confirmation=1)
for more videos to come! We definitely recommend joining the premieres on YouTube to participate
in the live chat and Q&A session for each episode!

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],["The content addresses common questions about rich results and structured data. Key information includes: structured data is not a ranking factor but aids Google's understanding; product markup should be on product pages, not category pages; there's no limit to structured data quantity, but it must be visible and relevant. FAQ page rich results count impressions and clicks when displayed in search. Reviews must be user-sourced, not from the business. The Rich Results Test tool verifies data for Google Search. Additional structured data types can be added for other search engines.\n"]]
