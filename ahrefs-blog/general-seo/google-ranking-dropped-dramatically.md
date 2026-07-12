---
title: "Google Ranking Dropped Dramatically? (Here's What to Check)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-ranking-dropped-dramatically"
url: "https://ahrefs.com/blog/google-ranking-dropped-dramatically/"
canonical: "https://ahrefs.com/blog/google-ranking-dropped-dramatically/"
author: "Chris Haines"
published: "2023-05-11T05:39:03+00:00"
updated: "2024-06-16T22:14:28+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T11:34:13+00:00"
status_code: 200
html_hash: "557cd1d13be411297d863e267f912cac11676431fe74aff5ba7cc41293fd3535"
clean_word_count: 3219
clean_char_count: 19745
---
# Google Ranking Dropped Dramatically? (Here’s What to Check)

It can be alarming if your website’s Google rankings drop suddenly.

But before you make any changes, it’s important to check certain things first.

## 1. Check for any Google algorithm updates

[Google’s algorithm updates](https://ahrefs.com/google-algorithm-updates) are among the most common ways your website’s rankings can be negatively impacted.

Google doesn’t like low-quality or misleading results appearing at the top of its organic search results, so it runs regular [algorithm updates](https://ahrefs.com/google-algorithm-updates) to preserve the quality of its search index.

Updates are announced on Google’s [status page](https://status.search.google.com/summary). So it’s worth checking if any dates align with your website’s ranking drops.

![Google ranking updates, via Google
](https://ahrefs.com/blog/wp-content/uploads/2023/05/image27-1.png)

It takes time to align these dates against your organic traffic data, so a faster way to understand the impact is to use a tool like Ahrefs.

To do this, head to Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer), plug in your domain, and scan the Ⓖ updates at the bottom of the **Overview 2.0** organic traffic chart.

The highlighted Ⓖ symbol indicates that there was a Google update at each of these points.

Hovering over the Ⓖsymbols will give you more detailed information about the updates.

## 2. Check your organic traffic in Ahrefs’ Site Explorer

Once you’ve established there’s been a Google update, you’ll need to check its date against your total organic traffic to see if there’s been a drop at the same time.

To check your organic traffic in [Site Explorer](https://ahrefs.com/site-explorer), you can:

1. Plug in your domain and scroll down to the **Overview 2.0** chart.
2. Uncheck everything apart from “Avg. organic traffic.”
3. Set the timeline to “All” and “Weekly.” This helps you to see the complete timeline for the organic traffic, giving you a better idea of how significant the drop is.

I’ve highlighted the most recent traffic drop for this website. Let’s see if we can work out why this happened. Let’s zoom in and change the timeline to “1Y,”hovering our cursor around the time of the drop.

The **March 2023 Core Update** roughly aligns here.

It may have contributed to the loss of traffic, but we can also see that the *exact* date of the organic traffic drop doesn’t align with the release of this update.

So we can’t say that this algorithm update caused the drop. In this situation, it’s usually best to keep investigating.

If your website’s organic traffic drop does align exactly with an update, then a Google update has likely impacted you.

## 3. Check your top traffic-driving keywords

Once you’ve established a significant drop in organic traffic, you’ll want to know which of your website’s keywords have lost rankings.

To do this, head to the **Organic keywords** report in [Site Explorer](https://ahrefs.com/site-explorer). I like to compare keywords year on year (YoY), so let’s add a YoY “Compare” filter.

We can see that in the “Change” column, there’s been a significant drop for this website’s top keyword, “yamaha motorcycles.”

Let’s head over to Ahrefs’ [Keywords Explorer](https://ahrefs.com/keywords-explorer) by clicking on the keyword “yamaha motorcycles.”

Scrolling down to the SERP overview, we can see what happened if we make a year-on-year (YoY) comparison.

Google has switched the `/motorcycle` page for the homepage. So there may be an issue with the `/motorcycle` page.

For reference, in [Site Explorer](https://ahrefs.com/site-explorer), we can see the exact date of the drop is March 14.

Let’s remove the comparison and plug this date into the SERP overview in [Keywords Explorer](https://ahrefs.com/keywords-explorer).

Using the SERP overview, we can see that this page was a 404 page on that date. If we change the date to March 16, 2023, we can see that this page disappears from the SERPs.

As this date matches up, it’s likely to be the reason for the significant drop in traffic for this website.

Using [Site Explorer](https://ahrefs.com/site-explorer) and [Keywords Explorer](https://ahrefs.com/keywords-explorer) in conjunction is a great way to diagnose the reasons for ranking drops.

## 4. Check any recent technical changes to the site

Technical issues can impact your Google rankings. You’ll need to run a website crawl to determine these issues.

In my opinion, the easiest way to identify technical issues with your site is to run a crawl using Ahrefs’ [Site Audit](https://ahrefs.com/site-audit).

To set one up, head to Site Audit, click “+ New project,”and follow the prompts.

![Navigating to Ahrefs' Site Audit

Once you’ve completed the crawl, you’ll see an “Overview” screen similar to the screenshot below.

![Overview example, via Ahrefs' Site Audit

This page gives a bird’s-eye view of technical issues and monitors your website’s [health score](https://help.ahrefs.com/en/articles/1424673-what-is-health-score-and-how-is-it-calculated-in-ahrefs-site-audit).

Once you’ve clicked on a specific issue, click “Why and how to fix.” A sidebar will then appear, explaining the problem and how to fix it—this information is critical to helping you solve your technical issues.

!["Why and how to fix" closeup, via Ahrefs' Site Audit

If your website crawl reveals that you’ve got many technical issues, it’s worth spending time fixing each problem until your overall health score improves.

Once you’ve done this, you’ll be able to eliminate the possibility of any technical issues impacting your site’s Google rankings.

Tip

Technical issues can occur any time but often happen during a [website migration](https://ahrefs.com/blog/website-migration/). Running [Site Audit](https://ahrefs.com/site-audit) before and after your migration allows you to compare crawls to see if there’s been an increase in technical issues following the migration.

Now we know how to set up and analyze a [Site Audit](https://ahrefs.com/site-audit), let’s look at some specific technical issues that often result in lost rankings and organic traffic.

### 4XX Pages

![Ahrefs 404 page, via ahrefs.com

4XX pages are error pages. You’ll probably be most familiar with the classic “404 page not found.” When these types of pages occur, it can result in lost traffic.

If we return to our earlier website (`/motorcycle` page) example in [Keywords Explorer](https://ahrefs.com/keywords-explorer) and scroll down to the SERP overview, we can see it’s a 404 page.

![404 page, via Ahrefs' Keywords Explorer

But are there any more 404 pages on this site? Let’s return to the **Organic keywords** report and click through other top keywords, such as “r7” and “yamaha r1.”

![List of keywords, via Ahrefs' Keywords Explorer

If we click through on the keyword “r7” to [Keywords Explorer](https://ahrefs.com/keywords-explorer), scroll to the SERP overview, and set the date to March 14, 2023, we can see that this keyword also has a [404 status code](https://ahrefs.com/blog/http-status-codes/).

![404 page shown in SERP overview, via Ahrefs' Keywords Explorer

Repeating the process with the “yamaha r1” keyword, we can see this page is also a 404 page on March 14, 2023.

![404 page shown in SERP overview, via Ahrefs' Keywords Explorer

It seems fair to conclude that this website’s top traffic-driving pages were dead pages.

Although we have quickly used [Keywords Explorer](https://ahrefs.com/keywords-explorer) and [Site Explorer](https://ahrefs.com/site-explorer) to find this information, the same information can be found using [Site Audit](https://ahrefs.com/site-audit).

This is what it will look like once your crawl has been completed and where you can identify the 404 or 4XX pages in the report.

![4XX issues, via Ahrefs' Site Audit

### Canonicals

![Canonical tag illustration, via Ahrefs Blog

Lack of or poorly implemented [canonical tags](https://ahrefs.com/blog/canonical-tags/) is another technical issue that can cause problems for your site.

When it comes to identifying them, you can spot-check them on a page-by-page basis using Ahrefs’ [SEO Toolbar](https://ahrefs.com/seo-toolbar), or you can run a [Site Audit](https://ahrefs.com/site-audit) crawl to get a full view.

I’ve highlighted below the types of issues that can be flagged by the **Overview** report.

![Canonical tag issues, via Ahrefs' Site Audit

For more tips, check our [“canonical tags” beginner’s guide](https://ahrefs.com/blog/canonical-tags/) to learn more.

### Redirects

Forgetting to add or poorly implementing redirects is one of the most common reasons for a drop in rankings and organic traffic.

There are a couple of simple points to remember with redirects:

- Use [301 redirects](https://ahrefs.com/blog/301-redirects/) to redirect one webpage to another
- Try to avoid [redirect chains](https://help.ahrefs.com/en/articles/79340-what-are-redirect-chains) and [redirect loops](https://help.ahrefs.com/en/articles/2754354-what-does-the-redirect-loop-issue-in-site-audit-mean)

Detecting these redirect issues is best done using Ahrefs’ [Site Audit](https://ahrefs.com/site-audit). Simply run a crawl of your website and then check the **Redirects** report to get a view of the issues.

![Redirects report, via Ahrefs' Site Audit

Check out our [redirects for SEO](https://ahrefs.com/blog/redirects-for-seo/) guide to learn more.

### Robots.txt

Changes to a website’s [robots.txt](https://ahrefs.com/blog/robots-txt/) file can also impact how Google crawls your website. Sometimes you, or another stakeholder, can accidentally block some essential pages.

You can keep track of your robots.txt file changes if you run a regular crawl of your site using Ahrefs’ [Site Audit.](https://ahrefs.com/site-audit)

For each crawl, **Page Explorer** stores the details of your robots.txt file, making it easy to understand if any changes have been made to the file that could negatively affect the website.

![Disavow store, via Ahrefs' Site Audit

If you’ve seen a ranking drop while migrating your site, it’s worth heading to your robots.txt file to see if you are blocking the crawling of any search engine bots or essential pages of your website.

Check our [robots.txt beginner’s guide](https://ahrefs.com/blog/robots-txt/) to learn more.

## 5. Check your competitors’ rankings

If you’re confident your website’s [technical SEO](https://ahrefs.com/seo/technical-seo) is in order, it’s worth checking to see if your competitors have outranked your website on some of its keywords.

It may sound obvious, but this is another common reason a website loses rankings. Unfortunately, sometimes your competitors are better at SEO than you are.

The quickest way to monitor a competitor’s rankings is by plugging its domain in [Site Explorer](https://ahrefs.com/site-explorer) and heading to the **Organic keywords** report.

In this example, I’ve entered Backlinko’s domain.

![Organic keywords report with positions highlighted, via Ahrefs' Site Explorer

Here, you can see the rankings of your competitor’s website and performance week on week, month on month, or any other custom date comparisons.

### Check your tracked keywords against theirs

Another way to check your competitors’ recent activities is with Ahrefs’ [Rank Tracker](https://ahrefs.com/rank-tracker).

![Competitors overview report, via Ahrefs' Rank Tracker

The great thing about this tool is that you can compare the rankings of your competitors and your website side by side.

Here’s an example of me looking at three different competitors’ rankings.

![Competitors' and ahrefs' rankings for "google discover," via Ahrefs' Rank Tracker

Once you’ve established that a competitor performs better than you on specific keywords, you might want to learn more about their total strategy. It’s worth checking out our guide to [keyword competitor analysis](https://ahrefs.com/blog/keyword-competitive-analysis/) to learn more about this topic.

## 6. Check your links

As links are a [confirmed Google ranking factor](https://ahrefs.com/blog/google-ranking-factors/) (yes, [they still matter](https://ahrefs.com/blog/impact-of-links/)), here’s what you should check:

### Check for broken links

Keeping track of all broken links to your website can be a time-consuming task. Many websites rarely check broken links that point to them.

Using [Site Explorer](https://ahrefs.com/site-explorer), we can look at any website’s broken links by plugging in a domain and heading to the **Broken backlinks** report.

Here’s an example of the broken backlinks for the website we looked at earlier.

![Broken backlinks report, via Ahrefs' Site Explorer

There are 3,442 groups of [follow links](https://ahrefs.com/seo/glossary/dofollow-link) that we can fix here.

If you can’t see anything else wrong with your site, looking at this report is an excellent place to start.

The report shows this website has lost three high Domain Rating (DR) links from high-profile sites.

![Broken backlinks examples, via Ahrefs' Site Explorer

### Do a backlink audit (and if you need to, disavow)

Once you’ve checked your broken links, it’s a good idea to run a [backlink audit](https://ahrefs.com/blog/backlink-audit/) on your site if you believe there is an issue with the overall quality of your website’s links.

In some instances, you may see [unnatural links](https://ahrefs.com/seo/glossary/unnatural-links) pointing to your site that may impact your rankings. Here are some examples of what Google may classify as “bad links”:

- [Paid links](https://ahrefs.com/seo/glossary/paid-link)
- [Private blogging network (PBN) links](https://ahrefs.com/seo/glossary/private-blog-network)
- Low-quality directories
- Comment and forum spam
- Hacked sites

If you believe you have some links that negatively impact your site, you may want to consider using [Google Search Console’s disavow tool](https://ahrefs.com/blog/google-disavow-links/).

But remember to use the disavow tool with caution:

> We said multiple times that the disavow tool is a very heavy gun. And if you don’t know what you are doing, you can shoot yourself in the foot with it.
>
>
>
> Gary Illyes, Webmaster Trends Analyst [Google](https://www.google.com)

## 7. Check your content

If your site has a lot of low-quality content and you lost rankings during a content-focused Google update, you’ll need to improve it.

But how exactly can you improve your content? The first step is to do a [content audit](https://ahrefs.com/blog/content-audit/) of your website. Here’s a visual representation of the process we use to audit content at Ahrefs.

![Flowchart showing how to do a content audit, via Ahrefs Blog

Google also offers some [self-assessment questions](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) that you can use to further audit and improve your content:

> - Does the content provide original information, reporting, research, or analysis?
> - Does the content provide a substantial, complete, or comprehensive description of the topic?
> - Does the content provide insightful analysis or interesting information beyond the obvious?
> - If the content draws on other sources, does it avoid simply copying or rewriting those sources and instead provide substantial additional value and originality?
> - Does the main heading or page title provide a descriptive, helpful summary of the content?
> - Does the main heading or page title avoid exaggerating or being shocking in nature?
> - Is this the sort of page you’d want to bookmark, share with a friend, or recommend?
> - Would you expect to see this content in or referenced by a printed magazine, encyclopedia, or book?
> - Does the content provide substantial value when compared to other pages in search results?

Although there is no guarantee that improving content will immediately impact your rankings, ensuring your content is the best for your visitors is a good idea.

Further reading

- [How to Create Great Content for Search](https://ahrefs.com/blog/how-to-write-great-content/)
- [How to Write Website Content That Ranks (And People Want to Read)](https://ahrefs.com/blog/website-content/)
- [Content Creation: The Complete Guide for Beginners](https://ahrefs.com/blog/content-creation/)

## 8. Check the SERPs

[Google SERPs](https://ahrefs.com/blog/serps/) are constantly changing. And yes, it’s another factor that can impact rankings and organic traffic to your site—one that you have little control over.

To explain this concept, let’s look at a historical example of a dramatic SERP intent shift by plugging the keyword “corona” into [Keywords Explorer](https://ahrefs.com/keywords-explorer).

We’ll set the date to March 31, 2020, and compare it to the SERP pre-pandemic on January 3, 2020.

![SERP overview and comparison for "corona," via Ahrefs' Keywords Explorer

In this example, we can see Corona beer–related websites on the left-hand side were displaced by websites covering COVID-19 and “Top stories” in the space of a few months.

If we set the date to something more recent, we can see that Corona, the beer, has regained its number #1 position. Why? Well, the search intent has reverted.

![Corona beer SERP overview, via Ahrefs' Keywords Explorer

If you think a SERP intent shift may have impacted your website, then it’s worth using the “SERP overview” tool in [Keywords Explorer](https://ahrefs.com/keywords-explorer) to see how the historical SERP has changed.

## 9. Check Google Search Console for a manual action

If your website has lost all organic search traffic, you should check [Google Search Console’s “Manual actions” report](https://support.google.com/webmasters/answer/9044175?hl=en).

To do this, click on the tab on the left-hand side:

!["Manual actions" tab highlighted, via Google Search Console

If there’s no issue, you’ll see a “No issues detected” notice in Google Search Console that looks like this:

!["No issues detected" under "Manual actions" tab, via Google Search Console

If there is a problem, it will look similar to this. This is a “Pure spam” manual action.

If your site gets a manual action, a human reviewer at Google believes you have violated the [search quality guidelines](https://developers.google.com/search/docs/essentials) severely. Google will then generally remove your website and its pages from the search index.

Here’s a list of the different types of manual actions you can receive:

- Site abused with third-party spam
- User-generated spam
- Spammy free host
- Structured data issue
- Unnatural links to your site
- Unnatural links from your site
- Thin content with little or no added value
- Cloaking and/or sneaky redirects
- Pure spam
- Cloaked images
- Hidden text and/or keyword stuffing
- AMP content mismatch
- Sneaky mobile redirects
- News and Discover policy violations

Guidance from Google on how to fix these types of issues can be found [here](https://support.google.com/webmasters/answer/9044175).

It’s usually rare to receive a manual action, but it’s not unheard of. To stay on the right side of Google, remember to take our [SEO training course](https://ahrefs.com/academy/seo-training-course) and follow the [Google Search Essentials](https://developers.google.com/search/docs/essentials).

## Final thoughts

It’s never easy working out why your website’s rankings have dropped dramatically. It involves investigating, analyzing, and finding data you can rely on to make decisions.

Tools like [Ahrefs](https://ahrefs.com/) can help, as they enable you to look behind the curtain to see what’s going on.

Got more questions? Ping me [on Twitter](https://twitter.com/chris_at_b449?lang=en-GB). 🙂
