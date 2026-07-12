---
title: "Options for retailers to control how their crawled product information appears on Google"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2020-08-options-for-retailers-to-control-how"
url: "https://developers.google.com/search/blog/2020/08/options-for-retailers-to-control-how"
canonical: "https://developers.google.com/search/blog/2020/08/options-for-retailers-to-control-how"
author: "Bernhard Schindlholzer, Product Manager"
published: "2020-08-21T00:00:00+00:00"
updated: "2020-08-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:37:15+00:00"
status_code: 200
html_hash: "19a6d0180055fdb92714b53f39da5a64ad3f05a9866be2da95dcb1bf44e1ae8b"
clean_word_count: 871
clean_char_count: 5798
---
# Options for retailers to control how their crawled product information appears on Google

Earlier this year Google launched a new way for shoppers to
[find clothes, shoes and other retail products on Search](https://www.blog.google/products/search/new-way-find-clothes-shoes-and-more-search/)
in the U.S. and recently announced that
[retail listings are coming to product knowledge panels on Google Search](https://blog.google/products/shopping/bringing-free-retail-listings-google-search/).
These new types of experiences on Google Search, along with the global availability of
[rich results](/search/docs/appearance/structured-data/product) for
products, enable retailers to make information about their products visible to millions of
Google users.

The best way for retailers and brands to participate in this experience is by annotating the
product information on their websites using schema.org markup or by submitting this information
directly to
[Google Merchant Center](https://www.google.com/retail/get-started/).
Retailers can refer to our documentation to learn more about
[showing products on surfaces across Google](https://support.google.com/merchants/answer/9199328)
or
[adding schema.org markup to a website](/search/docs/appearance/structured-data/product).

While the processes above are the best way to ensure that product information will appear in
this Search experience, Google may also include content that has not been marked up using
schema.org or submitted through Merchant Center when the content has been crawled and is related
to retail. Google does this to ensure that users see a wide variety of products from a broad
group of retailers when they search for information on Google.

While we believe that this approach positively benefits the retail ecosystem, we recognize that
some retailers may prefer to control how their product information appears in this experience.
This can be done by using existing mechanisms for Google Search, as covered below.

## Controlling your preview preferences

There are a number of ways that retailers can control what data is displayed on Google. These
are consistent with changes
[announced](/search/blog/2019/09/more-controls-on-search)
last year that allow website owners and retailers specifically to provide preferences on which
information from their website can be shown as a preview on Google. This is done through a set
of robots `meta` tags and an HTML attribute.

Here are some ways you can
[implement these controls](/search/docs/crawling-indexing/robots-meta-tag)
to limit your products and product data from being displayed on Google:

### `nosnippet` robots `meta` tag

Using this `meta` tag you can specify that no snippet should be shown for this page in search
results. It completely removes the textual, image, and rich snippet for this page on Google and
removes the page from any listing experience.

![Google Search result with and without the nosnippet robots meta tag](/static/search/blog/images/import/89d64d3aa1cfd57b3f83626359f60d5a.png)

### `max-snippet:[number]` robots `meta` tag

This `meta` tag allows you to specify a maximum snippet length, in characters, of a snippet for
your page to be displayed on Google results. If the structured data (for example, product name,
description, price, availability) is greater than the maximum snippet length, the page will be
removed from any listing experience.

![Google Search result with and without the max-snippet robots meta tag](/static/search/blog/images/import/f8cb2a46d601cfc5d86f03ee30f55b62.png)

### `max-image-preview:[setting]` robots `meta` tag

This `meta` tag allows you to specify a maximum size of image preview to be shown for images on
this page, using either `none`, `standard`,
or `large`.

![Google Search result with and without the max-image-preview robots meta tag](/static/search/blog/images/import/c2196a84cb4d9246098b959d6e3c9d4b.png)

### `data-nosnippet` HTML attribute

This attribute allows you to specify a section on your webpage that should not be included in a
snippet preview on Google. When applied to relevant attributes for offers (price, availability,
ratings, image) removes the textual, image, and rich snippet for this page on Google and removes
the listing from any organic listing experiences.

![Google Search result with and without the data-nosnippet robots meta tag](/static/search/blog/images/import/92dcb3c74e54cabfe82c47f9e505c716.png)

Additional notes on these preferences:

- The preferences do not apply to information supplied via schema.org markup on the page
  itself. The schema.org markup needs to be removed first, before these opt-out mechanisms can
  become active.
- The opt-out preferences do not apply to product data submitted through Google Merchant Center,
  which offers specific mechanisms to
  [opt-out products](https://support.google.com/merchants/answer/191180) from
  appearing on surfaces across Google.

Use of mechanisms like `nosnippet` and `data-nosnippet` only affect the display of data and
eligibility for certain experiences. Display restrictions don't affect the ranking of these
pages in Search. The exclusion of some parts of product data from display may prevent the
product from being shown in rich results and other product results on Google.

We hope these options make it easier for you to maximize the value you get from Search and
achieve your business goals. These options are available to retailers worldwide and will operate
the same for results we display globally. For more information, check out our
[developer documentation on `meta` tags](/search/docs/crawling-indexing/robots-meta-tag).

Should you have any questions, you can
[reach out to us](/search/help), or drop by our
[help forums](https://support.google.com/webmasters/go/community).
