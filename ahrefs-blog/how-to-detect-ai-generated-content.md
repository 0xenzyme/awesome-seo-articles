---
title: "How to Detect AI-Generated Content"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "how-to-detect-ai-generated-content"
url: "https://ahrefs.com/blog/how-to-detect-ai-generated-content/"
canonical: "https://ahrefs.com/blog/how-to-detect-ai-generated-content/"
author: "Ryan Law"
published: "2025-08-11T13:04:52+00:00"
updated: "2025-08-26T14:46:16+00:00"
categories:
  - "AI Search"
  - "General Marketing"
  - "General SEO"
freshness_reasons: []
fetched_at: "2026-06-12T11:37:49+00:00"
status_code: 200
html_hash: "caeef27e8e240ad92ad1a078c15da5bfcdfe7ad12316cadaf999e726a24f9354"
clean_word_count: 1441
clean_char_count: 9571
---
# How to Detect AI-Generated Content

In April 2025, we analyzed 900,000 newly created web pages and discovered that 74.2% contained AI-generated content.

With the rapid growth of generative AI, businesses, educators, and publishers are asking a critical question: how can we tell what’s written by humans and what’s produced by machines?

The answer: it’s possible, but not foolproof. Here’s how to approach AI detection effectively, the limitations you need to understand, and a better way to get more reliable results.

