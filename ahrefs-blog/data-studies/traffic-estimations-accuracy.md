---
title: "How Accurate Are the Search Traffic Estimations in Ahrefs? (New Research)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "traffic-estimations-accuracy"
url: "https://ahrefs.com/blog/traffic-estimations-accuracy/"
canonical: "https://ahrefs.com/blog/traffic-estimations-accuracy/"
author: "Tim Soulo"
published: "2022-05-03T12:02:35+00:00"
updated: "2022-10-20T15:04:27+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-12T12:13:37+00:00"
status_code: 200
html_hash: "579246fcd17be275abd6f46b4411266d2a5d4c3d67464320ca9e005f9fb1291b"
clean_word_count: 1052
clean_char_count: 6040
---
# How Accurate Are the Search Traffic Estimations in Ahrefs? (New Research)

One of the most common use cases of Ahrefs is to check how much organic search traffic a given website (or webpage) gets.

It is widely known that the search traffic numbers in Ahrefs are merely estimations. But how far do they deviate from the actual traffic numbers?

We decided to run a small study and try to quantify that.

## What to expect from Ahrefs’ traffic estimations

Before I share the results of our study with you, I think it is quite important that you understand how Ahrefs traffic estimates are calculated in the first place.

Here’s what it looks like in a nutshell:

1. Take all keywords that a website ranks for
2. Pull the monthly search volume of each keyword
3. Look up that website’s ranking position for each keyword
4. Predict the CTR for each of their search snippets
5. Sum up clicks from each keyword and compute the total estimated monthly search traffic

Can you tell at which step the discrepancies kick in? (Hint: each one)

- **Keywords** – It is practically impossible to know *all* the keywords that a given website is ranking for.
- **Monthly search volumes** – These aren’t particularly precise either (see [our recent study](https://ahrefs.com/blog/gsc-gkp-search-volume-study/)).
- **Ranking positions** – The SERPs are very volatile. Today, your page ranks #3; a day later, it ranks #4.
- **CTR** – It is incredibly hard to predict the CTR of a page on a SERP. There are just too many factors to consider: search intent, ads, SERP features, brand affinity, etc.

As you can tell, the data that we *(or any other SEO tool)* use for computing the search traffic estimations has many issues that are nearly impossible to fix. And these issues inevitably affect the quality of the resulting traffic estimations.

And yet, even though our traffic estimations may deviate from the actual data quite a bit, they’re still good enough to be of immense value for digital marketing professionals of all kinds.

Especially so when one understands how these values are being computed (which you do now) and can, therefore, factor in some level of discrepancy while using that data (more on that later).

So that aside, let’s finally see the results of our research.

## How accurate are Ahrefs’ search traffic estimations?

This very study is inspired by the good folks at [AuthorityHacker](https://www.authorityhacker.com/). They recently performed research comparing the quality of search traffic estimations from six different SEO tools.

In their study, Ahrefs turned out to be the winner *(with an average discrepancy of 22.5% and 0.99 correlation with GSC data).*

But that study was done on a small sample of just 50 websites. So we decided to replicate it on a larger scale and see how the numbers change.

In our study, we took 1,635 random websites and compared their monthly GSC traffic in the U.S. to their monthly U.S. organic traffic estimates in Ahrefs.

We studied the same two factors:

1. How much Ahrefs’ traffic estimations deviate from GSC
2. How consistent our traffic estimations are when compared to GSC

### Deviation

In our studied sample of 1,635 websites, the median deviation turned out to be **49.52%**.

In other words, most of the time you can expect Ahrefs to misreport a website’s U.S. traffic by up to half of its value.

This may seem like a lot. But in reality, the margin of our error largely depends on the type of website and the industry the site is in. For some websites, we are off by less than 5%. For some others, we can be off by more than 1,000%.

But more often than not, our estimates are rather good:

To put our median deviation of **49.52%** in perspective, we also calculated it for SEMrush, and it turned out to be 68.36%.

### Consistency

Here’s what the “consistency” of traffic estimations refers to:

If one website gets more traffic than the other website (according to GSC data), that should hold true when looking at Ahrefs’ data (regardless of the accuracy of the estimates).

As you may have already guessed, this can be studied by calculating the good old [correlation](https://en.wikipedia.org/wiki/Correlation) between the two sets of values.

In our sample size of 1,635 websites, the monthly GSC traffic in the U.S. correlated with that of Ahrefs’ at **0.76** (Pearson’s). This means that the above statement will hold true in the vast majority of cases.

Sidenote.

In case you’re unfamiliar with correlations, “1” means that the two sets of values are in perfect sync. And 0.76 is pretty close to 1.

As for SEMRush, theirs was 0.74 for the same set of websites.

## A workaround for manually fixing the discrepancy

As you just learned, Ahrefs can be off by a rather considerable amount when estimating a website’s traffic. But at the same time, it is highly consistent in its traffic estimations. Even more so if the websites you’re comparing belong to the same industry.

What this means is that you can better estimate the actual search traffic of your competitors by using this simple formula:

The relationship between GSC traffic and Ahrefs traffic for your own website should hold roughly true for your competitors’ (given that they’re in the same niche as you). So more often than not, using this formula should produce a pretty accurate result.

## Final words

Hopefully, this helped you folks understand what you can expect from Ahrefs’ search traffic estimations and how to work around the discrepancy to get much more accurate data.

But most important of all, the results of this research will now serve as a reference point for our product team on our quest to further improve the accuracy of our estimations. Even though it is technically impossible to make them perfect, there’s still quite a bit of room for improvement—which we can try to address.

As always, should you have any comments or questions, you can find me [on Twitter](https://twitter.com/timsoulo).

P.S. Big thanks to Alex from our Data Science team for helping me with this.
