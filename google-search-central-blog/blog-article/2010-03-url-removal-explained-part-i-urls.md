---
title: "URL removal explained, Part I: URLs and directories"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-03-url-removal-explained-part-i-urls"
url: "https://developers.google.com/search/blog/2010/03/url-removal-explained-part-i-urls"
canonical: "https://developers.google.com/search/blog/2010/03/url-removal-explained-part-i-urls"
author: "Susan Moskwa, Webmaster Trends Analyst"
published: "2010-03-30T00:00:00+00:00"
updated: "2010-03-30T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:05:24+00:00"
status_code: 200
html_hash: "17f807e78bfba3af93e0d6e5eac245c55ec212fa1c00cba9e128a0a9304e4192"
clean_word_count: 1260
clean_char_count: 7721
---
# URL removal explained, Part I: URLs and directories

There's
[a lot of content on the Internet these days](https://googleblog.blogspot.com/2008/07/we-knew-web-was-big).
At some point, something may turn up online that you would rather not have out there—anything
from an inflammatory blog post you regret publishing, to confidential data that accidentally got
exposed. In most cases, deleting or restricting access to this content will cause it to naturally
drop out of search results after a while. However, if you urgently need to remove unwanted
content that has gotten indexed by Google and you can't wait for it to naturally disappear, you
can use our URL removal tool to expedite the removal of content from our search results as long
as it meets certain [criteria](/search/docs/crawling-indexing)
(which we'll discuss below).

We've got a series of blog posts lined up for you explaining how to successfully remove various
types of content, and common mistakes to avoid. In this first post, I'm going to cover a few basic
scenarios: removing a single URL, removing an entire directory or site, and reincluding removed
content. I also strongly recommend our previous post on
[managing what information is available about you online](/search/blog/2009/10/managing-your-reputation-through-search).

## Removing a single URL

In general, in order for your removal requests to be successful, the owner of the URL(s) in
question—whether that's you, or someone else—must have indicated that it's okay to
remove that content. For an individual URL, this can be indicated in any of three ways:

- block the page from crawling via a
  [robots.txt file](/search/docs/crawling-indexing/robots/intro)
- block the page from indexing via a
  [`noindex` `meta` tag](/search/docs/crawling-indexing/block-indexing)
- indicate that the page no longer exists by returning a
  [`404` or `410` status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

Before submitting a removal request, you can check whether the URL is correctly blocked:

- **robots.txt:** You can check whether the URL is correctly disallowed using either the
  [Fetch as Googlebot](https://www.google.com/support/webmasters/bin/answer.py?answer=158587)
  or
  [Test robots.txt](https://www.google.com/support/webmasters/bin/answer.py?answer=156449)
  features in Webmaster Tools.
- **`noindex` `meta` tag:** You can use Fetch as Googlebot to make sure the `meta` tag
  appears somewhere between the `<head>` and `</head>` tags. If you
  want to check a page you can't verify in Webmaster Tools, you can open the URL in a browser, go
  to *View > Page source*, and make sure you see the
  `meta` tag between the `<head>` and `</head>` tags.
- **`404` and `410` status code:** You can use Fetch as Googlebot, or
  tools like
  [Live HTTP Headers](https://addons.mozilla.org/en-US/firefox/addon/3829)
  or [web-sniffer.net](https://web-sniffer.net/)
  to verify whether the URL is actually returning the correct code. Sometimes "deleted" pages may
  *say* "404" or "Not found" on the page, but actually return a
  `200` status code in the page header; so it's good to use a proper header-checking
  tool to double-check.

If unwanted content has been removed from a page but the page hasn't been blocked in any of the
above ways, you will *not be able to completely remove that URL* from our search results.
This is most common when you don't own the site that's hosting that content. We cover what to do
in this situation in a subsequent post in
[Part II of our removals series](/search/blog/2010/04/url-removals-explained-part-ii-removing).

If a URL meets one of the above criteria, you can remove it by going to
[the Removals Tool](https://www.google.com/webmasters/tools/removals),
entering the URL that you want to remove, and selecting the "Webmaster has already blocked the
page" option. Note that you should enter the URL where the content was hosted, *not* the URL
of the Google search where it's appearing. For example, enter
`https://www.example.com/embarrassing-stuff.html` *not*
`https://www.google.com/search?q=embarrassing+stuff`.

[Our help center article](https://www.google.com/support/webmasters/bin/answer.py?answer=63758)
has more details about making sure you're entering the proper URL. Remember that if you don't tell
us the exact URL that's troubling you, we won't be able to remove the content you had in mind.

## Removing an entire directory or site

In order for a directory or site-wide removal to be successful, the directory or site must be
*disallowed in the site's
[robots.txt file](/search/docs/crawling-indexing/robots/intro)*. For example, in order to
remove the `https://www.example.com/secret/` directory,
your robots.txt file would need to include:

```
User-agent: *
Disallow: /secret/
```

It isn't enough for the root of the directory to return a `404` status code,
because it's possible for a directory to return a `404` but still serve out files underneath it.
Using robots.txt to block a directory (or an entire site) ensures that all the URLs under that
directory (or site) are blocked as well. You can test whether a directory has been blocked
correctly using either the
[Fetch as Googlebot](https://www.google.com/support/webmasters/bin/answer.py?answer=158587)
or
[Test robots.txt](https://www.google.com/support/webmasters/bin/answer.py?answer=156449)
features in Webmaster Tools.

Only verified owners of a site can request removal of an entire site or directory in Webmaster
Tools. To request removal of a directory or site, click on the site in question, then go to
*Site configuration >
Crawler access >
Remove URL*. If you enter the root of your site as the URL you want to remove, you'll be
asked to confirm that you want to remove the entire site. If you enter a subdirectory, select the
"Remove directory" option from the drop-down menu.

## Reincluding content

You can cancel removal requests for any site you own at any time, including those submitted by
other people. In order to do so, you must be a
[verified owner of this site](https://www.google.com/support/webmasters/bin/topic.py?topic=8469)
in Webmaster Tools. Once you've verified ownership, you can go to
*Site configuration >
Crawler access >
Remove URL >
Removed URLs* (or  *> Made by others*) and click
"Cancel" next to any requests you wish to cancel.

Still have questions? Stay tuned for the rest of our series on removing content from Google's
search results. If you can't wait, much has already been written about URL removals, and
troubleshooting individual cases, in our
[Help Forum](https://support.google.com/webmasters/community/label?lid=5489e59697a233d7&hl=en).
If you still have questions after reading others' experiences, you can ask. Note that, in most
cases, it's hard to give relevant advice about a particular removal without knowing the site or
URL in question. We recommend sharing your URL by using a
[URL shortening service](https://www.google.com/search?q=url+shorteners)
so that the URL you're concerned about doesn't get indexed as part of your post; some shortening
services will even let you disable the shortcut later on, once your question has been resolved.

## Other posts of this series

- [Part II: Removing and updating cached content](/search/blog/2010/04/url-removals-explained-part-ii-removing)
- [Part III: Removing content you don't own](/search/blog/2010/04/url-removal-explained-part-iii-removing)
- [Part IV: Tracking requests, what not to remove](/search/blog/2010/05/url-removal-explained-part-iv-tracking)

Finally, you might be also interested to read about
[managing what information is available about you online](/search/blog/2009/10/managing-your-reputation-through-search).