![](https://ahrefs.com/blog/wp-content/uploads/2025/08/word-image-190577-1.jpg)

Learn more in our study: [74% of New Webpages Include AI Content (Study of 900k Pages)](https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/)

## Yes, it’s possible to detect AI-generated content

Some people are skeptical that AI content detection is even possible. It is possible, but with some important caveats.

AI-generated text tends to have distinctive statistical and stylistic patterns. These patterns are not always obvious to human readers, but they can often be detected by specially constructed detection models.

In simple terms, all AI detectors work by comparing patterns in text against large collections of human-written and AI-generated examples.

Traditionally, this was done with statistical detection: counting features like word and n-gram frequencies, common syntactic structures, stylistic choices, and even statistical measures like perplexity (predictability of word choice) and burstiness (variation in sentence length), then flagging anomalies.

| Feature type | Explanation |
| --- | --- |
| Word frequencies | Count how often words like “the” or “cat” appear in a sample: the: 3, cat: 2 |
| N-gram frequencies | Measure sequences such as bigrams: “the cat” appears twice, “cat sat” appears once |
| Syntactic structures | Identify patterns like Subject–Verb–Object (SVO) structures, e.g., “the cat sat,” “the cat yawned” |
| Stylistic choices | Note tone, perspective, or formality; e.g., third-person, neutral tone |
| Perplexity | Calculate the predictability of each word based on preceding context—lower perplexity often means more predictable (and possibly machine-generated) text |
| Burstiness | Compare variation in sentence length; AI text may show consistent lengths while human text is more variable |

A third, less common approach is watermarking—embedding hidden signals into AI-generated text at creation time.

Like UV marks on currency, these signals can later be checked to confirm whether text came from a specific model, but this only works if the model owner chooses to implement it.

As of now, no major LLM providers like OpenAI, Anthropic, or Google have confirmed that they use watermarking on their public-facing model outputs. (And why would they want to penalize their users?)

Learn more: [How Do AI Content Detectors Work? Answers from a Data Scientist](https://ahrefs.com/blog/how-do-ai-content-detectors-work/)

## How to use AI content detectors

There are lots of AI detection tools available, ranging from free browser-based checkers to enterprise-grade platforms with API integrations.

If you’re an Ahrefs user, you can run our AI Content Detector directly within [**Site Explorer**](https://app.ahrefs.com/site-explorer)’s **Page Inspect** feature. Simply open **Site Explorer,** enter the URL you want to check, navigate to the **Page Inspect** report, and you can click the AI Detector tab to see an analysis, right alongside other key SEO metrics:

Good detectors don’t just give you a single yes-or-no verdict: they also break the text down and show you the likelihood that different passages are AI-generated, provide an overall article-level likelihood score, and in some cases even attempt to identify which models (such as GPT-4o) were likely used to create the content.

We ran a small-scale test comparing several of the most popular AI detectors to see how they perform in practice. The table below shows our results:

Based on my testing, Ahrefs’ AI detector and Copyleaks were the best-performing AI detectors, with GPTZero and Originality.ai close behind. At the other end of the scale, Grammarly and Writer performed the worst in my testing.

| AI content detector | Score |
| --- | --- |
| Ahrefs | 13/18 |
| Copyleaks | 13/18 |
| GPTZero | 12/18 |
| Originality.ai | 12/18 |
| Scribbr | 10/18 |
| ZeroGPT | 9/18 |
| Grammarly | 6/18 |
| Writer | 4/18 |

Learn more in my full write-up: [The 8 Best AI Detectors, Tested and Compared](https://ahrefs.com/blog/best-ai-detectors-tested/)

## No AI detector is perfect

Like LLMs, AI detectors are probabilistic—they estimate likelihood, not certainty. They can be highly accurate, but false positives are inevitable. That’s why you shouldn’t base decisions on a single result. Run multiple checks, look for patterns, and combine findings with other evidence.

All AI detectors share the same fundamental limitations, regardless of the tool or technology used.

- **Heavily edited or “humanized” AI text may evade detection. “**Post-processing’ (things like rephrasing sentences, swapping in synonyms, rearranging paragraphs, or running the text through a grammar checker) can disrupt the statistical signals that detectors look for, reducing their accuracy.
- **Basic detectors may lack accuracy and advanced features.** Detection tools require frequent updates to stay ahead of new AI models—generative AI evolves quickly, and detectors need regular retraining to recognize the latest writing styles and avoidance techniques. At Ahrefs, our detector supports multiple leading models, including models from OpenAI, Anthropic, Meta, Mixtral, and Qwen, so you can check content against a broader range of likely sources.
- **Effectiveness varies by language, content type, and model.** Detectors trained primarily on English prose may struggle with technical writing, poetry, or less common languages.
- **Ambiguous cases (like human text edited by AI) can blur results.** These hybrid workflows create mixed signals that can confuse even advanced systems.
- **Even the best tools can produce false positives or negatives.** Statistical detection is never infallible, and occasional misclassifications are inevitable because the patterns these systems rely on can overlap between human and AI writing, and subtle edits or atypical writing styles can easily blur the distinctions.

Remember: false accusations based on incorrect AI detection results can seriously damage the reputation of individuals, companies, or academic institutions.

With these limitations in mind, it’s a good idea to corroborate any detector output with additional methods before drawing conclusions.

## How to use human intuition

Human judgment can be extremely helpful for adding context to results from AI detectors. By examining context—such as patterns across multiple articles, a history of posts on social media, or the surrounding circumstances of publication—you can better gauge the likelihood that AI was involved in the writing.

Signs to look for:

- **Overly consistent tone with no subtle quirks.** Human writing is inherently a bit messy and unpredictable, with small variations in style, rhythm, and word choice that reflect personality and context. AI-generated text can sometimes lack these imperfections, producing a uniform tone that feels slightly too polished or mechanical.
- **Verbosity.** AI is very good at stretching simple ideas into long-winded explanations.
- **Lack of new information.** AI outputs often read as generic or surface-level (this is particularly obvious on LinkedIn: many AI-generated comments simply restate the original author’s idea in new words without adding any meaningful perspective or value).
- **Tell-tale word choices.** AI has a preference for slightly “off” idioms like *“ever-evolving landscape”*, formulaic hooks (*“This isn’t X… it’s Y”*), or overuse of em dashes and emojis.
- **Incentives.** Is there a clear motivation for the author to use AI content?

I see you, ChatGPT.

None of these signs offer definitive evidence for AI content, but they can add helpful context to other forms of evidence.

## A better way to use AI content detectors

If you run an AI detector on just one article, an unreliable result can be problematic. But that issue becomes less important when you look at results at scale. Running this process across many pages gives you a much clearer picture of how AI is used as part of the company’s broader marketing strategy.

With Ahrefs’ **Top pages** report in **Site Explorer,** you can see an “AI Content Level” column for almost any website page. From there, you can even inspect any individual URL and get an idea of the AI models that were likely used in the page’s creation.

Here’s a video talking through this process:

For a quick tip: use this report to spot top-ranking, heavily AI-generated content and consider creating your own AI version. If it’s ranking, it’s meeting search intent—making it a potential opportunity for you, and your AI content workflow.

Further reading

- [AI-Generated Content Does Not Hurt Your Google Rankings (600,000 Pages Analyzed)](https://ahrefs.com/blog/ai-generated-content-does-not-hurt-your-google-rankings/)
- [74% of New Webpages Include AI Content (Study of 900k Pages)](https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/)
- [AI Overviews Cite AI-Generated Content More Than Human Writing](https://ahrefs.com/blog/ai-overviews-cite-ai-generated-content-more-than-human-writing/)
