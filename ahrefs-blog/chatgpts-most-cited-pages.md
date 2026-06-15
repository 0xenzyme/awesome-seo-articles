---
title: "67% of ChatGPT's Top 1,000 Citations Are Off-Limits to Marketers (+ More Findings)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "chatgpts-most-cited-pages"
url: "https://ahrefs.com/blog/chatgpts-most-cited-pages/"
canonical: "https://ahrefs.com/blog/chatgpts-most-cited-pages/"
author: "Louise Linehan"
published: "2025-10-28T08:56:47+00:00"
updated: "2026-05-31T08:28:27+00:00"
categories:
  - "AI Search"
  - "Data & Studies"
freshness_reasons:
  - "ai_search_topic"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:21:38+00:00"
status_code: 200
html_hash: "c7da7576649be485bc60bd3d07a12c9405286b523df32c4fa5c77569f3b7d34f"
clean_word_count: 1443
clean_char_count: 9165
---
# 67% of ChatGPT’s Top 1,000 Citations Are Off-Limits to Marketers (+ More Findings)

I analyzed the top 1,000 pages ChatGPT cited in September 2025 using [Ahrefs Brand Radar](https://ahrefs.com/brand-radar), to understand what types of content AI is referencing right now.

You can repeat this analysis yourself pretty easily.

Just do an open database search in Brand Radar, head to the “Cited pages” report for your desired AI assistant, and export the top 1,000 cited pages.

![A screenshot of Ahrefs Brand Radar's Cited Pages report, with an arrow indicating the export button on the right of the page](https://ahrefs.com/blog/wp-content/uploads/2025/10/word-image-192202-1-1.jpg)

Then run the cited pages through our [Batch Analysis](https://ahrefs.com/batch-analysis) tool to grab more organic data on each URL.

I did exactly that. Here’s what I found…

## 1. Only a third of ChatGPT’s most-cited pages are pitch-worthy or influenceable

ChatGPT’s citations aren’t confined to encyclopedic or editorial pages—but Wikipedia stands out as the single most-cited content type, far ahead of all others.

The rest of the citations are spread across educational content, homepages, app listings, blogs, and other formats.

I used Claude to categorize this data. It may not be 100% fool-proof, but it gives a directional understanding of ChatGPT’s most-cited pages.

Here’s what the top 1,000 cited URLs look like broken down by content type:

Wikipedia plays a central role in ChatGPT’s citation behavior. The assistant is clearly looking for structured, reference-style sources that summarize topics comprehensively and predictably.

Educational and homepage pages also crop up regularly.

But what’s most interesting is the lack of opportunity to actually *get mentioned* in these high-visibility citations.

Our Director of Content Marketing, Ryan Law, refers to Wikipedia, homepages, app store pages as “dead” citations, in that you can’t easily influence them.

Going by the above categorization, only 32.3% of the top 1,000 citations in ChatGPT are [pitch/outreach-worthy](https://ahrefs.com/blog/pr-pitching-opportunities-chatgpt/)—or at least off-site and influenceable.

In other words, roughly two-thirds of ChatGPT’s top citations are effectively off-limits to traditional outreach tactics—they’re organizational pages, reference sites, and other “dead” citations you can’t realistically influence.

Further reading

- [100 Most Cited Domains in ChatGPT](https://ahrefs.com/blog/most-cited-domains-in-chatgpt/)

## 2. 28% of ChatGPT’s most-cited pages have zero organic visibility

Nearly one-third of ChatGPT’s citations point to pages with no traditional search visibility.

Here are some possible explanations for this:

**Freshness:** Some zero-keyword pages are potentially fresh content not yet ranked by search engines. ChatGPT may discover and cite new content before it accumulates search rankings.

**Niche topics:** Citations may cover specific, long-tail topics with minimal search demand. They answer questions accurately but don’t attract significant search traffic. This also applies to fan-out queries—even when someone asks ChatGPT about a popular topic, the conversation often branches into more specific subtopics where few pages directly target those angles.

**Different discovery:** ChatGPT tends to access and evaluate content differently than search engines, seemingly prioritizing accuracy, freshness, and relevance over popularity signals like backlinks.

The reality is it’s likely a combination of all three. Fresh content, niche topics, and alternative quality signals all contribute.

#### **UPDATE**

Here is a random sample of actual ChatGPT cited URLs with zero organic keywords and traffic…

This article ranked briefly in 2023, but today has zero traditional search visibility—yet it is cited in ChatGPT 4.6K times…

Then there’s this article from Lifehack on “7 ways you can be helpful today”. It is cited 1.4K times in ChatGPT, but has never gained any organic keywords or traffic.

Quite a few Apple store app pages turned up in the dataset, but again, no organic visibility.

And then there were a few pages with zero search visibility, but respectable ChatGPT presence, from news media sites like New York Post and Condé Nast Traveller.

Further reading

- [ChatGPT May Scrape Google, but the Results Don’t Match](https://ahrefs.com/blog/chatgpt-google-citations/)
- [Is ChatGPT Really Powered by Google? 118,931 Fan-Out Queries Analyzed](https://ahrefs.com/blog/is-chatgpt-really-powered-by-google/)

## 3. The cited pages that *do* rank have a median DR of 90

The pages that *do* rank display some interesting patterns. Here are the key takeaways:

1. **Site authority really matters**: 65.3% are DR 81+, median DR 90
2. **But page authority doesn’t**: 67.3% have UR 0-10 and a median UR only 6. ChatGPT cites pages from authoritative domains, but not necessarily the most linked-to pages on those domains.
3. **Pages are keyword-rich**: Median 279 keywords
4. **Most have strong backlink profiles**: Median 70 referring domains
5. **Half have high search visibility**: 52.1% rank in top 3 for keywords
6. **Low-authority exceptions exist**: 11.7% have DR 0-20

ChatGPT heavily favors pages from high-authority domains that have strong backlink profiles and rank well in search, but will cite low-authority sources for specific relevant content.

## **4. Fresh pages are prominent**

The pages ChatGPT cites are often newer and less established, suggesting recency influences citation visibility.

Our awesome data scientist, [Xibeijia](https://sg.linkedin.com/in/xibeijia-guan), has helped me with the data.

Publish dates were tricky to come by. Unfortunately, we only found dates for 12.6% of the top 1,000 pages.

Of course, this is a very small pool of data, and other pages may follow a different pattern, but from what we can analyze, it appears that ChatGPT leans towards fresh content.

Of those with detectable publication dates, 60.5% were published within the last two years.

For example, there’s this guide from Forbes that has 639 citations in ChatGPT—it was published in May 2024.

And then there’s this “Best mattress” guide from The Guardian which has 610 citations…

It was published in early 2025, then updated multiple times throughout the course of the year, as evidenced by the green “[Content changes](https://ahrefs.com/blog/content-changes/)” circles on the traffic chart.

We also analyzed update dates. We were able to retrieve freshness data for just over half of the URLs.

This was based on HTTP responses and HTTP meta data—e.g.

```
Meta:og:updated_time, meta:article:modified_time, meta:last-modified, meta:article:published_time.
```

An overwhelming number of those pages were updated in 2025 (89.7%).

Even when I tested excluding pages that had a “Last modified” date matching the time of our data request (for context, “Last modified” sometimes reflects the date of the *request* rather than an actual content update—especially when analyzing dynamic content), pages with 2025 updates still made up north of 80% of the dataset.

Another important thing to note is that Wikipedia makes up a significant chunk of this analysis—53% to be precise.

However, when I tested removing Wikipedia and analyzing the reduced dataset, the overwhelming majority of pages were still updated in 2025 (~82%).

Here’s an example from Tech Radar that gets 1.3K citations in ChatGPT. It was published eons ago, but updated as recently as October.

Its most significant recent update was published in September 2025, when two new laptops were added and reviewed.

And below you’ll find another example from Tom’s Buying Guide on the best web hosting services. It attracts 968 ChatGPT citations, and was updated on October 27th.

Here’s how recently ChatGPT’s most-cited pages were refreshed, based on the 564 URLs with detectable dates…

| Updated | % |
| --- | --- |
| 30 days | 76.4% |
| 1-6 months | 11% |
| 6-12 months | 3.7% |
| >1 year | 8.9% |

The data indicates a recency bias, consistent with findings from [Metehan Yeşilyurt’s recent research](https://metehan.ai/blog/i-found-it-in-the-code-science-proved-it-in-the-lab-the-recency-bias-thats-reshaping-ai-search/).

Yeşilyurt identified a URL\_freshness\_score in ChatGPT that favors newer content, and cited studies showing that artificially refreshing publication dates can improve AI ranking positions by as much as 95 places.

Further reading

- [AI Assistants Prefer to Cite “Fresher” Content (17 Million Citations Analyzed)](https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/)

## Wrapping up

ChatGPT’s top citations skew toward newer content, include almost a third of pages with no organic visibility, and are dominated by reference sites you can’t easily influence.

The data suggests your best bet for ChatGPT visibility is getting mentioned in specific content that falls into those influenceable categories.

To find outreach opportunities, you can use Brand Radar. Just drop in your market or niche, head to the cited pages report and look out for the top blogs, publications, and review sites.
