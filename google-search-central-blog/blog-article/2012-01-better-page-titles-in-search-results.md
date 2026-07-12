---
title: "Better page titles in search results"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-01-better-page-titles-in-search-results"
url: "https://developers.google.com/search/blog/2012/01/better-page-titles-in-search-results"
canonical: "https://developers.google.com/search/blog/2012/01/better-page-titles-in-search-results"
author: "Pierre Far"
published: "2012-01-12T00:00:00+00:00"
updated: "2012-01-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:17:12+00:00"
status_code: 200
html_hash: "ff2d81066d85fd0961d3ccb280b8d4a6f710787dd6338d37fc1e9bd394abd84e"
clean_word_count: 363
clean_char_count: 2189
---
# Better page titles in search results

Page titles are an important part of our search results: they're the first line of each result
and they're the actual links our searchers click to reach websites. Our advice to webmasters
has always been to write unique, descriptive page titles (and meta descriptions for the snippets)
to describe to searchers what the page is about.

We use many signals to decide which title to show to users, primarily the `<title>`
tag if the webmaster specified one. But for some pages, a single title might not be the best one
to show for all queries, and so we have algorithms that generate alternative titles to make it
easier for our users to recognize relevant pages. Our testing has shown that these alternative
titles are generally more relevant to the query and can substantially improve the clickthrough
rate to the result, helping both our searchers and webmasters. About half of the time, this is
the reason we show an alternative title.

Other times, alternative titles are displayed for pages that have no title or a non-descriptive
title specified by the webmaster in the HTML. For example, a title using simply the word "Home"
is not really indicative of what the page is about. Another common issue we see is when a
webmaster uses the same title on almost all of a website's pages, sometimes exactly duplicating
it and sometimes using only minor variations. Lastly, we also try to replace unnecessarily long
or hard-to-read titles with more concise and descriptive alternatives.

For more information about how you can write better titles and meta descriptions, and to learn
more about the signals we use to generate alternative titles, we've recently updated the
[Help Center article on this topic](/search/docs/advanced/appearance/good-titles-snippets).
Also, we try to notify webmasters when we discover titles that can be improved on their websites
through the HTML Suggestions feature in Webmaster Tools; you can find this feature in the
Diagnostics section of the menu on the left hand side.

As always, if you have any questions or feedback, please tell us in the
[Webmaster Help Forum](https://support.google.com/webmasters/community).
