---
title: "How to discover and suggest Google-selected canonical URLs for your pages"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2019-03-how-to-discover-suggest-google-selected"
url: "https://developers.google.com/search/blog/2019/03/how-to-discover-suggest-google-selected"
canonical: "https://developers.google.com/search/blog/2019/03/how-to-discover-suggest-google-selected"
author: "John Mueller"
published: "2019-03-26T00:00:00+00:00"
updated: "2019-03-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:33:49+00:00"
status_code: 200
html_hash: "9f1896b26a67701e1cb06a81ebc1e858df9c1c23b5c6a51ffa419ae5bf35e4cd"
clean_word_count: 283
clean_char_count: 1818
---
# How to discover and suggest Google-selected canonical URLs for your pages

Sometimes a web page can be reached by using more than one URL. In such cases, Google tries to
determine the best URL to display in search and to use in other ways. We call this the
"canonical URL." There are ways site owners can help us better determine what should be the
canonical URLs for their content.

If you suspect we've not selected the best canonical URL for your content, you can check by
entering your page's address into the
[URL Inspection tool](https://support.google.com/webmasters/answer/9012289)
within
[Search Console](https://search.google.com/search-console/about). It
will show you the
[Google-selected canonical](https://support.google.com/webmasters/answer/9012289#google-selected-canonical).
If you believe there's a better canonical that should be used, follow the steps on our
[duplicate URLs](/search/docs/crawling-indexing/consolidate-duplicate-urls) help page
on how to suggest a preferred choice for consideration.

Please be aware that if you search using the `site:` or `inurl:` commands,
you will be shown the domain you specified in those, even if these aren't the Google-selected
canonical. This happens because we're fulfilling the exact request entered. Behind-the-scenes, we
still use the Google-selected canonical, including for when people see pages without using the
`site:` or `inurl:` commands.

We've also changed URL Inspection tool so that it will display any Google-selected canonical for a
URL, not just those for properties you manage in Search Console. With this change, we're also
retiring the `info:` command. This was an alternative way of discovering canonicals. It
was relatively underused, and URL Inspection tool provides a more comprehensive solution to help
publishers with URLs.
