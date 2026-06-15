---
title: "Adding markup support for organization-level return policies"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "2024-06-structured-data-return-policies"
url: "https://developers.google.com/search/blog/2024/06/structured-data-return-policies"
canonical: "https://developers.google.com/search/blog/2024/06/structured-data-return-policies"
author: "Irina Tuduce"
published: "2024-06-11T00:00:00+00:00"
updated: "2024-06-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
fetched_at: "2026-06-14T13:43:54+00:00"
status_code: 200
html_hash: "bf720b81fa0bc510c677c9a7828812dadf8a6cea5788c2531c15e98ff4804237"
clean_word_count: 426
clean_char_count: 2932
---
# Adding markup support for organization-level return policies

A return policy is a major factor considered by shoppers when buying products online, and so
[last year](/search/docs/appearance/structured-data/merchant-listing#product-with-returns-example)
we enabled the extraction of structured data return policies for individual products. Today we're adding support
for return policies at the [organization](/search/docs/appearance/structured-data/organization) level
as well, which means you'll be able to specify a general return policy for your business instead of having to
define one for each individual product you sell.

![An illustration of a knowledge panel that shows a free 30-day return policy](/static/search/blog/images/merchant-organization-information.png)

Adding an organization-level return policy can help reduce the size of your [Product](/search/docs/appearance/structured-data/product)
structured data markup and make it easier to manage your return policy markup in one place. It can also make your return
policies eligible to show with additional search results such as [knowledge panels](https://support.google.com/knowledgepanel/answer/9163198)
and [brand profiles](https://support.google.com/merchants/answer/14998338), in addition
to product search results.

Adding a return policy to your organization structured data is especially important if you don't have a Merchant Center
account and want the ability to provide a return policy for your business. Merchant Center already lets you
provide a [return policy](https://support.google.com/merchants/answer/10220642) for
your business, so if you have a Merchant Center account we recommend defining your return policy there instead.

## Adding support for return policies to the Rich Results Test

You can test [return policies](/search/docs/appearance/structured-data/organization#example-online-store) defined
under your organization structured data using the [Rich Results Test](https://search.google.com/test/rich-results)
by submitting the URL of a page or a code snippet. Using the tool, you can confirm whether or not your markup is valid.

![Rich Results Test showing organization-level return policies](/static/search/blog/images/rich-results-test-return-policy.png)

If your site is an online or local business, we recommend using one of the [`OnlineStore`](https://schema.org/OnlineStore),
or [`LocalBusiness`](https://schema.org/LocalBusiness) subtypes of `Organization`.

We hope this addition makes it easier for you to add return policies for your business, and enable them to be shown
across Google shopping experiences. If you have any questions or concerns, reach out to us using the
[Google Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category%3Astructured_data)),
on [Twitter](https://twitter.com/googlesearchc), or on [LinkedIn](https://www.linkedin.com/showcase/googlesearchcentral/).
