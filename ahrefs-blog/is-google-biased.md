---
title: "I Thought Google Was Biased, But The Data Shows They're Not"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "is-google-biased"
url: "https://ahrefs.com/blog/is-google-biased/"
canonical: "https://ahrefs.com/blog/is-google-biased/"
author: "Patrick Stox"
published: "2020-11-05T16:20:43+00:00"
updated: "2023-08-19T18:59:33+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
fetched_at: "2026-06-12T11:42:51+00:00"
status_code: 200
html_hash: "04d91606019d99c2d8801c0b3f437e000a8b1e6cc5a8e579e2ee96674ad63900"
clean_word_count: 1332
clean_char_count: 7917
---
# I Thought Google Was Biased, But The Data Shows They’re Not

Recently, Google CEO Sundar Pichai was called to testify in front of Congress about potential bias in Google’s algorithms. This isn’t the first time Google has been accused of bias and likely will not be the last time. Google alleges there is no bias, yet many Conservatives argue that Google is biased against them.

With our expert knowledge of [search engine optimization (SEO)](https://ahrefs.com/seo/seo-basics) and Ahrefs’ massive amounts of data, we wanted to see if we could identify any bias from Google by looking at data for popular Conservative and Liberal news sites. If you’re not familiar with Ahrefs, we’re one of the top SEO tools with seriously big data about the web.

- [Methodology](#methodology)
- [Results](#results)

## Methodology

Google makes hundreds of tweaks to its ranking algorithms every year. Most of these go unnoticed because they’re small, but every so often, there’s a big ‘core’ update that impacts a large percentage of search results. As Google tells us the dates of these updates, we figured we could look for bias by studying organic traffic to well-known Liberal and Conservative news sites before and after these updates.

For instance, here’s the estimated organic search traffic to Fox News since 2015. Each line represents a Google Core Update:

Google Core Updates overlaid on a traffic graph for Fox News

However, looking at this data for one website doesn’t tell us much, so we did the same and for the top Conservative and Liberal news sites. We pulled these from [AllSides Media Bias Ratings](https://www.allsides.com/media-bias/media-bias-ratings) (left and right bias ratings). Here is a list of those websites:

### Conservative news sites:

- New York Post
- The Last Refuge
- Drudge Report
- The Federalist
- Orange County Register
- The Epoch Times
- Washington Times
- Christian Broadcasting Network
- National Review
- Townhall
- The Mark Levin Show
- The Rush Limbaugh Show
- Breitbart
- Newsmax
- The National Interest
- The Gateway Pundit
- RedState
- PJ Media
- Washington Examiner
- Fox News
- Christian Today
- Zero Hedge
- The Daily Caller
- TheBlaze
- The Daily Wire

### Liberal news sites:

- Vox
- U.S. News & World Report
- The Washington Post
- CNN
- Bustle
- NBC News
- Hollywood Reporter
- Los Angeles Times
- Yahoo News
- Al Jazeera
- Rolling Stone
- HuffPost
- The Verge
- The New York Times
- ABC News
- TIME
- CBS Local
- The Guardian
- Bloomberg
- NPR
- CBS News
- The Atlantic
- Politico
- Univision

Before we get to the results, I should cover a bit about Ahrefs data. We have hundreds of millions of search terms and large amounts of clickstream data. We use this data to estimate organic traffic by looking at all the different queries people search for, the positions that websites occupy in the search results, and where users click. For the Core Updates, we decided to look at traffic at the start of the [Google Core Updates](https://ahrefs.com/google-algorithm-updates) and traffic 14 days later. This is to give Google time to roll out the changes to their different data centers. It also gives us time for our data to reflect the changes.

Our data is normalized in the sense that volumes are averaged over 12 months, so it should account for seasonality mostly, with elections being an exception since they’re not every year. We’re also not going to see newer stories or search topics early on, but we should pick up any popular searches and related clickstream data later.

## Results

From 2015 to the present, we see a decline in average traffic for the top news sites in each category during Google Core Update periods.

**Conservative total traffic decline:** -2.65%
 **Liberal total traffic decline:** -1.78%

These numbers are actually very similar and not statistically significant, considering we’re taking into account the traffic of 50 websites and looking at a period of 6 years. Leading up to the last election in 2016, the impact on both categories was roughly equal. Leading up to the 2020 election, if you look at the results from the previous year or so, you’ll see that the impact was roughly equal for both categories, with the most recent update seeming to be better for Conservative websites.

If we look at the individual data points, both Conservative and Liberal news sites saw positive and negative impacts during every one of these Google Core Updates. Each box plot below represents the top websites in each category, and I’ll reiterate that every single update had winners and losers for both categories. Typically, whether a site wins or loses in a core update is related more to its quality than anything else.

While we can’t conclude from this data that there is no bias in Google search results, we can say that within the last 6 years, we don’t see any new bias introduced during Google Core Updates.

### Is there a traffic bias?

One of the things that stood out to us is that Liberal websites definitely get more traffic than Conservative websites.

Now the question is, why is that the case? Does this show a potential bias that predates our keyword data set? Let’s find out if we can explain the traffic difference.

#### Amount of content

When looking at the number of indexed pages, Liberal news sources have over 8x more pages indexed than Conservative news sources. In fact, the chart is almost identical to the one above for traffic share. As a result, the top Liberal news sites generally have more chances to rank for different things than the top Conservative news sites.

#### Branded vs. unbranded traffic

The branded traffic for CNN and Fox News is roughly the same, meaning that a similar number of people are specifically seeking them out in organic search. However, branded traffic makes up a smaller percentage of CNN’s overall traffic, likely because they simply have more content. CNN has ~2.5 times the number of indexed pages as Fox News, so they have more chances to rank for different things.

#### Other explanations for traffic differences

With only Google search data, it’s hard to definitively determine why Liberal sites get more traffic than Conservative sites. It may be that Conservatives tend to use Google less. It’s also possible that Conservatives get more news from TV, apps, or social media than Google. All of this may be true, but without additional data, these statements can’t be confirmed and are merely conjecture.

### More ways we could have looked for bias

If we looked at specific examples of queries, I’m sure we would have found what appeared to be examples of bias. The problem with using individual examples is there is an inherent bias from the person doing the analysis. The data is complex and you’d need a good way to determine if the sites and content are relevant to specific queries. Unfortunately, this would be difficult and extremely subjective, which is why we chose not to pursue this route.

We could have also looked at link data or links from other websites to these news sites. Again, I have no doubt that this data is biased as the more popular and high-ranking websites with more pages would tend to get more links naturally. We already proved this in our [backlink growth study](https://ahrefs.com/blog/backlink-growth-study/).

We could have looked at specific examples of search terms suggested by Google via their autocomplete system, but we already know that they remove many negative terms from these results. Again, this is already biased, and it would be difficult to prove any malicious bias here.

## Final thoughts

There’s an inherent bias in everything. While our data shows that Google Core Updates didn’t seem biased one way or another over the past few years, we still can’t confidently say there is no bias elsewhere in Google’s system.

Got questions about this data? Ping me [on Twitter](https://twitter.com/patrickstox?lang=en).
