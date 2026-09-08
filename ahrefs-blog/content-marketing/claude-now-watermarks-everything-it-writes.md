---
title: "Claude Now Watermarks Everything It Writes. Here’s What It Means for Marketers"
source: "ahrefs-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "claude-now-watermarks-everything-it-writes"
url: "https://ahrefs.com/blog/claude-now-watermarks-everything-it-writes/"
canonical: "https://ahrefs.com/blog/claude-now-watermarks-everything-it-writes/"
author: "Ryan Law"
published: "2026-08-14T13:39:21+00:00"
updated: "2026-08-14T13:39:21+00:00"
categories:
  - "Content Marketing"
  - "General SEO"
freshness_reasons: []
fetched_at: "2026-09-08T09:16:24.779077+00:00"
status_code: 200
html_hash: "b3b37add692b2d551e66c90a9cd168fed570e042407579a4909f7300204ef6ae"
clean_word_count: 1581
clean_char_count: 9315
---
# Claude Now Watermarks Everything It Writes. Here’s What It Means for Marketers

Anthropic now embeds an invisible watermark into everything Claude writes. The mark is woven into the words themselves, so it survives copy and paste, and it applies in every version of Claude, worldwide. Should you worry?

For most marketers, I don't think so.

Meanwhile, AI generation has become a default feature of software marketers open every day: Gmail, Google Docs, Canva, Figma, Photoshop, Word, Notion, Slack, Grammarly, LinkedIn... finding a marketing tool without AI in it is harder than finding one with it.

This is really only a problem if you're passing off AI work as human-written when you've promised otherwise. If you're honest about how your content gets made, a watermark shouldn't worry you.

Here's what was announced, how it works, and where it genuinely matters.

## What Anthropic announced

Anthropic is adding machine-readable marks to Claude's output to comply with EU law. From [their help doc](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content):

