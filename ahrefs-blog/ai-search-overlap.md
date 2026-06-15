---
title: "Only 12% of AI Cited URLs Rank in Google's Top 10 for the Original Prompt"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "ai-search-overlap"
url: "https://ahrefs.com/blog/ai-search-overlap/"
canonical: "https://ahrefs.com/blog/ai-search-overlap/"
author: "Louise Linehan"
published: "2025-08-11T10:00:00+00:00"
updated: "2026-05-31T14:32:29+00:00"
categories:
  - "AI Search"
  - "Data & Studies"
freshness_reasons:
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:14:35+00:00"
status_code: 200
html_hash: "0d3c0e4c5231d3d0bc9c1611405428c02e8e4e6493c77cf703a6c98d5fb653eb"
clean_word_count: 1657
clean_char_count: 10163
---
# Only 12% of AI Cited URLs Rank in Google’s Top 10 for the Original Prompt

In a dataset of 15,000 prompts, we found that—on average—only 12% of links cited by ChatGPT, Gemini, and Copilot appear in Google’s top 10 results for the same prompt.

Perplexity is the outlier: nearly 1 in 3 of its citations point to pages that rank in the top 10 for the target query.

We analyzed four AI assistants—ChatGPT, Gemini, Copilot, and Perplexity—to measure how often the URLs they cite or reference overlap with what Google or Bing ranks for the same query.

On average, the citation overlap between AI assistants and Google and Bing’s top 10 stands at 11%.

`((Google AI overlap total + Bing AI overlap total) / 10) = 10.96%`

