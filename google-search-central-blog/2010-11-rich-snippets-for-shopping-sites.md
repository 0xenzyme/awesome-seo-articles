---
title: "Rich snippets for shopping sites"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-11-rich-snippets-for-shopping-sites"
url: "https://developers.google.com/search/blog/2010/11/rich-snippets-for-shopping-sites"
canonical: "https://developers.google.com/search/blog/2010/11/rich-snippets-for-shopping-sites"
author: "Written by Nitin Shetti and Mircea Ciurumelea, Search Quality team"
published: "2010-11-02T00:00:00+00:00"
updated: "2010-11-02T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:09:59+00:00"
status_code: 200
html_hash: "e0b007e4b092668cd6a76b3b0041ce1dad9dc60a386e38f2abf22e5a6e021dc5"
clean_word_count: 784
clean_char_count: 4944
---
# Rich snippets for shopping sites

In time for the holiday season, we now support rich snippets for shopping (e-commerce) sites!
As many of you know,
[rich snippets](/search/docs/appearance/structured-data/intro-structured-data)
are search results that have been enhanced using structured data from your web pages. Our new
format shows price, availability, and product reviews on pages offering a product for sale. Here's
a result for
["office lava lamp"](https://www.google.com/search?q=office+lava+lamp):

![office lava lamp search result](/static/search/blog/images/import/c9190b39acf0528586afbf86615421d6.png)

As a webmaster, there are two ways that you can provide the information needed for product rich
snippets to show up for your site, both described on the
[Product rich snippets help page](/search/docs/appearance/structured-data/product):

## Option 1: Provide a Merchant Center feed

Many sites already provide
[Merchant Center feeds](https://www.google.com/support/merchants/bin/topic.py?topic=30064)
for use in
[Google Product Search](https://www.google.com/products),
which means that most of the work needed for rich snippets is already done. For Google to make use
of Merchant Center feeds for rich snippets, you should also use the
[`rel="canonical"` `link` element](/search/docs/crawling-indexing/consolidate-duplicate-urls)
on your product pages. By adding `rel="canonical"` to your pages, Google can match the
URLs in your feed to the pages found by our crawler.

**Update on November 4, 2010:**
In order to have your product review information in your rich snippets, you can submit your
product ratings directly in your
[feed](https://www.google.com/support/merchants/bin/answer.py?answer=188494#recommended),
or you can work with one of our
[reviews partners](https://www.google.com/products/submit/reviews)
to submit this information. If you work with a partner, your reviews information will appear in
rich snippets, and shoppers on Google Product Search will be able to see your
[full-length reviews](https://googlemerchantblog.blogspot.com/2010/04/announcing-google-product-reviews)
on relevant product pages, branded with your logo.

## Option 2: Add markup to your site

If prices for your products tend to change only infrequently, then adding markup is an alternative
method to provide product data for rich snippets. We've updated our
[product markup format](/search/docs/appearance/structured-data/product)
to allow a variety of different types of shopping sites to participate. In addition to the Google
format, we support two other standards: the
[hProduct](https://microformats.org/wiki/hproduct) microformat and
[GoodRelations](https://www.heppnetz.de/projects/goodrelations/).
You can use the
[rich snippets testing tool](https://www.google.com/webmasters/tools/richsnippets)
to test your markup and make sure it's being parsed correctly.

This feature is currently available to merchants located in the US, but we will be rolling it out
in more markets soon. Additionally, there are a number of
[rich snippets formats](/search/docs/appearance/structured-data/search-gallery)
that can be used
[world-wide in various languages](/search/blog/2010/04/rich-snippets-go-international)
—make your snippets compelling and useful! Should you have any questions about the use of rich
snippets, check out our
[FAQs](https://sites.google.com/site/webmasterhelpforum/en/faq-rich-snippets)
and you can post in our
[Webmaster Help Forum](https://support.google.com/webmasters/community).

## Q&A

**Which should I provide—a Merchant Center feed or markup?**
For most merchants, providing a Merchant Center feed is the best bet. That way your product prices
and availability are updated quickly, and the data can be shown in rich snippets as well as in
other applications like Google Shopping and Product Ads. If prices and availability change only
infrequently, and you don't want to set up a feed, then adding markup is also a valid option.

**If I add markup to my site, will Google show product rich snippets for my pages?**
We can't guarantee that providing a feed or adding markup will result in rich snippets being
shown. Note also that it may take a few weeks after providing data for rich snippets to be shown.
If you mark up your pages, we encourage you to make sure that the data is parsed correctly by
Google by using the
[rich snippets testing tool](https://search.google.com/test/rich-results).
The testing tool updates are rolling out over the next few days, so in this interim period the
testing tool may not show previews for some types of markup.

**I've already done reviews markup for my product offer pages. Should I add product/offer markup
as well?**
Yes, absolutely. Rich snippets are shown if the information provided accurately represents the
main focus of the page. Therefore, for product pages you should add markup using the relevant
offer/product fields which can include nested reviews.
