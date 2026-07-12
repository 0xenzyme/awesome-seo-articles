---
title: "How to Measure SEO Performance & Results (The Right Way)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "seo-performance-results"
url: "https://ahrefs.com/blog/seo-performance-results/"
canonical: "https://ahrefs.com/blog/seo-performance-results/"
author: "Michal Pecánek"
published: "2023-03-03T05:09:19+00:00"
updated: "2023-03-03T05:09:23+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T12:06:48+00:00"
status_code: 200
html_hash: "095b9d45891eee9b114948c082ad576a42b3fa419623a4ef2b6be655e3734866"
clean_word_count: 2804
clean_char_count: 16702
---
# How to Measure SEO Performance & Results (The Right Way)

If you tried to put together a list of metrics from all resources about SEO topics, you’d easily end up with hundreds of them. It can be overwhelming to make sense of it all. But you only need to focus on a few metrics that really matter for your SEO performance and the results it brings.

In this article, you’ll learn about just four SEO metrics that represent all you need to measure your SEO performance properly. On top of that, we’ll also go through multiple ways to measure impact on how your SEO performs.

Let’s dive in.

## How to measure SEO performance and results

In the big picture, there are only two ways to measure SEO performance and results: organic traffic and the money it makes for the business.

There are a lot of nuances involved, so let’s dive straight into three organic traffic metrics followed by conversions the traffic brings.

### Organic traffic

Organic traffic represents all non-paid clicks that come from search engines.

We all like to see the organic traffic curve going up, as it’s usually a sign of better performing SEO. But keep in mind that not all organic traffic spikes automatically translate into more sales (unless you monetize your website traffic by displaying ads).

The “Search results” report under the Performance tab in [Google Search Console](https://search.google.com/search-console/about) is going to give you the most accurate view of your organic traffic over time:

![Performance report in Google Search Console](https://ahrefs.com/blog/wp-content/uploads/2023/03/image6-1.png)

If you’re an established brand, it’s worth applying a query filter to exclude branded traffic for a more accurate view of your SEO performance:

For example, you can see that around half of the clicks to our blog are branded queries. The number of clicks went down from 1.37M to 686K after applying the filter:

Filtering out these branded queries can be considered as isolating your SEO performance from your overall marketing performance. SEO plays an important role in brand building, but it can’t take all the credit for it.

On top of this, you should also always compare your results over time, preferably over comparable time periods to avoid including one period that suffered from a seasonal swing.

The easiest way to do this is to click on the Date settings, head over to the Compare tab, and select a year-over-year comparison for the period you’re investigating.

Keep in mind that GSC only keeps 16 months of historical data, but it isn’t necessary to look further back to compare your current SEO performance.

### Keyword positions

Keyword positions refer to a website’s organic ranking positions in the search results for particular keywords.

While we were able to spot the trend with organic traffic in GSC, the specific keywords you rank for complete the story and provide you with all the needed context for your traffic’s relevance and worth.

That’s because you should care about ranking well for some keywords more than others. Generally speaking, the more relevant the keyword is to your product and business, the more valuable it is for you to rank well for it.

For example, HubSpot ranks for many keywords with enormous search volumes. But I’d bet that ranking first for “crm” is more valuable for it than the traffic from the rest of the keywords here combined:

That’s simply because HubSpot is a CRM, and it can easily create this association in each visitor’s mind. It may even start converting the traffic right away:

You can’t do that ranking for any of the remaining keywords from the screenshot.

To track your keywords, you’ll need a third-party rank tracking tool like Ahrefs’ [Rank Tracker](https://ahrefs.com/rank-tracker). Set up a project for your website, paste a bunch of keywords you want to track your rankings for, and you’re good to go.

You can get regular email alerts about the progress of your tracked keywords or just check the Rank Tracker reports once in a while:

### Share of voice

Share of voice (SOV) for organic search is the percentage of all clicks for your tracked keywords that land on your website. It measures how visible your brand is on the SERPs.

Consider this as keyword position tracking on steroids.

SOV is one of [the most important marketing KPIs](https://ahrefs.com/blog/marketing-kpis/) because it has a strong relationship with market share. Generally speaking, the higher your SOV, the bigger your share of the pie.

To measure organic SOV, paste a representative sample of keywords that matter to you into Ahrefs’ [Rank Tracker](https://ahrefs.com/rank-tracker). You should have this at least partially done if you’re actively tracking keywords already.

Note that these should be the main keywords that encompass what your target audience is searching for (don’t bother adding too many [long-tail keywords](https://ahrefs.com/blog/long-tail-keywords/)). It’s helpful to tag these most important keywords so you can easily filter them out from the rest of your rank tracking project:

When you enter the rank tracking project, head to the “Competitors overview” tab, apply your SOV tag filter if applicable, and check the “Share of Voice” column:

That’s it. SOV is a great [SEO KPI](https://ahrefs.com/blog/seo-kpis/) for everyone.

Further reading

- [What Is Share of Voice? How to Measure It Across Channels](https://ahrefs.com/blog/share-of-voice/)

### Organic conversions

Organic conversions are important actions your visitors from search engines make on the website, such as checking out, signing up, or subscribing to a service.

Conversion tracking is the only way to directly tie your SEO efforts to generating revenue. This is what likely matters the most to your boss, clients, or stakeholders.

Setting up [conversion tracking in Google Analytics 4](https://support.google.com/analytics/topic/10313214) isn’t rocket science, even though it may seem daunting at first. You don’t need any coding knowledge to do it. The most important thing here is making sure that you track the right conversions.

If you’re running an e-commerce store, the number of conversions, their value, and your average order value make the most sense for you. You’ll have to [set up specific e-commerce tracking](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce) to do that.

If you offer subscription-based software like us, your best bet is to track leads, trial sign-ups, paid subscriptions and, eventually, even each tier of new subscriptions.

Got the data collection right? In Google Analytics 4, go to *Reports > Engagement > Conversions* and filter organic traffic sessions using the “Edit comparisons” button:

There’s a lot to be said about the accuracy of conversion reporting and all the nuances regarding the attribution behind it. Generally speaking, you’ll get the most accurate data if:

1. You’re using GA4 (you should by now).
2. You use the data-driven attribution model as the default ([check](https://support.google.com/analytics/answer/10597962) *Admin > Attribution settings > Reporting attribution model*).
3. You have at least a few hundred conversions a month (to make sure that Google’s black box model has enough data to do its magic).

If you don’t have that many conversions on your website yet, it’s a good idea to also check your assisted conversions using different attribution models. Go to *Advertising > Attribution > Conversion paths,* select the conversion event you want to analyze, and check the impact of organic search throughout [customer journeys](https://ahrefs.com/blog/buyers-journey/):

I recommend checking [this resource about attribution modeling](https://www.kaushik.net/avinash/multi-channel-attribution-modeling-good-bad-ugly-models/) if you want to better understand this complex topic.

This wraps up metrics used to directly measure SEO performance and results. But we’re not done yet. You should also keep track of SEO metrics that impact your performance. Because if you ignore improving those, there may not be much of a performance.

## How to measure impact on your SEO performance and results

We need to focus on the three main SEO areas here: content creation and optimization, link building, and technical SEO.

Note that improving any of the metrics mentioned here doesn’t guarantee better SEO results. There are almost no guarantees in SEO. But these metrics are as close as it gets to increasing your organic traffic and conversions.

### Content metrics

There’s no SEO performance without content that Google is happy to push toward the top of its search results.

But measuring how good your content is and how well it’s optimized to rank at the top of the SERPs are factors that can’t be quantified using a single metric. We’ll have to rely on content quantity.

#### Content velocity

Content velocity measures the number of content pieces you publish during a given time period. Focus only on [content made to drive organic traffic](https://ahrefs.com/seo/seo-content) if you also publish other types of content like product updates, company announcements, PPC landing pages, or pages for social media.

If you’re constantly [creating great content](https://ahrefs.com/blog/how-to-write-great-content/), increasing your content velocity can be a good indicator of improving your SEO performance. Just note that you shouldn’t focus on new content only, as [updating your older content](/blog/republishing-content/) is equally important.

Example of an immediate improvement from updating older content. Chart is from the **Overview** report in Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer).

### Link building metrics

Backlinks are one of the most [important SEO ranking factors](https://ahrefs.com/blog/google-ranking-factors/).

You can either get them *passively* through mere exposure of your content to other creators who are happy to refer to you or *actively* by reaching out to these creators and asking them to link to you.

We can use this passive and active link building distinction for choosing the most appropriate metrics to assess the link building efforts.

#### New backlinks and referring domains

First, let’s start with passive link acquisition and its high-level overview.

Head over to the “Referring domains” graph in [Site Explorer’s](https://ahrefs.com/site-explorer) **Overview** report after plugging in your domain to see how you’re growing in this aspect over time:

It’s a good first check because there’s a clear positive correlation between referring domains and organic traffic:

However, a single graph doesn’t necessarily reflect your SEO success. You need to make sure that the websites linking to you are actually good and not just spam. You can do that in the **Referring domains** report:

This still isn’t a deep dive, though. Links matter on the page level too and, sometimes, [building more links from the same domain](https://ahrefs.com/blog/links-from-same-domain/) can be more beneficial than focusing on new referring domains.

You’ll need to head over to the **Backlinks** report for that:

Assessing link quality itself is too complex to dive into here, so let me point you to [our link building guide](https://ahrefs.com/seo/link-building#good-vs-bad-links) that covers all the aspects of high-quality backlinks.

#### Newly built backlinks

Link building isn’t easy. But at least its tracking is pretty straightforward when you engage in its active form.

That’s because you need to do link prospecting before you can even start reaching out to people and asking them to link to you. It’s the process of figuring out what backlinks you want to get. This ensures that you’re putting your time and effort into getting links that are really worth it.

All you need to do to measure your results here is to indicate “link status” in your link prospecting system. I used to do this in simple Google Sheets back when I was [doing the outreach](https://ahrefs.com/blog/email-outreach/) myself, and there’s no need to overcomplicate things for most:

You’ll either learn that your outreach was successful by receiving a positive reply or discovering the desired backlink in the **Backlinks** report. You can set up new [backlink alerts](https://ahrefs.com/alerts) to make this easier for you.

### Technical SEO metrics

Last but not least, we’re in the SEO discipline where a lot of work can’t be directly attributed to improvements in performance. Well, unless the technical SEO problems are so severe that it’s completely blocking your way to your desired results.

Or, as my colleague, [Patrick Stox, puts it](https://ahrefs.com/seo/technical-seo):

> Technical SEO is the most important part of SEO until it isn’t. Pages need to be crawlable and indexable to even have a chance at ranking, but many other activities will have minimal impact compared to content and links.

That said, there are three ways you can quantify your technical SEO efforts.

#### Page indexing errors in Google Search Console

These errors are anything that prevents your pages from being indexed when it’s not done intentionally using the noindex [robots meta tag](https://ahrefs.com/blog/meta-robots/).

There are many reasons why Google may deindex your pages or refuse to index them straight away. Keeping the number of these errors to a minimum is a sign of a solid technical SEO foundation.

You can find these errors in your GSC account in the Pages report under the Indexing tab. Make sure to switch the view scope to “All submitted pages” to only show errors for pages submitted in your [sitemaps](https://ahrefs.com/blog/how-to-create-a-sitemap/):

The lower the number of non-indexed pages, the better—given that sitemaps should only contain URLs that you want Google to crawl and index. Of course, this should be proportional to the size of the website. If you have millions of URLs, then (tens of) thousands of unindexed pages can be considered natural.

When you scroll down, you’ll see the reasons why those pages aren’t in the index:

You can click through those reasons to see a list of URLs affected by that error with a link to learn more about it. There’s also usually an instruction on how to fix it.

#### Health Score in Ahrefs’ Site Audit

Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) has a metric called Health Score that reflects the proportion of internal URLs on your website that don’t have technical SEO errors:

The Health Score offers a great proxy for your overall state of technical SEO. All you need is to set up a Site Audit project and start a crawl. You can do that for free as a part of [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools).

Every time AhrefsBot finishes crawling your website, it will update your Health Score and report accordingly.

However, keep in mind that Health Score can’t reflect and qualify the importance of each error in the context of your website. Let me illustrate this issue with an example:

A 404 [HTTP status code](https://ahrefs.com/blog/http-status-codes/) is one of those technical SEO issues that will trigger an error in any crawler. Showing that a resource wasn’t found is usually bad for both visitors and search engines. But there’s a huge difference between having a 404 on a well-converting page with high organic traffic and one that’s not very important.

For this reason, it’s always a good idea to dive deeper into the specific issues behind your Health Score.

#### Issues in Ahrefs’ Site Audit

To see the specific technical SEO issues, their importance, and how many pages they affect, go to the **All issues** report in [Site Audit](https://ahrefs.com/site-audit):

You can then click on the tooltip to learn what you need to know about the issue and how to fix it.

Then click through to see the affected pages and assess how the specific issue is hindering the potential success of those pages in the list.

### Final thoughts

Even though we’ve gone through quite a few metrics to properly measure and evaluate your SEO performance, I want to wrap things up by telling you to sometimes take a step back.

Don’t refresh your keyword rankings for a piece you published a few weeks ago. Rather, give your content and other SEO efforts the time to show results. According to our [survey](https://ahrefs.com/blog/how-long-does-seo-take/), it takes three to six months on average.

Once you start getting comfortable analyzing SEO metrics, you should start creating [comprehensive SEO reports](https://ahrefs.com/blog/seo-report-template/) customized to your business needs to take it to the next level.

Got any questions? Ping me [on Twitter](https://twitter.com/michalpecanek).
