---
title: "Understanding web pages better"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-05-understanding-web-pages-better"
url: "https://developers.google.com/search/blog/2014/05/understanding-web-pages-better"
canonical: "https://developers.google.com/search/blog/2014/05/understanding-web-pages-better"
author: "Michael Xu, Kazushi Nagayama"
published: "2014-05-23T00:00:00+00:00"
updated: "2014-05-23T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:24:42+00:00"
status_code: 200
html_hash: "e394962d0f5b365bc62826487779608ccf61cc572c57d128de6678ee1e35ad59"
clean_word_count: 551
clean_char_count: 3405
---
# Understanding web pages better

In [1998](https://www.google.com/about/company/history/) when our
servers were running in
[Susan Wojcicki](https://twitter.com/SusanWojcicki)'s garage, we
didn't really have to worry about JavaScript or CSS. They weren't used much, or, JavaScript was
used to make page elements... blink! A lot has changed since then. The web is full of rich,
dynamic, amazing websites that make heavy use of JavaScript. Today, we'll talk about our
capability to render richer websites—meaning we see your content more like modern Web
browsers, include the external resources, execute JavaScript and apply CSS.

Traditionally, we were only looking at the raw textual content that we'd get in the HTTP response
body and didn't really interpret what a typical browser running JavaScript would see. When pages
that have valuable content rendered by JavaScript started showing up, we weren't able to let
searchers know about it, which is a sad outcome for both searchers and webmasters.

In order to solve this problem, we decided to try to understand pages by executing JavaScript.
It's hard to do that at the scale of the current web, but we decided that it's worth it. We have
been gradually improving how we do this for some time. In the past few months, our indexing system
has been rendering a substantial number of web pages more like an average user's browser with
JavaScript turned on.

Sometimes things don't go perfectly during rendering, which may negatively impact search results
for your site. Here are a few potential issues, and—where possible,—how you can help
prevent them from occurring:

- If resources like JavaScript or CSS in separate files are blocked (say, with robots.txt) so that
  Googlebot can't retrieve them, our indexing systems won't be able to see your site like an
  average user. We recommend allowing Googlebot to retrieve JavaScript and CSS so that your
  content can be indexed better. This is especially important for mobile websites, where external
  resources like CSS and JavaScript help our algorithms understand that the pages are
  [optimized for mobile](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#crawling_requirement).
- If your web server is unable to handle the volume of crawl requests for resources, it may have a
  negative impact on our capability to render your pages. If you'd like to ensure that your pages
  can be rendered by Google, make sure your servers are able to handle crawl requests for
  resources.
- It's always a good idea to have your site degrade gracefully. This will help users enjoy your
  content even if their browser doesn't have compatible JavaScript implementations. It will also
  help visitors with JavaScript disabled or off, as well as search engines that can't execute
  JavaScript yet.
- Sometimes the JavaScript may be too complex or arcane for us to execute, in which case we can't
  render the page fully and accurately.
- Some JavaScript removes content from the page rather than adding, which prevents us from
  indexing the content.

To make things easier to debug, we're currently working on a tool for helping webmasters better
understand how Google renders their site. We look forward to making it to available for you in the
coming days in
[Webmaster Tools](https://search.google.com/search-console).

If you have any questions, please you can visit our help forum.
