---
title: "Updating our technical Webmaster Guidelines"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-10-updating-our-technical-webmaster"
url: "https://developers.google.com/search/blog/2014/10/updating-our-technical-webmaster"
canonical: "https://developers.google.com/search/blog/2014/10/updating-our-technical-webmaster"
author: "Pierre Far"
published: "2014-10-27T00:00:00+00:00"
updated: "2014-10-27T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:25:42+00:00"
status_code: 200
html_hash: "eaa5cee9fa93c67502517c3b3122fc05ffffb79bb66d0c96eddf449462137a7e"
clean_word_count: 434
clean_char_count: 3023
---
# Updating our technical Webmaster Guidelines

We recently announced that our indexing system has been
[rendering web pages](/search/blog/2014/05/understanding-web-pages-better)
more like a typical modern browser, with CSS and JavaScript turned on. Today, we're updating one
of our
[technical Webmaster Guidelines](/search/docs/essentials)
in light of this announcement.

For optimal rendering and indexing, our new guideline specifies that you should allow Googlebot
access to the JavaScript, CSS, and image files that your pages use. This provides you optimal
rendering and indexing for your site. **Disallowing crawling of Javascript or CSS files in
your site's robots.txt directly harms how well our algorithms render and index your content and
can result in suboptimal rankings.**

## Updated advice for optimal indexing

Historically, Google indexing systems resembled old text-only browsers, such as Lynx, and that's
what our Webmaster Guidelines said. Now, with indexing based on page rendering, it's no longer
accurate to see our indexing systems as a text-only browser. Instead, a more accurate
approximation is a modern web browser. With that new perspective, keep the following in mind:

- Just like modern browsers, our rendering engine might not support all of the technologies a page
  uses. Make sure your web design adheres to the principles of
  [progressive enhancement](https://en.wikipedia.org/wiki/Progressive_enhancement)
  as this helps our systems (and a wider range of browsers) see usable content and basic
  functionality when certain web design features are not yet supported.
- Pages that render quickly not only help users get to your content easier, but make indexing of
  those pages more efficient too. We advise you follow the best practices for
  [page performance optimization](/web/fundamentals/performance),
  specifically:

  - [Eliminate unnecessary downloads](/web/fundamentals/performance/optimizing-content-efficiency/eliminate-downloads)
  - [Optimize the serving of your CSS and JavaScript files](/web/fundamentals/performance/optimizing-content-efficiency/optimize-encoding-and-transfer)
    by concatenating (merging) your separate CSS and JavaScript files, minifying the
    concatenated files, and configuring your web server to serve them compressed (usually gzip
    compression)
- Make sure your server can handle the additional load for serving of JavaScript and CSS files to
  Googlebot.

## Testing and troubleshooting

In conjunction with the launch of our rendering-based indexing, we also updated the
[Fetch and Render as Google](https://support.google.com/webmasters/answer/158587)
feature in Webmaster Tools so webmasters could see how our systems render the page. With it,
you'll be able to identify a number of indexing issues: improper robots.txt restrictions,
redirects that Googlebot cannot follow, and more.

And, as always, if you have any comments or questions, please ask in our
[Webmaster Help forum](https://support.google.com/webmasters/community/).
