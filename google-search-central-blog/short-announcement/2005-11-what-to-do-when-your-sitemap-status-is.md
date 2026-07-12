---
title: "What to do when your Sitemap status is \"Denied URLs\""
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2005-11-what-to-do-when-your-sitemap-status-is"
url: "https://developers.google.com/search/blog/2005/11/what-to-do-when-your-sitemap-status-is"
canonical: "https://developers.google.com/search/blog/2005/11/what-to-do-when-your-sitemap-status-is"
author: "Vanessa Fox"
published: "2005-11-01T00:00:00+00:00"
updated: "2005-11-01T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:44:17+00:00"
status_code: 200
html_hash: "f64a2a6b06d9d1957275d179c010628b612d0883065264811b0e674c04091ad6"
clean_word_count: 254
clean_char_count: 1467
---
# What to do when your Sitemap status is "Denied URLs"

If your Sitemap status is "Denied URLs" and the error listed is "URL not under Sitemap path",
here are some things to check.

## Make sure the URL root matches

If you submit your Sitemap using the path `https://example.com/sitemap.xml`, then the
URLs in your Sitemap should begin with `example.com`. Any URLs that begin with
`www.example.com` aren't considered to be under the Sitemap path. Along those lines,
if you Submit your Sitemap using the path `https://www.example.com/sitemap.xml`, the
URLs in that Sitemap should begin with `www.example.com`.

To fix this problem, you can either edit the URLs listed in your Sitemap file to match the
submitted path, or you can delete the Sitemap and then submit it again using the path that
matches the URLs listed in it.

## Make sure the Sitemap is at the highest-level directory

If you submit your Sitemap using the path
`https://www.example.com/sample_folder/sitemap.xml`, then all URLs in that Sitemap must
begin with that path. This means that
`https://www.example.com/sample.html` wouldn't be considered a valid URL in the
Sitemap.

If all possible, place your Sitemap at the root location of your site to avoid these types of
problems. If you can't place the Sitemap at the root, then list only URLs from the Sitemap
location and lower.

See the
[Sitemaps documentation](/search/docs/crawling-indexing/sitemaps/overview#deniedurls_error)
for more details.
