---
title: "AI Chatbot Traffic: What It Is, and How to Get More"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "ai-chatbot-traffic"
url: "https://ahrefs.com/blog/ai-chatbot-traffic/"
canonical: "https://ahrefs.com/blog/ai-chatbot-traffic/"
author: "Mateusz Makosiewicz"
published: "2026-05-15T08:43:56+00:00"
updated: "2026-06-05T22:51:00+00:00"
categories:
  - "AI Search"
freshness_reasons: []
fetched_at: "2026-06-12T11:12:46+00:00"
status_code: 200
html_hash: "42bbcd007707c3ee073e216894dc0ae1f8927b048872088bc19b22f340debfc7"
clean_word_count: 2607
clean_char_count: 16060
---
# AI Chatbot Traffic: What It Is, and How to Get More

Everyone’s talking about the traffic they’re losing to AI. Fewer people are talking about the traffic they’re gaining from it.

When ChatGPT, Perplexity, or Claude cites your content in a response, some of those users click through the citation and visit your website. That’s AI chatbot traffic, and it may convert better than most channels you’re probably already tracking.

Here’s which AI assistants send the most AI traffic, how to measure it, and how to get more of it.

## What is AI chatbot traffic?

AI chatbot traffic is referral traffic from users who clicked a link cited inside an AI chatbot response. Someone asks ChatGPT a question, ChatGPT links to your article as a source, and the user clicks through to your website. That click shows up in your analytics as a referral from chatgpt.com.

It’s worth separating this from another type of “AI bot traffic” that gets confused with it: automated crawl traffic from AI systems hitting your server.

GPTBot, ClaudeBot, PerplexityBot: these crawlers fetch and index your pages so the AI systems behind them can pull your content into training data and into live answers, but they don’t necessarily send human visitors.

