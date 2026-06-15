---
title: "Do Links From Pages With Traffic Help You Rank Higher? [Ahrefs Study]"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "links-with-traffic-study"
url: "https://ahrefs.com/blog/links-with-traffic-study/"
canonical: "https://ahrefs.com/blog/links-with-traffic-study/"
author: "Tim Soulo"
published: "2019-02-19T12:24:21+00:00"
updated: "2025-12-18T14:09:24+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:45:50+00:00"
status_code: 200
html_hash: "563bbe95ea3efe4e23efc4f28e6042a9869eaaae0bd55cf7f819c5142ccae723"
clean_word_count: 1517
clean_char_count: 8907
---
# Do Links From Pages With Traffic Help You Rank Higher? [Ahrefs Study]

Ever since members of the SEO community got their hands on [Google’s Reasonable Surfer patent](http://www.seobythesea.com/2016/04/googles-reasonable-surfer-patent-updated/), there’s been no shortage of arguments about the value of links from pages with traffic.

Some believe they’re worth more than those from pages without traffic, and others don’t.

This debate is so prevalent that whenever I find myself in a group of like-minded people discussing the value of different kinds of links, I will inevitably get asked:

> Tim, you guys have the best link data at Ahrefs, why don’t you crunch some numbers and give us a definitive answer to this question based on hard cold data?

And I started to hear that question even more after we released [search traffic data for referring pages](https://ahrefs.com/blog/backlinks-and-traffic/) last year.

Use the Backlinks report in [Site Explorer](https://ahrefs.com/site-explorer) to see the estimated organic traffic for each referring page.

Long story short, I recently managed to carve out some time for our data science team to study this.

But before I share the results, I want to be transparent about our data and its limitations.

## Is our data flawed?

Let me first reiterate the fact that [correlation does not prove causation](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation).

That’s something to keep in mind when looking at any “[Google ranking factor](https://ahrefs.com/blog/google-ranking-factors/)” study as they all analyze how a particular ranking factor correlates to Google ranking position.

It’s also important to note that:

1. **We only know the organic search traffic of referring pages.** This study doesn’t take into account any traffic sources except for organic. That means no direct, referral, social, or paid traffic.
2. **Our search traffic numbers are estimations.** Sometimes these are unbelievably accurate. Other times we can easily be off by 3-7x ([read this post](/blog/ahrefs-seo-metrics/) to learn more about how we calculate search traffic at Ahrefs).
3. **We don’t predict link clicks.** As Bill Slawski [states](http://www.seobythesea.com/2016/04/googles-reasonable-surfer-patent-updated/), the idea behind [Google’s “reasonable surfer” model](http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1=9,305,099.PN.&OS=PN/9,305,099&RS=PN/9,305,099) is to rank web pages “based upon a probability that a person following links at random on the web might end up upon a particular page.” However, the patent relates mostly to the position of a link on a given page. Nowhere does the patent mention traffic.

Which begs the question: If the study is flawed from the start, why even bother?

I see at least three reasons:

1. Because quite a few people in the SEO community want us to do it;
2. Because someone might later build upon this study (we’ll be glad to help you);
3. Because we can.

I’m also interested to see if our somewhat “flawed data” can still help uncover any interesting anomalies.

Now with that aside, let’s see what the numbers say.

## Study 1: Backlinks from pages with organic traffic vs. rankings

We took 44,589 (non-branded) keywords with monthly search volumes between 2,000 and 5,000, pulled the top 10 ranking pages for each, and studied how well the following metrics correlate ([Spearman](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)) with each page’s ranking position:

Honestly, I expected the number of links from pages with traffic to have a stronger correlation than the total number of links. But that didn’t happen.

Sidenote.

SERPs where no pages had at least one backlink with traffic were excluded from our sample when calculating the correlation for the number of backlinks from referring pages.

Here are a couple of interesting observations though:

Firstly, the correlation for the number of “dofollow” backlinks is a little bit weaker than that of the total number of backlinks. This **could** be an indication that Google values **some** nofollowed links from strong pages more than followed links from weak pages. **#whoknows**

Or the result could merely be because we didn’t study the factor in isolation.

Secondly, the sum of organic traffic to referring pages has a higher correlation than the number of referring pages with traffic. This suggests that our threshold of 100+ visits is arbitrary and that links from “powerful” referring pages (in terms of how much search traffic they get) have more weight than links from pages with “a bit” of search traffic.

Interestingly, [URL Rating (UR)](/blog/ahrefs-seo-metrics/) is the strongest correlating factor of all, which indicates that the way Ahrefs calculates the “link popularity” of a page correlates nicely with the ability of that page to rank high in Google.

## Study 2: Backlinks from domains with organic traffic vs. rankings

After studying the correlation of referring pages with search traffic, we decided to do the same for referring domains with traffic.

Here’s what we got:

Perhaps the most striking observation here is that the number of referring domains with traffic didn’t correlate higher than the total number of referring domains. That’s quite surprising.

It’s the same story when it comes to the sum of traffic to referring domains vs. the total number of referring domains. There’s virtually no difference in the correlations, so it seems that the amount of organic traffic to a referring domain has little impact on the value of a link.

If you think about it, that makes total sense.

I mean, which of these two links would you rather have? -

1. A link from a page with tons of backlinks on a domain with little organic traffic
2. A link from a page buried deep on a massive website with tons of organic traffic

Hopefully, you said #1.

All that said, it’s important not to forget about our data limitations and caveats:

1. [Correlation ≠ causation](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation);
2. The threshold of 1,000 visits/month for the number of referring domains with traffic is an arbitrary one.

In other words, take the observations above with a large pinch of metaphorical salt.

Speaking of pinches of salt, you might be wondering:

## How common are “links with traffic” across the studied SERPs?

The above correlations are based on a study of 44,589 SERPs.

But how many of those SERPs had results with links from referring pages with traffic?

It looks like “links with traffic” aren’t too common among the top-ranking pages.

There were only 20 SERPs where all the top ranking pages had at least one link with traffic. That’s one in every 2,229.

Furthermore, for roughly 1/5th of SERPs, none of the top-ranking pages had links with traffic.

That’s interesting because it means **it’s possible to rank on the first page of Google without links from pages with traffic** even if other pages in the SERP have such links.

## Final thoughts

I think that the results of our data studies turn out to be quite interesting.

But at the same time, the takeaways I’ve suggested along the way are unfortunately **far from definitive.** Although the research itself is reliable and the numbers are accurate, they’re merely correlations and thus, cannot confirm causation. (I know I’m repeating this a lot, but it’s a crucial point).

As Albert Einstein famously said:

> No amount of experimentation can ever prove me right; a single experiment can prove me wrong.
>
>
>
> Albert Einstein, Super smart guy [from the past](https://en.wikipedia.org/wiki/Albert_Einstein)

So what can we learn from this study?

The only thing we can say with absolute certainty is that no single factor is a panacea—neither the raw number of pages or domains that link to you nor the search traffic of those pages and domains.

A variety of factors determine the value of a link.

It’s somewhat difficult to say whether one factor is more valuable than others.

However, if you want to prioritize your link building efforts, it’s worth prioritizing links from:

1. Pages with a high [URL Rating (UR)](/blog/ahrefs-seo-metrics/#section9)
2. Pages on websites with lots of referring domains

Those are the two attributes that correlate most strongly with organic search traffic according to our study. You can check both of these for any web page or website in [Ahrefs Site Explorer](https://ahrefs.com/site-explorer):

UR metric in [Ahrefs Site Explorer](https://ahrefs.com/site-explorer)

Domain-level metrics in [Ahrefs Site Explorer](https://ahrefs.com/site-explorer)

I’d love to know what you guys think about these results.

If you’re an SEO data nerd and would love to collaborate with us on a similar research study, feel free to reach out and we’ll figure something out.
