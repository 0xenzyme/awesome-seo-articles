---
title: "A note on unsupported rules in robots.txt"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2019-07-a-note-on-unsupported-rules-in-robotstxt"
url: "https://developers.google.com/search/blog/2019/07/a-note-on-unsupported-rules-in-robotstxt"
canonical: "https://developers.google.com/search/blog/2019/07/a-note-on-unsupported-rules-in-robotstxt"
author: "Gary Illyes"
published: "2019-07-02T00:00:00+00:00"
updated: "2019-07-02T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:34:32+00:00"
status_code: 200
html_hash: "d11bd0dc203e9988e8230378939e1f50bf851290723a533920c7e1e05dd71a7d"
clean_word_count: 551
clean_char_count: 3588
---
# A note on unsupported rules in robots.txt

Yesterday we announced that we're
[open-sourcing Google's production robots.txt parser](/search/blog/2019/07/repp-oss).
It was an exciting moment that paves the road for potential Search open sourcing projects in the
future! Feedback is helpful, and we're eagerly collecting questions from
[developers](https://github.com/google/robotstxt) and
[webmasters](https://twitter.com/googlesearchc) alike. One question
stood out, which we'll address in this post:

Why isn't a code handler for other rules like crawl-delay included in the code?

[The internet draft](/search/blog/2019/07/rep-id) we published yesterday provides an
extensible architecture for rules that are not part of the standard. This means that if a
crawler wanted to support their own line like `unicorns: allowed`,
they could. To demonstrate how this would look in a parser, we included a very common line,
sitemap, in our [open-source robots.txt parser](https://github.com/google/robotstxt).

While open-sourcing our parser library, we analyzed the usage of robots.txt rules. In particular,
we focused on rules unsupported by the internet draft, such as
`crawl-delay`, `nofollow`, and
`noindex`. Since these rules were never documented by Google,
naturally, their usage in relation to Googlebot is very low. Digging further, we saw their usage
was contradicted by other rules in all but 0.001% of all robots.txt files on the internet.
These mistakes hurt websites' presence in Google's search results in ways we don't think
webmasters intended.

In the interest of maintaining a healthy ecosystem and preparing for potential future open source
releases, we're retiring all code that handles unsupported and unpublished rules (such as
`noindex`) on September 1, 2019. For those of you who relied on the
`noindex` indexing rule in the
`robots.txt` file, which controls crawling, there are a number of
alternative options:

- **[`noindex`](/search/docs/crawling-indexing/block-indexing)
  in robots `meta` tags:** Supported both in the HTTP response headers and in HTML, the
  `noindex` rule is the most effective way to remove URLs from
  the index when crawling is allowed.
- **[`404` and `410` HTTP status codes](https://en.wikipedia.org/wiki/HTTP_404):**
  Both status codes mean that the page does not exist, which will drop such URLs from Google's
  index once they're crawled and processed.
- **Password protection:** Unless markup is used to indicate
  [subscription or paywalled content](/search/docs/appearance/structured-data/paywalled-content),
  hiding a page behind a login will generally remove it from Google's index.
- **`Disallow` in `robots.txt`:** Search engines can only index pages
  that they know about, so blocking the page from being crawled usually means its content won't
  be indexed. While the search engine may also index a URL based on links from other pages,
  without seeing the content itself, we aim to make such pages less visible in the future.
- **[Search Console Remove URL tool](https://support.google.com/webmasters/answer/1663419):**
  The tool is a quick and easy method to remove a URL temporarily from Google's search results.

For more guidance about how to remove information from Google's search results, visit our
[Help Center](/search/docs/guides/advanced/remove-information?ref_topic=1724262).
If you have questions, you can find us on [Twitter](https://twitter.com/googlesearchc)
and in our [Webmaster Community](https://support.google.com/webmasters/community),
both [offline](/search/events/search-central-live) and online.
