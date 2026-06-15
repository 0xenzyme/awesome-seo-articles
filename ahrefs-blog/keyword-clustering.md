---
title: "How To Do Keyword Clustering the Easy Way"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "keyword-clustering"
url: "https://ahrefs.com/blog/keyword-clustering/"
canonical: "https://ahrefs.com/blog/keyword-clustering/"
author: "Joshua Hardwick"
published: "2023-10-31T23:39:04+00:00"
updated: "2023-12-04T08:24:27+00:00"
categories:
  - "Keyword Research"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T11:43:31+00:00"
status_code: 200
html_hash: "ea1901829906b3f3402433d20b24c7fe32839c82b9f284e8a627e19784237c6f"
clean_word_count: 1451
clean_char_count: 8777
---
# How To Do Keyword Clustering the Easy Way

Keyword clustering is the process of grouping keywords with the same or similar intent. You can then target these with one page instead of multiple pages.

![How keyword clustering works](https://ahrefs.com/blog/wp-content/uploads/2023/10/keyword-clustering-explained.png)

Here’s an example of what a cluster might look like:

![Example keyword cluster

These keywords all have the same or similar meaning—so they form a cluster.

Let’s explore how to do it.

## How to do keyword clustering

Keyword clustering is typically done by grouping keywords with the same or similar search results. The idea here is that if Google ranks the same pages for many keywords, they have the same or similar intent and should generally be targeted on the same page.

This is something that would take forever to do manually, but can be done in two quick steps using the right tools.

### 1. Build a list of keyword ideas

If you already have this, skip to [the next step](#step-2). Otherwise, enter a few broad “seed” terms that define your industry into a keyword research tool like Ahrefs’ [Keywords Explorer](https://ahrefs.com/keywords-explorer).

For example, if you sell coffee equipment online, you might enter:

- coffee
- espresso
- cappuccino
- french press
- percolator

Next, head to a keyword ideas report. In Ahrefs, the **Matching Terms** report is the best starting point. It shows all the keywords in our database containing one or more of the “seeds” you entered. In this case, over four million keywords.

![Finding keyword ideas in Ahrefs' Keywords Explorer

You can either work with this keyword list as is or narrow it down to focus on more specific keywords to cluster.

For example, if you’re searching for low-competition keywords, try filtering for keywords with:

- **Low Keyword Difficulty (KD) scores.** These have top-ranking pages with few or no backlinks, so you shouldn’t need to build many links to rank.
- **Low Domain Rating (DR) sites in the top 5.** If sites with similar “authority” to yours are ranking, it’s clear that you don’t need tons of authority to rank.

![Filtering for low-difficulty keywords in Ahrefs' Keywords Explorer

Or, if you’re looking for keywords for an affiliate site, add words like “best” and “review” to the **Include** filter.

![Filtering for keywords containing "best" or "review"

### 2. Cluster them with a tool

In Ahrefs, click the “Clusters by Parent topic” tab while viewing your list of keywords to **instantly** cluster them.

![Instantly clustering by Parent Topic in Ahrefs' Keywords Explorer

You can see the total search volume of all keywords in each cluster, as well as metrics for the Parent Topic like KD score, search volume, and Traffic Potential (TP).

To see the keywords in a cluster, just hit the caret.

![Viewing pages in the cluster

If you’re wondering how we’re able to cluster keywords instantly (unlike other tools), it’s because of the clustering method we use—*by Parent Topic*.

Parent Topic is the keyword sending the most traffic to the top-ranking page.

For example, the Parent Topic for “best moka coffee” is “best coffee for moka pot”:

![Parent Topic for "best moka coffee"

This is because the top-ranking page for “best moka coffee” gets the most traffic from the keyword “best coffee for moka pot.”

If you want to confirm this, plug the top-ranking page for “best moka coffee” into [Site Explorer](https://ahrefs.com/site-explorer) and go to the **Organic Keywords** report. You’ll see that “best coffee for moka pot” sends the most traffic to the page by far.

![The Parent Topic is the keyword sending the most traffic to the top-ranking page

You can also try dedicated keyword clustering tools like [Keyword Insights](https://www.keywordinsights.ai/). These group keywords by comparing the top 10 or 100 search results for your keywords.

I did it for 4,703 keywords and ended up with this pivot table in Google Sheets:

![Result of clustering with Keyword Insights

It took 51 minutes and cost a dollar on the trial. (This could have cost between $24.98 and $45.46 on a paid plan.)

After checking the top 25 clusters, over half were the same as in Keywords Explorer.

There was a lot of overlap between keywords in the clusters, too.

For example, the top cluster in both tools was “best espresso beans.” Keyword Insights put 50 keywords in this cluster vs. 40 in Keywords Explorer. 38 of these keywords were the same across both tools.

Just want to cluster a couple of keywords?

If you just want to know if you should target two keywords on the same page, eyeball the search results for both keywords in Google. If they’re similar, it probably makes sense to cluster them.

If you want to do the same thing faster, use Ahrefs’ [Keywords Explorer](https://ahrefs.com/keywords-explorer).

1. Enter one of the keywords
2. Scroll to the SERP overview
3. Click “Compare with”
4. Enter the second keyword
5. Hit “Apply”

You’ll see a SERP similarity score out of 100 (high = cluster, low = don’t, middle = take your best guess).

Example of two keywords with many similar search results.

Example of two keywords with few similar search results.

## The overlooked benefit of keyword clustering

Keyword clustering has another big benefit: it helps you better understand search intent. This helps you craft comprehensive content that covers more of what searchers are looking for, which often performs better in organic search.

For example, take a look at these keywords in the “best coffee maker” cluster:

![Keywords in the "best coffee maker" cluster

The first few are obvious. They’re just different ways of searching for the same thing.

But look at these:

- best tasting coffee maker
- best coffee maker for home
- best coffee maker for the money

These keywords tell you that searchers want coffee maker recommendations for the home (not business) that make tasty coffee and won’t break the bank.

This is all helpful information for creating content searchers want.

## The drawback to keyword clustering

Results from keyword clustering will never be “perfect.” They’re almost always open to interpretation.

For example, take the keyword “best chocolate cake recipe with coffee.” Both Ahrefs and the keyword clustering tool I tested grouped this under the topic of “chocolate cake.” This happens because there’s some overlap between the results.

![Checking SERP similarity in Ahrefs' Keywords Explorer

That’s right. For some reason, Google ranks a mix of pure chocolate cake recipes and chocolate cake recipes with coffee for this keyword.

![Strange Google results

Because of this, whether you should target both of these keywords on the same page is not obvious.

In cases like these, a closer look at the metrics of the top-ranking pages can help you make a more informed decision.

For example, take a look at the number of linking websites and DR scores of these pages:

![SEO metrics for the top-ranking pages for "best chocolate cake recipe with coffee"

Notice anything?

Yep. They’re both way lower for chocolate cake recipes with coffee than pure chocolate cake recipes.

Here are the stats:

| Pages about: | Average DR | Average Domains |
| --- | --- | --- |
| Chocolate cake recipe | 74 | 318 |
| Chocolate cake recipe with coffee | 33 | 11 |

Based on this, ranking a *chocolate cake recipe with coffee* seems easier than a pure *chocolate cake recipe*. Clustering, as the tools suggested, would probably be a mistake.

## Looking to better understand search trends or find a niche? Try term clustering

Term clustering is where you group keywords by common words or phrases rather than search result similarity. You can do this in Ahrefs’ Keywords Explorer. Just click the “Cluster by terms” tab.

![Clustering by terms in Ahrefs' Keywords Explorer

This is really useful for understanding trends and finding niches.

For example, as you can see above, some of the clusters with the highest volumes for the seed keyword “hotels” are:

- Near
- Beach
- City
- Downtown
- Airport

Immediately, this tells us that many people are searching for hotels near places like beaches, city centers, and airports.

If we then filter that same report for low-competition keywords (low KD, low DR site in top 5), one of the most popular terms is “jacuzzi.”

![Example of a super hot term

If we hit the caret to reveal keywords in that cluster, we see that it’s mainly people searching for hotels with jacuzzis in various locations.

![Trends in keywords within this cluster

Given that the keywords in this cluster have a combined US monthly search volume of 173K, this could be an excellent niche for an affiliate website.

Got questions? [Ping me on ~~Twitter~~ X](https://twitter.com/joshuachardwick?lang=en).
