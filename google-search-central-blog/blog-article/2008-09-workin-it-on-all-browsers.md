---
title: "Workin' it on all browsers"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-09-workin-it-on-all-browsers"
url: "https://developers.google.com/search/blog/2008/09/workin-it-on-all-browsers"
canonical: "https://developers.google.com/search/blog/2008/09/workin-it-on-all-browsers"
author: "Maile Ohye"
published: "2008-09-05T00:00:00+00:00"
updated: "2008-09-05T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:54:29+00:00"
status_code: 200
html_hash: "507f9ada13cc69dc3cdd23edc68010bf1a564c2d66b0eaeabcd67706a18019e9"
clean_word_count: 497
clean_char_count: 3182
---
# Workin' it on all browsers

To web surfers,
[Google Chrome](https://www.google.com/chrome)
is a quick,
[exciting new browser](https://googleblog.blogspot.com/2008/09/fresh-take-on-browser.html).
As webmasters, it's a good reminder that regardless of the browser your visitors use to access
your site—Firefox, Internet Explorer, Google Chrome, Safari, etc.—browser
compatibility is often a high priority. When your site renders poorly or is difficult to use on
many browsers you risk losing your visitors' interest, and, if you're running a monetized site,
perhaps their business. Here's a quick list to make sure you're covering the basics:

## Ensure browser compatibility by focusing on accessibility

The same techniques that make your site more accessible to search engines, such as static HTML
versus fancy features like AJAX, often help your site's compatibility on various browsers and
numerous browser versions. Simpler HTML is often more easily cross-compatible than the latest
techniques.

## Consider validating your code

If your code
[passes validation](https://validator.w3.org/),
you've eliminated one potential issue in browser compatibility.
[With validated code](https://validator.w3.org/docs/why),
you won't need to rely on each browsers' error handling technique. There's a greater chance that
your code will function across different browsers, and it's easier to debug potential problems.

## Check that it's usable (not just properly rendered)

It's important that your site displays well; but equally important, make sure that users can
actually use your site's features in their browser. Rather than just looking at a snapshot of
your site, try navigating through your site on various browsers or adding items to your shopping
cart. It's possible that the clickable area of a linked image or button may change from browser
to browser. Additionally, if you use JavaScript for components like your shopping cart, it may
work in one browser but not another.

## Step 4: Straighten out the kinks

This step requires some trial and error, but there are several good places to help reduce the
"trials" as your make your site cross-browser compatible.
[Doctype](https://code.google.com/doctype/)
is an open source reference with test cases for cross-browser compatibility, as well as CSS tips
and tricks.

For example, let's say you're wondering how to find the offset for an element on your page. You
notice that your code works in Internet Explorer, but not Firefox and Safari. It turns out that
certain browsers are a bit finicky when it comes to finding the offset—thankfully contributors to
Doctype
[provide the code](https://code.google.com/p/doctype/wiki/ArticlePageOffset)
to work around the issue.

## Share your browser compatibility tips and resources!

We'd love to hear the steps you're taking to ensure your site works for the most visitors. We've
written a more
[in-depth Help Center article](/search/docs/advanced/guidelines/browser-compatibility)
on the topic which discusses such things as specifying a character encoding. If you have
additional tips, please share. And, if you have browser compatibility questions regarding search,
please ask!
