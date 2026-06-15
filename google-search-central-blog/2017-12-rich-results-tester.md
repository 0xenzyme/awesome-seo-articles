---
title: "Introducing Rich Results and the Rich Results Testing Tool"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2017-12-rich-results-tester"
url: "https://developers.google.com/search/blog/2017/12/rich-results-tester"
canonical: "https://developers.google.com/search/blog/2017/12/rich-results-tester"
author: "Shachar Pooyae, Software Engineer"
published: "2017-12-19T00:00:00+00:00"
updated: "2017-12-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:31:30+00:00"
status_code: 200
html_hash: "7513beef9081be9755d9501dd785f721969d20ac1b51f03a5065c48497ef4305"
clean_word_count: 339
clean_char_count: 2106
---
# Introducing Rich Results and the Rich Results Testing Tool

[Over the years](/search/blog/2009/05/introducing-rich-snippets), the different ways
you can choose to highlight your website's content in search has grown dramatically. In the past,
we've called these rich snippets, rich cards, or enriched results. Going forward - to simplify the
terminology - our documentation will use the name "rich results" for all of them. Additionally,
we're introducing a
[new rich results testing tool](https://search.google.com/test/rich-results)
to make diagnosing your pages' structured data easier.

The new testing tool focuses on the structured data types that are eligible to be shown as rich
results. It allows you to test all data sources on your pages, such as JSON-LD (which we
recommend), Microdata, or RDFa. The new tool provides a more accurate reflection of the page's
appearance on Search and includes improved handling for Structured Data found on dynamically
loaded content. The tests for Recipes, Jobs, Movies, and Courses are currently supported —
but this is just a first step, we plan on expanding over time.

![](/static/search/blog/images/import/77614fc7f974abccc9393c9bfedb3ac3.png)

Testing a page is easy: just open the
[testing tool](https://search.google.com/test/rich-results), enter a
URL, and review the output. If there are issues, the tool will highlight the invalid code in the
page source. If you're working with others on this page, the share-icon on the bottom-right lets
you do that quickly. You can also use preview button to view all the different rich results the
page is eligible for. And once you're happy with the result, use Submit To Google to fetch and
index this page for search.

Want to get started with rich snippets rich results? Check out our
[guides for marking up your content](/search/docs/appearance/structured-data/search-gallery).
You can drop by our
[Webmaster Help forums](https://support.google.com/webmasters/go/community)
should you have any questions or get stuck; the awesome experts there can often help resolve
issues and give you tips in no time!
