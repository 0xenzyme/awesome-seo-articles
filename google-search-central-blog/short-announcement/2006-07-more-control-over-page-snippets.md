---
title: "More control over page snippets"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-07-more-control-over-page-snippets"
url: "https://developers.google.com/search/blog/2006/07/more-control-over-page-snippets"
canonical: "https://developers.google.com/search/blog/2006/07/more-control-over-page-snippets"
author: "Vanessa Fox"
published: "2006-07-13T00:00:00+00:00"
updated: "2006-07-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:45:50+00:00"
status_code: 200
html_hash: "47d918e7c1cf36f32b35abbe108d57a13780e8a5bf6c0d8d75d38c11c870ebdc"
clean_word_count: 221
clean_char_count: 1307
---
# More control over page snippets

The way we generate the descriptions (snippets) that appear under a page in the search results is
completely automated. The process uses both the content on a page as well as references to it that
appear on other sites.

One source we use to generate snippets is the
[Open Directory Project](https://www.dmoz.org/),
or ODP. Some site owners want to be to able to request not using the ODP for generating snippets,
and we're happy to let you all know we've added support for this. All you have to do is add a
`meta` tag to your pages.

To direct all search engines that support the `meta` tag not to use ODP information for the page's
description, use the following:

```
<meta name="robots" content="noodp">
```

Note that not all search engines may support this `meta` tag, so check with each for more
information.

To direct Google specifically from using this information to describe a page, use the following:

```
<meta name="googlebot" content="noodp">
```

For more information, visit the
[webmaster help center.](/search/docs/appearance/snippet)

Once you add this `meta` tag to your pages, it may take some time for changes to your snippets to
appear. Once we've recrawled your pages and refreshed our index, you should see the updated
snippet in search results.
