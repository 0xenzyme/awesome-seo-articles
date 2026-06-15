---
title: "An update on the Structured Data Testing Tool"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2020-12-structured-data-testing-tool-update"
url: "https://developers.google.com/search/blog/2020/12/structured-data-testing-tool-update"
canonical: "https://developers.google.com/search/blog/2020/12/structured-data-testing-tool-update"
author: "Ryan\n      Levering"
published: "2020-12-15T00:00:00+00:00"
updated: "2020-12-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:38:09+00:00"
status_code: 200
html_hash: "02b154fedea258bb9063a59cdab41ebf7f8d0d28f115a1e5fd26de126ac8182b"
clean_word_count: 409
clean_char_count: 2611
---
# An update on the Structured Data Testing Tool

In July, we announced that the [Rich Results
Test is out of beta](/search/blog/2020/07/rich-results-test-out-of-beta). In that blog post, we said that the [Structured
Data Testing Tool](/search/docs/advanced/structured-data) would be deprecated. Since then, we've heard your feedback and we'd like to
give an update on what the future looks like for the Structured Data Testing Tool.

To better support open standards and development experience, we're refocusing the Structured Data
Testing Tool and migrating it to a new domain serving the schema.org community by April 2021. The
main purpose of the tool will be to check syntax and compliance of markup with schema.org standards.
Going forward however, the tool will no longer check for Google Search rich result types. To test
your markup for Google Search rich result types, you can continue to use the
[Rich Results Test](https://search.google.com/test/rich-results).

As an example, if you are trying to implement <https://schema.org/Event>
markup for the rich event experiences on Google Search based on [our
documentation](/search/docs/appearance/structured-data/event), the [Rich
Results Test](https://search.google.com/test/rich-results) and [Search
Console](https://search.google.com/search-console/about) are the best tools to make sure your markup is valid for Google Search. However, if
you only want to make sure that you're using valid schema.org properties, or validate a type that
we don’t explicitly consume at this time (for example, <https://schema.org/ExercisePlan>),
then you will be able to use the refocused schema.org validator.

If you have questions or feedback, visit our [Google
Search Central Help Community](https://support.google.com/webmasters/community) or let us know through [Twitter](https://twitter.com/googlesearchc).

---

## Updates

- **Update on May 11, 2021**: Schema.org [announced
  the new home](https://blog.schema.org/2021/05/announcing-schema-markup-validator.html) for the structured data validator previously known as the Structured Data Testing
  Tool (SDTT). The new tool, [Schema Markup
  Validator](https://validator.schema.org/), is still under development. Once the new Schema Markup Validator stabilizes,
  Google plans to redirect the Structured Data Testing Tool to the Rich Results Test.
- **Update on August 9, 2021**: The [Schema Markup Validator](https://validator.schema.org/) has stabilized, and Google now redirects the Structured Data Testing Tool to a [landing page](/search/docs/advanced/structured-data) to help you select the right tool.