![A line graph from Ahrefs Bot Analytics showing traffic trends for four categories: AI Assistant (1.3M), AI Search (298K), AI Crawler (162K), and AI Agent (25.2K). An orange arrow points specifically to the "AI Crawler" metric.](https://ahrefs.com/blog/wp-content/uploads/2026/05/a-line-graph-from-ahrefs-bot-analytics-showing-tra.png)

What we’re talking about here is human visitors who clicked out of a chatbot—the kind of traffic that can lead to sales, not learn what your site is about.

## How much AI chatbot traffic is there?

In short, AI traffic is still small, but growing fast.

According to our website [chatgpt-vs-google.com](https://chatgpt-vs-google.com/), which tracks referral traffic across 74,752 websites, all AI chatbots combined sent 3.5 million visitors in March 2026—just 0.28% of total web traffic. Google sent 345.2M million, a 28.12% share.

But Google’s share has been eroding. It dropped from 35.11% in June 2025 to 30.53% in March 2026—a 4.58 percentage point decline in ten months. At the same time, Detailed.com has reported that [only 18% of large publishers experienced year-over-year traffic growth in early 2025](https://detailed.com/state-of-seo/), largely due to shifts in AI-driven search.

## Which AI chatbots send the most traffic?

ChatGPT is the clear leader. It sent 2.7 million visitors in March 2026, roughly ten times more than any other platform. Perplexity and Gemini each sent around 230,000 visitors. Claude sent about 102,000. (source: [chatgpt-vs-google.com](http://chatgpt-vs-google.com), tracking 74,752 sites.)

But the growth numbers tell an interesting story, too. Claude grew 153.5% month-over-month in March—attributed to Anthropic expanding its web search capabilities—with an average growth rate of 30.7% over the tracked period.

Gemini grew 21.2% in March, averaging 12.8% growth. ChatGPT is the volume leader, but it’s the slowest-growing of the four, with a 1.4% average growth rate. Perplexity sits at 2.9%.

## Is AI chatbot traffic high quality?

Better than you’d expect—and in some cases, dramatically better than Google organic.

The most striking data point comes from our own analytics: AI search visitors accounted for just [0.5% of total visitors but drove 12.1% of signups](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/)—a 23x higher conversion rate than organic search.

We also track sign-ups self-attributed to AI at onboarding: March 2026 was a record month, with ChatGPT credited by 1978 new users, Claude by 2,836, Gemini by 619, and Perplexity by 67—with Claude growing fastest.

I’ve seen many stories like that shared directly by companies on LinkedIn. Here’s another one from Simon Heaton, Director of Growth Marketing at Buffer: [conversion rates 185% higher than organic search](https://www.linkedin.com/posts/heatonsimon_seo-aeo-llm-activity-7389292271738863617-Hnt6?utm_source=share&utm_medium=member_desktop&rcm=ACoAAA4j_FEBJ-6LtWbeDBK6OXr4LiCKVvlxHek).

One of the reasons why this type of traffic often converts better is that the AI already does some product research for the customer. Someone who clicks a citation in a chatbot response has already received an AI-generated answer and decided they want more. That’s a deliberate click. Compare it to someone who followed a display ad or clicked a social post while scrolling.

In fact, Kevin Indig’s [study of 48 participants making high-stakes purchases](https://www.growth-memo.com/p/how-consumers-navigate-high-stakes) found that 64% of AI Mode users clicked nothing at all—they got their answer without leaving the chatbot. Of the 23% who did click through, most visited to confirm a choice already made, not to explore options. So, AI-referred visitors who land on your site have typically already decided. It’s more verifying before the purchase than browsing.

## How to track AI chatbot traffic

AI chatbot traffic often shows up as direct traffic or disappears into an unlabeled referral bucket unless you set up specific tracking.

#### GA4 referral filtering

In GA4, create a custom segment filtering referral source against this regex:

```
.*chatgpt\.com.*|.*perplexity.*|.*gemini\.google\.com.*|.*copilot\.microsoft\.com.*|.*openai\.com.*|.*claude\.ai.*|.*deepseek\.com.*|.*huggingface\.co.*
```

This won’t catch everything—some visits will still appear as direct, particularly from mobile apps—but it gives you a workable baseline.

#### Ahrefs Web Analytics

[Ahrefs Web Analytics](https://ahrefs.com/web-analytics) has AI traffic reporting built in—no custom segments, no consent banners. Add the JavaScript snippet to your site, and here’s what you can do ([full guide](https://ahrefs.com/blog/track-analyze-ai-traffic/)):

Here are a few ideas on exploring that data in a practical way.

**See your AI traffic vs. other channels.** This shows AI as a share of total sessions alongside organic, direct, and referral—useful for deciding how much strategic weight to give the channel. You can also compare behavior metrics (bounce rate, session duration) directly against other channels here.

1. Go to the **Overview** report
2. Under “Traffic Sources,” select the **Channels** tab
3. Click **View More** to open the full channel report
4. Apply the **LLM channel filter** to isolate AI traffic

**Find which AI platforms send you the most traffic**. You’ll see a breakdown by platform (ChatGPT, Gemini, Perplexity, Copilot, Claude) with trend lines over time. Switch to **Relative** view to spot share shifts — useful for catching when one platform starts outpacing another.

1. Keep the **LLM filter** active
2. Under “Traffic Sources,” switch to the **Sources** tab
3. Click **View More**

**Find which content gets cited most***.* The Pages report shows your most-visited content from AI with bounce rate and time-on-page. Low bounce + high time on page signals content that AI visitors actually engage with after clicking — worth doubling down on.

1. Keep the **LLM filter** active
2. Under “Pages,” select **Top Pages → View More**

#### Ahrefs Bot Analytics

If you also want to monitor AI crawler activity—not human referrals, but the bots actually crawling your pages—[Ahrefs Bot Analytics](https://help.ahrefs.com/en/articles/14297049-about-bot-analytics) tracks which bots visit your site, how often, and which pages they crawl, broken down into 12 categories, including a dedicated AI bots filter.

This matters because crawl access is a prerequisite for citation. If GPTBot or ClaudeBot isn’t crawling your content, those platforms can’t cite it—which means no referral traffic downstream. Bot Analytics shows you whether they’re getting in, how frequently, and which pages they’re hitting.

#### Bing Webmaster Tools

If Copilot is on your radar, Bing Webmaster Tools has a dedicated report for AI-generated response clicks. Under the Search Performance section, you can filter by “Generative” to isolate traffic that came from Copilot’s AI answers—broken down by page and by the prompt that triggered the response.

It’s one of the few places you can see the actual user queries that led to a click, which makes it useful for understanding what topics your content is being surfaced for—and what you’re missing.

Additionally, you can use this data as an AI visibility proxy for Google Search. There’s a high chance that people will find you in other AI systems through the same prompts as you see in Bing Webmaster Tools.

## How to get more traffic from AI chatbots

Getting more AI chatbot referral traffic requires solving two separate but connected problems: getting your **brand mentioned** in AI answers, and getting your **content cited** as a source.

Mentions build awareness even when users don’t click (at least not directly). Citations are what generate the actual referral traffic.

### Get your brand mentioned more

Most of your brand’s AI mentions won’t come from your own site. In our case, when AI mentioned Ahrefs in answers, they cited our site as rarely as 10% of the time, 51% in the best-case scenario.

[Branded web mentions are the factor that correlates most strongly](https://ahrefs.com/blog/ai-visibility/) with brand appearance in AI answers (Spearman correlation: 0.664). More mentions across the web mean more training signal for the LLM, which means a stronger association with your topic.

To get more meaningful online mentions, you should focus on:

- **PR and media coverage.** Arguably more valuable in the AI era than it was before. What authoritative outlets say about you gets ingested by AI systems and shapes the answers they generate, so coverage becomes part of the training and retrieval substrate. The stronger the consensus across publications, the more consistently you’ll show up in AI responses, because the model gets more confident about the narrative around your brand.
- **Industry “best of” lists.** They aren’t always the highest-quality content on the web, but AI systems still lean on them heavily for product recommendations because rankings and reviews look like the most directly relevant piece of information for a buying question. Last time we checked across all source links AI systems pull from, [“best X” blog lists make up 43.8% of all page types](https://ahrefs.com/blog/best-lists-research/). Getting onto the right roundups—the ones real publications maintain, not the SEO-bait ones—is one of the most direct paths to AI citations.
- **Reddit and YouTube.** Reddit and YouTube have a special place in AI’s pipeline — [they sit on a dedicated retrieval lane](https://ahrefs.com/blog/why-chatgpt-cites-pages/) (separate API feeds layered on top of regular search), pulled in at huge volume so the model can sense “what real people say.” They almost always show up in the top-cited domains because of that volume.

A straightforward way to start with this is to find your AI mention gaps using [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) (AI answers that mention your competitor but not you).

1. Enter your brand and add competitors (or use the AI suggest feature)
2. In the **Overview** tab, compare mentions, impressions, and AI Share of Voice per platform
3. Click into any platform, select **Others only** to filter to queries where competitors are mentioned but you aren’t
4. Open **Cited Domains** to see which outlets are driving competitor mentions—those are the publications to target with PR

### Build content AI wants to cite

Four things drive whether a page earns citations once crawlers can reach it: format, structure, topical coverage, and freshness.

**Pick formats AI leans on**. Across sites, “best” roundups (7.06% of AI traffic), how-to guides (6.35%), “top” lists (5.5%), “vs” comparisons (4.88%), and product/service pages (4.5–6.8%) consistently outperform.

The pattern across our own three months of AI traffic data agrees: how-to guides and original data studies pull the most views and the deepest engagement, while definitions and product pages do quieter but valuable work for navigational and bottom-funnel queries.

The takeaway isn’t to pick one format—it’s to cover several so you catch different user intents.

**Cover the long tail**. Studies of real ChatGPT conversations found the [average prompt is 42 words long, and 75% are commands rather than questions](https://ahrefs.com/blog/llm-search/) (“how to create,” “best way to track”). Content clusters that cover every angle of a topic—not just the head term—match how people actually prompt AI.

Two ways to find the gaps in Ahrefs:

[Keywords Explorer,](https://ahrefs.com/keywords-explorer) enter your main topic, go to Matching Terms, group by Clusters by Parent Topic, open the Questions tab, and filter by your domain to see which angles you cover and which you don’t.

Command-based gaps: in [Competitive Analysis](https://ahrefs.com/competitive-analysis), compare your domain against two or three competitors and filter for keywords containing “how to,” “create,” “track,” or “make.” Those are the task-completion queries competitors may already own.

**Lead with the answer**. AI systems only consider the first 30 passages of a page for embeddings, and passages get retrieved individually, so each section needs to make sense on its own. Don’t bury the main point. Answer first, then expand.

**Keep content fresh**. [AI assistants cite content that is 25.7% fresher](https://ahrefs.com/blog/ai-visibility/) than what appears in organic search, with a 13.1% preference for recently updated pages. HubSpot updated one post on small business ideas and earned 1,135 new AI Overview mentions from that single refresh. Regular updates aren’t just SEO hygiene—they’re a direct citation signal.

## Use Agent A to analyze your traffic and help you get more

Doing all of that manually—finding citation gaps, uncovering long-tail opportunities, deciding which posts to refresh first—can take hours. [Agent A](https://ahrefs.com/agent-a), Ahrefs’ built-in AI assistant, handles it for you.

It connects directly to the same data sources mentioned throughout this article, including Keywords Explorer, Brand Radar, Web Analytics, and Bot Analytics. From a single prompt, it can run multi-step workflows that would normally take a full research session.

Here are a few prompts that work especially well for an AI citation strategy:

```
“Compare our ‘how-to’ content against [competitor] and [competitor]. Show the highest-volume keyword gaps.”
```

```
“Find every page on our site ranking for AI-cited queries with a bounce rate above 70%. Those are good candidates for an answer-first rewrite.”
```

```
“Which pages haven’t been updated in the last 6+ months but still receive AI traffic?”
```

```
“Using Brand Radar, show domains where competitors are being cited but we aren’t, ranked by frequency. Those are potential PR opportunities.”
```

## Final thoughts

Most “AI SEO” advice right now is people pattern-matching on a channel that barely exists yet. 0.28% of total web traffic is not a strategic priority for most businesses. But it’s a strategic priority for the ones who notice the conversion math: a channel converting, in some cases, 23x better than organic search, is worth ten times the effort its raw volume suggests.

Don’t rebuild your content strategy around it yet. Do set up tracking, ship the formats AI leans on, and check your analytics. That’s enough to be ready when the volume arrives.

Further reading

- [How to Optimize for AI Search (GEO Guide)](https://ahrefs.com/blog/how-to-optimize-for-ai-search/)
- [AI Overviews: What They Are and How They Affect SEO](https://ahrefs.com/blog/google-ai-overviews/)
- [What Is Generative Engine Optimization (GEO)?](https://ahrefs.com/blog/generative-engine-optimization/)

Thanks for reading! Feel free to reach out on [LinkedIn](https://www.linkedin.com/in/mateusz-makosiewicz/).
