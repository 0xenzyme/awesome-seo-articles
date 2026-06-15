---
title: "Google does not use the keywords meta tag in web ranking"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-09-google-does-not-use-keywords-meta-tag"
url: "https://developers.google.com/search/blog/2009/09/google-does-not-use-keywords-meta-tag"
canonical: "https://developers.google.com/search/blog/2009/09/google-does-not-use-keywords-meta-tag"
author: "Matt Cutts"
published: "2009-09-21T00:00:00+00:00"
updated: "2009-09-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:00:29+00:00"
status_code: 200
html_hash: "44683fd863c918805e3d64a216ccf773be845fd0aab5dba0c876f9846e56bf27"
clean_word_count: 465
clean_char_count: 2887
---
# Google does not use the keywords meta tag in web ranking

Recently we received some questions about how Google uses (or more accurately, doesn't use) the
keywords `meta` tag in ranking web search results. Suppose you have two website owners,
Alice and Bob. Alice runs a company called AliceCo and Bob runs BobCo. One day while looking at
Bob's site, Alice notices that Bob has copied some of the words that she uses in her
keywords `meta` tag. Even more interesting, Bob has added the words "AliceCo" to his
keywords `meta` tag. Should Alice be concerned?

At least for Google's web search results currently (September 2009), the answer is no. Google
doesn't use the keywords `meta` tag in our web search ranking. This video explains
more, or see the questions below.

## Does Google ever use the keywords `meta` tag in its web search ranking?

In a word, no. Google does sell a Google Search Appliance, and that product has
[the ability to match `meta` tags](https://code.google.com/apis/searchappliance/documentation/50/help_gsa/serve_filters),
which could include the keywords `meta` tag. But that's an
enterprise search appliance that is completely separate from our main web search. Our web search
(the well-known search at Google.com that hundreds of millions of people use each day) disregards
keywords `meta` tag completely. They simply don't have any effect in our search ranking at present.

## Why doesn't Google use the keywords `meta` tag?

About a decade ago, search engines judged pages only on the content of web pages, not any
so-called "off-page" factors such as the links pointing to a web page. In those days, keyword meta
tags quickly became an area where someone could stuff often-irrelevant keywords without typical
visitors ever seeing those keywords. Because the keywords `meta` tag was so often
abused, many years ago Google began disregarding the keywords `meta` tag.

## Does this mean that Google ignores all `meta` tags?

No, Google does support several other `meta` tags. This
[`meta` tags](/search/docs/advanced/crawling/special-tags) page documents more info on
several `meta` tags that we do use. For example, we do sometimes use the description
`meta` tag as the text for our search results snippets, as this screenshot shows:

![a simple google search result](/static/search/blog/images/archived_meta-description.png)

Even though we sometimes use the description`meta` tag for the snippets we show, we
still don't use the description `meta` tag in our ranking.

## Does this mean that Google will always ignore the keywords `meta` tag?

It's possible that Google could use this information in the future, but it's unlikely. Google has
[ignored the keywords `meta` tag for years](https://searchengineland.com/meta-keywords-tag-101-how-to-legally-hide-words-on-your-pages-for-search-engines-12099)
and currently we see no need to change that policy.
