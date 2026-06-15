---
title: "New markup for multilingual content"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-12-new-markup-for-multilingual-content"
url: "https://developers.google.com/search/blog/2011/12/new-markup-for-multilingual-content"
canonical: "https://developers.google.com/search/blog/2011/12/new-markup-for-multilingual-content"
author: "Christopher Semturs"
published: "2011-12-05T00:00:00+00:00"
updated: "2011-12-05T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:16:58+00:00"
status_code: 200
html_hash: "487e340c190df2393cb7ed6351195cd8927d40d2d646dc17b3012276a99532e4"
clean_word_count: 518
clean_char_count: 3503
---
# New markup for multilingual content

Many websites serve users from around the world. There are different approaches to serving content
appropriate to your users' language and/or region. Last year, we launched support for
[explicit annotations](/search/blog/2010/09/unifying-content-under-multilingual)
for web pages rendering the same content with different language templates.

Today we're going further with our support for multilingual content with improved handling for
these two scenarios:

- Multiregional websites using substantially the same content. Example: English webpages for
  Australia, Canada and USA, differing only in price
- Multiregional websites using fully translated content, or substantially different monolingual
  content targeting different regions. Example: a product webpage in German, English and French

## Specifying language and location

We've expanded our support of the
[`rel="alternate" hreflang link` element](/search/docs/specialty/international/localized-versions)
to handle content that is translated or provided for multiple geographic regions. The
`hreflang` attribute can specify the language, optionally the country, and URLs of
equivalent content. By specifying these alternate URLs, our goal is to be able to consolidate
signals for these pages, and to serve the appropriate URL to users in search. Alternative URLs
can be on the same site or on another domain.

## Annotating pages as substantially similar content

Optionally, for pages that have substantially the same content in the same language and are
targeted at multiple countries, you may use the
[`rel="canonical"` `link` element](/search/docs/crawling-indexing/consolidate-duplicate-urls)
to specify your preferred version. We'll use that signal to focus on that version in search,
while showing the local URLs to users where appropriate. For example, you could use this if you
have the same product page in German, but want to target it separately to users searching on the
Google properties for Germany, Austria, and Switzerland.

**Update:** to simplify implementation, we no longer recommend using
`rel="canonical"`.

## Example usage

To explain how it works, let's look at some example URLs:

- https://www.example.com/ - contains the general home page of a website, in Spanish
- https://es-es.example.com/ - is the version for users in Spain, in Spanish
- https://es-mx.example.com/ - is the version for users in Mexico, in Spanish
- https://en.example.com/ - is the generic English language version

On all of these pages, we could use the following markup to specify language and optionally the
region:

```
<link rel="alternate" hreflang="es" href="https://www.example.com/" />
<link rel="alternate" hreflang="es-ES" href="https://es-es.example.com/" />
<link rel="alternate" hreflang="es-MX" href="https://es-mx.example.com/" />
<link rel="alternate" hreflang="en" href="https://en.example.com/" />
```

If you specify a regional subtag, we'll assume that you want to target that region.

Keep in mind that all of these annotations are to be used on a **per-URL basis**. You should
take care to use the specific URL, not the home page, for both of these link elements.

## More help

As always, if you need more help correctly implementing multiregional and multilingual websites,
please see our
[Help Center article](/search/docs/specialty/international/localized-versions)
about this topic, or ask in our
[Webmaster Help Forum](https://support.google.com/webmasters/community).
