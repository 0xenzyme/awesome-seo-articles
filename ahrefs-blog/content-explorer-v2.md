---
title: "Ahrefs Content Explorer 2.0: Rebuilt From Scratch (With New Features)"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "low"
slug: "content-explorer-v2"
url: "https://ahrefs.com/blog/content-explorer-v2/"
canonical: "https://ahrefs.com/blog/content-explorer-v2/"
author: "Tim Soulo"
published: "2019-04-04T11:37:28+00:00"
updated: "2024-09-17T11:24:20+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2024_watch"
  - "product_or_tool_content"
fetched_at: "2026-06-12T11:23:23+00:00"
status_code: 200
html_hash: "807031da17dc6892ec924f0590deb34c29e73775c7fd6e50040165c8be38c331"
clean_word_count: 2895
clean_char_count: 16564
---
# Ahrefs Content Explorer 2.0: Rebuilt From Scratch (With New Features)

In 2014, we released Content Explorer: a searchable and filterable database of hundreds of millions of web pages. It has since grown to over 1.1 BILLION web pages and today, we’re announcing the launch of the new and much improved Content Explorer 2.0.

Before I talk about new features, let me stress that this is **not** a small update.

We rebuilt Content Explorer (v2) from the ground up!

If you’re not already familiar with [our CEO’s](https://twitter.com/botsbreeder) vision behind rebuilding all Ahrefs’ tools from scratch and with the latest tech, please first read [our launch post for Keywords Explorer 3.0](https://ahrefs.com/blog/keywords-explorer-3-0/).

No time? Here’s the TLDR version: Moving things to new tech makes Ahrefs’ tools work noticeably faster and substantially ramps up the speed of development. That means we’re able to fulfil [your feature requests](https://ahrefs.canny.io/content-explorer) much quicker.

Here’s a quick overview of the new features in Content Explorer 2.0:

- [Broken (404 & 410) pages](#broken-pages)
- [Published & republished dates](#published-republished)
- [Content trends graph](#content-trends)
- [New in-line charts](#inline-charts)
- [UI and filtering improvements](#ui-filtering)

Let’s take a look at these new features in more detail and discuss some actionable use cases.

## Search the content of broken (404, 410 & “No domain”) pages

Have you ever searched Content Explorer and found a dead page? No? That’s because we used to remove them from the index as soon as our crawler saw they were no longer online.

But during the creation of Content Explorer v2, we had a brainwave:

> Why not keep dead pages in the index and just add a filter for live/broken pages?

So that’s what we did. You can now filter for live or broken pages or both:

How is that useful? Because some “dead” pages [have high-quality backlinks pointing to them](https://ahrefs.com/blog/high-quality-backlinks/)!

For example, imagine that you run a cooking website. If you search for something like “recipe” and filter for broken pages, you get 69,789 results. If you then narrow the results down to only pages with at least 100 referring domains, you’re left with 86 web pages.

Let’s do the math:

> 86 web pages \* 100+ linking websites = **8,600+ potential link building opportunities!**

Did I lose you? Let’s take a closer look at that very first result:

This page clearly used to be home to a double broccoli quinoa recipe (you can check the URL at [archive.org](https://web.archive.org/web/20130221001457/https://www.101cookbooks.com/archives/double-broccoli-quinoa-recipe.html) to see some historical snapshots). It must have been a good one too, as it managed to attract backlinks from 203 referring domains. If we click the title, the page opens in a new tab and we can confirm that it is indeed a 404 (i.e., dead page).

So, on the face of it, this looks like a perfect [broken link building](https://ahrefs.com/blog/broken-link-building/) opportunity. We can reach out to those 203 people, tell them they’re linking to a dead page, and possibly get them to link to us instead.

But are any of those backlinks from 203 unique websites *actually* worth pursuing?

Let’s hit the caret and click through to the **Backlinks** report for this page.

Right away, we see “dofollow” contextual links from:

- Buzzfeed (DR91)
- Smithsonian Magazine (DR89)
- MNN [Mother Nature Network] (DR 83)

… and hundreds of other small-to-medium-sized websites and blogs.

But remember, this page no longer exists. That means **203 sites are linking to a dead page.**

Therein lies the opportunity:

- Publish your own delicious broccoli quinoa recipe (unless you have one already)
- Ask anyone linking to the dead page to link to your working recipe instead.

Here’s [an in-depth video](https://www.youtube.com/watch?v=IOSrx95e4lo) explaining how to execute this strategy to perfection:

Here’s another neat tip:

Dead pages often occur due to bad [site migrations](https://ahrefs.com/blog/website-migration/), the deletion of content in bulk following a [content audit](https://ahrefs.com/blog/content-audit/), or the expiration of a domain. So, I’d say that there’s a high chance of a site with one dead page having more dead pages.

How can you check? Click on the domain of a result to see all other dead pages from that site:

Now we have two good broken link building opportunities!

At this stage, you might be wondering how many dead pages are in our index. I had the same question, and so I asked our team to run the numbers. I also asked them to check how many referring domains point to each dead page.

Here are the results:

Right now, we have just shy of 26 million dead pages in Content Explorer. Of those, ~14% have at least one backlink. Now, that number might not sound huge and it isn’t. That’s because we only stopped deleting dead pages from the index in November 2018, which means that **the number of dead pages is growing by around 5 million per month** and will continue to do so!

That’s a critical point. It means that, in theory, you should **never** run out of broken link building opportunities!

By the way, if you’re curious how many dead pages are in our index as of today, try this:

1. Go to [Content Explorer](https://ahrefs.com/v2-content-explorer)
2. Run a blank search
3. Filter for broken pages only.

The number of results is roughly equal to the number of dead pages in our index.

IMPORTANT

Please note that we **don’t** crawl the web looking for 404 & 410 pages to add to Content Explorer. We simply retain existing pages as they go missing. In other words, we won’t add any pages that were already “dead” by November 2018 to our database.

## See published & republished dates

Have you seen [our list of the top 100 Google searches](https://ahrefs.com/blog/top-google-searches/)?

We originally published this post in April 2017. But we now update and republish it with fresh data every month. This ensures that we continue to rank high in Google, which often rewards publishers who keep content up-to-date.

We’re not the only ones to do this either. Lots of sites regularly update and republish content.

That’s why we decided to tag the pages in Content Explorer v2 as either *Published once* or *Republished*.

We also now store two different dates for each piece of content:

1. **First published:** the date the page was first published, or the date when we first crawled it.
2. **Published/Republished:** the date the page was published (for the pages published once) or the republish date (for pages that have been republished).

However, we only show two dates in the UI for republished pages. Reason being, for content that hasn’t been republished, the *First published* and *Published* dates are the same—so there’s no point showing them both!

Here’s how that looks:

IMPORTANT

If a page is republished within 30 days of publishing, we don’t mark it as republished. This is because people often issue small updates to a piece of content (e.g., spelling fixes) shortly after publishing.

Now here’s the best part: There are filters for both!

These allow you to do some really cool stuff when it comes to content research.

For a start, if you’re an SEO freelancer or run a marketing agency, you may want to run a quick check to see whether a potential client is updating their old content. If they aren’t, this could be a low-hanging opportunity to increase their organic traffic.

Here are a couple more use cases:

### 1. Find out-of-date pages with lots of backlinks

Let’s say that you run a fitness blog. You’re looking for content ideas to which there’s a clear path to build backlinks. Here’s what you could do:

Search Content Explorer for something like “fitness” or “protein,” then filter for pages:

- That are **live** (not broken)
- That have only been **published once**
- That were **published many years ago**
- With **100+ referring domains**.

Here’s what we get:

2,084 pages that match our criteria, and this one looks super-relevant:

It has backlinks from 150 referring domains and was published in 2016.

If we take a look at the page itself, we can see that it lists high-protein smoothie recipes from other websites.

That’s important because the recipes aren’t actually on this page. So, for this page to have any value to its visitors, those links to the recipes still *need* to work.

Given that this page hasn’t been republished for the best part of three years, I’m betting that isn’t the case… and I’m right. I clicked the first recipe link in that post, only to find that the recipe no longer exists.

So, here’s what you could do:

1. Create an up-to-date working list of high-protein smoothie recipes
2. Ask anyone linking to the old page to swap out the link in favor of yours

You can find all backlinks to a page by hitting the caret and clicking through to the **Backlinks** report.

### 2. Find old, but recently-updated pages about a given topic

If an old page has been updated recently, then the author has clearly identified the topic as having potential and being something that people are still very interested in.

So, it’s a topic you should consider covering too (if you haven’t done so already).

To find such pages, search Content Explorer for your chosen topic, then filter for pages:

- That are **live** (not broken)
- That have been **republished recently**
- That were **originally published many years ago**

For example, there are 135,596 articles about “best apps” published between 2000 and 2016. Of those, 2,894 were republished in the last 12 months. That’s roughly **2%**.

But if we search for “best iPod,” we see only 7,735 articles published during that time, and only 17 were republished in the last 12 months.

That’s roughly **0.2%**.

This makes sense. iPods are old news, so that’s why so few sites bother to update their articles on the topic. However, “best apps” is something that people still care about. It’s also a topic that needs regular updates because new apps are released all the time.

## See content trends over time

I’m sure you’re familiar with Google Trends, which shows the search popularity of a given topic over time. Here it shows when people around the world were searching for MMA superstar “Conor McGregor” between 2016 and 2018:

Now compare that to how much content bloggers and journalists created during the same period in Content Explorer:

If you compare peoples’ interest in that [bus incident](https://www.youtube.com/watch?v=63OCvuC-GSY) with how vastly it was covered, journalists’ hunger for sensationalist stories becomes evident.

How else can you use these charts? Here are a couple of ideas:

### 1. Find brand mentions over time

Enter your brand name into Content Explorer and exclude your own domain. Check the content trends chart.

If it shows a rising trend, then your brand is getting mentioned more and more as time goes on.

If it shows a declining trend, then that indicates that people are talking about your brand less and less.

Editor’s Note

Be aware that as our infrastructure grows, so does the number of pages we add to Content Explorer each month. That’s why some topics may appear to show a slight upward trend, even if interest hasn’t significantly increased or decreased over the years (e.g., try the query “pizza”).

Joshua Hardwick

Head of Content

You can also do the same for your competitors, and compare which of them gets the most online mentions over time.

### 2. Check the publishing frequency of you vs. competitors

Ever wondered how often your competitors republish their content?

Just paste their blog URL into Content Explorer and switch the search mode to “In URL.” Here’s what we see for the Moz blog:

It looks like they rarely republish any of their posts, despite publishing around twenty new posts per month.

However, if we do the same for the Ahrefs blog, we see the opposite:

We republish content all the time, as shown by the dark blue bars in Content Explorer.

### 3. Find topics with a lot of outreach potential

People who’ve written about the same topic as your content make great outreach prospects (given that you have something unique to impress them with).

The fact they mentioned the topic tells you they have an interest in it. So it makes perfect sense to reach out and introduce yourself and your work in that field.

For example, if we wanted to promote [our link building guide](https://ahrefs.com/seo/link-building), we could search Content Explorer for pages that mention things like “link building”…

… then all we have to do is shoot them a quick email, introduce ourselves, and explain why our link building guide is worth taking a look at.

This is nothing new. You could do this in the old version of Content Explorer.

What is new, however, is the ability to check the “ongoing outreach potential” of a topic before even creating content.

Let me explain. Say that you were torn between writing two blog posts: one about “PageRank” or one about “link building.” If we search for “PageRank” in Content Explorer and filter for pages that were first published in the last 6 months, we can see from mousing over the bars on the trends chart that there are around 500 new posts mentioning “PageRank” published each month.

If we do the same for “link building,” we see that there are around 2,000 new posts published each month.

Translation: there are potentially 4x more fresh outreach prospects for “link building” compared to “PageRank” each month.

This is a very useful exercise when pitching clients and trying to figure out how many links you can expect to build for them month after month. If you assume a consistent conversion rate across all campaigns, then you can expect to build 4x more links to a topic with 2,000 new mentions each month compared to one with only 500.

## See more insights at a glance with new in-line charts

The early version of Content Explorer focused solely on helping you find the “most shared” content from all around the web. But over time, we gradually added more SEO metrics to every piece of content in our index.

And in v2, we’ve given the [SEO metrics](/blog/ahrefs-seo-metrics/) of each page the visual emphasis they deserve:

For the Ref. domains, Organic traffic, and Traffic value graphs, it’s also possible to choose the period for which the data is displayed. You can choose from the *last 30 days*, *last 6 months*, or the *last 3 years*.

Here are a couple of use cases for these charts:

### Referring domains chart

Use this to identify pages at a glance that are attracting a lot of links.

For example, try searching for a topic related to a piece of content you already have on your site. This will find other pages about the same topic. You can then look for pages that are attracting links consistently, or that have seen a huge increase in links recently.

Investigate these pages further by checking the **Backlinks** report. You may find that the person behind this content is running a link building campaign that’s working. This is something you can often learn from and replicate.

### Traffic chart

If the traffic graph correlates with an increase in Ref. domains, then it’s likely that the owner of the web page is building or earning links that are moving the needle in terms of organic traffic.

If you notice a page with declining traffic, then there’s a chance it hasn’t been updated for a long time. In which case, you may be able to outrank it by publishing a fresh piece of content on the topic.

## Other new features and filters

Before I wrap this up, here are a few more new things that deserve a mention.

### 1-click filtering by website or author

Click the name of the author for any result to see all other content by that author.

This is especially useful for finding sites to pitch [guest posts](https://ahrefs.com/blog/guest-blogging/) to:

### Better date filter UI

No longer do you have to waste valuable time scrolling through months or years of our poorly-designed calendar UI. We’ve added a bunch of presets along with a “custom” filter to make filtering by publish/republish date easier than ever.

## Final thoughts

This article only scratches the surface of what’s possible in the new Content Explorer.

We have a more in-depth video tutorial coming soon.

Having said that, I’m sure there are use cases of the new Content Explorer that even I haven’t discovered yet. Let me know in the comments if you think of any! 🙂
