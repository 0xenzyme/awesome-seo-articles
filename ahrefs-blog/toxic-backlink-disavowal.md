---
title: "I Disavowed \"Toxic Backlinks\": Here's What Happened"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "toxic-backlink-disavowal"
url: "https://ahrefs.com/blog/toxic-backlink-disavowal/"
canonical: "https://ahrefs.com/blog/toxic-backlink-disavowal/"
author: "Joshua Hardwick"
published: "2024-08-29T13:34:32+00:00"
updated: "2024-08-29T13:34:37+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
fetched_at: "2026-06-12T12:13:24+00:00"
status_code: 200
html_hash: "e5816bac56504de69343e11dda83d4e6711bd4a95c8fadd530d51fe9b97b3697"
clean_word_count: 1145
clean_char_count: 7048
---
# I Disavowed “Toxic Backlinks”: Here’s What Happened

On July 26th 2024, I exported all “toxic” and “potentially toxic” backlinks to three of our blog posts from a well-known SEO tool. There were 129 URLs in total, which I disavowed in Google Search Console.

![Disavowing the links in GSC](https://ahrefs.com/blog/wp-content/uploads/2024/08/disavowing-the-links-in-gsc.png)

After disavowing, **traffic (as reported by GSC) fell by 7.1%**:

Sidenote.

Google began rolling out a Core Update on August 15th, which is why I cut the experiment short to only 20 days. My plan was to leave it running for a full month, but I think just shy of three weeks is enough time to see results anyway.

Before disavowing, according to GSC, traffic to these posts was trending *slightly* upward:

After disavowing? Slightly downward:

However, Ahrefs’ organic traffic estimates tell a slightly different story. Visibility is trending slightly downward *before* disavowing…

… and *after* disavowing:

I asked Patrick Stox how he’d interpret this. Here’s what he said:

> I would personally look at Ahrefs data here. Average search volume in Ahrefs will show if it impacted rankings and visibility, although our data may be slower to update than GSC. GSC can have seasonality, luck, etc. involved, so it’s not as consistent of a measure.
>
>
>
> Patrick Stox, Product Advisor & technical SEO [Ahrefs](https://ahrefs.com/blog/author/patrick-stox/)

Makes sense. In this case, it looks like **disavowing had little to no impact on rankings/visibility overall**. But let’s take a closer look at the data…

## Test pages

The data above is for all three pages combined, so let’s take a look at what happened to each page individually.

### Page 1: 12% traffic drop

This page was [our SEO pricing guide](https://ahrefs.com/blog/seo-pricing/).

For the 20-day period before the disavow, the post got 574 organic visits. This fell by 12% to 505 visits in the following 20 days (when the disavow was in place).

Before disavowing, organic traffic to this post was flatlining:

After disavowing, it’s still flatlining:

Ahrefs data tells a slightly different story…

Before disavowing, estimated organic traffic was trending *slightly* downward:

After disavowing, it’s flatlining:

Long story short? **Disavowing *might* have had a small positive impact,** but I believe it’s more likely that a long downward trend is just finally leveling off.

### Page 2: 8.25% traffic drop

This page was [our list of top YouTube searches](https://ahrefs.com/blog/top-youtube-searches/).

For the 20-day period before the disavow, the post got 291 organic visits. This fell by 8.25% to 267 visits in the following 20 days (when the disavow was in place).

Before disavowing, organic traffic to the post was trending upward:

After disavowing, it’s trending downward:

Ahrefs’ data tells the same story…

Before disavowing, estimated organic traffic was trending upwards:

After disavowing, it’s trending downwards:

The results seem pretty clear: **disavowing likely had a negative impact**—especially with a big drop in estimated traffic around ten days after.

### Page 3: 12.82% traffic growth

This page was [our list of top Bing searches](https://ahrefs.com/blog/top-bing-searches/).

For the 20-day period before the disavow, the post got 156 organic visits. This grew by 12.82% to 176 visits in the following 20 days (when the disavow was in place).

Before disavowing, organic traffic to this post was trending upward:

After disavowing, it’s still trending upward:

Ahrefs tells a slightly different story here…

Before disavowing, estimated traffic was trending ever so slightly (it really is slight!) downward:

After disavowing, it’s the same story:

So, **disavowing seemed to have little or no impact here**…

## What does all of this mean?

My interpretation of these results is that disavowing “toxic backlinks” basically did nothing. It seemed to hurt one page a bit, *maybe* slightly help another, and have no impact on another.

**In short, blindly disavowing “toxic backlinks” reported by SEO tools is unlikely to have much if any positive impact—at least according to our data.**

Is this a surprise? Not really. Google has been [saying](https://www.reddit.com/r/SEO/s/cb4d85RVro) this pretty much forever:

That said, while the most likely outcome of disavowing is basically nothing, it’s definitely still risky. Disavowing “toxic backlinks” could tank your traffic, as this reply to John on Reddit illustrates:

Does this mean that disavowing is *always* a bad idea? No. If you already have a manual penalty for unnatural links or a very large number of manipulative links (e.g., paid links), then you should absolutely disavow.

[Google](https://support.google.com/webmasters/answer/2648487?hl=en) recommends this…

> You should disavow backlinks only if:
>
> You have a considerable number of spammy, artificial, or low-quality links pointing to your site,
>
> AND
>
> The links have caused a manual action, or likely will cause a manual action, on your site.

… and so does [Marie Haynes](https://searchengineland.com/toxic-links-disavows-seo-383324):

> There are two situations where we will recommend to our clients a thorough link audit followed by filing a disavow:
>
> - The site has a manual action for unnatural links in GSC.
> - The site has a very large number of links that we feel the webspam team would consider to be “manipulative”.
>
>
>
> Marie Haynes, CEO [Marie Haynes Consulting](https://twitter.com/Marie_Haynes)

If that’s not you, then disavowing “toxic backlinks”—especially those reported by SEO tools—probably isn’t the best idea or use of your time. As Marie Haynes [said](https://searchengineland.com/toxic-links-disavows-seo-383324), they’re unlikely to be truly toxic anyway:

> I find that the truly toxic links…the ones that could have the potential to harm your site algorithmically are rarely returned by an SEO tool.
>
>
>
> Marie Haynes, CEO [Marie Haynes Consulting](https://twitter.com/Marie_Haynes)

That said, plenty of SEOs don’t agree with this advice and are convinced that disavowing “toxic backlinks” helps. If that’s you and you’re seeing good results from disavowing, fantastic! Don’t let me stop you 🙂

For everyone else, it’s probably not the best idea…

This isn’t the first time we’ve studied this either. My colleague Patrick [disavowed **all** links to these same three posts back in 2021](https://ahrefs.com/blog/impact-of-links/)—and traffic fell off a cliff:

We didn’t specifically disavow “toxic” backlinks here, but links clearly still help pages rank. If an SEO tool wrongly labels some of these helpful links as “toxic” and you disavow them, it could harm your traffic.

My advice? Spend your time [improving your SEO](https://ahrefs.com/blog/how-to-improve-seo/), not disavowing “toxic backlinks” that might actually be helping you!

Got questions? Disagree? Ping me on [LinkedIn](https://uk.linkedin.com/in/joshuahardwick28) (or [X](https://twitter.com/joshuachardwick?lang=en) if you insist!)
