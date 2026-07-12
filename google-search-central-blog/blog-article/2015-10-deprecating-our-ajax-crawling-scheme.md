---
title: "Deprecating our AJAX crawling scheme"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-10-deprecating-our-ajax-crawling-scheme"
url: "https://developers.google.com/search/blog/2015/10/deprecating-our-ajax-crawling-scheme"
canonical: "https://developers.google.com/search/blog/2015/10/deprecating-our-ajax-crawling-scheme"
author: "Kazushi Nagayama"
published: "2015-10-14T00:00:00+00:00"
updated: "2015-10-14T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:27:38+00:00"
status_code: 200
html_hash: "d2c0dc9d1c0c9b4716830f9e9f3e9d98cbe4a9e5d36c97da52adc9ffca4e1fbf"
clean_word_count: 470
clean_char_count: 3109
---
# Deprecating our AJAX crawling scheme

In short: We are no longer recommending the [AJAX crawling](/search/docs/ajax-crawling)
proposal we made
[back in 2009](/search/blog/2009/10/proposal-for-making-ajax-crawlable).

In 2009, we made a
[proposal to make AJAX pages crawlable](/search/blog/2009/10/proposal-for-making-ajax-crawlable).
Back then, our systems were not able to render and understand pages that use JavaScript to present
content to users. Because
"[crawlers are not able to see any content created dynamically](/search/docs/ajax-crawling/learn-more)",
we proposed a set of practices that webmasters can follow in order to ensure that their AJAX-based
applications are indexed by search engines.

Times have changed. Today, as long as you're not blocking Googlebot from crawling your JavaScript
or CSS files, we are generally able to
[render and understand your web pages like modern browsers](/search/blog/2014/05/understanding-web-pages-better).
To reflect this improvement, we recently
[updated our technical Webmaster Guidelines](/search/blog/2014/10/updating-our-technical-webmaster)
to recommend against disallowing Googlebot from crawling your site's CSS or JS files.

Since the assumptions for our 2009 proposal are no longer valid, we recommend following the
principles of
[progressive enhancement](https://en.wikipedia.org/wiki/Progressive_enhancement).
For example, you can use the
[`History API pushState()`](https://developer.mozilla.org/en-US/docs/Web/API/History_API)
to ensure accessibility for a wider range of browsers (and our systems).

## Questions and answers

**Q: My site currently follows your recommendation and supports `_escaped_fragment_`.
Would my site stop getting indexed now that you've deprecated your recommendation?**
A: No, the site would still be indexed. In general, however, we recommend you implement industry
best practices when you're making the next update for your site. Instead of the
`_escaped_fragment_` URLs, we'll generally crawl, render, and index the
`#!` URLs.

**Q: Is moving away from the AJAX crawling proposal to industry best practices considered a site
move? Do I need to implement redirects?**
A: If your current setup is working fine, you should not have to immediately change anything. If
you're building a new site or restructuring an already existing site, simply avoid introducing
`_escaped_fragment_` urls.

**Q: I use a JavaScript framework and my webserver serves a pre-rendered page. Is that still
ok?**
A: In general, websites shouldn't pre-render pages only for Google—we expect that you might
pre-render pages for performance benefits for users and that you would follow progressive
enhancement guidelines. If you pre-render pages, make sure that the content served to Googlebot
matches the user's experience, both how it looks and how it interacts. Serving Googlebot different
content than a normal user would see is considered cloaking, and would be against our Webmaster
Guidelines.

If you have any questions, you can post them here, or
[in the webmaster help forum](https://support.google.com/webmasters/go/community).
