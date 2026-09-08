---
title: "Google Doesn’t Punish AI Content; It Punishes Bad Content (331k Pages Studied)"
source: "ahrefs-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "google-doesnt-punish-ai-content"
url: "https://ahrefs.com/blog/google-doesnt-punish-ai-content/"
canonical: "https://ahrefs.com/blog/google-doesnt-punish-ai-content/"
author: "Ryan Law"
published: "2026-07-27T08:00:13+00:00"
updated: "2026-07-27T08:33:17+00:00"
categories:
  - "Content Marketing"
  - "Data & Studies"
  - "General SEO"
freshness_reasons: []
fetched_at: "2026-09-08T09:16:40.886942+00:00"
status_code: 200
html_hash: "1bad0613bd0e1bfb735052d36700e45fcb02afc801753737843dd1e4e9c40fa2"
clean_word_count: 2059
clean_char_count: 12199
---
# Google Doesn’t Punish AI Content; It Punishes Bad Content (331k Pages Studied)

I still have plenty of questions about how Google treats AI-generated content.

![Quotation marks](/assets/esbuild/quotation-marks-6PWBEG7B.svg)

Automation has long been used in publishing to create useful content. AI can assist with and generate useful content in exciting new ways.

On the other hand, people like [Lily Ray](https://lilyraynyc.substack.com/p/it-works-until-it-doesnt-ai-content-risks) and [Glenn Gabe](https://www.gsqi.com/marketing-blog/when-mt-ai-crumbles-chatgpt-follows/) have shared many examples of so-called “mount AI” traffic graphs: websites that scaled content creation with AI, saw a heroic spike in rankings and traffic… and then watched their organic performance tank a few months after publication.

An example of a "Mount AI" traffic graph from Lily's article.

Many marketers are now unwilling to use generative AI in *any* capacity for fear Google will punish them. But is Google punishing these websites for using AI content? Or is their AI use incidental to the fact that they’re making spammy, scaled content?

We set out to answer four questions that might shed some light on the issue:

- Are there any fully AI-generated pages in top-ranking positions?
- How common is AI-generated content throughout the top 10?
- Does Google index content with a very high likelihood of being AI?
- Does the organic performance of AI-generated content tank within a few months?

Based on this research, I believe that Google is not against AI content; it is against bad content, but confusion arises because AI content and bad content overlap a significant amount of the time.

- **5.3% of top-ranking (positions 1–3) pages are 100% AI-generated**, and 9% are ≥80% AI content—so fully AI-written pages can and do rank at the very top.
- **Pages with under 50% AI content account for 82.2% of top-3 rankings**, meaning heavily AI-generated content is still a minority at the top.
- **Every position in the top 10 contains a meaningful share of heavily AI-generated pages**: between 8.4% (position 1) and 11.7% (position 10) of pages have ≥80% AI content.
- **Average AI content level rises only slightly from position 1 (27.1%) to position 10 (30.9%)**, and the median tells a similar story, climbing from 17.1% to 19.5% over the same range.
- **Indexation rate drops from 49.28% for low-AI-content pages to 40.35% for very-high-AI-content pages**: a meaningful but far from disqualifying gap.
- **Even in the very-high-AI-content bucket, 40% of pages were still indexed**, showing no binary block on AI-generated content entering the index.
- **Low and moderate AI-content pages received 2–3x the organic impressions of high or very-high AI-content pages**, the starkest performance gap found in the study.
- **High and very-high AI-content pages showed similar, stable impressions over time** with no precipitous drop-off.

This research uses Ahrefs AI content detector, which Ahrefs customers can use via [Site Audit](https://ahrefs.com/site-audit) and the **Top pages** and **Page inspect** reports in [Site Explorer](https://ahrefs.com/site-explorer).

AI content levels indicate the estimated percentage of AI-generated text on the page, ranging from low (<20%) to very high (≥80%). For greater accuracy, AI detection only triggers on pages at least 350 words in length.

Importantly, AI content detection is not perfect, and the way we detect AI content will be different from how Google does (*if* it does).

In the same way that an LLM uses probability to generate text, AI detectors use probability to classify it. This type of research is, in my opinion, the best way to use AI content detection: looking at large-scale datasets and directional trends, and not fixating on individual articles and their AI content.

We analyzed 1,000,000 pages pulled from the top 10 positions in 100,000 SERPs in June 2026. Around 300,000 of these pages were available in our crawler database, of which 150,000 contained enough page content for AI detection.

We found that the majority of top-ranking pages are predominantly human-written. 54.7%—over half—have less than 20% AI content. Together, pages with under 50% AI content account for 82.2% of top-3 rankings.

But although our data suggests that higher AI use is correlated with lower ranking positions, it also suggests that it *is* possible for fully AI-generated content to rank in positions 1-3.

Fully or near-fully AI-generated pages are a small minority, but they certainly exist in this sample: **9% of top-ranking pages are ≥80% AI content**, and **5.3% are 100% AI-generated**.

Here’s how the data breaks out:

- 5.3% of top-ranking pages returned an AI content level of 100%.
- 9.0% of top-ranking pages returned an AI content level of ≥80%.
- 8.8% of top-ranking pages returned an AI content level of 50-80%.
- 27.5% of top-ranking pages returned an AI content level of 20-50%.
- 54.7% of top-ranking pages returned an AI content level of <20%.

But what about the rest of the SERP?

Looking at the distribution of AI-generated content across the top 10 positions, highly AI-generated content gets rarer as you move higher in the SERP.

Position 1 has the highest share of low-AI-content pages and the lowest share of very-high-AI-content pages:

But there is a gentle gradient: the prevalence of AI-generated content gets gradually rarer moving from position 10 to 1, in relatively small increments.

Every ranking position, including position 1, still contains a meaningful share of heavily AI-generated pages: between 8-12% containing ≥80% AI content.

We also calculated the average and median AI content level across a sample of 15,000 pages for each position. It’s a similar story: AI content becomes more common further down the SERP, but still appears in higher positions:

Analysing ranking pages introduces a type of selection bias: we are only evaluating successful URLs that Google has already deemed fit for indexing. But does AI use reduce the chance of a URL being indexed in the first place?

We looked at the indexation rates for buckets of pages with different AI content levels. We sampled 1,000,000 pages from our crawler database, 1 page per domain. Around 100,000 pages contained enough content for AI detection. We counted a page as indexed if it had **any** of the following traits:

- At least one identifiable organic keyword ranking, or
- At least one GSC impression since January 2026, or
- An exact URL hit for a Google site: search.

If we bucket pages by their estimated AI content level, we can see that higher AI content levels correlate with lower indexation rates:

Here’s how the data breaks out by bucket:

- Pages with low AI content level had an indexation rate of 49.28%
- Pages with moderate AI content level had an average indexation rate of 43.38%
- Pages with high AI content level had an average indexation rate of 40.72%
- Pages with very high AI content level had an average indexation rate of 40.35%

While the indexation rate is lower for content with high or very high AI content levels, a full **40% of these pages were still indexed**—not a million miles away from the 49% indexation rate of low AI content.

Finally, we wanted to see how the organic performance of AI-generated pages trended over time relative to non-AI-generated pages.

To do this, we used GSC data from live URLs, matched those URLs with our crawler database, filtered out pages with too little text for AI detection, and then bucketed the URLs by their estimated AI content level. This left us with the following samples:

- **Low AI content level:** 28,643 pages
- **Moderate AI content level:** 23,498 pages
- **High AI content level:** 12,911 pages
- **Very High AI content level:** 15,809 pages

For each bucket, we used GSC data to plot the change in impressions over time, starting with one panel of websites from June 2025 to January 2026…

…and a second panel of websites from January 2026 to June 2026:

Organic performance is obviously influenced by many, many factors, and there are few concrete conclusions we can draw from this limited time window, but I thought the data was interesting for a few reasons:

- Generally, AI content use seems **negatively correlated** with impressions.
- Low and moderate AI level content received **2–3x the impressions** of high or very high AI-generated content.
- High and very high AI-generated content both received **similar impressions** across both samples.
- There are no obvious precipitous **drops in impressions** for highly AI-generated content.

There are many reasons why AI-generated content might earn fewer impressions, so it would be wrong to assume that there is any kind of automatic suppression happening. Sites that lean heavily on AI content may tend to be newer or lower-authority in the first place; inversely, sites with good organic performance may be disincentivized to publish AI content.

Most likely, in my opinion, is that **increasing use of AI correlates with decreasing content quality**. I think this is the key to understanding how Google treats AI content.

Throughout this research, AI use seems to be correlated with lower performance in search: lower impressions, lower ranking position, and lower indexation rate.

But this doesn't tell the entire picture. AI-generated content is found in significant amounts in every ranking position, including the top 1 to 3. A significant amount of AI-generated content is successfully indexed. Impressions to AI-generated content remained relatively stable over time.

There are no obvious hard cutoffs suggesting a binary AI classifier is preventing AI-generated pages from ranking highly or making it into the index. Instead, we see a gradual gradient: performance generally worsens with increasing AI use… probably because **content quality** generally worsens with increasing AI use.

As I've [said before](https://www.linkedin.com/posts/thinkingslow_does-ai-content-work-is-entirely-the-wrong-share-7470769355325161474-Qb0W/), when companies engage in an AI content strategy, they are often engaging in a strategy that is very different from traditional content creation and SEO—different and *worse* in many ways. Basic AI content often:

- Repeats common knowledge without adding any new information to the SERP.
- Fails to include internal and external links, images, visual interest, and first-person experiences.
- Relies on tedious academic-style writing.
- Contains obvious mistakes and inaccuracies.

These are all problems that could markedly worsen the organic performance of *any* piece of content, but they are *especially* common in most AI-generated content. As Dan Taylor explained in his great [SEJ article](https://www.searchenginejournal.com/scaled-ai-content-often-fails-googles-crawl-economics-explain-why/581325/) recently, publishing this content at scale is the perfect recipe for your very own "Mount AI" situation, as Google “burst-crawls” new low-quality, AI-generated pages but dumps them from the index soon after:

![Quotation marks](/assets/esbuild/quotation-marks-6PWBEG7B.svg)

Google might initially burst-crawl the new setup out of curiosity. But, if the domain lacks the baseline authority to sustain that scale, Google will throttle its resource allocation. Just because Google gives you the resources to index your pages initially, it does not mean it will grant them to you indefinitely.

I don't think Google is trying to punish AI-generated content; I think it is relying on the same old hallmarks of content quality that it always has. It's just that AI-generated content is usually lower quality than human-generated content.

Crucially, these quality problems commonly co-occur with AI use, but they are not guaranteed by AI use—as shown by the not-insignificant number of indexed and top-ranking AI-generated pages. I know from [firsthand experience](https://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/) that it is very possible to create detailed, interesting, well-researched content using AI generation—the caveat being that most people do not. *Yet.*

I don't believe marketers and SEOs should be scared of AI content creation—but they should be scared of spam and scaled content.
