---
title: "AI Overviews Change Every 2 Days (But Never Change Their Mind)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "ai-overview-change"
url: "https://ahrefs.com/blog/ai-overview-change/"
canonical: "https://ahrefs.com/blog/ai-overview-change/"
author: "Louise Linehan"
published: "2025-11-11T09:56:10+00:00"
updated: "2026-06-06T22:25:06+00:00"
categories:
  - "AI Search"
  - "Data & Studies"
freshness_reasons:
  - "ai_search_topic"
  - "news_or_research"
fetched_at: "2026-06-12T11:13:47+00:00"
status_code: 200
html_hash: "2fca670c4f654f46d9e4321779246542122cc78b91b25819a57cdc895bde688b"
clean_word_count: 1622
clean_char_count: 10111
---
# AI Overviews Change Every 2 Days (But Never Change Their Mind)

Just how stable are AI Overviews? If you manage to get your brand mentioned or cited in them, can you take the rest of the month off? Or do you have to fight for ongoing visibility?

To find the answers, our data scientist, [Xibeijia Guan](https://sg.linkedin.com/in/xibeijia-guan), analyzed over 43,000 keywords—each with at least 16 recorded AI Overviews—over the course of a month.

She extracted this data from [Brand Radar](https://ahrefs.com/brand-radar), our new AI visibility tool that tracks hundreds of millions of prompts and queries across seven different AI assistants.

![Ahrefs Brand Radar dashboard view showing results for Toyota, versus competitors Honda, Nissan, Chevrolet, Ford, Volkswagen](https://ahrefs.com/blog/wp-content/uploads/2025/11/ahrefs-brand-radar-dashboard-view-showing-results.jpg)

The results reveal a surprising paradox in how Google’s AI operates—a constant state of change on the surface, but a deep, underlying stability.

Further reading

[10 Ways to Use Ahrefs’ Brand Radar to Grow AI Visibility](https://ahrefs.com/blog/brand-radar-use-cases/)

## AI Overview content changes 70% of the time

The content of the AI Overviews we studied changed drastically over the month of our analysis.

In fact, we found that AI Overviews have a **70% chance of changing** from one observation to the next.

This is known as the “Pointwise Change Rate”, and is calculated by dividing the number of changes observed by the number of consecutive pairs.

`# of change observed/ # of consecutive pairs`

- **Number of consecutive pairs:** The total number of times we compared two sequential AI Overview responses for the same search query.
- **Number of changes observed:** A count of how many of those comparisons resulted in the AI Overview content being different from the previous version.

Here’s an example of that flux in action.

Below are two AI Overviews for the query “renters insurance”, captured two minutes apart in incognito mode.

For easy comparison, one is in light mode…

And the other in dark mode…

It’s immediately obvious that the phrasing and content of each overview is different.

For instance, the opening paragraph of the dark mode AI Overview lists out the types of events that renters insurance covers (e.g. fire, theft, or flood)…

Whereas the light mode AI Overview focuses more on whose responsibility it is to obtain renters insurance…

Other differences include the use of examples, the level of detail, and the overall structure.

Our research revealed that AI Overviews have a persistence of 2.15 days on average, meaning their content tends to change every 2.15 days.

Since our checks weren’t daily, it’s likely that the real citation change rate is much higher.

## 45.5% of citations change when AI Overviews update

Even if your content gets cited in AI Overviews, you’re not guaranteed ongoing visibility.

Our research shows citation flux is common.

In fact, between consecutive responses, Xibeijia found that only 54.5% of URLs overlap on average.

This works out as approximately 1 URL change every time the same AI Overview query is re-run.

Meaning that, from one observation of an AI Overview to the next, **nearly half (45.5%) of the cited sources are entirely new**.

To illustrate this, here’s an example of the query “Best protein powder”, captured in Ahrefs’ SERP Overview tool via [Keywords Explorer](https://ahrefs.com/keywords-explorer).

Forbes and Fortune showed up consistently between October and November, but the third URL changed.

Initially, a Reddit comment about protein powders took second place, but a month later it was replaced by Fortune’s “best” list, and a new article from NBC on “protein shake safety” entered the third spot.

Here’s one more example for the query “renter’s insurance”—each AI Overview was captured just a week apart.

The first AI Overview returned three citations, but only two of those carried over to the second capture, where a further ten citations joined the list.

It’s clear that AI Overview visibility doesn’t follow the same consistency patterns as traditional search rankings.

Your brand can be cited today, and gone tomorrow.

Further reading

- [An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied)](https://ahrefs.com/blog/ai-overview-brand-correlation/)
- [The Complete AI Visibility Guide for SEOs, Marketers, and Site Owners](https://ahrefs.com/blog/ai-visibility/)
- [AI Visibility Audit: How to Measure Your Brand’s Presence in AI Search](https://ahrefs.com/blog/ai-visibility-audit/)

## 54% of entities stay consistent when AI Overviews refresh

Entity representation in AI Overviews is nearly as volatile as citations.

We define entities as specific, identifiable named items that appear in the text of the AI Overview—for example: people, organizations, locations, and brands.

Of the AI Overviews we studied, 37% contained entities—with each of those displaying roughly three entities per response.

By studying entity overlap, we were able to measure how often real-world information stays the same between two sequential AI Overview responses for the same search query.

The formula we used was:

`# common entities / total entities consecutive pairs`

- **Common entities:** This is the count of the named things (people, organizations, or locations) that appeared identically in both of the consecutive AI Overviews being compared.
- **Total entities consecutive pairs:** This is the total count of all unique entities found when you compare both sequential AI Overviews.

From this, we were able to calculate the percentage of named entities that remained consistent when the AI Overview changed—otherwise known as the “entity overlap”.

This worked out as 54%—or approximately 1 entity change for every AI Overview update.

Meaning that the remaining 46% experienced volatility—that’s just a .5% difference in flux vs. citations.

It could be a coincidence, but one theory is that Google regenerates URLs and entities at a similar rate.

This constant swapping of text, sources, and subjects means that you can often get a different AI Overview answer just by refreshing the page.

Here’s [Despina Gavoyannis](https://au.linkedin.com/in/despina-gavoyannis) from our blog team experiencing exactly that…

## AI Overviews score 0.95 out of 1.0 for semantic consistency

While words are in constant flux, the underlying **meaning** of the AI Overview is incredibly consistent.

We measured the “Semantic stability” between consecutive AI Overview responses and found an average cosine similarity score of 0.95, where 1.0 represents a perfect match.

This score indicates an **extremely high** degree of semantic consistency.

It’s like asking two different experts the same question—you’ll get different wording, different phrasing, and maybe different examples, but the fundamental answer is the same.

My earlier “renters insurance” example proves this.

Though each AI Overview differed in length, language, and structure, they covered largely the same topics and themes—like personal property coverage, liability protection, and common exclusions.

In other words, AI Overviews are continuously rephrasing a stable, underlying consensus drawn from their sources—this is the nature of probabilistic large-language models.

They don’t change their “opinion” on a topic day to day.

The core message remains the same, even if the text, citations, and entities switch in and out.

Further reading

[LLMs Don’t Reward Originality, They Flatten It](https://ahrefs.com/blog/llms-flatten-originality/)

## Popular AI Overviews aren’t cached

Our CMO, [Tim Soulo](https://www.linkedin.com/in/timsoulo), had a theory that Google might cache AI Overviews belonging to popular keywords to save on computational resources.

In fact, his hypothesis sparked this whole study…

But the findings disprove this.

Firstly, we’d expect to see far more stability across AI Overview content if some were being cached.

But, as we already know, consecutive AI Overviews showed different content 7 out of 10 times.

Secondly, Xibeijia measured the actual relationship between a keyword’s **search volume** and its **AI Overview change rate**, and found a Spearman correlation of -0.014.

A correlation this close to zero indicates there is likely no relationship between the two variables—hugely popular search queries are just as likely to have their AI Overview text change as very niche ones.

So, it’s unlikely Google caches popular AI Overviews—at least based on our data.

## Wrapping up

AI Overviews are both dynamic and stable at the same time.

The surface details, like the exact wording, URLs cited, and entities mentioned all switch constantly—but the underlying meaning and the core topics stay the same.

This changes how we can think about AI-generated search results.

They’re not static like traditional search results, but they’re not random either.

While you should expect your brand mentions and citations in AI Overviews to be volatile, there’s still a way to show up consistently.

Rather than focusing on individual prompts or queries, you need to become an authority on the **themes** associated with your core topics.

You can understand which themes AI ties to your brand using [Ahrefs Brand Radar](https://ahrefs.com/brand-radar).

Just drop in your brand, and head to the “Topics” report. This will show you which themes individual AI responses ladder up to.

For example, Ahrefs is most closely linked to the topics of “SEO tools” and “SEO software” in AI Overview responses.

Tracking AI visibility over a volume of answers will also help you see past the variance of AI responses.

By focusing on aggregated visibility and AI Share of Voice, you can:

- See if AI consistently ties you to a category—not just if you appeared once.
- Track trends over time—not just snapshots.
- Learn how your brand is positioned against competitors—not just mentioned.

Winning the topic, not the query, is the best way to stay visible—even when AI answers are changing daily.
