---
title: "Google’s Universal Commerce Protocol capabilities expand to main SERP"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-ucp-checkout-in-main-serp"
url: "https://www.semrush.com/blog/google-ucp-checkout-in-main-serp/"
canonical: "https://www.semrush.com/blog/google-ucp-checkout-in-main-serp/"
author: "Leigh McKenzie"
published: "2026-05-07T08:36:00+00:00"
updated: "2026-05-07T08:36:00+00:00"
categories:
  - "Industry News"
freshness_reasons:
  - "news_or_research"
schema_genre: "Industry News"
fetched_at: "2026-06-12T16:03:15+00:00"
status_code: 200
html_hash: "94c91025a706e1342bb8bd62efbe43a80aba031fd72c9576525117df1bcd7d8a"
clean_word_count: 672
clean_char_count: 4682
---
# Google’s Universal Commerce Protocol capabilities expand to main SERP

UCP-powered checkout has begun appearing in Google Search product listings, allowing logged-in users to transact via a “Buy” button directly from the search engine results page (SERP).

Clicking the “Buy” button connects the shopper's Google Pay account directly to the retailer’s checkout system to complete the purchase without requiring a visit to the retailer's website.

Universal Commerce Protocol (UCP) is Google’s open standard for agentic commerce. And until now, UCP-powered checkout has only been available through AI Mode and the Gemini App.

[Google launched UCP](https://www.semrush.com/blog/universal-commerce-protocol/) in January 2026 as a co-developed open standard with partners including Shopify, Etsy, Wayfair, Target, and Walmart. And the expansion to product listings on the main SERP was spotted on Wayfair product listings, as reported by [SERP Alert on X](https://x.com/serpalerts/status/2051647067718590845?s=46).

![SERP Alert posted on X about seeing UCP-powered checkout directly in SERP product listings.](https://static.semrush.com/blog/uploads/media/ef/4f/ef4f363f0cb7c49d76870dc73d2aa5c4/6f96d6648ee6f8aa4258c97b0242264e/image.png)

The rollout will likely extend to other partners. But UCP-powered checkout seems to only be enabled for Wayfair at the moment.

I ran several similar searches related to furniture. The “Buy” button only appeared for Wayfair products:

![Google search results for "futons" showing UCP-powered checkout for a Wayfair product.](https://static.semrush.com/blog/uploads/media/42/40/4240d15545a3b2642493f7f8404dde41/11ec29543631a68d3482d4f8646afd52/image.png)

## Why UCP-powered checkout on the main SERP matters

For marketers, UCP-powered checkout coming to the main SERP signals that Google sees agentic commerce as ready for its most familiar interface.

It’s also another concrete step toward an agentic future, one where AI agents act on behalf of users to research, compare, and now complete transactions.

Discoverability is a prerequisite for participating in those transactions. If your products and any relevant actions aren’t clear when an agent goes looking, you risk losing out.

For businesses interested in UCP-powered checkout, you need to have a Google Merchant Center account with approved products eligible for free listings. And your account should have the following settings configured:

- The `native_commerce` product attribute set on eligible items via your product feed, which is what triggers the "Buy" button on those listings
- Defined return policies, shipping settings, and customer support information
- A Google Pay & Wallet Console account, with your payment service provider integrated with the Google Pay API
- A published `/.well-known/ucp` profile and the three core REST endpoints (session creation, updates, and completion), per [Google's UCP developer guide](https://developers.google.com/merchant/ucp/guides)
- Submission of the [early access interest form](https://support.google.com/merchants/contact/ucp_integration_interest)

## How to prepare for agentic commerce

To prepare for successful transactions directly on the Google SERP, you need accurate product structured data. Because Google uses it to verify your Merchant Center feed.

Use Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool to crawl your website and detect any issues with your product structured data that could impact your Merchant Center eligibility.

Just look for any invalid items in the “Merchant listings” row. There are none in the example below.

![The Markup report in Site Audit reveals issues with merchant listing structured data.](https://static.semrush.com/blog/uploads/media/67/3e/673e73932123445a0fd4eae84441712b/9113f708fae350f255beb807ef8d4dd1/image.png)

It’s also a good idea to use Site Audit to check whether AI crawlers can effectively crawl your site. Doing that now prepares you for a future where agentic actions happen on your website.

![The Overview report in Site Audit shows any issues with AI crawlers' ability to access your site.](https://static.semrush.com/blog/uploads/media/e0/51/e051cc4ee41cc00d07080ed851de05fc/bd076b9f0921ecb7d88805714b08de22/image.png)

For enterprise teams, [Semrush Enterprise Site Intelligence](https://enterprise.semrush.com/solutions/site-intelligence/) includes Bot Analytics for an even more advanced way to analyze AI bot activity.

![Semrush Enterprise Site Intelligence includes Bot Analytics to reveal AI bot activity.](https://static.semrush.com/blog/uploads/media/f8/c7/f8c741a8391f024643cfd27b40b6fb55/0ab70614c47430164f4e81fc49e0b4f9/image.png)
