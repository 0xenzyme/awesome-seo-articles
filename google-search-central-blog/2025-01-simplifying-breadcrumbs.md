---
title: "Simplifying the visible URL element on mobile search results"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "low"
slug: "2025-01-simplifying-breadcrumbs"
url: "https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs"
canonical: "https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs"
author: "Caitlin Dorsey, Product Manager on Google Search"
published: "2025-01-23T00:00:00+00:00"
updated: "2025-01-23T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:44:43+00:00"
status_code: 200
html_hash: "c0b9fd7a5723dd9d45e62af452806e96c34fa54e6a723806d7f8bdd171a12f31"
clean_word_count: 295
clean_char_count: 1953
---
# Simplifying the visible URL element on mobile search results

Mobile searchers will soon see a cleaner, more streamlined look for how URLs appear in search
results. Initially introduced as part of the ["site hierarchy" feature](https://googleblog.blogspot.com/2009/11/new-site-hierarchies-display-in-search.html),
we've found that the breadcrumb element isn't as useful to people who are searching on mobile
devices, as it gets cut off on smaller screens. Starting today, we're rolling out a change to no
longer show breadcrumbs on mobile search results in all languages and regions where Google Search
is available (they continue to appear on desktop search results).

Here's how it'll look. On desktop, the [visible URL](/search/docs/appearance/visual-elements-gallery#visible-url)
continues to have two parts: the domain and breadcrumb.

![how the visible URL element looks on desktop search results](/static/search/blog/images/breadcrumb-on-desktop.png)

On mobile, the visible URL will be simplified to the domain only:

![how the visible URL element looks on mobile search results](/static/search/blog/images/breadcrumb-on-mobile.png)

If you're using [breadcrumb markup](/search/docs/appearance/structured-data/breadcrumb),
there's nothing you need to do, as we continue to support breadcrumb markup for use in desktop
search results. The [breadcrumb rich result report](https://support.google.com/webmasters/answer/7552505)
in Search Console continues on, and you can still implement and test breadcrumb markup in the
[Rich Results Test](https://support.google.com/webmasters/answer/7445569).

We hope this change makes it easier for people to find what they're looking for when they're
searching on mobile. If you have any feedback, questions, or comments, you can find us on
[LinkedIn](https://www.linkedin.com/showcase/googlesearchcentral/)
or post in the [Google Search Central Community](https://support.google.com/webmasters/community).