- **Text gets an embedded watermark.** You can't see it, it travels with the text when copied and pasted, and it may survive some editing.
- **Files get signed provenance metadata.** For image outputs, Claude attaches metadata following the [C2PA standard](https://c2pa.org/), an industry format for recording where content came from.
- **Models launched on or after August 2, 2026 support watermarking at launch.** Older models are being retrofitted.
- **It applies everywhere Claude runs**, including the API, Claude Code, and access through AWS, Google Cloud and Microsoft Foundry. This is worldwide, not only in the EU.

Crucially, Anthropic says a detected mark means content "may have been **processed by** Claude," and the word doing the work there is *processed*.

If you paste your own draft into Claude to fix your typos, the output can carry the mark. The same applies if you use it to translate or summarize something. What the watermark tells you is that Claude was somewhere in the pipeline, and it says nothing about who wrote the words.

Anthropic is also upfront that the absence of a mark proves nothing. A mark can go undetected when the passage is short, when the text has been heavily rewritten, or when a format conversion strips the file metadata.

## Watermarking will soon apply to all major AI companies

If you're hurriedly ditching your Claude subscription and switching to OpenAI, don't.

Anthropic is doing this to comply with Article 50 of the EU AI Act, which became applicable on **August 2, 2026** and requires providers of generative AI systems to mark their output in a machine-readable format.

Anthropic was first to implement and first to get the headlines, but every major provider has committed to the same obligation. Switching to a different model won't prevent eventually watermarking.

There's a second obligation, Article 50(4), that impacts publishers rather than model providers. If you publish AI-generated text to inform the public on a matter of public interest, you have to disclose it. But per the Commission's [own guidance](https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content), that requirement doesn't apply where the text "has undergone a process of human review or editorial control and where a natural or legal person holds editorial responsibility for the publication."

## How watermarking actually works

In a nutshell: the AI model nudges its word choices, very slightly, toward a secret list.

When an LLM writes, it produces one token at a time (a token is roughly a word or part of a word), scoring every possible next token by how likely it is to come next. Watermarking interferes with that scoring. The foundational approach (see [Kirchenbauer et al.](https://arxiv.org/abs/2301.10226)) works by "selecting a randomized set of 'green' tokens before a word is generated, and then softly promoting use of green tokens during sampling."

Any single word choice looks normal, because it is. But do it across a few hundred words and the pattern becomes very hard to explain as chance. Think of a coin that comes up heads 53% of the time: flip it five times and you'd never notice; but flip it a thousand times and the bias is obvious. Anyone with the key can run that test and get a confidence score.

It's worth understanding the limits of watermarking. Short text doesn't carry enough signal for reliable detection. Heavy rewriting degrades it, and Google DeepMind [notes](https://deepmind.google/discover/blog/watermarking-ai-generated-text-and-video-with-synthid/) that confidence scores drop sharply when text is "thoroughly rewritten or translated to another language." File metadata disappears on re-saving. Most important of all, detection requires the key, which only Anthropic holds for now, since they haven't published their detection method yet.

## Does this change anything for Google rankings?

Probably not. As we explained, Google is apparently agnostic to AI use, and our own research backs that up. AI-generated content can and does rank in the very highest positions in Google search:

- **5.3% of top-ranking pages are 100% AI-generated.** Another 9% are at least 80% AI.
- **Every position, including #1, has 8-12% of pages at 80%+ AI content.**
- **40% of high-AI pages get indexed**, against 49% for low-AI pages.

There is a gradient, and AI content does get gradually rarer as you move up the SERP. But it's a gentle one, with no hard line anywhere in the data.

The same holds for indexing. If Google were gating AI content out of the index, the drop between low-AI and very-high-AI pages would be severe. It's nine percentage points.

AI content detection is already possible even without watermarking. If Google wanted to penalize AI content just for AI content's sake, it would be very obvious, and we see no evidence of that in our data.

Instead, I believe Google is doing what it has always done: punishing bad content. AI content generation often coincides with creating bad content, but it doesn't have to.

So I doubt this ever becomes a ranking signal. Where it will get used is, I suspect, in contractual disputes, when an agency signed a no-AI clause or a client paid for human writing and wants to check they got it. Even then, a mark only tells you Claude was involved somewhere, and no mark tells you almost nothing.

Check any site for AI content

---

Want to test this theory yourself? Ahrefs rates the AI content level of every page in [Site Explorer](https://ahrefs.com/site-explorer), so you can check a whole site in one go instead of one URL at a time.

It works on any domain, including your competitors', and it doesn't need the provider's cooperation or a secret key. That's the gap the Claude watermark leaves open, and it's the same detector behind the research in this article.

Check out [Chris Long's post](https://www.linkedin.com/posts/chris-long-marketing_big-seo-news-claude-is-embedding-a-hidden-share-7492910177940254721-YR1_/) for a great discussion of the potential impact and implications of this on the search industry:

- **Detection just got cheaper for Google.** [Chris Long](https://www.linkedin.com/in/chris-long-marketing/) argued that a team of highly paid engineers won't struggle to read the watermark, so Google gets AI detection at a fraction of the cost, and expects OpenAI to follow.
- **A watermark can't tell slop from quality.** [Mark Barrera](https://www.linkedin.com/in/markbarrera) pointed out that Google has been fine with AI-assisted content for a while and is clear about it. What it doesn't want is spam, and a watermark doesn't separate the two.
- **Lightly edited human writing gets marked too.** [Ralph Man](https://nl.linkedin.com/in/ralph-man) asked what happens to text that's 90% his own and 10% Claude, and whether a page gets flagged or just the sentences. Put another way: a human article that Claude touched once gets marked the same as a fully generated one, which is exactly why no search engine could act on the signal responsibly.
- **Expect scrubber tools.** [Kevin Briody](https://www.linkedin.com/in/kevinbriody) predicted that anything visible to search engines and detector apps is equally visible to the wave of "watermark scrubber" plugins that follow, which makes the whole exercise moot.
- **Nothing changes for SEO.** [Bojan Maric](https://rs.linkedin.com/in/bojan-maric-7aa541184) said he got the transparency angle but couldn't see what actually changes for SEO, given Google already punishes thin content regardless of who wrote it.

## Final thoughts

Watermarking is arriving at every major AI provider because of a legal deadline. Expect OpenAI and Google to ship their versions within months, since they've already signed the paperwork.

I don't think it will change much for search. Fully AI-generated pages rank in the top three today, and Google maintains that they don't care about AI, only about thin, spammy content.

I [wrote about this on LinkedIn](https://www.linkedin.com/posts/thinkingslow_does-ai-content-work-is-entirely-the-wrong-share-7470769355325161474-Qb0W/) before any of the watermarking news broke, and my position hasn't changed: using AI to create content is not a problem, but using AI to create something *worse* than normal content marketing is.
