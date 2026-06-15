---
title: "Issues with the site: operator query"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-05-issues-with-site-operator-query"
url: "https://developers.google.com/search/blog/2006/05/issues-with-site-operator-query"
canonical: "https://developers.google.com/search/blog/2006/05/issues-with-site-operator-query"
author: "Vanessa Fox"
published: "2006-05-19T00:00:00+00:00"
updated: "2006-05-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:45:31+00:00"
status_code: 200
html_hash: "a4a6362b7c89d0e735f6038969b2d3096feb38c8b836b05bfff853879cd19ad8"
clean_word_count: 298
clean_char_count: 1733
---
# Issues with the site: operator query

We'd like to give you all a quick update on some of the issues you have been seeing when you do a
`site:` search to see how many pages of your site are in the index. We've been
refreshing our supplemental results (you can read more about that in
[Matt Cutts'
blog post](https://www.mattcutts.com/blog/indexing-timeline/)) and this refresh has involved some serious changes under the hood. Unfortunately,
with change of this scale, there sometimes are bugs. In this case, we found a few bugs that
affected the site: operator. Some particular ones you may have noticed are that the following
types of queries don't return the correct number of results:

- `site:` queries where you type in a trailing slash
  (such as `site:www.example.com/`)
- `site:` queries for a domain with punctuation (such as
  `site: www.example-site.com`)

We've got fixes for all of these rolling out in the next few days. They didn't come out sooner
because we've been testing them thoroughly, making sure you don't get any unexpected surprises.

This bug doesn't involve any pages being dropped from the index. It's the `site:`
operator that isn't working properly. We're freezing all refreshes of the supplemental results
until these issues are fixed, and things should be back to normal in a few days. We'll keep you
posted when all fixes have been made.

In the meantime, site: queries without the trailing slash may provide a better result (such as
`site:www.example.com`). If you are checking your site using the Index Stats page of
Google Sitemaps, note that it uses the trailing slash in the query, so you may see incorrect
results until this bug is fixed.

Thanks for your patience as we resolve this issue.
