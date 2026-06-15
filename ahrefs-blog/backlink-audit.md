---
title: "How to Do a Basic Backlink Audit (in Under 30 Minutes)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "backlink-audit"
url: "https://ahrefs.com/blog/backlink-audit/"
canonical: "https://ahrefs.com/blog/backlink-audit/"
author: "Joshua Hardwick"
published: "2018-08-28T15:40:15+00:00"
updated: "2023-10-05T07:46:41+00:00"
categories:
  - "Link Building"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T11:16:40+00:00"
status_code: 200
html_hash: "0d175990818d8ccd1867d58f3937329f46ef89d793f09204b5d172284fd111f4"
clean_word_count: 3847
clean_char_count: 22515
---
# How to Do a Basic Backlink Audit (in Under 30 Minutes)

Have you just taken on a new SEO client? Or perhaps been put in charge of SEO for your company’s website? You *need* to perform a backlink audit.

The reason for this is simple: It allows you to check that the site is in good shape **before** you begin working on it. That means making sure that there are no spammy backlinks which could hinder future SEO efforts or worse, trigger a [Google penalty](https://ahrefs.com/blog/google-penalties/).

Spammy backlink example

Think of this like buying a home. You plan to decorate and renovate said home once purchased, but that doesn’t mean you want to buy a house on the verge of crumbling to the ground, right? So you scrutinize it, checking for damp and other potentially costly issues before you part with even a single penny (cent) of your cash.

Performing a backlink audit is the SEO equivalent of this process.

It’s your insurance policy against working with clients who’ve had the misfortune of working with scummy SEOs in the past, and now want to push all their problems onto you.

But, importantly, this isn’t *all* about finding the “bad” things. Auditing your backlink profile will lead to insights that will aid your future [link building](https://ahrefs.com/seo/link-building) efforts, and make life easier.

In this post, I’ll show you how to perform a simple, insightful backlink audit that should take roughly 30 minutes (for most sites).

Sidenote.

30 minutes is an approximation. If you go deeper and investigate specific issues, it will take longer. Likewise, it will take an experienced SEO less time than an inexperienced SEO. Either way, it’s still well worth the relatively small time investment.

## What you need

You can do this entire thing with nothing but [an Ahrefs account](https://ahrefs.com/pricing)*.*

However, should you have the budget available to do so, it’s always preferable to download data from all available link sources—Ahrefs, Google Search Console, Majestic, Moz, etc.

Please be advised, however, that merging data from multiple sources can be a complicated process that requires spreadsheet or coding skills. So if you don’t feel comfortable using APIs and working with large amounts of data, your best bet is to stick to an online tool with a convenient UI.

For that reason, we’ll keep things simple in this guide and use only Ahrefs which is known to have the [best link data](https://ahrefs.com/big-data) in the industry. The coverage we provide should be enough to perform a sufficient link audit without the hassle of merging multiple datasets.

For consistency, I’ll be auditing the [Ahrefs blog](https://ahrefs.com/blog/) (*ahrefs.com/blog*)throughout this guide. (Fingers crossed we don’t come across anything too nauseating!)

## Step 1. Get a high-level view of your backlink profile

First things first, let’s plug the site into [Site Explorer](https://ahrefs.com/site-explorer) and do some basic analysis.

*[Site Explorer](https://ahrefs.com/site-explorer)**> enter domain > choose the “prefix” mode*

Please note that in this instance, we’re choosing the “prefix” mode because we want to restrict things to the Ahrefs blog, rather than site the as a whole. If you’re auditing your entire website, choose the “\*.domain/\*” option instead.

*[Site Explorer](https://ahrefs.com/site-explorer)**> enter domain > choose the “\*.domain/\*” mode*

Everything in this section requires nothing but the **Overview** report (i.e., the one you see after entering a site into Site Explorer).

### 1. See how your backlink profile compares to the competition

Let’s start with the absolute basics and answer a simple question: how many backlinks and referring domains do you have pointing to your site?

You’ll find the answer to that question here:

It looks like we have 40.2K backlinks from ~5K referring domains.

These numbers seem quite large at first glance and, if you see similar ones for your site, might be enough to provide a small ego boost. However, unless you compare these numbers with your competitors, they don’t tell you much.

So let’s do that. Here are the same stats for the Moz blog:

… and the Majestic blog:

Referring domains is the number I’d pay most attention to here. From this, we can see that Moz is doing ~8x “better” than us, whereas Majestic is doing much “worse.”

But to glean some real insights, we also need to look at the pace of link acquisition.

### 2. Look at your backlink acquisition rate over time, and compare this to the competition

Looking at the raw numbers is a good start, but it doesn’t provide much in the way of context.

Like, have we been building links consistently over the years? Have things been flatlining for a while? Have our competitors been acquiring links at a faster pace than us? Let’s look at the interactive referring domains graph to find out.

This graph is cumulative, meaning that the number of referring domains linking to us continues to rise over time, which is good.

It’s also worth noting that this is interactive and updated daily. Mouse over any point on the graph to see a historical snapshot of your backlink profile for any date.

Because this unveils the absolute numbers, it’s easy to see the cumulative growth (or decline) of your backlink profile between any two dates.

But once again, these figures are more insightful when comparing things against the competition. Here’s *moz.com/blog*, for example:

It looks like we’ve been acquiring links faster than them, right? Not exactly; the absolute numbers tell a different story. The Moz blog has seen a cumulative increase of 7,230 referring domains over the past two years, whereas Ahrefs’ blog has grown by just 1,811.

This is because Moz has accumulated tons of fantastic resources on their blog over the years, whereas we’ve only been publishing industry-leading content (we hope!) for a few years.

### 3. Identify negative SEO attacks by looking for link spikes

Everything is pretty straightforward with our referring domains graph; we’re acquiring links at a consistent pace, and there have been no big spikes (or dips) over the years.

However, if you look at the same graph for *matthewwoodward.co.uk*, it’s a different story.

In mid-2014, he experienced a significant spike in referring domains followed by a sudden drop of equal magnitude. Having reached out to him about this, we can confirm that this was the result of a [negative SEO](https://ahrefs.com/blog/negative-seo/) attack on his site.

This is quite tame for a negative SEO attack. Some are much more extreme and obvious.

An extreme negative SEO attack, reflect in the referring domains graph in [Ahrefs Site Explorer](https://ahrefs.com/site-explorer)

Is this something to worry about? Maybe. Google is better than ever at ignoring “bad” backlinks, which means that you’re [unlikely to receive a manual penalty](https://ahrefs.com/blog/google-penalties/) for such things.

But still, an influx of spammy backlinks is never a positive thing, so they can be worth [disavowing](https://ahrefs.com/blog/google-disavow-links/). Just make sure you analyze things further before considering this (keep reading!).

### 4. Look for a disproportionate amount of links from “spammy” CTLDs

What if I said that most of the links to the Ahrefs blog come from .cn and .gq domains?

You’d say that looks pretty unnatural and spammy, right? *Correct.* Luckily, this isn’t the case here. Just check the CTLDs graph on the **Overview** report.

It’s clear that we have backlinks from a good distribution of totally non-spammy CTLDs; everything from *.com’s* to *.co.uk’s* to *.net’s*. Are there still some links from sites on .cn domains and other less common TLDs? Of course, but this isn’t anything to worry about—the distribution percentage is super-low (~2%).

Sidenote.

Not every link from a .cn TLD will be spammy. It’s just that they’re more likely to be spam, especially if you see a high distribution of links from such TLDs.

Furthermore, this isn’t representative of a non-spammy backlink profile for every single website.

If you’re a China-based business, it might be quite natural to see a much higher percentage of links from .cn domains. It’s about context.

I’d say that if things look “off” to you (i.e., you wouldn’t expect such a high number of links from a certain CTLD), then it warrants further investigation.

### 5. Look for indications of spam in your anchor text profile

Most people will **naturally** link to you using branded anchor text.

For example, when most people link to Ahrefs, the anchor text they use (i.e., the [clickable words](https://ahrefs.com/blog/anchor-text/) that make up the link) is branded: *ahrefs; ahrefs.com; here’s something I read on ahrefs*, etc.

The anchor text distribution for our site reflects this.

Anchors, from the **Overview** report in [Site Explorer](https://ahrefs.com/site-explorer)

At least 1/5 of referring domains link to us using branded anchor text, which is a clear indication of a non-spammy backlink profile.

If you see “dodgy” and unexpected stuff here, such as crude language or even a high distribution non-branded anchors, then you should check out the full **Anchors** report and investigate further.

To illustrate what I mean by “dodgy,” here’s an extreme example I made up:

Believe me when I say, if your anchor text distribution looks like this, you’ve got problems.

Things don’t have to be this bad for them to be an issue, however. You should also be on the lookout for a high distribution of so-called keyword-rich anchor text.

Learn more about this in [our anchor text guide](https://ahrefs.com/blog/anchor-text/).

## Step 2. Delve (a bit) deeper

Believe it or not, our **Overview** report is called *that* for a reason: it gives you a general overview; nothing more, nothing less.

In the same way that damp can hide behind decades of redecorations, [bad links](https://ahrefs.com/blog/bad-links/) can hide behind years of shoddy SEO work. So we need to delve deeper… much deeper.

That’s the only way to make wise SEO decisions going forward.

### 1. Find wasted backlinks to your site

Link building isn’t easy; attracting good backlinks takes a lot of time and effort.

That’s why it’s important to make sure that none of your backlinks are wasted, which you can do with our **Best by links** report. Not familiar with this report? It shows which of the pages on your website have the most backlinks pointing to them.

**Best by links** report for *ahrefs.com/blog*, via [Site Explorer](https://ahrefs.com/site-explorer)

This report is super-useful for understanding what topics and types of content attract links for your site. And if you take a look at this same report for competitors, it can uncover content ideas that are likely to attract links.

But back to the task at hand. Let’s filter for 404 errors (i.e., broken pages), and sort by referring domains.

Because these pages return 404 errors, all these backlinks are effectively wasted. The so-called “link juice” isn’t able to flow around the site. These should [be fixed](https://ahrefs.com/blog/fix-broken-links/).

But there’s another instance where backlinks are effectively wasted: when you have a ton of backlinks pointing to pages with little or no organic search traffic. To find these, we can use the **Top Pages** report.

Here’s one such page on Ahrefs’ blog which has a whopping 296 referring domains, yet it attracts 16 organic visitors per month. Not good.

This usually happens because the pages aren’t optimized around anything worthwhile. So a quick win here is to refresh the content and reoptimize around [keywords with organic traffic potential](https://ahrefs.com/blog/keyword-search-volume/).

### 2. Find the best and worst sites that link to you

Looking at the **Referring domains** report will unveil who links to your site. This can be insightful in itself, but the *real* opportunities start appearing when you specifically look for the best and worst referring sites.

This is simple to do. To find the “worst” sites, add a dofollow filter and sort by [Domain Rating (DR)](https://ahrefs.com/blog/domain-rating/) from low to high. All of the lowest quality sites will rise to the top.

Editor’s Note

Low DR doesn’t necessarily indicate that a site is “bad.” It just means that the site doesn’t have a lot of links, or that the links it does have aren’t strong.

You will need to review a website firsthand to determine its legitimacy. However, you can often get a sense of this just by looking at the domain from which it comes. For example, it’s pretty apparent that a link from *make-money-on-the-internetz.cn* is less likely to be a legitimate link than one from *forbes.com*.

Bottom line: links from low-DR sites are more likely to be of lower-quality, but not always.

Tim Soulo

Head of Marketing

Look through these and see if anything looks “fishy.”

Here’s another trick: sort by the number of dofollow links from each site, from high to low.

Sites that link to your site hundreds or thousands of times will often be sitewide links.

Sitewide links aren’t always “bad,” but it can help to uncover links in sites’ sidebars, footers, etc., which are often [paid links](https://ahrefs.com/blog/buy-backlinks/).

However, this report isn’t only useful for uncovering “bad” stuff. If you sort by Domain Rating from high to low and skim the “links to site” column, you’ll be able to see your existing “superfans.”. These are the people with whom you’ll want to nurture relationships.

Neil Patel clearly loves Ahrefs 😉

### 3. Check for spam in the full “anchors” report

Spammy [anchor text](https://ahrefs.com/blog/anchor-text/) is something we touched on already in step one.

But the anchors report on the **Overview** report only shows the top 10 most common link anchors, which is far from a comprehensive view for most sites. That’s why it pays to skim the full **Anchors** report to double-check for anything suspicious.

Having said that, this report can often be overwhelming, even when filtered. There are, for example, over 5K different anchor phrases for the Ahrefs blog.

The solution? Use the search function to find mentions of anything spammy.

You can then use the “Details” dropdown to the see linking site and context for the backlink.

Here’s another trick, courtesy of [Russ Jones](https://twitter.com/rjonesx?lang=en):

Export the **Anchors** report, open the CSV, copy everything from the “Anchor text” column, then paste it into [Keywords Explorer](https://ahrefs.com/keywords-explorer). Sort the list of keywords by CPC from high to low. All the most commercial keywords will rise to the top.

This is super-useful for finding over-optimized links which were possibly built by a previous (dumb) SEO agency.

Sidenote.

Be careful with that final trick because it can eat up your credits in Keywords Explorer pretty fast. To begin with, I recommend only exporting the top 100-or-so rows. That is unless you have reason to suspect issues in this area and feel it requires a full dissection.

### 4. Look for backlinks from the same C-Class IPs (advanced)

Every website lives at its own IP address, which looks something like this: `192.168.653.789`.

Those first three numbers represent what we call the IPs “a-class,” the second three the “b-class,” and so forth, like this: `AAA.BBB.CCC.DDD`. This matters because websites that share the same c-class IP are effectively internet neighbors, meaning that they usually share the same web host.

Using the **Referring IPs** report in [Site Explorer](https://ahrefs.com/site-explorer), you can see all referring domains grouped by their “network” (i.e., c-class IP). If you then sort the results by the Domains column, you’ll see the c-class IPs that have a lot of domains linking to you.

To recap, these are domains that likely share the same host *and* each link to the same site.

Conclusion: the probability of the same person or company owning them is high.

This isn’t always a negative thing; many people own many sites and, well, may choose to link out to the same websites in a legitimate manner. However, it can also be an indication of a lousy PBN (Private blog network).

Google has [targeted PBNs](https://www.seroundtable.com/google-algorithm-update-targets-pbn-23358.html) in the past. Such links are far from being [white-hat](https://ahrefs.com/blog/white-hat-seo/) and thus, should be removed or [disavowed](https://ahrefs.com/blog/google-disavow-links/).

Sidenote.

Be very careful with this one. It’s for advanced SEOs only. You shouldn’t go about disavowing all links that share the same c-class IP. You need to know what you’re looking for.

## Step 3. Review the full backlinks report

So far, we’ve used a variety of reports in [Site Explorer](https://ahrefs.com/site-explorer) to help uncover the most common backlink-related issues and opportunities sites’ face. Yet still, we haven’t checked the full **Backlinks** report.

The reason for this is simple: it’s better to uncover broader issues and opportunities first, as this helps to guide your process when perusing the full list of backlinks (of which there are often thousands).

But it’s now time to do precisely this. And, plot twist, we’ll mainly be focussed on finding opportunities in this section, rather than negative things.

Editor’s Note

While we have outlined a basic process we recommend for auditing your backlinks in full below, it’s important to note that all professional SEOs do their audits differently.

So, if you want a more advanced version that involves some [spreadsheet magic](https://ahrefs.com/blog/google-sheets-formulas-seo/), tweet us and let us know. We’ll happily update this post if there’s enough demand! 🙂

Tim Soulo

Head of Marketing

### 1. Start with a web page (not the entire domain)

While it is possible to analyze and audit the backlinks to your entire site at once, it’s not something we recommend. Why? Because it’s challenging to reach any actionable insights from doing this.

To illustrate, here are some of the “top” dofollow backlinks to Ahrefs’ blog as a whole.

You can see that some people are linking to our blog homepage, whereas others are linking to specific blog posts. Some are linking with branded anchor text, and some aren’t.

This doesn’t tell us much. We need to do things on a page-by-page basis.

So, head over to the **Best by links** report and sort by the referring domains (RD) column. You will then see which pages on your site are linked-to from the most referring domains. There is a lot you can learn from these pages.

Via the **Best by links** report, in [Site Explorer](https://ahrefs.com/site-explorer)

Select a page, paste it into Site Explorer and head to the **Backlinks** report. To begin with, filter out the “nofollow” links.

Sidenote.

Alternatively, you can begin with a page that has attracted a lot of backlinks over the past 30-days-or-so. Use the **Best by links growth** report to find these pages.

### 2. Sort by traffic (optional)

By default, the backlinks will be ordered by [URL Rating (UR)](https://help.ahrefs.com/en/articles/72658-what-is-url-rating-ur) which tells you the so-called “link popularity” (or strength) of a linking page.

But we like to sort by organic traffic from high to low. Why? Because this way you can see which backlinks are likely to be sending the most referral traffic to your website. These are rumored to be the “best” backlinks by some in the SEO community.

By the way, Ahrefs is the only tool that shows organic traffic data for linking pages. [Learn more about](https://ahrefs.com/blog/unique-features-ahrefs/) [some of](https://ahrefs.com/blog/unique-features-ahrefs/) [Ahrefs’ unique features here](https://ahrefs.com/blog/unique-features-ahrefs/).

### 3. Look for commonalities between backlinks

This is the real crux of the backlink audit process.

If you can identify commonalities between your most “powerful” links, then you start to understand why such people are linking to you. If you can understand why they’re linking to you, well, finding new prospects (that you actually want links from) becomes a damn sight easier, believe me.

So how do you do this? That’s where things become a little tricky, as there’s a lot of nuance to this process. However, the basics are always the same: look at link anchor text, site type (use our “platform” filter for this), surrounding link text, etc.

Looking at the **Backlinks** report for [our keyword research guide](https://ahrefs.com/seo/keyword-research), I can see right away that we’re attracting a fair few links from list-style posts. Mainly those listing the best SEO posts, tutorials, training courses, marketing resources, etc.

This is insightful. It tells us that should we be able to find more of these types of posts (hint: we could do this with [Content Explorer](https://ahrefs.com/content-explorer) in seconds), we could probably get a fair few more links.

I also noticed that we’re getting some decent links from blog posts about content writing.

This makes sense. Keyword research is crucial when writing content for the web. Fail to do this and your article will never attract a consistent stream of traffic, no matter how great it is.

So again, we could use Content Explorer to find articles about content writing that don’t already mention the importance of keyword research, then [reach out](https://ahrefs.com/blog/outreach/) and suggest that they may want to add something about that (with a link to our article, of course).

Hopefully, you’re starting to see how this works. I would recommend that everyone do this for at least a few pages on their site; it can be crazily insightful.

## Final Thoughts

Backlink audits can get complicated, especially if you start exporting mountains of data from a plethora of tools. Hopefully, however, this article shows that with just one tool and a limited amount of time, it’s possible to conduct a decent audit that will result in valuable insights.

But before I wrap this up, here’s one final idea: why not do this same audit for your competitors?

You can often learn a lot by doing this, such as what strategies they’re using and how they’re attracting backlinks.

If you want to learn more about this sort of thing, check out [this article about looting competitors links](https://ahrefs.com/blog/find-competitors-backlinks/), and [this one about replicating your competitors’ backlinks](https://ahrefs.com/blog/find-backlinks/).
