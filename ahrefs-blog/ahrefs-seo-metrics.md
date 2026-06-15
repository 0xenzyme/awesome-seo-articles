---
title: "Ahrefs’ SEO Metrics: A Glossary"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "low"
slug: "ahrefs-seo-metrics"
url: "https://ahrefs.com/blog/ahrefs-seo-metrics/"
canonical: "https://ahrefs.com/blog/ahrefs-seo-metrics/"
author: "Rebekah Bek"
published: "2023-11-30T20:22:04+00:00"
updated: "2024-09-17T11:00:15+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2024_watch"
  - "product_or_tool_content"
fetched_at: "2026-06-12T11:12:06+00:00"
status_code: 200
html_hash: "76ac6971d41c1612dbcc168ee3efed6bb1b162a449f159435dca4703997da96f"
clean_word_count: 2604
clean_char_count: 15178
---
# Ahrefs’ SEO Metrics: A Glossary

Want to make sure that you have the right understanding of the SEO metrics in our tools? Here’s a centralized glossary of Ahrefs metrics and how they’re calculated, along with some other popular metrics in our toolset.

We’ll be covering:

- URL Rating (UR)
- Domain Rating (DR)
- Ahrefs Rank (AR)
- Organic Keywords
- Organic Traffic
- Organic Traffic Value
- Paid Traffic Cost
- Keyword Difficulty (KD)
- Traffic Potential
- Keyword Search Volume
- Parent Topic
- Share of Voice
- Organic Pages
- Crawled Pages

