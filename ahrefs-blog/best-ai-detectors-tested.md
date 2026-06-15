---
title: "The 8 Best AI Detectors, Tested and Compared"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "best-ai-detectors-tested"
url: "https://ahrefs.com/blog/best-ai-detectors-tested/"
canonical: "https://ahrefs.com/blog/best-ai-detectors-tested/"
author: "Ryan Law"
published: "2025-07-02T10:29:41+00:00"
updated: "2026-05-28T18:21:29+00:00"
categories:
  - "AI Search"
  - "General Marketing"
  - "General SEO"
freshness_reasons:
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:17:01+00:00"
status_code: 200
html_hash: "b9b9540bdf78dbf1dab990756db1834504bc01bc3c21b6746d0f1b017dcb260d"
clean_word_count: 2021
clean_char_count: 12978
---
# The 8 Best AI Detectors, Tested and Compared

We recently launched our new AI detector. For almost any webpage, you can analyze the likelihood that AI was used to create it, highlight AI-generated sections of text, and even identify the specific AI models used to create the text.

![](https://ahrefs.com/blog/wp-content/uploads/2025/06/word-image-189302-1.jpg)

There are tons of AI detectors available. And, while ours is the only one that can *also* show you any webpage’s backlinks and estimated search traffic, how the page content has changed over time, and how it performs relative to other pages…

…we still wanted to know how Ahrefs’ AI detector compares to other popular detectors. So we tested it.

## Methodology

I took a sample of nine articles, consisting of three **human-written** articles, three fully **AI-generated** articles, and three **hybrid** articles containing a mixture of 50% human-written and 50% AI-generated content.

I analyzed each article with free AI detectors from Ahrefs (that’s us), Scribbr, Grammarly, ZeroGPT, Copyleaks, Writer, GPTZero, and Originality.ai. In some cases, it was necessary to truncate the text sample tested.

I normalized the results (for example, translating a “24% human” score to the equivalent “76% AI”) and scored them using the following rubric:

- **2 points** if the detector’s score is within ±10 percentage points of the actual.
- **1 point** if it’s within ±20 points.
- **0 points** otherwise.

Importantly, this is not a scientific test. This is a very small sample size, my scoring rubric is arbitrary, and these are all articles I have either written, generated, or edited. This was necessary to ensure I knew the makeup of each article, but it means that these samples are biased towards a particular style of writing (mine).

Instead, think of this as a quick pulse check of the state of AI content detectors. Many of the leading AI detectors performed very well.

## The best AI detectors

Based on my testing, Ahrefs’ AI detector and Copyleaks were the best-performing AI detectors, with GPTZero and [Originality.ai](http://originality.ai) close behind. At the other end of the scale, Grammarly and Writer performed the worst in my testing.

Interestingly, false positives were not a big issue. Only 2/24 tests run on human-written content incorrectly flagged the text sample as AI-generated. All the AI detectors struggled the most with the hybrid human/AI content (for reasons explained below).

In the table below, you can see the actual AI content of each test article, followed by each tool’s analysis:

| Actual AI% | Ahrefs | Copyleaks | GPTZero | Originality.ai | Scribbr | ZeroGPT | Grammarly | Writer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100% | 100% | 100% | 92% | 100% | 94% | 99.62% | 59% | 24% |
| 100% | 100% | 100% | 100% | 100% | 100% | 98.99% | 57% | 23% |
| 100% | 86% | 83.8% | 52% | 64% | 0% | 67.76% | 7% | 15% |
| 0% | 2% | 0% | 0% | 0% | 0% | 0% | 0% | 2% |
| 0% | 6% | 0% | 0% | 0% | 0% | 2.76% | 0% | 2% |
| 0% | 0% | 0% | 4% | 0% | 0% | 91.69% | 0% | 27% |
| 50% | 13% | 46.4% | 42% | 46% | 0% | 39.06% | 0% | 0% |
| 50% | 32% | 0% | 28% | 4% | 0% | 29.4% | 0% | 5% |
| 50% | 70% | 100% | 86% | 4% | 83% | 83.21% | 0% | 6% |
| Score | 13 | 13 | 12 | 12 | 10 | 9 | 6 | 4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Ahrefs’ AI Detector

**Score:** 13/18

**URL:** <https://ahrefs.com/writing-tools/ai-content-detector>

Ahrefs AI Detector showed good accuracy across the board, with no false positives for human-written content, and good detection for AI content. It also managed to detect the specific model types used for the AI content: GPT-4o and Meta’s Llama.

By my criteria, it failed one out of nine tests, struggling to identify AI content that was blended with human writing. This is a known limitation of all AI detection tools (more on that below), and was true of all detection models.

Ahrefs AI detector is based on our own proprietary detection model, trained on a huge amount of web content. It’s unique among AI detectors because you can use it in conjunction with tons of other Ahrefs data points to see how content actually performs.

You can use Ahrefs’ AI detector to see:

- Which AI models are the best for **creating high-quality content**.
- How often **your competitors publish AI content**, and which models they use.
- How much AI content is **present in a particular SERP**, and how much effort you might need to invest to rank.
- How organic performance metrics **correlate with different levels of AI use**, like search traffic, keyword rankings, and backlinks.
- Whether AI content use **correlates with traffic drops** on particular pages or in particular subfolders.

How to use Ahrefs’ AI detector

Start by heading to [**Site Explorer**](https://ahrefs.com/site-explorer) and pasting the URL you want to analyse. From there:

1. Click the **Page inspect** report tab in the left sidebar.
2. Choose the **AI Detector** tab.
3. See your AI content level report in the right sidebar. Text that our model has detected as likely AI-generated will be color-coded according to the colors in the pie chart

In this example, our AI detector has found a section of my blog post that I used ChatGPT’s GPT-4o model to generate:

From there, you can also see how the page content has changed over time, how many backlinks it has earned, how many keywords it ranks for, how much estimated organic traffic it receives…

You can also test out the model via our [free AI content detector](https://ahrefs.com/site-explorer) page. We’re also adding bulk AI content detection to the **Top pages** report in Site Explorer (coming soon).

### Copyleaks

**Score:** 13/18

**URL:** <https://copyleaks.com/ai-content-detector>

Copyleaks matched the top score, showing solid detection ability across both extremes of AI content. It proved especially effective at catching obvious AI writing, though it occasionally faltered in mixed or borderline passages.

### GPTZero

**Score:** 12/18

**URL:** <https://gptzero.me>

GPTZero offered reliable results overall, with a clear strength in catching high-percentage AI content. However, it sometimes hesitated in assigning confident AI probabilities to mid-range or hybrid examples, slightly affecting its total accuracy.

### Originality.ai

**Score:** 12/18

**URL:** <https://originality.ai/ai-checker>

Originality.ai performed well in most cases, accurately flagging AI-heavy text but showing a tendency to overestimate human authorship when faced with subtle or well-edited AI-generated material.

### Scribbr

**Score:** 10/18

**URL:** <https://www.scribbr.com/ai-detector/>

Scribbr landed in the middle of the pack, handling clear-cut AI content reasonably well but displaying a drop in performance on more nuanced pieces, where its predictions tended to be inconsistent or overly cautious.

### ZeroGPT

**Score:** 9/18

**URL:** <https://zerogpt.com>

ZeroGPT’s performance was uneven—it occasionally nailed high-AI content but frequently misclassified partial-AI and low-AI samples. The tool’s sensitivity seemed skewed toward extremes, resulting in a less balanced profile.

### Grammarly

**Score:** 6/18

**URL:** <https://www.grammarly.com/ai-detector>

Grammarly’s free AI detector struggled with accurate AI detection, offering low-confidence or inaccurate predictions in many cases. It often failed to recognize clear signs of AI authorship and was unreliable on mixed or borderline content.

### Writer

**Score:** 4/18

**URL:** <https://writer.com/ai-content-detector/>

Writer’s free AI detector scored the lowest, frequently misidentifying or entirely missing AI-generated material. It lacked precision across the board and provided little useful signal even when dealing with content that was 100% AI-written.

## How AI detectors work

All AI content detectors work in the same basic way: they look for patterns or abnormalities in text that appear slightly different from those in human-written text.

To do that, you need two things: lots of examples of both human-written and AI-generated text to compare, and a mathematical model to use for the analysis.

| Example text | Word frequencies | N-gram frequencies | Syntactic structures | Stylistic notes |
| --- | --- | --- | --- | --- |
| “The cat sat on the mat. Then the cat yawned.” | the: 3  cat: 2  sat: 1  on: 1  mat: 1  then: 1  yawned: 1 | Bigrams  “the cat”: 2  “cat sat”: 1  “sat on”: 1  “on the”: 1  “the mat”: 1  “then the”: 1  “cat yawned”: 1 | Contains S-V (Subject-Verb) pairs such as “the cat sat” and “the cat yawned.” | Third-person viewpoint; neutral tone. |

The table above provides examples of the types of writing structures that AI detectors can identify. These patterns will appear different between AI-generated and human-written content.

Most AI detectors today use neural networks, computer systems that loosely mimic how the human brain works. They contain artificial neurons, and through practice (known as training), the connections between the neurons adjust to get better at their intended goal: identifying AI-generated text.

Even small models can do a good job at AI detection, as long as they’re trained with enough data (at least a few thousand examples).

In the academic literature, AI detectors routinely hit [80% (or greater) successful detection rates](https://ahrefs.com/blog/how-do-ai-content-detectors-work/). But all AI detectors are statistical models. They deal in probabilities, not certainty, and as our testing shows, they can be incredibly accurate, but they **always carry the risk of errors and false positives.**

Further reading

- [How Do AI Content Detectors Work? Answers From a Data Scientist](https://ahrefs.com/blog/how-do-ai-content-detectors-work/)
- [What’s the Point of AI Detectors?](https://ahrefs.com/blog/whats-the-point-of-ai-detectors/)
- [74% of New Webpages Include AI Content (Study of 900k Pages)](https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/)

## The limitations of AI detectors

All AI detectors–including the best-performers in this test, Ahrefs AI detector and Copyleaks–share the same core limitations:

- **Heavily edited or “humanized” AI content may evade detection.** Editing AI-generated content disrupts the machine-generated writing patterns AI detectors use to identify AI content.
- **Free or basic versions often lack advanced features and may have lower accuracy.** Regular updates are also required for AI detectors to keep up with new AI writing and bypass techniques. Detection effectiveness can vary based on the AI model or language used.
- **Detectors may struggle with content written in less common languages or formats.** Most detection models are trained on a specific type of content, or a specific language, and content that falls outside of these will be harder to accurately test.
- **There are not always clear answers.** As writing workflows incorporate AI in more subtle, nuanced ways, it becomes harder to answer the question “is this AI-generated?” Is something AI-generated if it was written by a human but copyedited by AI? Or outlined by AI but written by a human? These are increasingly blurry lines.

This matters because very few companies publish “pure” AI content. In our research report, [The State of AI in Content Marketing](https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/), we found that only 4.04% of all published content was unedited AI content. Almost all AI content contains some amount of human editing, and that can make AI detection tricky:

## Ethical considerations

Because of these limitations, it’s important to use AI detectors in a fair, ethical way. I recommend following these best practices for AI content detection, written in conjunction with the data scientists who developed our AI detection model:

- **Try to learn as much about the detector’s training data as possible,** and use models trained on material similar to what you want to test.
- **Test multiple documents from the same author.** A writer’s article was flagged as AI-generated? Run all their past work through the same tool to get a better sense of their base rate.
- **Never use AI content detectors to make decisions that will impact someone’s career or academic standing.** Always use their results in conjunction with other forms of evidence.
- **Use with a good dose of skepticism.** No AI detector is 100% accurate. There will always be false positives.

## Final thoughts

We used our AI detector to analyze 900,000 web pages published in April 2025 and found that [74% included AI-generated content](https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/).

It’s clear that AI content isn’t going away, so it’s a good idea to use a tool like Ahrefs’ AI detector to understand how AI content impacts your website performance. To get started, head to [**Site Explorer**](https://ahrefs.com/site-explorer).
