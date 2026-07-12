---
title: "AI Overviews Cite AI-Generated Content More Than Human Writing"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "ai-overviews-cite-ai-generated-content-more-than-human-writing"
url: "https://ahrefs.com/blog/ai-overviews-cite-ai-generated-content-more-than-human-writing/"
canonical: "https://ahrefs.com/blog/ai-overviews-cite-ai-generated-content-more-than-human-writing/"
author: "Si Quan Ong"
published: "2025-07-14T09:00:12+00:00"
updated: "2026-06-05T22:44:04+00:00"
categories:
  - "AI Search"
  - "Data & Studies"
freshness_reasons:
  - "ai_search_topic"
  - "news_or_research"
fetched_at: "2026-06-12T11:14:03+00:00"
status_code: 200
html_hash: "8de1907f72df2f2501d1c56c0b2b90d2c8e251c5d26b152eb5a684833c91140a"
clean_word_count: 733
clean_char_count: 4652
---
# AI Overviews Cite AI-Generated Content More Than Human Writing

AI Overviews are AI-generated content, which means they can contain hallucinations.

Google uses [“grounding”](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview) to improve their accuracy, but according to our research, AI Overviews are more likely to cite AI-generated content than human-written content.

Here’s what we found:

## Methodology

We took one million SERPs showing AI Overviews from Ahrefs [Keywords Explorer](https://ahrefs.com/keywords-explorer) and extracted the top three cited links. 1.9 million URLs in total, of which we had 500,000 in our database.

We ran each URL through our own AI content detector, which is part of **Page Inspect** in [Site Explorer](https://ahrefs.com/site-explorer).

![Running my blog post through AI Content Detector](https://ahrefs.com/blog/wp-content/uploads/2025/07/running-my-blog-post-through-ai-content-detector-1.jpg)

Here’s what our content detector found:

- **3.6%** of pages cited in AI Overviews were categorized as “pure AI.”
- **8.6%** were categorized as “pure human.”
- **87.8%** were categorized as a mix of two.

Of the ones that were a mix of both human and AI:

- **11.2%** showed minimal AI use (1-10% of the page content was categorized as AI)
- **44%** showed moderate AI use (11-40%)
- **24.7%** showed substantial AI use (41%-70%)
- **7.9%** showed dominant AI use (71%-99%)

These findings become even more striking when compared to our previous research on AI content across the web. In our [analysis of 900,000 new pages](https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/), we found that:

- **2.5%** of pages were categorized as “pure AI.”
- **25.8%** were categorized as “pure human.”
- **71.7%** were categorized as a mix of the two.

Even though this research looked only at new pages (and not all cited URLs in AI Overviews will be new), this suggests that Google’s AI Overviews might show a bias toward citing AI-generated or AI-assisted content compared to the general distribution of content on the web.

Sidenote.

No AI content detector is perfect. Like LLMs, AI detectors are statistical models. They deal in probabilities, not certainty. They can be incredibly accurate, but they always carry the risk of false positives. You can learn more about how AI detectors work, and why they’re useful, in these articles:

- [How Do AI Content Detectors Work? Answers From a Data Scientist](https://ahrefs.com/blog/how-do-ai-content-detectors-work/)
- [What’s the Point of AI Detectors?](https://ahrefs.com/blog/whats-the-point-of-ai-detectors/)

## The ouroboros problem

We calculated the correlation between AI content percentage and the order of citations in AI Overviews across our entire dataset. **The correlation was 0.017, effectively zero**.

This suggests that Google doesn’t explicitly penalize or reward content based on whether it’s human or AI-generated when selecting sources for AI Overviews.

But considering that 87.8% of cited pages are at least AI-assisted, we’re watching AI eat its own tail in real-time. Google’s own AI-generated content is citing other AI-generated content and thus creating a feedback loop.

I don’t think Google is necessarily being careless either. Part of what we’re observing may simply reflect the current state of the web. For example, in our study of 900K pages, we found that [74% of new webpages include AI-generated content](https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/).

Google depends on creators for content. But creators are increasingly using AI to create or assist with content creation. For example, in our [State of AI in Content Marketing report,](https://ahrefs.com/blog/marketers-using-ai-publish-more-content/) where we surveyed 879 marketers, 87% of respondents use AI to help create content.

And even though Google’s trying to improve accuracy through retrieval-augmented generation (RAG), we’ve also found that [86.5% of top-ranking pages contain some amount of AI-generated content](https://ahrefs.com/blog/ai-generated-content-does-not-hurt-your-google-rankings/).

This means AI Overviews are drawing from a content ecosystem that’s increasingly AI-generated. We’re potentially witnessing the emergence of an AI content ecosystem where machines talk to machines.

## Start using AI Content Detector

Ahrefs’ AI Content Detector is part of [Site Explorer](https://app.ahrefs.com/site-explorer). Just enter any URL, go to **Page inspect**, then click on the AI Detector tab.

It’ll tell you what percentage of the content is AI-generated and which LLM was used.
