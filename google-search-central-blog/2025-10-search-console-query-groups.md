---
title: "Introducing Query groups in Search Console Insights"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "low"
slug: "2025-10-search-console-query-groups"
url: "https://developers.google.com/search/blog/2025/10/search-console-query-groups"
canonical: "https://developers.google.com/search/blog/2025/10/search-console-query-groups"
author: "Moshe Samet"
published: "2025-10-27T00:00:00+00:00"
updated: "2025-10-27T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:45:38+00:00"
status_code: 200
html_hash: "5052577b6cb51e8f0dd36b6049c56ee2abc6975133a235bc40f37f6e27e20f78"
clean_word_count: 509
clean_char_count: 3294
---
# Introducing Query groups in Search Console Insights

We are excited to announce [Query groups](https://support.google.com/webmasters/answer/16308503#query-groups),
a powerful Search Console Insights feature that groups similar search queries.

One of the challenges when analyzing search performance data is that there are many different ways to write
the same query: you might see a dozen different variations for a single user question - including common misspellings,
slightly different phrasing, and different languages.

For example, here are a few different ways to search for the same thing - "how to make guacamole dip?":

- how to make guacamole dip
- recipe for guacamole dip
- guacamole dip recipe
- guac dip recipe
- easy guacamole dip recipe
- simple guacamole dip recipe
- guacamole dip recipe easy
- how to make guacamole dip easy

While these are distinct queries, they reflect a similar user intent. The volume of these variations
makes it tedious to identify the main user interest and plan content strategically.

Query groups solve this problem by grouping similar queries. Instead of a long, cluttered list of individual
queries, you will now see lists of queries representing the main groups that interest your audience. The groups
are computed using AI; they may evolve and change over time. They are designed for providing a better high level
perspective of your queries and don't affect ranking.

![Search Console Insights report with query groups](/static/search/blog/images/search-console-query-groups.png)

The new **Queries leading to your site** card in the Insights report offers a better organized summary:

- **Group performance:** You will see the total clicks for the entire group, giving you
  the overall group's performance.
- **Queries list:** A list of the queries that belong to this group ordered by clicks
  (this list may be truncated). The query with the largest number of clicks will appear first and help
  quickly identify the group.
- **Drill-down:** You can click any group and be directed to the performance
  report to see all the individual, granular queries that make up that group and further analyze them.

The card also groups your website queries using three variations:

- **Top**: The groups with the highest click volume.
- **Trending up**: The groups where clicks increased the most compared to the previous period.
- **Trending down**: The groups where clicks decreased the most compared to the previous period.

This feature will be **rolling out gradually** over the coming weeks, and it'll be available as
a new card in [the Search Console Insights report](https://search.google.com/search-console/performance/insights).
Query groups are available only to properties that have a large volume of queries, as the need to group queries
is less relevant for sites with fewer queries.

We encourage you to explore the new feature and tell us what you think. Make sure to provide feedback through the
thumbs up and thumbs down available in the cards and, if needed, with **Submit feedback**.
You can also share your comments on [LinkedIn](https://www.linkedin.com/showcase/googlesearchcentral/)
or post in the [Google Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)).
