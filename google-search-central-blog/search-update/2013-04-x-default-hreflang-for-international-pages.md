---
title: "Introducing \"x-default hreflang\" for international landing pages"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2013-04-x-default-hreflang-for-international-pages"
url: "https://developers.google.com/search/blog/2013/04/x-default-hreflang-for-international-pages"
canonical: "https://developers.google.com/search/blog/2013/04/x-default-hreflang-for-international-pages"
author: "Pierre Far"
published: "2013-04-10T00:00:00+00:00"
updated: "2013-04-10T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2013_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:21:41+00:00"
status_code: 200
html_hash: "cc12c80642180b52a17fe070c1ffaf00373c26637b812e5fced9471af8cf1109"
clean_word_count: 352
clean_char_count: 2429
---
# Introducing "x-default hreflang" for international landing pages

The home pages of multinational and multilingual websites are sometimes configured to point visitors
to localized pages, either via redirects or by changing the content to reflect the user's
language. Today we'll introduce a new `rel-alternate-hreflang` annotation that you can
use to specify such home pages that is supported by both Google and
[Yandex](https://webmaster.ya.ru/replies.xml?item_no=15326).

To see this in action, let's look at an example. The website example.com has content that targets
users around the world as follows:

![Map of the world illustrating which hreflang code to use for which locale](/static/search/blog/images/import/841250378284b344c1d79f132ed1cae8.png)

- `https://example.com/en-gb`: For English-speaking users in the UK
- `https://example.com/en-us`: For English-speaking users in the USA
- `https://example.com/en-au`: For English-speaking users in Australia
- `https://example.com/`: The home page shows users a country selector and is the
  default page for users worldwide

In this case, you can annotate this cluster of pages using
[`rel-alternate-hreflang`](/search/docs/specialty/international/localized-versions)
using [sitemaps](/search/docs/crawling-indexing/sitemaps/overview) or using HTML
`link` tags like this:

```
<link rel="alternate" href="https://example.com/en-gb" hreflang="en-gb" />
<link rel="alternate" href="https://example.com/en-us" hreflang="en-us" />
<link rel="alternate" href="https://example.com/en-au" hreflang="en-au" />
<link rel="alternate" href="https://example.com/" hreflang="x-default" />
```

The new **`x-default` `hreflang` attribute value** signals to
our algorithms that this page doesn't target any specific language or locale and is the default
page when no other page is better suited. For example, it would be the page our algorithms try to
show French-speaking searchers worldwide or English-speaking searchers on google.ca.

The same annotation applies for home pages that dynamically alter their contents based on a user's
perceived geolocation or the `Accept-Language` headers. The `x-default`
`hreflang` value signals to our algorithms that such a page doesn't target a specific
language or locale.

As always, if you have any questions or feedback, please tell us in the
[Internationalization Webmaster Help Forum](https://support.google.com/webmasters/community/).
