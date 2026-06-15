---
title: "New in June: Backend magic, Ahrefs Academy, Link lost reasons, etc"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "high"
slug: "new-in-june"
url: "https://ahrefs.com/blog/new-in-june/"
canonical: "https://ahrefs.com/blog/new-in-june/"
author: "Tim Soulo"
published: "2017-07-05T04:15:09+00:00"
updated: "2017-07-05T04:54:42+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "product_or_tool_content"
fetched_at: "2026-06-12T11:53:09+00:00"
status_code: 200
html_hash: "0dd0dcb238205a730ce4938cfa7bd307a99e1790cc1c0eca91a1b39462ac7a96"
clean_word_count: 1314
clean_char_count: 7519
---
# New in June: Backend magic, Ahrefs Academy, Link lost reasons, etc

Another month of hard work for Ahrefs team is over. Which means it’s time we report our progress to you.

*(Just in case you’ve missed our report for May, click here: [What’s new at Ahrefs in May](https://ahrefs.com/blog/whats-new-ahrefs-may/))*

So here’s what we’ve been up to in June:

## 0. Backend magic

Because [Ahrefs is a big data company](/blog/ahrefs-seo-metrics/), a fair share of all development work is happening on the backend. *(Which means it might not be as visible to our users as the features that we add to our interface.)*

Here’s a snapshot of what is being brewed at our server racks right now:

1. **Better scheduler for web crawler is at the testing stage.** (This is a long term project we started in 2016.) - this will affect how we prioritise crawling and re-crawling of pages and should drastically improve link discovery.
2. **JS links crawling is now at second Beta** (i.e. very close to release) - afaik, none of the commercial crawlers can handle links in JS as of today. Hopefully Ahrefs will be the first to crack this.
3. **Better support of new web standards for data markup.**
4. **Improvements to DR algorithm**
5. **Counters of internal backlinks**
6. **Support for all SERP features in mobile search results** (in new Rank Tracker)
7. **Improvements in crawling of content in Content Explorer**

Quite a lot, right? And that is just the part that I was allowed to disclose.

## 0. Two BIG tools are (still) on their way

Our focus hasn’t changed much since May. Nearly 70% of all our development resources are still being poured into two major tools: new **Rank Tracker** and new **Site Audit**.

I posted screenshots of both tools in [previous post](https://ahrefs.com/blog/whats-new-ahrefs-may/), so here are 2 more screenshots to tease you further:

![](https://ahrefs.com/blog/wp-content/uploads/2017/07/ahrefs-sa-screen.jpg)

How the new Site Audit tool will (should) look like

How the new Rank Tracker tool will (should) look like

Please note that these are the “screenshots” of how these tools were designed by our UI/UX team, and not the screenshots of the actual tools.

Which means that the final release might look somewhat different from what you see on the above images. We might remove some things and add some others.

As for the release date, I’m pretty sure that Rank Tracker will go live before summer ends. And in case of Site Audit, that’s a much more ambitious tool, so all I can say is “autumn”.

## 1. Ahrefs Academy

I can’t express how much I enjoy jumping on a Skype call with random Ahrefs customers and showing them all sorts of amazing features that they didn’t know they have access to.

But unfortunately, this kind of “customer education” doesn’t really scale. So there was clearly a need for a comprehensive (and brief) course around Ahrefs tools and data.

Enter **[Ahrefs Academy (https://ahrefs.com/academy)](https://ahrefs.com/academy)**:

We’ve teamed up with [Kathryn Aragon](https://kathrynaragon.com/) to create 10 short and value-packed video lessons, that take you by the hand and walk you though almost all major features of Ahrefs toolset.

*(Each video lesson is accompanied by a detailed article, if you prefer text to video.)*

This “introductory course” is just the beginning. I’m already in the process of creating a new one, so watch the announcements!

## 2. Notifications Center

Most likely this small new feature is how you landed on this very article:

We believe it is utterly important for our customers to be up to date with all the latest developments of the toolset that they are paying for.

Every day Ahrefs team is working on some new things that should make your online marketing work easier and more effective. But what’s the point if you will never learn about them?

Hence the need for this “Notifications center” and these “what’s new” monthly reports.

We figured that displaying a “facebook-style” notification in your Ahrefs account is much less intrusive than sending you an email or a browser push-notification.

This feature will also let you know of the newly published articles at [Ahrefs Blog](https://ahrefs.com/blog/).

We only publish new articles once a week (at best) so you don’t have to worry about tons of notifications flooding your Ahrefs account.

## 3. Link lost reasons

Our Backend Team ([yes, with capital letters](https://tech.ahrefs.com/)) is now storing more precise “link lost” reasons. Which is now being reflected in Site Explorer reports.

Generally, there are two groups of “link lost” reasons.

Those, related to a linking page:

- **404 not found** - the linking page was not accessible on our last re-crawl, so we consider a link from it “lost” (but we will add it back if on the next re-crawl that page will be live);
- **Noindex** - the linking page got a “noindex” attribute and therefore we don’t count links from it (that is an arguable decision, but that is what we decided to do for the time being);
- **301/302 redirect** - the linking page is now redirected somewhere else. And in case the page it redirects to does have a link to your target, it will soon appear in your backlink profile;
- **not canonical** - the linking page has a “rel canonical” tag to some other page, which means it is no longer a unique page, so we don’t count links from it.

And those, related to the actual link:

- **link removed** - means that the linking page is live, but it no longer has a link to your target;
- **broken redirect** - means that both the linking page and the link are ok, but that link was reaching your target via a few redirects and one of them no longer works, so the link is now kind of “disconnected” from the target.

Please keep in mind that these reasons are “reversible” and often caused by webmaster making temporal changes on their website. So it is a common case for a “lost” backlink to go “live” pretty much the next day.

The only exception is “link removed” tag, as it refers to purposeful editing of the page with a goal to strip out that particular link.

## 4. Broken backlink dates

We figured there was some confusion as to what “Dates” in the “Broken backlinks” report refer to.

So we fixed that:

- **Destination page check** — last time Ahrefs bot re-crawled destination page to verify it is not accessible (i.e. broken).
- **Referring page check** — last time Ahrefs bot re-crawled referring page to verify the target link was still there.

At this point I want to say big thanks to our amazingly smart and attentive customers, who don’t allow us to have any duds in our interface.

And speaking of customer feedbacks…

## 5. Feature Requests

We have adopted a cool online service, that helps to collect and prioritise customer feature requests:

**<https://ahrefs.canny.io/>**

Just by sharing it with our Facebook group, the board got quickly filled with a lot of great feature requests and suggestions.

So far we love where this is going and we’re already looking for a place to feature this little service on our website, so that anyone could easily locate it and request features.

Meanwhile, feel free to add anything that you think should be added to Ahrefs platform here: **<https://ahrefs.canny.io/>**

As I’ve already mentioned, right now we’re buried with work on Rank Tracker and Site Audit. But once these two biggies are released, we’ll dig into your feature requests and will do our best to ship them fast.

That’s it for June.

See you next month!
