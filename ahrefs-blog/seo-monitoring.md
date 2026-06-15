---
title: "SEO and AI Search Monitoring: 7 Core Things to Track Using Free Tools"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "seo-monitoring"
url: "https://ahrefs.com/blog/seo-monitoring/"
canonical: "https://ahrefs.com/blog/seo-monitoring/"
author: "Mateusz Makosiewicz"
published: "2023-09-11T05:02:46+00:00"
updated: "2026-03-25T15:30:18+00:00"
categories:
  - "AI Search"
  - "General SEO"
freshness_reasons:
  - "ai_search_topic"
  - "time_sensitive_title"
fetched_at: "2026-06-12T12:06:24+00:00"
status_code: 200
html_hash: "b05b051b8a36197723ae896511ed62440daa5661da2de58d86ca779bc6927fe2"
clean_word_count: 2150
clean_char_count: 13396
---
# SEO and AI Search Monitoring: 7 Core Things to Track Using Free Tools

SEO monitoring is about regularly checking whether your site is performing well in search and catching problems before they cost you traffic. That part hasn’t changed.

What has changed is that “search” no longer means just Google. People now ask ChatGPT, Perplexity, Copilot, and Gemini for recommendations. If your brand doesn’t show up in those answers, you’re invisible to a growing chunk of your audience.

In this post, I’ll walk you through what’s worth monitoring, how to do it, and which free tools actually get the job done

## The free tools you need

Three tools, all free for website owners:

