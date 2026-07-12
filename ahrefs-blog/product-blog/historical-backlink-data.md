---
title: "[New Feature Alert] Historical Backlink Data"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "low"
slug: "historical-backlink-data"
url: "https://ahrefs.com/blog/historical-backlink-data/"
canonical: "https://ahrefs.com/blog/historical-backlink-data/"
author: "Tim Soulo"
published: "2015-09-21T08:00:22+00:00"
updated: "2025-12-18T14:08:36+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "product_or_tool_content"
fetched_at: "2026-06-12T11:36:05+00:00"
status_code: 200
html_hash: "f7994f1d4aa2113b53e0095984f4d7a25d6691bb52995546398c30fbc5560070"
clean_word_count: 689
clean_char_count: 4096
---
# [New Feature Alert] Historical Backlink Data

Usually when we add a new feature to Ahrefs toolset, not many people will notice it right away *(that’s the reason why I started writing these “what’s new” blog posts on Mondays)*.

But last week we’ve added something that was noticed immediately:

> [@ahrefs](https://twitter.com/ahrefs) What’s the difference between Live and Fresh? [pic.twitter.com/Vrx10rnh4o](http://t.co/Vrx10rnh4o)
>
> — Acro Media Inc. (@AcroMediaInc) [September 17, 2015](https://twitter.com/AcroMediaInc/status/644624047477772288)

> Hey [@ahrefs](https://twitter.com/ahrefs) I saw a new drop down menu appear right next to the search bar in Site Explorer. What does “Live” and “Fresh” mean?
> Thanks
>
> — Jaime A (@James\_Searches) [September 18, 2015](https://twitter.com/James_Searches/status/644984366054158338)

> Nice feature [@ahrefs](https://twitter.com/ahrefs) the Fresh and live search !
>
> — Aymen Loukil (@LoukilAymen) [September 17, 2015](https://twitter.com/LoukilAymen/status/644484934879608832)

So let me tell you about this new feature real quick…

## Historical Backlink Data

The backlink profile of your website is a subject to change. As time goes by, you build new links to your site, while some of the old ones pass away.

That is why we were receiving many requests to start collecting historical backlink data, so that you could see all backlinks that a website used to have VS the backlinks that it has “live” at the present moment.

***TIP:** Knowing which of your links are no longer “live” gives you an opportunity to restore them and improve your backlink profile.*

So, starting 13th of August we began collecting historical data.

Which means we have two indexes right now: **Fresh** and **Live**.

![ahrefs historical index](https://ahrefs.com/blog/wp-content/uploads/2015/09/ahrefs-historical-index.png)

- **Live Index** - contains all links that were “live” on our last re-crawl;
- **Fresh Index** - contains all links that we’ve seen “live” starting 13th of August *(including those, that were “dead” on our last re-crawl)*.

I’d like to point your attention to the **“on our last re-crawl”** phrase.

Web pages are not carved in stone and they may go down and back up for numerous reasons:

- hosting server downtime;
- DNS issues;
- website closed for maintenance;
- high volume of traffic;
- etc.

So the fact that the page was “down” on our last re-crawl doesn’t guarantee that this page is still down at this very moment *(and vice versa)*.

And that’s the reason we’re calling our second index **“Fresh”**. The odds are that many of the pages/links that we’ve seen “down” may be back online already.

Thus our “Fresh” index will most likely be limited to 3 months of data *(we didn’t decide yet actually)* and as you can tell, in the course of a few months we’re also going to add “Historic” index, that would include all backlinks that we seen live starting from 13th of August 2015.

Right now the difference in **Fresh** and **Live** indexes can clearly be seen at the top of [Site Explorer](https://ahrefs.com/site-explorer) “Overview” report:

Even though we’ve only started collecting historical data a little more than a month ago, the difference between the two is clearly visible.

## “Dead” Backlinks

When exporting a list of your backlinks from **“Fresh”** index, you’ll see a new column, called “Backlink Status”:

We have three statuses of “dead” backlinks:

- **Not Found** - the page with the backlink was not found for some reason *(like I said earlier, this kind of link may be back up by the time you check it)*;
- **Removed** - the page was ok, but we didn’t find the backlink that used to be there;
- **Dropped** - we’re constantly improving our index and dropping pages that we think are gibberish *(so the page and the link do exist, but the quality is so low that we don’t want to have it in our index)*.

That’s it!

This feature was just added and we still have tons of work as to implementing it across all our tools/reports/filters.

In case you have any feedback or requests - please let me know!
