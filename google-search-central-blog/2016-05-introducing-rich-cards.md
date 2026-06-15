---
title: "Introducing Rich Cards"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2016-05-introducing-rich-cards"
url: "https://developers.google.com/search/blog/2016/05/introducing-rich-cards"
canonical: "https://developers.google.com/search/blog/2016/05/introducing-rich-cards"
author: "Na'ama Zohary, Search Console Team, and Elliott Ng, Product Management Director, Search Ecosystem"
published: "2016-05-17T00:00:00+00:00"
updated: "2016-05-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2016_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:28:48+00:00"
status_code: 200
html_hash: "d288ade2a7a307ff27bc075df977db56bee1aebbef61ace28efa6bbcdc60f283"
clean_word_count: 767
clean_char_count: 5027
---
# Introducing Rich Cards

Rich cards are a new Search result format building on the success of rich snippets. Just like
rich snippets, rich cards use schema.org structured markup to display content in an even more
engaging and visual format, with a focus on providing a better mobile user experience.

![Evolution of search results for queries like [peanut butter cookies recipe]: with rich cards, results are presented in carousels that are easy to browse by scrolling left and right. Carousels can contain cards all from the same site or from multiple sites.](/static/search/blog/images/import/128e44dec1ceb16824989f41542dd9f0.png)

For site owners, this is a new opportunity to stand out in Search results and attract more targeted
users to your page. For example, if you have a recipe site, you can build a richer preview of your
content with a prominent image for each dish. This visual format helps users find what they want
right away, so you're getting users who specifically want that especially delicious cookie recipe
you have.

We're starting to show rich cards for two content categories: recipes and movies. They will appear
initially on mobile search results in English for google.com. We're actively experimenting with
more opportunities to provide more publishers with a rich preview of their content.

We've built a comprehensive set of tools and completely updated our developer documentation to take site owners and developers from initial exploration through implementation to performance monitoring.

## Explore rich card types and identify where your content fits

Browse the [new gallery](/search/docs/appearance/structured-data/search-gallery) with screenshots and code
samples of each markup type.

## Test and tweak your markup

We strongly recommend using JSON-LD in your implementation.

- Find out
  [which fields are essential](/search/docs/guides/mark-up-content)
  to mark up in order for a rich card to appear. We've also listed additional fields that can
  enhance your rich cards.
- See a preview in the
  [revamped
  Structured Data Testing Tool](/search/docs/advanced/structured-data) of how the rich card might appear in Search (currently
  available for recipes and movies).
- Use the Structured Data Testing Tool to see errors as you tweak your markup in real time.

![analysis results in the structured data testing tool](/static/search/blog/images/import/bf9afabd1ff5bece38803fb7ccac9159.png)

## Keep track of coverage and debug errors

Check how many of your rich cards are indexed in the
[new Search Console Rich Cards report](https://www.google.com/webmasters/tools/rich-cards).

![aggregate report showing a decrease in validation errors in the Search console rich cards report](/static/search/blog/images/import/952fe140814a2355959933caa1366b2c.png)

- Keep an eye out for errors (also listed in the Rich Cards report). Each error example links
  directly to the Structured Data Testing tool so you can test it.
- [Submit a sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap) to help us discover
  all your marked-up content.

## Find opportunities for growth

In the Rich Cards report, you'll see which cards can be enhanced by marking up additional fields.

![aggregate report in the search console rich cards report showing the potential number of rich cards that can be improved ](/static/search/blog/images/import/7e7bccf4b8f6b21382238b2228be78ad.png)

## Monitor performance

A new "Rich results" filter in Search Analytics (currently in a closed beta) will help you track
how your rich cards and rich snippets are doing in search: you'll be able to drill down and see
clicks and impressions for both.

## FAQ

### Can I keep my existing rich snippets markup?

Yes, you can! We'll keep you posted as the rich result ecosystem evolves.

### What about the Structured Data report in Search Console?

The Structured Data report will continue to show only
[top-level entities](https://support.google.com/webmasters/answer/2650907)
for the existing rich snippets (Product, Recipe, Review, Event, SoftwareApplication, Video, News
article) and for any new categories (for example, Movies). We plan to migrate all errors from the
Structured Data report into the Rich Card report.

### What if I use the wrong markup?

Technical and quality guidelines apply for rich cards as they do for rich snippets. We will enforce them as before.

Learn more about rich cards in the
[Search and the mobile content ecosystem](https://events.google.com/io2016/schedule?sid=8f9c1403-0cef-e511-a517-00155d5066d7#day2/8f9c1403-0cef-e511-a517-00155d5066d7)
session at Google I/O (watch the
[recording on YouTube](https://www.youtube.com/watch?v=xeGzQhAU2XI)) or in our
[documentation](/search/docs/appearance/structured-data/intro-structured-data). If you have more questions,
find us in the [dedicated
structured data section](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:structured_data)) of our forum or [on Twitter](https://twitter.com/googlesearchc).
