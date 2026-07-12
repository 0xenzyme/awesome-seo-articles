---
title: "Crawling and indexing of locale-adaptive pages"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2015-01-crawling-and-indexing-of-locale"
url: "https://developers.google.com/search/blog/2015/01/crawling-and-indexing-of-locale"
canonical: "https://developers.google.com/search/blog/2015/01/crawling-and-indexing-of-locale"
author: "Pierre Far"
published: "2015-01-28T00:00:00+00:00"
updated: "2015-01-28T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:25:56+00:00"
status_code: 200
html_hash: "e9bcf1f4dcc1bea9cf5707acc7648aa5c007564ffb98e009649212ad17d80163"
clean_word_count: 281
clean_char_count: 1905
---
# Crawling and indexing of locale-adaptive pages

Locale-adaptive pages change their content to reflect the user's language or perceived geographic
location. Since, by default, Googlebot requests pages without setting an
`Accept-Language` HTTP request header and uses IP addresses that appear to be located
in the USA, not all content variants of locale-adaptive pages may be indexed completely.

Today we're introducing new
[locale-aware crawl configurations](/search/docs/specialty/international/locale-adaptive-pages)
for Googlebot for pages that we detect may adapt the content they serve based on the request's
language and perceived location. These are:

- **Geo-distributed crawling** where Googlebot would start to use IP addresses that
  appear to be coming from outside the USA, in addition to the current IP addresses that appear to
  be from the USA that Googlebot currently uses.
- **Language-dependent crawling** where Googlebot would start to crawl with an
  `Accept-Language` HTTP header in the request.

As these new crawling configurations are enabled automatically for pages we detect to be
locale-adaptive, you may notice changes in how we crawl and show your site in Google search
results without you altering your CMS or server settings.

Note that these new configurations do not alter our recommendation to use separate URLs with
[`rel=alternate hreflang` annotations](/search/docs/specialty/international/localized-versions)
for each locale. We continue to support and recommend using separate URLs as they are still the
best way for users to interact and share your content, and also to maximize indexing and better
ranking of all variants of your content.

As always, if you have any questions or feedback, please tell us in the
[internationalization Webmaster Help Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:crawling_indexing_ranking)).
