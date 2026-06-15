---
title: "Squarespace SEO vs. WordPress: 3.6M Domains Studied"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "squarespace-seo"
url: "https://ahrefs.com/blog/squarespace-seo/"
canonical: "https://ahrefs.com/blog/squarespace-seo/"
author: "Si Quan Ong"
published: "2019-11-01T00:01:32+00:00"
updated: "2021-06-29T16:57:00+00:00"
categories:
  - "Data & Studies"
  - "General SEO"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-12T12:11:01+00:00"
status_code: 200
html_hash: "6104340465509850fe49bb8ca865789c24820107f13e914124756347a4f28b4a"
clean_word_count: 1621
clean_char_count: 9862
---
# Squarespace SEO vs. WordPress: 3.6M Domains Studied

Is Squarespace bad for SEO? Or are haters just jumping on the bandwagon? Let’s find out.

When it comes to search engine optimization for Squarespace sites, SEOs are divided. Some think it’s the worst thing in the world:

While others think it’s good enough:

What is the truth?

To answer this question, we decided to run a similar study to the one we did for [Wix SEO](https://ahrefs.com/blog/wix-seo/). In total, we studied 1.8 million Squarespace websites and 1.8 million WordPress websites.

In this post, I’ll go through our findings, and you can decide for yourself which CMS is best for you.

## The data

Before I talk about the findings, I should let you know where we got our data and which metrics we studied.

If you’ve read our [Wix SEO study](https://ahrefs.com/blog/wix-seo/), you’ll notice that we used the same methodology.

### The sample

Like the previous study, we used the [BuiltWith](https://builtwith.com/) API to pull our sample of 1.8 million Squarespace and WordPress websites.

Unfamiliar with how this works?

Essentially, BuiltWith is a tool that shows you which technologies websites use. Enter any domain, scroll to the “Content management system” section, and you’ll see which CMS the site uses.

For example, Pixar uses Squarespace.

### The SEO metrics

For the [SEO metrics](/blog/ahrefs-seo-metrics/), we pulled them from [our own API](https://ahrefs.com/api). Here are the four metrics we acquired:

- **Number of referring domains:** The number of unique linking websites;
- **Number of “dofollow” referring domains:** The number of unique linking websites with potentially value-passing links;
- **Estimated organic traffic:** The estimated number of monthly organic visits from Google;
- **Domain Rating (DR):** The overall strength of a website’s backlink profile on a scale from 0–100.

## The study

As with the Wix SEO study, we split the dataset into two “buckets.”

- **Bucket #1:** Sites with some organic traffic
- **Bucket #2:** Sites with 100+ monthly organic visits

Here’s what we found:

In Bucket #1, 45.5% of WordPress websites get some monthly search traffic, compared to only 15.1% of Squarespace sites.

For Bucket #2, 8.1% of WordPress websites get more than 100 monthly search visits, compared to 1.6% for Squarespace.

As you can see, on average, WordPress websites get significantly more organic traffic than Squarespace websites.

If you recall, when compared to WordPress, only 1.4% of Wix sites get some monthly search traffic, and 0.06% get >100 search visits.

While Squarespace sites get less search traffic as compared to WordPress, in general, they seem to do better than Wix sites.

That said, don’t take this to mean that one CMS is superior to the rest.

When it comes to [ranking in Google](https://ahrefs.com/blog/how-to-rank-higher-on-google/), there are plenty of factors at play. And most of them are unrelated to the platform you use.

We also decided to take a look at the average Domain Rating, the number of dofollow referring domains, and monthly search traffic for each platform.

Based on this, it looks like WordPress sites win… right?

Not quite.

As our data scientist repeatedly cautions:

> When measuring the central tendency of data, it’s best to calculate both mean and median and compare the two values.
>
> Generally speaking, if both values are not too different from each other, we use the mean. But a considerable difference between them indicates that the data is skewed.
>
> When the data is skewed, large values have an ENORMOUS impact, making the mean larger than the actual distribution that the data suggests.
>
> In this case, the median is a more appropriate idea of the data distribution.
>
>
>
> Loveme Felicilda, Data Science [Ahrefs](https://ahrefs.com/)

This concept is the central premise behind the popular joke: “Bill Gates walks into a bar and everyone inside becomes a millionaire…on average.”

Simply put, if there are outliers in the dataset (e.g., certain sites that get more search traffic than the rest), the average numbers will get skewed to a higher value, making it inaccurate.

As such, it’s better to look at the median values, which we checked as well:

From the results, there isn’t much difference in the numbers. This goes to show that there are indeed high-traffic and high-authority WordPress websites in our sample that skew the average towards WordPress, as compared to Squarespace.

Sidenote.

We found the same thing when we compared WordPress versus Wix.

### Diving deeper

To level the playing field and eliminate possible bias from our samples, we did three things:

#### 1. We leveled the sample sizes across both platforms

There were way more WordPress domains than Squarespace domains in both buckets. To reduce bias, we balanced the number of analyzed domains, resulting in **~280,000 domains** studied for each platform.

#### 2. We excluded exact-match keywords

To exclude traffic from branded queries, we removed the keyword *xyz* if the domain was *xyz.com.*

#### 3. We found the number of top 10 keyword rankings

We pulled the number of keywords that each site in our dataset ranks for in Google’s top 10 search results.

We also summed up the amount of organic traffic each site gets from those keywords.

…

Here’s what we found for domains with some search traffic:

Once again, when it comes to the average number of top 10 keyword rankings and the sum of traffic from those keywords, WordPress beats Squarespace. However, since the median numbers are pretty close, this indicates that there are outliers that skew the samples.

So, unfortunately, we can’t say anything conclusively about these results.

Now, let’s take a look at Bucket #2:

In this case, it looks like the mean and median closely align.

As such, our data seems to suggest that WordPress websites typically have a marginally higher number of top 10 rankings than Squarespace websites on average. WordPress sites also get more organic traffic from those keywords when compared to Squarespace.

Interestingly enough, when you compare the Domain Rating and the number of dofollow referring domains, Squarespace comes out on top.

## The conclusion

Like the Wix SEO study, the results are somewhat inconclusive.

Based solely on our study, we can’t say whether one CMS is better than the other.

It’s also difficult to isolate factors like “skill-level” in studies like this. After all, platforms like Wix and Squarespace tend to attract less SEO-savvy people than WordPress.

So, as one person pointed out on Twitter, this could be the reason why WordPress sites tend to perform better in search.

> That’s because people who use Wix are on average a lot less SEO savvy than people using WordPress, not necessarily because one platform is better than the other 😉
>
> — Andrea Bosoni (@theandreboso) [June 12, 2019](https://twitter.com/theandreboso/status/1138860805838053376?ref_src=twsrc%5Etfw)

## Why then, do SEOs not like Squarespace?

I’ll be completely transparent here. Before I wrote this post, the Squarespace team reached out to us.

They read our study on Wix SEO, and they were wondering if we were going to conduct something similar for Squarespace. They also volunteered to give us a demo on the SEO capabilities of their platform.

Given that I had no experience with the platform at all, I agreed. And I learned a lot during that short video call.

For starters, when it comes to basic on-page SEO tasks like changing [title tags](https://ahrefs.com/blog/title-tag-seo/), meta descriptions, and URLs, Squarespace works just fine. (They even have a tab for “SEO”.)

You can also verify your site in Google Search Console, and see your data within the platform.

But unfortunately, there are some restraints when it comes to customizability and technical SEO.

For example:

### 1. Page speed optimization

Squarespace handles this on their end. If you want faster load times, there’s only a [limited number of things](https://support.squarespace.com/hc/en-us/articles/360022529371-Reducing-your-page-size-for-faster-loading) you can do.

Considering that [pagespeed is a ranking factor](https://webmasters.googleblog.com/2010/04/using-site-speed-in-web-search-ranking.html), some SEOs might find this disadvantageous.

### 2. Robots.txt & XML sitemaps

Squarespace automatically generates the [robots.txt](https://ahrefs.com/blog/robots-txt/) file and [XML sitemap](https://ahrefs.com/blog/how-to-create-a-sitemap/) for your site. However, it is not possible to make edits to either of those.

For bigger sites, this may not be ideal.

### 3. Canonicalization

By default, Squarespace adds self-referencing URLs for you. You can add a custom [canonical](https://ahrefs.com/blog/canonical-tags/) URL using the advanced page injection option, but then you end up with multiple conflicting canonicals on the page.

### 4. Alt text for images

This is more an annoyance rather than a big issue, but Squarespace doesn’t make it easy to add [alt text](https://ahrefs.com/blog/alt-text/). I had to go through [their documentation](https://support.squarespace.com/hc/en-us/articles/206542357-Adding-alt-text-to-images) to understand how to do this.

It would be much better if they had a field for [alt texts](https://ahrefs.com/blog/image-seo/) as WordPress does.

## Final thoughts

So, which is better: Squarespace or WordPress?

If you have a small, simple site that doesn’t need much technical optimization, Squarespace isn’t a bad choice. (Plus, I’m a fan of their templates.)

But if SEO matters to you and it’s a critical acquisition channel, then you might want to consider other platforms (not only WordPress) for better customization and scalability.

What do you think of the study? Let me know in the comments or [on Twitter](https://twitter.com/siquanong).
