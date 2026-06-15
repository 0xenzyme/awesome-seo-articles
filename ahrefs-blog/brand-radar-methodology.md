---
title: "Ahrefs Brand Radar Methodology: How we collect and model AI visibility data"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "low"
slug: "brand-radar-methodology"
url: "https://ahrefs.com/blog/brand-radar-methodology/"
canonical: "https://ahrefs.com/blog/brand-radar-methodology/"
author: "Rebekah Bek"
published: "2025-10-29T07:13:15+00:00"
updated: "2026-04-27T19:37:02+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "product_or_tool_content"
fetched_at: "2026-06-12T11:20:01+00:00"
status_code: 200
html_hash: "3e2a0177e3e1020688dbd8037ba0bb07acd07be6f8b58a4aedf7bd0cb398f829"
clean_word_count: 992
clean_char_count: 6737
---
# Ahrefs Brand Radar Methodology: How we collect and model AI visibility data

Brand Radar lets you monitor and explore how visible brands are across AI and search. In this post, we break down how data is collected, modeled, and kept current.

## Short version: The quick overview

> **Ahrefs Brand Radar = Real Demand + Semantic Coverage**

Most AI visibility tools force a choice between behavioral relevance (what users actually ask) or semantic completeness (logical topic expansion).

Ahrefs Brand Radar gives you both. You capture what users actually ask (real search demand) AND cover what the topic structurally requires (semantic completeness).

> **Breadth + Depth = Maximum AI Surface Area.**

Here’s how it works in practice: we collect keywords and SERPs from Ahrefs’ database with over 100 billion keywords.

To model how people naturally ask questions online, we expand queries using two different systems: Google’s People Also Ask (PAA) and semantic fanout.

Then run millions of these questions across AI platforms like ChatGPT, Perplexity, Gemini, Copilot, and Google’s AI Overviews (+ AI Mode) and store their responses, so you can search through the text and links to see where your brand name (or any term) appears.

- Question sets are updated and tested in chatbots monthly, using a 90-day reporting window.
- Metrics like AI Share of Voice (SOV) and Estimated Impressions model how visible a brand is across popular topics, based on real search interest. They show potential visibility, not actual audience reach.

## Extended version

Brand Radar helps companies understand how their brand shows up across AI and search.

It calculates AI Share of Voice (SOV) based on how often brands are mentioned or cited in responses from ChatGPT, Perplexity, Gemini, Microsoft Copilot, and Google’s AI Overviews and AI Mode.

### **1. Data collection**

Brand Radar models real-world user behavior, rather than fabricating prompts.

 Queries are collected from Google’s “People Also Ask” corpus and Ahrefs’ 110 billion keyword database ([28.7 billion keywords tracked with positive search volume](https://ahrefs.com/big-data)), then expanded into related sub-questions using two different systems: PAA and Fanout. They overlap sometimes, but they serve different purposes:

- **PAA (People Also Ask)**: PAA is based on real keywords searched by real people. It reflects how users refine their queries and what follow-up questions they actually click on in Google. So it’s optimized for behavioral relevance and engagement. It surfaces questions that users are genuinely curious about and frequently explore (read: real search demand).
- **Fanout**: Fanout is based on semantic relationships. It expands a query by analyzing meaning and topic structure, aiming to improve information retrieval and ensure broader topic coverage. Its goal is logical completeness rather than behavioral popularity.

For example, PAA may include questions that are popular but not directly helpful for answering the original question (e.g., for “what is the first sign of kidney problems,” PAA might suggest: “What foods help repair kidneys and liver?” or “What not to drink if you have kidney problems?”).

Fanout, on the other hand, may include semantically important sub-questions that structurally help answer the core query but aren’t frequently searched by users.

![ChatGPT fanout queries in Ahrefs Brand Radar](https://ahrefs.com/blog/wp-content/uploads/2025/10/2026-02-26_16-35-44-1.png)

ChatGPT fanout queries in Ahrefs Brand Radar

By combining them, **Ahrefs Brand Radar gives you the full picture of your AI visibility funnel**.

Each query is executed in supported AI interfaces. We store the raw responses, and users can then search this corpus to surface citations (linked URLs) and mentions (string matches) for any term.

Ahrefs AI Visibility Index

**Monthly query volume (approx.):**ChatGPT – 13.3 million
 Perplexity – 13.3 million
 Gemini – 12.4 million
 Copilot – 13.3 million
 AI Overviews – 143 million
 AI Mode – 41 million

All prompts run through the free, publicly available web interfaces of ChatGPT, Gemini, Perplexity, Copilot, and other supported platforms to reflect typical user experiences.

Locale parameterization mirrors the ratio of queries by country and language in our keyword database, allowing proportional representation across markets.

### **2. Data modeling**

Because AI prompts are effectively infinite, Brand Radar focuses on high-demand, recurring topics that mirror search interest. Metrics are directional indicators, not exact traffic counts – best understood as modeled visibility signals, and not performance metrics.

- **Estimated Impressions** weight mentions by Google search volume to model potential exposure.

**Update cadence varies by platform:**

- ChatGPT, Perplexity, Gemini, and Copilot are refreshed monthly, using a 90-day reporting window for stability and consistency. Each report includes all questions still valid within the 90 days before the selected date.
- Google AI Overviews and AI Mode update continuously, aligning with keyword database refresh cycles.
- Aggregated “All platforms” reporting combines data from both groups.

### **3. Transparency and limitations**

- **Coverage bias** – Strongest in English; non-English markets represented proportionally.
- **Scope** – Chatbot usage is highly personalized, and the number of possible AI queries is effectively infinite. We prioritize the most common and high-demand questions based on popularity in our 110B keyword database and Google’s People Also Ask corpus. This ensures coverage of the kinds of questions most likely to surface in AI search results, even though long-tail or niche prompts may not always be included.
- **Anomalies –** LLMs occasionally generate hallucinated or malformed links. We do not filter out hallucinated or malformed links, as they reflect real model output.
- **Cadence** – Update frequency by platform is described in the Data Modeling section.

### **4. How to interpret the data**

Brand Radar is best suited for:

- Benchmarking brand visibility and AI Share of Voice (SOV)
- Comparing competitor coverage across AI platforms
- Identifying co-citation patterns and visibility gaps

It is not a substitute for audience measurement or traffic analytics. Think of it as a media-visibility audit, showing what appears in AI and search – not *who* saw it.

### **5. Data foundation**

Brand Radar builds on Ahrefs’ data infrastructure:

- 28.7 billion keywords filtered from 110 billion discovered

This foundation ensures Brand Radar combines verified search data with transparent, modeled AI visibility – staying true to Ahrefs’ focus on accuracy and real-world behavior.
