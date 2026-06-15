---
title: "GSC vs. GKP: Comparing Search Volumes for 72k Keywords [A Study by Ahrefs]"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "gsc-gkp-search-volume-study"
url: "https://ahrefs.com/blog/gsc-gkp-search-volume-study/"
canonical: "https://ahrefs.com/blog/gsc-gkp-search-volume-study/"
author: "Tim Soulo"
published: "2021-11-03T16:00:40+00:00"
updated: "2024-03-18T12:45:02+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:35:15+00:00"
status_code: 200
html_hash: "17113e0b62e05d4d5f71f48b4692d312d0f2cd0545803a2accec70ec11052c07"
clean_word_count: 1472
clean_char_count: 8538
---
# GSC vs. GKP: Comparing Search Volumes for 72k Keywords [A Study by Ahrefs]

There are two sources of keyword search volume data that come directly from Google: Google Search Console (GSC) and Google Keyword Planner (GKP). We decided to compare the numbers between the two and see how much they align.

GSC is widely considered the “single source of truth” for accurate keyword data because it shows you the exact number of times your page appeared in Google’s search results for a specific keyword.

So if your page consistently ranks on the front page of Google for a given search query, the number of impressions for that query in GSC should accurately reflect the search volume (in most cases).

As for GKP, its search volume data is known to be a lot less precise. Mainly because:

- It groups keywords with similar meaning.
- It rounds search volumes into buckets.

And yet, a lot of SEO professionals are perfectly happy with the search volumes they get from GKP and consider them to be accurate.

So we decided to run a little experiment and study how search volumes from GKP stack up against the “single source of truth,” aka GSC.

## Comparing search volumes between GSC and GKP

For this experiment, we took 72,635 random keywords in the 1K to 10K search volume range. Then we compared the number of “impressions” in GSC with the search volume data from GKP (for the same month).

The first thing we found is that GKP almost always overestimates “true” search volume:

But the real question is by how much? After all, if it only overestimates search volumes slightly, then what’s the big deal?

Here’s the answer:

Most search volumes in GKP (54.28%) are overestimations, while just under half (45.22%) are roughly accurate (i.e., deviating from GSC “impressions” by no more than 50%).

For the SEO nerds among you, here’s a more granular view of how GSC data compares to GKP:

Quite a discrepancy, right?

So why don’t we dig a little deeper and investigate the actual causes of such a stark difference in search volumes between GKP and GSC?

## GKP groups keywords with similar meaning (and makes mistakes)

According to our GSC data, the keyword *“ahrefs”* got 25,436 impressions in June (in the U.S.):

But if we look at the data from GKP for the same month, it shows a search volume of 33,100:

This means that the “GKP/GSC” ratio for this keyword is **1.3x**. Not too bad, but not very accurate either.

So what is causing this discrepancy?

Apparently, the GKP search volume for the keyword “ahrefs” includes the search volumes of all its misspellings that we can see in our GSC:

- ahref (2,826 impressions)
- hrefs (906 impressions)
- aherfs (435 impressions)
- arefs (267 impressions)
- a hrefs (224 impressions)
- aherf (185 impressions)
- ahrfs (100 impressions)
- etc

