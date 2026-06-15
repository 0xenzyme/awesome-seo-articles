---
title: "Is It OK to Remove 301 Redirects After a Year? We Tested It"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "are-pemanent-redirects-permanent"
url: "https://ahrefs.com/blog/are-pemanent-redirects-permanent/"
canonical: "https://ahrefs.com/blog/are-pemanent-redirects-permanent/"
author: "Patrick Stox"
published: "2023-06-09T05:10:58+00:00"
updated: "2023-06-09T05:11:02+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
fetched_at: "2026-06-12T11:15:55+00:00"
status_code: 200
html_hash: "fa2c7b55beda0f1199c961c54086435f1b69b115b52176eb9217d2cb073e03cf"
clean_word_count: 977
clean_char_count: 5412
---
# Is It OK to Remove 301 Redirects After a Year? We Tested It

In 2021, Google’s Gary Illyes said on Twitter that redirect signals consolidate permanently to the new location after one year.

> after 1 y all signals had time to pass on from A to B.
> if the redirect is broken after 1 y, A will be standing on its own and so will B
>
> — Gary 鯨理／경리 Illyes (so official, trust me) (@methode) [July 21, 2021](https://twitter.com/methode/status/1417925974256095234?ref_src=twsrc%5Etfw)

This means that, in theory, signals to the original URL are permanently passed to the new one after a year.

If the redirect is removed and the original page is restored, the original page has to build brand-new signals on its own.

Even though the old links still point to the original page, they count for the page that was the redirect target for over a year.

![How 301s work](https://ahrefs.com/blog/wp-content/uploads/2023/06/how-301s-work.png)

Sidenote.

Note that one year is measured from the time Google crawls it.

This is different from what SEOs believe. Usually, it is assumed that if the redirect is no longer in place that the signals are lost. It’s also been understood that if the original page is restored that the signals will build back up for that page. Have we been wrong this whole time? Let’s find out.

## Test and results

I removed redirects to these pages on January 30, 2023:

- <https://ahrefs.com/blog/content-syndication/>
- [https://ahrefs.com/blog/structured-data/](https://ahrefs.com/blog/schema-markup/)
- <https://ahrefs.com/blog/keyword-search-volume/>
- <https://ahrefs.com/blog/what-is-https/>

These posts were chosen because they had older posts redirected to them. Those older posts were about the same topics and had enough links and referring domains that I thought removing them would have a visible impact.

You can see the clear drop in referring domains after I did this:

What I don’t see is much drop in traffic to these posts. One actually has increased traffic, one is down, and two are relatively flat.

The post on keyword search volume is the one that was down. The drop that looks like it occurred about the same time as when the redirects were removed actually happened a few days before the removal. You can see that the drop already happened on January 24, but I didn’t remove redirects until January 30.

The traffic to the post did decline during the test, so I can’t rule out that removing the redirects hurt this post.

## Verdict and next steps

I’m not willing to conclusively say that permanent redirects pass value even after one year, but what Gary said seems to mostly hold true.

It’s not that I don’t believe Gary, but this is radically different from how SEOs thought redirects consolidated. It seems crazy that signals could be consolidated to a different location than where a link points.

It’s certainly not something I want to take lightly. I’m already running another test, have a larger test planned if that pans out, and will likely do a study after that. Even though it’s not conclusive, it likely will hold true, and that’s why I want to share this now.

## SEO implications

If the way we understand redirect consolidation is wrong, it has massive implications for the SEO industry.

### Redirect recommendations

One of the tactics that I always use with a new client is to redirect 404 pages that have links pointing to them. I think, in most of those cases, the pages had never been redirected.

If redirects are actually permanent after one year, I’ll need to segment those that were redirected longer than a year from those that weren’t. There might still be value to be had with this tactic, but with less work needed.

### Domain buying

This is a big one. The value of a domain can change a lot based on the links pointing to it.

A lot of SEOs buy domains that already have links from sites in the same niche when they plan to launch a new website or redirect it to their current site. They hope that these old links will help them rank better.

Imagine if that value was no longer actually there. If the domain had been redirected for a year or more and the value permanently passed to a different domain, then that domain might be worth a lot less.

### Tools

There’s also a massive impact on various tools like Ahrefs if the redirects do permanently pass value. We would need to change how we show links and domains to these sites when redirects are involved.

I’m sure we’d also get a lot of questions when the redirects were removed, e.g., “Why do you still show these links to this page when the other page no longer redirects?” It’s a weird concept, right? But if that’s how it works, that’s what we need to do.

## Final thoughts

I haven’t seen any change in the SEO industry or the recommendations from SEOs since Gary’s tweet. I’m not sure if that’s because few people saw it or followed the fractured conversation, or we collectively don’t want to believe that redirects consolidate differently than what we think.

I still don’t think many SEOs believe me when I say temporary redirects consolidate backward to the original URL, but they do.

As I said, I’m not willing to call this one just yet. At the very least, a lot more tests need to be run before I’m willing to conclude that permanent redirects do permanently pass signals.

If you have any questions, message me [on Twitter](https://twitter.com/patrickstox).