![](https://ahrefs.com/blog/wp-content/uploads/2023/11/seo-metrics-1.png)

Knowing where each metric comes from and how it’s calculated lets you understand the advantages and flaws of that metric and apply them to your SEO efforts, giving you an edge over your competitors.

## Why trust Ahrefs’ SEO data

Before we get into the metrics themselves, here’s why you should trust Ahrefs.

Ahrefs has the most active crawler in the SEO industry according to [CloudflareRadar](https://radar.cloudflare.com/traffic/verified-bots), and the third most active crawler worldwide behind [GoogleBot](https://ahrefs.com/blog/googlebot/) and BingBot.

We also have top-notch infrastructure, and we’re the only tool using the technology and insights from building [our own search engine](https://yep.com/) to improve Ahrefs tools and data.

According to [Aira’s report: The State of Link Building Report 2022](https://aira.net/state-of-link-building/), Ahrefs has the most trusted backlinks data in the SEO industry.

- 64% of SEO professionals trust Ahrefs’ link data over its competitors (the next closest competitor, GSC, only had 14% of votes)
- 44% of SEO professionals use Ahrefs’ Domain Rating as their SEO metric of choice.

Now let’s get into it.

## URL Rating (UR)

URL rating represents the overall strength of a page’s backlink profile, measured on a logarithmic scale from 0 to 100. The bigger the number, the stronger a page’s backlink profile is.

If you’re familiar with [Google’s PageRank formula](https://ahrefs.com/blog/google-pagerank/), it should be easy to grasp Ahrefs’ URL Rating since we use similar principles in our calculations. Those similarities include:

- Counting links between pages
- Looking at both internal and external links pointing at a target
- Weighting the links differently
- Respecting the “nofollow” attribute
- Using a [damping factor](https://ahrefs.com/blog/single-page-website/#:~:text=When%20PageRank%20is%20passed%20on,diminished%20with%20each%20%E2%80%9Chop.%E2%80%9D)

Sidenote.

While UR and PR are similar in nature, you shouldn’t think of URL rating as a direct replacement. Our algorithm is simpler compared to Google’s, which has evolved quite a bit over the years.

From our [own studies](https://ahrefs.com/blog/search-traffic-study/), we’ve also found a clear positive correlation between URL rating and search traffic. This means that higher UR pages get more search traffic.

All in all, it’s a pretty versatile and reliable metric. You can use it for link prospecting, gauging ranking difficulty, and more.

## Domain Rating (DR)

Domain Rating represents the overall strength of a website’s backlink profile and considers both the size and [quality of the links](https://ahrefs.com/blog/high-quality-backlinks/) pointing at a website. Like UR, DR is also plotted on a logarithmic scale from 0-100.

To calculate DR, we use nearly the same principles as URL Rating, but look at links between domains instead of pages.

There are three main things to note when considering how DR is calculated.

1. **The number of unique referring domains that have at least one followed link pointing at the target website**. This means that links that are nofollowed won’t improve DR for the target website. Since referring domains only count one link per website, subsequent links from the same website won’t help a website’s DR either.
2. **The DRs of the linking domains**. For example, if a website has 1,000 followed referring domains from DR 0 websites, it’s unlikely that those links will help their pages rank. This also means that a website’s DR can increase if the DRs of its linking websites increase.
3. **The number of unique domains the referring websites link to with at least one followed link**. The more unique websites a site links to, the less “DR equity” it’ll transfer to each of them.

   Take for instance if you were to get a link from the New York Times. Since it has a DR of 94, you might think that your DR should see a little bump. That’s not necessarily true, since they also link to nearly 300,000 other websites with followed links. Getting a followed link from a site like IMDB, which has a DR of 93 and links out to around 7,000 websites, would impact your DR much more.

Sidenote.

We don’t recommend using Domain Rating as a standalone metric. It’s not a good indicator of a website’s quality or legitimacy; it’s merely a measure of “link popularity.” A good practice is to pair DR with other metrics like domain-level search traffic or UR, which paints a clearer picture of a website’s quality and popularity.

## Ahrefs Rank (AR)

Ahrefs Rank ranks all the websites in our database by the size and quality of their backlink profiles — basically, by their DR. The higher its DR is, the closer its AR is to #1.

You can look at Ahrefs Rank as a much more granular version of Domain Rating, since it gives you the entire spectrum of DR across the web.

Sidenote.

Ahrefs’ Rank has nothing to do with your Google rankings or search traffic. It also doesn’t directly affect your rankings.

## Organic Keywords

This metric refers to the total number of keywords that your target ranks for in the top 100 organic search results. When ranking for the same keyword across different locations in “All locations” mode, it’s still counted as one keyword.

## Organic Traffic

This metric is an estimation of how much organic search traffic your target website, subfolder or URL gets each month.

Here’s how it’s calculated:

1. We find all the keywords for which your target ranks in the top 100 organic search results
2. We estimate the search traffic your target gets from each of those keywords based on its ranking position, monthly search volume and our estimated CTR for that position
3. We sum up the traffic estimations of each keyword.

Remember to treat the organic traffic estimations in Ahrefs as precisely that: estimations.

Here’s why:

1. We don’t know all the possible search queries a page ranks for
2. Search volumes are just approximations – even Google doesn’t give exact values
3. Ranking positions are volatile and can change by the second
4. Our CTR estimations are also approximations based on our own CTR model.

These four things contribute to discrepancies in search traffic estimations in Ahrefs. Any other tool providing a similar metric will face similar discrepancies.

At the same time, these estimates work incredibly well for comparing whether your competitors’ websites get more or less organic search traffic than your own. Since websites in the same industry will rank for the same range of keywords and suffer from the same discrepancies, if Ahrefs estimates that one website is getting more traffic than the other, this will likely be true for their actual traffic as well.

You can use the following formula to estimate your competitor’s traffic:

Sidenote.

The good folks at AuthorityHacker compared the quality of search traffic estimations from six different SEO tools. In their study, Ahrefs turned out to be the winner with an average discrepancy of 22.5% and 0.99 correlation with GSC data. In [this blog post](https://ahrefs.com/blog/traffic-estimations-accuracy/), we replicated the study on a larger scale and reported on how the numbers change.

## Organic Traffic Value

Organic traffic value shows the value of the organic search traffic, if it were to be acquired via PPC in Google Ads.

To calculate it, we take the estimated clicks for a keyword and multiply it by the CPC value for that keyword. Then we sum the total values to come up with a total traffic value metric.

In essence, the number gives you a sense of how valuable a domain’s keyword profile is. Another way to think of it is how much it would cost you, if you had to pay Google for every click that you’re getting for free by ranking organically.

For example, let’s say that a page ranks for 2 keywords: blue widgets and red widgets.

Blue widgets is responsible for sending the page 100 monthly organic visits and has an average CPC of $2. The traffic value for that keyword would then be $200. On the other hand, the keyword red widgets is also responsible for generating 100 monthly organic visits and has a CPC value of $1.

The traffic value for that keyword would be $100, and the total traffic value for that page would be $300.

Sidenote.

Cost per click metrics are highly volatile and can change by the second. Regardless of exact live values, this metric can be helpful to understand the commercial value of both yours and your competitors’ pages so you can prioritize your SEO and marketing tasks accordingly.

## Paid Traffic Cost

Paid traffic cost shows the estimated monthly cost of paid search traffic from all the keywords that your target ranks for via PPC.

We calculate it based on multiplying the monthly paid traffic of a keyword by the CPC value. Then, we add up the paid traffic cost of individual paid keywords.

NOTE: Like all other metrics, this value is a rough estimation. We don’t capture all paid keywords due to a few reasons:

1. Websites bid on some keywords that we do not have in our keyword index, hence we don’t scan them.
2. Websites bid on keywords that we do have and scan, but they use specific locations like a city. We can guarantee scanning from a country, but not an exact location.

## Keyword Difficulty (KD)

Keyword Difficulty gives an estimation of how hard it’ll be to rank in the top 10 organic search results on Google for a given keyword. It’s measured on a scale from 0 to 100, with the latter being the hardest to rank for.

We calculate KD by pulling the top 10 ranking pages for your keyword and looking up how many websites link to each of them. The more links the top-ranking pages for your keyword have, the higher its KD score.

This is a complicated metric and there’s a lot more to say about it – to learn more, check out our [in-depth post on Keyword Difficulty](https://ahrefs.com/blog/keyword-difficulty/).

Sidenote.

KD doesn’t take anything else into account. You should always study the top 10 results manually for a more complete sense of ranking difficulty.

## Keyword Search Volume

Keyword search volume represents the average number of times people search for a query in a target country in a given month.

We use Google Keyword Planner data as a base to build our model, which is the data that you see in every other third party keyword tool.

At this time, search volume in Ahrefs is calculated based on a 12-month average. Since the same person can perform multiple searches a month, search volume can be misleading and should be taken into account with another metric, like Traffic Potential.

For a closer look at this metric, check out our [in-depth post on keyword search volume](https://ahrefs.com/blog/keyword-search-volume/).

## Traffic Potential

Traffic potential shows the total organic traffic the #1 ranking page for your target keyword receives from all the keywords it ranks for.

For example, the keyword “submit website to search engines” has a traffic potential of 6.4k, even though it only has a search volume of 500.

Since a page can rank for hundreds of keywords and get traffic from all of them, traffic potential is often a better metric to consider than search volume alone.

## Parent Topic

Parent Topic determines if you can rank for your target keyword while targeting a more general topic instead.

To identify the Parent Topic, we take the #1 ranking page for your keyword and find the query responsible for sending the most search traffic to that page.

For example, let’s say you own a fitness site and you want to teach people how to do lunges with weights. If you analyze the query “how to do lunges with weights,” you’ll see that the search volume is 350. However, the Parent Topic is “lunge with weights.”

It looks like the #1 result for this query gets an estimated 2,000 monthly search visits.

This should help you prioritize your keyword research and target more lucrative keywords.

## Share of Voice (SOV)

Share of voice represents a website’s overall visibility in the organic search results for a set of tracked keywords.

We calculate it by dividing the traffic to a website by the total search traffic for all keywords that you’re tracking. Traffic is allocated based on the click-through rate curve for a particular keyword.

## Organic Pages

Organic pages represents the total number of pages on your target that rank in the top 100 organic search results.

To track this over time, go to Site Explorer’s Overview > Organic search tab.

## Crawled Pages

Crawled pages represents the total number of unique pages on your target that were visited by Ahrefs crawler and saved to Ahrefs’ index.

In general, the more “popular” a site is (ie. a higher Domain Rating, has higher quality backlinks), the more likely a domain will be crawled. Domains that are less “popular” (ie. lower DR, less quality backlinks) will be partially crawled.

To see if your website is crawled, go to Site Explorer’s Overview and check “Crawled pages” on the General > Performance chart. If Crawled pages is 0, it means the target website is not indexed.

If it’s a new site, allow some time for our crawler to index your page. If not, make sure AhrefsBot can crawl your website ([learn how to enable our crawler](https://help.ahrefs.com/en/articles/1565233-how-do-i-enable-ahrefs-bot-to-crawl-my-website-and-index-its-pages)). To find out if a domain is blocking our bot, check the status of its robots.txt in [our robots checker](https://ahrefs.com/robot).

You can see the distribution of your target’s pages by [HTTP status code](https://ahrefs.com/blog/http-status-codes/) by going to Site Explorer’s Overview and looking for the Crawled pages widget.

## More resources

There you have it: definitions for the most common metrics you’ll see throughout Ahrefs SEO toolset and explanations on how they’re calculated.

Now that you know how to interpret our metrics, here are some other resources to help you figure out which ones to monitor and how to build reports with them:

- [Steal Our SEO Report Template (Inspired by SEO Experts)](https://ahrefs.com/blog/seo-report-template/)
- [10 SEO Metrics That Actually Matter (And 4 That Don’t)](https://ahrefs.com/blog/seo-metrics-to-track/)
- [12 SEO KPIs You Should (And Shouldn’t) Track](https://ahrefs.com/blog/seo-kpis/)

Curious about something that we haven’t covered here? Have a look in [our Academy](https://ahrefs.com/academy), search in [our Help Center](https://help.ahrefs.com/en/), or contact our support team and we’ll be happy to point you in the right direction.
