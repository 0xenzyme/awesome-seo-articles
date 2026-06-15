---
title: "How We Built a Content Optimization Tool for AI Search [Study]"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "content-optimization-ai-search-study"
url: "https://www.semrush.com/blog/content-optimization-ai-search-study/"
canonical: "https://www.semrush.com/blog/content-optimization-ai-search-study/"
author: "Luke Harsel, Roma Chereshnev, Cecilia Meis"
published: "2026-01-14T13:50:00+00:00"
updated: "2026-01-14T13:50:00+00:00"
categories:
  - "Content"
freshness_reasons:
  - "ai_search_topic"
  - "time_sensitive_title"
schema_genre: "Content"
fetched_at: "2026-06-12T14:43:51+00:00"
status_code: 200
html_hash: "6f7ada2f8b604ca6edae006ef38403247cef2a8e073eb84fe88576fbbccdfd6e"
clean_word_count: 1044
clean_char_count: 6893
---
# How We Built a Content Optimization Tool for AI Search [Study]

AI search platforms like ChatGPT, Google AI Mode, and Perplexity are changing how content gets discovered. But what makes one piece of content get cited while another gets ignored?

To answer this, we analyzed thousands of citations and compared them to similar pages ranking in Google. Our goal was to identify which text-only qualities most strongly correlate with AI citation behavior, and whether these patterns differ from traditional SEO signals.

## Key takeaways:

Based on our research, we found five content qualities that showed a strong positive correlation with AI citations, plus one that showed a negative correlation:

- **Clarity and summarization: +**32.83%
- **EEAT signals:** +30.64%
- **Q&A format: +**25.45%
- **Section structure: +**22.91%
- **Structured data elements:** +21.60%

- **Non-promotional tone:** -26.19%

![img-semblog](https://static.semrush.com/blog/uploads/media/f6/e3/f6e3392fdeebf24801feaa768c7299c3/b7a11cd6e4d3dbc3e82c20df66bd26c9/image.png)

In other words: Content that leads with clear answers, demonstrates expertise, and uses structured formatting gets cited more often.

## The Five Content Qualities That Improve AI Citations

These five criteria stood out because the difference between cited and non-cited pages was especially strong. Below is a breakdown of each criterion and how it appeared in the pages that LLMs selected.

1. Clarity and summarization (33%)
2. E-E-A-T signals (30%)
3. Q&A format (25%)
4. Section structure (22.91%)
5. Structured data score (21.60%) ![img-semblog](https://static.semrush.com/blog/uploads/media/36/40/3640bcfd8a4d6b0fe4889cc76a94afad/7c9fc671a324725b241684a1a758ff72/image.png)

One interesting parameter here was non-promotional tone, which showed a negative correlation. This doesn’t necessarily mean LLMs prefer promotional language.

A more likely explanation is that professionally written articles, which tend to be well-structured, well-sourced, and optimized, often use a commercial or persuasive tone.

As Roma Chereshnev, data scientist at Semrush explains:

> Articles written by professional copywriters are well-optimized for SEO, well-structured, or simply contain useful information. And since these articles are often written by professionals to attract traffic or to offer services or products, it's possible that these articles more often employ a promotional tone.
> Therefore, it's possible that the issue isn't that they use a promotional tone, but that often, if an article is good in itself, it's because it's written by a professional.
>
> Roma Chereshnev, Data Scientist at Semrush

Cecilia Meis, senior editor at Semrush, notes that these findings also align with core principles of high-quality content:

> Clarity and structure are not SEO shortcuts. They simply make information easier for both people and AI systems to interpret. When content is organized, direct, and backed by clear expertise, models can understand it more reliably.
>
> Cecilia Meis, Senior Editor at Semrush

## How to Use This Research

With this data, consider experimenting with your content to improve your AI visibility. Look for pages on your site that are ranking well on Google but perform poorly in AI search, and compare them using the criteria above.

Add a brief, structured summary at the beginning of the page that clearly states the key takeaway

1. Strengthen E-E-A-T signals by including author credentials and linking to reliable sources
2. Use Q&A formatting in sections where readers benefit from direct answers
3. Add structure with headings, lists, tables, or charts to help LLMs segment the content
4. Monitor performance in Semrush using Organic Rankings (for Google rankings) and the Visibility Overview report (for AI citations)

## Content Qualities With Minimal Impact on AI Citations

The scope of our study checked for 13 content parameters in total. Five of them were positive, one was negative.

The “impact” here is the % difference in our positive and negative scores

Here are the content qualities that showed little to no correlation with AI citation behavior:

![img-semblog](https://static.semrush.com/blog/uploads/media/42/91/429182f2ce8bd85d9b3d29963d266a9f/e271db2e7ea2f8364627f6f9c319f26e/image.png)

This doesn't mean these qualities are unimportant for content quality, Chereshnev explains. Instead, they simply didn’t distinguish cited pages from non-cited ones in our dataset. These qualities appeared in both samples at similar rates, so they didn’t meaningfully differentiate cited URLs from non-cited ones.

Things change fast in the AI search space, so in the future (keep an eye out for an updated study) these parameters could look more impactful.

## How We Ran the Study

Our goal was to understand how LLMs think when selecting URLs to cite. Therefore, when creating the criteria, we didn't try to match the LLM's answer with a human's opinion. We conducted research trying to consider the criteria from an LLM perspective.

In this study, we focused solely on the text visible on the page. We didn’t evaluate metadata, HTML structure, schema markup, page layout, or any technical SEO factors. The goal was to understand how LLMs respond to content as text, independent of page code or keyword targeting.

To identify which content qualities correlate with AI citations, we compared two sample groups of URLs:

1. A “positive sample” of URLs cited by AI platforms for a set of prompts
2. A “negative sample” of URLs ranking in Google's top 20 for related keywords

We scored both sample groups across 13 content parameters and measured the % difference in scores.

That way, we could see which specific content parameters appeared more often on pages that were cited by AI—even when they weren’t ranking on Google for relevant queries.

**Study period:** July 15 – August 6, 2025

**Sample size:**

- 11,882 prompts (across ChatGPT Search, Google AI Mode, and Perplexity)
- 59,410 keywords (on Google search)
- 304,805 URLs cited by LLMs (positive sample)
- 921,614 URLs ranking on Google search (negative sample)
- 337,785 total unique URLs

## What We Built

These findings directly informed the development of our [Content Toolkit](https://www.semrush.com/content/), which helps you optimize content for AI citation potential. The tool helps you identify where your content aligns with these patterns, and where it may need improvement.

![semrush content toolkit offering AI SEO improvements](https://static.semrush.com/blog/uploads/media/a7/fc/a7fc56911a961d2b019871bbc8f4442a/114d3c7de3720505ee1d8b5eebe6979d/AI-SEO-recommendations-for-a-clearer-summary.png)

AI search citations are volatile, but they’re not random.

Our data sheds some light on what works, so audit your content to give it clear structure, E-E-A-T signals, and Q&A formatting to make it AI search-ready.