We know this because [GKP groups them together](http://www.thesempost.com/googles-keyword-planner-now-combines-keywords-for-search-volume/) (and shows the same search volume that it shows for “ahrefs”):

But when a keyword’s search volume accounts for its misspellings, it’s not that big of a deal, right? In fact, it can actually be quite useful.

Well, there are some cases when GKP is grouping things that should not be grouped. And this can be misleading for us SEOs.

For example, the keyword “chusky” has a search volume of 550k in the U.S. GKP thinks that it’s a misspelling of “husky” because those two keywords are being grouped together:

But if you look at the search results for the keyword “chusky,” you’ll instantly see that it’s not a misspelling. Rather, it’s a unique dog breed, meaning that it should have a distinct search volume of its own.

Same story with these four keywords: “red room,” “red rose,” “red rock,” and “red robin”:

GKP treats them as one, but you don’t even have to check the search results to know that these things are not the same.

A few more examples:

- american banks & bank of america
- mosquito bites & mosquito bits
- book a driver & drive book

In all honesty, these kinds of “false groupings” are not common, but they may cause you lots of headaches should you stumble across one of them.

What’s a lot more common (and irritating) is that GKP doesn’t show distinct search volumes for closely related search query variations.

For example, the following search queries are grouped together in GKP with no way to see individual search volumes:

- comparing vpns
- compare vpn
- comparison vpn
- compare vpns
- vpns compared
- vpn compare
- vpn comparison
- vpn comparisons

This “grouping” issue is then being picked up by every SEO tool that pulls its search volume data from GKP (and nearly all of them do that).

But here at Ahrefs, we mix keyword data from multiple sources (including many years of historical clickstream data). This allows us to “un-group” search queries and show the distinct search volume for each variation:

Knowing the distinct search volume of each individual search query prevents you from accidentally overestimating a topic’s total search traffic potential when summing the search volumes of all keywords in a group.

Other than that, knowing the most popular ways of how people phrase their search queries can help you adjust the language of your page accordingly and come up with a more eye-catching page title.

As you can tell, this “grouping” feature in GKP can be frustrating for us SEOs. But it’s not like we can blame GKP for hiding precise search volumes from us. GKP is a tool for advertisers, not SEOs. And this grouping of similar keywords is actually convenient for them.

## GSC shows local impressions for search queries with local intent

According to GKP, the keyword “golf courses” has an impressive average monthly search volume of one million in the U.S.:

But here’s the thing. Depending on the location of where you’re searching from, you’ll see different pages ranking for this keyword:

- If you search from **Rochester**, you’ll see a page from **visitrochester.com** at #2.
- If you search from **Bakersfield**, you’ll see a page from **visitbakersfield.com** at #1.

Thus, the owners of these two websites will see a different number of monthly impressions for the keyword “golf courses” in their GSC. That’s because each website ranks well for this keyword only in a specific location.

And only the owner of a huge website like **golflink.com** (which seems to have pages ranking for “golf courses” in every conceivable location) would likely see the number of impressions that is close to the 1 million that GKP shows us.

These “regional” keywords quite often have the biggest discrepancy (**4x+**) between GKP and GSC numbers, which can be seen in our graph above.

## “Impressions” in GSC are sometimes inflated by bot traffic

Let’s talk about those rare cases where GSC shows a higher search volume than GKP.

We believe that it likely happens because of the bot traffic. According to John Mueller, not all of the impressions from bots are filtered in GSC:

But what is “bot traffic?”

Well, that is any kind of script or software program that does automated searches in Google.

The “bots” that I’m sure you’re familiar with are [rank trackers](https://ahrefs.com/blog/best-rank-tracker/) that make automated searches in Google to report where your website ranks.

A much nastier example is bots that generate fake clicks on Google ads to put some pressure on their competitors.

Anyhow, according to our study, GSC data seems artificially inflated in only 0.5% of cases. So it’s unlikely that you will suffer much from bots polluting your GSC reports.

## How does Ahrefs’ search volume data stack up?

I’m sure some of you are wondering how Ahrefs’ search volume data compares.

Well, let’s plot “Ahrefs/GSC” ratios right next to “GKP/GSC” ratios from the previous graph:

It looks like Ahrefs shows “roughly accurate” values in 60% of cases vs. 45% of cases for GKP.

That is mostly due to our ability to “un-group” clusters of similar keywords and report distinct search volumes for each of them.

So if you were wondering why the search volumes in Ahrefs are not the same as those in GKP, now you know that is by design.

## Final thoughts

I hope you enjoyed this research study and that it gave you a better understanding of how the numbers in GSC and GKP differ and, more importantly, *why* they differ.

Have questions? Ping me [on Twitter](https://twitter.com/timsoulo).

And by the way, **huge thanks** to our awesome data science team for carving out some time in their busy schedules to help me with this research.
