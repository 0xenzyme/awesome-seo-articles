---
title: "Over 67% of Domains Using Hreflang Have Issues (Study of 374,756 Domains)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "hreflang-study"
url: "https://ahrefs.com/blog/hreflang-study/"
canonical: "https://ahrefs.com/blog/hreflang-study/"
author: "Patrick Stox"
published: "2023-08-10T05:05:59+00:00"
updated: "2024-08-08T23:55:19+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:40:37+00:00"
status_code: 200
html_hash: "e81d487bb3489b4efafa14b573f022128b145112a4bd3407376115542fd4549f"
clean_word_count: 1201
clean_char_count: 7022
---
# Over 67% of Domains Using Hreflang Have Issues (Study of 374,756 Domains)

We ran the largest hreflang study ever, nearly 10X larger than any other study. In total, we looked at issues on 374,756 different domains that used hreflang tags. Our findings show that 67% of them have at least one issue.

![67% of domains have hreflang issues across 374,756 domains studied](https://ahrefs.com/blog/wp-content/uploads/2023/08/hreflang-study-2.png)

Let’s look at the most common issues you should actually care about.

## 56.3% have pages missing x-default

Setting an x-default is not required. But it is recommended if you need a fallback page for users whose language settings don’t match any of your localized versions.

Hreflang works by the most specific match. Language+country is more specific than just language, which is more specific than x-default. X-default mostly serves as a backup or global default page, where you want to send people.

## 18% have pages missing self-referencing hreflang tags

Self-referencing hreflang tags are [included in the guidelines](https://developers.google.com/search/docs/specialty/international/localized-versions#all-method-guidelines). But they’re really more like a best practice and [not actually required](https://www.youtube.com/watch?v=bjbaDP-P7PA&t=24m39s).

In the old days of hreflang, before the systems and plugins handled it, having a missing self-referencing tag meant that when you copied the tags to other pages, at least one of the connections would be broken. This is less likely to happen on modern websites, so it’s not as big of an issue.

## 16.9% have hreflang tags referencing redirected or broken pages

If you link to an incorrect URL, then the tags are broken and pages can’t swap properly in the search results. They work in pairs to form a cluster of pages. This is what an hreflang cluster looks like.

If the broken links are temporary while you’re still setting up pages, it’s OK to leave them. If these broken pages don’t exist and you don’t plan to have them, it doesn’t really hurt anything—but you may want to remove the references anyway.

Redirected pages included in hreflang tags are OK only if you have an auto-redirecting global version of the homepage.

There is an [approved setup for homepages](https://developers.google.com/search/blog/2014/05/creating-right-homepage-for-your) only that uses a [302 redirect](https://ahrefs.com/blog/301-vs-302-redirects/) for dynamic redirects based on location and language settings. I see people try to change this all the time, but it’s a documented setup that has been recommended and working on many sites for years.

In all other situations, a redirected page referenced in hreflang tags will mean that something is broken.

## 15.3% have pages missing reciprocal tags

As I mentioned, hreflang tags work in pairs. If both pages don’t reference each other, they can’t establish the connection and swap properly in the search results.

This is especially important when you have multiple versions of a page in the same language. You may end up sending the user to a version of the page for the wrong country.

## 8% have hreflang tags pointing to non-canonical URLs

Hreflang is one of many [canonicalization signals](https://ahrefs.com/blog/canonicalization/) that Google uses to determine which version of a [duplicate page](https://ahrefs.com/blog/duplicate-content/) it should index. In many cases I’ve looked at, the [canonical tag](https://ahrefs.com/blog/canonical-tags/) was ignored in favor of the URL specified in hreflang.

However, this is just a signal like many others and can be ignored, so it may work differently.

## 4.6% have pages with incorrect hreflang values

Hreflang requires two-letter language codes ([ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)) and two-letter country codes ([ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

Some of the common incorrect values are people using the country code instead of the language code, typos, trying to use region codes when they aren’t supported, or trying to use three-letter codes instead of two-letter ones.

Some people just use codes that are wrong as well. For example, they use things like “la” for Latin America, but that doesn’t work. Another common one is “uk” when they should use “gb.” But the funny thing here is that “uk” is a specially reserved code, and Google actually accepts this one!

## 3.2% have pages with inconsistent language attributes

This issue shows pages with different language codes declared in the HTML language attribute and hreflang annotation for the URL.

These are different systems, but both are used to say what language the page is in. If they don’t match, something is fishy and you should check which language the page is actually in.

## 2.5% of domains have more than one page referenced for the same language

For an hreflang language or language and country combination, you should only have one page specified for each unique value. If you specify “en” for a page and use “en” again but say it’s a different page, then Google is going to have to choose one or the other. They can’t both be the correct version.

While this sometimes happens in the code of the page, it’s often a mismatch between the code of the page and sitemaps. Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) looks at all the supported hreflang implementation locations, including the <head>, HTTP header, and sitemaps.

## 2.5% of domains have the same page referenced for more than one language

In this case, pages were referenced for more than one language in hreflang annotations. For example, you may see this issue if you reference the page in an hreflang tag that specifies the page is for English and another hreflang tag that says it’s for Spanish.

You shouldn’t have two languages on the same page, so check which one is correct and remove the other one.

## Final thoughts

A huge thanks and shoutout to my colleague, [Oleksiy Golvoko](https://twitter.com/zindelzindel?lang=en), for helping me gather this data! I’m surprised the numbers weren’t worse in the study, but I suspect that a lot of these sites have basic implementations.

Hreflang is complex and hard to get right. It can break in so many different ways. Here’s what Google’s John Mueller has to say about it.

https://twitter.com/JohnMu/status/965507331369984002

Want to see if your site has hreflang issues? Run it through [Site Audit](https://ahrefs.com/site-audit) or try it for free with [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools).

Hreflang is a topic I’m passionate about and one that I’ve written and presented many times, so I was happy to write this up. One of the first blog posts I made edits to when I joined Ahrefs was our [hreflang guide](https://ahrefs.com/blog/hreflang-tags/). I’d recommend that if you want to learn more about hreflang and some of the nuances of it.

If you have questions, message me [on Twitter](https://twitter.com/patrickstox).
