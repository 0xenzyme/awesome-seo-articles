---
title: "How ChatGPT Does Query Fan-Out (15 Million Queries Studied)"
source: "ahrefs-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "query-fan-out-chatgpt"
url: "https://ahrefs.com/blog/query-fan-out-chatgpt/"
canonical: "https://ahrefs.com/blog/query-fan-out-chatgpt/"
author: "Louise Linehan"
published: "2026-10-12T08:55:12+00:00"
updated: "2026-10-12T08:55:12+00:00"
categories:
  - "AI Search"
  - "Data & Studies"
freshness_reasons: []
fetched_at: "2026-10-12T10:02:37.972167+00:00"
status_code: 200
html_hash: "5f761f0fb987caf8d64155f6fe2b73018a030d2414c89c79c85ea8c2b6000bb0"
clean_word_count: 2438
clean_char_count: 14288
---
# How ChatGPT Does Query Fan-Out (15 Million Queries Studied)

The SEO industry has spent the last few months taking ChatGPT apart to see how it searches and finds its sources.

We wanted to see for ourselves how ChatGPT retrieves information—and what that means for AI visibility—so we analyzed 66.6 million free, logged-out GPT-5.6 Luna responses and their 15 million fan-out queries from August and September.

Logging out also strips out chat history and memory, so we see ChatGPT's default behavior rather than answers shaped by one person's past chats.

## Key findings

- Only **14.4% of the 66.6 million responses** required a web search.
- When they did, ChatGPT ran about **1.6 fan-out queries** on average.
- **6.8% of fan-out queries** (i.e. 6.8% of 14.4%) used a `site:` operator to search a single website, spread across ~116K different domains.
- **75.9% of the most common** `site:` searches pointed at a brand site, versus retailers, government sites, forums, or review sites.
- The word “official” appeared in **13.1% of English fan-out queries** in September, up from 10.1% in August.
- "Price" and "review" fan-outs rose up to **47% in a month**.
- In separate citation data, ChatGPT's Reddit citations **dropped 88%** in six months.
- ChatGPT seems to be moving from sites that summarize information to the **sources that produce it**.

## ChatGPT answers 6 in 7 prompts without searching the web

Only 14.4% of the 66.6 million ChatGPT responses we tracked triggered a web search.

When ChatGPT did search, it ran an average of about 1.6 fan-out queries for each response that searched.

Every web search costs OpenAI money, so it makes sense for ChatGPT to skip one when it can answer well enough from what it already knows.

