---
title: "Improving URL removals on third-party sites"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2013-12-improving-url-removals-on-third-party"
url: "https://developers.google.com/search/blog/2013/12/improving-url-removals-on-third-party"
canonical: "https://developers.google.com/search/blog/2013/12/improving-url-removals-on-third-party"
author: "John Mueller"
published: "2013-12-18T00:00:00+00:00"
updated: "2013-12-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2013_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:23:11+00:00"
status_code: 200
html_hash: "406ecb7bb0230150e5f04ce8772486291f569c9d6a5a164fc873f9b578e076e7"
clean_word_count: 682
clean_char_count: 4210
---
# Improving URL removals on third-party sites

Content on the Internet changes or disappears, and occasionally it's helpful to have search
results for it updated quickly. Today we launched our improved public URL removal tool to make it
easier to request updates based on changes on other people's websites. You can find it at
[improved public URL removal tool](https://www.google.com/webmasters/tools/removals)

![The improved public URL removal tool](/static/search/blog/images/import/dcf9553ab437cabfdbef53a8c103eae6.png)

This tool is useful for removals on other peoples' websites. You could use this tool if a page has
been removed completely, or if it was just changed and you need to have the snippet and cached
page removed. If you're the webmaster of the site, then using the
[Webmaster Tools URL removal feature](https://support.google.com/webmasters/answer/1663416)
is faster and easier.

## How to request a page be removed from search results

If the page itself was removed completely, you can request that it's removed from Google's search
results. For this, it's important that the page returns the proper
[HTTP result code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
(`403`, `404`, or `410`), has a
[`noindex` robots `meta` tag](/search/docs/crawling-indexing/block-indexing),
or is
[blocked by the robots.txt](/search/docs/crawling-indexing/robots/intro)
(blocking via robots.txt may not prevent indexing of the URL permanently). You can check the HTTP
result code with a
[HTTP header checker](https://www.google.com/search?q=http+header+checker).
While we attempt to recognize
[`soft 404`](/search/docs/crawling-indexing/troubleshoot-crawling-errors#soft-404-errors)
errors, having the website use a clear response code is always preferred. Here's how to submit a
page for removal:

1. Enter the URL of the page. As before, this needs to be the exact URL as indexed in our search
   results.
   [Here's how to find the URL](https://support.google.com/webmasters/answer/63758).
2. The analysis tool will confirm that the page is gone. Confirm the request to complete the
   submission.
3. There's no step three!

## How to request a page's cache and snippet be removed from search results

If the page wasn't removed, you can also use this tool to let us know that a text on a page (such
as a name) has been removed or changed. It'll remove the snippet and cached page in Google's
search results until our systems have been able to reprocess the page completely (it won't affect
title or ranking). In addition to the page's URL, you'll need at least one word that used to be on
the page but is now removed. You can learn more about
[cache removals in our Help Center](/search/docs/crawling-indexing/remove-information).

1. Enter the URL of the page which has changed. This needs to be the exact URL as indexed in our
   search results.
   [Here's how to find the URL](https://support.google.com/webmasters/answer/63758).
2. Confirm that the page has been updated or removed, and confirm that the cache and snippet are
   outdated (do not match the current content).
3. Now, enter a word that no longer appears on the live page, but which is still visible in the
   cache or snippet. See our
   [previous blog post on removals](/search/blog/2010/04/url-removals-explained-part-ii-removing)
   for more details.

You can find out more about URL removals in our
[Help Center](https://support.google.com/webmasters/answer/9689846), as well as in our
earlier blog posts on
[removing URLs and directories](/search/blog/2010/03/url-removal-explained-part-i-urls),
[removing and updating cached content](/search/blog/2010/04/url-removals-explained-part-ii-removing),
[removing content you don't own](/search/blog/2010/04/url-removal-explained-part-iii-removing), and
[tracking requests and what not to remove](/search/blog/2010/05/url-removal-explained-part-iv-tracking).

We hope these changes make it easier for you to submit removal requests! We welcome your feedback
in our
[removals help forum category](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:search_console)),
where other users may also be able to help with more complicated removal issues.
