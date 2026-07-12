---
title: "Google Search at I/O 2018"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2018-06-google-search-at-io-2018"
url: "https://developers.google.com/search/blog/2018/06/google-search-at-io-2018"
canonical: "https://developers.google.com/search/blog/2018/06/google-search-at-io-2018"
author: "Martin Splitt"
published: "2018-06-07T00:00:00+00:00"
updated: "2018-06-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2018_very_old"
  - "news_or_research"
  - "title_year_2018_before_2026"
fetched_at: "2026-06-14T13:32:23+00:00"
status_code: 200
html_hash: "e5c6400c515d0e45ffa32c673600392c323875efeb298524472aa24e82bd4316"
clean_word_count: 700
clean_char_count: 4471
---
# Google Search at I/O 2018

With the eleventh annual [Google I/O](https://events.google.com/io/)
wrapped up, it's a great time to reflect on some of the highlights.

## What we did at I/O

The event was a wonderful way to meet many great people from various communities across the globe,
exchange ideas, and gather feedback. Besides many great
[web sessions](https://www.youtube.com/watch?v=FglWLLA4g-s),
[codelabs](https://codelabs.developers.google.com/codelabs/structured-data/index.html?index=..%2F..%2Findex#0),
and office hours, we shared a few things with the community in two
sessions specific to Search:

- [Deliver search-friendly JavaScript-powered websites](https://www.youtube.com/watch?v=PFwUbgvpdaQ)
  with John Mueller and Tom Greenaway
- [Build a successful web presence with Google Search](https://www.youtube.com/watch?v=NO-sdBzb1Hc)
  with Mariya Moeva and John Mueller

![Mariya Moeva and John Mueller on stage at Google I/O](/static/search/blog/images/import/4b520b62416053c25b3a5d8978ecc7b7.png)

The sessions included the launch of JavaScript error reporting in the
[Mobile Friendly Test tool](https://search.google.com/test/mobile-friendly),
dynamic rendering (we will discuss this in more detail in a future post), and an explanation of
how CMS can use the Indexing and Search Console APIs to provide users with insights. For example,
Wix lets their users
[submit their home page to the index](https://youtu.be/FBG3-pwMFxU?t=1m22s)
and see it in Search results instantly, and Squarespace created a
[Google Search keywords report](https://support.squarespace.com/hc/en-us/articles/360001014647)
to help webmasters understand what prospective users search for.

During the event, we also presented the
[new Search Console](https://search.google.com/search-console) in the
Sandbox area for people to try and were happy to get a lot of positive feedback, from people being
excited about the
[AMP Status report](https://support.google.com/webmasters/answer/7450883)
to others exploring how to improve their content for Search.

## Hands-on codelabs, case studies and more

We presented the
[Structured Data Codelab](https://codelabs.developers.google.com/codelabs/structured-data/index.html?index=..%2F..%2Findex#0)
that walks you through adding and
[testing structured data](/search/docs/advanced/structured-data).
We were really happy to see that it ended up being one of the top 20 codelabs by completions at
I/O. If you want to learn more about the benefits of using Structured Data, check out our
[case studies](/search/case-studies).

![Hallway discussions at Google I/O](/static/search/blog/images/import/f30c5258e9540cc58e99add6cb232c61.png)

During the in-person office hours we saw a lot of interest around HTTPS,
[mobile-first indexing](/search/blog/2018/03/rolling-out-mobile-first-indexing), AMP,
and many other topics. The in-person Office Hours were a wonderful addition to our monthly
[Webmaster Office Hours hangout](/search/events/join-office-hours).
The questions and comments will help us adjust our documentation and tools by making them clearer
and easier to use for everyone.

## Highlights and key takeaways

We also repeated a few key points that web developers should have an eye on when building
websites, such as:

- Indexing and rendering don't happen at the same time. We may defer the rendering to a later
  point in time.
- Make sure the content you want in Search has metadata, correct HTTP statuses, and the intended
  canonical tag.
- Hash-based routing (URLs with `#`) should be deprecated in favour of the JavaScript
  History API in Single Page Apps.
- Links should have an `href` attribute pointing to a URL, so Googlebot can follow the links
  properly.

Make sure to
[watch this talk](https://www.youtube.com/watch?v=PFwUbgvpdaQ) for
more on indexing, dynamic rendering and troubleshooting your site. If you wanna learn more about
things to do as a CMS developer or theme author or Structured Data,
[watch this talk](https://www.youtube.com/watch?v=NO-sdBzb1Hc).

We were excited to meet some of you at I/O as well as the
[global I/O extended events](https://events.google.com/io/extended/)
and share the latest developments in Search. To stay in touch, join the
[Webmaster Forum](https://support.google.com/webmasters/community/)
or follow us on
[Twitter](https://twitter.com/googlesearchc),
[Google+](https://plus.google.com/+googlewebmasters), and
[YouTube](https://www.youtube.com/@GoogleSearchCentral).
