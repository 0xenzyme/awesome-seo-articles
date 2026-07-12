---
title: "URL removal explained, Part III: Removing content that you don't own"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-04-url-removal-explained-part-iii-removing"
url: "https://developers.google.com/search/blog/2010/04/url-removal-explained-part-iii-removing"
canonical: "https://developers.google.com/search/blog/2010/04/url-removal-explained-part-iii-removing"
author: "Jonathan Simon"
published: "2010-04-20T00:00:00+00:00"
updated: "2010-04-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:06:04+00:00"
status_code: 200
html_hash: "5e587302dcfc56b7c351af689197934e47dbee15b68176eca92712bb2f0a39ad"
clean_word_count: 1078
clean_char_count: 6805
---
# URL removal explained, Part III: Removing content that you don't own

Welcome to the third episode of our URL removals series! In episodes one and two, we talked about
[expediting the removal of content that's under your control](/search/blog/2010/03/url-removal-explained-part-i-urls)
and
[requesting expedited cache removals](/search/blog/2010/04/url-removals-explained-part-ii-removing).
Today, we're covering how to use Google's
[public URL removal tool](https://www.google.com/webmasters/tools/removals)
to request removal of content from Google's search results when the content originates on a
website not under your control.

Google offers two tools that provide a way to request expedited removal of content:

1. Verified URL removal tool: for requesting to remove content from Google's search results when
   it's published on a site of which you're a verified owner in Webmaster Tools (like your blog or
   your company's site)
2. Public URL removal tool: for requesting to remove content from Google's search results when it's
   published on a site which you can't verify ownership (like your friend's blog)

Sometimes a situation arises where the information you want to remove originates from a site that
you don't own or can't control. Since each individual webmaster controls their site and their
site's content, the best way to update or remove results from Google is for the site owner (where
the content is published) to either block crawling of the URL, modify the content source, or
remove the page altogether. If the content isn't changed, it would just reappear in our search
results the next time we crawled it. So the first step to remove content that's hosted on a site
you don't own is to
[contact the owner of the website](https://www.google.com/support/webmasters/bin/answer.py?answer=9109)
and request that they remove or block the content in question.

## Removed or blocked content

If the website owner removes a page, requests for the removed
page should return a
[`404 Not Found` response or a `410 Gone` response](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).
If they choose to block the page from search engines, then the page should either be disallowed
in the site's
[robots.txt](/search/docs/crawling-indexing/robots/intro)
file or contain a
[`noindex` `meta` tag](/search/docs/crawling-indexing/block-indexing).
Once one of these requirements is met, you can submit a removal request using the "Webmaster has
already blocked the page" option.

![google url removal tool](/static/search/blog/images/import/0ff6fcc7b17f1dd585acce821b9989ed.png)

Sometimes a website owner will claim that they've blocked or removed a page but they haven't
technically done so. If they claim a page has been blocked you can double check by looking at the
site's robots.txt file to see if the page is listed there as disallowed.

```
User-agent: *
Disallow: /blocked-page/
```

Another place to check if a page has been blocked is within the page's HTML source code itself.
You can visit the page and choose "View Page Source" from your browser. Is there a meta noindex
tag in the HTML `head` section?

```
<html>
<head>
<title>blocked page</title>
<meta name="robots" content="noindex">
</head>
...
```

If they inform you that the page has been removed, you can confirm this by using an HTTP response
testing tool like the
[Live HTTP Headers](https://addons.mozilla.org/en-US/firefox/addon/3829)
add-on for the Firefox browser. With this add-on enabled, you can request any URL in Firefox to
test that the HTTP response is actually `404 Not Found` or `410 Gone`.

## Content removed from the page

Once you've confirmed that the content you're seeking to remove is no longer present on the page,
you can request a
[cache removal](https://www.google.com/support/webmasters/bin/answer.py?answer=59819)
using the 'Content has been removed from the page' option. This type of
removal—usually called a "cache" removal—ensures that Google's search results will not
include the cached copy or version of the old page, or any
[snippets](/search/docs/appearance/snippet)
of text from the old version of the page. Only the current updated page (without the content
that's been removed) will be accessible from Google's search results. However, the current updated
page can potentially still rank for terms related to the old content as a result of inbound links
that still exist from external sites. For cache removal requests you'll be asked to enter a "term
that has been removed from the page." Be sure to enter a word that is not found on the current
live page, so that our automated process can confirm the page has changed—otherwise the
request will be denied. Cache removals are covered in more detail in
[part two of the "URL removal explained" series](/search/blog/2010/04/url-removals-explained-part-ii-removing).

![google cache removal tool](/static/search/blog/images/archived_1_removal-cache.png)

## Removing inappropriate webpages or images that appear in our SafeSearch filtered results

Google introduced the
[SafeSearch](https://www.google.com/support/websearch/bin/answer.py?answer=510)
filter with the goal of providing search results that exclude potentially offensive content. For
situations where you find content that you feel should have been filtered out by SafeSearch, you
can request that this content be excluded from SafeSearch filtered results in the future. Submit
a removal request using the 'Inappropriate content appears in our SafeSearch filtered results'
option.

![google safe search removal tool](/static/search/blog/images/import/f21311b0c4bd0d4d0151d174d1dc65c1.png)

If you encounter any issues with the public URL removal tool or have questions not addressed here,
please post them to the
[Webmaster Help Forum](https://support.google.com/webmasters/community/label?lid=5489e59697a233d7)
or consult the more
[detailed removal instructions](https://www.google.com/support/webmasters/bin/answer.py?answer=164734)
in our Help Center. If you do post to the forum, remember to use a
[URL shortening service](https://www.google.com/search?q=url+shorteners)
to share any links to content you want removed.

## Other posts of this series

- [Part I: Removing URLs and directories](/search/blog/2010/03/url-removal-explained-part-i-urls)
- [Part II: Removing and updating cached content](/search/blog/2010/04/url-removals-explained-part-ii-removing)
- [Part III: Removing content you don't own](/search/blog/2010/04/url-removal-explained-part-iii-removing)
- [Part IV: Tracking requests, what not to remove](/search/blog/2010/05/url-removal-explained-part-iv-tracking)

Finally, you might be also interested to read about
[managing what information is available about you online](/search/blog/2009/10/managing-your-reputation-through-search).
