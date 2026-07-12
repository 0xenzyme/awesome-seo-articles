---
title: "What Is llms.txt, and Should You Care About It?"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "what-is-llms-txt"
url: "https://ahrefs.com/blog/what-is-llms-txt/"
canonical: "https://ahrefs.com/blog/what-is-llms-txt/"
author: "Ryan Law"
published: "2025-04-22T14:42:35+00:00"
updated: "2026-03-20T14:15:14+00:00"
categories:
  - "AI Search"
  - "General SEO"
freshness_reasons: []
fetched_at: "2026-06-12T12:16:46+00:00"
status_code: 200
html_hash: "9c4ef6c7e39a30d5557194b914c8622a83233ac190013b9b900a4ec12e40da27"
clean_word_count: 1336
clean_char_count: 8241
---
# What Is llms.txt, and Should You Care About It?

Developers and marketers are being told to add llms.txt files to their sites to help large language models (LLMs) “understand” their content.

But what exactly is llms.txt, who’s using it, and—more importantly—should you care?

## What is llms.txt?

llms.txt is a proposed standard for helping LLMs access and interpret structured content from websites. You can read the full proposal on [llmstext.org](https://llmstxt.org/).

In a nutshell, it’s a text file designed to tell LLMs where to find the *good stuff*: API documentation, return policies, product taxonomies, and other context-rich resources. The goal is to remove ambiguity by giving language models a curated map of high-value content, so they don’t have to guess what matters.

![](https://ahrefs.com/blog/wp-content/uploads/2025/04/word-image-187176-1.png)

A screenshot from the proposed standard over on https://llmstxt.org/.

In theory, this sounds like a good idea. We already use files like [robots.txt](https://ahrefs.com/blog/robots-txt/) and [sitemap.xml](https://ahrefs.com/blog/how-to-create-a-sitemap/) to help search engines understand what’s on a site and where to look. Why not apply the same logic to LLMs?

But importantly, **no major LLM provider currently supports llms.txt.** Not OpenAI. Not Anthropic. Not Google.

Google included llms.txt in their [Agent2Agent (A2A) protocol](https://github.com/a2aproject/A2A/blob/6351e4c45abaf2f0a6817d66540660af277e7772/llms.txt), launched in April 2025—but that’s effectively adding a proposed protocol into another proposed protocol. Notably, Google hasn’t committed to crawling it yet.

As I said in the intro, llms.txt is a *proposed* standard. I could also propose a standard (let’s call it please-send-me-traffic-robot-overlords.txt), but unless the major LLM providers agree to use it, it’s pretty meaningless.

That’s where we’re at with llms.txt: it’s a speculative idea with no official adoption.

Don’t sleep on robots.txt

llms.txt might not impact your visibility online, but robots.txt definitely does.

You can use Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) to monitor hundreds of common technical SEO issues, including problems with your robots.txt file that might seriously hamper your visibility (or even stop your site from being crawled).

## llms.txt example

Here’s what an llms.txt file looks like in practice. This is a screenshot of [Anthropic’s actual llms.txt file](https://docs.anthropic.com/llms.txt):

At its core, llms.txt is a [Markdown](https://www.markdownguide.org/getting-started/) document (a kind of specially formatted text file). It uses H2 headers to organize links to key resources. Here’s a sample structure you could use:

```
# llms.txt
## Docs
- /api.md
A summary of API methods, authentication, rate limits, and example requests.
- /quickstart.md
A setup guide to help developers start using the platform quickly.
## Policies
- /terms.md
Legal terms outlining service usage.
- /returns.md
Information about return eligibility and processing.
## Products
- /catalog.md
A structured index of product categories, SKUs, and metadata.
- /sizing-guide.md
A reference guide for product sizing across categories.
```

You can make your own llms.txt in minutes:

1. Start with a basic [Markdown file](https://www.markdownguide.org/getting-started/).
2. Use H2s to group resources by type.
3. Link to structured, markdown-friendly content.
4. Keep it updated.
5. Host it at your root domain: https://yourdomain.com/llms.txt

You can create it yourself or use a free llms.txt generator ([like this one](https://llmstxt.firecrawl.dev/)) to make it for you.

I’ve read about some developers also experimenting with LLM-specific metadata in their llms.txt files, like token budgets or preferred file formats (but there’s no evidence that this is respected by crawlers or LLM models).

## Who’s using it (if anyone)?

You can see a list of companies using llms.txt at [directory.llmstxt.cloud](https://directory.llmstxt.cloud/)—a community-maintained index of public llms.txt files.

Here are a few examples:

- [Mintlify](https://mintlify.com): Developer documentation platform.
- [Tinybird](https://tinybird.co): Real-time data APIs.
- [Cloudflare](https://www.cloudflare.com): Lists performance and security docs.
- [Anthropic](https://www.anthropic.com): Publishes a full Markdown map of its API docs.

But what about the big players?

So far, **no major LLM provider has formally adopted llms.txt** as part of their crawler protocol:

- **OpenAI (GPTBot):** Honors robots.txt but doesn’t officially use llms.txt.
- **Anthropic (Claude):** Publishes its own llms.txt, but doesn’t state that its crawlers use the standard.
- **Google (Gemini/Bard):** Uses robots.txt (via User-agent: Google-Extended) to manage AI crawl behavior, with no mention of llms.txt support.
- **Meta (LLaMA):** No public crawler or guidance, and no indication of llms.txt usage.

This highlights an important point: creating an llms.txt is not the same as enforcing it in crawler behavior. Right now, most LLM vendors treat llms.txt as an interesting idea, and not something that they’ve agreed to prioritize and follow.

## So is llms.txt actually useful?

In my opinion, no, not yet.

There’s no evidence that llms.txt improves AI retrieval, boosts traffic, or enhances model accuracy. And no provider has committed to parsing it.

But it’s also very easy to set up. If you already have structured content like product pages or developer docs, compiling an llms.txt is trivial. It’s a Markdown file, hosted on your own website. There might be no observed benefit, but there’s also no risk. If LLMs do eventually follow it as a standard, there might be some small advantage to being early adopters.

I think llms.txt is gaining traction because we all want to influence [LLM visibility](https://ahrefs.com/blog/llm-optimization/), but we lack the tools to do it. So we latch onto ideas that *feel* like control.

How to track AI visibility

If you *do* want to track your visibility with AI systems, Ahrefs gives you two ways to get actual data instead of hoping a text file makes a difference:

- **[Bot Analytics](https://app.ahrefs.com/bot-analytics/)** (beta, free): See which AI bots are actually visiting your site. It tracks visits across 12 bot categories—including AI assistants, AI search bots, and AI crawlers—using server-side data collection through Cloudflare (no JavaScript needed). Want to know if GPTBot or ClaudeBot are even looking at your llms.txt? Now you can check. Bot Analytics
- **[Brand Radar](https://ahrefs.com/brand-radar)**: Monitor how AI assistants actually *talk* about your brand. Track mentions across ChatGPT, Perplexity, Gemini, and other platforms to see what these models say when users ask about you.

But in my personal view, llms.txt is a solution in search of a problem. Search engines already crawl and understand your content using existing standards like robots.txt and sitemap.xml. [LLMs use much of the same infrastructure](https://ahrefs.com/blog/geo-is-just-seo/).

As Google’s John Mueller put it in a [Reddit post recently](https://www.searchenginejournal.com/google-says-llms-txt-comparable-to-keywords-meta-tag/544804/):

> AFAIK none of the AI services have said they’re using LLMs.TXT (and you can tell when you look at your server logs that they don’t even check for it). To me, it’s comparable to the keywords meta tag – this is what a site-owner claims their site is about … (Is the site really like that? well, you can check it. At that point, why not just check the site directly?)
>
>
>
> John Mueller, Search Advocate, [Google](https://www.searchenginejournal.com/google-says-llms-txt-comparable-to-keywords-meta-tag/544804/)

Disagree with me, or want to share an example to the contrary? Message me on [LinkedIn](https://www.linkedin.com/in/thinkingslow) or [X](https://x.com/thinking_slow).

Further reading

- [LLMO: 10 Ways to Work Your Brand Into AI Answers](https://ahrefs.com/blog/llm-optimization/)
- [Brand Monitoring: 3 Must-Track Areas for Success](https://ahrefs.com/blog/brand-monitoring/)
- [GEO, LLMO, AEO… It’s All Just SEO](https://ahrefs.com/blog/geo-is-just-seo/)