- [**Google Search Console (GSC)**](https://search.google.com/search-console/about) — still the most accurate source for organic traffic data, because the data comes straight from Google.
- [**Ahrefs Webmaster Tools (AWT)**](https://ahrefs.com/webmaster-tools) — fills the gaps GSC leaves in keyword data, backlinks, and technical audits. No limits on keywords or data history. It also includes Web Analytics, which automatically tracks AI search traffic as a separate channel and shows AI bot activity on your site via a free Cloudflare API integration.
- [**Bing Webmaster Tools (BWT)**](https://www.bing.com/webmasters) — now with AI Performance report. Bing’s index powers Microsoft Copilot, and BWT now has an AI Performance dashboard that shows how often your content gets cited in AI answers. No other major search engine offers this for free.

## What to monitor in SEO (and how)

Here’s what matters:

- Organic traffic.
- Keyword rankings.
- Backlinks.
- Technical issues.
- AI mentions and citations.
- AI search traffic.
- AI bot activity.

Let’s go through each one.

### Organic search traffic

Organic traffic is the clicks you get from SERPs when you rank for keywords people search. It’s the most high-level SEO metric there is. If this number goes up, things are probably working. If it goes down, something needs attention.

#### How to check

Use Google Search Console.

1. Go to **Search results** report (“Performance” section).
2. Set a time range and make sure your data is set to **Web.**
3. The **Clicks** metric is your organic search traffic.

![Search results report in Google Search Console](https://ahrefs.com/blog/wp-content/uploads/2023/09/image3-1-2.jpg)

You can also see the same traffic data in AWT if you [link your GSC account](https://help.ahrefs.com/en/articles/5311821-how-do-i-see-my-google-search-console-performance-in-ahrefs). The benefit here is that you will be able to see data past GSC’s 16-month limit.

Pro Tip

Some SEOs also track conversions from organic traffic to see which pages have the biggest business impact. If you want to do that for free, Google Analytics, Ahrefs’ Web Analytics, and Matomo all work. But keep in mind: [the buyer’s journey](https://ahrefs.com/blog/buyers-journey/) for content is often too complex to attribute to a single article.

Further reading

- [12 Fast & Proven Ways to Increase Organic Traffic](https://ahrefs.com/blog/how-to-increase-organic-traffic/)

## Keyword rankings

A keyword ranking is the position a page holds on the SERP for a given query. When rankings drop, traffic follows. You also need to know when they go up because that probably means your SEO is working.

You don’t need to track every keyword—just the [target keywords](https://ahrefs.com/blog/how-many-seo-keywords/) for your most important pages.

#### How to check

You can use GSC or AWT. Both work, but they’re different.

- GSC limits you to 1,000 keywords (5,000 via API) and 16 months of history. Data is updated daily.
- [AWT](https://ahrefs.com/webmaster-tools) has no limits on keywords, backlinks, or history. It also shows you SEO metrics like search volume and Keyword Difficulty alongside your rankings.

If you’re using Google Search Console, you can:

1. Go to the **Search results** report and set up a new filter for the exact query you want to check. You will be able to see only one query at a time.

2. Enable the **Average position** metric.

If you’re using Ahrefs Webmaster Tools:

1. Go to your **Dashboard** and click on the **Organic keywords** card.

2. The tool will take you to [**Site Explorer**](https://ahrefs.com/site-explorer) where you can see your keyword rankings (“Position” column), which pages rank (“URL” column), and how fresh the data is (“Updated” column).

3. To get a list of only your most important keywords, plug them into the **Keyword** filter. Make sure to set “is” and “any” modes.

Further reading

- [How to Rank Higher on Google (10 Steps)](https://ahrefs.com/blog/how-to-rank-higher-on-google/)

### Referring domains

Referring domains are unique websites linking to yours. A growing link profile means growing [authority](https://ahrefs.com/seo/glossary/website-authority), which helps rankings.

#### How to check

Use [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools). You can:

1. Go to your **Dashboard**.

2. Access the **Backlinks** card, which gives you a quick insight into backlinks growth.

3. Click on the card to get more data (if you need it).

4. The tool will take you to [**Site Explorer**](https://ahrefs.com/site-explorer)**,** where you can see all [backlinks](https://ahrefs.com/seo/glossary/backlinks) from the domains, [Domain Rating (DR)](https://ahrefs.com/seo/glossary/domain-rating), and other related data.

You should aim to build as many or more links than your competitors to increase your chances for ranking. Read our [Link Building for SEO: The Beginner’s Guide](https://ahrefs.com/seo/link-building) to learn how.

### Technical SEO issues

[Technical SEO](https://ahrefs.com/seo/technical-seo) issues are problems Google might have with finding, [crawling](https://ahrefs.com/seo/glossary/crawlability), [indexing](https://ahrefs.com/seo/glossary/indexability), or understanding your site. Some are critical ([see these 10 issues](https://ahrefs.com/blog/seo-issues/)). Others (like missing alt text) won’t tank your rankings.

#### How to check

Use [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) to monitor for serious technical issues, i.e., errors. You can:

1. Open AWT and go to **Site Audit.**

2. Click on **Errors** in the “Issues distribution” card.

3. Go to the issue list, then click on the question mark next to the error and follow the instructions.

To keep your site in good technical health, schedule regular crawls in AWT and fix the most pressing issues.

### AI citations and mentions

AI [citations](https://ahrefs.com/blog/llm-citations/) and [mentions](https://ahrefs.com/blog/brand-mentions/) refer to what AI assistants say about your brand when people ask them questions. Are you among the recommended brands? Is the information accurate? Are competitors showing up instead of you?

**How to check**

The most straightforward method for monitoring AI mentions is to ask the AI yourself. Go to ChatGPT, Google AI Mode, Google Gemini, Perplexity, and Microsoft Copilot once a month. Ask them questions your customers would ask. This tells you whether you’re among the top recommended brands, what information AI relays about you, and whether that information is actually true.

That last part matters more than people think. AI can confidently state wrong pricing, discontinued features, or outdated descriptions of your product. If you don’t check, you won’t know.

Here are 20 questions to start with (swap the brackets for your own brand, product, and category):

| Brand awareness | Competitive positioning | Product and features | Use case and recommendations |
| --- | --- | --- | --- |
| What is [your brand]? | What are the best [product category] tools/products/services? | What features does [your brand] offer? | What [product category] should I use if I need [specific use case]? |
| What is [your brand] known for? | What are the top alternatives to [competitor]? | How much does [your brand] cost? | I’m looking for a [product category] that does [specific feature]. What do you recommend? |
| Is [your brand] a good choice for [your product category]? | How does [your brand] compare to [competitor]? | Does [your brand] offer a free plan? | What’s the best [product category] for [specific industry]? |
| What do people say about [your brand]? | What’s the best [product category] for small businesses? | What’s new with [your brand] in [current year]? | How do I get started with [product category]? |
| What are the pros and cons of [your brand]? | What’s the best [product category] for beginners? | What integrations does [your brand] support? | What [product category] do experts recommend? |

Save the responses each time. After a few months, you’ll have a log that shows whether your visibility is improving, declining, or flat.

For Copilot specifically, Bing Webmaster Tools now has an AI Performance dashboard that shows which of your pages get cited and for what prompts. Go to bing.com/webmasters, click “AI Performance,” and check your Total citations, Grounding queries (the phrases AI used when retrieving your content), and page-level citation data.

To check citations for free, there’s a quicker path. Simply open your site’s data in Site Explorer—your citation data will be right there in the Overview report.

### AI search traffic

AI search traffic is the visits you get when someone clicks through to your site from an AI-generated answer. When ChatGPT, Perplexity, or Copilot cites your page, some users click that link. This is the traffic equivalent of organic clicks, but from AI.

It’s still a small percentage of total traffic for most sites, but it’s growing fast, and the visitors tend to arrive with higher intent. They’ve already had their basic questions answered by the AI—if they’re clicking through, they’re closer to a decision.

**How to check**

Use [Ahrefs Web Analytics](https://ahrefs.com/web-analytics). It’s free, privacy-friendly, and automatically breaks out AI search traffic as its own channel. No custom setup needed. You can see visits from ChatGPT, Perplexity, Gemini, Copilot, and others right out of the box.

1. Open the dashboard and check traffic sources below the main chart.
2. Click the “AI Search” channel for a platform-by-platform breakdown.

### AI bot activity

AI bot activity refers to how AI crawlers interact with your site. These are the bots that read your pages, so AI systems can potentially use them in answers. Tracking this tells you which pages AI considers as potential sources—not necessarily what it cites, but what it’s looking at.

This is useful because it confirms your content is discoverable by AI and gives you ideas for what prompts to monitor.

For example, if you see heavy bot activity on your comparison page for “best project management tools,” the prompts worth checking could be “What’s the best project management tool for remote teams?” or “How does [your brand] compare to Asana?” If bots are hitting your pricing page a lot, check what AI says when someone asks, “How much does [your brand] cost?”

Not all AI bots do the same thing. There are two main types:

- **Training bots** crawl your site to collect data for building AI models. Examples: GPTBot (OpenAI), Google-Extended (Google/Gemini), anthropic-ai (Anthropic/Claude), CCBot (Common Crawl). They don’t send you traffic. They take content for model training.
- **Search/citation bots** fetch your pages in real time when a user asks a question. Examples: ChatGPT-User, OAI-SearchBot (OpenAI), PerplexityBot, ClaudeBot. These are the ones that can actually drive referral traffic back to your site when they cite you.

If you see training bot activity on a page, AI models are learning from it. If you see search bot activity, AI assistants are actively pulling that content into live answers.

**How to check**

Use Ahrefs Web Analytics with the Cloudflare integration. If your site uses Cloudflare (free plan works), connect your account in Web Analytics to see AI bot activity—which bots are reading your content, how often, and which pages they focus on.

Setting up the integration—use the option on the right if you have a free Cloudflare plan.

Further reading

- [The Complete AI Visibility Guide for SEOs, Marketers, and Site Owners](https://ahrefs.com/blog/ai-visibility/)

## Final thoughts

GSC, AWT, and BWT together cover both traditional SEO and the basics of AI visibility monitoring. That’s a lot of ground for three free tools.

But there are things only premium tools unlock:

- **Thorough rank tracking**—use [Rank Tracker](https://ahrefs.com/rank-tracker) to get ranking data across locations and devices, ranking history, competitor reports, and share of voice.
- **Competitive analysis**—with [Site Explorer](https://ahrefs.com/site-explorer), you can see which keywords competitors rank for and how they earn backlinks.
- **Email alerts**—[get notified](https://ahrefs.com/alerts) when competitors gain new keywords or backlinks, or when your brand gets mentioned.
- **Advanced AI visibility**—full [Brand Radar](https://ahrefs.com/brand-radar) lets you track custom prompts, monitor citations at scale, and run competitive intelligence on who’s winning the AI visibility race in your space.

Thanks for reading! Questions or feedback? Find me on [LinkedIn](https://www.linkedin.com/in/mateusz-makosiewicz/).
