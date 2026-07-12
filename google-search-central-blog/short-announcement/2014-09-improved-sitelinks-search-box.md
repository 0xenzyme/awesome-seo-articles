---
title: "An improved search box within the search results"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2014-09-improved-sitelinks-search-box"
url: "https://developers.google.com/search/blog/2014/09/improved-sitelinks-search-box"
canonical: "https://developers.google.com/search/blog/2014/09/improved-sitelinks-search-box"
author: "Mariya\n  Moeva"
published: "2014-09-05T00:00:00+00:00"
updated: "2014-09-05T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:25:25+00:00"
status_code: 200
html_hash: "ac4b098647c4f8b22ecdfdcaaf35d9b8f64d7a13d028b456cd140360a528d825"
clean_word_count: 337
clean_char_count: 2139
---
# An improved search box within the search results

Today you'll see a new and improved sitelinks search box. When shown, it will make it easier for
users to reach specific content on your site, directly through your own site-search pages.

## What's this search box and when does it appear for my site?

When users search for a company by name—for example, "Megadodo Publications" or
"Dunder Mifflin"—they may actually be looking for something specific on that website. In the
past, when our algorithms recognized this, they'd display a larger set of
[sitelinks](/search/docs/appearance/sitelinks) and an additional search box
below that search result, which let users do
[`site:` searches](/search/docs/monitor-debug/search-operators/all-search-site)
over the site straight from the results, for example `site:example.com hitchhiker guides`.

This search box is now more prominent (above the sitelinks), supports
[Autocomplete](https://support.google.com/websearch/answer/106230),
and—if you use the right markup—will send the user directly to your website's own
search pages.

![Sitelinks search box in Google Search](/static/search/blog/images/import/1ecdd8e6a67cd48a02dcd2d4357ac297.png)

## How can I mark up my site?

You need to have a working site-specific search engine for your site. If you already have one, you
can let us know by marking up your home page as a
[schema.org/WebSite](https://schema.org/WebSite) entity with the
`potentialAction`
property of the
[schema.org/SearchAction](https://schema.org/SearchAction)
markup. You can use JSON-LD, microdata, or RDFa to do this; check out the
[full implementation details](/search/docs/appearance/structured-data/sitelinks-searchbox)
in our documentation.

If you implement the markup on your site, users will have the ability to jump directly from the
sitelinks search box to your site's search results page. If we don't find any markup, we'll show
them a Google search results page for the corresponding `site:` query, as we've done
until now.

As always, if you have questions, you can ask in our
[Webmaster Help forum](https://support.google.com/webmasters/go/community).
