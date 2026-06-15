---
title: "Authorship markup and web search"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2011-06-authorship-markup-and-web-search"
url: "https://developers.google.com/search/blog/2011/06/authorship-markup-and-web-search"
canonical: "https://developers.google.com/search/blog/2011/06/authorship-markup-and-web-search"
author: "Othar Hansson"
published: "2011-06-07T00:00:00+00:00"
updated: "2011-06-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:13:29+00:00"
status_code: 200
html_hash: "4e3391850152cfe3b2ae5d284854180b41477fc857e40978770a0e4edfc55b90"
clean_word_count: 299
clean_char_count: 1847
---
# Authorship markup and web search

Today we're beginning to support authorship markup—a way to connect authors with their content on
the web. We're experimenting with using this data to help people find content from great authors
in our search results.

We now support markup that enables websites to publicly link within their site from content to
author pages. For example, if an author at The New York Times has written dozens of articles,
using this markup, the webmaster can connect these articles with a New York Times author page.
An author page describes and identifies the author, and can include things like the author's bio,
photo, articles and other links.

If you run a website with authored content, you'll want to learn about authorship markup in our
[Help Center](https://www.google.com/support/webmasters/bin/answer.py?answer=1229920).
The markup uses existing standards such as HTML5 (`rel="author"`) and XFN
(`rel="me"`) to enable search engines and other web services to identify works by the
same author across the web. If you're already doing structured data markup using
[microdata from schema.org](/search/blog/2011/06/introducing-schemaorg-search-engines),
we'll interpret that authorship information as well.

We wanted to make sure the markup was as easy to implement as possible. To that end, we've already
worked with several sites to markup their pages, including The New York Times, The
Washington Post, CNET, Entertainment Weekly, The New Yorker and others. In addition, we've taken
the extra step to add this markup to everything hosted by YouTube and Blogger. In the future,
both platforms will automatically include this markup when you publish content.

We know that great content comes from great authors, and we're looking closely at ways this markup
could help us highlight authors and rank search results.
