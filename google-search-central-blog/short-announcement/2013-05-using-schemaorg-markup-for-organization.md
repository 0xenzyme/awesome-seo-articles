---
title: "Using schema.org markup for organization logos"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2013-05-using-schemaorg-markup-for-organization"
url: "https://developers.google.com/search/blog/2013/05/using-schemaorg-markup-for-organization"
canonical: "https://developers.google.com/search/blog/2013/05/using-schemaorg-markup-for-organization"
author: "RJ Ryan"
published: "2013-05-15T00:00:00+00:00"
updated: "2013-05-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2013_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:21:54+00:00"
status_code: 200
html_hash: "6ced6ace59fd8c2dba6cfd120bc120ec24db2acf981e08df5ef77c611e0d2142"
clean_word_count: 217
clean_char_count: 1329
---
# Using schema.org markup for organization logos

Today, we're launching support for the schema.org markup for organization logos, a way to connect
your site with an iconic image. We want you to be able to specify which image we use as your logo
in Google search results.

Using schema.org
[`Organization` markup](https://schema.org/Organization),
you can indicate to our algorithms the location of your preferred logo. For example, a business
whose home page is www.example.com can add the following markup using visible on-page elements on
their home page:

```
<div itemscope itemtype="https://schema.org/Organization">
  <a itemprop="url" href="https://www.example.com/">Home</a>
  <img itemprop="logo" src="https://www.example.com/logo.png" />
</div>
```

This example indicates to Google that this image is designated as the organization's logo image
for the home page also included in the markup, and, where possible, may be used in Google search
results. Markup like this is a strong signal to our algorithms to show this image in preference
over others, for example when we show Knowledge Graph on the right hand side based on users'
queries.

As always, please ask us in the
[Webmaster Help Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:structured_data))
if you have any questions.
