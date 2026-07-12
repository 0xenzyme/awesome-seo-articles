---
title: "SEOs Are Breaking Pagination After Google Changed Rel=Prev/Next: Here's How to Get It Right"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "rel-prev-next-pagination"
url: "https://ahrefs.com/blog/rel-prev-next-pagination/"
canonical: "https://ahrefs.com/blog/rel-prev-next-pagination/"
author: "Patrick Stox"
published: "2020-04-15T00:00:10+00:00"
updated: "2024-06-16T21:13:32+00:00"
categories: []
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T11:58:59+00:00"
status_code: 200
html_hash: "9c7926270fec3fb04741ec47c40b07859d0490f5a4a2e9e293cfd9ceef39f5dd"
clean_word_count: 2155
clean_char_count: 12969
---
# SEOs Are Breaking Pagination After Google Changed Rel=Prev/Next - Here’s How to Get It Right

When Google announced that [rel=prev/next markup hadn’t been used in years](https://twitter.com/JohnMu/status/1108717486424363009), we noticed an increase in websites changing their implementation and actively harming their sites. Let’s look at what changed and what you should be doing.

The purpose of rel=prev/next is to indicate paginated pages in a series. [Google originally used the markup](https://webmasters.googleblog.com/2011/09/pagination-with-relnext-and-relprev.html) to share signals with the group of paginated pages while still swapping to show the most relevant page in their search results. Typical use cases included dividing content into multiple parts and creating multiple pages for product lists, forum threads, and lists of blogs.

Let’s take a look at what the actual code might look like for a three-page series.

**Page one:**
 This is the first page, so it only needs to reference the next page.

```
<link rel="next" href="https://website.com/page/2" />
```

**Page two:**
 This references both the next and previous pages in the series.

```
<link rel="next" href="https://website.com/page/3" />
<link rel="prev" href="https://website.com/page/1" />
```

**Page three:**
 This is the last page, so it only needs to reference the previous page.

```
<link rel="prev" href="https://website.com/page/2" />
```

However, in 2019, Google decided to tell us they no longer used rel=prev/next for pagination. Even worse, they apparently hadn’t used it for years.

> Spring cleaning!
>
> As we evaluated our indexing signals, we decided to retire rel=prev/next.
>  Studies show that users love single-page content, aim for that when possible, but multi-part is also fine for Google Search. Know and do what’s best for \*your\* users! [#springiscoming](https://twitter.com/hashtag/springiscoming?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/hCODPoKgKp](https://t.co/hCODPoKgKp)— Google Webmasters (@googlewmc) [March 21, 2019](https://twitter.com/googlewmc/status/1108726443251519489?ref_src=twsrc%5Etfw)

This change really didn’t impact SEO. For [duplicate content](https://ahrefs.com/blog/duplicate-content/), having some blocks of text the same isn’t going to hurt your site and there’s no penalty. Google will still try to find the best version of that content to show.

So the question is, why the change? And what should you do about it, if anything?

In this post, you’ll learn:

- [Why Google removed support for rel=prev/next](#why-google-removed-support-for-rel-next-prev)
- [How SEOs could have known rel=prev/next no longer worked](#how-seos-could-have-known)
- [Whether or not you should remove rel=prev/next from your pages](#should-seos-remove-rel-prev-next)
- [How to properly implement pagination in 2020](#acceptable-pagination-implementations)
- [How people are hurting their sites with improper implementation](#how-people-are-hurting-their-sites)

Let’s start at the top.

## Why did Google remove support for rel=prev/next?

Before Google dropped the bombshell that they no longer use rel=prev/next, [one of the official recommendations](https://web.archive.org/web/20131116024920/https://support.google.com/webmasters/answer/1663744?hl=en#) for pagination was to do nothing and let them figure it out.

> Do nothing. Paginated content is very common, and Google does a good job returning the most relevant results to users, regardless of whether content is divided into multiple pages.

Knowing this, the most likely reason they stopped using rel=prev/next is that they just got better at figuring it out and felt they no longer needed the additional hints.

Google has several options besides rel=prev/next that they can use to identify the pages in a series. For the most part, websites are consistent with their implementations of paginated pages, and Google can look at things like:

- Headings
- Page titles (same title or with a page number added)
- Links on the page ([internal links](https://ahrefs.com/blog/internal-links-for-seo/) to other pages in the set)

It’s also possible that the recommendations for pagination were leading to poor user experiences as sites split their content across multiple pages. Most of the time, this was done for page views and advertising revenue, but the experience was annoying to users and made it difficult for people to find what they were looking for. Here are [two](https://www.sheknows.com/entertainment/slideshow/2160450/best-dressed-celebrities-academy-awards-2020-photos/) [examples](https://www.harpersbazaar.com/uk/celebrities/red-carpet/g20947712/best-dressed-celebrities-models/?slide=10) of what I mean.

## How could SEOs have known rel=prev/next didn’t work?

When Google announced they hadn’t supported rel=prev/next in years, one of the first questions I got from a lot of SEOs was how could we as technical SEOs not have known this?

The simple answer is there wasn’t a way to tell. If Google had not told us, we wouldn’t know.

If the pagination were working, then Google would consolidate signals for the set of pages. While they would commonly show the first page in the set, they would also swap which page was shown if there was a more relevant page from the set in the search results. If the pagination wasn’t working, well, the same would happen because that’s how search works—Google returns the most relevant page for the query.

## Should SEOs remove rel=prev/next?

No.

If you’ve already implemented rel=prev/next on your website, do not remove it. Google was not the only source to use this information. It is still [recommended by W3C](https://www.w3.org/TR/relations.html) and used for web accessibility and ADA compliance. Some browsers also use it for prefetching. Also, [other search engines](https://ahrefs.com/blog/alternative-search-engines/) like Bing still use the markup.

> We’re using rel prev/next (like most markup) as hints for page discovery and site structure understanding. At this point we’re not merging pages together in the index based on these and we’re not using prev/next in the ranking model. <https://t.co/ZwbSZkn3Jf>— Frédéric Dubut (@CoperniX) [March 21, 2019](https://twitter.com/CoperniX/status/1108799603963514880?ref_src=twsrc%5Etfw)

## Acceptable pagination implementations

Most setups that use rel=prev/next also use self-referencing [canonical tags](https://ahrefs.com/blog/canonical-tags/). For this setup, don’t change anything at all. Treat the pages as you would any other indexable page on your site and make sure to internally link to other pages in the pagination set.

You can also [canonicalize](https://ahrefs.com/blog/canonicalization/) paginated pages so that they point to a view-all page that displays all the content. In this way, the content can still be broken up into pages for users, but the indexed version is going to contain all of the content.

## How people are hurting their sites

This is how a typical setup looks where each page is crawled and discovered:

But there are a few common mistakes people make when handling pagination that hurt their site. These are:

- Canonicalizing to the first page
- Noindexing pages
- Nofollowing links
- Blocking crawling

Let’s take a closer look at each of these issues, and how to check for them on your site.

### Mistake 1: Canonicalizing to the first page

The best-case scenario here is that Google ignores the canonical tag. If the canonical tags are respected, you’ll end up cutting off crawl paths to many pages and orphaning the content. This makes it harder for search engines to find and index valuable content, and also cuts off the flow of [PageRank](https://ahrefs.com/blog/google-pagerank/) throughout your site.

#### How to check for this mistake on your website

Crawl your site in [Ahrefs’ Site Audit](https://ahrefs.com/site-audit), then go to the Page Explorer and apply this set of filters:

If there are any matching URLs, take a look at the canonical URL. Pages in the pagination series that canonicalize to the first page should be changed.

### Mistake 2: Noindexing pages

Adding [noindex](https://ahrefs.com/blog/meta-robots/#:~:text=Instructs%20search%20engines%20not%20to%20index%20the%20page.%20That%20prevents%20it%20from%20showing%20in%20search%20results.) to pages is going to remove pages from the index. Those pages are no longer eligible to rank and PageRank won’t be passed.

While the links on the page may initially be crawled, that may change over time. Google Webmaster Trends Analyst John Mueller has mentioned that noindex pages will be treated as nofollow at some point, but it’s unknown how long that takes. When another Webmaster Trends Analyst Gary Illyes was asked about this, he seemed to think they would still be crawled. Without knowing fully how this works, it’s best to err on the side of caution and not noindex these pages unless you have an alternate crawl path.

#### How to check for this mistake on your website

Crawl your site in [Ahrefs’ Site Audit](https://ahrefs.com/site-audit), then go to the Page Explorer and apply this set of filters:

If there are any matching URLs, remove the noindex directive from the [robots meta tag](https://ahrefs.com/blog/meta-robots/) or X-Robots-Tag HTTP header on the page or URL.

### Mistake 3: Nofollowing links

Internal links to other paginated pages should never be marked [nofollow](https://ahrefs.com/blog/nofollow-links/). Nofollow is now a hint for Google, and your best case is that they ignore what you mark nofollow. What happens is you could cut off crawling and passing of signals like PageRank through your site and again can orphan pages.

#### How to check for this mistake on your website

Crawl your site in [Ahrefs’ Site Audit](https://ahrefs.com/site-audit), then go to the Page Explorer and apply this set of filters:

If there are any matching URLs, click on the number in the “No. of inlinks nofollow” column.

This will bring up an overlay showing where to find those nofollowed links on your site.

Remove the nofollow attributes from those specific links, or remove the nofollow directive from the robots meta tag or X-Robots-Tag HTTP header on the page or URL.

### Mistake 4: Blocking From Crawling

[Blocking the pages from crawling](https://ahrefs.com/blog/robots-txt/#:~:text=Use%20this%20directive%20to%20instruct%20search%20engines%20not%20to%20access%20files%20and%20pages%20that%20fall%20under%20a%20specific%20path.%20For%20example,%20if%20you%20wanted%20to%20block%20all%20search%20engines%20from%20accessing%20your%20blog%20and%20all%20its%20posts,%20your%20robots.txt%20file%20might%20look%20like%20this:) will again make it more difficult to find content on the website, end up orphaning pages, and also cut off the flow of PageRank through your site.

#### How to check for this mistake on your website

Check your robots.txt file for directives blocking search engines from crawling paginated pages. Here’s what that might look like:

```
User-agent: *
Disallow: /blog/page/
```

Remove these directives from your robots.txt file.

## Final thoughts

If you already had rel=prev/next implemented for pagination, leave it alone. There’s no reason to change it, and you’re likely to do more harm than good.

If you want to change pagination because you believe these paginated pages are low quality or they don’t provide much value, then consider grouping the pages in a way that’s useful to users and also provides an alternate crawl path for search engines. For example, if you wanted to use categories to group a bunch of blog posts, then that’s probably more useful to users than a bunch of paginated pages containing posts about many topics. These category pages containing posts about one topic have a chance of showing up in the [SERPs](https://ahrefs.com/blog/serps/) for relevant terms about the category.

If you’re going to use categories as the crawl and navigation path, you also need to make sure your categories are linked from your homepage. That may require a website redesign, so it’s not something I’d recommend unless you’re going to be changing your site design anyway. Even with this method, you may still end up using some form of pagination for the categories if you have a lot of posts in each one, so it also adds complexity to the setup.

If you haven’t implemented rel=prev/next yet and are wondering if you should, then that’s a tough call. I would say it mostly depends on the effort required to add it now vs. the impact. Remember that this markup is still used by other search engines, some browsers, and for accessibility, so it may still be worth the effort.

Just in case anyone needs a link to the original documentation that was deleted, [here you go](https://web.archive.org/web/20190217083902/https://support.google.com/webmasters/answer/1663744?hl=en).

Have questions about rel=prev/next or pagination? Message me on [Twitter](https://twitter.com/patrickstox).
