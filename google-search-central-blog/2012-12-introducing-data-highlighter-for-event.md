---
title: "Introducing Data Highlighter for event data"
source: google-search-central-blog
content_type: "event"
freshness_risk: "historical"
slug: "2012-12-introducing-data-highlighter-for-event"
url: "https://developers.google.com/search/blog/2012/12/introducing-data-highlighter-for-event"
canonical: "https://developers.google.com/search/blog/2012/12/introducing-data-highlighter-for-event"
author: "Justin Boyan"
published: "2012-12-12T00:00:00+00:00"
updated: "2012-12-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:20:46+00:00"
status_code: 200
html_hash: "45bf4aaaeebc2e9252239d719f6bb69b8bbc9a0aa75aad46554e9c6a561c3d33"
clean_word_count: 479
clean_char_count: 3099
---
# Introducing Data Highlighter for event data

At Google we're making more and more use of structured data to provide enhanced search results,
such as
[rich snippets](/search/docs/appearance/structured-data/intro-structured-data)
and
[event calendars](https://support.google.com/websearch/bin/answer.py?answer=2620861),
that help users find your content. Until now, marking up your site's HTML code has been the only
way to indicate structured data to Google. However, we recognize that markup may be hard for some
websites to deploy.

Today, we're offering webmasters a simpler alternative: Data Highlighter. At initial launch,
it's available in English only and for structured data about *events*, such as concerts,
sporting events, exhibitions, shows, and festivals.

We'll make Data Highlighter available for more languages and data types in the months ahead.

**Update 19 February 2013:** Data Highlighter for events structured markup is available in all
languages in Webmaster Tools.

**Update 2:**

You can see the
[full list of schemas supported in Data Highlighter](https://support.google.com/webmasters/topic/2774098?ref_topic=2692946).

Data Highlighter is a point-and-click tool that can be used by anyone authorized for your site in
Google Webmaster Tools. No changes to HTML code are required. Instead, you just use your mouse to
highlight and "tag" each key piece of data on a typical event page of your website:

![Events markup with Data Highlighter](/static/search/blog/images/import/5febb6d7f961bc4f9e200e6b8d7a56e5.png)

If your page lists multiple events in a consistent format, Data Highlighter will "learn" that
format as you apply tags, and help speed your work by automatically suggesting additional tags.
Likewise, if you have many pages of events in a consistent format, Data Highlighter will walk you
through a process of tagging a few example pages so it can learn about their format variations.
Usually, 5 or 10 manually tagged pages are enough for our sophisticated machine-learning
algorithms to understand the other, similar pages on your site.

When you're done, you can review a sample of all the event data that Data Highlighter now
understands. If it's correct, click "Publish."

From then on, as Google crawls your site, it will recognize your latest event listings and make
them eligible for enhanced search results. You can inspect the crawled data on the
[Structured Data Dashboard](/search/blog/2012/07/introducing-structured-data-dashboard),
and unpublish at any time if you're not happy with the results.

Here's a short video explaining how the process works:

To get started with Data Highlighter, visit
[Webmaster Tools](https://search.google.com/search-console),
select your site, click the "Optimization" link in the left sidebar, and click "Data Highlighter".

If you have any questions, please read our
[Help Center article](https://support.google.com/webmasters/bin/answer.py?answer=2692911)
or ask us in the
[Webmaster Help Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:structured_data)).
Happy Highlighting!
