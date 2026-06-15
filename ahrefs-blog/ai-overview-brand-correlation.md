---
title: "An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "ai-overview-brand-correlation"
url: "https://ahrefs.com/blog/ai-overview-brand-correlation/"
canonical: "https://ahrefs.com/blog/ai-overview-brand-correlation/"
author: "Louise Linehan"
published: "2025-05-26T09:41:41+00:00"
updated: "2026-04-27T19:17:59+00:00"
categories:
  - "AI Search"
  - "Data & Studies"
freshness_reasons:
  - "ai_search_topic"
  - "news_or_research"
fetched_at: "2026-06-12T11:13:44+00:00"
status_code: 200
html_hash: "0f53aeeb681c3d4297526e2a15163dcd07a35f09be5f72274e2c04f595a136d0"
clean_word_count: 2258
clean_char_count: 14233
---
# An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied)

With Google’s [AI mode developments](https://www.youtube.com/watch?v=UG-8YsHnvt4), we’re heading toward a future where search results could eventually roll up into one big AI Overview.

Soon it won’t be a case of “Should I, or shouldn’t I optimize for AI Overviews?”

If you want *any* chance of search visibility, you’ll need to understand how to rank in Google’s AI results.

With this new reality in mind, we’ve analyzed 75,000 brands to see which search factors are most likely to influence brand mentions in AI Overviews.

As ever, I’d like to say a huge thanks to our awesome data scientist Xibeijia Guan for pulling the data together for this study.

Let’s get into it.

## Top takeaways

The objective of this study was to find out which search factors correspond with higher brand visibility in AI Overviews.

We used the [Spearman correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) to analyze the data in this study–larger positive values reflect stronger positive correlations.

![Factors that correlate with brand appearance in AI overviews. Branded web mentions (0.664), Branded anchors (0.527), Branded search volume (0.392), DR (0.326), # of ref domains (0.295), Branded traffic (0.274), Number of backlinks (0.218), Ad traffic (0.216), Ad cost (0.215), URL rating (0.18), Number of site pages (0.17)](https://ahrefs.com/blog/wp-content/uploads/2025/05/1-brand-factor-correlation-study-1.png)

- **Brand web mentions** show the strongest correlation (0.664) with AI Overview brand visibility.
- Web mentions (0.664) correlate **much more strongly than backlinks** (0.218).
- The top 3 correlations are all **off-site factors**: brand web mentions (0.664), brand anchors (0.527), and brand search volume (0.392).
- Paid factors like branded ad traffic (0.216) and branded ad cost (0.215) show **weak positive correlations** with AI mentions.
- Brands earning the most web mentions earn up to **10X more mentions** in AI Overviews vs. the next closest quartile.
- **26% of brands have zero mentions** in AI Overviews.

While the data shows statistical relationships, I should emphasize that **correlation ≠ causation**.

All the factors we studied revealed moderate to very weak correlations on the Spearman scale, but that doesn’t necessarily mean they should be overlooked.

These signals, and tons of others, all combine to influence your brand’s visibility in AI search.

## The methodology

In this study, we set out to research “domain” factors and “keyword” factors, and see how they correlated with visibility in AI Overviews.

The “domain” factors included:

- Domain Rating (DR)
- # of referring domains
- # of backlinks
- Ad traffic
- Ad cost
- URL rating

All “domain” factors corresponded to the brand’s domain. This was based on data extracted from [Ahrefs Site Explorer](https://ahrefs.com/site-explorer) via [Ahrefs API](https://docs.ahrefs.com/docs/api/reference/introduction).

The “keyword” factors included:

- Branded web mentions (mentions of the brand name anywhere across the web)
- Branded anchors (mentions of the brand name in hyperlinked text)
- Branded search volume (monthly search volume attached to the brand name)

All “keyword” factors corresponded to the domain’s #1 ranking keyword.

We filtered for domains with DR > 40 and took their highest volume keyword with a monthly search volume of at least 800.

Though not a perfect calculus, it worked pretty well in helping us find legitimate brands.

Following that, we analyzed millions of AI Overview responses to find mentions of those brands, using [Ahrefs Brand Radar](https://ahrefs.com/brand-radar)

Roughly 26% had zero mentions–we studied the remaining ~74%.

## 1. Your brand’s web presence is everything

The strongest correlations with AI Overview mentions are all **off-site factors**:

- Branded web mentions (0.664)
- Branded anchors (0.527)
- Branded search volume (0.392)

This aligns with what we’re seeing across the industry: AI visibility isn’t just about your website—it’s about how widely your brand shows up across the web.

As [Kevin Indig](https://www.linkedin.com/in/kevinindig/) found in his recent [AI visibility research](https://www.growth-memo.com/p/what-content-works-well-in-llms):

> Brand search volume is the biggest predictor for visibility in ChatGPT… The number of AI Chatbot mentions and brand search volume have a correlation of .334 - pretty good in this field.
>
>
>
> Kevin Indig, Organic Growth Advisor, [kevin-indig.com](https://www.kevin-indig.com/)

Our correlation of 0.392 for branded search volume closely supports Kevin’s findings—but we’ve uncovered even stronger signals.

Branded web mentions–linked or unliked–show the highest correlation with brand presence in AI Overviews.

As our Content Marketing Director, [Ryan Law](https://www.linkedin.com/in/thinkingslow/), noted in his article [GEO, LLMO, AEO… It’s All Just SEO](https://ahrefs.com/blog/geo-is-just-seo/):

> Unlinked mentions—text written about your brand on other websites—have very little impact on SEO, but a much bigger impact on GEO… LLMs derive their understanding of a brand’s authority from words on the page, from the prevalence of particular words, the co-occurrence of different terms and topics, and the context in which those words are used.
>
>
>
> Ryan Law, Director of Content Marketing, [Ahrefs](https://ahrefs.com)

Another major thing to note is that all three of these factors represent “keyword” factors in our study.

Large Language Models (LLMs) are predictive language models. They train on a huge corpus of web text.

It makes sense that the signals determining your brand’s visibility in the LLMs of AI Overviews are rooted in text and language.

From all of this data we can infer that your brand’s presence across the web—not just your own website—is what AI Overviews draw on when deciding whether to mention you.

## 2. AI Overview visibility correlates weakly with link metrics

When it comes to brand visibility in AI Overviews, online brand mentions appear to be more impactful than link building.

We found moderate to weak correlations between link metrics and brand mentions in AI Overviews:

- Domain Rating (0.326)
- Number of referring domains (0.295)
- Number of backlinks (0.218)

[Research from Seer Interactive](https://www.seerinteractive.com/insights/what-drives-brand-mentions-in-ai-answers) confirms this pattern.

The Seer team studied keywords, backlinks, domain rank, and SERP features across Google and Bing, to understand their relationship with brand mentions in ChatGPT.

As you can see, they also discovered weaker correlations in link metrics such as domain rank (0.25) and backlinks (0.10), and observed the strongest relationships between Google keywords when it came to ChatGPT brand visibility.

## 3. Branded traffic matters, but not as much as you’d think

Branded traffic is the organic traffic your site receives from branded keywords.

We found it to show a weak correlation (0.274) with brand mentions in AI Overviews.

Tip

Assess your branded traffic in Ahrefs Site Explorer. Just enter your domain, and head to “Organic keywords by intent” for branded and non-branded traffic trend data.

[Google’s web ranking systems](https://static.googleusercontent.com/media/www.google.com/en//search/howsearchworks/google-about-AI-overviews.pdf) are integrated into AI Overviews–that’s how they’re able to curate information from the top web results.

[Leaked internal documents](https://sparktoro.com/blog/an-anonymous-source-shared-thousands-of-leaked-google-search-api-documents-with-me-everyone-in-seo-should-see-them/) suggest that Google’s web ranking systems also consider user interaction data, like traffic and user behavior signals.

Based on that, you could be forgiven for thinking that your site’s traffic plays an important role in your AI Overview visibility.

But it seems that AI Overviews are more likely to favor text-based signals like web mentions (0.664) and anchors (0.527), over user behavior signals like organic traffic (0.274).

## 4. Ads won’t save you if you want AI Overview visibility

We saw relatively weak correlations between paid efforts and AI mentions:

- Branded ad traffic (0.216)
- Branded ad cost (0.215)

It seems that throwing money at paid search won’t necessarily boost your brand’s AI Overview visibility.

Google does [feature ads in AI Overviews](https://blog.google/products/ads-commerce/google-lens-ai-overviews-ads-marketers/), but our [latest research](https://ahrefs.com/blog/insights-from-56-million-ai-overviews/#AIOs-non-monetized-searches) shows these features aren’t widely monetized yet. As Patrick Stox noted in his analysis:

> What’s more interesting is that 71.67% of the searches with AIOs had no CPC data. This indicates a majority of the AIO searches weren’t monetized at all. It’s no wonder no one has seen ads in AIOs yet. They aren’t showing for the majority of the terms that make Google money.
>
>
>
> Patrick Stox, Product Advisor, [Ahrefs](https://ahrefs.com)

The issue is that AI Overviews are click deterrents–they always seek to provide the answer in-SERP, giving users less incentive to click.

And ads that drive minimal clicks aren’t the most attractive prospect to advertisers.

This may be one reason we haven’t seen many ads in AI Overviews.

But that’s not stopping Google. They have [just expanded search and shopping ads in AI Overviews](https://blog.google/products/ads-commerce/google-search-ai-brand-discovery/).

I expect we’ll start to see stronger correlations between paid search factors and AI Overview brand presence with this development.

## 5. Brands with top web mentions earn up to 10X more AI mentions

We analyzed how branded web mentions correlate with AI Overview brand mentions, broken down by quartiles of web mention frequency.

Brands in the top 25% for “web mentions” (75-100%) average 169 AI Overview mentions—that’s over 10X more than brands in the next quartile down (50-75%), which average just 14 mentions.

Meanwhile, brands in the bottom two quartiles barely register in AI Overviews—averaging just 0-3 mentions.

Putting it another way, if your brand sits in the lower 50% of web mentions, you’re essentially invisible to AI systems.

Just like the [vicious circle of SEO](https://ahrefs.com/blog/backlink-growth-study/), it’s a strong reminder that visibility breeds more visibility.

This is a winner-takes-all scenario. If your brand isn’t being discussed across the web already, it’s likely it won’t be included in AI Overview responses either.

## Track your own brand visibility in search and AI Overviews

Here’s how you can track your own branded search and AI Overview presence, to understand the relationship between your search performance and AI visibility.

### Track your branded mentions in AI Overviews

1. Go to Ahrefs Brand Radar
2. Hit the “Google AI Overviews” tab and search for your brand name
3. Select “keyword OR AI Overview” from the dropdown
4. This will show your total AI Overview ownership, and any growth or decline over time

### Track your branded mentions across the web

1. Go to Ahrefs Brand Radar
2. Hit the “Web visibility” tab and search for your brand name
3. Select the “Total” tab
4. Monitor growth or decline in web mentions over time

### Track your branded keywords and search volume

1. Head to Ahrefs Brand Radar
2. Hit the “Search demand” tab and search for your brand name
3. This will show your branded keywords
4. Select the “Total” tab to monitor any growth or decline in keywords over time
5. Select the “Search volume” tab to track any growth or decline in keywords over time

## What’s next?

If you want to boost your brand’s AI Overview presence, here’s what to prioritize:

1. **Build your web mentions**: With the strongest correlation (0.664), focus on getting your brand discussed across the web. Think: PR, thought leadership, and strategic partnerships.
2. **Encourage relevant brand anchors**: Brand-rich anchor text (0.527) matters significantly. Move beyond “click here” links and make sure publications are linking to you with your brand name in the anchor.
3. **Drive branded search volume**: The third strongest factor (0.392) suggests you should invest in campaigns that get people actively searching for your brand name.
4. **Mind the visibility cliff**: If you’re in the bottom 50% of web mentions, you’re essentially invisible to AI. Prioritize climbing into that top quartile to see any meaningful AI Overview presence.

Engineering brand visibility in AI search is not a perfect science right now, especially as AI Overviews are still technically in the “experimental” phase.

SEO experts [Lily Ray](https://www.linkedin.com/in/lily-ray-44755615/) and [Mark Williams-Cook](https://www.linkedin.com/in/markseo/) have revealed how easily AI Overview visibility can be manipulated [¹](https://www.linkedin.com/feed/update/urn:li:activity:7330539960703332352?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7330539960703332352%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29) [²](https://www.linkedin.com/pulse/google-ai-overviews-have-major-spam-problem-lily-ray-go74f/) [³](https://www.linkedin.com/posts/lily-ray-44755615_the-fact-that-this-works-confirms-the-activity-7328425955507564545-nfSq?utm_source=share&utm_medium=member_desktop&rcm=ACoAABoEm7QBekJrKEnvC5H6nTAmYwOb4R1k5GE) , exposing flaws in the current system.

Further reading

- [LLMO Is in Its Black Hat Era](https://ahrefs.com/blog/black-hat-llmo/)
- [Google Made It So You Can’t Track Clicks From AI Mode](https://ahrefs.com/blog/google-ai-mode-is-here-but-you-cant-track-it-properly/)
- [Insights From 55.8M AI Overviews Across 590M Searches—A Study by Ahrefs](https://ahrefs.com/blog/insights-from-56-million-ai-overviews/)

But the struggle for **enduring** AI visibility that remains after those shortcuts are removed still looks a lot like brand building—because that’s exactly what it is.

Ultimately, building and [measuring your brand awareness](https://ahrefs.com/blog/how-to-measure-brand-awareness/) is key to earning compounding visibility in AI search.
