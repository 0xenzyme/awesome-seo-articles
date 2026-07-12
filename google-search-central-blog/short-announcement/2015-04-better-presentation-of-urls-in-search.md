---
title: "Better presentation of URLs in search results"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2015-04-better-presentation-of-urls-in-search"
url: "https://developers.google.com/search/blog/2015/04/better-presentation-of-urls-in-search"
canonical: "https://developers.google.com/search/blog/2015/04/better-presentation-of-urls-in-search"
author: "Bartlomiej Niechwiej, Software Engineer, and Rob Ennals, Product Manager"
published: "2015-04-16T00:00:00+00:00"
updated: "2015-04-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:26:29+00:00"
status_code: 200
html_hash: "673a46c7b0d85d57fba52113094b5af026d5f84b01d70081a8c38b20b8749ae7"
clean_word_count: 221
clean_char_count: 1471
---
# Better presentation of URLs in search results

Well-structured URLs offer users a quick hint about the page topic and how the page fits within
the website. To help mobile searchers understand your website better when we show it in the mobile
search results, today we're updating the algorithms that display URLs in the search results to
better reflect the names of websites, using the real-world name of the site instead of the domain
name, and the URL structure of the sites in a breadcrumbs-like format.

![](/static/search/blog/images/import/9778f65099745fb53d5857e086c462b1.png)
![](/static/search/blog/images/import/6cc0f6b5955df62d049a48bd0a6d9b3c.png)

## Structured data site names and URLs

As part of this launch, we're also introducing support for schema.org structured data for websites
to signal to our algorithms:

- The website name to be used instead of the domain name
- The URL structure of the URL as breadcrumbs

For more details and code examples, please see our structured data documentation for providing
[site names](/search/docs/appearance/structured-data/search-gallery)
and
[breadcrumbs](/search/docs/appearance/structured-data/breadcrumb).

These changes are rolling out gradually and affect only mobile results. The site name change is
US-only for now and breadcrumbs are rolling out worldwide.

As always, if you have any questions or feedback, please ask in the
[Webmaster Help Forum](https://support.google.com/webmasters/go/community).
