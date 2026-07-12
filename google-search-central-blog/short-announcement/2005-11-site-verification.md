---
title: "Site Verification"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2005-11-site-verification"
url: "https://developers.google.com/search/blog/2005/11/site-verification"
canonical: "https://developers.google.com/search/blog/2005/11/site-verification"
author: "Vanessa Fox"
published: "2005-11-18T00:00:00+00:00"
updated: "2005-11-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:44:08+00:00"
status_code: 200
html_hash: "d2364f5e33f91fc7361d1ed4c3b55afb20f214c810f576f60945c2aa1584581a"
clean_word_count: 216
clean_char_count: 1274
---
# Site Verification

This morning we learned of an issue with the Google Sitemaps tool that may have temporarily
enabled users to view statistics about sites they do not own. We acted quickly and fixed the
issue. To ensure the security of all sites using the Google Sitemaps tool, we will re-verify all
sites added in the last 48 hours.

When we
[first started showing statistics](/search/blog/2005/08/mobile-pages-and-new-statistics)
a couple of months ago, we put a system in place to prevent anyone other than site owners from
seeing stats for a site. We ask each site owner to place a unique file on the site and then we
check to see if that file exists. When we do that check, we first make sure that the server isn't
misconfigured to return a valid page when a request is made for a page that doesn't exist. We only
verify sites that are configured correctly. You can read more about that process in our
[documentation](https://support.google.com/webmasters/answer/9008080#verificationfileconfigerror).

Unfortunately, with our latest release, a bug prevented this process from working correctly. We
fixed this as soon as we found out about the problem. We take your privacy very seriously and are
currently investigating other approaches to further enhance security.
