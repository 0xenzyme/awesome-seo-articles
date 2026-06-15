---
title: "Faceted Navigation: Definition, Examples & SEO Best Practices"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "faceted-navigation"
url: "https://ahrefs.com/blog/faceted-navigation/"
canonical: "https://ahrefs.com/blog/faceted-navigation/"
author: "Sam Underwood"
published: "2021-09-09T16:00:30+00:00"
updated: "2025-02-08T00:36:05+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:30:14+00:00"
status_code: 200
html_hash: "c73589045d88b398f9c80af6e8a95dc845a1cde8a5bc3e3bfbf4bbb11ad3fd58"
clean_word_count: 4970
clean_char_count: 30320
---
# Faceted Navigation: Definition, Examples & SEO Best Practices

If you’ve worked with any type of site that deals with a large number of listings, you’ve likely come across faceted navigation.

Faceted navigation is a widely accepted UX pattern that helps users discover what they’re looking for in less time. The downside is that it comes with many potential SEO complications that you’ll need to mitigate.

In this guide, you’ll learn:

- [What faceted navigation is](#what-is-faceted-navigation)
- [How faceted navigation works](#how-it-works)
- [SEO issues caused by faceted navigation](#seo-issues)
- [How to check for faceted navigation issues](#how-to-check)
- [How to fix faceted navigation issues](#how-to-fix)
- [How to prevent faceted navigation issues](#how-to-prevent)
- [How to use faceted navigation to get more traffic](#get-more-traffic)

## What is faceted navigation?

Faceted navigation is a UX pattern that helps users find specific listings on category/archive pages by allowing them to filter based on various attributes that the listings have. It’s commonly used on large sites as it speeds up the time for users to find what they’re looking for.

Many people also refer to faceted navigation as ‘faceted search’, or simply ‘filters’.

You will find this type of navigation on various types of sites; here are some examples:

- **E-commerce:** Filtering products by color, size, brand, and price.
- **Library catalogs:** Sorting books by genre, author, or publication year.
- **Travel platforms:** Refining flights or accommodations by date or airline.
- **Real estate:** Filtering properties by location, amenities, or price.
- **Online directories:** Narrowing down job or course listings by type or duration.

## How does faceted navigation work?

Faceted navigation works by filtering listings on category pages by their attributes. As mentioned, listings will often be:

- Jobs
- Products
- Hotels/flights

Attributes vary by site, but common examples include:

- Price
- Color
- Brand
- Weight
- Flight time
- Salary
- Pack quantity
- Delivery time

Once site admins have given relevant attributes to listings, the site then displays these attributes to the user in a list:

What happens when a user selects a filter varies, but generally one of four things will happen.

1. The listings instantly update to reflect the selection without a page reload (by using JavaScript).
2. The page reloads, and the listings reflect the selection (no JavaScript involved).
3. When the user selects an item in the list, nothing happens until they also click an ‘Apply’ button, which then updates the listings to reflect the selection (again, using JavaScript).
4. When the user clicks to apply the filters, a new page loads.

The first two options have a similar UX but a different UX pattern to option three.

Which UX pattern you use depends on whether a user is likely to use more than one filter. If users tend to apply multiple filters, it makes sense to only apply the filters and update the listings once they opt to apply them.

Once filters are applied, the URL can also optionally update to reflect the selection. What happens with the URL at this stage can also vary:

1. **It does nothing.** The listings update with no URL change.
2. **The site appends parameters to the URL** like ‘?colour=blue&brand=samsung’.
3. **The site appends a hash to the URL** identifying the facets applied, e.g., #colour=blue
4. **A new static URL is created** like /jeans/blue/ (the user is using a ‘blue’ color facet in this example).

## What SEO issues can faceted navigation cause?

The types of issues you’ll be looking to prevent or fix with a faceted navigation implementation include:

- Duplicate content
- Index bloat
- Crawling

Unfortunately, faceted navigation potentially creates a near-infinite number of facet combinations and indexable URLs. If you have issues with one of these, the SEO impact tends to be high.

Below are some examples of how these issues occur and their impact on your site’s SEO.

### Duplicate content

[Duplicate content](https://ahrefs.com/blog/duplicate-content/) is when the same or similar content is accessible at multiple URLs. Filters are notorious for creating URLs with duplicate content en masse. Duplication is mainly due to filter pages being close copies of the original page, just with different listings.

While duplicate content [isn’t necessarily a negative ranking signal](https://www.searchenginejournal.com/google-duplicate-content-is-not-a-negative-ranking-factor/394321/), it can cause issues with:

- [Keyword cannibalization](https://ahrefs.com/blog/keyword-cannibalization/)
- Dilution of ranking signals into multiple URLs (rather than consolidating into a single stronger URL)

See the ecommerce site currys.co.uk as an example. We start on their [HP PC Monitors page](https://www.currys.co.uk/gbuk/hp-computing/pc-monitors/pc-monitors/354_3057_30059_16_xx/xx-criteria.html). It’s a reasonably standard ecommerce layout, with a header, listings, and faceted search above the fold:

And then below the product listings, some content about HP monitors:

Now apply a filter for ‘4k monitors’.

You’ll see the product listings update, the H1 change, and the URL go from:

`/hp-computing/pc-monitors/pc-monitors/354_3057_30059_16_xx/xx-criteria.html`

To:

`/hp-4k-monitors/pc-monitors/pc-monitors/354_3057_30059_16_ba00012894-bv00311096/xx-criteria.html`

But if you scroll back to the bottom of the page, **the same block of content exists** below the listings.

This is just one example of duplication on the site. Scale this across every filter available, and you’ll quickly have millions of duplicate pages for Google to try and consolidate into one canonical page.

### Index bloat

Index bloat is when search engines index pages on your site that don’t have search value.

Only allowing Google to index quality pages is critical as having low-quality pages indexed can impact Google’s overall view of your site, as explained by John Mueller in [this video](https://www.youtube.com/watch?v=B1UrnctsiZU):

Faceted navigation can potentially create millions of indexable URLs with no unique content to them. It can also create page variants that provide no value to users using search engines.

Here’s an example:

AO.com has [a category page](https://ao.com/l/washing_machines-free_standing/1-9/1/) dedicated to freestanding washing machines:

A user may visit this page and decide they want to filter for:

- **Brand:** Samsung
- **Wash Load:** Large
- **Colour:** Silver
- **Wash Load:** Large
- **Features:** Quick Wash
- **Energy Rating:** A

Thanks to the filters, the site has returned precisely the washing machine that suits that user’s needs.

But would a user ever search in Google for something that precise?

The answer is resoundingly a no.

We know this because there are only an estimated 90 searches per month for ‘freestanding washing machines’ in the UK, so it’s extremely unlikely that there’ll be many (if any) searches for something even more specific like ‘large silver samsung freestanding washing machine with quick wash feature and energy rating A.’

Having pages like this indexed that do not cater to search demand and are low quality can put your site at risk of being impacted negatively by an algorithm.

Sidenote.

You should maintain a consistent order for your filter parameters. If the order is able to change, you will create even more URLs.

### Crawl budget wastage

Google can only dedicate a finite amount of resources to crawling the pages on your site. This is known as your [crawl budget](https://ahrefs.com/blog/crawl-budget/).

Managing crawl budget isn’t something that Google deems a priority unless you have a large site (1M+ unique pages) or medium site (10K+ unique pages) with very rapidly changing content.

Given that advice, if you only have a few thousand categories and products, you might think you don’t need to worry about crawl budget management.

That could be **very wrong.**

Some faceted navigation implementations will create a crawlable link for each facet combination available.

Ignoring the potential index bloat issues, this also means you’re potentially generating millions of URLs for Google to crawl, so you’ll quickly make crawl budget management something to consider.

You can find an example of this on the next.co.uk site:

When you inspect the HTML of a facet, you’ll see a link in the HTML:

[Once you’ve followed that link](https://www.next.co.uk/shop/gender-men-productaffiliation-coatsandjackets/size-40r), you can then check the HTML of another facet like the blue one:

You can see how the facets combine to create an entirely new URL to be crawled.

Now consider all the potential combinations of different filters. You can quickly see how crawling a site with facet issues would cause issues for a search engine.

### Dilution of PageRank

Faceted navigation can also dilute the PageRank passed around your site.

This is because PageRank is divided by the total number of links on the page. This presents an inherent issue with faceted navigation as a large number of them generate many internal links.

So rather than PageRank passing to important product or category pages, it’ll pass to the links found within your filters, which in most cases won’t help improve search traffic.

**Recommended reading:** *[Google PageRank is NOT Dead: Why It Still Matters](https://ahrefs.com/blog/google-pagerank/)*

## How to check for faceted navigation issues

There are always obvious telltale signs of faceted navigation issues; here are some steps to discover if your filters could be impacting your SEO.

### 1. Start with a site search

A great tactic to check for signs of index bloat quickly is to use the [site: search operator](https://ahrefs.com/blog/google-advanced-search-operators/). While not the most accurate way, it’s quick and easy to do.

It works by simply prepending ‘site:’ before your domain name, like below.

Take note of the number of results Google returns. Does that seem higher than the number of URLs you know to be available on your site?

If it is, that’s the first sign you have issues with index bloat.

### 2. Validate with Google Search Console (GSC) coverage reports

GSC’s coverage report is another great way to uncover crawling and indexing issues quickly.

Just head to the ‘Coverage’ report within GSC and select ‘Valid’ on the chart for a more accurate figure on the number of pages Google has indexed:

If this seems high, or you’ve recently implemented faceted search, and it’s shot up, this points towards the index bloat issues mentioned previously.

But how do we know if filters caused it?

Accurate XML sitemaps help diagnose issues here. If you’ve uploaded those to GSC, the table below the chart will split the indexed URLs down into:

- Indexed, not submitted in sitemap
- Submitted and indexed

That means we can look at ‘Indexed, not submitted in sitemap’ pages to see unwanted pages Google is indexing:

This example is for a betting site that lets you filter for locations and tournaments. We can see here Google is indexing unwanted URLs.

Another helpful way to discover potential issues is to filter for ‘Excluded’ URLs:

Investigating ‘Crawled - currently not indexed’ URLs can give you insights into pages Google is discovering but has decided not to index.

Google won’t index everything they crawl. If the page is of low quality like many facet pages are, they may decide not to index it.

In this example, we know there are 1,000 additional pages Google has discovered that they may index in the future. You can also view the URLs table to see faceted URLs by clicking on this report.

The above is a relatively mild example of issues with faceted navigation highlighted in GSC. Over time, these issues can scale to hundreds of thousands of URLs being discovered but not indexed (showing the potential crawling problems):

Or potentially hundreds of thousands of URLs being indexed when they shouldn’t be:

### 3. Collect more data with a site auditor

Using a site search and GSC is a great way to quickly get data on an issue, but neither will surface all indexable/indexed URLs, making it hard to spot trends and understand the scale of the problem.

Site auditing tools like the Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) can help remedy that by giving you detailed information on the URLs discovered from crawling the site.

The below example is a site with faceted navigation issues causing crawl budget wastage, and you can spot that with only a couple of clicks.

First, head to the **Indexability** report in the left sidebar.

Next, take a glance at the ‘Indexability distribution’ chart, and you’ll see if something looks off.

From a partial crawl, Site Audit found 39 non-indexable URLs for every indexable URL. Given that this isn’t a full crawl of the site, we could expect that the ratio of indexable to non-indexable URLs will likely worsen as the crawl continues.

The above highlights a **tremendous amount of crawl budget wastage**, and it’s also an excellent example of a crawler trap—where technical issues create an almost infinite amount of irrelevant URLs for search that a bot will crawl.

If your faceted navigation is causing index bloat, the chart you’ll see here will look a bit different. Rather than a large amount of non-indexable URLs, you’ll see vast amounts of indexable URLs on the chart like the below.

To confirm this is a faceted navigation issue, select the non-indexable portion of the chart and scan the list. You’ll now see a table of all the non-indexable pages crawled.

Here is where you’ll need to spot a pattern.

What’s causing crawlers to find all of these non-indexable pages?

If the vast majority of the URLs returned in the table are faceted URLs, you’ve found yourself a faceted navigation issue.

## How to fix faceted navigation issues

Now that you know how to check for faceted navigation problems, here’s how to fix them.

### 1. Fix indexing with the canonical tag

If you’re facing indexing issues but no alarming crawl budget issues (and don’t have a huge site), the best solution is arguably to use [the canonical tag](https://ahrefs.com/blog/canonical-tags/). It consolidates link signals for similar/duplicate pages into the URL you specify as the canonical.

The benefit?

If you have links to a facet page, which then canonicalizes to the non-facet page, those link signals aren’t lost; search engines will pass them to the category page, which may help it to rank.

Here’s an example of how to implement this…

Say this is the URL of your category page:

`https://example.com/washing-machines/samsung/`

Your facet URLs work with [parameters](https://ahrefs.com/blog/url-parameters/), so when someone applies some filters, the URL looks like this:

`https://example.com/washing-machines/samsung/?drumsize=16kg&color=silver&energyrating=A`

On the above facet URL above, you’d simply add a canonical tag pointing back to the category page, so your canonical tag would look like this:

```
<link rel="canonical" href="https://example.com/washing-machines/samsung/" />
```

Or like this in your HTTP headers:

```
Link: <https://example.com/washing-machines/samsung/>; rel="canonical"
```

While this seems like a nice and easy fix for a serious SEO problem, as always, there are some potential issues, the main one being that Google may ignore your canonical tag.

This is simply because canonical tags are suggestions to search engines, not directives. So if Google, for some reason, thinks that you’ve implemented the tag incorrectly, they may decide to ignore it.

The common reasons Google will decide to ignore your canonical tag suggestions are:

- **The pages aren’t duplicates.**If your facet pages significantly change when you apply a filter, Google will likely think they aren’t duplicates of one another. For example, if content, titles, and headers change, Google may get confused.
- **You internally link to facet pages.**If you have many internal links to a canonicalized facet page, Google may misunderstand the page’s importance and ignore your canonical tag.

If you don’t see the number of valid URLs in your coverage reports decreasing after implementing the canonical tag, move onto step two.

### 2. Fix crawling with robots.txt

If you’re facing crawl budget issues and you don’t need signals to consolidate, you’ll want to use robots.txt to block Google from crawling any faceted URLs.

To block crawling of a URL with the robots.txt, add a disallow rule like the below:

```
User-agent: *
Disallow: *size=*
```

In the example above, I’ve added two wildcards (\*) around the parameter. If your faceted navigation works by appending directories, your rule will look like this:

```
User-agent: *
Disallow: */size/*
```

There are two instances when the robots.txt doesn’t work well:

- **You have no discernible patterns within the URL for disallowing.** This could be because each page is given unique parameters or directories for facets.
- **You want to allow some URL patterns to be crawled and block others.** For example, you want the /color/ directory to be crawled for the t-shirts category (as it provides value for search), but want it blocked for the underwear category. While you could work around this by mixing ‘Allow’ and ‘Disallow’ rules within the robots.txt, this can quickly become difficult to manage on large-scale websites.

You should also be aware blocking crawling doesn’t necessarily prevent Google from indexing the blocked URLs. Generally speaking, Google **will** drop blocked URLs from the index—but only if they have no backlinks and/or many followed internal links pointing to them. In other words, as long as nothing else is signalling to Google that those URLs are valuable.

### 3. Nofollow and/or remove internal links to faceted URLs

If blocking crawling doesn’t fully eliminate indexing issues caused by faceted search, nofollowing internal links to those URLs **may** solve the problem.

There are typically two sources of these links:

1. **Faceted search links**. I.e., links within your faceted navigation.
2. **Links elsewhere on your website**. E.g., from blog posts, etc.

**For faceted search links**, applying a blanket nofollow is easy enough with a bit of basic coding. However, this probably isn’t the best idea if you have canonical tags on faceted URLs and/or faceted URLs that you want Google to index. Reason being, if Google ends up not crawling these links because they’re nofollowed, it can cause other indexing issues.

The alternative is to pick and choose the facets that you nofollow. That’s a bit harder to implement from a technical standpoint, but it can be worth it if you want to target long-tail queries with faceted search (more on that later).

The main downside of this approach is that it’s less useful after [Google started treating rel=’nofollow’ as a hint](https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify), meaning it’s not a directive like the robots.txt is.

However, Google will use an internal nofollow to indicate that the URL within the href attribute isn’t that important and Google should deprioritize crawling it.

John Mueller has [confirmed this](https://www.searchenginejournal.com/google-internal-nofollow-links/327545/):

> […] we will continue to use these internal nofollow links as a sign that you’re telling us:
>
> - These pages are not as interesting.
> - Google doesn’t need to crawl them.
> - They don’t need to be used for ranking, for indexing.
>
>
>
> John Mueller, Search Advocate [Google](https://www.google.com/)

Sidenote.

This approach doesn’t correct the dilution of PageRank. PageRank is still distributed between all links on the page, even those with the nofollow attribute. If you want to fix that, you’ll need to implement proper [canonicalization](https://ahrefs.com/blog/canonicalization/).

**For links elsewhere on your website**, your best bet is to just remove them.

You can find internal links to problematic faceted URLs using Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer):

1. Enter a problematic faceted URL.
2. Go to the **Internal Backlinks** report.
3. Filter for **Dofollow** links.

You can then simply look for ‘followed’ internal links elsewhere on your site and remove them.

### 4. Definitively fix indexing with the noindex tag

If you’re still facing indexing issues after following the steps above, then your last port of call is [the noindex tag](https://ahrefs.com/blog/meta-robots/).

The benefit of the noindex tag is that it’s a surefire way to prevent the indexing of facet pages. The downside is you don’t consolidate ranking signals, and over time, Google may stop crawling internal links on a noindexed page, meaning no passage of ranking signals.

Still, this is a good way of getting faceted URLs out of Google’s index if all else fails.

To implement this, simply add either a meta robots tag in the <head> of a faceted URL:

```
<meta name="robots" content="noindex">
```

Or the X-Robots header within your HTTP headers of a faceted URL:

```
X-Robots-Tag: noindex
```

You then **need** to remove/adjust any crawl blocks for the URL in robots.txt. Fail to do this, and Google will never see the noindex directive—meaning that the page will stay indexed.

### 5. Return a 404 status code for filter combinations with no results

A 404 response signals that the page does not exist, discouraging indexing and ensuring search engines focus on product-rich pages instead.

Without this, search engines might waste crawl budget on thin or empty pages, diluting the authority of more valuable pages.  However, if a temporary stock issue causes the empty results, a 200 status with a helpful message may be more appropriate to retain user experience.

**Recommended reading:** *[Robots Meta Tag & X‑Robots-Tag: Everything You Need to Know](https://ahrefs.com/blog/meta-robots/)*

## How to prevent faceted navigation issues in the first place

From the previous section, you would have realized that correcting all the potential issues faceted navigation can create isn’t easy.

Every approach to fix both indexing and crawling has some downsides or complications.

But there is a better way.

Suppose you’re implementing a new faceted navigation configuration or creating one for the first time. In that case, you can circumvent all of the above issues while still making the most of the UX benefits.

Here’s how to do that.

### 1. Use AJAX and avoid internal links

First, build your faceted navigation with AJAX and don’t add any <a href=…> internal links.

By doing that, users get a great experience due to the page not reloading whenever they filter, and Google won’t see any internal links to facet pages, meaning:

1. They don’t crawl them
2. Resulting in Google not indexing them
3. While also removing any potential dilution of PageRank

Here’s an example.

I’ve implemented faceted navigation with the WP Grid Builder WordPress plugin on a resource I created called [SEO Toolbelt](https://seotoolbelt.co/).

It looks like this:

When you right-click and inspect element on any of the checkboxes to apply a filter, you’ll see they don’t include a <a href=…> link on them, preventing Google from crawling any additional URLs.

Because of that, I’ve circumvented having to even think about crawl budget wastage from faceted navigation.

### 2. Ensure URLs are still shareable

Next, we need to make sure that when a user clicks a filter, the URL changes.

I recommend doing this as we’ve materially changed the contents of the page, and ideally, if a user bookmarks, links to the page, or shares a URL with a friend, the contents of the URL will still reflect the filters they applied when they bookmarked/shared/linked the page.

There are two ways to do this:

- URL parameters (?)
- URL hashes (#)

The best solution is URL hashes, as Google tends to ignore anything after the hash in the URL.

WP Grid Builder uses parameters, so after applying the filter, the URL changes to be something like this:

`https://seotoolbelt.co/tools/auditing/?_tool_type=browser-extension`

If you access that URL, you’ll see the filtered grid of tools is updated to reflect the applied filters.

In this instance, as I’m using URL parameters, I’ll also need to add a canonical tag to the version of the URL without parameters, so this URL:

`https://seotoolbelt.co/tools/auditing/`

Given that these parameter versions of URLs aren’t internally linked to and are much less likely to receive external links from other sites (which is the only way Google would discover them), we’re at low risk of them being ignored.

### 3. Provide alternate crawl paths to important pages for search

In some cases, a filtered version of a page may be helpful for search.

For example, there are filters for ‘Firefox’ and ‘Chrome’ on my SEO browser extensions page. Both of these pages have some search potential.

So we want to make sure that they have indexable URLs created. The best way to do that is by making sure you have alternate crawl paths to those pages. I’ve done that by adding sub-navigation links to indexable versions of those filter pages at the top of the page.

Those sub-collections are generated based upon the same attributes that create the faceted version of the page, but I have to ‘opt-in’ to making them.

This implementation has achieved a few things:

- I’ve prevented crawl budget wastage, as I don’t internally link to facet pages.
- The facet pages have remained shareable, which is a positive UX.
- If a facet page has search potential, I can editorially allow this page to be indexed.

As you can see, this is significantly simpler to manage SEO-wise but doesn’t have any drawbacks.

## How to use faceted navigation to get more traffic

So far, I’ve positioned faceted navigation as something that just causes SEO complications. However, you can also use faceted navigation as a way to get more traffic by pairing it [with a long-tail keyword strategy](https://ahrefs.com/blog/long-tail-keywords/).

I can’t understate how incredibly beneficial getting this right can be. Ahrefs data shows that 99.84% of keywords get fewer than 1,000 searches per month, and account for 39.33% total search demand:

​​

Facet URLs are ideal for capturing long-tail traffic, given how facets create more specific versions of pages targeting broader queries.

First, I will run you through the steps to spot opportunities to capture more long-tail traffic with faceted navigation; then, I’ll explain some implementation considerations.

### 1. Identify long-tail keyword variations

To start with, you’ll need to identify keyword opportunities with Ahrefs Keyword Explorer. Doing this is incredibly easy.

Enter the name of a category you already have on your site, like ‘high rise jeans.’

Head to the ‘Matching Terms’ report.

Use the terms sidebar and change over to ‘Parent Topics.’

By doing this, the tool will group all keywords with a similar SERP together. You can then scan this list and pick out potential facet pages that’d be worth making indexable. Here are some I’ve spotted from checking the screenshot above:

- high rise bootcut jeans (1,900 searches)
- high rise skinny jeans (1,800 searches)
- high rise wide leg jeans (1,300 searches)
- ultra high rise jeans (970 searches)
- high waisted boyfriend jeans (700 searches)
- high rise super skinny jeans 380 searches)
- high waisted white jeans (360)

### 2. Make those pages indexable

Next, we need to make these pages both crawlable and indexable to Google.

This can work in a few different ways depending on your type of faceted navigation.

#### Faceted navigation with internal links

If you’ve implemented faceted navigation that isn’t the ideal setup and does have internal links to each facet, for these URLs you’ll need to make sure that:

- The canonical tag is self-referential.
- The noindex tag is removed (if applicable).
- Any relevant disallow rules within the robots.txt are removed (or that you’ve added an allow rule)
- Any nofollow attributes on internal links are removed (if applicable)

Precisely what you need to do above depends on your implementation, but the important part is that search engines can both crawl and index these pages.

#### AJAX faceted navigation without internal links

You’ll need to create a sub-category page for the ideal faceted navigation setup mentioned in the previous section.

You’ll need to do this because the faceted navigation isn’t generating internal links, so you can’t use it to create these pages for you.

Most ecommerce platforms support creating sub-categories, but ideally, you want additional functionality to base the sub-categories products upon a filtered version of the parent category, mainly to save having to merchandise each sub-category manually. This way, you get the benefits of quickly generating pages like faceted navigation does while still circumventing SEO complications.

For example, if we’re creating a ‘high rise skinny jeans’ sub-category, we’d want to inherit the ‘high rise jeans’ product listings but only show products that also have the ‘skinny’ attribute applied.

### 3. Optimize the URLs for search

This is an obvious one, but you’ll want to do the fundamental SEO optimizations, such as:

- Have simple, readable URLs. For example, your URL should ideally be `/jeans/high-rise/skinny/`, not `/jeans/high-rise/?fit_variant=skinny`
- Optimized title tags, meta descriptions, and header tags.
- Unique written content.
- Adding the URL to XML sitemaps.

The main complications here tend to be with configurations where you’re opting a facet page out of the default indexing and crawling controls in place.

This is simply because, technically, facet pages are inherently dynamic and aren’t the same as creating a new sub-category.

Custom functionality would be required to ensure critical on-page optimizations are possible with faceted URLs.

## Final thoughts

Hopefully, now you’ve fully understood not just the inherent risks with faceted navigation for SEO but also the significant opportunities it presents to optimize for long-tail search.

Got a question on faceted navigation? [Tweet me.](https://twitter.com/SamUnderwoodUK)
