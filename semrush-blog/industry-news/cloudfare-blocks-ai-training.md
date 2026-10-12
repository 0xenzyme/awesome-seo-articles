---
title: "Cloudflare's AI training block now spares Googlebot"
source: "semrush-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "cloudfare-blocks-ai-training"
url: "https://www.semrush.com/blog/cloudfare-blocks-ai-training/"
canonical: "https://www.semrush.com/blog/cloudfare-blocks-ai-training/"
author: "Cecilia Meis"
published: "2026-09-18T14:04:00+00:00"
updated: "2026-09-18T14:04:00+00:00"
categories:
  - "Industry News"
  - "News & Research"
freshness_reasons: []
fetched_at: "2026-10-12T10:04:00.387573+00:00"
status_code: 200
html_hash: "f20834073b21ce836addfdab8cd6ce1f6deda1773381e84abe250658b5e9c8ed"
clean_word_count: 1012
clean_char_count: 6114
---
# Cloudflare's AI training block now spares Googlebot

Cloudflare [released a setting](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/) on September 15 that lets website owners refuse AI training on their content without blocking the Google, Bing, and Apple crawlers that put them in search results. The setting is called Disallow AI Training, and it's available on every plan, including the free one.

Until now, Googlebot, Bingbot, and Applebot index pages for search and gather content that can be used to train AI models, so a site that blocked one of them lost its search listings too. Cloudflare says fewer than 1% of the sites on its network block search bots, whereas 17% have turned on some way to block training.

In July, [Cloudflare said](https://www.searchenginejournal.com/cloudflares-ai-crawler-rules-can-block-googlebot/581385/) that from September 15, any site blocking AI training would block those three crawlers as well. Since then, the company has been in talks with Google, Microsoft, and Apple, and each has now added a training opt-out or promised one by a set date.

![Cloudflare domain settings for allowing search bots, blocking AI agents on ad pages, and disallowing AI training crawlers](https://static.semrush.com/blog/uploads/media/5a/2d/5a2de111a82e40680cd035badf519a79/7014b07097c9382e6f5934e73056f129/image.png)

## How disallow AI training works

When you turn on the setting, Cloudflare's Bot Preference Sync adds two rules to your robots.txt file: one disallowing Google-Extended and one disallowing Applebot-Extended. Google and Apple use those tokens only for AI training.

Amazon, Anthropic, Meta, and OpenAI already run separate crawlers for training and search, and Cloudflare blocks their training crawlers outright. Your pages should still be readable by ChatGPT search and similar tools.

Googlebot, Bingbot, and Applebot stay allowed because Cloudflare now labels their operators "Accountable,” available by offering four things:

- A way for site owners to opt out of AI training through robots.txt or a similar standard
- A way to opt out of AI summaries
- URL-level visibility into which pages were made available for training
- Assurance that opting out of training won't affect search rankings

Google says its URL-level reporting will arrive in the coming weeks, and Apple's is planned for next year. Microsoft is furthest behind. Bingbot won't read the robots.txt rule until early 2027, which means that, for now, the only way to keep Bing from training on a page is to add a NOARCHIVE meta tag.

## What the early data shows

[SeenSure tested](https://seensure.com/research/september-15) how 1,046 websites responded to eight AI crawlers on September 14 and again on September 16. Of those sites, 746 used Cloudflare, and more of them refused training crawlers after the change. GPTBot refusals rose from 18.9% to 22.0%, and ClaudeBot refusals from 19.9% to 22.8%.

Cloudflare's announcement didn't mention any change for AI search crawlers or agents, but refusals of those fell by about 13 points each. OAI-SearchBot, which feeds ChatGPT search, was refused by 16.9% of the Cloudflare sites before the change and 3.0% after. The 300 sites that don't use Cloudflare stayed flat. If the pattern holds, ChatGPT search and Perplexity can now read many Cloudflare-hosted pages they were refused last week.

"Search moved the most of any category," SEO consultant Aleyda Solis wrote on X when she shared the findings.

## Opting out of training doesn't take you out of AI answers

The new setting decides whether your content can be used to train models, but of course doesn’t determine whether you appear in AI answers. That leaves site owners with separate choices about search indexing, AI training, and AI answers, and Cloudflare's setting covers only training. Cloudflare says AI summaries are next on its list, with its own controls planned for next year.

Opting out isn't the obvious choice for every site. For sites that don't run ads, Cloudflare's recommended default leaves training set to Allow. A brand that wants AI tools to know and mention it could benefit from being in the training data, though no AI company has said how much that matters. Cloudflare recommends Disallow AI Training for publishers that make money from ads on their content.

A robots.txt rule is a request, and a crawler can ignore it. Cloudflare can detect and block crawlers that do, but with Google, Apple, and Microsoft, it's relying on commitments made to a company that sells bot-blocking products and wrote the "Accountable" standard. Cloudflare says it will track their progress publicly on Cloudflare Radar.

## Check your AI crawler settings in Semrush

Site Audit's [Blocked from AI Search](https://www.semrush.com/kb/1571-blocked-from-ai-search-site-audit) check reads the file and lists which AI crawlers are blocked from which pages. Google-Extended is on its list, so it will show as blocked once Disallow AI Training is on. Googlebot, OAI-SearchBot, and the other search crawlers shouldn't appear as blocked.

Site Audit reads robots.txt only and won't detect a block made at Cloudflare's firewall. Your [server logs will](https://www.semrush.com/blog/how-to-prepare-your-site-for-ai-agents/), so check that the search crawlers you want are still getting 200 status codes.

![Semrush Site Audit showing crawled pages where ChatGPT-User and Google-Extended AI search bots are blocked](https://static.semrush.com/blog/uploads/media/cc/51/cc510c0ebc68c076520876f0bfde2d03/4cc59fab7e99ef95e11afd850a3cacf4/image.png)

The AI Visibility Toolkit shows whether any of this changes how often you appear in AI answers. It tracks your brand and pages across ChatGPT, Google AI Mode, AI Overviews, and Gemini, and the Cited Pages tab in Visibility Overview lists which of your URLs get cited and by how many prompts. Record your numbers before you change the setting and compare them a few weeks later.

![Cited Pages report showing URLs and the number of AI prompts citing each page](https://static.semrush.com/blog/uploads/media/72/84/72843c8661ebafbe8cba375b4079683e/1ca9581f927cd5295e23762f015c7c54/image.png)
