---
title: "Mobile-First indexing, structured data, images, and your site"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2018-12-mobile-first-indexing-structured-data"
url: "https://developers.google.com/search/blog/2018/12/mobile-first-indexing-structured-data"
canonical: "https://developers.google.com/search/blog/2018/12/mobile-first-indexing-structured-data"
author: "John Mueller"
published: "2018-12-19T00:00:00+00:00"
updated: "2018-12-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2018_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:33:19+00:00"
status_code: 200
html_hash: "cd339a2ca1a1adadabf39a5e79bec3fad5ebabba1f6db5aea007c3514088b614"
clean_word_count: 687
clean_char_count: 4402
---
# Mobile-First indexing, structured data, images, and your site

It's been two years since we started
[working on "mobile-first indexing"—crawling the web with smartphone Googlebot](/search/blog/2016/11/mobile-first-indexing),
similar to how most users access it. We've seen websites across the world embrace the mobile web,
making fantastic websites that work on all kinds of devices. There's still a lot to do, but today,
we're happy to announce that **we now use mobile-first indexing for over half of the pages shown
in search results globally**.

## Checking for mobile-first indexing

In general, we move sites to
[mobile-first indexing](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
when our tests assure us that they're ready. When we move sites over,
[we notify the site owner](/search/blog/2018/03/rolling-out-mobile-first-indexing)
through a message in Search Console. It's possible to confirm this by checking the server logs,
where a majority of the requests should be from Googlebot Smartphone. Even easier, the
[URL inspection tool](https://support.google.com/webmasters/answer/9012289)
allows a site owner to check how a URL from the site (it's usually enough to check the home page)
was last crawled and indexed.

![A view of the URL Inspection tool in Search Console, with the 'Crawled as' field highlighted](/static/search/blog/images/import/0198059950ae7da2a69d4956e191c75c.png)

If your site uses responsive design techniques, you should be all set! For sites that aren't using
[responsive web design](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#responsive-design), we've seen
two kinds of issues come up more frequently in our evaluations:

## Missing structured data on mobile pages

[Structured data](/search/docs/appearance/structured-data/intro-structured-data) is very
helpful to better understand the content on your pages, and allows us to
[highlight your pages in fancy ways in the search results](/search/docs/appearance/structured-data/search-gallery).
If you use structured data on the desktop versions of your pages, you should have the same
structured data on the mobile versions of the pages. This is important because with mobile-first
indexing, we'll only use the mobile version of your page for indexing, and will otherwise miss the
structured data.

Testing your pages in this regard can be tricky. We suggest
[testing for structured data in general](/search/docs/guides/prototype), and then
comparing that to the mobile version of the page. For the mobile version, check the source code when you
[simulate a mobile device](/web/tools/chrome-devtools/device-mode),
or use the HTML generated with the
[Mobile-Friendly Test](https://search.google.com/test/mobile-friendly).

## Missing alt text for images on mobile pages

The value of `alt` attributes on images ("`alt text`") is a great way to
describe images to users with screen readers (which are used on mobile too!), and to search engine
crawlers. Without alt text for images, it's a lot harder for Google Images to
[understand the context of images](/search/docs/appearance/google-images) that
you use on your pages.

Check `img` tags in the source code of the mobile version for representative pages of
your website. As above, the source of the mobile version can be seen by either using the browser
to simulate a mobile device, or by using the
[Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
to check the Googlebot rendered version. Search the source code for `img` tags,
and double-check that your page is providing appropriate alt-attributes for any that you want to
have findable in [Google Images](https://images.google.com/).

For example, that might look like this:

With `alt` text (good!):

```
<img src="cute-puppies.png" alt="A photo of cute puppies on a blanket" />
```

Without `alt` text:

```
<img src="sad-puppies.png" />
```

It's fantastic to see so many great websites that work well on mobile! We're looking forward to
being able to index more and more of the web using mobile-first indexing, helping more users to
search the web in the same way that they access it: with a smartphone. We'll continue to monitor
and evaluate this change carefully. If you have any questions, please drop by our
[Webmaster forums](https://support.google.com/webmasters/go/community)
or our [public events](/search/events).
