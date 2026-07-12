---
title: "Google Launches Open Knowledge Format, an AI Standard"
source: "semrush-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "google-launches-open-knowledge-format-for-ai-agents"
url: "https://www.semrush.com/blog/google-launches-open-knowledge-format-for-ai-agents/"
canonical: "https://www.semrush.com/blog/google-launches-open-knowledge-format-for-ai-agents/"
author: "Cecilia Meis"
published: "2026-06-23T09:15:00+00:00"
updated: "2026-06-23T09:15:00+00:00"
categories:
  - "Industry News"
  - "News & Research"
freshness_reasons: []
fetched_at: "2026-07-12T19:58:22.791619+00:00"
status_code: 200
html_hash: "22bea9133464dab85cce6711ed3bebe653c77d2aa8637bdaa6080673dfbff3bd"
clean_word_count: 656
clean_char_count: 4252
---
# Google Launches Open Knowledge Format, an AI Standard

Google has introduced Open Knowledge Format (OKF), a new open specification designed to standardize the way content is packaged and shared with AI agents. [Google Cloud Tech’s X post](https://x.com/GoogleCloudTech/status/2067012903337664886) describes it as a "vendor-neutral" standard, built to be readable by both humans and machines without requiring new tools or software to implement.

![A post on X by Google Cloud Tech introducing Open Knowledge Format (OKF) along with how it works and the benefits.](https://static.semrush.com/blog/uploads/media/83/c4/83c4e4c117d84b958f811aa380bfb2d2/c99d84c23a5301055f237eeca3d58e31/image.png)

## What is Open Knowledge Format?

OKF v0.1 uses a directory of markdown files with YAML frontmatter to establish standardized conventions, making content more compatible between producers and AI agents. According to Google, a bundle of OKF documents is:

- “**Just markdown**:” every file is plain markdown that opens in any editor, renders on GitHub, and can be indexed by standard search tools
- “**Just files**:” a bundle ships as a tarball, lives in any git repo, and mounts on any filesystem
- “**Just YAML frontmatter**:” a short list of queryable fields covers type, title, description, resource, tags, and timestamp

Google has emphasized the simplicity of the format. There is no compression scheme, new runtime, or required SDK involved.

For now, the reference implementations and tooling center on Google Cloud, but the spec itself is open and vendor-neutral, published on GitHub under the Apache 2.0 license. OKF v0.1 will evolve as producers and consumers learn what knowledge representations agents actually need.

## Why this matters for marketers

It's still early. OKF is an internal knowledge format for AI agents, not a search ranking or web-publishing signal, and it isn't tied to Google Search, YouTube, Maps, or other consumer products.

Google's argument is that OKF can pull answers from otherwise incompatible sources. Its own examples are internal and technical: table definitions, metrics, and runbooks. For marketing teams, the parallels are internal too, like brand knowledge bases, reporting, sales enablement, and training.

OKF isn't the only standard pointed at AI agents, and the differences are easy to confuse. An XML sitemap lists the pages on your site. An llms.txt file points crawlers toward your most useful content. OKF goes a step further and hands over the knowledge itself, packaged as files an agent reads directly. The difference that matters is direction: llms.txt and sitemaps face outward, toward the crawlers visiting your site, while OKF faces inward, toward an organization's own agents.

For most marketers, none of this calls for action today. A published OKF bundle won't move your rankings this week or next. Ensure your content is clean and well-structured, watch how the standard develops, and confirm that AI crawlers can already reach the content you publish. If agent-facing standards catch on the way sitemaps and schema did, that foundational work pays off.

## How to prepare with Semrush

Site Audit flags whether your site is blocking AI crawlers and surfaces technical issues that can keep your content out of AI-generated answers, including a missing llms.txt file. It runs on every Semrush plan, so it's a low-lift place to start.

To see how that work translates into visibility, the AI Visibility Toolkit tracks how often your brand gets cited across ChatGPT, Perplexity, Google AI Mode, and Gemini.

![Visibility Overview report showing metrics like mentions, citations, cited pages, distribution by LLM, and mentions by country.](https://static.semrush.com/blog/uploads/media/9a/bc/9abc00aa5277320a93b68aab7de4a979/da3e3a4f03651605a7c4372050b6a85d/image.jpeg)

For enterprise teams, Semrush Enterprise AIO goes deeper, with AI visibility tracking across more LLMs and Crawler Profiles that simulate how bots like ChatGPT and Googlebot access and interpret your site.

![Site Intelligence showing a list of projects & crawlers along with metrics like a score, issues, pages crawled, clicks, & AI referrals.](https://static.semrush.com/blog/uploads/media/96/f4/96f40fb126fb9bf5bf39fa0d476e7406/1019c21a2b611e9c3f4b49229c3f91b9/image.jpeg)
