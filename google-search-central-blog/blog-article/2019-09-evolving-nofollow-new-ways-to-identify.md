---
title: "Evolving \"nofollow\" – new ways to identify the nature of links"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2019-09-evolving-nofollow-new-ways-to-identify"
url: "https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify"
canonical: "https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify"
author: "Danny Sullivan, Gary Illyes"
published: "2019-09-10T00:00:00+00:00"
updated: "2019-09-10T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:34:56+00:00"
status_code: 200
html_hash: "3ec98b8fef2cdfdf914b068caa7d6b9bea79f33679be317dd1e9b1e596b1da44"
clean_word_count: 1005
clean_char_count: 6097
---
# Evolving "nofollow" – new ways to identify the nature of links

Nearly 15 years ago, the [`nofollow`
attribute](/search/docs/advanced/guidelines/qualify-outbound-links) was [introduced](https://googleblog.blogspot.com/2005/01/preventing-comment-spam.html)
as a means to help fight comment spam. It also quickly became one of Google's
[recommended methods](/search/docs/essentials/spam-policies#link-spam)
for flagging advertising-related or sponsored links. The web has evolved since nofollow was
introduced in 2005 and it's time for nofollow to evolve as well.

Today, we're announcing two new link attributes that provide webmasters with additional ways
to identify to Google Search the nature of particular links. These, along with
`nofollow`, are summarized below:

- **`rel="sponsored"`:** Use the sponsored attribute to identify links on your site
  that were created as part of advertisements, sponsorships or other compensation agreements.
- **`rel="ugc"`:** UGC stands for User Generated Content, and the `ugc`
  attribute value is recommended for links within user generated content, such as comments and
  forum posts.
- **`rel="nofollow"`:** Use this attribute for cases where you want to link to a
  page but don't want to imply any type of endorsement, including passing along ranking credit to
  another page.

When nofollow was introduced, Google would not count any link marked this way as a signal to use
within our
[search algorithms](https://www.google.com/search/howsearchworks/how-search-works/ranking-results/).
This has now changed. All the link attributes—`sponsored`, `ugc`, and
`nofollow`—are treated as hints about which links to consider or exclude within
Search. We'll use these hints—along with other signals—as a way to better understand
how to appropriately analyze and use links within our systems.

Why not completely ignore such links, as had been the case with `nofollow`? Links
contain valuable information that can help us improve search, such as how the words within links
describe content they point at. Looking at all the links we encounter can also help us better
understand unnatural linking patterns. By shifting to a hint model, we no longer lose this
important information, while still allowing site owners to indicate that some links shouldn't be
given the weight of a first-party endorsement.

We know these new attributes will generate questions, so here's an FAQ that we hope covers most of
those.

## Do I need to change my existing nofollows?

No. If you use `nofollow` now as a way to block sponsored links, or to signify that you
don't vouch for a page you link to, that will continue to be supported. There's absolutely no need
to change any `nofollow` links that you already have.

## Can I use more than one `rel` value on a link?

Yes, you can use more than one `rel` value on a link. For example,
`rel="ugc sponsored"` is a perfectly valid attribute which hints that the link came
from user-generated content and is sponsored. It's also valid to use `nofollow` with
the new attributes—such as `rel="nofollow ugc"`—if you wish to be
backwards-compatible with services that don't support the new attributes.

## If I use `nofollow` for ads or sponsored links, do I need to change those?

No. You can keep using `nofollow` as a
[method](/search/docs/essentials/spam-policies#link-spam)
for flagging such links to avoid possible link scheme penalties. You don't need to change any
existing markup. If you have systems that append this to new links, they can continue to do so.
However, we recommend switching over to `rel="sponsored"` if or when it is convenient.

## Do I still need to flag ad or sponsored links?

Yes. If you want to avoid a possible [link
scheme action](/search/docs/essentials/spam-policies#link-spam), use `rel="sponsored"` or `rel="nofollow"` to flag these
links. We prefer the use of `sponsored`, but either is fine and will be treated the
same, for this purpose.

## What happens if I use the wrong attribute on a link?

There's no wrong attribute except in the case of sponsored links. If you flag a UGC link or a
non-ad link as `sponsored`, we'll see that hint but the impact—if any at
all—would be at most that we might not count the link as a credit for another page. In this
regard, it's no different than the status quo of many UGC and non-ad links already marked as
`nofollow`.

It is an issue going the opposite way. Any link that is clearly an ad or sponsored should use
`sponsored` or `nofollow`, as described above. Using `sponsored`
is preferred, but `nofollow` is acceptable.

## Why should I bother using any of these new attributes?

Using the new attributes allows us to better process links for analysis of the web. That can
include your own content, if people who link to you make use of these attributes.

## Won't changing to a "hint" approach encourage link spam in comments and UGC content?

Many sites that allow third-parties to contribute to content already deter link spam in a variety
of ways, including moderation tools that can be integrated into many blogging platforms and human
review. The link attributes of `ugc` and `nofollow` will continue to be a
further deterrent. In most cases, the move to a hint model won't change the nature of how we treat
such links. We'll generally treat them as we did with `nofollow` before and not
consider them for ranking purposes. We will still continue to carefully assess how to use links
within Search, just as we always have and as we've had to do for situations where no attributions
were provided.

## When do these attributes and changes go into effect?

All the link attributes, `sponsored`, `ugc`, and `nofollow`, now
work today as hints for us to incorporate for ranking purposes. For crawling and indexing
purposes, `nofollow` will become a hint as of March 1, 2020. Those depending on
nofollow solely to block a page from being indexed (which was never recommended) should use one of
the much more robust mechanisms listed on our
[Learn how to block URLs from Google](/search/docs/crawling-indexing/control-what-you-share)
help page.
