---
title: "Are AI Mode and AI Overviews Just Different Versions of the Same Answer? (730K Responses Studied)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "ai-overviews-vs-ai-mode"
url: "https://ahrefs.com/blog/ai-overviews-vs-ai-mode/"
canonical: "https://ahrefs.com/blog/ai-overviews-vs-ai-mode/"
author: "Despina Gavoyannis"
published: "2025-12-15T14:33:50+00:00"
updated: "2026-06-05T21:40:06+00:00"
categories:
  - "AI Search"
  - "Data & Studies"
freshness_reasons:
  - "ai_search_topic"
  - "news_or_research"
fetched_at: "2026-06-12T11:14:24+00:00"
status_code: 200
html_hash: "1e51590b5307b4ea6efda912acd518d26c36c1a7bd470e8bf0e14ec206c4be6d"
clean_word_count: 2108
clean_char_count: 13019
---
# Are AI Mode and AI Overviews Just Different Versions of the Same Answer? (730K Responses Studied)

Google’s AI Mode generates responses that are 4x longer than AI Overviews (on average). When we first noticed this, the natural assumption was that AI Mode simply expands on the same information, taking AI Overview’s concise answer and adding more detail from the same sources.

But after analyzing 730,000 response pairs, we found something unexpected: AI Mode and AI Overviews reach very similar conclusions (86% semantic similarity) while citing different sources (only 13.7% citation overlap).

This matters because it suggests these aren’t just a “short version” and “long version” of the same answer. They’re two distinct systems that happen to converge on similar conclusions through different paths.

For marketers and SEO professionals, this raises critical questions:

- If your brand is cited in AI Overviews, will it appear in AI Mode too?
- Do you need separate optimization strategies for each?
- What does it mean when two AI systems agree on *what* to say but not *where* they found it?

We analyzed citation patterns, content similarity, and entity mentions across hundreds of thousands of queries to find out. Here’s what we discovered.

## Key findings

- **Citation overlap**: Only 13.7% of citations overlap between AI Overviews and AI Mode, indicating they cite different sources in practice.
- **Word-level overlap**: There is very low (16%) word-level overlap between AI Overviews and AI Mode. They start with the same first sentence only 2.51% of the time.
- **Semantic similarity**: 9 out of 10 times, AI Mode and AI Overview agreed on what to say; they just said it differently and cited different sources.
- **Entity overlap**: AI Mode responses include 2.5x more people and brand entities than AI Overviews. But, if your brand gets mentioned in AI Overviews, there’s a 61% chance it’ll also appear in AI Mode’s longer response.
- **Brand gaps**: 32.8% of responses had no person or brand mentioned at all.
- **Citation gaps**: For 3% of responses, AI Mode doesn’t cite any sources. AI Overviews don’t cite any sources 11% of the time.

