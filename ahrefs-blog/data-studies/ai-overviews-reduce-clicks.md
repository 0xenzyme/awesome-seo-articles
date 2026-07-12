---
title: "AI Overviews Reduce Clicks by 34.5%"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "ai-overviews-reduce-clicks"
url: "https://ahrefs.com/blog/ai-overviews-reduce-clicks/"
canonical: "https://ahrefs.com/blog/ai-overviews-reduce-clicks/"
author: "Ryan Law"
published: "2025-04-17T11:08:32+00:00"
updated: "2026-06-05T23:02:48+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "ai_search_topic"
  - "news_or_research"
fetched_at: "2026-06-12T11:14:19+00:00"
status_code: 200
html_hash: "00ae8b13d3125166538b780fb815c09e20b23f7f868f92a1190085ee5f8e689b"
clean_word_count: 766
clean_char_count: 4814
---
# AI Overviews Reduce Clicks by 34.5%

Google says AI Overviews increase clicks. Cold, hard logic disagrees, and so does our research.

We analyzed 300,000 keywords and found that the presence of an AI Overview in the search results correlated with a **34.5% lower average clickthrough rate (CTR)** for the top-ranking page, compared to similar informational keywords without an AI Overview.

Thanks to our data scientist, [Xibeijia Guan](https://ahrefs.com/blog/author/xibeijia-guan/), for pulling the data for this analysis.

> “In fact, if you put content and links within AI Overviews, they get higher clickthrough rates than if you put it outside of AI Overviews.”
>
>
>
> Sundar Pichai, CEO, [Google](https://www.theverge.com/24158374/google-ceo-sundar-pichai-ai-search-gemini-future-of-the-internet-web-openai-decoder-interview)

Editor’s Note

We recently re-ran this study for 2026. [See the results here](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/).

## Methodology

We selected 300,000 keywords from Ahrefs [Keywords Explorer](https://ahrefs.com/keywords-explorer) database, consisting of 150,000 keywords with an AI Overview present and 150,000 keywords with informational intent and no AI Overview present.

Sidenote.

Our research found that [99.2% of keywords that trigger AI Overviews](https://ahrefs.com/blog/ai-overview-keywords/) are *informational* in intent, so we’ve focused on *informational* keywords for a better like-for-like comparison.

We used aggregated GSC data to get each keyword’s average desktop clickthrough rate (CTR) per month (sum of clicks/sum of impressions). We then compared the clickthrough rates for both samples for March 2024 (before the US rollout of AI overviews) and March 2025 (after).

See where AI Overviews appear for your rankings

You can use the **SERP features** filter to see exactly where AI Overviews are triggering for your keyword rankings. Head to Ahrefs’ [**Site Explorer**](https://ahrefs.com/site-explorer), navigate to the **Organic keywords** report, and select **AI Overview**from the SERP features filter.

![](https://ahrefs.com/blog/wp-content/uploads/2025/04/AIO-SERP-Features-filter.jpg)

## Findings

In March 2024, the average position one CTR for informational keywords was 0.056. In March 2025, this had dropped to 0.031:

In March 2024, the average position one CTR for AI Overview keywords was 0.073. In March 2025, this had dropped to 0.026:

Sidenote.

“AI Overview keywords” refer to keywords that triggered an AI Overview in March 2025. In March 2024, before the US rollout of AI Overviews, these keywords did not trigger an AI Overview.

We can use the drop in CTR for informational keywords to predict the CTR for our sample of AI Overview keywords, assuming AI Overviews had not rolled out. This forecasted CTR is **0.040** `(0.073*(0.031/0.056))`.

Calculating the difference between the forecasted and actual CTR for AI Overview keywords suggests that the presence of AI Overviews reduces the click-through rate for position 1 by **~34.5%** `((0.026-0.040)/0.040)`:

## Final thoughts

This isn’t surprising. I have seen anecdata suggesting that some websites have seen [clicks reduce by 20–40%](https://ahrefs.com/blog/seo-is-still-your-best-marketing-channel/) since the rollout of AI overviews.

It seems possible. AI Overviews function in a similar way to Featured Snippets, by trying to resolve the searcher’s query directly in the SERP—likely contributing to more zero-click searches. And although AI Overviews often contain citation links, there can be many of these links cited, making it less likely for any single link to earn the lion’s share of clicks.

It’s also telling that despite [Google’s optimistic claim](https://blog.google/products/search/generative-ai-google-search-may-2024/) that *“links included in AI Overviews get more clicks than if the page had appeared as a traditional web listing for that query”*, there is still no way to disambiguate AI Overview clicks and impressions from the rest of your Search Console data.

It seems that Google doesn’t want us to see the clickthrough rate for AI Overviews.

Assuming AI Overviews stay in this current form, this is also likely the *highest* the CTR will be. As the novelty wears off and the [law of shitty clickthroughs](https://andrewchen.com/the-law-of-shitty-clickthroughs/) kicks in, I would expect to see clicks reduce further.

Further reading

- [I Analyzed 300K Keywords. Here’s What I Learned About AI Overviews](https://ahrefs.com/blog/ai-overview-keywords/)
- [SEO Is the Worst It’s Ever Been (And It’s Still Your Best Marketing Channel)](https://ahrefs.com/blog/seo-is-still-your-best-marketing-channel/)
- [Google Is Looking Out for #1. It’s Time You Do, Too](https://ahrefs.com/blog/google-looking-out-for-number-one/)
