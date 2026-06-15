---
title: "What's New At Ahrefs? (March 2020)"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "high"
slug: "whats-new-ahrefs-march-2020"
url: "https://ahrefs.com/blog/whats-new-ahrefs-march-2020/"
canonical: "https://ahrefs.com/blog/whats-new-ahrefs-march-2020/"
author: "Si Quan Ong"
published: "2020-03-25T17:30:37+00:00"
updated: "2020-03-26T14:12:34+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "product_or_tool_content"
  - "title_year_2020_before_2026"
fetched_at: "2026-06-12T12:17:14+00:00"
status_code: 200
html_hash: "a9ee9ab2ca9b22357645df7fbbdac0dd59155e47eaa3509585e228abafffbdeb"
clean_word_count: 1487
clean_char_count: 9352
---
# What’s New At Ahrefs? (March 2020)

It’s been almost a year since our [last product update](https://ahrefs.com/blog/site-audit-update-may-2019/).

The reason why is a somewhat ironic one: we’ve been so busy working on our product that we just haven’t had time to write anything up.

So, in today’s post, we’re going to go over some of the features we’ve shipped in the past 10 months.

1. [Tracking ‘rel=UGC’ and ‘rel=sponsored’](#rel-sponsored-ugc)
2. [Updated keyword volume calculation](#keyword-volume-calculation)
3. [Total monthly search traffic for API](#search-traffic-api)
4. [Improved Dashboard](#improved-dashboard)
5. [Projects manager](#projects-manager)
6. [Ads history](#ads-history)
7. [“How to use” tutorials](#how-to-use-tutorials)
8. [Search improvements in Content Explorer](#content-explorer-search)
9. [Ranking data for massive sites](#ranking-data-big-sites)
10. [Wildcards (\*) in Keywords Explorer](#keywords-explorer-wildcards)
11. [Free tools](#free-tools)
12. [Other smaller updates](#others)

By the way, this is really only the tip of the iceberg. Look forward to seeing more product update posts, especially with all the releases we’ve done for Site Audit and our SEO toolbar!

## 1. Tracking ‘rel=UGC’ and ‘rel=sponsored’

On 10 September 2019, Google shook up the SEO world by announcing two new link attributes for webmasters: “sponsored” and “UGC”.

> Today, we’ve announced two new link attributes - “sponsored” and “ugc” - that join “nofollow” as ways to identify the nature of links. All will now work as hints about which links Google Search should consider or exclude for ranking purposes. More details:<https://t.co/V6X2xjEC5L>— Google Webmasters (@googlewmc) [September 10, 2019](https://twitter.com/googlewmc/status/1171460946037858304?ref_src=twsrc%5Etfw)

Here’s how [Google explains](https://webmasters.googleblog.com/2019/09/evolving-nofollow-new-ways-to-identify.html) the new attributes:

- **rel=“sponsored”:** Use the sponsored attribute to identify links on your site that were created as part of advertisements, sponsorships or other compensation agreements.
- **rel=“ugc”**: UGC stands for User Generated Content, and the ugc attribute value is recommended for links within user-generated content, such as comments and forum posts.

We started tracking these just two days after Google’s announcement.

This means you can now easily filter for UGC and sponsored backlinks within our *Backlinks*, *Referring domains* and *Linked domains* reports.

![1 ugc sponsored](https://ahrefs.com/blog/wp-content/uploads/2020/03/1-ugc-sponsored.png)

## 2. Updated keyword volume calculation

Previously, we used a 30-month average to calculate our search volumes. However, this time period was unintuitive.

So, we’ve made the switch to a **12-month average**.

How does this affect you?

Firstly, you’ll notice changes in average monthly search volume for some keywords.

Secondly, you’ll notice a sudden drop in estimated traffic for some websites. This is because the keywords they rank for are not as popular as they were a year ago.

Just look at the drop for Coinbase.com:

Because most bitcoin and cryptocurrency-related searches peaked in late-2017 (over 12 months ago), their “new” search volumes are lower and that has a knock-on effect on the site’s traffic estimation.

For websites in more “evergreen” industries, the change should be barely noticeable.

Sidenote.

To address this, we’re planning on rolling out an update that will recalculate data going backward. This will fix any sudden drops.

## 3. Total monthly search traffic for API

This was one of the most upvoted features in our [feature request board](https://ahrefs.canny.io/).

And yes, we finally did it. You can now see the total estimated organic traffic in [our API](https://ahrefs.com/api/documentation/positions-metrics).

You can also look forward to seeing some of your favorite tools update their services with this metric. Pitchbox and Screaming Frog have already added them:

> Just released a small update to version 12.6 of the [@screamingfrog](https://twitter.com/screamingfrog?ref_src=twsrc%5Etfw) SEO Spider - <https://t.co/4quvZRJ4JU>. Now includes Ahrefs keyword, traffic and value data courtesy of their updated API. Enjoy. [pic.twitter.com/2r0j6aPGfT](https://t.co/2r0j6aPGfT)— Screaming Frog (@screamingfrog) [February 3, 2020](https://twitter.com/screamingfrog/status/1224261745461678080?ref_src=twsrc%5Etfw)

## 4. Improved Dashboard

You’ve probably noticed that our Dashboard has a new look, but what changed?

First, we added organic traffic to the Dashboard, which was a [highly requested feature](https://ahrefs.canny.io/dashboard/p/add-traffic-to-dashboard).

Second, we added trend graphs for important [SEO metrics](/blog/ahrefs-seo-metrics/) like referring domains, backlinks, and more.

You can also select the timeframe you want for these trend graphs, from 30 days, 90 days and the past 12 months:

Third, we added the option to rearrange your projects by drag and dropping them.

## 5. Projects manager

We used to have separate projects for the Dashboard, Rank Tracker and Site Audit. That meant you had to set up multiple projects if you wanted to crawl a site and track your rankings.

Now, we’ve combined these projects across all our tools for a single, more cohesive experience.

Even better, you can now easily change the settings for any of your projects. All you have to do is click on “Settings”…

… and you’ll be able to edit the project:

## 6. Ads history

Our new Ads History report in [Keywords Explorer](https://ahrefs.com/keywords-explorer) shows you the paid search history for any keyword.

With this, you can see which websites have been competing for your target keyword over time. Keywords that your competitors are bidding on consistently may be lucrative, so you might want to consider targeting them.

You can also see the ad copy and landing pages that have appeared in the paid search results, which can serve as inspiration for your own ad copy and landing pages.

## 7. “How to use” tutorials

Having so much data at your fingertips can be overwhelming, so we added actionable tutorials to our reports to help you get the most out of them.

These tutorials are available across most of our reports in Site Explorer, Keywords Explorer, Content Explorer, Rank Tracker, and Alerts.

Even if you feel like you already know us inside out, take a look at these tutorials. We might surprise you with a trick or two.

## 8. Search improvements in Content Explorer

We’ve introduced three new ways to group search results in Content Explorer: by authors, websites, and languages.

These new angles might help you come up with better tactics to [rank higher on Google](https://ahrefs.com/blog/how-to-rank-higher-on-google).

For example, one SEO task this is useful for is finding [guest post opportunities](https://ahrefs.com/blog/guest-blogging/). Just search for a topic, then click on the total pages number for an author who’s been published on numerous websites.

You’ll then see all the posts they’ve written for different sites.

Most of these will be guest posts, which means the sites are probably receptive to guest post pitches.

## 9. Ranking data for massive sites

Originally, you couldn’t access the Organic keywordsreport for big sites like YouTube or Amazon.

But we’ve since removed this limit.

How do you make use of this change?

Watch this video:

## 10. Wildcards (\*) in Keywords Explorer

Previously, you couldn’t use wildcards to include or exclude ideas in Keywords Explorer.

Now, you can.

For example, you can add “blog\*” into the “Include” box to filter for all variations, including “blogging”, “blogger”, “blogs”, etc.

## 11. Free tools

To encourage new people to [try our toolset](https://ahrefs.com/), we’ve also released a bunch of free tools:

1. [Backlink checker](https://ahrefs.com/backlink-checker) — see the top 100 backlinks to any page
2. [Keyword generator](https://ahrefs.com/keyword-generator) — see up to 100 keyword ideas for search engines like Google, [Bing](https://ahrefs.com/bing-keyword-tool), [YouTube](https://ahrefs.com/youtube-keyword-tool) and [Amazon](https://ahrefs.com/amazon-keyword-tool)
3. [Website authority checker](https://ahrefs.com/website-authority-checker) — check the [Domain Rating](/blog/ahrefs-seo-metrics/) of your site
4. [Broken link checker](https://ahrefs.com/broken-link-checker) — check your site for broken inbound and outbound links

This is only the tip of the iceberg. We’ll be releasing more in the future, so keep a lookout!

## 12. Others

Here are some smaller updates we’ve made:

### Hide tracked keywords in Rank Tracker

We’ve added a toggle so you can easily hide keywords you’re already tracking:

### Keyword history in Rank Tracker

Keyword history in Rank Tracker now shows all URLs that your website was ranking for since we started tracking, so you can see a complete ranking history for that target keyword.

### Search volume ranges for “New keywords” alerts

You can now choose your desired search volume range when setting up keyword alerts. No more notifications about keywords you aren’t interested in.

## What should we improve next?

Got a feature request? [Let us know here](https://ahrefs.canny.io/), and vote for your favorite feature ideas from others.
