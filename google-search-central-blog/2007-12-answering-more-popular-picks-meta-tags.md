---
title: "Answering more popular picks: meta tags and web search"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-12-answering-more-popular-picks-meta-tags"
url: "https://developers.google.com/search/blog/2007/12/answering-more-popular-picks-meta-tags"
canonical: "https://developers.google.com/search/blog/2007/12/answering-more-popular-picks-meta-tags"
author: null
published: "2007-12-04T00:00:00+00:00"
updated: "2007-12-04T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:50:56+00:00"
status_code: 200
html_hash: "fbfe3c2b48f9c750943303a530c6ab5571771e034d7291ef935145e13237af24"
clean_word_count: 1208
clean_char_count: 7783
---
# Answering more popular picks: meta tags and web search

In writing and maintaining accurate `meta` tags (for example, descriptive titles and robots
information), you help Google to more accurately crawl, index and return your site in search
results. Meta tags provide information to all sorts of clients, such as browsers and search
engines. Just keep in mind that each client will likely only interpret the `meta` tags that it uses,
and ignore the rest (although they might be useful for other reasons).

Here's how Google would interpret `meta` tags of this sample HTML page:

```
<!DOCTYPE ...>
<head>
<title>Traditional Swiss cheese fondue recipes<title> # Utilized by Google, accuracy is valuable to webmasters
<meta name="description" content="Cheese fondue is ..."> # Utilized by Google, can be shown in our search results
<meta name="revisit-after" content="14 days"> # Not utilized by Google or other major search engines
<META name="verify-v1" content="e8JG...Nw=" /> # Optional, for Google Webmaster Tools
<meta name="GoogleBot" content="noOdp"> #  Optional
<meta ...>
</head>
```

## `<meta name="description" content="A description of the page">`

This tag provides a short description of the page. In some situations this description is used as
a part of the snippet shown in the search results. For more information, learn how to
[Improve snippets with a meta description makeover](/search/blog/2007/09/improve-snippets-with-meta-description)
and create [good titles](/search/docs/appearance/title-link) and
[snippets](/search/docs/appearance/snippet) in Search Results. While the use of a
description `meta` tag is optional and will have no effect on your rankings, a good description can
result in a better snippet, which in turn can help to improve the quality and quantity of visitors
from our search results.

## `<title>The title of the page</title>`

While technically not a `meta` tag, this tag is often used together with the "description." The
contents of this tag are generally shown as the title in search results (and of course in the
user's browser when visiting the page or viewing bookmarks). Some additional information can be
found in our blog post
[Target visitors or search engines?](/search/blog/2006/10/target-visitors-or-search-engines),
especially under "Make good use of page titles."

## `<meta name="robots" content="..., ...">` and `<meta name="googlebot" content="..., ...">`

- [`nofollow`](/search/docs/crawling-indexing/robots-meta-tag#nofollow):
  Don't follow links from this page when looking for new pages to crawl (also see
  [Block or remove pages using `meta` tags](/search/docs/crawling-indexing/block-indexing)).
- [`nosnippet`](/search/docs/crawling-indexing/robots-meta-tag#nosnippet):
  Don't show a snippet of this page when displaying it in the search results.
- `noodp`: Don't use text from ODP (The Open Directory Project a.k.a. dmoz.org) to
  generate a title or snippet for this page (see how to create
  [good titles](/search/docs/appearance/title-link) and
  [snippets](/search/docs/appearance/snippet)).
- [`noarchive`](/search/docs/crawling-indexing/robots-meta-tag#noarchive):
  Don't display a "Cached" link for this page in the search results.
- [`unavailable_after:[date]`](/search/docs/crawling-indexing/robots-meta-tag#unavailable-after):
  remove this page from the search results after the specified date and time.

The default rule is `index, follow`—this is used if you omit this tag entirely or
if you specify `content="all"`. Additional information about the robots `meta` tag can be found in
[Using the robots `meta` tag](/search/blog/2007/03/using-robots-meta-tag). As a side
note, you can now also specify this information in the header of your pages using the
[`X-Robots-Tag` HTTP header rule](https://googleblog.blogspot.com/2007/07/robots-exclusion-protocol-now-with-even.html).
This is particularly useful if you wish to fine-tune crawling and indexing of non-HTML files like
PDFs, images or other kinds of documents.

## `<meta name="google" content="notranslate">`

When we recognize that the contents of a page are not in the language that the user is likely
to want to read, we often provide a link in the search results to an automatic translation of
your page. In general, this gives you the chance to provide your unique and compelling content to
a much larger group of users. However, there may be situations where this is not desired. By using
this `meta` tag, you can signal that you do not wish for Google to provide a link to a translation
for this page. This `meta` tag generally does not influence the ranking of the page for any
particular language. Learn more about the
[`notranslate` `meta` tag](/search/docs/crawling-indexing/robots-meta-tag#notranslate).

## `<meta name="verify-v1" content="...">`

This [Google Webmaster Tools](https://search.google.com/search-console)
-specific `meta` tag is used on the top-level page of your site to verify ownership of a site in
webmaster tools (alternatively you may upload an HTML file to do this). The content value you put
into this tag is provided to you in your Webmaster Tools account. Please note that while the
contents of this `meta` tag (including upper and lower case) must match exactly what is provided to
you, it does not matter if you change the tag from XHTML to HTML or if the format of the tag
matches the format of your page. For details, see
[Verify your site ownership](https://support.google.com/webmasters/answer/9008080#zippy=%2Chtml-tag).

## `<meta http-equiv="Content-Type" content="...; charset=...">`

This `meta` tag defines the content-type and character set of the page. When using this `meta` tag,
make sure that you surround the value of the `content` attribute with quotes; otherwise
the `charset` attribute may be interpreted incorrectly. If you decide to use this meta
tag, it goes without saying that you should make sure that your content is actually in the
specified character set.
[Google Webauthoring Statistics](https://code.google.com/webstats/2005-12/metadata.html)
has interesting numbers on the use of this `meta` tag.

## `<meta http-equiv="refresh" content="...;url=...">`

This `meta` tag sends the user to a new URL after a certain amount of time, sometimes used as a
simple form of redirection. This kind of redirect is not supported by all browsers and can be
confusing to the user. If you need to change the URL of a page as it is shown in search engine
results, we recommended that you use a server-side `301` redirect instead.
Additionally, W3C's
[Techniques and Failures for Web Content Accessibility Guidelines 2.0](https://www.w3.org/TR/WCAG20-TECHS/#F41)
lists it as being deprecated.

## (X)HTML and Capitalization

Google can read both HTML and XHTML-style `meta` tags (regardless of the code used on the page).
In addition, upper or lower case is generally not important in `meta` tags—we treat
`<TITLE>` and `<title>` equally. The `verify-v1`
`meta` tag is an exception, it's case-sensitive.

## revisit-after Sitemap lastmod and changefreq

Occasionally webmasters needlessly include `revisit-after` to encourage a search
engine's crawl schedule, however this `meta` tag is largely ignored. If you want to give search
engines information about changes in your pages, use and submit an
[XML sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap#xml). In this file
you can specify the `last-modified` date and the `change-frequency` of the
URLs on your site.

If you're interested in more examples or have questions about the `meta` tags mentioned above, jump
into our
[Google Webmaster Help Group](https://support.google.com/webmasters/community)
and join the discussion.

Posted by
[John Mueller](https://twitter.com/JohnMu),
Webmaster Trends Analyst, Zürich
