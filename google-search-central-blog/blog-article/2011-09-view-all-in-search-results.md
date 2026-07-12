---
title: "View-all in search results"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-09-view-all-in-search-results"
url: "https://developers.google.com/search/blog/2011/09/view-all-in-search-results"
canonical: "https://developers.google.com/search/blog/2011/09/view-all-in-search-results"
author: "Written by Benjia Li and Joachim Kupke, Software Engineers, Indexing Team"
published: "2011-09-15T00:00:00+00:00"
updated: "2011-09-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:15:17+00:00"
status_code: 200
html_hash: "8eee8e5ffa305a6bce17a09d8ea58bd8d3b45ca992110a0ba27b3a75ef857946"
clean_word_count: 946
clean_char_count: 6063
---
# View-all in search results

User testing has taught us that searchers much prefer the view-all, single-page version of content
over a component page containing only a portion of the same information with arbitrary page breaks
(which cause the user to click "next" and load another URL).

![Example of preferred search experiences for paginated content](/static/search/blog/images/import/74163423a458340b5a8d647542054fed.jpg)

Searchers often prefer the view-all vs. paginated content with arbitrary page breaks and worse
latency.

Therefore, to improve the user experience, when we detect that a content series (for example,
`page-1.html`, `page-2.html`, etc.) also contains a single-page version
(for example, `page-all.html`), we're now making a larger effort to return the single-page
version in search results. If your site has a view-all option, there's nothing you need to do;
we'll work to do it on your behalf. Also, indexing properties, like links, will be consolidated
from the component pages in the series to the view-all page.

## High latency can make the view-all less preferred

Interestingly, the cases when users didn't prefer the view-all page were correlated with high
latency (for example, when the view-all page took a while to load, say, because it contained many
images). This makes sense because we know users are
[less satisfied with slow results](https://googleresearch.blogspot.com/2009/06/speed-matters.html).
So while a view-all page is commonly desired, as a webmaster it's important to balance this
preference with the page's load time and overall user experience.

## Best practices for a series of content

1. **If your site includes view-all pages:** We aim to detect the view-all version of your
   content and, if available, its associated component pages. There's nothing more you need to
   do! However, if you'd like to make it more explicit to us, you can include
   `rel="canonical"` from your component pages to your view-all to increase the
   likelihood that we detect your series of pages appropriately.

   ![Implementation diagram for rel-canonical for content series](/static/search/blog/images/import/4db1f72dc1cc43cee91b7016b0e30647.jpg)

   `rel="canonical"` can specify the superset of content (that is, the view-all
   page, in this case `page-all.html`) from the same information in a series of
   URLs.

   *Why does this work?* In the diagram, `page-2.html` of a series may specify
   the canonical target as `page-all.html` because `page-all.html` is a
   superset of `page-2.html`'s content. When a user searches for a query term and
   `page-all.html` is selected in search results, even if the query most related to
   `page-2.html`, we know the user will still see `page-2.html`'s relevant
   information within `page-all.html`.

   On the other hand, `page-2.html` shouldn't designate `page-1.html` as
   the canonical because `page-2.html`'s content isn't included on
   `page-1.html`. It's possible that a user's search query is relevant to content on
   `page-2.html`, but if `page-2.html`'s canonical is set to
   `page-1.html`, the user could then select `page-1.html` in search
   results and find herself in a position where she has to further navigate to a different page
   to arrive at the desired information. That's a poor experience for the user, a suboptimal
   result from us, and it could also bring poorly targeted traffic to your site.

   However, if you strongly desire your view-all page not to appear in search results:

   1. Make sure the component pages in the series don't include `rel="canonical"` to
      the view-all page, and
   2. Mark the view-all page as
      [`noindex`](/search/docs/crawling-indexing/block-indexing) using any
      of the standard methods.
2. **If you'd like to surface individual, component pages (or there's no view-all available)**:
   It may be the case that one or both of the situations below apply to your site:

   - The view-all page is undesirable as a search result (for example, load time too high or too
     difficult for users to navigate).
   - Your users prefer the multi-page experience and to be directed to a component page in search
     results, rather than the view-all page.

   If so, you can use standard HTML
   [`rel="next"` and `rel="prev"` elements](/search/blog/2011/09/pagination-with-relnext-and-relprev)
   to specify a relationship between the component pages in your series of content. If done
   correctly, Google will generally strive to:

   - Consolidate indexing properties, such as links, between the component pages/URLs.
   - Send users to the most relevant page/URL from the component pages. Typically, the most
     relevant page is the first page of your content, but our algorithms may point users to one
     of the component pages in the series.

It's not uncommon for webmasters to incorrectly use `rel="canonical"` from component
pages to the first page of their series (for example, `page-2.html` with
`rel="canonical"` to `page-1.html`). We recommend against this
implementation because the component pages don't actually contain duplicate content. Using
`rel="next"` and `rel="prev"` is far more appropriate.

## Summary

Because users generally prefer the view-all option in search results, we're making more of an
effort to properly detect and serve this version to searchers. If you have a series of content,
there's nothing more you need to do. If you'd like to hint more to Google how best to serve users
your information:

1. To better optimize your view-all page, you can use `rel="canonical"` from component
   pages to the single-page version; otherwise,
2. If a view-all page doesn't provide a good user experience for your site, you can use the
   [`rel="next"` and `rel="prev"`](/search/blog/2011/09/pagination-with-relnext-and-relprev)
   attributes as a strong hint for Google to identify the series of pages and still surface a
   component page in results.

As always, you can ask questions in our
[Webmaster Help Forum](https://support.google.com/webmasters/community/).
