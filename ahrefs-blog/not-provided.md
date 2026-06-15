---
title: "'Not Provided' in Google Analytics: How to Reclaim Your Keyword Data"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "not-provided"
url: "https://ahrefs.com/blog/not-provided/"
canonical: "https://ahrefs.com/blog/not-provided/"
author: "Mateusz Makosiewicz"
published: "2022-01-25T16:00:42+00:00"
updated: "2023-05-12T13:23:32+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2023_aging"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:54:08+00:00"
status_code: 200
html_hash: "e6e1e440ca41958c54a4144bc1e6dc5a8b6d79ca515702a3be9b95ed773f8b20"
clean_word_count: 2711
clean_char_count: 15871
---
# ‘Not Provided’ in Google Analytics: How to Reclaim Your Keyword Data

In Google Analytics, when you see “(not provided)” instead of the queries that led searchers to your website, this means Google is covering organic keywords data in the interest of protecting the privacy of searchers.

But no worries, this doesn’t mean you have configured your Google Analytics wrong or your data is lost. In this article, we’ll cover two solutions to the “not provided” problem and some tips on how to use your newly acquired keyword data:

- [Solution 1. Use Google Search Console](#1-use-gsc)
- [Solution 2. Use Ahrefs Webmaster Tools](#2-use-awt)
- [Three tips on how to use your keyword data](#3-tips-how-to-use-data)

Sidenote.

At the time of writing, Google Analytics 4, the successor of Universal Analytics, by default doesn’t show any organic keywords (or the “not provided” token) in the Acquisition report. To solve this problem, you can use the same solutions shown in this article.

## Solution 1. Use Google Search Console (free tool)

[Google Search Console](https://search.google.com/search-console/about) (GSC) is a free tool from Google designed to monitor and troubleshoot your website’s appearance in the search results. On top of revealing organic queries that led to your website, you can use GSC to find and fix technical errors, submit sitemaps, see backlinks, and more.

To see your organic keywords data, you need to set up the tool. You can learn how to do this in our [guide to setting up GSC](https://ahrefs.com/blog/google-search-console/).

Now, let’s see what type of data you will find in GSC. We’ll start with the main reason why you’d want to use GSC: You can see your organic keywords in the Performance report, which you’ll find here:

Once your data becomes available, you will see your keywords in the Queries tab located in the bottom panel:

Here’s what this data means:

- **Top queries** refer to Google Search queries (i.e., keywords) that generated impressions of your website. This means whenever your website’s URL shows up in Google’s search results (this can be web search, image search, video search, or Google News), the keyword that caused that impression will be reported here.
- **Clicks** are the number of clicks coming to your website’s URL from organic search results. Note this excludes paid Google Ads search results. Any click that takes the user outside of the search results is considered a click. And when someone clicks a link to a page, returns to the SERP (search engine results page), and then clicks on that page again, it counts only as one click.
- **Impressions** are the number of times any URL from your website appeared in the search results. Note this does not necessarily imply the searcher has seen your website. This just means it has been displayed.

It may take a while for Google to start showing your data. But the good news is once your data is in, you’ll see up to 16 months of retroactive data.

Sidenote.

While GSC offers insight into the queries that led searchers to your website, it doesn’t show the entire data. The first limitation is that Google doesn’t show very rare queries (performed only by a few users; Google calls those “anonymous queries”). Secondly, GSC will only show you up to 1,000 keywords in its interface.

Other tabs in the Performance report will show you clicks and impressions for:

- URLs of **pages** that were entered coming from the SERPs.
- **Countries** where the search came from.
- The **type of device** on which the search was performed.
- Grouped data for **specific types or features of search results** (Search Appearance tab). This data is reserved for search results other than typical blue links, such as recipe galleries, review snippets, videos, how-to results, and [more](https://support.google.com/webmasters/answer/7576553#zippy=%2Ccountries%2Cqueries%2Cdevices%2Csearch-type-filter-only%2Csearch-appearance).
- **Dates** (shown in Pacific Time Zone).

And so here it is. The first solution to “not provided” keywords is as simple as setting up GSC and waiting for your data to come in. But before we get into the second solution, let’s see what other things Google offers in the Performance report.

Starting from the top, we have the filters.

They allow you to display only data that meets certain criteria. By default, you can filter by search type and date. Additionally, the “Search type” filter allows you to compare sources:

You can also turn on additional filters for a particular query, page, country, or device.

Below the filters, you have the overview panel with another set of filters and a graph that dynamically displays the data set in filters and plotted against time. These filters also affect the data shown in the Keyword report. So if you tick the CTR filter, CTR data will be shown next to “Clicks” and “Impressions”:

Since we’ve already touched on clicks and impressions, let’s see what CTR (click-through rate) and average position are about:

- **CTR** is the percentage of organic impressions that result in a click.
- **Average position** is the average position of your site in the search results based on the site’s highest position whenever it appears in a search.

It’s worth noting that Universal Analytics and Google Analytics 4 users can integrate GSC data into Analytics to see all data in one tool.

**To integrate your Google Universal Analytics with GSC,** make sure you set up both services for the same property. Then access your Google Analytics and:

1. Choose your property (i.e., website you want to see data for).
2. Go to the **Admin** panel.
3. In the Product Linking section, choose **All products.**
4. Look for “Search Console” and click **Link Search Console.**
5. Follow the steps in the setup wizard to connect your GSC data with Universal Analytics data.

**To integrate your Google Analytics 4 with GSC**, make sure you have set up both services for the same property. Then access your Google Analytics and:

1. Choose your property (i.e., website you want to see data for).
2. Go to the **Admin** panel.
3. In the Product Linking section, choose **Search Console Linking**. If you don’t see that option yet, you may need to wait a few days; this is as the integration feature is still on the rollout.
4. In the Search Console linking panel, click **Link.**
5. Follow the steps in the setup wizard to connect your GSC data with Google Analytics 4 data.

That’s it for unlocking your organic keywords data in Google Analytics with the help of Search Console—our first solution. But that is not the end of your options for working with organic keywords. This brings us to the second solution for “not provided.”

## Solution 2. Use Ahrefs Webmaster Tools (free tool)

As already mentioned, GSC has its limitations, with the most important being the 1,000-keyword limit. If you need to work around this limit, you can consider an SEO tool like [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) (AWT).

It is our free tool that allows you to improve your website’s SEO performance and get more traffic from search. AWT has four main advantages over GSC when it comes to organic keywords. It shows you:

1. All known keywords. No 1000-keyword limit here.
2. SEO metrics for pages and keywords.
3. A depersonalized SERP snapshot with competitive data.
4. SERP features for every keyword.

Sidenote.

Additionally, with a premium Ahrefs account, you can [access your historical ranking data](https://ahrefs.com/pricing), as well as historical backlink data.

So let’s see how AWT works. Once you set it up, click on the “Organic keywords” widget in the project overview…

… and you will be directed to the **Organic keywords** report:

By default, you will be presented with the following data (from left to right):

- **Keywords** that searchers used to find your website—your solution to the “not provided” problem.
- **SF** stands for SERP Features that appear in search results for a keyword.
- **Volume** shows the number of average monthly searches for a keyword.
- **Keyword Difficulty (KD)** gives an estimate of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
- **Cost Per Click (CPC)** shows the average price that advertisers pay for each ad click in paid search results for a keyword.
- **Traffic** shows an estimation of the monthly organic search traffic that your target gets from a given keyword.
- **Change (next to Traffic)** refers to the change in traffic between your selected dates.
- **Position** is the top-ranking position of your target for a keyword.
- **Change (next to Position)** refers to the change in position between your selected dates.
- **URL** refers to the URL that is ranking in search results for a keyword.

Above your keyword data, there are filters you can use to display data that meets certain criteria, such as the country where the keyword comes from, position in SERP, search volume, or search for a particular keyword.

As seen in the above screenshots, there’s a lot you can do with [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools). Here, we’re only showing a fragment of the functionality related to organic keywords. In the video below, we go through other features that can help you in SEO and share how to set up the tool.

https://youtu.be/ipTk-qGrNlc

So there you have it—two different solutions to the “not provided” problem. Both are free to use. So go ahead and try them both without any commitments. You can even run them in parallel.

In fact, if you already have GSC up and running, it’s easier to set up [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools), as you can verify your property in it using GSC. On top of that, you can see the GSC data overview right in AWT.

One last thing worth knowing about these solutions is they display data using different sources. Google displays data from its own services, and [Ahrefs aggregates data from multiple sources](https://ahrefs.com/big-data).

## Three tips on how to use keyword data

Knowing which organic keywords bring traffic to your website is great. This is because you can use that knowledge to improve your SEO and grow your organic traffic. Here are three quick ideas to do that. Note that we will be using both GSC and [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools).

### 1. Optimize pages with underperforming keywords

Underperforming keywords are those keywords where you don’t rank in positions #1 or #2. The reason being most people click one of the first two search results. And if you’re not one of those results, you’ll miss out on a lot of organic traffic.

Ranking #6 for a competitive keyword is really good, but that position gives us less than half of the organic traffic that higher-ranking pages get.

To find your underperforming keywords using [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools), access your **Organic keywords** report by clicking on the “Organic keywords” widget in the project overview. Once in the report, set the country you want to see data for. Also, set the Position filter to “3.”

In a flash, you will get a list of keywords that rank in position #3 or lower. These are the keywords that are underperforming.

Now you can browse through that list to create a shortlist of pages for optimization. A good practice is to use the SERP tool to see who ranks above you in the SERPs. That way, you can gauge the probability of outranking them. To illustrate, there is little chance for us to outperform Google for the keyword “google keyword planner.”

As for the optimization itself, here are a few ideas on what you can do:

- Improve [on-page SEO](https://ahrefs.com/seo/on-page-seo)
- Add more relevant [internal links](https://ahrefs.com/blog/internal-links-for-seo/)
- Get more [backlinks](https://ahrefs.com/blog/how-to-get-backlinks/)

### 2. Optimize pages with low CTR but high keyword ranking

If you remember from the previous sections, CTR is the percentage of organic impressions that result in a click to your website.

Generally, a page with a high ranking on the SERP should analogically have a high CTR. This is as people tend to click search results with high rankings. And the higher the CTR, the higher the traffic to your site.

But in some cases, pages ranking high can have a lower than average CTR. With the help of GSC, you can quickly find these pages, analyze the cause of their performance, and see if there’s a way to improve CTR.

To do this, go to the Performance report in GSC. Tick the Average CTR and the “Average position” filters. Then filter for keywords with average rankings below 3.1. This way, you will see pages that you already rank for in the top three.

Now sort the report by CTR in ascending order. Then look for keywords with lots of impressions but low CTR. Here’s an example of such a keyword.

As you can probably guess, for position #3 in the SERP, the CTR here should be way higher. Meaning, we’re somehow missing out on a lot of potential traffic that could go to our article on [DIY SEO](https://ahrefs.com/blog/diy-seo/).

In the case of this keyword, the cause of low performance can be seen just by analyzing the SERP. Our webpage, though ranking high, is “buried” under ads, a featured snippet, a video carousel, and a [People Also Ask box](https://ahrefs.com/blog/people-also-ask/). Those elements of the SERP probably get the most attention from searchers.

So a viable solution, in this case, is to try and optimize our article on DIY SEO to win a [featured snippet](https://ahrefs.com/blog/featured-snippets/).

### 3. Find easy keywords to rank for

As you may know, a single page can rank for hundreds of keywords. (We even did a [study on this subject](https://ahrefs.com/blog/also-rank-for-study/).) Some of the keywords can even cause a page to be ranked unintentionally. This means Google can associate a webpage with a keyword even if you haven’t specifically targeted the keyword with a page.

When that happens, this is a sign you should create new content optimized for that “unintentional” keyword. If so, you could get more traffic than what you currently receive. And the lower the KD, the easier it is generally to create content that will rank high.

You can look for low-difficulty keywords using the KD metric in [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools). Just open the **Organic keywords** report and put something low like “20” in the KD filter. Then sort the results by volume to spot opportunities with the highest potential. Here’s an example from a blog on web design:

As you can see, the “tinder ui” keyword has a high search volume. But it doesn’t bring any traffic to the page that ranks for it because of the low position in the SERP. However, creating new, dedicated content targeting that keyword could help the blog rank higher and get additional organic traffic.

## Final thoughts

In this article, we’ve seen two different solutions for incomplete keyword reports in Google Analytics (both Universal Analytics and Google Analytics 4). Both Search Console and [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) will provide insight into the organic keywords that brought people to your website and/or made your website appear in the SERPs.

But if you want to go beyond just knowing what your organic keywords are, I recommend keeping both of those free tools running in parallel. This way, you will have access to more data and can spot more opportunities for growth, as shown in the three SEO tips above.

And if you’re serious about growing organic traffic, tools like GSC and AWT are simply must-haves.

Want to learn more than just the SEO tactics mentioned here? Head to our [complete guide on SEO](https://ahrefs.com/seo).

Got questions? Ping me [on Twitter](https://twitter.com/m_makosiewicz).
