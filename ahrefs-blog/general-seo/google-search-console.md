---
title: "How to Use Google Search Console to Improve SEO"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-search-console"
url: "https://ahrefs.com/blog/google-search-console/"
canonical: "https://ahrefs.com/blog/google-search-console/"
author: "Joshua Hardwick"
published: "2019-11-12T11:37:25+00:00"
updated: "2023-01-31T02:30:54+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T11:34:28+00:00"
status_code: 200
html_hash: "f8042ed8beadc0d74dbe213cd74820f298ca093da255dab5522a8b7b55cf2030"
clean_word_count: 3647
clean_char_count: 21328
---
# How to Use Google Search Console to Improve SEO (Beginner’s Guide)

Google Search Console is one of the most powerful, [free SEO tools](https://ahrefs.com/blog/free-seo-tools/) out there. But most people never use it for anything more than checking vanity metrics like clicks and impressions.

While there’s nothing wrong with looking at those things once in a while, they provide little value as standalone metrics.

Translation: staring at them isn’t going to [improve SEO](https://ahrefs.com/blog/how-to-improve-seo/) anytime soon.

In this guide, you’ll learn:

- [What Google Search Console is](#what-is-google-search-console)
- [How to set up Google Search Console](#how-to-set-up-google-search-console)
- [How to verify your website in Google Search Console](#how-to-verify-your-website-in-google-search-console)
- [How to submit a sitemap in Google Search Console](#how-to-add-a-sitemap-in-google-search-console)
- [How to add additional users to Google Search Console](#how-to-add-users-in-google-search-console)
- [How to use Google Search Console to improve your SEO](#how-to-use-google-search-console-to-improve-seo)

## What is Google Search Console?

[Google Search Console](https://search.google.com/search-console/about) (previously Google Webmaster Tools) is a free service from Google that helps you monitor and troubleshoot your website’s appearance in their search results.

Use it to find and fix technical errors, submit sitemaps, see backlinks, and more.

## How to set up Google Search Console

Sign in to [Search Console](https://search.google.com/search-console/about) with your Google account.

You should see a welcome message with two options. Select the first one, then enter your domain or subdomain (without the `http(s)://`).

Hit “Continue.”

DON’T WANT TO ADD YOUR ENTIRE DOMAIN?

Google [states](https://webmasters.googleblog.com/2019/02/announcing-domain-wide-data-in-search.html) that “domain properties show data for all URLs under the domain name, including all protocols, subdomains, and paths.”

This is perfect if you want a complete view of your website in Search Console, but what if you want to restrict data to a specific URL path? (e.g., domain.com/blog)

The answer is to use a URL prefix property instead. This adds only URLs under a specified address and protocol (i.e., HTTP/HTTPS, www/non-www).

Note that you can add both Domain and URL prefix properties for the same domain.

## How to verify your domain in Search Console

Before you can see any data in Search Console, you first need to verify ownership. This process differs according to the property type you added.

Jump straight to the instructions that apply to you:

- [I added a Domain property](#domain-property-verification)
- [I added a URL prefix property](#url-prefix-verification)

### Verification for a *Domain* property

Hit the instructions dropdown. Check if your domain is registered with any of the listed providers.

If so, select the provider and hit the “Start verification” button.

Sign in to your registrar account and follow the instructions.

You should see a message like this:

If your registrar isn’t on the dropdown, select “Any DNS provider.”

Sign in to your account with your domain provider, select your domain, then look for an option to manage DNS or Domain Name Servers.

Choose the option to add a TXT record, paste in the record from Search Console, then save it.

Go back to Search Console and hit “Verify.”

If the verification fails, keep trying. It can take a few minutes to go through.

HAVING ISSUES?

If your web host differs from your domain registrar, then you may find that your registrar doesn’t let you edit DNS records. In that case, you’ll need to edit DNS records on your hosting account instead.

If you’re doing this in cPanel, it’s super simple.

*Login to Cpanel > Zone editor > Manage (next to the domain) > Add record > Type > TXT*

Next, choose a name, copy and paste the TXT record from Search Console into the “Record” box, then hit “Add record.”

Go back to Search Console and hit “Verify.”

If the verification fails, keep trying until it works.

### Verification for a *URL prefix* property

Google offers a few ways to do this. Their default (and recommended) method is to upload an HTML file to your website. However, to keep things simple, we recommend choosing the Domain name provider option, then following [the instructions above](#url-prefix-verification).

## How to add a sitemap to Google Search Console

Sitemaps tell Google where to find important content on your website, and how they can crawl that content. We recommend that everyone submit a sitemap to Google via Search Console.

To do that, choose “Sitemaps” from the menu, paste the URL of your XML sitemap into the box labeled “Enter sitemap URL,” then hit “Submit.”

Sidenote.

 If you don’t already have a sitemap or aren’t sure where to find it, read [this](https://ahrefs.com/blog/how-to-create-a-sitemap/).

You should see a message like this:

## How to add a user to Google Search Console

Users are people with access to some or all of the data in Search Console.

There are three types:

1. **Owner**: Has full control over the property in Search Console, including the power to add and remove other users. There are two types of owner: *verified* and *delegated*.
2. **Full user:** Has view rights to all data within the selected property and the power to take some actions.
3. **Restricted user:** Has restricted view rights, meaning they may not be able to view all data.

**Recommended reading:** *[Managing owners, users, and permissions](https://support.google.com/webmasters/answer/7687615?hl=en)*

By default, when you verify a property in Search Console, you have *owner* privileges.

To add another user, go to:

*Search Console > Choose a property > Settings > Users and permissions > Add user*

Type their email address, then select either *full* or *restricted* access.

If you ever need to revoke or change their access, just return here.

## How to use Google Search Console to improve your SEO

Instead of going through each Search Console report in excruciatingly boring detail, we’re going to focus on a few actionable ways to use it to [improve SEO](https://ahrefs.com/blog/how-to-improve-seo/).

### 1. Improve rankings for underperforming keywords

Underperforming keywords are those where you don’t yet rank in positions one or two.

They’re underperforming because most people click one of the first two results, meaning that if you rank in lower positions, you’re missing out on tons of traffic.

For example, if you rank in position eight, roughly 1.8% of searchers will click on your result.

Bump that keyword ranking to position two, and the number jumps to almost 14%.

So let’s say the keyword in question has a monthly search volume of 1,000.

Ranking in position 8 gets you 18 visits from organic search per month, compared to 160 for position two.

| Position | CTR | Monthly organic search traffic |
| --- | --- | --- |
| #2 | 13.94% | 139 |
| #8 | 1.8% | 18 |

That’s **8x** more traffic just by jumping a few positions.

To find these underperforming keywords in Google Search Console, go to the “Search Results” report and toggle the average CTR and position data.

Next, scroll to the queries report and set the average ranking position filter to below 8.1, then sort the results by average position in descending order.

From here, it’s a case of skimming the list for underperforming keywords. I.e., those that you’re already ranking for in positions 3-8 and getting some traffic from.

Here’s one we found in our Search Console:

Our average ranking position for this keyword is 7.6, and we’re getting a CTR of 1%. That might seem quite low, but it’s not too far below the average for this position.

But here’s the important part: Despite this low ranking position, we’ve still averaged almost 1,200 clicks in the past three months and saw 121,000+ impressions. That’s around 400 clicks per month.

Sidenote.

 Impressions are the number of times we’ve appeared in the search results for this query.

So let’s click on this keyword and go to the “Pages” tab to see which page is ranking. From here, we can check whether the page is about the same topic and determine if there’s scope to further optimize it for this keyword.

Looks like there is optimization potential here, as the page that’s ranking is [our local SEO guide](https://ahrefs.com/seo/local-seo).

So it’s probably worth us performing an individual analysis of this page and seeing if we can boost its position by improving our [on-page SEO](https://ahrefs.com/seo/on-page-seo), adding some relevant [internal links](https://ahrefs.com/blog/internal-links-for-seo/), [getting more backlinks](https://ahrefs.com/blog/how-to-get-backlinks/), [improving page speed](https://ahrefs.com/blog/core-web-vitals/), or something else.

Just be sure to use common sense when going through this process. For example, our average ranking position for “google keyword planner” is 5.6, and we get thousands of visits per month from that keyword.

But if you look at the current US rankings for that query in [Ahrefs’ Keywords Explorer](https://ahrefs.com/keywords-explorer), we see that there’s only one result above us that **isn’t** from Google themselves.

So we’re unlikely to ever rank in position 1 or 2 for this keyword, no matter how hard we try.

The point here is that it makes sense to push some keywords more than others.

### 2. Optimize pages with high keyword rankings, but low CTR

Not every page that ranks #1 will get 30% of clicks. That’s just the average.

Some will perform better than average, and some will perform worse.

So what we can do is find the pages that perform worse than average, analyze why that’s the case, then see if there’s a way to boost their CTR to get more traffic.

To do this, head to the “Search results” report, toggle the average CTR and position data, then filter for keywords with average rankings below 3.1. These are the keywords for which you already rank in the top 3.

Sort the report by CTR in ascending order, then look for keywords with lots of impressions but lower-than-average CTR.

Here’s one we found:

Despite ranking in position three on average, our clickthrough rate is only 2.1% where it should be around 3-5x higher than that—especially as we’re definitively matching [search intent](https://ahrefs.com/blog/search-intent/) here.

So let’s Google this keyword and see if we can figure out what’s wrong.

Looks like Google is showing an ad, a featured snippet, a video carousel, and a [“people also ask” box](https://ahrefs.com/blog/people-also-ask/) above the “traditional” rankings where we are. Because these SERP features take up so much real estate, they’re almost certainly “stealing” clicks from us.

So the best course of action for us here would probably be to [optimize the page to try to win the featured snippet](https://ahrefs.com/blog/featured-snippets/), which gets 8.6% of clicks on average.

But averages can be misleading. So let’s take a look at the “Organic keywords” report in [Ahrefs’ Site Explorer](https://ahrefs.com/site-explorer) for the page that owns the snippet to see how much traffic it sends their way.

Looks like the featured snippet alone sends them 170 monthly organic visitors in the US, which is 38.5% of all US organic traffic to the page.

TIP: How to win more SERP real estate with video

For keywords with video carousels in the search results, there’s an opportunity to rank a YouTube video on Google. If you can do this and also rank in the ten blue links with your website, you can dominate the SERP. This is something we did for the keyword “SEO tutorial.”

Just be careful when doing this as not all keywords present a good opportunity.

For example, we get a measly 3.4% CTR for the query “link building tools” despite ranking between positions two and three for the past few months. But if we look at the search results, there are lots of ads above the organic results.

This tells us that this keyword may have commercial intent, so people are likely clicking ads instead of the organic results.

### 3. Fix sitemap issues

If there are issues with the sitemaps you submitted to Google, that may cause problems and confuse crawlers. This leads to wasted time and resources on their end, and can also cause them to index the wrong URLs in some cases.

To check for issues with submitted sitemaps, head to the “Sitemaps” report, click on the icon next to a sitemap, then click the “See index coverage” button.

You should now see a few tabs showing the number of errors, warnings, valid URLs, and excluded ones.

Looks like we don’t have any errors for our blog, but there is one URL under “Excluded.” If we click that tab, we see that one page has been excluded from the search results because it appears to be a duplicate of another submitted URL.

If we then click on this error, we see that the culprit is this URL related to guest blogging.

If we look at the HTTP status for this URL using [a free online tool](https://httpstatus.io/), we see that it [redirects](https://ahrefs.com/blog/301-redirects/) to [a newer post about guest blogging](https://ahrefs.com/blog/guest-blogging/).

The reason this happened is that the old URL is still set as published in WordPress, and the [SEO plugin](https://ahrefs.com/blog/best-seo-plugins-for-wordpress/) we’re using automatically adds all published URLs to our sitemap.

So all we had to do was delete this post, and the issue soon resolved itself.

IMPORTANT

Excluded pages are common in Google Search Console and aren’t always indicative of an issue. Errors and warnings tend to be more serious, so tackle those first.

### 4. Learn which content types and topics get the most backlinks

Backlinks are an important ranking factor. Google has told us this on numerous occasions, and we also found a clear positive relationship between organic search traffic and backlinks when [we studied 920 million pages.](https://ahrefs.com/blog/search-traffic-study/)

Sidenote.

Correlation ≠ causation.

So getting more backlinks to your content should be a priority if you want more traffic.

But what type of content should you publish to attract backlinks? And what topics should you talk about?

The best way to answer this question is to learn from the content you’ve already published.

To do that, go to the “Links” report, then click “More” on the “Top linked pages” report under the “External links” subheader.

Sort the report by “Linking sites” in descending order to see which of your pages have the most backlinks from unique websites, then look for patterns.

For example, four of the ten most-linked pages on our blog are studies.

This is a clear sign that original research tends to attract links in our industry, but this might differ for you.

For instance, while we can’t check the top linked pages for other sites in Google Search Console, we can in [Ahrefs’ Site Explorer](https://ahrefs.com/site-explorer). And if we paste in a popular web design blog and check the “Best by links” report, we see that many of the top-linked pages are inspirational list-style posts.

So this might be a better type of content to create if you want links in this industry.

### 5. Find pages that need more internal links or to be pruned

Imagine that you’re publishing a new page about protein powder.

If you already have a blog post about protein shake recipes and another about high protein foods, then it would make sense to add internal links from those to your new page.

There are two benefits to this:

1. They may help your new page get indexed faster.
2. They will transfer [PageRank](https://ahrefs.com/blog/google-pagerank/) to the new page, which may help it [rank higher in the search results](https://ahrefs.com/blog/how-to-rank-higher-on-google/).

Now, if there are posts and pages on your website that don’t have many or any internal links, then they’re probably old or forgotten posts. These usually won’t bring much traffic to your site or have much SEO value, so it’s often worth deleting them.

To find pages with few internal links, go to the Links report in Search Console. Click “More” under the “Top linked pages” report under the “Internal links” subheader.

Sort the list by “Internal links” in ascending order to see “forgotten” pages.

One of the first URLs that pops up for us is `/seo-case-studies/`, which has just three internal links.

If we visit the page, we see that it was published back in September 2015.

Because this isn’t exactly in-line with what we publish on the blog today, it would make sense for us to delete this post or redirect it elsewhere. In which case, we’d need to remove the few internal links that currently point to it.

To do that, click the URL in the “Top linked pages” report to see which pages have internal links.

IMPORTANT

Don’t delete pages on your site without making sure that they little or no organic traffic. To do that, go to the “Search results” report in Search Console, filter for the URL, then check the total number of clicks.

If you find pages with few internal links that are worth keeping, then it would make sense to either:

1. Add more relevant internal links to them;
2. Update the content and add more internal links where appropriate.

For example, we recently published [a post explaining what backlinks are and why they’re important](https://ahrefs.com/blog/what-are-backlinks/). But it looks like this page has only three internal links, so we could do with adding a few more where relevant.

To do that, we can search Google for something like `site:ahrefs.com/blog/ "backlinks"`, which will return all the pages on our blog that mention the word “backlinks.”

Because a lot of these will be relevant contextual internal linking opportunities, so all we need to do is visit the pages and add internal links where it makes sense.

### 6. Update pages that are losing organic traffic

Most pages won’t continue to get organic traffic forever because rankings tend to drop as they become outdated.

But how do you find pages with diminishing traffic in Search Console?

Go to the “Search results” report, then add a date range comparison to see stats for the past six months compared to the previous six months.

For this, we only care about clicks, so let’s toggle the “impressions” data off to clean things up.

Click on “Pages.”

Sort the report by Difference in ascending order to see the pages with the biggest traffic drops.

For us, one page that immediately stands out is [our list of free online marketing courses](https://ahrefs.com/blog/free-online-marketing-courses/). This has received around 40% less organic traffic in the last six months compared to the previous period.

If we click on the URL, then switch to the “Queries” report and sort by “Difference,” we can see which queries are sending us less traffic.

Looking at this page in [Ahrefs’ Site Explorer](https://ahrefs.com/site-explorer), it becomes clear why traffic is dropping. Our rankings for these have been dropping like a stone over the past six months or so.

Given that we published this post in mid-2018 and new online marketing courses are released all the time, it’s likely that Google is demoting us in the search results because our post is outdated.

So it might be worth us updating this post to see if we can reclaim some of that traffic.

IMPORTANT

Make sure to keep seasonality in mind when comparing six month periods like this. For example, if you have a post about Christmas trees, it would be perfectly reasonable to see lower traffic in the months from February to July than the six months prior for obvious reasons.

## Final thoughts

Google Search Console is a powerful free tool that shows a lot of data and insights about your website. But that’s its biggest limitation because SEO isn’t a single-player game, it’s multiplayer.

Ranking in Google means competing against other websites for the top spot. If you don’t understand the competitive landscape, there’s no way of knowing where you fall short or what you should do to improve rankings.

Therefore, it pays to combine insights from Google Search Console with those from a third-party competitive research tool like [Ahrefs](https://ahrefs.com/).

For example, Google Search Console tells us that we rank in position #6 on average for “[301 redirect](https://ahrefs.com/blog/301-redirects/).”

It even tells us how many backlinks that page has from unique websites.

But it can’t tell us who’s outranking us and why. Do they have more backlinks than us? Do they have tons of [authority](https://ahrefs.com/website-authority-checker)? Are the pages on strong domains?

If we look at this keyword in a tool like [Ahrefs’ Keywords Explorer](https://ahrefs.com/keywords-explorer), we see that all the pages outranking us are on stronger domains and have way more backlinks from unique websites.

Now we have some ideas as to [how difficult ranking for this keyword might be](https://ahrefs.com/blog/keyword-difficulty/), and that we likely need to [get more backlinks](https://ahrefs.com/blog/how-to-get-backlinks/) to compete.

Got more questions about Google Search Console? Leave a comment or [ping me on Twitter](https://twitter.com/joshuachardwick?lang=en).
