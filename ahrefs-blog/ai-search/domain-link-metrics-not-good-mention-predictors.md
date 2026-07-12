---
title: "Domain-Level Link Metrics May Not Be Good Predictors of AI Search Mentions"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "domain-link-metrics-not-good-mention-predictors"
url: "https://ahrefs.com/blog/domain-link-metrics-not-good-mention-predictors/"
canonical: "https://ahrefs.com/blog/domain-link-metrics-not-good-mention-predictors/"
author: "Patrick Stox"
published: "2025-06-25T10:00:00+00:00"
updated: "2025-08-26T14:51:18+00:00"
categories:
  - "AI Search"
  - "Data & Studies"
freshness_reasons:
  - "ai_search_topic"
  - "news_or_research"
fetched_at: "2026-06-12T11:27:39+00:00"
status_code: 200
html_hash: "ef7cb89ebf06a8e7f6dd7fca72fd8eeb29e26de8b9ec4915a291027f93cbf6b2"
clean_word_count: 621
clean_char_count: 3818
---
# Domain-Level Link Metrics May Not Be Good Predictors of AI Search Mentions

Going into this study, I suspected that domain-level link metrics would not be a good predictor for mentions. I was expecting Google AI Overviews to show more of a correlation since they may use some of the traditional search signals, whereas the other systems may not. For traditional search, usually the page-level metrics are more predictive of rankings than domain-level ones.

I looked at the top 50 websites mentioned in [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) for Google AI Overviews, ChatGPT, and Perplexity. This is across ~76.7M AI Overviews, 957k ChatGPT prompts, and 953.5k Perplexity prompts for the month of June 2025.

I compared the website mentions to their Ahrefs Rank (AR) in Ahrefs. Ahrefs Rank (AR) ranks all the websites in our database in order, by the size and quality of their followed referring domains.

Sidenote.

Brand Radar isn’t just another LLM visibility monitor, we track a large amount of queries across all of these systems and you can query for any product, service, or brand and compare vs competitors. It’s more like Site Explorer than it is Rank Tracker. Plus we have the web visibility index so that you can see how you’re talked about online and the search demand index to see how popular you are in searches.

Here’s what Brand Radar looks like.

![Ahrefs Brand Radar](https://ahrefs.com/blog/wp-content/uploads/2025/06/ahrefs-brand-radar.jpeg)

Let’s dig in.

## Key takeaways

**Perplexity shows a moderate correlation** between the mentions of its most-cited domains and their Ahrefs Rank, **Google AI Overviews a very weak correlation**, and **ChatGPT no correlation.** I was expecting Google to have a stronger relationship than Perplexity, so the results surprised me.

This correlation would likely change with a larger dataset outside of just the top 50. The top 50 are all extremely well-linked and cited websites, but that probably doesn’t matter as much as page-level signals.

## The nerdy data

I’ll give the usual correlation does not equal causation disclaimer.

Here are the [Spearman rank correlations](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) for mention share vs. Ahrefs Rank across the top 50 domains in each system:

| AI Assistant | Spearman Rho | P-Value | Correlation |
| --- | --- | --- | --- |
| Google AI Overviews | -0.12 | 0.47 | Very weak |
| ChatGPT | 0.01 | 0.95 | No relationship |
| Perplexity | -0.34 | 0.095 | Weak |

## Google AI Overviews

Google AI Overviews over-index on UGC sites like YouTube, Reddit, and Quora, as well as encyclopedic content like Wikipedia. We’ve seen this in a few other studies already.

These sites get extra weight in mentions than their link profile predicts.

Google AI Overviews underweights on social media sites like LinkedIn, Instagram, and Facebook. Another pattern we’ve seen in other studies.

## **ChatGPT**

We also see a similar story with ChatGPT, where they are overweight on things like Wikipedia and news sites like Reuters, exactly like we saw before.

## Perplexity

Perplexity also shows the same biases we’ve seen. YouTube and Wikipedia are overweight, social media sites are underweight.

## Final thoughts

I’m not sure this is enough of a sample size to get a good measure. We actually saw [higher correlations in Google AI Overviews compared to DR](https://ahrefs.com/blog/ai-overview-brand-correlation/) when we studied 75k sites than we saw in correlations to normal Google rankings across 1 million keywords, 0.326 vs 0.131.

We’ll run a bigger study beyond the top 50, as well as look at some more page level metrics for more insights.

If you have questions, ask me on [LinkedIn](https://www.linkedin.com/in/patrickstox/) or [X](https://x.com/patrickstox).
