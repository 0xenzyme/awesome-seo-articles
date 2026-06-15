---
title: "Meta Keywords: What Are They and Should You Use Them?"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "meta-keywords"
url: "https://ahrefs.com/blog/meta-keywords/"
canonical: "https://ahrefs.com/blog/meta-keywords/"
author: "Joshua Hardwick"
published: "2020-12-15T19:24:19+00:00"
updated: "2023-10-05T08:02:49+00:00"
categories:
  - "On-Page SEO"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T11:50:28+00:00"
status_code: 200
html_hash: "0f6704c2a559524676cfd6d70c8df9d123de528c065503d57165e70c9f50f394"
clean_word_count: 1740
clean_char_count: 10567
---
# Meta Keywords: What Are They and Should You Use Them?

Meta keywords are [meta tags](https://ahrefs.com/blog/seo-meta-tags/) that you can use to give search engines more information about a page’s content. They’re found in a webpage’s HTML source code, and are not visible to visitors.

Here’s an example of a meta keywords tag:

`<meta name="keywords" content="seo, search engine optimization"/>`

It’s easy to add meta keywords in most website builders and CMS’, but should you bother?

- [Do you still need meta keywords?](#do-you-still-need-meta-keywords)
- [Other use cases for meta keywords](#meta-keywords-use-cases)
- [How to remove meta keywords](#remove-meta-keywords)

## Do you still need to use meta keywords?

Google hasn’t used the meta keywords tag to help rank web pages for at least a decade. We know this because Matt Cutts, Google’s former Head of the Webspam Team, released [a video](https://www.youtube.com/watch?v=jK7IPbnmvVU) in 2009 where he said:

> […] we don’t use the keywords meta tag in our search ranking

Fast-forward to 2020, and according to [a recent Twitter poll](https://twitter.com/bill_slawski/status/1266409136125734913) by Bill Slawski, most SEO professionals no longer use the meta keywords tag.

> Do you still use meta keywords tags on pages you optimize?— Bill Slawski ⚓ (@bill\_slawski) [May 29, 2020](https://twitter.com/bill_slawski/status/1266409136125734913?ref_src=twsrc%5Etfw)

However, it’s important to remember that there’s more to SEO than Google, so there are a couple of reasons why you might still want to use the keywords meta tag.

### 1. It may still be used by Yandex

Yandex is the Internet’s largest Russian search engine, with [a market share roughly equal to that of Google’s](https://www.liveinternet.ru/stat/ru/searches.html?slice=ru) in Russia. Their official documentation [states](https://yandex.com/support/webmaster/controlling-robot/html.html) that meta keywords “Can be used when determining the page’s relevance to search queries.”

Does this mean that meta keywords are a proven ranking factor in Yandex search? No. But as that page has only been live since late-2018, the information is likely still accurate.

Even so, as one person mentioned on Twitter, it’s probably a low-weight factor.

> “Officially” they say they still do, but I think this is a very low weight factor, even for яндекс. This is the consensus among most of us who have done SEO in Russian 🙂<https://t.co/RrNAmzR0Vb>— orun bhuiyan (@orvn) [May 29, 2020](https://twitter.com/orvn/status/1266417952515067904?ref_src=twsrc%5Etfw)

If you’re curious about other [search engines](https://ahrefs.com/blog/alternative-search-engines/), it looks like none of the major ones use meta keywords:

#### Bing

In 2014, Bing stated in [a blog post](https://blogs.bing.com/webmaster/2014/10/03/blame-the-meta-keyword-tag/) that the meta keywords tag is “dead in terms of SEO value.” This was effectively confirmed in 2020 when Bing’s Head of Evangelism [tweeted](https://twitter.com/ChristiJOlson/status/1266415751172247552) the same thing.

> The meta keyword tag is dead in terms of SEO value for [@BingWMC](https://twitter.com/BingWMC?ref_src=twsrc%5Etfw). We exclude it and ignore it. [@CoperniX](https://twitter.com/CoperniX?ref_src=twsrc%5Etfw) [@facan](https://twitter.com/facan?ref_src=twsrc%5Etfw)— Christi Olson (@ChristiJOlson) [May 29, 2020](https://twitter.com/ChristiJOlson/status/1266415751172247552?ref_src=twsrc%5Etfw)

However, in 2011, Bing [hinted](https://www.seroundtable.com/bing-wont-rule-out-meta-keywords-tag-29535.html) that it could be used as a spam signal to help identify low-quality pages. It’s unknown whether that’s still the case, but it’s definitely not a [ranking factor](https://ahrefs.com/blog/google-ranking-factors/).

#### Baidu

In 2012, a Baidu engineer [stated](https://web.archive.org/web/20201028033221/http://bbs.zhanzhang.baidu.com/thread-7625-23-1.html) in their webmaster community that “Meta keywords have long been in the garbage heap of history, and we will ignore them directly.”

However, on [a page](https://zy.baidu.com/academy/detail?id=2961) updated in April 2020, they say:

> Title, description and **keywords** are important for Baidu to evaluate page’s value.

As it makes sense to trust the most recent information, it seems the keywords meta tag could be a ranking signal in Baidu.

#### Naver

According to [Wikipedia](https://en.wikipedia.org/wiki/Naver), Naver handles 74.7% of all web searches in South Korea. And while we couldn’t find a definitive statement about their use of the meta keywords tag, there’s zero mention of meta keywords throughout their [extensive documentation](https://searchadvisor.naver.com/guide/) on optimizing your website.

Given that fact, we can assume it’s either not used or is a very low-weight factor.

### 2. It’s used for some internal site searches

Most popular CMS’ don’t use the meta keywords tag for internal site searches, but some internal search systems can, including SOLR, Algolia, and ones built on Elasticsearch.

If any of these power your internal search, you might need to use the keywords meta tag.

## Other use cases for meta keywords

You’ve probably realized by now that most people don’t need to use the keywords meta tag, but there are a couple of things you can use it for.

### 1. Create an internal tagging system

Many CMS’ and website builders make it easy to add meta keywords to pages, as do many free [WordPress SEO plugins](https://ahrefs.com/blog/best-seo-plugins-for-wordpress/). This makes it easy to ‘repurpose’ the tag for an internal keyword tagging system. Just set the tag as your target keyword on each page.

For example, if our page’s target keyword was “[SEO tips](https://ahrefs.com/blog/seo-tips/),” it’d look like this:

`<meta name="keywords" content="seo tips"/>`

If you do this on every page, it’ll be easy to check whether you’ve already targeted a keyword in the future. Just crawl your site with an auditing tool like Ahrefs’ [Site Audit](https://ahrefs.com/site-audit), then use **Page Explorer** to look for pages with your keyword in the meta keywords tag.

There are three reasons it can be useful to do this:

1. **Help prevent keyword cannibalization.** [Keyword cannibalization](https://ahrefs.com/blog/keyword-cannibalization/) is where a website targets the same keyword across multiple pages. It can cause all kinds of issues, like undesirable pages outranking desirable pages.
2. **Avoid overlapping work.** If you work in [enterprise SEO](https://ahrefs.com/blog/enterprise-seo/), there are probably many people and teams working on similar things. Having an internal keyword tagging system helps prevent multiple teams from targeting the same keyword.
3. **Find collaboration opportunities.** If you see that you’re not ranking well for one of your keywords, you might want to collaborate with another team to improve and update your content.

Just know that there’s one potential downside to using the meta keywords tag for this purpose, which we’ll talk about in [the next section](#remove-meta-keywords).

### 2. Find ‘seed’ keywords from competitors

Bill Slawski’s [recent Twitter poll](https://twitter.com/bill_slawski/status/1266409136125734913) shows that roughly 33% of people still use the keywords meta tag. As some of those people will undoubtedly be your competitors, this can come in quite handy for finding ‘seed keywords’ during [keyword research](https://ahrefs.com/seo/keyword-research). Just look for the keywords meta tag on your competitor’s homepage.

For example, here’s the keywords meta tag for the homepage of a popular toy store:

It lists a bunch of toy-related keywords like *toys*, *climbing accessories*, *climbing frames*, *games*, *inflatables*, *pre school*, *sandboxes*, *slides*, etc.

Paste any relevant ones into a [keyword research tool](https://ahrefs.com/blog/free-keyword-research-tools/) like Ahrefs’ [Keywords Explorer](https://ahrefs.com/keywords-explorer) and choose a keyword ideas report. You’ll find thousands or even millions keyword ideas—complete with estimated monthly [search volumes](https://ahrefs.com/blog/keyword-search-volume/) and [SEO metrics](/blog/ahrefs-seo-metrics/).

You can use the inbuilt filters to narrow your search.

For example, here are all the keywords related to hand puppets with low [Keyword Difficulty](https://ahrefs.com/blog/keyword-difficulty/) scores.

Just know that you might need to check a few sites before you find any useful [seed keywords](https://ahrefs.com/blog/seed-keywords/) because many fill their keywords meta tags with junk or leave them empty.

## How to remove meta keywords

Given that you can use the meta keywords to ‘spy’ on your competitors’ keywords, they can also do the same for you. For that reason, unless you have a legitimate reason to use it, you might want to remove any lingering meta keywords from your website.

But first, you need to find them…

You can do this for free with [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools). Just sign up, crawl your website with Ahrefs’ [Site Audit](https://ahrefs.com/site-audit), then use these filters in **Page Explorer**:

You’ll see a list of all pages on your website that have a meta keywords tag.

If there are no results, there are no pages with the tag.

From there, all you need to do is run through and remove the tags from any offending pages.

Just know that this probably isn’t worth doing if you have a big website with keywords meta tags on every page. However, if you see the same meta keywords across all pages, chances are it’s being pulled from one location in your CMS or template/theme. In which case, you can likely remove it from all pages by editing just one piece of code.

That said, it’s worth noting that having meta keywords tags on your site is unlikely to have a negative SEO impact. Unless you’re overly concerned about competitors ‘stealing’ your keywords, your time is probably better spent elsewhere.

## Final thoughts

For 99.9% of people, the meta keywords tag is useless, and filling it out is a waste of time. You should only use it if you have a particular reason to do so, like using it for an internal keyword tagging system or an internal site search.

Other [meta tags](https://ahrefs.com/blog/seo-meta-tags/) like your [title](https://ahrefs.com/blog/title-tag-seo/) and [meta description](https://ahrefs.com/blog/meta-description/) deserve more attention.

Got questions? Ping me [on Twitter](https://twitter.com/joshuachardwick?lang=en).
