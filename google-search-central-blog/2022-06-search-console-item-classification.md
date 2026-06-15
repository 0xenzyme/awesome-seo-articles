---
title: "Simplifying Search Console reports with an updated item classification"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2022-06-search-console-item-classification"
url: "https://developers.google.com/search/blog/2022/06/search-console-item-classification"
canonical: "https://developers.google.com/search/blog/2022/06/search-console-item-classification"
author: "Moshe Samet"
published: "2022-06-15T00:00:00+00:00"
updated: "2022-06-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:40:40+00:00"
status_code: 200
html_hash: "fa1c7a27046426557e734d7cf959f19d25d9b906ccaceb854f01739d0eced93a"
clean_word_count: 397
clean_char_count: 2430
---
# Simplifying Search Console reports with an updated item classification

We are simplifying the way we classify pages, items, and issues in Search Console reports. We hope this will help you focus on
critical issues that affect your visibility in Search, and will help you better prioritize your work. We will roll out this change
to all properties gradually over the next few months, so you might not see any changes for now.

Users have told us that they are confused by the "warning" status when it's applied to a URL or item: does a warning mean that the page
or item can or can't appear on Google?

In response, we are grouping the top-level item (a rich result for the rich result reports, a page or URL for the other reports)
into two groups: pages or items with critical issues are labeled something like invalid; pages or items without critical issues
are labeled something like valid. We think this new grouping will make it easier to see quickly which issues affect your site's
appearance on Google, in order to help you prioritize your fixes. Read more about how this change will affect each of the reports
in [the Help Center](https://support.google.com/webmasters/answer/11510493).

To reiterate, this is only a reporting change in Search Console; there are no changes in how Google Search crawls, indexes, or
serves your pages.

![Updated Search Console reports item classification](/static/search/blog/images/search-console-item-classification.png "Updated Search Console reports item classification")

The changes discussed in this post will also be reflected in the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) when inspecting a particular URL inside Search Console.

However, they'll only be updated in the  [URL Inspection API](/search/blog/2022/01/url-inspection-api) when we complete
the rollout in a few months. This means that if your property shows the updated item classification in Search Console, you might see
differences when comparing results from the product interface and the API. Note that after the rollout is complete, there will be no
new values in the API. We'll update this blog post when the API has been updated.

If you have any questions or concerns, please reach out to us via the [Google Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)) or on [Twitter](https://twitter.com/googlesearchc).
