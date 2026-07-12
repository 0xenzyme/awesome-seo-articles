---
title: "Reunifying duplicate content on your website"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-10-reunifying-duplicate-content-on-your"
url: "https://developers.google.com/search/blog/2009/10/reunifying-duplicate-content-on-your"
canonical: "https://developers.google.com/search/blog/2009/10/reunifying-duplicate-content-on-your"
author: "John Mueller"
published: "2009-10-06T00:00:00+00:00"
updated: "2009-10-06T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:01:39+00:00"
status_code: 200
html_hash: "db3d5f77832d7d18ddba65f48fcba2c989ca29d1226c731194780df44c6b19cf"
clean_word_count: 796
clean_char_count: 5168
---
# Reunifying duplicate content on your website

Handling duplicate content within your own website can be a big challenge. Websites grow; features
get added, changed and removed; content comes—content goes. Over time, many websites collect
systematic cruft in the form of multiple URLs that return the same contents. Having duplicate
content on your website is generally not problematic, though it can make it harder for search
engines to crawl and index the content. Also, PageRank and similar information found via incoming
links can get diffused across pages we aren't currently recognizing as duplicates, potentially
making your preferred version of the page rank lower in Google.

## Steps for dealing with duplicate content within your website

1. **Recognize duplicate content on your website.** The first and most important step is to
   recognize duplicate content on your website. A simple way to do this is to take a unique text
   snippet from a page and to search for it, limiting the results to pages from your own website
   by using a
   [`site:` query](https://www.google.com/support/websearch/bin/answer.py?answer=136861)
   in Google. Multiple results for the same content show duplication you can investigate.
2. **Determine your preferred URLs.** Before fixing duplicate content issues, you'll have to
   determine your preferred URL structure. Which URL would you prefer to use for that piece of
   content?
3. **Be consistent within your website.** Once you've chosen your preferred URLs, make sure to
   use them in all possible locations within your website (including in your
   [Sitemap file](https://www.sitemaps.org/index.html)).
4. **Apply `301` permanent redirects where necessary and possible.** If you can,
   redirect duplicate URLs to your preferred URLs using a `301` response code. This
   helps users and search engines find your preferred URLs should they visit the duplicate URLs.
   If your site is available on several domain names, pick one and use the `301`
   redirect appropriately from the others, making sure to forward to the right specific page, not
   just the root of the domain. If you support both www and non-www host names, pick one, use the
   [preferred domain setting in Webmaster Tools](https://www.google.com/support/webmasters/bin/answer.py?answer=44231),
   and redirect appropriately.
5. **Implement
    [the `rel="canonical"` link element](/search/docs/crawling-indexing/consolidate-duplicate-urls)
   on your pages where you can.** Where `301` redirects are not possible, the `rel="canonical"` link
   element can give us a better understanding of your site and of your preferred URLs. The use of
   this link element is also supported by major search engines such as
   [Ask.com](https://blog.ask.com/2009/02/ask-is-going-canonical),
   [Bing](https://blogs.msdn.com/webmaster/archive/2009/02/12/partnering-to-help-solve-duplicate-content-issues.aspx)
   and
   [Yahoo!](https://ysearchblog.com/2009/02/12/fighting-duplication-adding-more-arrows-to-your-quiver/).
6. **Use the
    [URL parameter handling tool](https://www.google.com/support/webmasters/bin/answer.py?answer=147959)
   in Google Webmaster Tools where possible.** If some or all of your website's duplicate content comes from URLs with query parameters,
   this tool can help you to notify us of important and irrelevant parameters within your URLs.
   More information about this tool can be found in our
   [announcement blog post](/search/blog/2009/10/new-parameter-handling-tool-helps-with).

## What about the robots.txt file?

One item which is missing from this list is disallowing crawling of duplicate content with your
robots.txt file. **We now recommend not blocking access to duplicate content on your website,
whether with a robots.txt file or other methods**. Instead, use the
[`rel="canonical"` link element](/search/docs/crawling-indexing/consolidate-duplicate-urls),
the
[URL parameter handling tool](https://www.google.com/support/webmasters/bin/answer.py?answer=147959),
or `301` redirects. If access to duplicate content is entirely blocked, search engines
effectively have to treat those URLs as separate, unique pages since they cannot know that they're
actually just different URLs for the same content. A better solution is to allow them to be
crawled, but clearly mark them as duplicate using one of our recommended methods. If you allow us
to crawl these URLs, Googlebot will learn rules to identify duplicates just by looking at the URL
and should largely avoid unnecessary recrawls in any case. In cases where duplicate content still
leads to us crawling too much of your website, you can also
[adjust the crawl rate setting in Webmaster Tools](https://www.google.com/support/webmasters/bin/answer.py?answer=48620).

We hope these methods will help you to manage the duplicate content on your website! Information
about duplicate content in general can also be found in our
[Help Center](/search/docs/advanced/guidelines/duplicate-content). Should you have any
questions, you can join the discussion in our
[Webmaster Help Forum](https://support.google.com/webmasters/community/thread?tid=7ffaad3ce68b0a59).