This fits with [WordLift's research](https://wordlift.io/blog/en/ai-free-tiers-comparison/) which found that free-tier style models may lean more on training data to keep costs down.

This means that, for many prompts, your chances of appearing depend on what ChatGPT already knows about your brand, rather than what it can find.

## 76% of ChatGPT's 'site:' searches target a brand site

Of the 15 million fan-outs we analyzed, 6.8% used the `site:` operator to search a single website.

And among the ~160 most-searched sites, three in four of those searches targeted a brand site.

By "brand site," we mean a company website like apple.com or ikea.com, as opposed to a retailer, government site, forum, or review site.

Retailers like Walmart, Costco and Amazon made up 11.9%, and Reddit and Facebook just 1.9% between them.

The words inside the fan-outs show the same focus on official, first-hand information, with “official” and “price” the most common after “2026”, and growing by a few percentage points month-over-month.

None of this is a big surprise. If you want a product’s price or specifications, a brand site is the obvious place to check.

When a question has no single right answer, that’s when ChatGPT is more likely to look beyond official sources.

For instance, in a separate test of 20,000 US prompts, 84.4% of factual questions about pricing, product features or company details cited **at least one** official source.

For comparison questions like “A vs B” or “which is cheaper”, that dropped to 68.3%.

The mix of sources changed too.

For factual questions, 63.4% of citations were to official websites.

For comparison questions, it was 46.4%, so most citations went to other sites.

So ChatGPT relies most on official sources for facts, and leans more on other sites when it has to weigh one option against another.

We’ll dive deeper into fan-out query language a little later.

Make sure your brand site can answer the factual questions

---

If ChatGPT is going to run `site:youbrand.com` searches for your prices, specs and support details, those facts need to be on your site, in plain text, on a page it can find.

## Consumer brands make up 8 of ChatGPT's 10 most 'site:' searched domains

The domains ChatGPT targets most with `site:` are big consumer brands.

These rankings are, of course, based on our own dataset and prompts, but with around 1 million `site:` queries behind them, they give a strong sense of which domains ChatGPT leans on most.

These are mostly brands that sell products, so a brand site is the natural source for details like prices and specs.

Government domains also feature heavily.

Gov.br, gov.uk, France’s service-public.fr, the NHTSA, the FDA and the SEC all sit in the top 150, which matches [the observations](https://lilyraynyc.substack.com/p/what-we-can-learn-from-evolving-chatgpt) of [Lily Ray](https://www.linkedin.com/in/lily-ray-44755615), Founder of [Algorythmic](https://algorythmic.co/), that ChatGPT favors official sources for YMYL questions.

Note also that Reddit is still the ninth most `site:` searched domain.

## ChatGPT rarely 'site:' searches OpenAI's partners, but their citation share has doubled

Of the 17 publishers and platforms that currently have [licensing deals with OpenAI](https://tenpointlabs.com/post/ai-publisher-licensing-deals-brand-visibility-in-ai-search), Reddit is the only one in the top 150 most `site:` searched domains.

One possible reason is that ChatGPT already has its partner content pre-loaded and ready to go.

1. David McSweeney, founder of [QueryBurst](https://queryburst.com/), found that [some high-authority publications](https://queryburst.com/blog/how-chatgpt-works/#:~:text=Some%20high%20authority%20publications), including Time, Business Insider and Forbes, have pre-synthesized, page-level summaries that appear to be dropped straight into ChatGPT's context.
2. Suganthan Mohanadasan spotted a separate retrieval source in ChatGPT’s traffic called “labrador”. He describes it as a [“licensed tier”](https://suganthan.com/blog/how-chatgpt-picks-sources/#:~:text=labrador%20looks%20like%20a%20licensed%20tier%2C%20several%20of%20those%20publishers%20have%20signed%20content%20deals%20with%20OpenAI), and points out that several of its publishers have signed content deals with OpenAI.

Those `site:` searches show what ChatGPT looks up during query fan-out, but not what it ends up citing.

The cited domains tell a different story. Partner publications are everywhere.

In Brand Radar, partner titles among ChatGPT’s 200 most-cited domains more than doubled their combined share of citations, from 7.5% in March to 15.8% in July—and still held 12.5% in late September.

## "Price" and "review" fan-outs rose up to 47% in a month

The terms ChatGPT adds to its fan-out queries hint at the page types it wants to retrieve.

Between August and September, more of ChatGPT's fan-out queries were about prices, product specifications, and reviews, and slightly fewer were about definitions.

A gain of 1 or 2 percentage points can sound small, but these terms all started from a low base, and their relative rise shows starker growth.

For instance, "Price" went from 6.04% to 8.88% of fan-outs, a relative rise of nearly half (47%) in one month.

Adding to this, "Reviews" grew by a third, and "specifications" entered the top 50 for the first time.

On the flip side, "Meaning" and "definition" each fell by about a fifth, though from small shares, so that’s likely a dip rather than a trend.

Check which of your pages match the growing query types

---

You can assess which fan-out query types are most prominent in your industry using Brand Radar.

Just head to the AI responses report, filter to ChatGPT and your market, then filter the “Fan-out queries” column for words like “price”, “specifications” or “reviews” to see how often ChatGPT searches for each in your topic.

## ChatGPT's Reddit citations dropped 88% in six months

Alongside the fan-out data, we looked at which sites ChatGPT cites.

This draws on a separate dataset: Brand Radar's ChatGPT citations in the US from March to September 2026, covering 2.4 to 3.8 million answers a month.

[Snippet Digital](https://www.linkedin.com/posts/snippet-digital_does-reddit-still-matter-for-ai-search-activity-7501161037610741760-752X) found that Reddit citations in ChatGPT dropped 86% in August, and data shared by [Aleyda Solís](https://www.linkedin.com/posts/aleyda_more-insights-into-chatgpts-august-citation-activity-7501279413620150272-atem), founder of [Orainti](https://www.aleydasolis.com/en/seo-consultant/), showed social, reference, and news sites losing the most citation share between July and August.

Our Brand Radar data shows the same drop across Reddit, Wikipedia, and YouTube.

In March, about 1 in every 5 ChatGPT answers cited Reddit, but by late September it was about 1 in 43.

Similarly, Wikipedia dropped from 1 in 7 answers to 1 in 35 over the same period, and YouTube from about 1 in 370 answers to 1 in 500.

These sites are still among ChatGPT's most-cited domains, but their share has shrunk fast, so if a lot of your AI visibility comes through them, keep an eye on how often ChatGPT cites them for your topics.

### ChatGPT is moving from sites that summarize information to the sources that produce it

The citations Reddit, Wikipedia and YouTube lost went to research bodies, regulators, brands and hands-on testers, while explainer and aggregator sites fell.

The chart below shows some of the biggest rank changes among ChatGPT's 200 most-cited domains, across 2.4 million answers in March and 3.8 million in September.

PubMed climbed from 64th to 4th among ChatGPT's most-cited domains and the FDA entered at 8th, while health sites that summarize that research, like WebMD and Verywell Health, fell.

To make sure this wasn't just a result of new prompts being added to Brand Radar, we compared ~25,000 prompts that appeared among the 150,000 highest-volume prompts in both March and September.

Every site in the chart moved in the same direction on those identical prompts.

The prompts in any set will affect which sites show up, but the pattern is consistent: ChatGPT seems to be prioritizing original sources over sites that summarize them.

If your content mainly summarizes information that someone else publishes first, ChatGPT may be more likely to cite the original source instead.

The pages holding up best are the ones only you can publish, like original research, hands-on testing, and your own product facts.

## How to analyze fan-out queries in your industry

Analyzing fan-out queries in bulk shows you what ChatGPT checks before it recommends a brand in your industry, so you know what content to create and where to earn coverage.

### Pull the fan-out queries for your whole industry at once

A single fan-out query tells you very little, so it helps to see many side by side to recognize a pattern.

In Brand Radar, you can study fan-out queries across ChatGPT and Perplexity.

Just head to the AI responses report, add a filter, and enter your topic as prompt or response text.

We’ve chosen “running shoes”.

Then filter the platform to ChatGPT and the location to your market, and look at the “Fan-out queries” column next to each prompt.

To study them in bulk, filter the report on the fan-out text, such as `site:`, “official”, “price”, “review”, or “best”. You can then study them in-platform or export to a spreadsheet.

When we analyzed “running shoes”, Brand Radar returned 1,474 US ChatGPT responses with fan-out queries.

“Best” appeared 206 times, “2026” 160 times, “review” 117 times, “vs” 105 times and “official” only 65 times.

So for running shoes, ChatGPT mostly hunts for recent, third-party reviews and head-to-head comparisons, which is a different picture from the overall data above.

A running shoe brand would get more from review coverage and comparison pages than from its product pages alone.

This is based on the existing prompts in the Brand Radar database, but you can also run this analysis on your own custom “Tracked prompts”.

Let Ask Ahrefs group fan-out queries for you

---

[Ask Ahrefs](https://ahrefs.com/blog/new-features-may-2026/) can do the grouping and counting that would otherwise take hours in a spreadsheet.

For example, you can just paste in the prompt below:

> Pull the ChatGPT fan-out queries from Brand Radar for my tracked prompts/prompts about [your category]. Group them by intent (pricing, specs, reviews, comparisons, how-to), count the most common terms and `site:` domains, and tell me which groups my site answers and which it doesn’t.

Then run the same prompt each month to see which query types are growing.

Ask Ahrefs will run a full analysis, telling you the breakdown of fan-out query by topic, how your `site:` presence compares to competitor domains, and advising you on which gaps to fill.

For instance, we need to increase our reviews if we want our Brand Radar tool to be mentioned more in “AI visibility tool” related responses.

## How our data compares to other studies

Our data agrees with other research on the direction ChatGPT is heading: toward official sources, `site:` searches, and fewer citations.

The main difference is scale, since other studies found far more fan-outs and `site:` searches per prompt.

The prompts in our study are broad.

They stem from real search demand across every topic and country, while many other studies used commercial “best X” prompts that naturally trigger brand lookups.

We also tracked free, logged-out sessions, which search less than paid or reasoning models.

These numbers are a snapshot of one model between August and September 2026, and OpenAI changes how ChatGPT retrieves information constantly.

If you track fan-outs regularly, you can spot changes as they happen, rather than months later.

## Final thoughts

ChatGPT's free model answers many questions from what it already knows.

And, when it does search, it increasingly goes to whoever owns the information, like the brand that sets the price.

That leaves two ways into its answers: be well enough known that ChatGPT doesn't need to look you up, or be the original source it finds when it does.

Pages that only summarize someone else's work are currently the ones losing citations, so the pages worth investing in are the ones only you can publish, like your product facts or original research.

But, bear in mind, this could all shift again with the next model update, so keep a watchful eye on your own presence in fan-out queries and AI responses!
