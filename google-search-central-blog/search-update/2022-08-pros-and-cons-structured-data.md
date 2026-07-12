---
title: "New in structured data: Pros and cons"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2022-08-pros-and-cons-structured-data"
url: "https://developers.google.com/search/blog/2022/08/pros-and-cons-structured-data"
canonical: "https://developers.google.com/search/blog/2022/08/pros-and-cons-structured-data"
author: "Alan Kent"
published: "2022-08-05T00:00:00+00:00"
updated: "2022-08-05T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:40:49+00:00"
status_code: 200
html_hash: "7590122cbec26d6286da70580abe0acd2828cc0bcc846f579318ef8d790de1b3"
clean_word_count: 486
clean_char_count: 3999
---
# New in structured data: Pros and cons

Product reviews are a valuable resource for users researching which product to buy.
Product reviews often contain a list of pros and cons, which our research has shown
to be popular with shoppers when making their purchasing decisions.
Because of their importance to users, Google Search may highlight
[pros and cons](/search/docs/appearance/structured-data/product#pros-cons)
in the product review snippet in Search results.

![Example search results snippet highlighting pros and cons from an editorial review](/static/search/blog/images/pros-and-cons-structured-data.png "Example search results snippet highlighting pros and cons from an editorial review")

You can tell Google about your pros and cons by supplying
[pros and cons structured data](/search/docs/appearance/structured-data/product#pros-cons)
on editorial review pages. When you're adding structured data to your web pages, you can use
[Rich Results Test](https://search.google.com/test/rich-results)
to make sure it's correct and valid for Google Search.
The tool has been recently extended to check for pros and cons structured data in addition to
all the other structured data types supported by Google Search.

If you do not provide structured data,
Google may try to automatically identify pros and cons listed on the web page.
Google will prioritize supplied structured data provided by you over automatically extracted data.
We tested this with website owners, and received positive feedback on this capability.

Here is an example web page with JSON-LD encoded structured data that could be used for the
above search results experience.
Note that the text in the structured data must match the text on your page.

```
<html>
  <head>
    <title>Cheese Knife Pro review</title>
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "Cheese Knife Pro",
        "review": {
          "@type": "Review",
          "name": "Cheese Knife Pro review",
          "author": {
            "@type": "Person",
            "name": "Pascal Van Cleeff"
          },
          "positiveNotes": {
            "@type": "ItemList",
            "itemListElement": [
              {
                "@type": "ListItem",
                "position": 1,
                "name": "Consistent results"
              },
              {
                "@type": "ListItem",
                "position": 2,
                "name": "Still sharp after many uses"
              }
            ]
          },
          "negativeNotes": {
            "@type": "ItemList",
            "itemListElement": [
              {
                "@type": "ListItem",
                "position": 1,
                "name": "No child protection"
              },
              {
                "@type": "ListItem",
                "position": 2,
                "name": "Lacking advanced features"
              }
            ]
          }
    </script>
  </head>
  <body>
    . . .
    <p>Pros:</p>
    <ul>
      <li>Consistent results</li>
      <li>Still sharp after many uses</li>
    </ul>
    <p>Cons:</p>
    <ul>
      <li>No child protection</li>
      <li>Lacking advanced features</li>
    </ul>
    . . .
  </body>
</html>
```

Currently, only editorial product review pages are eligible for the pros and cons enhancement
in Search, not merchant product pages or customer product reviews.
The experience is available in Dutch, English, French, German, Italian, Japanese, Polish,
Portuguese, Spanish, and Turkish in all countries where Google Search is available.

For more information on how to implement pros and cons structured data, check out the
Google Search Central documentation on
[Product structured data](/search/docs/appearance/structured-data/product#pros-cons).
For additional advice, please check out Google Search Central
[help pages](/search/docs)
and our public
[forum](https://support.google.com/webmasters/community).
