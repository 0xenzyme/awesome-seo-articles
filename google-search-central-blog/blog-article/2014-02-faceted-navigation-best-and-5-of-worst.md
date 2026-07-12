---
title: "Faceted navigation best (and 5 of the worst) practices"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-02-faceted-navigation-best-and-5-of-worst"
url: "https://developers.google.com/search/blog/2014/02/faceted-navigation-best-and-5-of-worst"
canonical: "https://developers.google.com/search/blog/2014/02/faceted-navigation-best-and-5-of-worst"
author: "Maile Ohye"
published: "2014-02-12T00:00:00+00:00"
updated: "2014-02-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:23:42+00:00"
status_code: 200
html_hash: "bb0d6030ce77aca756d7555889f3b7416be5a7bec56ad91cf41159256e820f9c"
clean_word_count: 2918
clean_char_count: 21244
---
# Faceted navigation best (and 5 of the worst) practices

![Selecting filters with faceted navigation can cause many URL combinations](/static/search/blog/images/import/74b0b0afe58239f7e70336fa220bc8e7.png)

*Selecting filters with faceted navigation can cause many URL combinations, such as
`https://www.example.com/category.php?category=gummy-candies&price=5-10&price=over-10`*

Faceted navigation, such as filtering by color or price range, can be helpful for your visitors,
but it's often not search-friendly since it creates many combinations of URLs with
[duplicative content](/search/docs/advanced/guidelines/duplicate-content). With
duplicative URLs, search engines may not crawl new or updated unique content as quickly, and/or
they may not index a page accurately because indexing signals are diluted between the duplicate
versions. To reduce these issues and help faceted navigation sites become as search-friendly as
possible, we'd like to:

