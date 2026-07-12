---
title: "Is ChatGPT Really Powered by Google? 118,931 Fan-Out Queries Analyzed"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "is-chatgpt-really-powered-by-google"
url: "https://ahrefs.com/blog/is-chatgpt-really-powered-by-google/"
canonical: "https://ahrefs.com/blog/is-chatgpt-really-powered-by-google/"
author: "Si Quan Ong"
published: "2025-08-20T10:23:41+00:00"
updated: "2025-11-20T18:14:22+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "ai_search_topic"
  - "news_or_research"
fetched_at: "2026-06-12T11:42:46+00:00"
status_code: 200
html_hash: "f706de7066a6c911d780a22d8b2f0de772094f9e057fc1f430cffc4a6bf144b6"
clean_word_count: 548
clean_char_count: 3415
---
# Is ChatGPT Really Powered by Google? 118,931 Fan-Out Queries Analyzed

Given OpenAI’s close relationship with Microsoft, many expect that ChatGPT’s retrieval-augmented generation (RAG) process would use Bing.

However, over the past months, [some](https://newsletter-alekseo-com.translate.goog/p/searchgpt-bing-google?_x_tr_sl=fr&_x_tr_tl=en&_x_tr_hl=en&_x_tr_hist=true&ck_subscriber_id=2055546680&utm_source=convertkit&utm_medium=email&utm_campaign=%F0%9F%94%A5%2BThe%2BUpdate%2Bis%2BGetting%2BWarmer%2B&%2BMore%2BSEO%2Bnews%2B-%2BJuly%2B13%2C%2B2025%2B-%2B18277692=) [SEOs](https://www.reddit.com/r/SEO/comments/1m47avn/chatgpt_plus_is_secretly_googlepowered_my_hidden/) [discovered](https://www.aleydasolis.com/en/ai-search/chatgpt-uses-google-serp-snippets-for-answers/) that ChatGPT may have secretly pivoted to using Google instead.

![Aleyda Solis experiment to see if ChatGPT uses Google](https://ahrefs.com/blog/wp-content/uploads/2025/08/aleyda-solis-experiment-to-see-if-chatgpt-uses-goo.jpg)

These were all one-off experiments. So, I wondered if it was possible for us to find out the ‘truth’ using data instead.

Here’s what we found.

## Methodology

I asked our data scientist [Xibeijia Guan](https://ahrefs.com/blog/author/xibeijia-guan/) for help with this. Here’s what she did:

- She pulled the actual search queries ChatGPT made (“fan-out queries”) and the URLs it returned from those searches. This data is from our [Ahrefs Brand Radar](https://ahrefs.com/brand-radar).
- She then ran those exact same search queries through Google to see what URLs Google would return
- She measured how often ChatGPT’s returned URLs appeared in Google’s top 10, top 20, and anywhere in Google’s search results.

On average, ChatGPT pulls 1.78 search queries per prompt, with 75% of prompts triggering exactly two searches.

## ChatGPT search results rarely match Google rankings

On average:

- Only **6.82%** of ChatGPT search results are in the top 10 of Google’s SERPs
- Only **9.85%** of ChatGPT search results are in the top 20 of Google’s SERPs
- Only **16.61%** of ChatGPT search results are in Google’s SERPs.

If ChatGPT were simply pulling from Google’s search results, you’d expect much higher overlap. Instead, **83.39%** of ChatGPT’s chosen results don’t appear in Google’s search results at all for the same fan-out queries.

My colleague Louise also studied 15,000 prompts and found that on average, [only 12% of links](https://ahrefs.com/blog/ai-search-overlap/) cited by ChatGPT, Gemini, and Copilot appear in Google’s top 10 results for the same prompt.

So, there’s no clear indication that ChatGPT is *solely* or *predominantly* using Google as their search engine.

ChatGPT likely uses a hybrid approach where they retrieve search results from various sources, e.g. Google SERPs, Bing SERPs, their own index, and third-party search APIs, and then combine all the URLs and apply their own re-ranking algorithm.

## Final thoughts

ChatGPT doesn’t appear to be “secretly Google-powered.” Instead, it seems to use a sophisticated multi-source approach.

This makes sense from a product perspective.

OpenAI likely wants to reduce dependence on any single search provider while optimizing for their specific use case: providing accurate, contextual answers rather than general web discovery.

Any questions or comments? Let me know on [LinkedIn](https://www.linkedin.com/in/si-quan-ong/).
