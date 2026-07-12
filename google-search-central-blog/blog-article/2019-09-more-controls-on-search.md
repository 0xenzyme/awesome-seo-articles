---
title: "More options to help websites preview their content on Google Search"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2019-09-more-controls-on-search"
url: "https://developers.google.com/search/blog/2019/09/more-controls-on-search"
canonical: "https://developers.google.com/search/blog/2019/09/more-controls-on-search"
author: "John Mueller"
published: "2019-09-24T00:00:00+00:00"
updated: "2019-09-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:35:07+00:00"
status_code: 200
html_hash: "33a3f0dda43098a678ceef01548a15a6b2bc55dfe38eb0a74d2637bad8307bb8"
clean_word_count: 975
clean_char_count: 6235
---
# More options to help websites preview their content on Google Search

Google uses content previews, including
[text snippets](/search/docs/appearance/snippet) and other media, to help
people decide whether a result is relevant to their query. The type of preview shown depends on
many factors, including the type of content a person is looking for and the kind of device they're
viewing it on.

For instance, if you look for recipe results on Google, you may see thumbnail images and user
ratings—things that may be more helpful than text snippets when it comes to deciding what
you want to eat. Alternately, or perhaps you're looking for a concert nearby, and are able to
check out the events directly in the search results. These are made possible by publishers marking
up their pages with
[structured data](/search/docs/appearance/structured-data/search-gallery).

Google automatically generates previews in a way intended to help a user understand why the
results shown are relevant to their search and why the user would want to visit the linked pages.
However, we recognize that site owners may wish to independently adjust the extent of their
preview content in search results. To make it easier for individual websites to define how much or
which text should be available for snippeting and the extent to which other media should be
included in their previews, we're now introducing several new settings for webmasters.

## Letting Google know about your snippet and content preview preferences

Previously, it was only possible to allow a textual snippet or to not allow one. We're now
introducing a set of methods that allow more fine-grained configuration of the preview content
shown for your pages. This is done through two types of new settings: a set of robots `meta` tags
and an HTML attribute.

## Using robots `meta` tags

The robots `meta` tag is added to an HTML page's `<head>`, or specified via the
`x-robots-tag` HTTP header. The robots `meta` tags addressing the preview content for a
page are:

- `nosnippet`

  This is an existing option to specify that you don't want any textual snippet shown for this
  page.
- `max-snippet:`[number]

  New! Specify a maximum text-length, in characters, of a snippet for your page.
- `max-video-preview:`[number]

  New! Specify a maximum duration in seconds of an animated video preview.
- `max-image-preview:`[setting]

  New! Specify a maximum size of image preview to be shown for images on this page, using either
  `none`, `standard`, or `large`.

They can be combined, for example:

`<meta name="robots" content="max-snippet:50, max-image-preview:large" />`

Preview settings from these `meta` tags will become effective in mid-to-late October 2019 and may
take about a week for the global rollout to complete.

## Using the new data-nosnippet HTML attribute

A new way to help limit which part of a page is eligible to be shown as a snippet is the
`data-nosnippet` HTML attribute on `span`, `div`, and
`section` elements. With this, you can prevent that part of an HTML page from being
shown within the textual snippet on the page.

For example:

`<span data-nosnippet="data-nosnippet">Harry Houdini</span> is undoubtedly the most famous magician ever to live.`

The `data-nosnippet` HTML attribute will be start affecting presentation on Google
products later this year. Learn more in our
[developer documentation for the robots `meta` tag,
`x-robots-tag`, and `data-nosnippet`](/search/docs/crawling-indexing/robots-meta-tag).

## A note about rich results and featured snippets

Content in
[structured data](/search/docs/appearance/structured-data/intro-structured-data) is
eligible for display as
[rich results in search](/search/docs/appearance/structured-data/search-gallery). These
kinds of results do not conform to limits declared in the above meta robots settings, but rather,
can be addressed with much greater specificity by limiting or modifying the content provided in
the structured data itself. For example, if a
[recipe](/search/docs/appearance/structured-data/recipe) is included in structured data,
the contents of that structured data may be presented in a recipe carousel in the search results.
Similarly, if an event is marked up with structured data, it may be presented as such in the
search results. To limit that presentation, a publisher can limit the amount and type of content
in the structured data.

Some special features on Search depend on the availability of preview content, so limiting your
previews may prevent your content from appearing in these areas.
[Featured snippets](https://support.google.com/websearch/answer/9351707),
for example, requires a certain minimum number of characters to be displayed. This can vary by
language, which is why there is no exact `max-snippets` length we can provide to ensure
appearing in this feature. Those who do not wish to have content appear as featured snippets can
experiment with lower `max-snippet` lengths. Those who want a guaranteed way to
[opt-out of featured snippets](/search/docs/appearance/featured-snippets)
should use `nosnippet`.

## The AMP Format

The [AMP format](https://amp.dev/) comes with certain benefits,
including eligibility for more prominent presentation of thumbnail images in
[search results](/search/docs/crawling-indexing/amp/about-amp) and in the
[Google Discover feed](/search/docs/advanced/mobile/google-discover). These
characteristics have been shown to drive more traffic to publishers' articles. However, publishers
who do not want Google to use larger thumbnail images when their AMP pages are presented in search
and Discover can use the above meta robots settings to specify `max-image-preview` of
`standard` or `none`.

These new options are available to content owners worldwide and will operate the same for results
we display globally. We hope they make it easier for you to optimize the value you get from Search
and achieve your business goals. For more information, check out our
[developer documentation on `meta` tags](/search/docs/crawling-indexing/robots-meta-tag). Should you
have any questions, you can
[reach out to us](/search/news), or drop
by our
[webmaster help forums](https://support.google.com/webmasters/go/community).
