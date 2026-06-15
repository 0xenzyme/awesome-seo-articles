---
title: "The State of Nofollow, UGC, & Sponsored Link Attributes in 2020 [New Research]"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "nofollow-ugc-sponsored"
url: "https://ahrefs.com/blog/nofollow-ugc-sponsored/"
canonical: "https://ahrefs.com/blog/nofollow-ugc-sponsored/"
author: "Patrick Stox"
published: "2020-05-05T23:48:22+00:00"
updated: "2023-10-05T08:11:16+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
  - "time_sensitive_title"
  - "title_year_2020_before_2026"
fetched_at: "2026-06-12T11:54:04+00:00"
status_code: 200
html_hash: "5f79c01e15e16e6968e56908e8bb2412b7ccbf4854daf1aa835ddf990d30718a"
clean_word_count: 1148
clean_char_count: 6692
---
# The State of Nofollow, UGC, & Sponsored Link Attributes in 2020 [New Research]

In 2019, after 15 years, Google changed how [nofollow](https://ahrefs.com/blog/nofollow-links/) works. It’s now a hint for both crawling and ranking. They also added two brand new attributes, rel=“ugc“and rel=“sponsored”.

According to [the announcement](https://webmasters.googleblog.com/2019/09/evolving-nofollow-new-ways-to-identify.html), nofollow is meant for links where you don’t want to imply any kind of endorsement or pass ranking credit to another page. Sponsored works the same way, but also shows that the link is an advertisement, paid placement, sponsorship, or affiliate link. UGC (User Generated Content) also works the same as nofollow but shows that the link was added by someone else. UGC should be used for comments, forum posts, or any other content sections where users can add content.

The new attributes are optional. Google wants people to use them so they can better understand linking patterns and how people are linking across the web. But at this time, [you don’t have to make any changes if you don’t want to](https://twitter.com/methode/status/1171588032178339840).

For those of you who use Ahrefs, you’ll know that we added support for UGC and sponsored attributes early on. In fact, we started collecting data and added filters to the tool within two days of the official announcement.

> We just rolled out support for “UGC” and “SPONSORED” link attributes!
>
> And it looks like we’re the first to do it. 💪
>
> cc: [@jroakes](https://twitter.com/jroakes?ref_src=twsrc%5Etfw) 😉 [pic.twitter.com/m4ji3X1JkN](https://t.co/m4ji3X1JkN)— Ahrefs (@ahrefs) [September 12, 2019](https://twitter.com/ahrefs/status/1172038675372396544?ref_src=twsrc%5Etfw)

Given this and the fact that sponsored and UGC are optional, we thought we’d dig into our data to see how often people are using them. To do that, we studied the top 110k sites by [Ahrefs Rank](/blog/ahrefs-seo-metrics/#section11).

## How common is nofollow?

10.6% of all backlinks to the top 110k sites are nofollow.

While there are legitimate reasons to use nofollow, such as having it on blog comments, this percentage is quite high. That’s likely one of the reasons why Google changed nofollow to a hint. We see a lot of major websites using mostly nofollow on external links like Wikipedia, Forbes, Entrepreneur, CNN, NFL, and many others. My guess is people were using this to avoid penalties for linking out or try to conserve [PageRank](https://ahrefs.com/blog/google-pagerank/) for their own site, which doesn’t work.

In the announcement from Google, they mentioned that the link [anchor text](https://ahrefs.com/blog/anchor-text/) was valuable because it describes the linked content. With the hint model, they can now use this information to understand unnatural linking patterns better too.

So that’s backlinks. What about internal links?

We found internal nofollow on 35.3% of the sites we studied. They made up 3.6% of all internal links. While 3.6% doesn’t seem high, that number should be near zero. I’m a technical SEO, and I can’t think of a single case where I would use nofollow on my internal links. I know some people do it to sculpt PageRank or to try to block indexing of pages, which used to work with pages not linked from anywhere else, but it was never a great way to prevent indexation. If you were using nofollow to block pages from being indexed, you have [a few better options](https://ahrefs.com/blog/remove-urls-from-google/).

## Are people using UGC and sponsored attributes?

Barely. Only 0.44% of referring domains to the top 110k sites use rel=”ugc”, and it’s even lower with rel=”sponsored” seen on only 0.01% of referring domains. As for the total number of backlinks containing the attributes, only 0.016% contain rel=”ugc” and only 0.008% contain rel=”sponsored”.

This was not unexpected since the new attributes are optional. Most sites are just using nofollow instead.

## Are people using the attributes on internal links?

We also wanted to see how people were using these link attributes on internal links on their sites. When we ran this, I expected some use of nofollow but wasn’t expecting to see UGC or sponsored in the data.

3.1% of the sites studied used rel=” ugc” on internal links, and that drops to 0.14% for rel=“sponsored”. For the total internal links containing the attributes, 0.0002% contained rel=“ugc” and 0.0016% contained rel=“sponsored”.

It kind of makes sense for UGC to show up on internal links. When adding this at scale, many developers or plugins likely add it automatically to comment sections or user-generated content sections where people may still link to other pages on the site.

Sponsored showing up in the data surprised me, though. Why would someone pay to have an internal link on their own website? I think most cases of sponsored on internal links are user error, but it’s possible some sites are adding it automatically for guest posts or advertorials.

## Will people adopt these new attributes?

When nofollow launched, there were many partners from other search engines, blogging platforms, and CMS systems who helped drive adoption of the new attribute. Everyone wanted to get rid of the spam comments, and platforms were happy to use nofollow. With UGC and sponsored not having any real benefit or consequences, I don’t expect we’ll see widespread adoption.

We wanted to see if we could find any patterns in the sites using the new attributes. Our thinking was that individual websites wouldn’t adopt the attributes, but maybe some CMS systems or plugins would add support.

We looked at the CMS used on 7,130 of the sites. These are the totals for the identified sites:

WordPress is the obvious standout here. WordPress added UGC support in version 5.3, and we found that some of the plugins have added support for sponsored. That accounts for the majority of adoption so far. I checked the Tiki Wiki codebase also but didn’t find any mentions of the attributes, so likely those few sites are one-offs as are many of the others because there’s no indication of widespread adoption on the platforms.

## Final thoughts

Nofollow is used a lot more than I expected, potentially too much. With Google’s change to a hint model, I expect search results to become even more relevant as they’re able to use more signals from anchor text of nofollow links. Without any kind of forced adoption, UGC and sponsored attributes will likely require different systems to adopt them before we see them become common.

Have questions about nofollow, UGC, sponsored, or their usage? Ping me on [Twitter](https://twitter.com/patrickstox).
