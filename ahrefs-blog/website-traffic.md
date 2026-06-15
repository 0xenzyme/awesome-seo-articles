---
title: "Find Out How Much Traffic a Website Gets: 3 Ways Compared"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "website-traffic"
url: "https://ahrefs.com/blog/website-traffic/"
canonical: "https://ahrefs.com/blog/website-traffic/"
author: "Joshua Hardwick"
published: "2018-08-16T14:13:25+00:00"
updated: "2025-07-21T16:32:36+00:00"
categories:
  - "General SEO"
freshness_reasons: []
fetched_at: "2026-06-12T12:16:13+00:00"
status_code: 200
html_hash: "afd348f922070dcbd777a46ef5741f3f06fe0f8b28a8b841928b8935119d239b"
clean_word_count: 3744
clean_char_count: 22853
---
# Find Out How Much Traffic a Website Gets: 3 Ways Compared

Do you want to see how much traffic a website gets? There are a few different ways to do this.

Before I get to those, though, here’s an important point:

If you own the website, there’s no need to estimate. You can install Ahrefs’ [Web Analytics](https://ahrefs.com/web-analytics) or [Google Analytics](https://ahrefs.com/blog/google-analytics-for-seo/) (for free) and see close to exact traffic numbers.

[Ahrefs’ blog growth](https://ahrefs.com/blog/increase-blog-traffic/), via Google Analytics

Sidenote.

Server log file analysis can provide even more data about your traffic, as explained in [this article](http://www.analyticsmarket.com/blog/google-analytics-vs-log-files).

But as you’re reading this article, I’ll hazard a guess that you don’t own the website in question, right?

You’re probably trying to guess how much traffic your competitor gets, and it’s unlikely that they’ll share their Google Analytics with you.

In this post, I’ll run through **three** ways to get traffic estimates for any website.

## Method 1. Use a traffic estimation tool

There are two types of traffic estimation tools:

1. **Tools that estimate total traffic:** Visitors to your website can come from all kinds of places: search engines; forums; social media; etc. These tools estimate the total amount of traffic from *all* sources.
2. **Tools that estimate only organic traffic**: Most websites get a good chunk of their traffic from search engines like Google; this is called “organic traffic.” Estimates from these tools don’t take into account traffic from any other sources (e.g., social media) besides organic traffic.

Let’s explore each of these in more detail.

### 1. Find out how much traffic a website gets in total

Here at Ahrefs, we tried all the leading **total** traffic estimation tools and did a few small internal experiments to find out which was most accurate, and [SimilarWeb](https://www.similarweb.com/) won.

SimilarWeb shows a bunch of traffic-related stats, including:

- Total visits;
- Pages per visit;
- Average visit duration;
- Bounce rate

Sidenote.

Learn more about how Similarweb defines and calculates these metrics [here](https://support.similarweb.com/hc/en-us/articles/212999769-Total-Visits), [here](https://support.similarweb.com/hc/en-us/articles/360000802405-Pages-Visit), [here](https://support.similarweb.com/hc/en-us/articles/115000501485-Avg-Visit-Duration) and [here](https://support.similarweb.com/hc/en-us/articles/115000501625-Bounce-Rate).

Here are the traffic estimates for *ahrefs.com* as of July 2018:

Strangely, it doesn’t provide pageview estimates. But these can be reverse engineered by multiplying *total visits* by *pages per visit* (for us, this would be 5.63M \* 7.5 = 42.23M pageviews).

Free users can also view monthly traffic estimations for up to six months on an interactive graph.

Paying subscribers can see this data for up to two years.

All traffic estimates include both mobile and desktop traffic, and you can segment by device category if you’re a paying subscriber.

Scroll down, and the report shows some more useful traffic-related stats such as *traffic by countries (desktop only)*…

Sidenote.

Free users can only see stats for the top 5 countries that drive the highest percentage of traffic.

… *traffic sources (direct, referrals, search, etc)*…

… *top referring sites (this is useful when [building links](https://ahrefs.com/seo/link-building) or looking for [guest post opportunities](https://ahrefs.com/blog/guest-blogging/) that will bring referral traffic!)*…

… and *top 5 organic keywords*…

#### Where does the data come from?

To understand the reliability of this data, it’s vital that we know where it comes from.

Here’s what SimilarWeb [has to say](https://www.similarweb.com/ourdata) on the matter:

> Our data comes from 4 main sources:
>
> - A panel of monitored devices, currently the largest in the industry;
> - Local internet service providers (ISPs) located in many different countries;
> - Our web crawlers that scan every public website to create a highly accurate map of the digital world;
> - Hundreds of thousands of direct measurement sources from websites and apps that are connected to us directly.”

Translation: SimilarWeb get their data from a variety of sources which collect anonymized information about users’ online activity.

They don’t say how big their coverage is, but they don’t get information from everyone in the world. So their data is derived from a relatively small sample of the “online population.”

#### Is the data accurate?

Let’s test it. Here’s what we did:

1. Took a sample of 116 websites from Flippa;
2. Pulled **total** unique visitors and pageviews from Similarweb for all 116 sites;
3. Compared them.

Sidenote.

We only used websites from Flippa that were at least one year old and had [verified traffic](https://support.flippa.com/hc/en-us/articles/202470444-How-Can-I-Verify-my-Traffic-Stats-).

Here’s what we found:

- SimilarWeb overestimated **total unique visitors** for 91.67% of the websites.
- SimilarWeb overestimated **total unique visitors** by 308.81% on average;
- SimilarWeb overestimated **total pageviews** for 70.83% of the websites;
- SimilarWeb overestimated **total pageviews** by 210.58% on average.

To summarise, SimilarWeb tends to drastically overestimate actual unique visitors and pageviews, according to our testing. But it doesn’t always overestimate things; it underestimates unique visitors roughly 1/12th of the time, and pageviews between ⅓ and ¼ of the time.

But here’s a critical point:

**SimilarWeb only showed estimates for roughly ⅕ of the sites we tested.**

For the other ⅘, here’s what we saw:

No data. Nada.

If you’re wondering why this happened, it’s probably due to the size of the sites we tested. All of them were relatively small sites from Flippa.

You’ll remember that SimilarWeb calculates their estimates based on data from a small subset of the entire online population. So if they don’t show traffic estimates for a particular site, it’s because not enough people in the subset from which they derive their data have visited the website in question.

That’s why SimilarWeb tends to have less or no data on smaller sites.

To prove this, we looked at whether or not SimilarWeb gave estimates for the [top 100 sites in the world](https://ahrefs.com/ahrefs-top), according to [Ahrefs Rank](/blog/ahrefs-seo-metrics/#section3). SimilarWeb gave estimates for *all* of them.

Back to the data:

Because SimilarWeb only gave traffic estimates for roughly ⅕ of sites, all our findings are based on a sample size of just 24 websites. This is admittedly rather small.

You should, therefore, take our findings with a massive pinch of salt.

### 2. Find out how much traffic a website gets from search engines

It’s true that there are a few organic traffic estimation tools on the market. But we’re clearly biased towards our tool ([Ahrefs](https://ahrefs.com/)) and convinced that it has the best quality data.

Here are the traffic-related estimates we give you:

- Estimated monthly visits from Google (worldwide);
- Estimated traffic value (i.e., the equivalent cost of monthly organic traffic for the website or URL if bought via [PPC](https://ahrefs.com/blog/ppc-marketing/));
- Estimated number of keywords (in the top 100) that the website ranks for in Google.

Let’s look at the traffic estimates in Ahrefs for *ahrefs.com (how meta!)*, as of July 2018:

You can see that *ahrefs.com* gets an estimated 270,000 monthly visitors from Google.

This is a “live” traffic estimate, meaning that it’s a “rolling average.” It gets adjusted each time we update the pool of keywords for which the website ranks in our database. Because of this, traffic estimates can vary slightly from day to day. This number includes both desktop and mobile traffic.

Do you want to see traffic estimates for a subsection of a website?

Just paste any subdomain or subfolder (e.g., *ahrefs.com/blog* or *blog.ahrefs.com*) into [Site Explorer](https://ahrefs.com/site-explorer). Select the “Prefix” option from the drop-down.

For example, if you enter *ahrefs.com/blog*, you see the total sum of search traffic across all pages within the “/blog/” folder, like so:

If you want to look at the traffic to each page within this folder, use the **Top Pages** report. It will show a list of pages sorted by traffic (from high to low).

But this is global traffic. Click the **Organic Search** tab on the **Overview** report, and you will see traffic broken down by 170 countries.

Sidenote.

Just hit “Show more” to reveal the full list of 170 countries.

You’ll also notice that we plot historic organic traffic estimates on a graph. This shows daily organic traffic estimates for as far back as mid-2015. It’s fully interactive too. Just roll over the graph to see estimated traffic stats for any date over the years.

Want to see this graph filtered for a specific country? You can do that.

Here it is filtered to show only traffic estimates for the United Kingdom:

But wait, there’s more: go to the **Organic keywords** report, and we’ll show all the keywords driving traffic to the site, starting with those [driving the most traffic](https://ahrefs.com/blog/how-to-drive-traffic-to-your-website/).

Bottomline: Ahrefs kicks back tons of data for almost any website or URL. But how?

#### Where does the data come from?

Ahrefs’ estimates are based on ranking data from [our database](https://ahrefs.com/big-data) of 6.1 BILLION keywords.

This database is updated monthly, including the search volume estimates (check out [a few fun search stats from last month here](https://ahrefs.com/blog/top-google-searches/))

Here’s what we do to calculate traffic estimates in a nutshell:

1. Take all the keywords for which a website ranks;
2. Check monthly search volume, ranking position, and [click-through rate](https://ahrefs.com/blog/how-to-improve-ctr/) for each keyword (across 170 countries);
3. Estimate how much traffic the site gets from each keyword;
4. Sum up these numbers to estimate the total organic traffic a site receives.

You can learn more about exactly how we calculate this number [here](https://help.ahrefs.com/ahrefs-terminology/site-explorer/how-accurate-is-ahrefs-organic-traffic-metric-and-how-do-we-calculate-it).

#### Is this data accurate?

Let’s test it. Here’s what we did:

1. Took that same sample of 116 websites from Flippa (all of which showed verified global organic search traffic numbers);
2. Pulled **organic** traffic numbers from Ahrefs for all 116 websites;
3. Compared them.

Here’s what we found:

- Ahrefs underestimated **organic unique visitors** for 74.14% of the websites.
- Ahrefs underestimated **organic unique visitors** by 38.08% on average;
- Ahrefs underestimated **organic pageviews** for 90.52% of the websites;
- Ahrefs underestimated **organic pageviews** by 52.04% on average.

To summarise, Ahrefs tends to underestimate organic unique visitors and pageviews, according to our testing. But it doesn’t always underestimates things; it overestimates organic unique visitors roughly 1/4th of the time, and organic pageviews roughly 1/10th of the time.

Sidenote.

By the way, these findings are based on a larger sample size than our SimilarWeb data, because Ahrefs showed estimates for *all* 116 of the sites we tested. *(Remember that SimilarWeb only gave estimated for roughly ⅕ of them?)*

But why does Ahrefs tend to underestimate traffic anyhow?

It’s because we can only estimate traffic from the 6.1 BILLION keywords we have in [our database](https://ahrefs.com/big-data). Sound like a lot? It is, we have the biggest database of all similar tools on the market.

But even a database of 6.1B keywords isn’t enough to hold every possible search query that one could type into Google. That would be impossible.

For example, a lot of people perform super [long-tail searches](https://ahrefs.com/blog/long-tail-keywords/)…

… which we don’t have in our database and, therefore, can’t estimate the traffic from.

This is how all organic traffic estimation tools work, so we’re not alone here. They all tend to underestimate traffic. The degree to which this happens comes down to the size of their keywords database; the bigger it is, the more accurate their traffic estimations will be.

This is why it matters that we (Ahrefs) have the biggest keywords database on the market.

It’s also worth noting that [no-one has totally accurate search volume estimations](https://ahrefs.com/blog/keyword-search-volume/), not even Google. This is another reason that our estimates tend to be underestimations.

### Which tool is best for comparing multiple sites?

Sometimes, it’s not so much about estimating traffic with insane precision, but rather being able to **compare the relative popularity of two or more sites**.

For example, imagine that you have a list of one hundred [outreach](https://ahrefs.com/blog/outreach/) prospects, and you want to prioritize your outreach efforts starting with the sites that receive the most traffic.

In this case, you want to compare the sites to each other and rank them in order of traffic.

So which tool is best for doing this?

To learn that, we’ll run a [Spearman correlation](https://geographyfieldwork.com/SpearmansRank.htm) on our data.

Here are the results for SimilarWeb:

| Actual “Unique visitors” VS SimilarWeb Total visits | Actual “Pageviews” VS SimilarWeb “PageViews” |
| --- | --- |
| 0.713 | 0.779 |

… and Ahrefs:

| Actual “Unique organic visitors” VS Ahrefs “Global” organic traffic | Actual “Organic Pageviews” VS Ahrefs “Global” organic traffic |
| --- | --- |
| 0.767 | 0.784 |

Confused?

Here’s what a Spearman correlation shows:

> *Spearman’s Rank correlation coefficient is a technique which can be used to summarise the strength and direction (negative or positive) of a relationship between two variables. The result will always be between 1 and minus 1. Rank the two data sets.*

Even more confused? Let me explain (with examples).

We’re looking at the correlation between two sets of data: the “real” traffic numbers (set #1) and the estimated traffic (set #2). If the numbers **positively** correlate in any way, the Spearman correlation will be between zero and 1. If they **negatively** correlate, it will be between zero and -1.

So, the closer the correlation is to 1, the more of a positive correlation there is between the two data sets.

Let’s assume we have three websites with the following *actual* traffic…

- **Site1** - 100
- **Site2** - 5,000
- **Site3** - 40,000

… and Ahrefs reports the following traffic estimates…

- **Site1** - 50
- **Site2** - 2,000
- **Site3** - 10,000

… that would be a perfect positive correlation of 1. *(The “rank” of the corresponding numbers in each dataset have a perfect positive correlation with each other)*

But if Ahrefs estimated the traffic stats as follows…

- **Site1** - 10,000
- **Site2** - 2,000
- **Site3** - 50

… that would be a perfect negative correlation of -1. *(The “rank” of the corresponding numbers in each dataset have a perfect negative positive correlation with each other)*

So basically, the higher the correlation, the better the tool is for comparing two or more sites.

Looking at the Spearman correlation data above, you can see that both Ahrefs and SimilarWeb have a strong positive correlation with “real” traffic. But Ahrefs does trump SimilarWeb, marginally.

This means that should you use our [Batch Analysis tool](https://ahrefs.com/batch-analysis) to obtain domain-level traffic estimates for a bunch of outreach prospects, then sort by traffic (high to low)…

…this is likely to be a pretty good judge of the relative popularity of these sites.

### So which traffic estimation tool should you use?

It’s important to note that each of these tools do different things.

SimilarWeb estimates **total** traffic, whereas Ahrefs estimates **organic** (i.e., Google) traffic.

One of the unique benefits of SimilarWeb is that you can see where the majority of traffic to a website is coming from (e.g., organic search, social, etc.):

You can see, for example, that *thewirecutter.com* gets roughly 2/3 of its traffic from search engines, according to SimilarWeb.

Which brings us to a cool point:

If you see that a site gets a lot of traffic from organic search in SimilarWeb, you can use Ahrefs to dig deeper and better understand that traffic.

For example, in the case of *thewirecutter.com*, Ahrefs can show how organic traffic has grown over the past 3+ years…

… or every single one of the 3.1 MILLION keywords it ranks for…

… or the pages responsible for bringing the most organic traffic to the site…

… and [a whole lot more](https://ahrefs.com/blog/how-to-use-ahrefs/)!

But enough bragging! 😉 Let’s talk briefly about pricing.

SimilarWeb don’t publish pricing information [on their website](https://www.similarweb.com/corp/pricing/). But [this Quora thread](https://www.quora.com/What-is-the-price-of-the-SimilarWeb-PRO-package) puts their cheapest plan (which gives you access to only 6 months worth of traffic data) at $199/month.

That’s double the cost of [our lowest plan](https://ahrefs.com/pricing). We also have a free version of our toolset, [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools), whereas SimilarWeb offers no such thing.

But before you make a decision, let’s take a look at a couple of other ways to find out how much traffic a website gets.

## Method 2. Look for an “advertise with us” page

Most bloggers receive so many *“I’m interested in advertising on your site; how much traffic does it get?”* emails that it makes sense to publish this information on a publicly accessible advertising page.

Here’s one such page from *geekwire.com*:

It states their monthly unique visitors, pageviews, and some other useful information (e.g., social stats). It’s not just the big sites that do this, either; I’ve seen a lot of individual bloggers with similar pages.

But how do you find these pages anyhow?

The easiest way is with the following [Google search](https://ahrefs.com/blog/google-advanced-search-operators/):

`site:website.com advertise with us`

Nine times out of 10, if they have such a page, it will be the first result.

Not seeing traffic stats on the advertising page? See if there’s a link to a “media pack;” a lot of sites include their traffic stats here.

Still, this tactic doesn’t always work for three simple reasons:

1. Not all websites have “advertise with us” pages;
2. Traffic stats aren’t always published on them;
3. Traffic numbers aren’t always up-to-date

If you do find an “advertise with us” page with traffic stats, always try to check if they’re up to date.

Most websites will list when they were last updated…

example from [TravelFashionGirl.com](http://travelfashiongirl.com/advertise/)

… but some don’t.

For example, the traffic stats shown on the *geekwire.com* advertising page haven’t been updated for at least a year.

If the website hasn’t updated their traffic stats recently (or simply fails to give a “last updated” date), don’t trust the numbers; they’re unlikely to be accurate.

## Method 3. Ask!

If you want to know accurate, up-to-date traffic statistics for a website, you’ll need to [get in touch](https://ahrefs.com/blog/find-email-address/) with the owner and ask them directly.

But most bloggers aren’t going to give out that information to a complete stranger, right?

You’d be surprised. Many bloggers are perfectly willing to share this data with those with a genuine reason for asking, such as:

1. You’re interested in buying their website.
2. You want to advertise on their site;

Here’s an example email that I’ve used in the past when trying to find out traffic statistics:

Sidenote.

We don’t advise sending emails like this unless you’re genuinely looking for advertising opportunities. Don’t waste people’s time!

Like I said, most bloggers will be happy to share up-to-date traffic numbers with genuine advertisers. Many will even screenshot Google Analytics data as proof.

While this method is typically the most reliable way to decipher traffic stats, it’s not 100% foolproof. Here’s why:

- **Some bloggers/webmasters will fabricate traffic stats** in order to sell advertising;
- **Not everyone has Google Analytics installed.** Many will rely on less than accurate analytics platforms (e.g., WordPress plugins) for their data;
- **Google Analytics can be easily misinstalled, meaning that data isn’t always accurate.** If reported traffic sounds too high, try checking their website for duplicate GA code. Alternatively, ask them what their [bounce rate](https://ahrefs.com/blog/bounce-rate/) is; a super-low bounce rate is often a good indicator of duplicate GA code.

So even if do reach out to the blogger and get those elusive traffic stats, we would still recommend verifying their legitimacy with third-party tools.

## Here are a few more tips for estimating website traffic…

Estimated traffic stats are a good starting point, but you can tell a lot about the popularity of a website by manually checking a few things, such as:

- # of comments on their posts (on average);
- # of YouTube video views;
- # of social shares;
- Engagement levels on their fan pages (i.e., Facebook page, Twitter, etc.)

If you take a look at the [Ahrefs blog](https://ahrefs.com/blog/), for example, you’ll see that virtually every blog post has a good number of comments.

Most readers don’t bother leaving a comment, no matter how great the content happens to be. So a blog that receives a consistently high number of comments will almost certainly be getting a significant amount of traffic.

Sidenote.

I’d also recommend checking the quality of comments when using this tactic; sometimes high comment counts are due to a site being spammed.

“Social shares” can be another indication of high traffic.

For example, if we check the **Top Content** report for *ahrefs.com* in [Site Explorer](https://ahrefs.com/site-explorer), we can see that most of the posts on Ahrefs’ blog receive tons of social shares.

And finally, there’s YouTube…

All [our videos on YouTube](https://www.youtube.com/channel/UCWquNQV8Y0_defMKnGKrFOQ/videos?flow=grid&sort=p&view=0) have hundreds or thousands of views.

If this amount of people are watching our YouTube videos, well, it’s probably safe to say that a fair few are visiting our site too.

## Final thoughts

Traffic estimation tools aren’t perfect. However, they do offer by far the quickest way to estimate traffic to sites you don’t own.

If you need accurate numbers, you’ll have to ask directly; there are no two ways about it.

Do you know of any other reliable ways to estimate/find website traffic stats? Let us know.
