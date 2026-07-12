---
title: "URLs with HTTP errors"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2005-11-urls-with-http-errors"
url: "https://developers.google.com/search/blog/2005/11/urls-with-http-errors"
canonical: "https://developers.google.com/search/blog/2005/11/urls-with-http-errors"
author: "Vanessa Fox"
published: "2005-11-08T00:00:00+00:00"
updated: "2005-11-08T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:44:15+00:00"
status_code: 200
html_hash: "4f52402637acd2841444f1c5ce52c16653fa212879e20eb25eb860a5a908dddd"
clean_word_count: 464
clean_char_count: 2542
---
# URLs with HTTP errors

What can you do about URLs that we tried to crawl but couldn't because we received a
`404 (not found)` error? (You can
[see these](https://support.google.com/webmasters/answer/9008080#notfound)
once you've verified your site by clicking the **stats** link beside the Sitemap name on the
My Sitemaps page.)

You don't *have* to do anything about them. We'll continue to crawl and index your site and
will simply skip pages that return a `404`. But here are some things you *can*
do.

If we found the URLs from your Sitemap, the fix is simple. Just modify your Sitemap to list the
correct pages and resubmit it.

If we found the URLs by following links, the fix isn't quite as easy. In fact, in some cases,
there may be no fix. A webmaster may have liked your site and tried to link to it, but mistyped
the URL. You can look for sites that link to your pages and ask webmasters to fix any broken
links, but if that sounds like a lot of work, you can instead just focus on your own site.

## Check the links in your site

You may not be able to control inbound links from other sites, but you can control internal links.
Make sure that none of these broken links are coming from your site. You can generally check your
webserver logs to see what visitors clicked on in your site that returned 404 errors.

## If the links are outdated

It could be that a link points to a non-existent page because that page used to exist, but no
longer does. In that case, you can:

- Make sure that your site doesn't link to any outdated pages
- Check to see if any of these outdated pages are in the Google index

If the page used to exist, but no longer does, it might still be listed in the Google index. (You
can check this by doing a Google search for the URL.) If it is, you can either wait for
subsequent crawls (if we continue to get `404` errors when we try to crawl it, it will eventually
be removed), or you can
[request its removal](/search/docs/crawling-indexing/remove-information) using our
[automatic URL removal system](/search/docs/crawling-indexing/remove-information).

In order to use this system, the outdated page must return a `404` (and if the URL is
showing up on your Sitemaps Stats page, it already does). Log in and then choose the
**Remove an outdated link** option. Type in the URL,choose
**anything associated with this URL** and click **Remove outdated link**. The link will
show up in a status area as pending. The page should be removed from the index within 3-5 days
and the status will be updated.
