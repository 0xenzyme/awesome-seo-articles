---
title: "Crawling through HTML forms"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-04-crawling-through-html-forms"
url: "https://developers.google.com/search/blog/2008/04/crawling-through-html-forms"
canonical: "https://developers.google.com/search/blog/2008/04/crawling-through-html-forms"
author: "Written by Jayant Madhavan and Alon Halevy, Crawling and Indexing Team"
published: "2008-04-11T00:00:00+00:00"
updated: "2008-04-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:52:08+00:00"
status_code: 200
html_hash: "142597d8f9da3d0c575675b62a46c834183e3532fa1e96f6b0e4d438b59bad90"
clean_word_count: 543
clean_char_count: 3149
---
# Crawling through HTML forms

Google is constantly trying new ideas to improve our coverage of the web. We already do some
pretty smart things like scanning JavaScript and Flash to discover links to new web pages, and
today, we would like to talk about another new technology we've started experimenting with
recently.

In the past few months we have been exploring some HTML forms to try to discover new web pages and
RLs that we otherwise couldn't find and index for users who search on Google. Specifically, when
we encounter a `<form>` element on a high-quality site, we might choose to do a
small number of queries using the form. For text boxes, our computers automatically choose words
from the site that has the form; for
select menus, check boxes, and radio buttons on the form, we choose from among the values of
the HTML. Having chosen the values for each input, we generate and then try to crawl URLs that
correspond to a possible query a user may have made. If we ascertain that the web page resulting
from our query is valid, interesting, and includes content not in our index, we may include it
in our index much as we would include any other web page.

Needless to say, this experiment follows good Internet citizenry practices. Only a small number of
particularly useful sites receive this treatment, and our crawl agent, the
[ever-friendly Googlebot](/search/blog/2008/03/first-date-with-googlebot-headers-and),
always adheres to robots.txt, `nofollow`, and `noindex` rules. That means that if a search
form is forbidden in robots.txt, we won't crawl any of the URLs that a form would generate.
Similarly, we only retrieve `GET` forms and avoid forms that require any kind of user
information. For example, we omit any forms that have a password input or that use terms commonly
associated with personal information such as logins, userids, contacts, etc. We are also mindful
of the impact we can have on web sites and limit ourselves to a very small number of fetches for a
given site.

The web pages we discover in our enhanced crawl do not come at the expense of regular web pages that
are already part of the crawl, so this change doesn't reduce PageRank for your other pages. As
such it should only increase the exposure of your site in Google. This change also does not
affect the crawling, ranking, or selection of other web pages in any significant way.

This experiment is part of Google's broader effort to increase its coverage of the web. In fact,
HTML forms have long been thought to be the gateway to large volumes of data beyond the normal
scope of search engines. The terms Deep Web, Hidden Web, or
[Invisible Web](https://www.amazon.com/Invisible-Web-Uncovering-Information-Sources/dp/091096551X/ref=sr_1_1?ie=UTF8&s=books&qid=1207179068)
have been used collectively to refer to such content that has so far been invisible to search
engine users. By crawling using HTML forms (and abiding by robots.txt), we are able to lead
search engine users to documents that would otherwise not be easily found in search engines, and
provide webmasters and users alike with a better and more comprehensive search experience.
