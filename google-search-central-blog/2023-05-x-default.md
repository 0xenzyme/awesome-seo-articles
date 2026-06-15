---
title: "How x-default can help you"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2023-05-x-default"
url: "https://developers.google.com/search/blog/2023/05/x-default"
canonical: "https://developers.google.com/search/blog/2023/05/x-default"
author: "Gary Illyes"
published: "2023-05-08T00:00:00+00:00"
updated: "2023-05-08T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
fetched_at: "2026-06-14T13:42:08+00:00"
status_code: 200
html_hash: "33360d53088a2a261014a7f8ef64933fc3eed94164bf6e5a6aa0aec8497686ad"
clean_word_count: 570
clean_char_count: 3464
---
# How x-default can help you

A few recent issues made us realize that the
`hreflang x-default`
value is potentially underused by sites that already use `hreflang` to help search
users find the right version of their pages. We want to remind you that it can be a powerful tool
and can do more than you (probably) think.

The
`hreflang x-default`
value is used to specify the language and region neutral URL for a piece of content when the site
doesn't support the user's language and region. It is used along with other `hreflang`
values, which specify the version of a URL for a piece of content targeted to a specific language
and region.

For example, if a page has `hreflang` annotations for English and Spanish versions of a
page along with an `x-default` value pointing to the English version, French speaking
users are sent to the English version of the page due to the `x-default` annotation.
The `x-default` page can be a language and country selector page, the page where you
redirect users when you have no content for their region, or just the version of the content that
you consider, well, default. Naturally, you might not have localized versions of all your pages,
and that's ok: it is absolutely fine to have `hreflang` annotations on just parts of
your site.

So how does `x-default` help you, the site owner? You already know how it helps us rank
the right page for the right users, but there's more!

## 1. URL discovery

While we don't talk much about it, the URLs you specify in `hreflang` annotations,
including `x-default`, may be used for URL discovery. This can be helpful for large
sites with complex structures for example, where it's hard to make sure every localized URL on
the site is well linked.

In practice this means that the `href` attributes in the following example is extracted
and may be scheduled for crawling:

```
<link rel="alternate" href="https://example.com/en-us" hreflang="en-us" />
<link rel="alternate" href="https://example.com/country-selector" hreflang="x-default" />
```

## 2. Conversions

Your goal is very likely to convert in some way the users that land on your pages.
[Ryte explains conversion](https://ryte.com/wiki/Conversion) as
"the result of the occurrence of a desired action that has been defined in advance by the company
as a goal". For instance, when a user lands on your page with an essay about
[Wuthering Heights](https://en.wikipedia.org/wiki/Wuthering_Heights),
you might count a conversion as having the user read through the majority of your essay. Of course
there are many forms of conversions; you define what your goal is after all.

However if you only published the essay in German, it's unlikely that non-german speakers would
convert on that page, so you might want to send them somewhere else where they might actually
convert in some other way. You can express this with `hreflang="x-default"` as:

```
<link rel="alternate" href="https://example.com/de/stürmische-höhen" hreflang="de" />
<link rel="alternate" href="https://example.com/lang-selector" hreflang="x-default" />
```

If you want to learn more about `hreflang`,
[check out our documentation](/search/docs/specialty/international/localized-versions),
which also goes into more detail about `x-default`. And if you want to just chat with
us about `hreflang`, you can find us in the
[Google Search Central forums](https://support.google.com/webmasters/community)
and on [Twitter](https://twitter.com/googlesearchc).
