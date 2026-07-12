---
title: "Anonymized Queries Make Up Nearly Half of Google Search Console Traffic"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "gsc-anonymized-queries"
url: "https://ahrefs.com/blog/gsc-anonymized-queries/"
canonical: "https://ahrefs.com/blog/gsc-anonymized-queries/"
author: "Patrick Stox"
published: "2026-02-11T14:14:33+00:00"
updated: "2026-05-28T12:44:19+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "news_or_research"
fetched_at: "2026-06-12T11:35:10+00:00"
status_code: 200
html_hash: "77af26cd7e987432ccf7205ba0a9eb6e3d6b04fb9ee5b42b8e63bdc82a93000a"
clean_word_count: 780
clean_char_count: 4567
---
# Anonymized Queries Make Up Nearly Half of Google Search Console Traffic

In April 2025, anonymized queries made up 46.77% of website traffic. This is data from before AI Overviews were launched. Queries are longer now and I suspect that more queries are being anonymized.

This number is slightly higher than our [2022 study on anonymized queries](https://ahrefs.com/blog/gsc-hidden-terms-study/). However, that’s the average. Some websites in our research saw dramatically higher percentages of anonymized queries.

Read on to see how it might impact you.

## Anonymous queries explained

The problem is that I believe Google’s classification for anonymized queries is overly broad. Here’s [how Google defines anonymized queries](https://developers.google.com/search/blog/2022/10/performance-data-deep-dive):

> Some queries (called anonymized queries) are not included in Search Console data to protect the privacy of the user making the query.
>
> Anonymized queries are those that aren’t issued by more than a few dozen users over a two-to-three month period.

A few dozen users need to search for something over a two-to-three-month period or Google won’t tell you what was searched.

There was a similar definition used around Google’s obligations under the EU’s Digital Markets Act (DMA) where they are supposed to share data with competitors. For that, they classified anonymous queries as queries that haven’t been searched more than 30 times in the last 13 months by 30 separate signed-in users. [DuckDuckGo’s CEO said that omitted ~99% of longtail queries](https://spreadprivacy.com/investigate-google-dma/).

That methodology actually gives more data than the methodology used by Google Search Console to tell you what drove clicks to your own website. That means that more than 99% of longtail queries would be omitted by Google Search Console.

Tip

We (Ahrefs) actually built an [Anonymous Queries report](https://ahrefs.com/gsc-insights) to help close the gap and let you see some of these anonymized queries. We mash your GSC data with our data to show you terms where we saw your website ranking, but these searches weren’t reported in GSC.

![Anonymous Queries report inside Ahrefs](https://ahrefs.com/blog/wp-content/uploads/2026/02/anonymous-queries-report-inside-ahrefs.png)

It’s going to get worse. I had our amazing data scientist Xibeijia Guan pull data for April 2025, before the rollout of AI Overviews or AI Mode. 46.77% anonymous in April 2025 was only slightly worse than the 46.08% anonymous we saw in 2022.

That’s not the end of the story. Search behavior is changing in the era of AI search. People are now searching with longer queries.

In fact, Google removed the max word count on Google searches. In the past, Google would only use the first 32 words in your query. Now, the search only breaks when the max characters in the URL are reached, somewhere between 2,083 characters to several megabytes of data, depending on the browser.

Searches are getting longer, and Google anonymizes queries not searched by a few dozen users over a two-to-three-month period. You can see where this is going.

That anonymous query number is going to skyrocket. We’re going to have less data than ever on what people searched to come to our own websites.

We’ll soon be pulling the data to show how much more is being anonymized, but for now, enjoy the nerdy data from the study.

## The GSC data

We analyzed 22 billion clicks across 887,534 GSC properties. This is up from the 9 billion clicks we looked at across 146,741 properties in 2022.

Here’s how anonymous queries have trended:

- **46.08%** in 2022
- **45.02%** in April 2024
- **46.77%** in April 2025

Below is a histogram showing the breakdown of anonymized queries by the number of websites.

The mode, or most frequent percentage of anonymized queries for a site, falls between 45% and 80%. That means that many sites are missing more than the 46.77% average would have you believe.

If we look at the breakdown of sites by traffic, there’s an interesting phenomenon. Sites with average traffic actually have more data.

Sites with lower traffic and sites with higher traffic seem to be missing more data. These sites likely have more long-tail or niche/proprietary terms that are more likely to be anonymized than other sites.

In case you’re seeing box plots for the first time, here’s how you should read them:

## Final thoughts

As I said, I expect more data to fall into this anonymized query bucket with AIOs and AI Mode. We’ll have the data for you soon. Stay tuned.
