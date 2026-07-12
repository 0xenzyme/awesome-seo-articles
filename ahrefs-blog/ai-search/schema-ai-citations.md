---
title: "We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved."
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "schema-ai-citations"
url: "https://ahrefs.com/blog/schema-ai-citations/"
canonical: "https://ahrefs.com/blog/schema-ai-citations/"
author: "Louise Linehan"
published: "2026-05-11T16:36:19+00:00"
updated: "2026-06-09T07:38:48+00:00"
categories:
  - "AI Search"
  - "Data & Studies"
freshness_reasons:
  - "news_or_research"
fetched_at: "2026-06-12T12:00:28+00:00"
status_code: 200
html_hash: "832d15e5cc851b058c1843c930d4691658ebbfb11bb868fd9b5df5a8132c4cf3"
clean_word_count: 2314
clean_char_count: 13733
---
# We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved.

We kicked off this study by analyzing 6 million URLs, and found that [schema markup](https://ahrefs.com/blog/schema-markup/) is much more common on pages cited by AI than pages that aren’t.

![](https://ahrefs.com/blog/wp-content/uploads/2026/05/word-image-196889-1.png)

AI cited pages were almost three times more likely to have JSON-LD than non-cited pages.

That’s a big gap, and the kind of stat that gets shared in LinkedIn carousels and conference slides as proof that schema is an [AI visibility lever](https://ahrefs.com/blog/ai-visibility/).

But we weren’t satisfied with the data since it could easily have been correlation, not cause.

Schema markup tends to live on better-maintained, more technically sophisticated sites, and those same sites publish stronger content, build more authority, earn more links, and do all the other things that get pages cited.

Schema could be doing real work, but it could also just be riding the wave of every other signal.

So we couldn’t actually answer the question SEOs really care about: **if I add schema to my page, will I get cited more by AI?**

To find out, we ran a second study designed to isolate the effect of adding schema.

Here’s what we found.

## Adding schema didn’t boost citations on any platform

We tracked 1,885 web pages that added JSON-LD schema between August 2025 and March 2026, matched them against 4,000 control pages, and measured citation changes across Google AI Overviews, AI Mode, and ChatGPT.

Adding schema produced no major uplift in citations on any platform.

| AI source | Effect on citations | Verdict |
| --- | --- | --- |
| Google AIO | −4.6% | Small but statistically significant decline relative to matched controls; (both groups were declining together, but treated pages fell slightly faster) |
| Google AI Mode | +2.4% | Statistically indistinguishable from zero |
| ChatGPT | +2.2% | Statistically indistinguishable from zero |

These percentages come from our most reliable analysis (a *matched difference-in-differences [DiD]* test).

In this test, both AI Mode and ChatGPT treated pages performed slightly better than control pages on average, but the differences are small enough that they could easily be random noise across thousands of URLs.

AI Overviews showed a 4.6% decline, which is small but statistically significant relative to matched control pages.

But that isn’t quite the full story—we’ll get into that in the next section.

So, overall, we can’t tell whether the schema did a tiny bit of good or nothing at all.

## AI Overview pages dropped 4.6%

AI Overview citations on treated pages fell by 4.6% relative to control pages, and the result is “statistically significant” (the odds of seeing a gap this large by pure chance are about 1 in 2,500).

But before anyone reads this as “adding schema hurts your AI Overview citations”, there are two things you need to bear in mind.

1. The absolute size is small. We’re talking about an average loss of around 12 daily citations per page, in a sample where most pages were getting hundreds.
2. Both treated and matched control pages were already on a steep downward trajectory *before* schema was added—the kind of decline you’d expect from AI Overviews pulling back from these specific types of content for reasons unrelated to schema (e.g. a Google update changing what gets surfaced, the content getting stale, or Google not having recrawled the page recently).

Sidenote.

How to read this chart: both lines are anchored to 1.0 at week −1 (the week before schema was added), so they always start at the same point by design. Before treatment, both groups decline together. After treatment, treated pages sit slightly below the matched controls (this is the −4.6% gap).

That said, if adding schema had no effect on citations either way, we’d expect treated pages and matched controls to decline together at the same rate (which is broadly what we see for AI Mode and ChatGPT).

The fact that treated pages declined slightly more suggests schema had a small negative effect—but it could also reflect other factors.

We can’t tell which one it is from this data alone.

## How we isolated the effect of adding schema

Using [Brand Radar](https://ahrefs.com/brand-radar), Xibeijia pulled a few million URLs cited in AI Overviews.

She then retrieved the HTML history from our crawler database, labeled whether each URL contained `<script type="application/ld+json">`, and spotted the date that schema presence transitioned from “False” to “True”.

This left her with **1,885 pages** that introduced JSON-LD between August 2025 and March 2026.

Finally, to analyze all of that data, she used [Agent A](https://ahrefs.com/agent-a), our new AI marketing agent.

For each page Xibieijia knew two key dates:

- The last day our crawler checked the page and found no JSON-LD
- The first day our crawler detected JSON-LD on the page

The day a page added JSON-LD is its **treatment date**.

Sidenote.

“Treatment” is the standard term for the moment a change is applied to something we’re measuring.

Xibeijia measured how many times each page was cited by **Google AIO**, **Google AI Mode**, and **ChatGPT** in the 30 days before and 30 days after the treatment date.

The tricky part of any study like this is seeing past noisy data.

Citations across all of AI search were moving during this period; AI Overviews were contracting, AI Mode was exploding.

If Xibeija had just done a simple before-and-after comparison, it would have been measuring the platform trend, not the schema effect.

So for each treated URL she picked **3 control URLs** (from different domains, with similar pre-period citation levels) that had never added JSON-LD.

Comparing two groups of pages that were getting cited at the same rate before—where the only main difference was that one group added schema—made it easier to isolate what schema *actually did*.

## Four separate tests, all pointing in the same direction

We looked at the data four different ways to make sure any conclusion held up under scrutiny.

In each test, we asked a slightly different version of the question: “did schema do anything?”

You only really believe a finding when several of them agree and, in this case, they do.

**Test 1:** Compared average citation changes between treated and control pages (a two-sample t-test).

Sidenote.

How to read these charts: each bar shows how many pages experienced citation change after treatment. Right of zero = gained, left = lost. Treated pages in color, controls in grey. For AI Overviews, a few outliers (some losing 400 a day, some gaining 200) dragged the treated average negative. Strip them out, and treated and control groups look roughly the same.

**Test 2:** Ran a difference-in-differences (DiD) analysis to strip out platform-wide trends. This is the test we trust most, and the source of the findings in this article.

Sidenote.

How to read this chart: each dot shows the effect of schema after stripping out platform trends. The bar around a dot shows margin of error—if it crosses zero, the result could just be noise. If we just looked at the raw before-and-after growth of AI Mode, it came in at +43%, but this analysis revealed control URLs gained almost as much, meaning AI Mode was exploding for everyone. Strip that out and the +43% shrinks to the +2.4% shown here.

**Test 3:** Plotted citations week-by-week to check whether treated and control pages were already drifting apart before schema was added (an event study).

Sidenote.

How to read this chart: both lines are anchored to 1.0 at week −1, so they start at the same point by design. The shape is what matters. Treated and control tracked closely before week 0 and rose together after, which points to a platform-wide AI Mode boom rather than a schema effect.

**Test 4:** Re-ran the difference-in-differences (DiD) with a symmetrical window that excluded the recrawling period, to make sure the result wasn’t sensitive to how we defined “before” and “after.”

Sidenote.

How to read this chart: each platform shows two estimates side by side, one for each “before” and “after” definition. The bars around the dot show the margin of error. Both estimates land in roughly the same place for every platform, so the result holds regardless of how “before” and “after” are defined.

All four tests told the same story: no citation growth in AI Mode, no citation growth in ChatGPT, and a small AI Overview decline that’s real but small enough that we can’t definitively pin it on schema.

The most consistent finding is that not much really changed—schema had no clear positive or negative effect.

Caveat

### Where schema might still matter: pages not yet cited by AI

There’s one important thing you need to know about this data: **we studied pages that were already being cited heavily by AI.**

Every page in the dataset had 100+ AI Overview citations in February 2025, before any schema was added.

These pages were already inside the consideration set, being crawled and surfaced by LLMs.

If a page is already getting picked up, our data suggests that adding schema isn’t going to push it higher.

But for pages that *aren’t* being seen by AI systems at all, schema markup might still play a role in helping them get crawled, parsed, or indexed in the first place.

Our study can’t speak to that directly, but a recent experiment from [searchVIU](https://www.searchviu.com/en/schema-markup-and-ai-in-2025-what-chatgpt-claude-perplexity-gemini-really-see/) answers a related question.

They tested whether five major AI systems (ChatGPT, Claude, Perplexity, Gemini, and Google AI Mode) actually used schema markup when fetching a page in real-time.

Spoiler: none of them did. During direct retrieval, every system extracted only visible HTML content. JSON-LD, hidden Microdata, and hidden RDFa were all ignored.

A few other points to flag, and some questions worth testing next:

- Pages that add JSON-LD often change other things at the same time (e.g. links, content, technical fixes). We can’t fully separate schema from these kinds of co-occurrences.
- We pooled all schema types together. Article, FAQ, Product, HowTo, Organization. It’s possible some types help more than others. This may be worth digging into.
- We measured 30 days post-treatment. If JSON-LD has a slow-burn effect, a 60- or 90-day window might reveal more growth.
- We studied JSON-LD—the most widely used schema format. Other formats exist (Microdata and RDFa), but we haven’t yet tested them.
- We only looked at schema in the page’s HTML, not schema injected via JavaScript. AI crawlers appear to treat the two differently. [¹](https://www.searchviu.com/en/schema-markup-and-ai-in-2025-what-chatgpt-claude-perplexity-gemini-really-see/)
- The small AI Overview decline is real but unexplained. Treated pages dropped about 4.6% more than matched controls, and we don’t know why. A follow-up study could look at whether specific schema types or specific content types account for the gap.

## Test schema on your own pages

Want to know whether schema works for your site specifically? Run a smaller version of this study yourself. [Brand Radar](https://ahrefs.com/brand-radar) can help when it comes to tracking the course of AI citations:

- **Pick 5–10 test pages** where you plan to add JSON-LD. Ideally pages already getting some AI citations, so you have a baseline (pages with zero citations make it harder to tell whether schema did nothing, or whether the page just wasn’t going to get cited either way). You can check this in the Cited Pages report.

****

- **Pick 5–10 control pages** with similar citation levels that you’re *not* adding schema to. This is what separates “schema did something” from “AI Overviews shifted for everyone that month.”
- **Record baseline citations** for both groups across AI Overview, AI Mode, and ChatGPT in Brand Radar. Just apply URL filters to isolate those citation numbers.

- **Add schema to your test pages** and note the date. Don’t change anything else on those pages during the test window.
- **Compare both groups after 30 days** (or longer if you can). The question is: “did treated pages go up *more* than control pages did?”

If both groups moved by similar amounts, that’s more to do with the platform trend than the schema.

But if treated pages outperformed controls, that’s a sign schema is having a positive impact on citations.

If you run this on your own pages and get a different result to ours, let us know.

## Why 53% of AI-cited pages have schema (and what that doesn’t prove)

For pages already getting cited by AI, adding JSON-LD schema didn’t boost citations on Google AI Mode or ChatGPT, and showed only a small decline in AI Overviews that we can’t clearly attribute to schema.

So why are 53% of AI-cited pages running schema?

Because the sites that add structured data tend to also invest in technical SEO, publish authoritative content, [build links](https://ahrefs.com/seo/link-building), maintain their pages, and rank well in regular search.

AI systems are more likely to retrieve this kind of content, so cited pages over-index on all of those signals at once. Strip schema out and it’s very likely the rest of the signals still carry the page through to citation.

If you’re already doing the rest of the SEO work well, JSON-LD isn’t going to be the unlock.

There are still, of course, many good reasons to use JSON-LD schema (rich results, voice assistants, knowledge graphs, downstream entity recognition).

But if the only reason you’re adding it is to get more AI citations on pages that are already visible, our data doesn’t support that bet.
