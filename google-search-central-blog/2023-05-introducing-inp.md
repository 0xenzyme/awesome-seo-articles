---
title: "Introducing INP to Core Web Vitals"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2023-05-introducing-inp"
url: "https://developers.google.com/search/blog/2023/05/introducing-inp"
canonical: "https://developers.google.com/search/blog/2023/05/introducing-inp"
author: "Martin Splitt"
published: "2023-05-10T00:00:00+00:00"
updated: "2023-05-10T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
fetched_at: "2026-06-14T13:42:01+00:00"
status_code: 200
html_hash: "1e92e82e84cab30b0a9d102477b9615d038a6a1ff545dbbf3deb31503ab62e70"
clean_word_count: 586
clean_char_count: 3611
---
# Introducing INP to Core Web Vitals

In early 2020, Google's Chrome Team introduced the [Core Web Vitals](https://web.dev/articles/vitals) to provide a suite of quality signals for web pages.
Today, the Google Chrome team [announced](https://web.dev/blog/inp-cwv) an upcoming change in the metrics for the Core Web Vitals
to better evaluate the quality of a webpage's user experience. In this article, we'll explore this change
and what it means for Google Search and site owners.

## A better responsiveness metric

![The INP metric transitioned from being an experimental metric in May 2022 to the announcement today and will become a stable metric as part of the Core Web Vitals in May 2024.](/static/search/blog/images/introducing-inp/inp-timeline.png)

One of the Core Web Vitals metrics, [First Input Delay (FID)](https://web.dev/articles/fid), measures responsiveness, but there are
[known limitations of FID](https://web.dev/blog/better-responsiveness-metric). This led the Chrome team to explore and seek feedback on a (then) [experimental metric](https://web.dev/blog/responsiveness) that addresses these limitations more effectively.
In 2022, they announced [Interaction to Next Paint (INP)](https://web.dev/articles/inp) as that new metric and started working with the community to test its efficacy.

After another year of testing and gathering feedback from the community,
the Chrome team decided to promote INP as the new Core Web Vitals metric for responsiveness,
effective March 2024, replacing FID. The [Chrome team's blog post](https://web.dev/blog/inp-cwv) explains this change and the reasoning behind the new metric in more detail.

## What this means for Google Search Console

The new metric, INP, will replace FID as part of the Core Web Vitals in March 2024.
To help site owners and developers to take the necessary steps and evaluate their pages for the new metric,
Search Console will include INP in the Core Web Vitals report later this year.
When INP replaces FID in March 2024, the Search Console report will stop showing FID metrics and
use INP as the new metric for responsiveness.

## What this means for site owners

If you have been following our guidance to improve Core Web Vitals, you will have considered the responsiveness of your pages already.
The improvements made for FID are a good foundation to improve INP and the responsiveness of your pages.

We highly recommend site owners achieve good Core Web Vitals for success with Search and to ensure a great user experience generally.
However, great page experience involves more than Core Web Vitals. Good stats within the [Core Web Vitals report](https://support.google.com/webmasters/answer/9205520) in Search Console
or third-party Core Web Vitals reports don't guarantee good rankings.

To learn more about how Core Web Vitals fits into a holistic approach to page experience,
see our guidance on [understanding and thinking about page experience in Google Search results](/search/docs/appearance/page-experience).

You can find more information about the new metric in the [Chrome team's blog post](https://web.dev/blog/inp-cwv) and guidance
on how to optimize your pages with regards to INP in [this guide on optimizing INP](https://web.dev/articles/optimize-inp).

---

## Updates

- **Update on January 31, 2024**:
  [Interaction to Next Paint (INP) will replace FID](https://web.dev/blog/inp-cwv-march-12)
  as a part of Core Web Vitals on March 12, 2024.
- **Update on March 12, 2024**:
  [Interaction to Next Paint (INP) has replaced FID](https://web.dev/blog/inp-cwv-launch) as a part of Core Web Vitals.
