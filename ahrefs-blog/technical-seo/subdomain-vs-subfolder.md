---
title: "Subdomain vs Subdirectory: Subdirectories Are Not Better Than Subdomains For SEO"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "subdomain-vs-subfolder"
url: "https://ahrefs.com/blog/subdomain-vs-subfolder/"
canonical: "https://ahrefs.com/blog/subdomain-vs-subfolder/"
author: "Patrick Stox"
published: "2021-03-09T16:00:34+00:00"
updated: "2024-05-19T12:13:37+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T12:11:18+00:00"
status_code: 200
html_hash: "dae9731505e372233e71cab4f8fcf1a251b6051f5c37dc2d4d916246e297312c"
clean_word_count: 1357
clean_char_count: 8026
---
# Subdomain vs Subdirectory: Subdirectories Are Not Better Than Subdomains For SEO

A subdomain creates a section of a website to the left of the root domain (**subdomain**.domain.com). A subdirectory (or subfolder) creates a section of a website to the right of the root domain (domain.com/**subdirectory**).

Let’s look at why SEOs argue over this topic and how it really works.

1. [Subdomain or subfolder: Which is best for SEO?](#which-is-best-for-seo)
2. [SEO case studies](#seo-case-studies)
3. [Reasons for traffic differences](#reasons-for-traffic-differences)

## Is a subdomain or subfolder better for SEO?

SEOs have argued about whether subdomains or subfolders are better for SEO for as long as I can remember. Many SEOs say that subdirectories are better for SEO and insist on using them. This is a myth that’s persisted based on some old studies.

Google has repeatedly said either is fine.

Matt Cutts [said in 2012](https://www.youtube.com/watch?v=_MswMYk05tk):

> They’re roughly equivalent. I would basically go with whichever one is easier for you in terms of configuration, your CMSs, all that sort of stuff… Both are on the same domain overall and so it’s really a question of which one is easier for you. Whichever one makes you happier I’d go ahead and do it that way.
>
>
>
> Matt Cutts, Former Head of Webspam [Google](https://www.google.com/)

John Mueller [said in 2017](https://www.youtube.com/watch?v=uJGDyAN9g-g):

> Google websearch is fine with using either subdomains or subdirectories. Making changes to a site’s URL structure tends to take a bit of time to settle down in search so I recommend picking a setup that you can keep for longer.
>
>
>
> John Mueller, Search Advocate [Google](https://www.google.com/)

I don’t think they could make it any clearer, but some SEOs still argue with Google. I love [John’s sarcastic response](https://twitter.com/JohnMu/status/956126001016332288) to these arguments.

It’s silly to argue if a path is better on the left or the right. Without going into too much technical detail, these paths are virtual in most modern systems, which means they don’t even point to actual locations on a server. You can change their name and their location in the URL structure in a matter of minutes.

Think about that for a second; you can change a subdomain to be served as a subdirectory quickly and without changing anything else, so why do people think it’s important where the path is located in the URL?

Many SEOs believe that subdomains are treated as separate domains, but the truth is more complicated. Anyone that incorporates subdomains as a main part of their site will likely have them treated as part of the site. However, if you’re not treating the subdomains as part of your main website (read as not connecting them with [internal links](https://ahrefs.com/blog/internal-links-for-seo/)), then they may be treated as separate.

The same is true for subdirectories! If you don’t treat them as part of the same site, Google may not either. Gary Illyes confirmed this at Pubcon in 2023. He said it’s not common on the English web, but it is in other languages.

> Are there cases where subdirectories can be treated separately, as individual sites?
>
> Yes. It’s not common on the English web but it is in other languages. [@methode](https://twitter.com/methode?ref_src=twsrc%5Etfw) [#pubcon](https://twitter.com/hashtag/pubcon?src=hash&ref_src=twsrc%5Etfw)
>
> — Patrick Stox (@patrickstox) [September 21, 2023](https://twitter.com/patrickstox/status/1704963371420856347?ref_src=twsrc%5Etfw)

A little history lesson. At one time, subdomains could get you additional listings in the [SERPs](https://ahrefs.com/blog/serps/). As with many things, SEOs abused this. Google closed this loophole in one of the old domain/host clustering updates.

These days, subdomains are likely to be treated as part of the same website if they appear to be part of the same website. Even [sitelinks](https://ahrefs.com/blog/sitelinks/) include links to subdomains.

Various Disney subdomains that have shown as sitelinks. Data from Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer).

I can give you countless examples where various subdomains show as sitelinks for the brand—Github, LinkedIn, Google, Amazon, Microsoft, Yahoo, Netflix, Walmart, etc.

## SEO case studies: Subdomain vs subdirectory

Many case studies show subdirectories are better than subdomains, but I haven’t seen one that wasn’t complicated by other changes like additional internal linking or migrating multiple properties into one.

Let’s look at one of those case studies and what I see. Using **Top Pages 2.0** in [Site Explorer](https://ahrefs.com/site-explorer), you can click and drag on the history chart to see the difference between any two dates. In the case of mention.com, they migrated from a subdomain to a subdirectory in January 2016. I really don’t see any difference in that period. It’s only after that when they started adding additional content that I see their traffic growing.

And notice that an equivalent page for each page that lost traffic re-gained around the same amount of traffic. The traffic simply shifted to a new location, but there was no real increase.

Here’s another fun one. Github migrated from a subdirectory (github.com/blog) to a subdomain (blog.github.com) and then to a completely different domain (github.blog). There was some flux during the migration periods, and there were other changes during the transition, but it would be hard to argue that any one of these was better than the others simply because of the URL.

## Why you might see traffic differences

Several different issues may cause people to believe that [migrations](https://ahrefs.com/blog/website-migration/) had more or less impact than they really did.

### Temporary signal changes

When pages are new or moved, Google may have them [inherit some temporary signals](https://www.seroundtable.com/google-confirms-site-wide-signals-for-new-pages-21772.html) at a folder or site level because they’re not quite sure how much to crawl or how to rank them yet. This can cause some temporary fluctuations while they figure out the changes.

### Tracking or measuring issues

This can show up in many different forms. It might be analytics setup issues such as maybe subdomain tracking wasn’t set up correctly. It can be timing issues such as measuring growth during a fast season, such as holiday shopping vs. an average traffic period, or around a Google core update. It can only be looking at growth in the new folder. The main thing is to make sure that you’re comparing apples to apples.

### Blocked or noindexed pages

If you block pages from being crawled or noindex pages, signals won’t consolidate correctly, which means you’re likely to see a drop during the migration. I’d recommend reading our [robots.txt](https://ahrefs.com/blog/robots-txt/) guide to understand this better.

### Redesign or platform change

A lot of different things can change when you redesign a website or change the platform. Technology, speed, headings, URL changes, and more can all be different.

### Internal linking changes

I see this one often in subdomain vs. subdirectory case studies: Going from a separate subdomain that wasn’t linked internally to a subdirectory that’s linked to on every page. Of course there’s going to be an uplift.

### Removed or updated content

Changing content means ranking and traffic are likely to change. If you remove content that had traffic, then traffic drops.

## Final thoughts on using a subdomain vs subdirectory

Changes introduce risk. You might want to think twice before changing from a subdomain to a subdirectory if the only reason you’re doing it is for SEO.

If you have a case where you migrated and saw an uplift without any of the changes above, I’d love to see it. Send me a message on [Twitter](https://twitter.com/patrickstox), and I’ll investigate, but I’m willing to bet there is a change that can explain the difference.
