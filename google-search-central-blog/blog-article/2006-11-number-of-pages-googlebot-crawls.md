---
title: "The number of pages Googlebot crawls"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-11-number-of-pages-googlebot-crawls"
url: "https://developers.google.com/search/blog/2006/11/number-of-pages-googlebot-crawls"
canonical: "https://developers.google.com/search/blog/2006/11/number-of-pages-googlebot-crawls"
author: null
published: "2006-11-10T00:00:00+00:00"
updated: "2006-11-10T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:47:03+00:00"
status_code: 200
html_hash: "1addd3d41cb80b0bc6266a363384f7675a2a0caa38d1ae7f66378315f5c21c61"
clean_word_count: 725
clean_char_count: 4326
---
# The number of pages Googlebot crawls

The [Googlebot activity reports](/search/blog/2006/10/googlebot-activity-reports)
in Webmaster Tools show you the number of pages of your site Googlebot has crawled over the last
90 days. We've seen some of you asking why this number might be higher than the total number of
pages on your sites.

![number of pages crawled statistics in webmaster tools](/static/search/blog/images/import/713beb501485a66a08f173982fa1dd65.png)

Googlebot crawls pages of your site based on a number of things including:

- pages it already knows about
- links from other web pages (within your site and on other sites)
- pages listed in your Sitemap file

More specifically, Googlebot doesn't access pages, it accesses URLs. And the same page can often
be accessed via several URLs. Consider the home page of a site that can be accessed from the
following four URLs:

- https://www.example.com/
- https://www.example.com/index.html
- https://example.com
- https://example.com/index.html

Although all URLs lead to the same page, all four URLs may be used in links to the page. When
Googlebot follows these links, a count of four is added to the activity report.

Many other scenarios can lead to multiple URLs for the same page. For instance, a page may have
several named anchors, such as:

- https://www.example.com/mypage.html#heading1
- https://www.example.com/mypage.html#heading2
- https://www.example.com/mypage.html#heading3

And dynamically generated pages often can be reached by multiple URLs, such as:

- https://www.example.com/furniture?type=chair&brand=123
- https://www.example.com/hotbuys?type=chair&brand=123

As you can see, when you consider that each page on your site might have multiple URLs that lead
to it, the number of URLs that Googlebot crawls can be considerably higher than the number of
total pages for your site.

Of course, you (and we) only want one version of the URL to be returned in the search results.
Not to worry—this is exactly what happens. Our algorithms selects a version to include, and
you can provide input on this selection process.

## Redirect to the preferred version of the URL

You can do this using
[`301 (permanent)` redirect](https://en.wikipedia.org/wiki/URL_redirection).
In the first example that shows four URLs that point to a site's home page, you may want to
redirect index.html to www.example.com/. And you may want to redirect example.com to
www.example.com so that any URLs that begin with one version are redirected to the other version.
Note that you can do this latter redirect with the
[Preferred Domain feature](/search/blog/2006/09/setting-preferred-domain) in webmaster
tools. (If you also use a `301` redirect, make sure that this redirect matches what you
set for the preferred domain.)

## Block the non-preferred versions of a URL with a robots.txt file

For dynamically generated pages, you may want to block the non-preferred version using
[pattern matching](/search/docs/crawling-indexing/robots/intro)
in your robots.txt file. (Note that not all search engines support pattern matching, so check
the guidelines for each search engine bot you're interested in.) For instance, in the third
example that shows two URLs that point to a page about the chairs available from brand 123, the
"hotbuys" section rotates periodically and the content is always available from a primary and
permanent location. If that case, you may want to index the first version, and block the
"hotbuys" version. To do this, add the following to your robots.txt
file:

```
User-agent: Googlebot
Disallow: /hotbuys?*
```

To ensure that this rule will actually block and allow what you intend, use the robots.txt
analysis tool in Webmaster Tools. Just add this rule to the robots.txt section on that
page, list the URLs you want to check in the "Test URLs" section and click the Check button. For
this example, you'd see a result like this:

![robots.txt tester feature in webmaster tools](/static/search/blog/images/import/2a09d3d9ea00ca0791291a132e6976bf.png)

Don't worry about links to anchors, because while Googlebot will crawl each link, our algorithms
will index the URL without the anchor.

And if you don't provide input such as that described above, our algorithms do a really good job
of picking a version to show in the search results.