![Ahrefs research using Brand Radar: Only 11% of AI citations overlap with Google’s and Bing’s top 10](https://ahrefs.com/blog/wp-content/uploads/2025/08/3-ai-search-overlap-1.png)

Further down, we look at this broken down by individual search engine.

## Methodology

Using data from [Ahrefs Brand Radar](https://ahrefs.com/brand-radar), our data scientist, [Xibeijia Guan](https://sg.linkedin.com/in/xibeijia-guan), searched 15,000 long-tail queries in Google and Bing, then asked those same questions to AI assistants.

Example queries included:

- “How much does it cost to install a security camera?”
- “How to get enough protein when you can’t eat dairy?”
- “What is the cheapest full comprehensive insurance?”
- “¿Cuál es el mejor suplemento para la recuperación muscular?”

Xibeijia then extracted every visible citation returned for each question across both search and AI indices.

In the search dataset, she recorded the ranking positions of the cited URLs—then categorized them based on whether they appeared in the top 10, or top 100 results.

The AI assistants tested include ChatGPT (both in-text citations and bottom-of-response references), Gemini, Copilot, and Perplexity.

## 12% of AI citations are present in Google’s top 10

According to research carried out by our data scientist, [Xibeijia Guan](https://sg.linkedin.com/in/xibeijia-guan), just 12% of citations in AI assistants also rank in Google’s top 10, on average.

`((28.6 + 8 + 6.1 + 8.6 + 8.2) / 5) = 11.9%`

80% of those citations don’t rank anywhere in Google for the original query—80% is essentially the average of all the “red” columns in the chart above.

The overlap between AI and search citations is smaller than we anticipated, but we have a couple of theories as to why that might be.

We’ll get into them a little later on.

### Perplexity aligns closest to Google

Perplexity is an AI assistant that was literally [built to cite](https://www.perplexity.ai/hub/blog/getting-started-with-perplexity)—its goal is to support nearly every statement with a source.

> *Perplexity is the world’s first answer engine. It searches the internet in real time to deliver fast, clear answers to any question—with sources and citations included…Every answer comes with clickable citations, making it easy to verify the information and dig deeper if you want.*
> [Perplexity Team](https://www.perplexity.ai/hub/blog/getting-started-with-perplexity), Oct 2024

ChatGPT and Gemini, on the other hand, don’t always link out.

Their citation process is very much query-dependent, and their internal systems trigger searches based on different criteria.

ChatGPT, for example, seems to use something called the [sonic classifier](https://www.linkedin.com/posts/mihir23192_the-seo-community-will-soon-start-discussing-activity-7353609394435117057-4sqT/?utm_source=share&utm_medium=member_desktop&rcm=ACoAACFVHncB5jqhKHk56xrmoTazEwPvJ01c_Ig)—if the prompt “probability” exceeds a certain threshold (i.e. if the response is less easy to “predict” based on training data), then ChatGPT will perform a web search.

Perplexity consistently favors content that ranks well in Google, with 28.6% of its cited URLs landing in the top 10.

For the other AI assistants, that number hovers around 8%—and more than 80% of their citations come from pages that don’t rank at all for the target query.

Since Perplexity focuses heavily on citations, it seems logical that its results would align closely with Google’s.

But, unlike Gemini and other AI assistants, Perplexity doesn’t draw on Google *or* Bing’s index. In fact, it has its own search index, based on its crawler: [perplexitybot](https://docs.perplexity.ai/guides/bots).

AI assistants—even those that draw on Google and Bing—appear to query search indexes in a fundamentally different way. This explains why we’re seeing minimal crossover.

## 10% of AI citations overlap with Bing’s top 10 results

When measuring against Bing results, overlap remains low in the top 10—hitting roughly 10% on average.

`((16.6 + 14 + 8.1 + 8.1 + 3.3) / 5) = 10.02%`

Copilot rises to the top of the list, which is to be expected since it is a Microsoft-owned product that [draws on Bing search results](https://www.zdnet.com/article/what-is-copilot-formerly-bing-chat-heres-everything-you-need-to-know/) when generating its responses.

Perplexity still remains one of the most SEO-aligned AI assistants, while ChatGPT and Gemini show the least overlap.

## 76% of AI Overview citations pull from top 10 pages

This study builds on our earlier research into how often high-ranking pages get cited in Google’s AI Overviews.

Further reading:

- [76% of AI Overview Citations Pull From Top 10 Pages](https://ahrefs.com/blog/search-rankings-ai-citations/)
- [Does Ranking Higher on Google Mean You’ll Get Cited in AI Overviews?](https://ahrefs.com/blog/does-ranking-higher-on-google-mean-youll-get-cited-in-ai-overviews/)

In those studies, we found a moderate positive correlation between Google rankings and citations in AI Overviews, with 76% of cited URLs coming from pages in the top 10.

Based on the data, it seems as if AI Overviews function like an extension of traditional search—surfacing results that mostly reflect the SERP.

In other words, AI Overviews follow the SERPs—AI assistants don’t.

Even the assistants built *by* Google aren’t closely aligned with Google’s SERPs.

There are clearly other factors influencing what gets cited, beyond just search rankings.

## Why AI citations might differ from Google or Bing results

Our data shows that the URLs cited by AI assistants rarely match what Google and Bing ranks.

In most cases, they don’t appear in the top 10 for the target prompt—often, they aren’t in the top 100 at all.

This is because AI assistants don’t rank results in the same way search engines do.

Instead of processing just one user query when deciding what to cite, they tend to retrieve pages based on multiple variations of that query—a technique known as “**query fan-out**.”

These variations then get merged using methods like [Reciprocal Rank Fusion](https://metehan.ai/blog/chatgpt-is-using-reciprocal-rank-fusion-rrf/?s=09) (**RRF**), where the pages that appear consistently are favored more.

For example, a page that ranks around #6 for “how to descale a coffee machine,” “cleaning a Nespresso machine,” and “remove limescale from coffee maker” might be cited over one that ranks #1 for only one of those.

In fact, it’s possible that AI assistants may never search for the **actual** prompt that the user inputs—instead it just acts as a catalyst for other fan-out queries.

This is why eventual citations won’t always rank for the original prompt.

Personalization can also play a role: the exact same search query run through AI can lead to wholly different citations, due to factors like the user’s prompt or conversation history.

All of this may explain why AI citations don’t always mirror the SERPs.

Tip

You can optimize for multiple, long-tail query variations using Parent Topics in [Ahrefs Keyword Explorer](https://ahrefs.com/keywords-explorer).

Just search a keyword, head to the Matching Terms or Related Terms report, and check out the Parent Topics on the left, or hit the Clusters by Parent Topic tab.

Then hit the Questions tab for long-tail queries to target in your content…

And to see how much ownership you have over existing long-tail query permutations, add a Target filter for your domain.

## Does ChatGPT draw on Bing or Google?

Recent tests by [Aleksis Rylko](https://newsletter-alekseo-com.translate.goog/p/searchgpt-bing-google?_x_tr_sl=fr&_x_tr_tl=en&_x_tr_hist=true) suggests that SearchGPT citations closely resemble Google citations.

Rylko believes ChatGPT may now quietly pull from Google’s search index.

[Aleyda Solís corroborated this](https://www.searchenginejournal.com/chatgpt-appears-to-use-google-search-as-a-fallback/552089/#:~:text=Aleyda%20Sol%C3%ADs%20conducted%20an%20experiment,not%20yet%20indexed%20on%20Bing.)—she discovered that ChatGPT uses Google as a fallback when Bing pages are inaccessible.

These findings came as a surprise to many, because ChatGPT’s built-in provider is Bing.

From our own dataset, we aren’t seeing much differentiation in how ChatGPT surfaces both Google and Bing results.

|  | Google (top 10) | Bing (top 10) | Google (top 100) | Bing (top 100) |
| --- | --- | --- | --- | --- |
| ChatGPT (in-text citations) | 8.00% | 8.10% | 8.80% | 5.00% |
| ChatGPT (references) | 6.10% | 8.10% | 9.20% | 5.20% |

That said, we collected this data in early July, so results may have changed—especially given that OpenAI is planning to release its [AI-first web browser](https://www.reuters.com/business/media-telecom/openai-release-web-browser-challenge-google-chrome-2025-07-09/), and potentially even build its own search index, going by the recent memo [leak](https://drive.google.com/file/d/1WfKxSJIJLnYfxEpyjfwtsyBUNI8XazY0/view).

We’ll be doing further research to study any citation shifts.

## Wrapping up

From our research, it seems that ranking well does help, but not necessarily for the queries you might assume you’d need to rank well for.

We’ll keep studying citation overlap in traditional search and AI to see if anything changes.

In the meantime, optimizing for query variations, building topic clusters, and “owning the entity” seems to be the way to go if you are hoping to get cited in AI.
