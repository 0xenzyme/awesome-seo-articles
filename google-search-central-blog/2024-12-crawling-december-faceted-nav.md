---
title: "Crawling December: Faceted navigation"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "2024-12-crawling-december-faceted-nav"
url: "https://developers.google.com/search/blog/2024/12/crawling-december-faceted-nav"
canonical: "https://developers.google.com/search/blog/2024/12/crawling-december-faceted-nav"
author: "Gary Illyes"
published: "2024-12-17T00:00:00+00:00"
updated: "2024-12-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
fetched_at: "2026-06-14T13:44:29+00:00"
status_code: 200
html_hash: "018fc3e0c1edbc2ed7453016aac2558ec8b47c4c77444b0247cc4abd43370a5e"
clean_word_count: 494
clean_char_count: 3330
---
# Crawling December: Faceted navigation

We just published
[a new document about faceted navigation best practices](/search/docs/crawling-indexing/crawling-managing-faceted-navigation),
which was
[originally published as a blog post](/search/blog/2014/02/faceted-navigation-best-and-5-of-worst).
This is a summary of some of the important parts of the new documentation page.

Faceted navigation is a great way to help users find what they need on your site, but it can
create an SEO nightmare if not implemented carefully. Why? Because it can generate a near-infinite
number of URLs, leading to:

- **Overcrawling:** Search engines waste time crawling countless URLs that aren't
  valuable to search users.
- **Slower discovery:** This overcrawling slows down the discovery of your important,
  new content.

In fact, faceted navigation is by far the most common source of overcrawl issues site owners
report to us, and in the vast majority of the cases the issue could've been avoided by following
some best practices. But let's back up a little.

## The problem with URLs

Each filter combination in a faceted navigation generally creates a unique URL. For example:

```
https://example.com/items.shtm?products=fish&color=radioactive_green&size=tiny
```

Changing any parameter — `product`, `color`, or `size`
— creates a new URL, leading to a potential explosion of URLs. And that's the problem: a
virtually infinite number of new URLs waiting to be discovered. Let's fix it.

## Two approaches

1. **Block faceted navigation URLs:**
   - If you don't need these URLs indexed, use `robots.txt` to disallow crawling.
   - Or use URL fragments (`#`) for filters, as search engines generally ignore them.
2. **Optimize faceted navigation URLs (if you need them crawled, no matter the cost):**
   - Use the standard `&` separator for URL parameters. 💩
     is not a good parameter separator character.
   - Maintain a consistent order of filters in the URL path.
   - Return a `404` status code for filter combinations with no results.
   - Unless you have no other options (for example,
     [you have a single-page app](/search/docs/crawling-indexing/javascript/javascript-seo-basics#avoid-soft-404s)),
     avoid redirecting empty results to a generic "not found" page.

## Important considerations

- You can also use `rel="canonical"` to help consolidate signals by pointing variations
  to a main page. This one takes time to get picked up.
- `rel="nofollow"` on filter links can discourage crawling, but must be applied
  consistently. As in, every link pointing to these pages, internal and external, must have a
  `rel="nofollow"` attribute.
- Crawling faceted navigation URLs will always consume server resources and may impact the
  discovery of new content.

If you have suggestions or need clarification about our
[new document about faceted navigation best practices](/search/docs/crawling-indexing/crawling-managing-faceted-navigation),
use the feedback tool on that doc. If you are really into faceted navigation and wanna chat about
it with others, the
[Search Central community](https://goo.gle/sc-forum) is the place
to go, but you can also find us on
[LinkedIn](https://www.linkedin.com/showcase/googlesearchcentral/).

---

## Want to learn more about crawling? Check out the entire Crawling December series:
