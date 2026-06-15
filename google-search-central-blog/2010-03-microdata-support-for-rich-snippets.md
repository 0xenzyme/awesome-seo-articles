---
title: "Microdata support for Rich Snippets"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-03-microdata-support-for-rich-snippets"
url: "https://developers.google.com/search/blog/2010/03/microdata-support-for-rich-snippets"
canonical: "https://developers.google.com/search/blog/2010/03/microdata-support-for-rich-snippets"
author: "Pravir Gupta"
published: "2010-03-12T00:00:00+00:00"
updated: "2010-03-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:05:18+00:00"
status_code: 200
html_hash: "86e47fe5e25af242fa19a0cb734e9e1cc4cfddca2754bc3e793211e9fc464819"
clean_word_count: 421
clean_char_count: 2874
---
# Microdata support for Rich Snippets

HTML5 is the fifth major revision of HTML, the core language of the World Wide Web. The HTML5
specification includes a description of **microdata**, a new markup standard for specifying
structured information within web pages.

Today, we're happy to announce support for microdata for use in
[rich snippets](/search/docs/appearance/structured-data/intro-structured-data)
in addition to our existing support for microformats and RDFa. By using microdata markup in your
web pages, you can specify
[reviews](/search/docs/appearance/structured-data/review-snippet),
[people profiles](/search/docs/appearance/structured-data/intro-structured-data),
or
[events](/search/docs/appearance/structured-data/event)
information on your web pages that Google may use to improve the presentation of your pages in
Google search results.

Here is a simple HTML block showing a section of a review of
"L'Amourita Pizza"

:

```
  <div>
    <h1>Review: L'Amourita Pizza</h1>
    Written by Bob Smith
    Rated <b>4.5</b> - Excellent
  </div>
```

Here is the same HTML with microdata added to specify the restaurant being reviewed, the author
and date of the review, and the rating:

```
  <div itemscope itemtype="https://data-vocabulary.org/Review">
    <h1>Review: <span itemprop="itemreviewed">L'Amourita Pizza</span></h1>
    Written by <span itemprop="reviewer">Bob Smith</span>
    <time itemprop="dtreviewed" datetime="2010-01-15">Jan 15, 2010</time>
    Rated <b itemprop="rating">4.5</b> - Excellent
  </div>
```

Microdata has the nice property of balancing richness with simplicity. As you can see, it's easy
to add markup to your pages using a few HTML attributes like `itemscope` (to define a
new item), `itemtype` (to specify the type of item being described), and
`itemprop` (to specify a property of that item). Once you've added markup to a page,
you can test it using the
[rich snippets testing tool](https://www.google.com/webmasters/tools/richsnippets)
to make sure that Google can parse the data on your page.

As with microformats and RDFa, the vocabulary that we support—including which item types
and item properties are understood by Google—is specified in our rich snippets documentation
as well as on data-vocabulary.org. Marking up your content does not guarantee that rich
snippets will show for your site; Google will expand the use of microdata markup gradually to
ensure a great user experience.

To get started, here are some helpful links:

- [Rich snippets documentation](/search/docs/appearance/structured-data/intro-structured-data)
- [Overview of microdata](/search/docs/appearance/structured-data/intro-structured-data)
- [Official microdata specification](https://www.whatwg.org/specs/web-apps/current-work/multipage/microdata)
- [Rich snippets testing tool](https://www.google.com/webmasters/tools/richsnippets)
