---
title: "What We Learned From Studying Our Own \"AI Proof\" Keywords"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "ai-proof-keywords"
url: "https://ahrefs.com/blog/ai-proof-keywords/"
canonical: "https://ahrefs.com/blog/ai-proof-keywords/"
author: "Louise Linehan"
published: "2025-07-23T09:00:05+00:00"
updated: "2026-05-31T08:26:46+00:00"
categories:
  - "AI Search"
  - "Data & Studies"
freshness_reasons:
  - "news_or_research"
fetched_at: "2026-06-12T11:14:28+00:00"
status_code: 200
html_hash: "db978a58cdd3ba90aca20d4dcf3b52b04b4835a554fe9cee4c05c1efd80fef85"
clean_word_count: 1116
clean_char_count: 6697
---
# What We Learned From Studying Our Own “AI Proof” Keywords

Ever since AI Overviews began decimating clicks in organic search, I’ve had two questions on my mind: “What kind of AI Overview keywords still drive clicks?”, and “Is there a way to engineer more clicks from zero-click search?”

I asked our ace data scientist, [Xibeijia](https://sg.linkedin.com/in/xibeijia-guan), if she could help me build a profile of “AI proof keywords”.

By “AI proof keywords” I mean queries that keep (or increase) their clicks, even when AI Overviews are present in the SERP.

Xibeijia ran a small-scale study on Ahrefs’ keywords to find out.

Read on to see what she found…

## AI Overviews usually reduce clicks

AI Overviews tend to steal clicks.

Google now fields questions natively in the search results using AI, meaning that users don’t always need to click through to websites to find an answer.

[Ryan Law](https://uk.linkedin.com/in/thinkingslow) and [Xibeijia Guan](https://sg.linkedin.com/in/xibeijia-guan) ran a (now famous) study back in April into the [CTR impact of AI Overviews](https://ahrefs.com/blog/ai-overviews-reduce-clicks/).

They found that pages lose 34.5% CTR, on average, when the AI Overview is present on the SERP.

![Ahrefs AI Overview CTR study showing a CTR loss of 34.5% as a result of AI Overview presence](https://ahrefs.com/blog/wp-content/uploads/2025/07/word-image-190141-1.png)

But, what about the keywords that *don’t* experience a CTR drop—what do they look like, and do they have anything in common?

## Profiling our own “AI proof keywords”

Xibeijia ran a very small-scale check on [ahrefs.com](https://ahrefs.com) to see if we could learn anything from our own “AI proof keywords”.

It involved:

1. Heading to the Keyword report in Google Search Console via Ahrefs
2. Finding US keywords with 0-100% increase in CTR
3. Setting a date filter for March 13th (this is when [AI Overviews doubled](https://ahrefs.com/blog/ai-overview-growth/), following the March Core Update)
4. Applying the filter “impressions >= 100”
5. Adding those keywords to a keyword list
6. Filtering that list based on whether AI Overviews were present on the SERPs

Google Search Console performance in Ahrefs Dashboard

In total, 97 out of 1,393 keywords (~7%) also ranked in a SERP topped with an AI Overview.

As I said, the study was pretty small fry.

But, even so, Xibeijia spotted some interesting patterns in the data.

The keywords that saw *stable* or *increased* CTR fell into three categories:

### 1. They were “free tools” keywords

Xibeijia noticed that our “free tools” keywords didn’t experience as much of a CTR decline, despite growing AI Overview presence.

Meaning that utility pages like our [Website Traffic Checker](https://ahrefs.com/traffic-checker) and our [Free Keyword Generator](https://ahrefs.com/keyword-generator) still caused users to click.

[Zero-click search](https://ahrefs.com/blog/zero-click-search/) summaries weren’t enough for users in this situation—they had a job-to-be-done, and they required a tool to do it—which meant they needed to click.

Ahrefs SERP Overview in Keywords Explorer showing Ahrefs’ free tool—Traffic Checker—losing one organic position, but gaining an AI Overview citation, giving us two chances for clicks.

### 2. They didn’t rank originally

Some keywords didn’t rank on page one originally, but began ranking in the top 10 or in an AI Overview post-March 13th.

This reaffirms the importance of SEO.

If you optimize your content well, it *is* still possible to improve CTR in AI Overview SERPs—though some industries and content types will likely fare better than others.

Ahrefs SERP Overview in Keywords Explorer showing one of Ahrefs’ “Top Websites” pages claiming position 7 and an AI Overview.

### 3. They appeared in SERPs where AI Overviews ranked below position one

As [Patrick Stox](https://www.linkedin.com/in/patrickstox) shared recently on the Ahrefs blog, [AI Overviews aren’t always in the first position in the SERPs](https://ahrefs.com/blog/ai-overviews-positions/)—they can actually rank in positions one through six.

In fact, ~8.5% of the time they’re not in position one.

In our study, we saw either **click-parity** or **click-growth** across SERPs where AIOs ranked lower than position one.

In other words, our data indicates that when AI Overviews are not in position one, they don’t take as many clicks away.

Ahrefs SERP Overview in Keywords Explorer showing one of Ahrefs’ “Top Websites” pages climbing one ranking in a SERP where the AI Overview ranks in position 6.

This is something we’re going to be testing in more detail, so watch out for an AI Overview position CTR study on our blog.

## How to recreate this analysis using Ahrefs

First off, head to:

1. Dashboard
2. Projects
3. Google Search Console
4. Find your project

Then head to:

1. Keywords report
2. Select a region
3. Set an impression threshold (e.g. >100)
4. Set a positive CTR range (e.g. 0–100) and select “Improved”

Export those keywords, open them in a spreadsheet, and copy all.

Then go to:

1. Keywords Explorer
2. Paste in your list
3. Choose the same region
4. Apply a “SERP Feature” filter
5. Choose “Include > AI Overview”

Finally, apply the filter “Target > [enter your domain] > show ranking positions”.

This will show you your “AI proof” keywords—the ones retaining or gaining clicks, despite the presence of AI Overviews.

Check back on this report to see which types of keywords you can target to engineer more clicks.

## Wrapping up

AI Overviews have undeniably changed the search landscape—often to the detriment of organic CTR—but our small-scale study shows that some keywords continue to drive clicks.

So, what makes a keyword “AI proof”? In our dataset, three factors stood out:

- **It promotes free tools:** Utility-driven queries (like “free tools”) compel clicks—summaries alone aren’t always enough.
- **It didn’t rank highly to begin with:** Ranking improvements still boost CTR—even in AI-dominated SERPs.
- **It has AIOs in lower positions:** When AIOs don’t occupy the top slot in the SERPs, your page has more breathing room.

Even in zero-click search, some keywords still click.

So carry on tracking your keyword performance, and keep an eye on where AI Overviews appear in your SERPs.

Further reading

- [8.64% of AI Overviews Appear Outside Position #1 (And as Low as Position #6)](https://ahrefs.com/blog/ai-overviews-positions/)
- [Welcome to Zero-Click Search. Please Leave Your Traffic at the Door.](https://ahrefs.com/blog/zero-click-search/)
- [The Great Decoupling (or Why Your Clicks Are Down and Impressions Up)](https://ahrefs.com/blog/the-great-decoupling/)
