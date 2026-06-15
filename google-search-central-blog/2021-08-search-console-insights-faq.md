---
title: "Google Search Console Insights behind the curtains"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2021-08-search-console-insights-faq"
url: "https://developers.google.com/search/blog/2021/08/search-console-insights-faq"
canonical: "https://developers.google.com/search/blog/2021/08/search-console-insights-faq"
author: "Daniel Waisberg"
published: "2021-08-09T00:00:00+00:00"
updated: "2021-08-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:39:38+00:00"
status_code: 200
html_hash: "f22942a2744bc1ae6a0881d42472aae7a2dca85308f992c09d742b933405af85"
clean_word_count: 1681
clean_char_count: 10660
---
# Google Search Console Insights behind the curtains

[Search Console Insights](https://search.google.com/search-console/insights/about) is
an experience that makes both Google Search Console (GSC) and Google Analytics (GA) data available and tailored
to content creators and website owners. Following last month's [announcement](/search/blog/2021/06/search-console-insights),
we received great feedback from the community, and also questions about the data.

In this post, we provide answers to some of those questions and clarify some points. For example, if you're trying
to compare the data you see in GSC Insights to what you see in GA, you might find some differences - why is that?

## Google Search Console Insights Frequently asked questions

### Why can’t I see Google Analytics data in Search Console Insights?

If you associate GA to Search Console properly, you will have access to more insights that can help you understand
your content's performance. If you do not create an association you'll have access only to the **Google Search card**.

There are a few reasons why your GA data may not be appearing on GSC Insights:

1. **Your GSC property is not associated with a GA property**: visit the help center to
   learn [how to create
   an association](https://support.google.com/webmasters/answer/9419894#analytics). In particular, if you have separate properties for your HTTP and HTTPS traffic on GSC,
   make sure to associate the property that receives the most traffic or consider
   [verifying a domain property](https://support.google.com/webmasters/answer/9008080#domain_name_verification) to include all your traffic in one place. Note that you can't link
   [Google Analytics 4](https://support.google.com/analytics/answer/10089681) properties
   for now, but we're working on it.
2. **You do not have sufficient permissions on GA**: if your GSC property is associated with a GA
   property, and you still cannot see GA data, check that you have [Read
   and Analyze permissions](https://support.google.com/analytics/answer/2884495) to the associated GA property.
3. **You have the wrong GA view selected in GSC**: GSC Insights brings GA data for a specific GA
   view under the associated property. If you have no views under the property, we won't be able to populate data.
   You can see or change the selected view in the Search Console [Associations
   page](https://search.google.com/search-console/settings/associations).

### Why is the data I see in Google Analytics different from Search Console Insights?

First, it's important to understand that GA and GSC data are different in many ways, as described in this
[help center article](https://support.google.com/analytics/answer/1308626#diff).
The data is different by definition, since one represents activity that happened on Google Search, and the
other represents user behavior on your site. In addition, here are a few things to look for specifically:

- **Page title and URLs:** other reports in GSC are based on URLs, while GSC Insights uses
  GA's page title dimension. For each page title, there may be several URLs; GSC Insights extracts the most
  prominent canonical URL to fetch Search data.
- **Date ranges:** GSC Insights shows GA data for the last 28 days (last day might use partial data),
  sometimes compared to the previous 28 days. GA's and GSC's default time ranges are different, so make sure to
  check the dates are the same when comparing them. Also note that while you can set your time zone on GA,
  GSC Insights will always use Pacific Daylight Time, so even specific days might differ if compared.
- **Metrics:** GSC Insights combines GA metrics (pageviews, average time on page), with
  Search metrics (clicks, average position). Those metrics represent different aspects of your site, and they
  are calculated differently.

### How does Search Console Insights choose “new content”?

![Search Console Insights new content card](/static/search/blog/images/search-console-insights-new-content.png "Search Console Insights new content card")

The **New content card** shows pages in your site that got their first pageviews in the last 28 days.
For each title, we may also indicate the top Search queries for the leading canonical URL. Content is sorted
by recency, and must have at least a few views to appear. There are 3 main pieces of information we
use to populate this card:

- We start by checking page titles that received traffic in the last 28 days but didn't receive any
  traffic in the year before.
- We apply several rules to clean the data, and filter pages less likely to be new content; for example,
  title changes, comment pages, internal search result pages, and others.
- We filter out translations of the same content and keep the top-performing title. We don't aggregate
  translated pages' metrics to avoid confusion with the metrics in the GA interface.

If we didn't report your new content, it doesn't mean that it has no GA traffic or that it isn't indexed.
GSC Insights can show content that is not indexed when pulling data from GA. Also, note that new content
does not depend on the first crawl time, your content doesn't have to be crawled or indexed to appear
in this card.

### How does Search Console Insights choose the “most popular content”?

![Search Console Insights most popular content card](/static/search/blog/images/search-console-insights-most-popular-content.png "Search Console Insights most popular content card")

The **most popular content card** shows your top-performing page titles by pageviews in the last 28 days.
For each title, we may also indicate the top Search queries for the leading canonical URL. To see more Search
data for this content, you can click it and drilldown to the page overview.

If the URL is not under the associated GSC property, we won't be able to bring Search data.

### How does Search Console Insights choose the referring links from other websites?

![Search Console Insights referring links card](/static/search/blog/images/search-console-insights-referring-links.png "Search Console Insights referring links card")

The **referring links from other websites card** shows how users discover your site's content
through links to your content from other sites.

Our goal with this report is to provide you with a proxy on how many entrances were generated by a specific
referring page. On GA, when you look at traffic from a specific referral, it includes all pageviews in
the current session. On GSC Insights, for each incoming session from a specific referral, we'll count
only one pageview; the traffic you see in this card is only a subset of the referral traffic you are used
to seeing in GA.

Note that we do not use this logic in the **top traffic channels card**; pageviews are usually
lower in the **referring links card** when compared to the Referral channel.

### How can clicks be lower than pageviews in the Google Search card?

There are three main reasons for clicks being lower than pageviews:

- Each click can trigger more than a single pageview - other pageviews during the session are also attributed
  to *google / organic*. Learn more about [the way sessions are defined and classified](https://support.google.com/analytics/answer/2731565).
- GA pageviews for *google / organic* include more surfaces than web search results, such as Discover,
  Image Search and Video Search.
- GA and GSC don't necessarily report on the same group of pages. For example, you might have a GSC account
  that includes only your HTTP pages while the GA view you chose reports on both HTTP and HTTPS.

### What do the different badges in the GSC Insights cards mean?

We introduced badges on GSC Insights to help you focus your attention on interesting patterns in the data.
For now, there are three different badges:

1. **High avg. duration**: the content has a high average duration compared to your site's
   other pieces of content. This might be content your audience found engaging.
2. **Top 5 results**: the average position on Google Search (*organic*) of your content
   in the last 28 days for the given query is five or less.
3. **Trending x%**: represents a comparison between the last 28 days and the previous performance.
   This badge is only shown when the trend is significantly greater than the general site trend.

## Learn about the data, find tips, and more resources

To learn more about each of the cards available on GSC Insights, click the little hat, as shown in the
screenshot below. There, you'll find more context about the data, and tips on how to interpret it. For
example, there are short descriptions of what a change in the chart means and definitions of the metrics
used in charts and tables.

![Search Console Insights little hat](/static/search/blog/images/search-console-insights-education.png "Search Console Insights little hat")

If you have any questions or feedback, click the **send feedback** button available on GSC Insights,
reach out to us [on Twitter](https://twitter.com/googlesearchc), or post a
question in the [Search Central community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],["Google Search Console (GSC) Insights combines GSC and Google Analytics (GA) data, tailored for content creators. Key points include: associating GSC with GA to access more insights, understanding potential data discrepancies between GSC and GA, and how to link the properties. The \"New content\" card displays pages with first pageviews in the past 28 days, while \"most popular content\" shows top-performing pages by pageviews. The \"referring links\" card shows traffic from other websites. Badges indicate high engagement, top search rankings, or significant trends.\n"]]
