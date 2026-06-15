---
title: "More ways to share your shipping and returns policies with Google"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "2025-11-more-ways-to-share-shipping"
url: "https://developers.google.com/search/blog/2025/11/more-ways-to-share-shipping"
canonical: "https://developers.google.com/search/blog/2025/11/more-ways-to-share-shipping"
author: "Pascal Fleury, Irina Tuduce"
published: "2025-11-12T00:00:00+00:00"
updated: "2025-11-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "news_or_research"
fetched_at: "2026-06-14T13:45:43+00:00"
status_code: 200
html_hash: "33bd615dcd3c0b12842e671598a0539454981d697910feaffb4aa08001141546"
clean_word_count: 684
clean_char_count: 4747
---
# More ways to share your shipping and returns policies with Google

Shipping speed, cost, and return policies are critical factors for online shoppers. When customers
have clear information on fulfillment, it builds trust and improves their shopping experience.

Last year, we launched [shipping and return policies in Search Console](/search/blog/2024/07/configure-shipping-and-returns-search-console)
for merchants with a configured Merchant Center account. We also enabled all merchants to
[add organization-level return policies with structured data](/search/blog/2024/06/structured-data-return-policies)
for the first time.

We're excited to announce that we're now expanding the options for merchants to provide shipping
and returns information, even if they don't have a Merchant Center account. Merchants can now
tell Google about their shipping and returns policies in two distinct ways: by configuring them
directly in Search Console or by using new organization-level structured data.

## Configure policies directly in Search Console

![Shipping and returns settings page in Search Console](/static/search/blog/images/sc-shipping-settings.png)

We're expanding the "Shipping and returns" feature in Search Console settings to be available to
all websites that have been identified by Google as
[online merchants](https://support.google.com/webmasters/answer/12660034#online_merchant_def).

Previously, this feature was only available to merchants with a configured Merchant Center account.
Now, if Google identifies your website as an online merchant, you can set up your shipping and
returns policies directly within Search Console. This provides a UI-based method to
share your information with Google.

This is an alternative to providing this information with structured data. It's important to note
that settings configured in Search Console will take precedence over structured data on your site.

The "Shipping and returns" configuration will be rolling out gradually over the coming weeks for
all countries and languages.

## Add organization-level shipping policy markup

If you prefer to manage this information with code, we're introducing
[organization-level shipping policy structured data](/search/docs/appearance/structured-data/shipping-policy).

This new markup support complements last year's launch of organization-level *return*
policies. Instead of adding [shipping markup to every single product](/search/docs/appearance/structured-data/merchant-listing#shipping),
you can now specify a general, site-wide shipping policy. This is ideal when your shipping
policies apply to the majority of your products, as it reduces the amount of markup you need to
manage. Shipping policies specified for individual products will still take priority over this
general, organization-level policy for those specific items.

We recommend placing shipping structured data (nested under `Organization`)
on the page where you describe your shipping policy. You can then test your markup using the
[Rich Results Test](https://search.google.com/test/rich-results)
by submitting the URL of the page with shipping markup or pasting the code snippet with shipping
markup. Using the tool, you can confirm whether or not your markup is valid. For example, here is
a test for shipping policy markup:

![Shipping policy markup in the Rich Results Test](/static/search/blog/images/shipping-policy-markup-rrt.png)

If your site is an online or local business, we recommend using one of the
`OnlineStore` or
`LocalBusiness`
subtypes of `Organization`.

We continue to recommend adding shipping policies for individual products to override your
organization-level shipping policy or when you don't have a general shipping policy that applies
to the majority of your products. If you're already specifying product-level shipping policies, you
can continue to use them while also adding an organization-level shipping policy, if applicable.

By providing your shipping and returns information through either of these methods, your fulfillment
policies may appear in more search results, including
[knowledge panels](https://support.google.com/knowledgepanel/answer/9163198),
[brand profiles](https://support.google.com/merchants/answer/14998338), and product
search results. This can improve your visibility, showcase fulfillment services like free and fast
shipping, and ultimately attract more customers.

We hope these new options make it easier for all merchants to showcase their fulfillment policies
and optimize their appearance in search results. If you have any questions or concerns, please
reach out to us in the [Google Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)).
