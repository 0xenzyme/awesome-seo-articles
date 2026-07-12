---
title: "Simplifying the search results page"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "2025-06-simplifying-search-results"
url: "https://developers.google.com/search/blog/2025/06/simplifying-search-results"
canonical: "https://developers.google.com/search/blog/2025/06/simplifying-search-results"
author: "Henry Hsu, Product Manager, Google Search"
published: "2025-06-12T00:00:00+00:00"
updated: "2025-06-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "news_or_research"
fetched_at: "2026-06-14T13:45:20+00:00"
status_code: 200
html_hash: "457b12b601ed1521f8c49f2c9e78fbef75c7e9dab8ca04849dbacdee85d95d8d"
clean_word_count: 651
clean_char_count: 4647
---
# Simplifying the search results page

As part of our [ongoing efforts](/search/blog/2025/01/simplifying-breadcrumbs) to
simplify the Google Search results page, we will be phasing out support for a few
[structured data](/search/docs/appearance/structured-data/search-gallery) features in
Search. We regularly evaluate the usefulness of Search features, both for users and website owners.

We're phasing out these specific structured data types because our analysis shows that they're
not commonly used in Search, and we found that these specific displays are no longer providing
significant additional value for users. Removing them will help streamline the results page and
focus on other experiences that are more useful and widely used.

This update won't affect how pages are ranked. This simplification means that for some results,
the specific visual enhancements powered by these lesser-used markups will no longer appear,
leading to a more streamlined presentation. The use of these structured data types outside of
Google Search (and dependent features) is not affected.

The following structured data types will no longer be supported in Google Search results and will
be phased out over the coming weeks and months:

- [Book Actions](/search/docs/appearance/structured-data/book)
- [Course Info](/search/docs/appearance/structured-data/course-info)
- [Claim Review](/search/docs/appearance/structured-data/factcheck)
- [Estimated Salary](/search/docs/appearance/structured-data/estimated-salary)
- [Learning Video](/search/docs/appearance/structured-data/learning-video)
- [Special Announcement](/search/docs/appearance/structured-data/special-announcements)
- [Vehicle Listing](/search/docs/appearance/structured-data/vehicle-listing)

Structured data can be a valuable way for website owners to describe their content and enable
helpful Search features. While we're retiring some lesser-used displays, we'll continue to
actively support a range of structured data types that users find helpful when evaluating
content to visit.

We believe this change contributes to a cleaner, more focused Search results page for everyone.
We'll keep looking for ways to simplify the Search results page to provide the best experience for
users and website owners, and we'll share updates as we continue this work. If you have any
questions or concerns, please reach out to us in the
[Google Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category%3Astructured_data))
or on [LinkedIn](https://www.linkedin.com/showcase/googlesearchcentral/).

---

## Updates

### Update on September 8, 2025
:   We are removing support in Search Console for the
    following structured data types, as these types have been phased out from Search results:
    Course Info, Claim Review, Estimated Salary, Learning Video, Special Announcement, and Vehicle
    Listing. Starting on September 9, these types will be removed from Search Console rich result
    reporting, the Rich Result Test, and the [list of Search appearance filters](https://support.google.com/webmasters/answer/7576553#by_search_appearance&zippy=%2Csearch-appearance)
    (if applicable for the type). The [Search Console API](/webmaster-tools)
    will continue to support these types through December 2025.

    For [bulk data export users](https://support.google.com/webmasters/answer/12918484),
    keep in mind that the deprecated [search appearance fields](https://support.google.com/webmasters/answer/7576553#by_search_appearance&zippy=%2Csearch-appearance)
    will be reported as `NULL` by October 1, 2025. If your queries have conditions, you may need
    to update them.

    For example, the following query should be updated, as it doesn't account for the possibility of
    a deprecated search appearance:

    ```
    SELECT data_date, SUM(clicks) FROM `myproject.searchconsole.searchdata_url_impressions`

    WHERE data_date > DATE('2025-09-01') AND NOT is_learning_videos -- skips rows where is_learning_videos is NULL

    GROUP BY 1;
    ```

    Instead, we recommend using the `IS` operator to write future-proof queries that will
    continue to work even if an appearance becomes `NULL`.

    ```
    SELECT data_date, SUM(clicks) FROM `myproject.searchconsole.searchdata_url_impressions`

    WHERE data_date > DATE('2025-09-01') AND is_learning_videos IS NOT TRUE -- works whether is_learning_videos is false or NULL

    GROUP BY 1;
    ```

    For more information, refer to Google Cloud's
    [BigQuery documentation on the `IS` operator](https://cloud.google.com/bigquery/docs/reference/standard-sql/operators#is_operators).
