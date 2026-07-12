---
title: "Using the robots meta tag"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2007-03-using-robots-meta-tag"
url: "https://developers.google.com/search/blog/2007/03/using-robots-meta-tag"
canonical: "https://developers.google.com/search/blog/2007/03/using-robots-meta-tag"
author: null
published: "2007-03-06T00:00:00+00:00"
updated: "2007-03-06T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:48:32+00:00"
status_code: 200
html_hash: "383914bbc5217db4713fe7d021ba8ff4e05ad009f5b1cbaa49e7f5e74906f414"
clean_word_count: 616
clean_char_count: 4017
---
# Using the robots meta tag

Recently, Danny Sullivan brought up good questions about how
[search engines handle `meta` tags](https://searchengineland.com/070228-140603.php).
Here are some answers about how we handle these tags at Google.

## Multiple content values

We recommend that you place all content values in one `meta` tag. This keeps the `meta` tags easy to
read and reduces the chance for conflicts. For instance:

```
<meta name="robots" content="noindex, nofollow" />
```

If the page contains multiple `meta` tags of the same type, we will aggregate the content values.
For instance, we will interpret

```
<meta name="robots" content="noindex" />
<meta name="robots" content="nofollow" />
```

the same way as:

```
<meta name="robots" content="noindex, nofollow" />
```

If content values conflict, we will use the most restrictive. So, if the page has these `meta` tags:

```
<meta name="robots" content="noindex" />
<meta name="robots" content="index" />
```

We will obey the `noindex` value.

## Unnecessary content values

By default, Googlebot will index a page and follow links to it. So there's no need to tag pages
with content values of `index` or `follow`.

## Directing a robots `meta` tag specifically at Googlebot

To provide instruction for all search engines, set the meta name to `robots`. To
provide instruction for only Googlebot, set the meta name to `Googlebot`. If you want
to provide different instructions for different search engines (for instance, if you want one
search engine to index a page, but not another), it's best to use a specific `meta` tag for each
search engine rather than use a generic robots `meta` tag combined with a specific one. You can find
a [list of bots](https://www.robotstxt.org/db) at robotstxt.org.

## Casing and spacing

Googlebot understands any combination of lowercase and uppercase. So each of these `meta` tags is
interpreted in exactly the same way:

```
<meta name="robots" content="noodp" />
<meta name="Robots" content="noodp" />
<meta name="Robots" content="NoOdp" />
```

If you have multiple content values, you must place a comma between them, but it doesn't matter if
you also include spaces. So the following `meta` tags are interpreted the same way:

```
<meta name="robots" content="noindex, nofollow" />
<meta name="robots" content="noindex,nofollow" />
```

## If you use both a robots.txt file and robots `meta` tags

If the robots.txt and `meta` tag instructions for a page conflict, Googlebot follows the most
restrictive. More specifically:

- If you block a page with robots.txt, Googlebot will never crawl the page and will never read any
  `meta` tags on the page.
- If you allow a page with robots.txt but block it from being indexed using a `meta` tag, Googlebot
  will access the page, read the `meta` tag, and subsequently not index it.

## Valid meta robots content values

Googlebot interprets the following robots `meta` tag values:

- `noindex`: prevents the page from being included in the index.
- `nofollow`: prevents Googlebot from following any links on the page. (Note that this
  is different from the link-level `nofollow` attribute, which prevents Googlebot from
  following an individual link.)
- `noarchive`: prevents a cached copy of this page from being available in the search
  results.
- `nosnippet`: prevents a description from appearing below the page in the search
  results, as well as prevents caching of the page.
- `noodp`: blocks the
  [Open Directory Project](https://www.dmoz.org/) description of
  the page from being used in the description that appears below the page in the search results.
- `none`: equivalent to `noindex, nofollow`.

## A word about content value `none`

As defined by
[robotstxt.org](https://www.robotstxt.org/wc/meta-user), the
following direction means `noindex, nofollow`.

```
<meta name="robots" content="none" />
```

However, some webmasters use this tag to indicate no robots restrictions and inadvertently block
all search engines from their content.
