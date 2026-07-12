---
title: "An update on site names"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2023-07-sitenames"
url: "https://developers.google.com/search/blog/2023/07/sitenames"
canonical: "https://developers.google.com/search/blog/2023/07/sitenames"
author: "Kenji Inoue"
published: "2023-07-28T00:00:00+00:00"
updated: "2023-07-28T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:42:24+00:00"
status_code: 200
html_hash: "0fdaa6b0cfbdc88e987fe2d267697425b4040c7b210ae18a94d72b17906b59cd"
clean_word_count: 441
clean_char_count: 2844
---
# An update on site names

In May, we [introduced](https://twitter.com/googlesearchc/status/1660731696247984136) support for [site names](/search/docs/appearance/site-names) for subdomains on mobile devices only, for English, French, German, and Japanese.
We now support subdomains on all devices in these languages.
In addition, we recently updated how the site names system works, to increase its ability to make selections that are representative of sites listed in search results.

![A screenshot of a Google Search result showing the site name highlighted above the URL](/static/search/blog/images/sitenames-2023/sitename-developers-google-com.png)

## Updated guidance on getting the site name you'd prefer

As a reminder, the best way to indicate a preferred site name to Google is to make use of `WebSite` structured data, as explained on our [site name documentation](/search/docs/appearance/site-names).

We've also now updated that documentation to encourage more use of the `alternateName` property.
Sometimes, a preferred site name isn't available for use.
For example, our system generally won't use the same site name for two different sites that are global in nature.
Providing an alternative name using the `alternateName` property allows our system to consider other options, if your preferred choice isn't selected.

## A workaround if your preferred or alternative names are not selected

In rare cases, our system might not select either a preferred or alternative site name.
This could happen if a name doesn't appear to be unique, concise, or commonly-recognized with a particular site.

Our documentation [now has a workaround](/search/docs/appearance/site-names#workaround) for this case.
If you provide your domain or subdomain name as a site name, that will be generally used.
Before trying this workaround, we'd encourage reviewing that preferred and secondary names are provided through `WebSite` structured data and that [other sources](/search/docs/appearance/site-names#sources) on your home page help support that structured data.

## A known issue with internal pages

We're aware that in some cases, a site name shown for a home page may not have propagated to appear for other pages on that site.
For example, `https://example.com/` might be showing a site name that's different from `https://example.com/internal-page.html`.

We're actively working to address this.
We will update the documentation when this issue is resolved.
In the meantime, if your home page is showing the site name you prefer, understand that it should also appear for your internal pages eventually.

We're also working to bring site name support to all languages globally in the future.
Should you have any questions, feel free to post in the [Search Central help community](https://support.google.com/webmasters/thread/227739087).
