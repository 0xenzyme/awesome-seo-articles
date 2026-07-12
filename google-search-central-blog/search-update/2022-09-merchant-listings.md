---
title: "New Search Console Merchant Listings report: expanding eligibility with Product structured data"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2022-09-merchant-listings"
url: "https://developers.google.com/search/blog/2022/09/merchant-listings"
canonical: "https://developers.google.com/search/blog/2022/09/merchant-listings"
author: "Alan Kent"
published: "2022-09-13T00:00:00+00:00"
updated: "2022-09-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:40:54+00:00"
status_code: 200
html_hash: "7add00753839c490e0ab7769336e711a557aa9f0b008090987621e5490a2d4d8"
clean_word_count: 780
clean_char_count: 5549
---
# New Search Console Merchant Listings report: expanding eligibility with Product structured data

Google is pleased to announce expanded eligibility for enhanced product experiences in
Google Search through the use of `Product` structured data. These enhanced
product experiences were previously only open to Merchant Center users. We're also making
it easier to understand the requirements for these experiences by updating our documentation
and reporting in Search Console.

## Expanded eligibility for websites that directly sell products

For some time, Google has provided shoppers with rich product experiences in search results.
To make these experiences more accessible to website owners, Google has expanded eligibility
for websites that implement structured data. For website owners, there are two broad categories
of experiences:

- **Merchant listing experiences** for web pages that allow shoppers to buy a product on the site.
- **Product snippets** for a broader set of web pages with product information (including
  pages that sell products, publish product reviews, and/or aggregate information from other sites).

Initially, product snippets in Google search results were primarily powered by schema.org
[`Product` structured data](https://schema.org/Product),
and merchant listing experiences were primarily powered by product details supplied via a
[Google Merchant Center feed](https://support.google.com/merchants/answer/7052112).
Now merchants can be eligible for merchant listing experiences by providing product data on web
pages without a Google Merchant Center account. This improved eligibility has in part been made
possible by recent extensions to product-related properties and types in schema.org for areas
such as apparel sizing and energy efficiency ratings.

## Enhanced product experiences available in Search

Once you add structured data, you may be eligible for the following experiences.

![How a merchant listing experience can appear in search results](/static/search/blog/images/merchant-listings-popular-products.png "How a merchant listing experience can appear in search results")

**Figure 1.** How a merchant listing experience can appear in search results

Merchant listing experiences offer enhanced experiences including the
[Shopping Knowledge panel](https://blog.google/products/shopping/bringing-free-retail-listings-google-search/) and
[Popular Products](https://www.blog.google/products/search/new-way-find-clothes-shoes-and-more-search/),
as well as shopping experiences in
[Google Images](https://images.google.com/) and
[Google Lens](https://lens.google/). The structured data
required for merchant listings and product snippets is described in our
[`Product` structured data documentation](/search/docs/appearance/structured-data/product).

![An example product snippet in search results](/static/search/blog/images/merchant-listings-product-snippet.png "An example product snippet in search results")

**Figure 2.** An example product snippet in search results

## Introducing new Search Console reports for site owners

![Search Console navigation sidebar showing links to new reports](/static/search/blog/images/merchant-listings-report-navigation.png)

To help websites take advantage of these experiences, the existing Search Console report for
`Product` structured data has been replaced with two reports: a new
[Merchant listings report](https://search.google.com/search-console/r/merchant-listings), and a
[Product snippets report](https://search.google.com/search-console/r/product)
(which subsumes the old Product report). These reports are
grouped under a new Shopping section in the Search Console navigation bar.

The reports allows you to see errors, warnings, and valid pages for markup implemented on your
site. The changes in reporting have also been reflected in the
[Rich Result Test tool](https://support.google.com/webmasters/answer/7445569).

### New Merchant listings report

- Identifies structured data issues for
  [free listing experiences](https://support.google.com/merchants/answer/9826670)
  in search results.
- Relevant to pages that sell products.
- Covers the wider range of schema.org structured data properties and types used by the
  `Product` type that are now supported for advanced cases, such as apparel sizing
  and energy efficiency ratings.

### Product snippets report

- Identifies structured data issues for product snippets in search results.
- Relevant to pages that share product review information or aggregate product data from
  multiple sites. Note that pages selling products may also include product reviews.
- Replaces the previous Product structured data report with adjustments related to the
  separation of merchant listing validations into a dedicated report. The history of prior
  validation errors is retained in this report.

## Which report should I use?

If you are a merchant with an online store, you should:

- Check the merchant listings report for your pages selling products.
- If you publish product reviews on pages that don't sell products, also check the Product snippets report.

If you don't sell products online but still publish pages with Product structured data:

- Check the Product snippets report.

## Learn more about Product structured data

To learn more, check our updated documentation on
[`Product` structured data](/search/docs/appearance/structured-data/product).
If you have questions, please reach out on the
[Google Search Central forum](https://support.google.com/webmasters/community).