- [Provide background and potential issues with faceted navigation](#background)
- [Highlight worst practices](#worst-practices)
- Share best practices

  - [New faceted navigation implementations or redesigns](#new-sites)
  - [Existing faceted navigation implementations](#existing-sites)

## Background

In an ideal state, unique content—whether an individual product/article or a category of
products/articles— would have only one accessible URL. This URL would have a clear click
path, or route to the content from within the site, accessible by clicking from the home page or a
category page.

### Ideal for searchers and Google Search

- Clear path that reaches all individual product/article pages

  ![On the left is potential user navigation on the site (or, the click path), on the right are the pages accessed.](/static/search/blog/images/import/df35374908a244695f0803c6bc698e2a.png "On the left is potential user navigation on the site (or, the click path), on the right are the pages accessed.")
- One representative URL for category page
  `https://www.example.com/category.php?category=gummy-candies`

  ![Category page for gummy candies](/static/search/blog/images/import/d6a0a5e654a74a98d42f5f615e528b6e.png)
- One representative URL for individual product page
  `https://www.example.com/product.php?item=swedish-fish`

  ![One representative URL for individual product page](/static/search/blog/images/faceted-nav-representative-url.png)

### Undesirable duplication caused with faceted navigation

- Numerous URLs for the same article/product

  - Canonical: `example.com/product.php?item=swedish-fish`

    ![Canonical URL for the same product](/static/search/blog/images/import/f22edc33107a27646e59ddd2f1f69762.png)
  - Duplicate:
    `example.com/product.php?item=swedish-fish&category=gummy-candies&price=5-10`

    ![Duplicate URL for the same product](/static/search/blog/images/faceted-nav-duplicate.png)

  The same product page for swedish fish can be available on multiple URLs.
- Numerous category pages that provide little or no value to searchers and search engines), as
  demonstrated in the following table:

  |  |  |  |
  | --- | --- | --- |
  | **URL** | `example.com/category.php?category=gummy-candies&taste=sour&price=5-10` | `example.com/category.php?category=gummy-candies&taste=sour&price=over-10` |
  |  | category page for gummy candies in the price range $5-10 | category page for gummy candies that are over $10 |
  | **Issues** | - No added value to Google searchers given users rarely search for "sour gummy candy   price five to ten dollars". - No added value for search engine crawlers that discover same item ("fruit salad")   from parent category pages (either "gummy candies" or "sour gummy candies"). - Negative value to site owner who may have indexing signals diluted between numerous   versions of the same category. - Negative value to site owner with respect to serving bandwidth and losing crawler   capacity to duplicative content rather than new or updated pages. | - No value for search engines (should have   [404 response code](/search/docs/crawling-indexing/http-network-errors)). - Negative value to searchers. |

## Worst (search un-friendly) practices for faceted navigation

### Worst practice #1: Non-standard URL encoding for parameters, like commas or brackets, instead of `key=value&` pairs.

#### Worst practices:

```
example.com/category?[category:gummy-candy][sort:price-low-to-high][sid:789]
```

- Key-value pairs marked with `:` rather than `=`.
- Multiple parameters appended with `[ ]` rather than `&`.

```
example.com/category?category,gummy-candy,,sort,lowtohigh,,sid,789
```

- Key-value pairs marked with a `,` rather than `=`.
- Multiple parameters appended with `,,` rather than `&`.

#### Best practice:

```
example.com/category?category=gummy-candy&sort=low-to-high&sid=789
```

While humans may be able to decode odd URL parameters, such as `,,`, crawlers have
difficulty interpreting URL parameters when they're implemented in a non-standard fashion.
Software engineer on Google's Crawling Team, Mehmet Aktuna, says "Using non-standard encoding is
just asking for trouble." Instead, connect key-value pairs with an equal sign (`=`) and
append multiple parameters with an ampersand (`&`).

### Worst practice #2: Using directories or file paths rather than parameters to list values that don't change page content.

#### Worst practice:

Where `/c123/` is a category, `/s789/` is a
[session ID](https://wikipedia.org/wiki/Session_ID) that doesn't
change page content:

```
example.com/c123/s789/product?swedish-fish
```

#### Good practice:

The directory, `/gummy-candy/`, changes the page content in a meaningful way:

```
example.com/gummy-candy/product?item=swedish-fish&sid=789
```

#### Best practice:

URL parameters allow more flexibility for search engines to determine how to crawl efficiently.

```
example.com/product?item=swedish-fish&category=gummy-candy&sid=789
```

It's difficult for automated programs, like search engine crawlers, to differentiate useful values
(for example, `gummy-candy`) from the useless ones (for example,
`sessionID`) when values are placed directly in the path. On the other hand, URL
parameters provide flexibility for search engines to quickly test and determine when a given value
doesn't require the crawler access all variations.

Common values that don't change page content and should be listed as URL parameters include:

- Session IDs
- Tracking IDs
- Referrer IDs
- Timestamp

### Worst practice #3: Converting user-generated values into (possibly infinite) URL parameters that are crawlable and indexable, but not useful in search results.

#### Worst practices:

For example, user-generated values like longitude/latitude or "days ago" as crawlable and
indexable URLs:

```
example.com/find-a-doctor?radius=15&latitude=40.7565068&longitude=-73.9668408
```

```
example.com/article?category=health&days-ago=7
```

#### Best practices:

```
example.com/find-a-doctor?city=san-francisco&neighborhood=soma
```

```
example.com/articles?category=health&date=january-10-2014
```

Rather than allow user-generated values to create crawlable URLs—which leads to infinite
possibilities with very little value to searchers—perhaps publish category pages for the
most popular values, then include additional information so the page provides more value than an
ordinary search results page. Alternatively, consider placing user-generated values in a separate
directory and then robots.txt disallow crawling of that directory.

```
example.com/filtering/find-a-doctor?radius=15&latitude=40.7565068&longitude=-73.9668408
```

```
example.com/filtering/articles?category=health&days-ago=7
```

with robots.txt:

```
User-agent: *
Disallow: /filtering/
```

### Worst practice #4: Appending URL parameters without logic.

#### Worst practices:

```
example.com/gummy-candy/lollipops/gummy-candy/gummy-candy/product?swedish-fish
```

```
example.com/product?cat=gummy-candy&cat=lollipops&cat=gummy-candy&cat=gummy-candy&item=swedish-fish
```

#### Better practice:

```
example.com/gummy-candy/product?item=swedish-fish
```

#### Best practice:

```
example.com/product?item=swedish-fish&category=gummy-candy
```

Extraneous URL parameters only increase duplication, causing less efficient crawling and indexing.
Therefore, consider stripping unnecessary URL parameters and performing your site's "internal
maintenance" before generating the URL. If many parameters are required for the user session,
perhaps hide the information in a cookie rather than continually append values like:

```
cat=gummy-candy&cat=lollipops&cat=gummy-candy&...
```

### Worst practice #5: Offering further refinement (filtering) when there are zero results.

#### Worst practice:

Allowing users to select filters when zero items exist for the refinement.

![category page that lets users select filters when zero items exist](/static/search/blog/images/faceted-nav-filtering-when-zero-worst.png)

#### Best practice:

Only create links/URLs when it's a valid user-selection (items exist). With zero items, grey out
filtering options. To further improve usability, consider adding item counts next to each filter.

![categopry page that greys out filters if there aren't any items](/static/search/blog/images/faceted-nav-filtering-when-zero-best.png)

Prevent useless URLs and minimize the crawl space by only creating URLs when products exist. This
helps users to stay engaged on your site (fewer clicks on the back button when no products exist),
and helps minimize potential URLs known to crawlers. Furthermore, if a page isn't just temporarily
out-of-stock, but is unlikely to ever contain useful content, consider returning a
[`404` status code](/search/docs/crawling-indexing/http-network-errors).
With the `404` response, you can include a helpful message to users with more
navigation options or a search box to find related products.

## Best practices for new faceted navigation implementations or redesigns

New sites that are considering implementing faceted navigation have several options to optimize
the "crawl space" (the totality of URLs on your site known to Googlebot) for unique content pages,
reduce crawling of duplicative pages, and consolidate indexing signals.

- Determine which URL parameters are required for search engines to crawl every individual content
  page (for example, determine what parameters are required to create at least one click-path to
  each item). Required parameters may include `item-id`, `category-id`,
  `page`, and others.
- Determine which parameters would be valuable to searchers and their queries, and which would
  likely only cause duplication with unnecessary crawling or indexing. In the candy store
  example, I may find the URL parameter `taste` to be valuable to searchers for
  queries like "sour gummy candies" which could show the result
  `example.com/category.php?category=gummy-candies&taste=sour`. However, I may
  consider the parameter `price` to only cause duplication, such as
  `category=gummy-candies&taste=sour&price=over-10`. Other common examples:

  - **Valuable parameters to searchers**: `item-id`, `category-id`,
    `name`, `brand`, and others.
  - **Unnecessary parameters**: `session-id`, `price-range`, and so on.
- Consider implementing one of several configuration options for URLs that contain unnecessary
  parameters. Just make sure that the unnecessary URL parameters are never required in a crawler
  or user's click path to reach each individual product!

  - **Option 1**: `rel="nofollow"` internal links

    Make all unnecessary URLs links
    [`rel="nofollow"`](/search/docs/advanced/guidelines/qualify-outbound-links).
    This option minimizes the crawler's discovery of unnecessary URLs and therefore reduces
    the potentially explosive crawl space (URLs known to the crawler) that can occur with
    faceted navigation. `rel="nofollow"` doesn't prevent the unnecessary URLs from
    being crawled (only a robots.txt `disallow` prevents crawling). By allowing
    them to be crawled, however, you can consolidate indexing signals from the unnecessary
    URLs with a searcher-valuable URL by adding `rel="canonical"` from the
    unnecessary URL to a superset URL (for example
    `example.com/category.php?category=gummy-candies&taste=sour&price=5-10`
    can specify a `rel="canonical"` to the superset "sour gummy candies" view-all
    page at
    `example.com/category.php?category=gummy-candies&taste=sour&page=all`).
  - **Option 2**: Robots.txt `disallow`

    For URLs with unnecessary parameters, include a `/filtering/` directory that
    will be robots.txt disallowed. This lets all search engines crawl good content, but
    will prevent crawling of the unwanted URLs. For instance, if my valuable parameters were
    item, category, and taste, and my unnecessary parameters were session-id and price. I may
    have the URL:

    ```
    example.com/category.php?category=gummy-candies
    ```

    which could link to another URL valuable parameter such as taste:

    ```
    example.com/category.php?category=gummy-candies&taste=sour
    ```

    But for the unnecessary parameters, such as price, the URL includes a predefined
    directory, `/filtering/`:

    ```
    example.com/filtering/category.php?category=gummy-candies&price=5-10
    ```

    which is then robots.txt disallowed:

    ```
    User-agent: *
    Disallow: /filtering/
    ```
  - **Option 3**: Separate hosts

    If you're not using a CDN (sites using CDNs don't have this flexibility easily available
    in Webmaster Tools), consider placing any URLs with unnecessary parameters on a separate
    host—for example, creating main host `www.example.com` and secondary
    host, `www2.example.com`. On the secondary host (`www2`), set the
    [Crawl rate in
    Webmaster Tools](https://support.google.com/webmasters/answer/48620) to "low" while keeping the main host's crawl rate as high as possible.
    This would allow for more full crawling of the main host URLs and reduces Googlebot's
    focus on your unnecessary URLs.

    - Be sure there remains at least one click path to all items on the main host.
    - If you'd like to consolidate indexing signals, consider adding
      `rel="canonical"` from the secondary host to a superset URL on the main host
      (for example
      `www2.example.com/category.php?category=gummy-candies&taste=sour&price=5-10`
      may specify a `rel="canonical"` to the superset "sour gummy candies" view-all
      page,
      `www.example.com/category.php?category=gummy-candies&taste=sour&page=all`).
- Prevent clickable links when no products exist for the category or filter.
- Add logic to the display of URL parameters.

  - Remove unnecessary parameters rather than continuously append values. Avoid:

    ```
    example.com/product?cat=gummy-candy&cat=lollipops&cat=gummy-candy&item=swedish-fish
    ```
  - Help the searcher experience by keeping a consistent parameter order based on
    searcher-valuable parameters listed first (as the URL may be visible in search results)
    and searcher-irrelevant parameters last (for example, session ID). Avoid:

    ```
    example.com/category.php?session-id=123&tracking-id=456&category=gummy-candies&taste=sour
    ```
- Improve indexing of individual content pages with
  [`rel="canonical"`](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  to the preferred version of a page. `rel="canonical"` can be used across hostnames or
  domains.
- Improve indexing of paginated content (such as `page=1` and `page=2` of
  the category "gummy candies") by either:

  - Adding `rel="canonical"` from individual component pages in the series to the
    category's "view-all" page (for example, `page=1`, `page=2`, and
    `page=3` of "gummy candies" with `rel="canonical"` to
    `category=gummy-candies&page=all`) while making sure that it's still a good
    searcher experience (for example, the page loads quickly).
  - Using
    [pagination markup with `rel="next"` and `rel="prev"`](/search/blog/2011/09/pagination-with-relnext-and-relprev)
    to consolidate indexing properties, such as links, from the component pages/URLs to the
    series as a whole.
- Be sure that if using JavaScript to dynamically sort/filter/hide content without updating the
  URL, there still exists URLs on your site that searchers would find valuable, such as main
  category and product pages that can be crawled and indexed. For instance, avoid using only the
  home page (or one URL) for your entire site with JavaScript to dynamically change content with
  user navigation—this would unfortunately provide searchers with only one URL to reach all
  of your content. Also, check that performance isn't negatively affected with dynamic filtering,
  as this could undermine the user experience.
- Include only canonical URLs in [sitemaps](/search/docs/crawling-indexing/sitemaps/overview).

## Best practices for existing sites with faceted navigation

First, know that the best practices listed above (for example, `rel="nofollow"` for
unnecessary URLs) still apply if/when you're able to implement a larger redesign. Otherwise, with
existing faceted navigation, it's likely that a large crawl space was already discovered by search
engines. Therefore, focus on reducing further growth of unnecessary pages crawled by Googlebot and
consolidating indexing signals.

- Use parameters (when possible) with standard encoding and key-value pairs.
- Verify that values that don't change page content, such as session IDs, are implemented as
  standard key-value pairs, not directories.
- Prevent clickable anchors when no products exist for the category/filter. Don't allow clicks or
  URLs to be created when no items exist for the filter.
- Add logic to the display of URL parameters. Remove unnecessary parameters rather than
  continuously append values. For example, avoid:

  ```
  example.com/product?cat=gummy-candy&cat=lollipops&cat=gummy-candy&item=swedish-fish
  ```
- Help the searcher experience by keeping a consistent parameter order based on
  searcher-valuable parameters listed first (as the URL may be visible in search results) and
  searcher-irrelevant parameters last. For example, avoid:

  ```
  example.com/category?session-id=123&tracking-id=456&category=gummy-candies&taste=sour&
  ```

  in favor of:

  ```
  example.com/category.php?session-id=123&tracking-id=456&category=gummy-candies&taste=sour
  ```
- Configure
  [Webmaster Tools URL Parameters](https://support.google.com/webmasters/answer/1235687)
  if you have strong understanding of the URL parameter behavior on your site (make sure that
  there is still a clear click path to each individual item/article). For instance, with URL
  Parameters in Webmaster Tools, you can list the parameter name, the parameters effect on the
  page content, and how you'd like Googlebot to crawl URLs containing the parameter. The
  following table demonstrates how different settings affect parameters:

  | Parameter name | Effect on content? | What should Googlebot crawl? |
  | --- | --- | --- |
  | `trackingId` | None | One representative URL |
  | `SortOrder` | Sorts | Only URLs with value = 'LowToHigh' |
  | `SortBy` | Sorts | Only URLs with value = 'Price' |
  | `FilterByColor` | Narrows | No URLs |
  | `itemId` | Specifies | Every URL |
  | `page` | Paginates | Every URL |
- Be sure that if using JavaScript to dynamically sort, filter, and hide content without updating
  the URL, there still exists URLs on your site that searchers would find valuable, such as main
  category and product pages that can be crawled and indexed. For instance, avoid using only the
  home page (or, one URL) for your entire site with JavaScript to dynamically change content with
  user navigation—this would unfortunately provide searchers with only one URL to reach all
  of your content. Also, check that performance isn't negatively affected with dynamic filtering,
  as this could undermine the user experience.
- Improve indexing of individual content pages with
  [`rel="canonical"`](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  to the preferred version of a page. `rel="canonical"` can be used across hostnames or
  domains.
- Improve indexing of paginated content (such as `page=1` and `page=2` of
  the category "gummy candies") by either:

  - Adding `rel="canonical"` from individual component pages in the series to the
    category's "view-all" page (for example, `page=1`, `page=2`, and
    `page=3` of "gummy candies" with `rel="canonical"` to
    `category=gummy-candies&page=all`) while making sure that it's still a good
    searcher experience (for example, the page loads quickly).
  - Using [pagination markup with `rel="next"` and `rel="prev"`](/search/blog/2011/09/pagination-with-relnext-and-relprev)
    to consolidate indexing properties, such as links, from the component pages/URLs to the
    series as a whole.
- Include only canonical URLs in [sitemaps](/search/docs/crawling-indexing/sitemaps/overview).

Remember that commonly, the simpler you can keep it, the better. Questions? Please ask in our
[Webmaster discussion forum](https://support.google.com/webmasters/community).
