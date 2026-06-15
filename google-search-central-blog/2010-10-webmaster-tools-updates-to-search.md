---
title: "Webmaster Tools: Updates to Search queries, Parameter handling and Messages"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-10-webmaster-tools-updates-to-search"
url: "https://developers.google.com/search/blog/2010/10/webmaster-tools-updates-to-search"
canonical: "https://developers.google.com/search/blog/2010/10/webmaster-tools-updates-to-search"
author: "Jonathan Simon"
published: "2010-10-08T00:00:00+00:00"
updated: "2010-10-08T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:09:22+00:00"
status_code: 200
html_hash: "ed92ff6a27f6925fa9f54e336f7e2cfaa1eec90d9cb8018cdb08d59eaa2a2b7a"
clean_word_count: 857
clean_char_count: 5376
---
# Webmaster Tools: Updates to Search queries, Parameter handling and Messages

We've just released updates to several features in Webmaster Tools to provide you with more detail
and more control of how your site appears in search results.

## Search queries

Time does not stand still and neither should your site. With that in mind we've added a "Change"
column next to the impressions, clicks, clickthrough rate (CTR) and position columns, making it
easier to identify trends for each of these important metrics. The change column is tied to the
date range you specify, which should help when you're trying to pinpoint when a particular change
occurred.

![the new view of top search queries in webmaster tools](/static/search/blog/images/import/510163942d1a5e50ea10ab6723e8dedf.png)

Each query listed in Search queries now links to a query details page which includes a graph of
impressions and clicks for that specific query, providing a quick visual of its performance in the
search results over time. Below the graph is a table listing of the pages returned in search
results for that query, along with impressions, clicks and CTR. Each column in the table is
sortable, offering a quick way to re-sort the data based on what's most interesting to you. If
you'd rather use your own favorite tool to slice and dice the data you can use the "Download
this table" link to export all the information from the main Search queries page or from each
individual query details page.

![query detail view in the top search queries feature in webmaster tools](/static/search/blog/images/import/9369b95e53ad2ddf7e00427bc907ec90.png)

## Better Parameter Handling:

We've moved this feature under its own tab in the Settings section of Webmaster Tools, and
introduced a new action to manage parameters. When we introduced
[Parameter Handling](/search/blog/2009/10/new-parameter-handling-tool-helps-with)
last year, we allowed you to specify URL parameters and whether they should be ignored or not.
When you choose to ignore a parameter, you are telling us that this parameter has no impact on
the displayed content. For example, consider a session id parameter, like `sid` in the
following URLs:

```
https://example.com/product.php?item=swedish-fish
https://example.com/product.php?item=swedish-fish&sid=1234
https://example.com/product.php?item=swedish-fish&sid=5678
```

Assuming that these three URLs display exactly the same product page for tasty Swedish fish candy,
Google only needs to crawl and index one of them. You can simply select action "Ignore" for
parameter `sid` in Webmaster Tools and Google will just crawl and index one of these
URLs, avoiding duplicates.

In addition to the old functionality, you now have the ability to choose a specific value among
the known values for a given URL parameter. This is important when a parameter is relevant to the
content, but different values of this parameter lead to similar pages. For example, consider a
sorting parameter, like "sort-by" in the following URLs:

```
https://example.com/shop.php?category=candy&sort-by;=asc-price&page=1
https://example.com/shop.php?category=candy&sort-by;=desc-price&page=1
https://example.com/shop.php?category=candy&sort-by;=asc-price&page=2
https://example.com/shop.php?category=candy&sort-by;=desc-price&page=2
```

These four URLs show products in the candy category. There are enough items in this category to
fill two pages, and the products shown can be sorted by price, in ascending or descending order.
Selecting action "Ignore" for parameter "sort-by" would be incorrect and could potentially limit
our indexing of the site. This is because, after ignoring "sort-by", we would consider the first
two URLs equivalent and may choose to index the URL with ascending sort order. We would also
consider the last two URLs equivalent and may choose to index the URL with descending sort order.
In this scenario, we would be indexing the candy category inconsistently, with some candy products
appearing in both of the pages selected for the index, while other candy products not appearing in
either of them. The right solution comes from the new action "Use specific value" now available in
Webmaster Tools. To avoid duplicates but still keep our indexing consistent, you can simply select
action "Use specific value" for parameter "sort-by" and choose one of the valid values, say
`asc-price`. After this, our indexing would be fully consistent, as we would focus only
on the pages with products sorted by ascending price.

![the parameter handling tool feature in webmaster tools](/static/search/blog/images/import/c2ae69eb9ea47986f984da62fd1c0b86.png)

## Messages

Some sites receive lots of messages in the Webmaster Tools Message Center. With this update we've
added the ability to "star" specific messages that you deem important. There's now a separate
"Starred" view where you can see all the messages that you've starred, making tracking and finding
the most important messages for your site a breeze.

![starring messages in the webmaster tools message center](/static/search/blog/images/import/6fc7b79e993842d892262d085fb2fd8f.png)

We hope these updates make Webmaster Tools even more useful for your site. If you have feedback on
any of these updates, or if you have questions, post them in our
[Webmaster Help Forum](https://support.google.com/webmasters/community).
