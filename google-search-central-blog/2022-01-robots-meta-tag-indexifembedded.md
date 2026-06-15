---
title: "New robots tag: indexifembedded"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2022-01-robots-meta-tag-indexifembedded"
url: "https://developers.google.com/search/blog/2022/01/robots-meta-tag-indexifembedded"
canonical: "https://developers.google.com/search/blog/2022/01/robots-meta-tag-indexifembedded"
author: "Weizi Wang, Gary Illyes"
published: "2022-01-21T00:00:00+00:00"
updated: "2022-01-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:40:04+00:00"
status_code: 200
html_hash: "a0b50865eaac4d349e917ec0b438d2393e030ba451fcef8ea207a25800f04157"
clean_word_count: 324
clean_char_count: 2242
---
# New robots tag: indexifembedded

Today, we're introducing a new robots tag,
[`indexifembedded`](/search/docs/crawling-indexing/robots-meta-tag#indexifembedded),
that brings you more control over when your content is indexed. With the
`indexifembedded` tag, you can tell Google you'd still like your content indexed when
it's embedded through
[`iframes`](https://developer.mozilla.org/docs/Web/HTML/Element/iframe)
and similar HTML tags in other pages, even when the content page has the `noindex` tag.

The `indexifembedded` tag addresses a common issue that especially affects media
publishers: while they may want their content indexed when it's embedded on third-party pages,
they don't necessarily want their media pages indexed on their own. Because they don't want the
media pages indexed, they currently use a `noindex` tag in such pages. However, the
`noindex` tag also prevents embedding the content in other pages during indexing.

The new robots tag, `indexifembedded`, works in combination with the
`noindex` tag only when the page with `noindex` is embedded into another
page through an `iframe` or similar HTML tag, like
[`object`](https://developer.mozilla.org/docs/Web/HTML/Element/object).
For example, if
`podcast.host.example/playpage?podcast=12345` has both the `noindex` and
`indexifembedded` tag, it means Google can embed the content hosted on that page in
`recipe.site.example/my-recipes.html` during indexing.

To enable your content to be indexed only when it's embedded on other pages, make sure to add
`indexifembedded` in combination with the `noindex` tag. For example:

```
<meta name="googlebot" content="noindex" />
<meta name="googlebot" content="indexifembedded" />
<!-- OR -->
<meta name="googlebot" content="noindex,indexifembedded" />
```

Alternatively, you can specify the tag in the HTTP header:

```
X-Robots-Tag: googlebot:noindex
X-Robots-Tag: googlebot:indexifembedded
...
OR
…
X-Robots-Tag: googlebot:noindex,indexifembedded
```

Presently, only Google supports the `indexifembedded` tag.

We hope you find this new tag useful. If you have questions or comments, find us on
[Twitter](https://twitter.com/googlesearchc) and in our
[Help Forums](https://support.google.com/webmasters/community).
