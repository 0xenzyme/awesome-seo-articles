---
title: "Adding structured data support for Product Variants"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2024-02-product-variants"
url: "https://developers.google.com/search/blog/2024/02/product-variants"
canonical: "https://developers.google.com/search/blog/2024/02/product-variants"
author: "Irina Tuduce, Ryan Levering"
published: "2024-02-20T00:00:00+00:00"
updated: "2024-02-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:43:27+00:00"
status_code: 200
html_hash: "6a1bed951a439d947194320c306d39c9fe04c800bdbafef61d185cab289890d0"
clean_word_count: 448
clean_char_count: 3206
---
# Adding structured data support for Product Variants

In 2022, Google [expanded support for Product structured data](/search/blog/2022/09/merchant-listings), enabling enhanced product experiences in Google Search.
Then, in 2023 we [added support for shipping and returns structured data](/search/blog/2023/04/shipping-and-returns-information).
Today, we are [adding structured data support for Product variants](/search/docs/appearance/structured-data/product-variants), allowing merchants to easily show more variations of the products they sell, and show shoppers more relevant, helpful results.
Providing variant structured data will also complement and enhance [merchant center feeds](https://support.google.com/merchants/answer/7439882), including [automated feeds](https://support.google.com/merchants/answer/7538732).

Many products are sold in different variations.
For example apparel, shoes, furniture, and luggage are sold in various sizes, colors, materials, or patterns.
Similarly, electronics products such as laptops or smartphones are sold with different memory sizes, screen sizes, and processors.

![An illustration of how variants can appear on an ecommerce website](/static/search/blog/images/product-variants-2024-1.png)

*An illustration of how variants can appear on an ecommerce website*

Once you start using the new structured data for Product variants using the Schema.org `ProductGroup` type your product variants may be eligible to show in enhanced Google Search results.

## How to provide product variants to Google?

Websites for variant products are more complex than single-product sites, and, consequently, the associated structured data is more complex as well.
One added complexity is that variants must be grouped together under one "parent" product.
To allow such grouping of variants, we are now adding support for the [Schema.org](https://schema.org) `ProductGroup` type and 3 new properties:

- `hasVariant` (to nest `Product` variants under their parent `ProductGroup`),
- `variesBy` (to list the variant-identifying properties), and
- `productGroupID` (the ID, also known as "parent sku" of the `ProductGroup)`.

As part of this expanded support for product variants, we're adding new comprehensive [documentation](/search/docs/appearance/structured-data/product-variants) and validations for both single-page and multi-page variant websites.

## Verifying and monitoring your product variants structured data with Search Console

New validations for variants have been added to the [Product snippets and Merchant listings reports](https://support.google.com/webmasters/answer/12660034) in Search Console and [Rich Results Test](https://search.google.com/test/rich-results):

![Product variant structured data in the Rich Results Test](/static/search/blog/images/product-variants-2024-2.png)

We hope these additions make it easier for you to add variant structured data and show your product variants on Google Search.
If you have any questions or concerns, contact us using the [Google Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category%3Astructured_data)) or on [social media](https://twitter.com/googlesearchc).
