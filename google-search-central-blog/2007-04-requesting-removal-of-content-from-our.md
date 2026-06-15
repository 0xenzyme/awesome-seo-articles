---
title: "Requesting removal of content from our index"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-04-requesting-removal-of-content-from-our"
url: "https://developers.google.com/search/blog/2007/04/requesting-removal-of-content-from-our"
canonical: "https://developers.google.com/search/blog/2007/04/requesting-removal-of-content-from-our"
author: null
published: "2007-04-17T00:00:00+00:00"
updated: "2007-04-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:48:48+00:00"
status_code: 200
html_hash: "2fb1b7ded57ddacd45317bfd60e20d61821fd39aa5341019398505487f8cd907"
clean_word_count: 1360
clean_char_count: 8491
---
# Requesting removal of content from our index

As a site owner, you control what content of your site is indexed in search engines. The easiest
way to let search engines know what content you don't want indexed is to use a
[robots.txt file or robots `meta` tag](/search/docs/crawling-indexing/control-what-you-share).
But sometimes, you want to remove content that's already been indexed. What's the best way to do
that?

As always, the answer begins: it depends on the type of content that you want to remove. Our
webmaster help center
[provides detailed information](/search/docs/crawling-indexing/remove-information)
about each situation. Once we recrawl that page, we'll remove the content from our index
automatically. But if you'd like to expedite the removal rather than wait for the next crawl,
the way to do that has just gotten easier.

For sites that you've verified ownership for in your
[Webmaster Tools](https://search.google.com/search-console)
account, you'll now see a new option under the Diagnostic tab called URL Removals. To get started,
simply click the **URL Removals** link, then **New Removal Request**. Choose the option that
matches the type of removal you'd like.

## Individual URLs

Choose the **Individual URLs** option if you'd like to remove a URL or image. In order for the
URL to be eligible for removal, one of the following must be true:

- The URL must return a status code of either
  [`404` or `410`](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
- The URL must be blocked by the site's
  [robots.txt file](/search/docs/crawling-indexing/robots/intro).
- The URL must be blocked by a
  [robots `meta` tag](/search/docs/crawling-indexing/block-indexing).

![How to remove individual URLs in Webmaster Tools](/static/search/blog/images/import/2dce2fc0f9bce331570484954f61dfec.png)

Once the URL is ready for removal, enter the URL and indicate whether it appears in our web
search results or image search results. Then click **Add**. You can add up to 100 URLs in a
single request. Once you've added all the URLs you would like removed, click
**Submit Removal Request**.

![Filing a removals request for a specific URL in Webmaster Tools](/static/search/blog/images/import/edbf4009ac68d1ae65a4229214768b67.png)

## A directory

![Filing a removal request for a directory in Webmaster Tools](/static/search/blog/images/import/4d76b4ce6b7300c316ef27ead3613312.png)

Choose this option if you'd like to remove all files and folders within a directory on your site.
For instance, if you request removal of `https://www.example.com/myfolder`,
this will remove all URLs that begin with that path, such as:

- `https://www.example.com/myfolder`
- `https://www.example.com/myfolder/page1.html`
- `https://www.example.com/myfolder/images/image.jpg`

In order for a directory to be eligible for removal, you must block it using a robots.txt file.
For instance, for the example above, `https://www.example.com/robots.txt` could include
the following:

```
User-agent: Googlebot
Disallow: /myfolder
```

## Your entire site

Choose this option only if you want to remove your entire site from the Google index. This
option will remove all subdirectories and files. Do not use this option to remove the non-preferred
version of your site's URLs from being indexed. For instance, if you want all of your URLs indexed
using the www version, don't use this tool to request removal of the non-www version. Instead,
specify the version you want indexed using the [Preferred domain tool](/search/blog/2019/06/bye-bye-preferred-domain-setting)
(and do a
[`301` redirect](https://en.wikipedia.org/wiki/URL_redirection)
to the preferred version, if possible). To use this option, you must
[block the site using a robots.txt file](/search/docs/crawling-indexing/robots/intro).

## Cached copies

Choose this option to remove cached copies of pages in our index. You have two options for making
pages eligible for cache removal.

### Using a meta `noarchive` tag and requesting expedited removal

If you don't want the page cached at all, you can add a
[meta `noarchive` tag](/search/docs/crawling-indexing/robots-meta-tag)
to the page and then request expedited cache removal using this tool. By requesting removal
using this tool, we'll remove the cached copy right away, and by adding the meta
`noarchive` tag, we will never include the cached version. (If you change your mind
later, you can remove the meta `noarchive` tag.)

### Changing the page content

![Filing a removal request for cached content in Webmaster Tools](/static/search/blog/images/import/2694f83eef63cb3160a50c705462e697.png)

If you want to remove the cached version of a page because it contained content that you've
removed and don't want indexed, you can request the cache removal here. We'll check to see that
the content on the live page is different from the cached version and if so, we'll remove the
cached version. We'll automatically make the latest cached version of the page available again
after six months (and at that point, we likely will have recrawled the page and the cached version
will reflect the latest content) or, if you see that we've recrawled the page sooner than that,
you can request that we reinclude the cached version sooner using this tool.

## Checking the status of removal requests

![View the status of removal requests in Webmaster Tools](/static/search/blog/images/import/ba15dd442066e78ba0759acfd80224c8.png)

Removal requests show as pending until they have been processed, at which point, the status
changes to either Denied or Removed. Generally, a request is denied if it doesn't meet the
eligibility criteria for removal.

## To reinclude content

![Viewing succefful removal requests in Webmaster Tools](/static/search/blog/images/import/0fa80fa883229e2e53fd2882ecc3805a.png)

If a request is successful, it appears in the Removed Content tab and you can reinclude it any
time simply by removing the robots.txt or robots `meta` tag block and clicking **Reinclude**.
Otherwise, we'll exclude the content for six months. After that six month period, if the content
is still blocked or returns a `404` or `410` status message and we've
recrawled the page, it won't be reincluded in our index. However, if the page is available to our
crawlers after this six month period, we'll once again include it in our index.

## Requesting removal of content you don't own

![Webpage removals request tool](/static/search/blog/images/import/935d77ce1ae75bb58767e6a74f66f22a.png)

But what if you want to request removal of content that's located on a site that you don't own?
It's just gotten easier to do that as well. Our new
[Webpage removal request tool](https://www.google.com/webmasters/tools/removals)
steps through the process for each type of removal request.

Since Google indexes the web and doesn't control the content on web pages, we generally can't
remove results from our index unless the webmaster has blocked or modified the content or removed
the page. If you would like content removed, you can work with the site owner to do so, and then
use this tool to expedite the removal from our search results.

If you have found search results that contain specific types of personal information, you can
request removal even if you've been unable to work with the site owner. For this type of removal,
provide your email address so we can work with you directly.

![Selecting the personal information option in the Webpage removals request tool](/static/search/blog/images/import/4f663ab1932502bcb7ff01fc51cf6d0c.png)

If you have found search results that shouldn't be returned with SafeSearch enabled, you can let
us know using this tool as well.

![Remove inappropriate content in the Webpage removals request tool](/static/search/blog/images/import/e5c2f7004153a2725fbc10834abba76c.png)

You can check on the status of pending requests, and as with the version available in Webmaster
Tools, the status will change to Removed or Denied once it's been processed. Generally, the
request is denied if it doesn't meet the eligibility criteria. For requests that involve personal
information, you won't see the status available here, but will instead receive an email with more
information about next steps.

## What about the existing URL removal tool?

If you've made previous requests with this tool, you can still log in to check on the status of
those requests. However, make any new requests with this new and improved version of the tool.
