---
title: "Changes to HowTo and FAQ rich results"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2023-08-howto-faq-changes"
url: "https://developers.google.com/search/blog/2023/08/howto-faq-changes"
canonical: "https://developers.google.com/search/blog/2023/08/howto-faq-changes"
author: "John Mueller"
published: "2023-08-08T00:00:00+00:00"
updated: "2023-08-08T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
fetched_at: "2026-06-14T13:42:27+00:00"
status_code: 200
html_hash: "61feff5682ad1d01d30690ef0a9324dba65abfb596a087f0cddecf3d02730d55"
clean_word_count: 441
clean_char_count: 2850
---
# Changes to HowTo and FAQ rich results

To provide a cleaner and more consistent search experience, we're changing how some rich results types are shown in Google's search results.
In particular, we're reducing the visibility of FAQ rich results, and limiting How-To rich results to desktop devices.
This change should finish rolling out globally within the next week.

## Overview of the changes

For site owners, these changes primarily affect the use of [FAQ](/search/docs/appearance/structured-data/faqpage) and [How-To](/search/docs/appearance/structured-data/how-to) structured data.

Going forward, [FAQ](/search/docs/appearance/structured-data/faqpage) (from `FAQPage` structured data) rich results will only be shown for well-known, authoritative government and health websites.
For all other sites, this rich result will no longer be shown regularly.
Sites may automatically be considered for this treatment depending on their eligibility.

While you can drop this structured data from your site, there's no need to proactively remove it.
Structured data that's not being used does not cause problems for Search, but also has no visible effects in Google Search.

![A search result showing a full FAQ rich result, and one without](/static/search/blog/images/faq-snippet-change.png)

[How-To](/search/docs/appearance/structured-data/how-to) (from `HowTo` structured data) rich results will only be shown for desktop users, and not for users on mobile devices.
Note that with mobile indexing, Google indexes the mobile version of a website as the basis for indexing: to have How-To rich results shown on desktop, the mobile version of your website must include the appropriate markup.

## Changes in Search Console reporting

For both of these items, you may also notice this change in the Search Console reporting for your website.
In particular, this will be visible in the metrics shown for FAQ and How-To [search appearances in the performance report](https://support.google.com/webmasters/answer/7576553#zippy=%2Csearch-appearance), and in the number of impressions reported in the appropriate [enhancement reports](https://support.google.com/webmasters/answer/7552505).
This change does not affect the number of items reported in the enhancement reports.
The search appearances, and the reports, will remain in Search Console for the time being.

This update is rolling out globally, in all languages and countries, over the course of the next week.
This should not be considered a ranking change and won't be listed in the Search status dashboard.
Note that there will be a small holdback experiment, so some users may not see these changes right away.

Should you have any questions, feel free to drop by our [Search Central help community](https://goo.gle/sc-forum), or ping us on [social media](https://twitter.com/googlesearchc).
