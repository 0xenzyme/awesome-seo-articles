---
title: "Enriching Search Results Through Structured Data"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2019-04-enriching-search-results-structured-data"
url: "https://developers.google.com/search/blog/2019/04/enriching-search-results-structured-data"
canonical: "https://developers.google.com/search/blog/2019/04/enriching-search-results-structured-data"
author: "Daniel Waisberg"
published: "2019-04-24T00:00:00+00:00"
updated: "2019-04-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:33:56+00:00"
status_code: 200
html_hash: "4ec2661c594d1bd46a4cbfdc1b9cd68c6bdcabf3a340da56195c00ffe499da2b"
clean_word_count: 811
clean_char_count: 5497
---
# Enriching Search Results Through Structured Data

For many years we have been recommending the use of structured data on websites to enable a
richer search experience. When you add markup to your content, you help search engines
understand the different components of a page. When Google's systems understand your page more
clearly, Google Search can surface content through the cool features discussed in this post,
which can enhance the user experience and get you more traffic.

We've worked hard to provide you with tools to understand how your websites are shown in Google
Search results and whether there are issues you can fix. To help give a complete overview of
structured data, we decided to do a series to explore it. This post provides a quick intro and
discusses some best practices, future posts will focus on how to use Search Console to succeed
with structured data.

## What is structured data?

Structured data is a common way of providing information about a page and its content - we
recommend using the schema.org vocabulary for doing so. Google supports three different formats
of in-page markup: JSON-LD (recommended), Microdata, and RDFa. Different search features require
different kinds of structured data - you can learn more about these in our
[search gallery](/search/docs/appearance/structured-data/search-gallery). Our develo
per documentation has more details on the
[basics of structured data](/search/docs/appearance/structured-data/intro-structured-data).

Structured data helps Google's systems understand your content more accurately, which means it's
better for users as they will get more relevant results. If you implement structured data your
pages may become eligible to be shown with an enhanced appearance in Google search results.

## Sites that use structured data see results

Over the years, we've seen a growing adoption of structured data in the ecosystem. In general,
rich results help users to better understand how your pages are relevant to their searches, so
they translate into success for websites. Here are some results that are showcased in our
[case studies gallery](/search/case-studies):

- Eventbrite leveraged event structured data and saw 100% increase in the typical YOY growth of
  traffic from search.
- Jobrapido integrated with the job experience on Google Search and saw 115% increase in organic
  traffic, 270% increase of new user registrations from organic traffic, and 15% lower bounce rate
  for Google visitors to job pages.
- Rakuten used the recipe search experience and saw a 2.7X increase in traffic from search engines
  and a 1.5X increase in session duration.

## How to use structured data?

There are a few ways your site could benefit from structured data. Below we discuss some examples
grouped by different types of goals: increase brand awareness, highlight content, and highlight
product information.

### Increase brand awareness

One thing you can do to promote your brand with structured data is to take advantage of features
such as
[Logo](/search/docs/appearance/structured-data/organization#logo),
[Local business](/search/docs/appearance/structured-data/local-business), and
[Sitelinks searchbox](/search/docs/appearance/structured-data/sitelinks-searchbox). In
addition to adding structured data, you should
[verify your site](https://support.google.com/knowledgepanel/answer/7534902)
for the Knowledge Panel and
[claim your Business Profile](https://support.google.com/business/answer/2911778).
Here is an example of the knowledge panel with a Logo.

![a knowledge panel for the Google entity](/static/search/blog/images/import/11b525148241e0c462a9b141d1447ec4.png)

### Highlight content

If you publish content on the web, there are a number of features that can help promote your
content and attract more users, depending on your industry. For example:
[Article](/search/docs/appearance/structured-data/article),
[Breadcrumb](/search/docs/appearance/structured-data/breadcrumb),
[Event](/search/docs/appearance/structured-data/event),
[Job](/search/docs/appearance/structured-data/job-posting),
[Q&A](/search/docs/appearance/structured-data/qapage),
[Recipe](/search/docs/appearance/structured-data/recipe),
[Review](/search/docs/appearance/structured-data/review-snippet)
and others. Here is an example of a recipe rich result.

![Diagram of a recipe search result](/static/search/blog/images/import/5bc97f00d07bfb73939658de98e1e3d2.png)

### Highlight product information

If you sell merchandise, you could add
[product](/search/docs/appearance/structured-data/product)
structured data to your page, including price, availability, and review ratings. Here is how your
product might show for a relevant search.

![diagram of how product information may display in Google Images](/static/search/blog/images/import/12f30de91be99d558098366eba25abc8.png)

## Try it and let us know

Now that you understand the importance of structured data, try our
[codelab](https://codelabs.developers.google.com/codelabs/structured-data/index.html#0)
to learn how to add it to your pages. Stay tuned to learn more about structured data, in the
coming posts we'll be discussing how to use Search Console to better analyze your efforts.

We would love to hear your thoughts and stories on how structured data works for you, send us any feedback either through
[Twitter](https://twitter.com/googlesearchc) or
[our forum](https://support.google.com/webmasters/threads?thread_filter=(category:structured_data)).
