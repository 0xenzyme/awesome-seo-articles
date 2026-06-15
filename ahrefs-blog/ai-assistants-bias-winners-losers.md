---
title: "AI Assistant Bias Revealed: Here’s Who Gets Favored & Who Gets Shunned in the New Era"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "ai-assistants-bias-winners-losers"
url: "https://ahrefs.com/blog/ai-assistants-bias-winners-losers/"
canonical: "https://ahrefs.com/blog/ai-assistants-bias-winners-losers/"
author: "Patrick Stox"
published: "2025-06-19T10:00:00+00:00"
updated: "2026-05-28T12:37:00+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "news_or_research"
fetched_at: "2026-06-12T11:12:30+00:00"
status_code: 200
html_hash: "7c0949b69f0ae81a01dad5b8cb5122e4f1a10477d3f55c5a4e05a1050cf91b3a"
clean_word_count: 926
clean_char_count: 5768
---
# AI Assistant Bias Revealed: Here’s Who Gets Favored & Who Gets Shunned in the New Era

AI assistants are rewriting the rules when it comes to visibility on the web. The websites they mention are chosen based on different criteria than traditional search rankings.

Instead of just looking at which websites are mentioned the most, I wanted to understand whether those mentions actually match the popularity of the topics being discussed.

I compared each domain’s *Mention Share* (how often it shows up) to its *Impression Share* / *Potential Reach* (how often you’d expect it to show up based on search volume for those topics).

This comparison helps to uncover biases and show whether a particular system is leaning into certain sources more or less than expected based on the popularity of the topics the website covers.

I looked at the top 50 websites cited in [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) for Google AI Overviews, ChatGPT, and Perplexity.

This is across ~76.7M AI Overviews, 957k ChatGPT prompts, and 953.5k Perplexity prompts for the month of June 2025.

## Key takeaways

- **Google AI Overviews** lean heavily on UGC sites like Reddit, Quora, and YouTube. Wikipedia and health sites like Mayo Clinic and Cleveland Clinic are under-represented. YouTube is owned by Google, so they may prefer it. Google has a licensing deal with Reddit and has given them a lot of visibility in Google Search already.
- **ChatGPT** under-represents Wikipedia and News like Reuters.
- **Perplexity** is fairly neutral overall, but under-represents Wikipedia.
- **Wikipedia** was slightly under-represented in Perplexity, but under-represented quite a bit in Google and ChatGPT. Despite Wikipedia’s popularity in AI assistants, it looks like these systems are fairly biased against them.

Here’s the nerdy data.

## Google AI Overviews

Google seems to be relying on more user-generated content (UGC) sites than they are trustworthy sites, those considered to have more [EEAT](https://ahrefs.com/blog/eeat-seo/).

Here are a couple definitions to keep in mind:

- **Mention Share** is how frequently a domain is mentioned across all AI responses.

```
Mention Share = (Number of responses that mention the domain ÷ Total number of AI responses analyzed) × 100
```

- **Impression Share** weights mentions by Google search volume to estimate how much potential visibility a site gets across high- vs. low-demand topics.

```
Impression Share = (Sum of search volume for queries where the domain is mentioned ÷ Total search volume of all AI-analyzed queries) × 100
```

The difference between Mention Share and Impression Share tells you whether a website is being cited more in high-visibility queries or low-visibility ones. It reveals systemic biases in how AI assistants show different websites.

![mentions vs impression share for Google AI Overviews](https://ahrefs.com/blog/wp-content/uploads/2025/06/image-1.png)

**Over-relying on:**

- **Reddit** (7.4% vs 4.0%): mentioned 3.4% more than its expected visibility
- **Quora** (3.6% vs 1.4%): mentioned 2.2% more than its expected visibility
- **YouTube** (9.8% vs 7.8%): mentioned 2.0% more than its expected visibility

**Under-utilizing:**

- **Wikipedia** (8.4% vs 11.6%): mentioned 3.2% less than its expected visibility
- **Mayo Clinic** (2.9% vs 4.5%): mentioned 1.6% less than its expected visibility
- **Cleveland Clinic** (2.9% vs 4.5%): mentioned 1.6% less than its expected visibility

You can use [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) to see when these biases may have been introduced.

For example, here are the Mentions for the top 5 sites in AI Overviews over time, but weighted to the market. It looks like Google is moving away from Wikipedia, moving towards Reddit heavily in December and March, towards Google Translate in March, towards Quora in December and March, but away from Quora in April, and may have moved away from YouTube back in October, but brought it back in April.

This is how you see algorithm updates and trends in the new era.

## ChatGPT

ChatGPT was the system that I thought would have the most radical differences. Overall, they seem to under-represent Wikipedia and news sites.

One more definition:

- **Potential Reach Share (%)** estimates how much exposure a domain *could* be getting in an AI assistant responses. There is no reliable search volume for AI assistants, so this weights in search volume from Google searches and acts as a proxy based on historical web popularity.

```
Potential Reach Share = (Sum of search volume for prompts where the domain is mentioned ÷ Total search volume for all prompts analyzed) × 100
```

**Over-relying on:**

- **Google.com** (2.3% vs 1.7%): 0.6% over
- **Apple.com** (4.0% vs 3.8%): 0.2% over

**Under-utilizing:**

- **Wikipedia** (16.3% vs 19.3%): 3.0% under
- **Reuters** (4.3% vs 6.4%): 2.1% under

## Perplexity

I was expecting Perplexity to bias against Wikipedia more. The CEO has made some comments about Wikipedia’s bias and even offered to support anyone who wanted to build an alternative. I couldn’t have been more wrong.

Perplexity appears to be the most balanced, showing mention patterns that roughly align with topic popularity on the traditional web.

**Over-relying on:**

- **YouTube** (16.1% vs 15.7%): 0.4% over
- **Apple.com** (3.5% vs 2.6%): 0.9% over

**Under-utilizing:**

- **Wikipedia** (12.5% vs 13.4%): 0.9% under
- **Tuasaude.com** (1.6% vs 2.5%): 0.9% under

### Final thoughts

Search is fragmenting. We’re so used to just optimizing for Google. Now we might need to look at optimizing for different systems with different biases.

If you have questions, ask me on [LinkedIn](https://www.linkedin.com/in/patrickstox/) or [X](https://x.com/patrickstox).
