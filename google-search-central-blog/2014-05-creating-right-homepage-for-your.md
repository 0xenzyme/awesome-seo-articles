---
title: "Creating the Right home page for your International Users"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-05-creating-right-homepage-for-your"
url: "https://developers.google.com/search/blog/2014/05/creating-right-homepage-for-your"
canonical: "https://developers.google.com/search/blog/2014/05/creating-right-homepage-for-your"
author: "Zineb Ait Bahajji, Gary Illyes"
published: "2014-05-12T00:00:00+00:00"
updated: "2014-05-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:24:33+00:00"
status_code: 200
html_hash: "2b8f9890ea6ef96fd9bdcbeb25d8e1df90486ba9168b3d1d4d9ae2b8b2f08a3e"
clean_word_count: 814
clean_char_count: 5339
---
# Creating the Right home page for your International Users

If you are doing business in more than one country or targeting different languages, we recommend
having separate sites or sections with specific content on each URLs targeted for individual
countries or languages. For instance one page for US and english-speaking visitors, and a
different page for France and french-speaking users. While we have information on handling
[multi-regional and multilingual sites](/search/docs/specialty/international/managing-multi-regional-sites),
the home page can be a bit special. This post will help you create the right home page on your
website to serve the appropriate content to users depending on their language and location.

There are three ways to configure your home page / landing page when your users access it:

- Show everyone the same content.
- Let users choose.
- Serve content depending on users' localization and language.

Let's have a look at each in detail.

## Show users worldwide the same content

In this scenario, you decide to serve specific content for one given country and language on your
home page / generic URL (https://www.example.com). This content will be available to anyone who
accesses that URL directly in their browser or those who search for that URL specifically. As
mentioned above, all country and language versions should also be accessible on their own unique
URLs.

![banner on a website asking the user if they'd want to visit the store local to the user](/static/search/blog/images/import/97e76b518bd1570b3c3612737f0e614c.png)

## Let users choose which local version and which language they want

In this configuration, you decide to serve a country selector page on your home page / generic URL
and to let users choose which content they want to see depending on country and language. All
users who type in that URL can access the same page.

If you implement this scenario on your international site, remember to use the
[`x-default` `rel-alternate-hreflang` annotation](/search/docs/specialty/international/localized-versions)
for the country selector page, which was specifically created for these kinds of pages. The
`x-default` value helps us recognize pages that are not specific to one language or
region.

![a country selector page](/static/search/blog/images/import/08e5c2fbb96156b566c8c5ce45b9dcbc.png)

## Automatically redirect users or dynamically serve the appropriate HTML content depending on users' location and language settings

A third scenario would be to automatically serve the appropriate HTML content to your users
depending on their location and language settings. You will either do that by using server-side
`302` redirects or by dynamically serving the right HTML content.

Remember to use `x-default` `rel-alternate-hreflang` annotation on the
home page / generic page even if the latter is a redirect page that is not accessible directly for
users.

Whatever configuration you decide to go with, you should make sure all the pages—including
country and language selector pages:

- Have
  [rel-alternate-hreflang annotations](/search/docs/specialty/international/localized-versions).
- Are accessible for Googlebot's crawling and indexing: do not block the crawling or indexing of
  your localized pages.
- Always allow users to switch local version or language: you can do that using a drop down menu
  for instance.

*Reminder:* As mentioned in the beginning, remember that you must have separate URLs for each
country and language version.

## About `rel-alternate-hreflang` annotations

Remember to annotate all your pages—whatever method you choose. This will greatly help
search engines to show the right results to your users.

Country selector pages and redirecting or dynamically serving home pages should all use the
`x-default` annotation.

Finally, here are a few useful reminders about `rel-alternate-hreflang` annotations in
general:

- Your annotations must be confirmed from the other pages. If page A links to page B, page B must
  link back to page A, otherwise, your annotations may not be interpreted correctly.
- Your annotations should be self-referential. Page A should use
  `rel-alternate-hreflang` annotation linking to itself.
- You can specify the `rel-alternate-hreflang` annotations in the HTTP header, in the
  head section of the HTML, or in a sitemap file. We strongly recommend that you choose only one
  way to implement the annotations, in order to avoid inconsistent signals and errors.
- The value of the `hreflang` attribute must be in
  [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes class=)
  format for the language, and in
  [ISO 3166-1 Alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
  format for the region. Specifying only the region is not supported. If you wish to configure
  your site only for a country, use the geotargeting feature in
  [Webmaster Tools](https://support.google.com/webmasters/answer/62399).

Following these recommendations will help us better understand your localized content and serve
more relevant results to your users in our search results. As always, if you have any questions or
feedback, please tell us in the
[internationalization Webmaster Help Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:international_seo)).
