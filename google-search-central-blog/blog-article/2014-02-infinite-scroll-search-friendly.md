---
title: "Infinite scroll search-friendly recommendations"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-02-infinite-scroll-search-friendly"
url: "https://developers.google.com/search/blog/2014/02/infinite-scroll-search-friendly"
canonical: "https://developers.google.com/search/blog/2014/02/infinite-scroll-search-friendly"
author: "John Mueller, Maile Ohye, Joachim Kupke"
published: "2014-02-13T00:00:00+00:00"
updated: "2014-02-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:23:44+00:00"
status_code: 200
html_hash: "2a782c597343883b36fe337c7f603236f2ce966aa564e269dd47077559cacede"
clean_word_count: 684
clean_char_count: 4646
---
# Infinite scroll search-friendly recommendations

Your site's news feed or pinboard might use
[infinite scroll](https://infinite-scroll.com/)—much to your
users' delight! When it comes to delighting Googlebot, however, that can be another story. With
infinite scroll, crawlers cannot always emulate manual user behavior—like scrolling or
clicking a button to load more items—so they don't always access all individual items in the
feed or gallery. If crawlers can't access your content, it's unlikely to surface in search
results.

To make sure that search engines can crawl individual items linked from an infinite scroll page,
make sure that you or your content management system produces a paginated series (component pages)
to go along with your infinite scroll.

![Infinite scroll page is made search-friendly when converted to a paginated series](/static/search/blog/images/import/67654f4699e422c0d096eaf6a52e23a8.png)

Infinite scroll page is made "search-friendly" when converted to a paginated series—each
component page has a similar `<title>` tag declared in the
`<head>` tag on the page.

You can see this type of behavior in action in the
[infinite scroll with pagination demo](https://scrollsample.appspot.com/items)
created by Webmaster Trends Analyst,
[John Mueller](https://johnmu.com/). The demo illustrates some
key search-engine friendly points:

- **Coverage**: All individual items are accessible. With traditional infinite
  scroll, individual items displayed after the initial page load aren't discoverable to crawlers.
- **No overlap**: Each item is listed only once in the paginated series (for example, no duplication of items).

## Search-friendly recommendations for infinite scroll

### 1. Before you start

1. Chunk your infinite-scroll page content into component pages that can be accessed when
   JavaScript is disabled.
2. Determine how much content to include on each page.
   1. Be sure that if a searcher came directly to this page, they could easily find the exact item
      they wanted (for example, without lots of scrolling before locating the desired content).
   2. Maintain reasonable page load time.
3. Divide content so that there's no overlap between component pages in the series (with the
   exception of buffering).

   ![the example on the left is search-friendly, the right example isn't](/static/search/blog/images/import/e4a41dfb604f0fca287f12c6ef0e7359.png)

   The example on the left is search-friendly, the right example isn't—the right example
   would cause crawling and indexing of duplicative content.

### 2. Structure URLs for infinite scroll search engine processing

1. Each component page contains a full URL. We recommend full URLs in this situation to minimize
   potential for configuration error.

   - **Good**:
     `example.com/category?name=fun-items&page=1`
   - **Good**:
     `example.com/fun-items?lastid=567`
   - **Less optimal**:
     `example.com/fun-items#1`
2. Test that each component page (the URL) works to take anyone directly to the content and is
   accessible and referenceable in a browser without the same cookie or user history.
3. Any key and value URL parameters should follow these recommendations:

   - Be sure the URL shows conceptually the same content two weeks from now. Avoid relative-time
     based URL parameters:
     `example.com/category/page.php?name=fun-items&days-ago=3`
   - Create parameters that can surface valuable content to searchers. Avoid non-searcher
     valuable parameters as the primary method to access content:
     `example.com/fun-places?radius=5&lat=40.71&long=-73.40`

### 3. Implement `replaceState` and `pushState`

Implement
[`replaceState` and `pushState`](https://developer.mozilla.org/en-US/docs/Web/Guide/API/DOM/Manipulating_the_browser_history)
on the infinite scroll page. The decision to use one or both is
up to you and your site's user behavior. That said, we recommend including `pushState`
(by itself, or in conjunction with `replaceState`) for the following cases:

- Any user action that resembles a click or actively turning a page.
- To provide users with the ability to serially backup through the most recently paginated content.

### 4. Test

1. Check that page values adjust as the user scrolls up or down.
2. Verify that pages that are out-of-bounds in the series return a `404` response (for
   example, `example.com/category?name=fun-items&page=999` should return a
   `404` response if there are only 998 pages of content).
3. Investigate potential
   [usability implications introduced by your infinite scroll implementation](https://www.nngroup.com/articles/infinite-scrolling/).
