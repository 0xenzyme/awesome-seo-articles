---
title: "How to Measure SEO ROI (Incl. 6 Challenges of Calculating It)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "seo-roi"
url: "https://ahrefs.com/blog/seo-roi/"
canonical: "https://ahrefs.com/blog/seo-roi/"
author: "Michal Pecánek"
published: "2022-05-16T07:56:08+00:00"
updated: "2022-11-28T08:53:25+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2022_old"
fetched_at: "2026-06-12T12:07:52+00:00"
status_code: 200
html_hash: "41d381945b9368bb9df88ba0e1fdd5459072c1308ef4d8273e71fed31d0b10d6"
clean_word_count: 3081
clean_char_count: 18700
---
# How to Measure SEO ROI (Incl. 6 Challenges of Calculating It)

SEO ROI (return on investment) estimates the business value of all SEO activities in contrast to their cost. It’s one of the most common topics any SEO consultant or manager has to address when it comes to allocating marketing budgets and resources.

In its essence, calculating ROI is quite easy and straightforward. But in SEO, there are many caveats you should be aware of. Those ultimately make measuring and interpreting ROI one of the most complex and challenging problems you can face in SEO.

But we’ve got you covered and will share the ins and outs of measuring SEO ROI. In this article, we’ll go through these:

- [How to measure SEO ROI](#1-how-to-measure-roi)
- [Six main challenges of measuring SEO ROI](#2-six-main-challenges-of-measuring-seo-roi)
- [Alternative approach to measuring SEO ROI](#3-alternative-approach-to-measuring-roi)

Let’s dive in.

## How to measure SEO ROI

The ROI formula for SEO is simple in essence:

SEO ROI = (value of organic conversions - cost of SEO investments)/cost of SEO investments

In other words, you need to divide the SEO profit by the associated SEO costs. Let’s expand on each variable because it can be quite tricky to get to some final numbers.

### 1. Calculate your SEO investments

Organic search is often viewed as a “free traffic” channel, but that’s devaluing the huge time investments that usually go into it. And those are not the only associated SEO costs.

SEO investments can usually be divided into four categories:

1. **In-house employees** – It’s obvious to count in dedicated SEO and content creation staff, but you should also account for the required designer and developer resources.
2. **SEO freelancers and agencies** – This is straightforward. And if you hire SEO freelancers or agencies, they can and, in many cases, should be the ones measuring SEO ROI.
3. **SEO tools** – Count in all your subscriptions for dedicated SEO tools like Ahrefs. You can also partially include the costs of tools used by the broader marketing department if you also use them for SEO (e.g., Similarweb, BuzzSumo, [HARO](https://ahrefs.com/blog/haro-link-building/), PR software, etc.).
4. **Content distribution and link building** – As we know, SEO doesn’t end with publishing content. Consider partially including costs of content promotion efforts. Also, if you buy links as one of your link building tactics, count that in. Google and many SEOs warn against buying links, but the reality of link building is often different.

Combine these costs over your desired period of time. Now, choosing the time period is one of the big challenges. We’ll expand on that later, but you can start with monthly comparisons for the sake of simplicity.

### 2. Calculate the value of your organic traffic conversions

You need proper conversion tracking in Google Analytics (or its alternatives) to get this number. Segment the traffic to “organic” and check the value of conversions that you want to account for in the ROI calculations:

The type of conversions and how you assign conversion values will differ from business to business.

It’s pretty straightforward for e-commerce businesses, as they send the value of sales conversions to GA.

But, for example, it may be more complex for lead generation businesses. For them, it can be helpful to assign dollar values to new marketing or sales-qualified leads.

Further reading

- [How to Use Google Analytics to Improve SEO Performance](https://ahrefs.com/blog/google-analytics-for-seo/)
- [13 Google Analytics Tracking Mistakes (And How to Fix Them)](https://ahrefs.com/blog/google-analytics-tracking-mistakes/)

### 3. Account for the value of assisted conversions

Historically, we often had to get used to working with the default “last non-direct click” attribution model in Universal Analytics.

It’s a flawed model in most cases because it assigns 100% of the conversion credit to a single marketing channel closest to the conversion event.

Here’s a good sports analogy for understanding this: It’s similar to you only praising players who score a goal. Goalkeepers and those responsible for defense won’t be too happy.

Your website likely drives organic traffic at all [stages of the customer journey](https://ahrefs.com/blog/buyers-journey/). Even one piece of content can target multiple steps in the [marketing funnel](https://ahrefs.com/blog/marketing-funnels/):

For example, people may land on 10 of your articles from Google and then convert after clicking a search or retargeting ad. In that case, you’ll want to see that initial organic search contribution.

The shift to Google Analytics 4 (GA4) partially solves this problem via utilizing a [data-driven attribution (DDA) model](https://support.google.com/analytics/answer/10596866#zippy=%2Cin-this-article) by default (more on that later).

The conversions and the values you see in all GA4 reports already account for the partial contributions of organic traffic to the overall website conversions. If you already use GA4, you don’t technically need to dive into the assisted conversions report.

Nevertheless, it’s always a good idea to check and analyze the conversion paths of your visitors and how each channel contributes to conversions.

For Universal Analytics, I already covered the process of [analyzing assisted organic conversions](https://ahrefs.com/blog/seo-kpis/#assisted-organic-traffic-conversions).

In GA4, go to *Advertising > Attribution > Conversion paths*, select the conversion event you want to analyze, and check the impact of organic search throughout customer journeys:

You can also filter the organic traffic only to get the most relevant data, as seen in the table below:

The screenshots and data come from the official GA4 demo account, so the conversion paths are simplistic and won’t be like that in most cases. Also, feel free to play around with other attribution models to get some interesting insights there.

I can imagine this simplified process of calculating SEO ROI only raises more questions, so it’s time to dive deeper into all the nuances and caveats.

## Six main challenges of measuring SEO ROI

You should be aware of these challenges to calculate SEO ROI and all the other related metrics as best as you can. I’ll provide a few recommendations to apply in practice along the way.

### 1. Marketing attribution is inherently flawed

Marketing attribution is one of those topics that provoke many discussions. We have experts on completely opposite sides of the fence.

Some say it’s almost never worth the resources to try and solve it properly and that you should trust your gut instead. Others are convinced that proper attribution can be almost always reasonably achieved.

One thing is for sure. Attributing conversions to marketing channels is inherently flawed regardless of the attribution model used. Heuristic models like the last non-direct click will just be much more flawed than the new DDA.

Customer journeys and touchpoints are often much more complex than analytics software makes them look.

Here’s a great example of a specific buyer’s journey of a SparkToro customer. (SparkToro is the SaaS company of [Rand Fishkin](https://twitter.com/randfish), who is one of those experts on the “better trust your gut” side of things.)

Let’s take a look:

Taken from [Rand’s article about attribution](https://sparktoro.com/blog/provable-marketing-attribution-is-a-boondoggle-trust-your-gut-instead/).

As mentioned earlier, organic search traffic is a marketing channel that can span the whole customer journey from awareness to retention. Attribution is especially tricky here, so let’s discuss the implications further.

DDA is a solid solution for this that will likely shift many people closer to the “proper attribution is possible” camp. But it still doesn’t solve many other problems. It’s a black box that gets more accurate with increasing traffic and conversions.

Unless you have “higher” hundreds (or ideally thousands of conversions) a month, I’d still take those numbers with a huge grain of salt. And ultimately, no matter the attribution model, you still don’t see data from sessions where the tracking code wasn’t fired (e.g., ad blockers and quick bounces).

### 2. The connection between SEO and brand-building

Let’s say you browse through some YouTube videos and see someone talking about an interesting product. You Google that brand or product, head to the website, and make a purchase. Organic traffic gets 100% attribution for the conversion.

You can come up with many other scenarios where the only organic search interaction is through branded queries. SEO gets the credit when it shouldn’t.

On the other hand, you can have strong SEO with high search visibility on the SERPs throughout the whole funnel. It’s perfectly capable of converting many prospects from start to finish by itself.

But social media ads, display ads, and search ads get in the way and make a bigger contribution to the conversion just because they’re more prominent.

DDA in GA4 partly solves this problem, but it still can’t take into account the branding aspect of SEO. The brand awareness and salience you build by being seen in top-of-the-funnel content either through your own content production or by outreach aren’t things we can measure well.

Not being able to segment branded vs. non-branded organic traffic with conversion data makes all of this difficult to assess.

### 3. We can’t measure the retention impact of SEO

Ahrefs is a great example of this. We produce product-led content that’s constantly educating our (potential) customers about all the ways they can use our tools to solve their SEO and marketing problems.

As we neither use GA nor store cookies, I can’t back this up with data. But I’d estimate that 20-30% of organic traffic visits to our blog come from people who are already Ahrefs customers.

The retention impact of SEO, in this case, can be divided into two categories:

- As people learn to squeeze more out of our toolset, they start using the tool more and more, which leads to [lowering churn rates](https://ahrefs.com/blog/churn-rate/).
- Content about tools and features included in higher-priced plans makes some people upgrade their monthly subscriptions.

In other words, SEO has the power to increase the customer lifetime value, as many pieces of content also overlap with the retention and nurturing stages of the marketing funnel.

But again, it is difficult or even impossible to take this impact into account when calculating the SEO ROI.

### 4. Huge time discrepancies between “investment” and “return” periods

The variables in calculating ROI are the investments and returns over certain time periods. But when we look at that on the whole website and business level, it’s impossible to tie specific investments to specific returns in SEO.

This is where the simplified principle of comparing the same monthly periods of “investments” and “returns” fails.

SEO can take a lot of time to provide returns on the investment. Yes, you can certainly have [quick wins](https://ahrefs.com/blog/seo-wins/). But nothing is guaranteed.

A good alternative to choosing arbitrary time periods is to be more granular and start calculating ROI on the category, page, or keyword level. You can measure well the “return” of ranking with particular pages and can also know most of the “investments” that went into it.

We’d still omit technical SEO and other related costs and efforts that are usually applied to a broader scope of the website at once. But these partial costs are unlikely to shift a specific page from positive to negative ROI, so feel free to leave them out for simplicity’s sake—as long as you’re aware of them.

### 5. SEO testing has limited capabilities

One way to better understand the contribution of a marketing channel to overarching [marketing objectives](https://ahrefs.com/blog/marketing-objectives/) is to stop running campaigns on it for a while and see what happens.

For example, we ran such an experiment with PPC channels:

> We’ll be reallocating our paid traffic budget (~$200k💰) for December away from the Google/Facebook—and into sponsoring the industry’s best creators and thought leaders.
>
> — Ahrefs (@ahrefs) [November 24, 2021](https://twitter.com/ahrefs/status/1463495813900820488?ref_src=twsrc%5Etfw)

What you’d be looking for here is marketing incrementality—the lift the channel brings on top of a specific outcome that happens anyway.

Let’s say the outcome we want to monitor is conversions, so we’d be looking at how many conversions we’d still get if we halted specific marketing activities.

The problem with SEO is that you can’t just turn it off. Or well, you can. But no sane marketer will ever deploy [noindex robots meta tag](https://ahrefs.com/blog/meta-robots/) on the whole website.

Organic search is simply one of the most important channels for many businesses, and sabotaging your own SEO can have long-term detrimental effects.

This doesn’t mean that you can’t run SEO experiments and tests. You absolutely can. There’s been quite a lot of development and [coverage about SEO testing](https://ahrefs.com/blog/seo-testing/) in recent years.

But for the purpose of measuring incrementality and ROI, it is close to impossible for the vast majority of websites to come up with a good hypothesis and valid testing scenarios.

### 6. Forecasting future ROI

Last but not least, as SEOs, we’re often asked about the expected outcomes and ROI of certain SEO activities. This can get even more complicated, as [SEO forecasting](https://ahrefs.com/blog/seo-forecasting/) is a discipline on its own and can clash with all the aforementioned challenges as well.

Don’t try to beat around the bush. Instead, face the uncertainty head-on. [Setting up SEO objectives](https://ahrefs.com/blog/seo-goals/) and making sure we’re on the right track to achieving them is a crucial part of our job. Having good communication skills is another.

A good way to approach this is to consider the following factors when coming up with specific numbers:

- Past SEO performance of the page(s) or a website and its competitors
- Compounded traffic potential of the content in question
- Estimation of an average conversion rate (can be applied just to the bottom-of-the-funnel content for simplicity’s sake)

For SEO performance, a good start is to look up your website in Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer), head over to the Performance chart in the **Overview** report, and add all your relevant competitors:

You can also check the traffic value (estimated monthly cost of traffic from all keywords a site is ranking for if paid via PPC):

And the number of organic pages:

This should give you an idea about the relationship between the content output and organic traffic in your niche. It still leaves out link building activities and technical SEO, but that will only complicate things here even more.

As for the traffic potential, paste all the keywords you plan to target with the new proposed content into Ahrefs’ [Keywords Explorer](https://ahrefs.com/keywords-explorer) and take a look at the Traffic Potential (TP) column:

TP in Ahrefs shows how much organic traffic the #1 ranking page for your target keyword receives from all the keywords that it ranks for in your target country. You can either analyze this on a keyword-to-keyword basis or export the list to sum up the column values.

And lastly, we have the conversion. You should already have this data available for similar content in the tracking software, and you can also look up and/or survey other websites in your niche.

By the end of this, you can extrapolate and estimate the outcome of all the proposed SEO activities. Or you can go more “granular,” as that information will always be more accurate and easier to communicate.

Of course, stay away from any guarantees. But saying something along the lines of “I expect that [SEO activity] can increase traffic by X, which could bring Y conversions” can work when you set up the right expectations.

## Alternative approach to measuring SEO ROI

To be honest, I’m in the camp advocating that it’s not even necessary to calculate the ROI of your SEO and related content marketing efforts. This is especially true if you can prioritize content creation and other SEO tasks well.

Our CMO, Tim Soulo, wrote a great Twitter thread about the ROI of content marketing that’s highly relevant to this topic and also shows how we think about that in Ahrefs:

https://twitter.com/timsoulo/status/1374242996531597315

So what’s the alternative? Choosing and tracking the most suitable [SEO KPI](https://ahrefs.com/blog/seo-kpis/) that’s not based on conversions.

The best candidate for this KPI, in most cases, is search visibility. It’s the SEO version of one of the most important marketing KPIs, [share of voice (SOV)](https://ahrefs.com/blog/share-of-voice/), which measures how visible your brand is in the market.

That’s important because there’s a [strong relationship](https://ahrefs.com/blog/share-of-voice/#why-sov-is-important) between SOV and market share. Generally speaking, the higher your SOV, the bigger your share of the pie.

For the most accurate tracking of search visibility, paste the keywords that matter to you into Ahrefs’ [Rank Tracker](https://ahrefs.com/rank-tracker). Note that these should be the main keywords that encompass what your target audience is searching for (don’t bother with [long-tails](https://ahrefs.com/blog/long-tail-keywords/)).

From there, head to the Competitors Overview tab and check the Visibility column:

That’s it. As long as you see a long-term growth trend in the search visibility for your website, you should be confident that your SEO efforts are paying off.

I know this isn’t a possible alternative for many teams that are required to show “money metrics,” but it’s definitely worth tracking as one of your SEO KPIs.

## Final thoughts

I could have taken the easy path here and just touched the surface without diving into all the challenges and caveats of calculating SEO ROI. But this is what stakeholders care about the most, so we should all be knowledgeable and confident in communicating these matters.

Many topics covered here can be in-depth standalone articles. If you’re interested in learning more about everything related to marketing analytics and attribution, I highly recommend you check out the [blog of Avinash Kaushik](https://www.kaushik.net/avinash/sitemap/).

Got questions or interesting insights regarding SEO ROI? Ping me [on Twitter.](https://twitter.com/michalpecanek)
