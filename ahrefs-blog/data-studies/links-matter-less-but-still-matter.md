---
title: "Google Says \"Links Matter Less\"—We Looked at 1,000,000 SERPs to See if It's True"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "links-matter-less-but-still-matter"
url: "https://ahrefs.com/blog/links-matter-less-but-still-matter/"
canonical: "https://ahrefs.com/blog/links-matter-less-but-still-matter/"
author: "Patrick Stox"
published: "2025-01-30T11:01:52+00:00"
updated: "2026-05-28T09:14:43+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "news_or_research"
fetched_at: "2026-06-12T11:45:49+00:00"
status_code: 200
html_hash: "c2fc48e876a66a498c8d6646a6d279bc3e4df8e2538d1f10c5e058f7deab56a7"
clean_word_count: 1146
clean_char_count: 6733
---
# Google Says “Links Matter Less”—We Looked at 1,000,000 SERPs to See if It’s True

Google has said links are less important than they used to be, and most SEOs have come to accept that as true. Our findings indicate that this is true overall, but for certain types of queries, links matter more.

I still believe that links should be a part of your SEO strategy, but they shouldn’t be your whole strategy. A while back, I answered the question, [“Do links still matter for rankings?”](https://ahrefs.com/blog/impact-of-links/) by disavowing all links to a few blogs. Traffic and rankings fell, so yes, links still matter.

![impact of disavowing links](https://ahrefs.com/blog/wp-content/uploads/2025/01/impact-of-disavowing-links.png)

This time, I was curious if the importance of links had changed over time. I also was curious if we could segment the data to see when links matter more, and when they matter less.

Let’s dig in (after a huge thanks to our data scientist [Xibeijia Guan](https://sg.linkedin.com/in/xibeijia-guan) for doing all the hard data parts of this study, and to our CMO [Tim Soulo](https://ahrefs.com/blog/author/tim-soulo/) for his input).

## Methodology and findings

We selected the top 1,000,000 keywords with the most search volume from the US and calculated the [Spearman correlation](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) between their SERPs ranking (top 20) versus different SEO metrics, including:

- Domain rating: **0.131**
- Number of backlinks: **0.248**
- Number of followed backlinks: **0.242**
- Number of refdomains**: 0.255**
- Number of followed refdomains: **0.250**
- Number of internal inlinks**: 0.117**
- Number of internal outlinks: **0.093**
- Number of external outlinks: **0.083**
- If keywords present in URL: **0.034**
- Length of URL: **-0.107**

I want to give all the normal warnings like **Correlation ≠ Causation.** These are generally considered weak correlations or even very weak correlations on the Spearman scale, but that doesn’t mean that these things aren’t important. There are a lot of ranking factors and links do play a role in your rankings.

Here are a few box plots to show the data visually for important metrics. In case you’re seeing box plots for the first time, here’s how you should read them:

The small lines on the edges represent the minimum and maximum values. And 50% of all values fall in the highlighted areas. The line in that area is the median value.

Generally, better link metrics = higher rankings.

## Links matter more at higher search volumes

If we break these down by search volume, we see that links correlate better for searches with higher search volumes.

I see 2 possible explanations, and there’s probably some truth in both:

1. **These queries are likely more competitive**, and you may need links to move the needle for these competitive queries.
2. **These pages get more exposure due to the higher volume**, so higher-ranking sites may naturally get more links.

External links correlated better than incoming internal links. I was surprised at how big of a difference there was here. Links from other sites probably are weighted more or viewed as more credible than the links on your own site.

## Brands get more links

Links correlate better with branded searches than non-branded searches. But I don’t want people to interpret this as links matter more for brands. In my opinion, the correct way to interpret this is that due to the popularity of many brands, they tend to have more links. Their links and #1 rankings skew these results.

The other side of the equation here is that links correlate a little less with non-branded queries for the chart above, which would pull those numbers down a bit. This context is important for a historical comparison below.

## Links correlate to rankings slightly less than they used to

We did [a study](https://ahrefs.com/blog/links-with-traffic-study/) back in 2019 that looked at some of the same correlations.

The methodology was a bit different. It was low volume (2,000–5,000), non-branded queries. I can’t do an exact comparison, but the correlations were higher at the time:

- Links: **0.27**
- Followed links: **0.25**
- Referring domains: **0.29**
- Followed Referring Domains: **0.26**

The current correlations for these metrics and similar queries are 0.22–0.24, and may be slightly lower than that for non-branded terms as I mentioned before.

This is in line with Google comments on links becoming less important and how SEOs perceive them. However, one of the reasons I wanted to run this study is to see how this changes in the next couple years. With the rise of [AI content](https://ahrefs.com/blog/ai-content-is-short-term-arbitrage/), I suspect Google may end up relying on links or other signals more, and may start weighting them higher.

## Links matter a lot more for local queries

Links and RDs correlated at .33 for local queries, which is a lot higher than what we’ve seen and even higher than what we saw overall years ago. I suspect that because content on sites for local service companies is very similar, links make a good differentiator to see which company is popular.

I want to point out that internal links seem to matter a lot more for local queries. I suspect there are fewer external link signals for these queries, so the additional signals from internal links become more important.

## Links matter more for informational content

If we look at the data by search intent, navigational queries have the highest correlation. These are mostly branded, and as I said, brands have more links.

What’s more interesting is that backlinks for informational queries seem to have a higher correlation for rankings than commercial and transactional queries.

I suspect that because competition levels for these terms are high, links may be considered a good signal by Google. It could also be that better content ends up getting more links over time.

## Final thoughts

Links are one part of a bigger ranking puzzle, but you still need to do other things well, like create great content. Where Google has more signals, they may rely less on any one signal. Where they have fewer signals, they may rely more on things like links. In high-competition areas where content may be strong, they also may rely on link signals as more of a differentiator.

The way I view it is that companies, especially local companies, probably should focus on at least foundational links. Larger companies likely already have marketing efforts and content bringing them links, so links may not be as much of a priority. However, when pages for large companies need a push, I’ve seen even internal links give a nice boost.
