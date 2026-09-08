---
title: "AI adjusted volume: How Ahrefs approaches the challenge of estimating AI Search demand"
source: "ahrefs-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "how-ahrefs-estimates-ai-search-demand"
url: "https://ahrefs.com/blog/how-ahrefs-estimates-ai-search-demand/"
canonical: "https://ahrefs.com/blog/how-ahrefs-estimates-ai-search-demand/"
author: "Constance Tan"
published: "2026-08-17T11:27:47+00:00"
updated: "2026-09-01T12:56:50+00:00"
categories:
  - "Product Blog"
freshness_reasons: []
fetched_at: "2026-09-08T09:16:09.423790+00:00"
status_code: 200
html_hash: "349a2798868c75ddc46d6f1d578c584c77e556fecad8a3230150aedd1de6ef4b"
clean_word_count: 1177
clean_char_count: 7315
---
# AI adjusted volume: How Ahrefs approaches the challenge of estimating AI Search demand

This article covers Ahrefs’ current approach to estimating AI search demand, why we chosen to go with this approach, and the problems of existing methods. By the end, you'll also know how to use these numbers on our platform without being misled by them.

Unlike keyword search volume in Google search, there's no significant, reliable source of data about how people prompt AI for answers, across many popular AI platforms. This makes it challenging to determine what people are prompting into AI, and how often they are doing so. Every major AI visibility tool provider estimates this differently, and each has their advantages and disadvantages.

First, let's talk about how we estimate AI Search demand.

## How Ahrefs estimates AI Search demand

Ahrefs uses what we call "AI adjusted volume"—a platform-specific estimate derived from traditional Google search volume.

The estimation method works like this: For each prompt, we identify the parent keyword with the highest search volume in Google. We then apply a platform-specific ratio to that parent keyword search volume.

The ratios themselves are derived from Ahrefs' aggregated website traffic data coming from different AI platforms relative to organic traffic from Google.

And so for the same prompt you'll see different volumes in proportion to the overall usage of each AI platform:

The full table of each AI platform's ratios can be found in this [article](https://help.ahrefs.com/en/articles/16755865-what-is-ai-adjusted-volume-and-how-is-it-calculated).

Since this metric is relatively new, we've temporarily added an option in Brand Radar to switch back to plain Google search volume for comparison. **That option will be available until August 31, 2026, after which reports will use AI adjusted volume only**.

### The problem with using real prompt data

What people prompt in AI is significantly more diverse than what's typed into a search bar. And this is simply due to the way people use AI in general:

- **Prompts are long-form:** AI is used in many more ways than just retrieving information and websites. AI is used to plan trips, create blogs, write code, generate images, execute jobs. As a result, real AI prompt data are mostly complex sentences and instructions that vary wildly, even for the same request or topic.
- **Personalization:** AI personalizes responses based on what they've already conversed with the user. And many prompts are made in context of an existing, ongoing conversation.
- **AI is used in many forms:** Unlike Search where vast majority of people make their search queries through a browser, people can choose to use AI through a browser, desktop app, API, through third party AI platforms, messenger chatbots, etc. Most of these methods have no way for a third party tool to capture real user prompts.

All of this leads to more challenging, noisier data. Some platforms have attempted to extrapolate AI search demand using this data on its own, often referring to this as "prompt volumes". And through our research, we find that their AI prompt volumes can be significantly over-estimated.

### Why vastly over-estimated prompt volumes could be a problem

If you're trying to build a following for your brand, keyword search volume is one of the factors that help you estimate the market size or relative popularity for any given topic.

If you're using over-estimated prompt volumes, you could be spending your marketing efforts to prioritize covering topics that actually have a much smaller audience in reality. This can lead to misaligned expectations for return on investment from growing your brand in AI platforms.

## Why no one has accurate prompt volume data

With the exception of Microsoft Copilot, no major AI platform (such as ChatGPT, Perplexity, Gemini, Claude, etc.) shares their query data with anyone. None of them publish what users are actually asking AI, or how often.

To compensate with this, most other AEO tools choose one of the following:

- Extrapolate from a much smaller set of clickstream data from opt-in browser panels.
- Generate prompts based on algorithmically created variations of seed keywords—and assign them estimated volumes without any direct measurement at all.
- Like Ahrefs, derive estimates from traditional search volume estimations.
- Avoid providing estimates entirely

### Why does Ahrefs anchor to Google search volume?

Because Google volume is the most reliable proxy we have for understanding demand in general. Your audience may interact differently with AI compared to search, but their underlying interests aren't suddenly different. So while our estimates are not derived from user query data, they can be used directionally to understand what's more.

For example, if "best project management software" has a known Google search volume, the derived People Also Ask question—"what's the best project management software?"—likely reflects similar underlying demand.

For now, we find organic data derivations to be a more reliable proxy in measuring demand. Meanwhile we continue to investigate how to use real user prompts data to effectively aid volume estimations, identify new topics to monitor, and other things that could be helpful in measuring AI demand.

### Why is traditional search volume so much easier to estimate versus AI search demand?

Some people push back on this by pointing out that Google doesn't share exact query volumes either—Google Search Console and Keywords Explorer both deal in estimates. That's fair. But the difference is scale and infrastructure:

- Google still owns over 90% of the search market share. With AI, this is significantly less concentrated, across many more providers.
- Google shares an enormous amount of data about how people search through tools like Google Keyword Planner, Google Search Console, Google Trends, etc. So even though these are just estimates, you get good topical, geographical coverage of what gets searched by real users.
- Almost all search is made through the browser, so the representative query datasets that Opt-in panels and clickstream can collect is much more reliable.

## What AI adjusted volume is (and isn't useful for)

AI adjusted volume is helpful for:

- Benchmarking brand visibility and AI Share of Voice (SOV) against competitors
- Identifying which topics are more top-of-mind for your audience
- Comparing which AI Platforms can drive more brand impressions for your niche
- Determining which cited pages get more eyeballs in relevant answers
- Prioritizing topics and platforms that can increase traffic from AI sources

AI adjusted volume is not helpful for:

- Estimating AI search-only addressable market size
- Measuring how many real people saw your brand mentioned in a specific AI response

## Final thoughts

Because people prompt AI differently compared to search engines (they type in multi-sentence paragraphs spanning multiple topics + follow-up questions), using AI prompt clickstream data alone to estimate "prompt volume" might lead to overinflated results due to summing up the volume of each topic found in a prompt.

By anchoring to Google keyword search volumes instead, we view AI adjusted prompt volumes as a more reliable method to identifying the parent topic of any prompt in our database, and its relevant AI answer demand.