![AI Overviews vs AI Mode response similarity indicating 16% word similarity, 13.7% citation similarity and 86% semantic similarity between the two.](https://ahrefs.com/blog/wp-content/uploads/2025/12/ai-overviews-vs-ai-mode-response-similarity-indica.png)

## Methodology

We analyzed September 2025 US data from Ahrefs’ [Brand Radar](https://ahrefs.com/brand-radar), examining 540,000 query pairs for citation and URL analysis, and 730,000 query pairs for content similarity analysis. For each query, we captured both an AI Mode response and an AI Overview response.

We measured citation overlap by identifying how many URLs appeared in both AI Mode and AI Overview responses for the same query. We also tracked domain preferences to see which websites each platform cited most frequently.

For content similarity, we used two metrics: Jaccard similarity to measure word-level overlap (calculated as unique words in common divided by all unique words), and cosine similarity to measure semantic overlap on a scale from 0 (completely different) to 1 (identical meaning).

We also analyzed entity overlap by counting how many people, organizations, and brands were mentioned in both responses.

Sidenote.

This analysis compares single generations of AI Mode and AI Overview responses. Our [previous research](https://ahrefs.com/blog/ai-overview-change/#citations) showed that 45% of AI Overview citations change between generations. This means the citation pools available to each system may overlap more than our single-snapshot comparison suggests. However, the low overlap we observed (13.7%) indicates that even when multiple sources could support an answer, AI Mode and AI Overviews often select different ones in practice.

## 1. Cited URLs overlapped just 14% of the time

AI Mode and AI Overviews cited the same URLs only 13.7% of the time. When we looked at just the top 3 citations from each, the overlap was slightly higher at 16.3%. This means that 87% of the time, these two systems are pulling from completely different sources to answer the same query.

The domain preferences also differed between the two systems:

The most notable differences:

- YouTube held the top position in AI Overviews, being cited more than encyclopedic sources
- Wikipedia appeared in 10% more AI Mode citations than for AI Overviews
- While Reddit was cited a similar amount, Quora appeared 3.5x more in AI Mode citations
- Health websites were cited almost twice as much in AI Mode as in AI Overviews
- Facebook was also cited twice as much in AI Mode as in AI Overviews

AI Mode appears to lean more heavily on encyclopedic and detailed medical sources as it builds longer responses, while AI Overviews show a stronger preference for video content and community-driven platforms like Reddit.

However, both systems also showed similar preferences for content types:

AI Overviews cited videos and core pages (like homepages or main category pages) nearly twice as often as AI Mode, while both systems overwhelmingly preferred article-format content.

Try this yourself

You can see what sources AI Overviews and AI Mode cite the most in Ahrefs’ [Brand Radar](https://ahrefs.com/brand-radar). Run a blank search and check the **Cited domains** report.

Filter by AI Overview and AI Mode separately to see their preferred sources.

You can also filter for your target topics or specific brands if you want to analyze a more specific segment of the data. Check out our [guide to the best filter combinations](https://ahrefs.com/blog/brand-radar-use-cases/#:~:text=The%20filters%20let,them%20into%20action.) to try.

## 2. Only 16% of unique words overlapped between responses

AI Mode and AI Overview responses had a Jaccard similarity score of just 0.16, meaning only 16% of the unique words overlapped between the two responses for the same query.

They started with the exact same first sentence only 2.51% of the time, and produced identical responses in just 0.51% of cases.

This tells us that AI Mode isn’t simply taking AI Overview’s answer and adding more detail to it. Instead, both systems appear to research the query independently and formulate entirely new responses with minimal word or citation overlap.

Even when they agree on the answer (which they do 86% of the time semantically, as we’ll see next), they’re expressing it in fundamentally different ways.

## 3. Responses were semantically similar 90% of the time

Here’s where things get interesting: despite low word overlap (16%) and minimal citation overlap (13.7%), AI Mode and AI Overview responses achieved a semantic similarity score of 86% on average.

We measured this using cosine similarity. On a scale where 1.0 means “identical meaning” and zero means “completely unrelated,” nearly 90% of response pairs (89.7%) scored above 0.8, indicating strong semantic alignment.

Put simply: 9 out of 10 times, AI Mode and AI Overview agreed on what to say. They just said it differently and cited different sources.

There are many possible reasons why this can happen. However, Google’s documentation confirms that both [AI Mode and AI Overviews use “query fan-out”](https://developers.google.com/search/docs/appearance/ai-features#:~:text=Both%20AI%20Overviews,often%20don%27t%20trigger.) to help display a wider and more diverse set of helpful links.

Query fan-out is a process that runs multiple related searches to find supporting content while responses are being generated. Since AI Mode and AI Overviews use different models and techniques, they can easily cite different sources even when reaching similar conclusions.

This explains why they agree on *what* to say while disagreeing on *where* they found it.

Think of it like two experts answering the same question.

They might use completely different words and reference different studies, but if they’re both knowledgeable about the topic, their answers will convey the same core information. That’s what’s happening here; the systems are drawing from a consistent understanding of each topic, even as they express it differently.

## 4. AI Mode responses are 4x longer with 3x more entities

AI Mode responses are roughly 4x longer than AI Overviews and mention significantly more people and brands (3.3 entities on average compared to AI Overviews’ 1.3).

For example, looking at the keyword “cloud storage alternatives”, the AI Overview mentions seven brands only once each, and toward the end of the response:

Whereas the AI Mode response includes 23 brand mentions, repeating some brand mentions throughout the reply. Also, every component of the response contains a brand, including the very first sentence:

It’s easy to think that since AI Mode answers are 4x longer, that’s naturally why they also include more brands in absolute terms. But it’s often the case that AI Overviews is more selective with whether it mentions brands, limiting the amount of brand exposure available within the response itself.

But here’s what’s perhaps most interesting: 61% of the time, AI Mode includes every entity that AI Overview mentioned, then adds more on top.

For example, an AI Overview might mention Mayo Clinic as a health authority. AI Mode’s response includes Mayo Clinic but also adds Cleveland Clinic and WebMD. The core authority appears in both, but AI Mode expands the expert pool.

This means that if your brand is mentioned in AI Overviews, there’s a good chance it’ll also appear in AI Mode’s longer response.

But you’ll be sharing space with additional competitors or sources that didn’t make the AI Overview cut.

This pattern suggests AI Mode is building on a similar foundation of related entities as AI Overviews rather than starting from scratch with an entirely different approach.

## 5. 59% of AI Overviews contain no brands or entities

Not every response includes citations or brand mentions. For instance, 59.41% of AI Overview and 34.66% of AI Mode responses contain no brands or entities.

About one-third (32.8%) of all AI responses in our dataset mentioned no brands or people at all. These are usually informational queries where no brand is searched for or expected in the response, such as “Nov 21 zodiac”, “revenue cycle”, and “meditation before bed”.

Some responses also showed no cited sources. When citations are missing entirely, it’s typically for edge cases like:

- Simple calculations (“4 divided by 1/2”)
- NSFW or sensitive content (“sexual abuse,” “my wife hit me”)
- Redirects to help centers
- Unsupported languages (“678是美国哪里的区号”)

### Why the difference in citation rates?

AI Mode is more reliable for attribution. Only 3% of responses lack citations compared to 11% for AI Overviews.

A few possible reasons:

- **Length and format requirements:** 4x longer responses need more grounding and supporting evidence
- **User expectations differ:** AI Overviews appear in traditional search results, where users sometimes just need a quick fact. AI Mode is an interactive chat or research experience where users expect transparency about sources
- **Query filtering:** AI Overviews likely surface for more edge cases that don’t warrant citations, while AI Mode may filter these out or handle them differently

## What these findings mean for marketers and SEO professionals

These distinctions between AI Mode and AI Overviews have direct implications for how you approach AI optimization.

1. **Track visibility for AI Overviews and AI Mode separately:** With only 13.7% source overlap, being cited in one doesn’t guarantee visibility in the other. Monitor your visibility in both by using Ahrefs’ [Brand Radar](https://ahrefs.com/brand-radar).
2. **Focus on semantic authority, not exact wording:** The 86% semantic similarity shows both systems look for the same themes, just expressed differently. Build topical authority and comprehensive coverage (rather than targeting specific phrases) so your brand is seen as relevant to the topic.
3. **Consider the format differences:** AI Mode’s 97% citation rate and entity expansion (3.3 vs 1.3 entities) favor longer, well-sourced content, especially from encyclopedic sources. AI Overviews prefer video and community platforms like Reddit. The same content may not perform equally in both.
4. **Prepare for more competition in AI Mode:** If you’re cited in an AI Overview, there’s a 61% chance you’ll appear in AI Mode too, but alongside additional competitors who didn’t make the shorter cut.
5. **Invest in encyclopedic content:** Wikipedia appears in 28.9% of AI Mode citations versus 18.1% in AI Overviews. Consider how your content can serve as a comprehensive reference or be cited in existing encyclopedic resources.

The bottom line: treat AI Mode and AI Overviews as separate channels with overlapping goals but different execution. Optimize for both, but don’t assume success in one translates to the other.
