---
title: "New User Agent for News"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-12-new-user-agent-for-news"
url: "https://developers.google.com/search/blog/2009/12/new-user-agent-for-news"
canonical: "https://developers.google.com/search/blog/2009/12/new-user-agent-for-news"
author: "Jonathan Simon"
published: "2009-12-02T00:00:00+00:00"
updated: "2009-12-02T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:03:26+00:00"
status_code: 200
html_hash: "15b2e9c2801fa95b56073e592efa358e87a63f07d90e62da2d72c6628647fed2"
clean_word_count: 695
clean_char_count: 4359
---
# New User Agent for News

Today we are announcing a new user agent for robots.txt called Googlebot-News that gives
publishers even more control over their content. In case you haven't heard of
[robots.txt](/search/docs/crawling-indexing/robots/intro), it's a web-wide standard that has
been in use
[since 1994](https://en.wikipedia.org/wiki/Robots_exclusion_standard)
and which has support from all major search engines and well-behaved "robots" that process the
web. When a search engine checks whether it has permission to crawl and index a web page, the
"check if we're allowed to crawl this page" mechanism is robots.txt.

Publishers could easily contact us
[via a form](https://www.google.com/support/news_pub/bin/answer.py?answer=94003)
if they didn't want to be included in Google News but did want to be in Google's web search index.
Now, publishers can manage their content in Google News in an even more automated way. Site owners
can just add `Googlebot-News` specific rules to their robots.txt file. Similar to
the `Googlebot` and `Googlebot-Image` user agents, the new
`Googlebot-News` user agent can be used to specify which pages of a website should be
crawled and ultimately appear in Google News.

Here are a few examples for publishers:

**Include pages in both Google web search and News:**

```
User-agent: Googlebot
Disallow:
```

This is the easiest case. In fact, a robots.txt file is not even required for this case.

**Include pages in Google web search, but not in News:**

```
User-agent: Googlebot
Disallow:

User-agent: Googlebot-News
Disallow: /
```

This robots.txt file says that no files are disallowed from Google's general web crawler,
called `Googlebot`, but the user agent `Googlebot-News` is blocked from all
files on the website.

**Include pages in Google News, but not Google web search:**

```
User-agent: Googlebot
Disallow: /

User-agent: Googlebot-News
Disallow:
```

When parsing a robots.txt file, Google obeys the most specific rule. The first two lines
tell us that Googlebot (the user agent for Google's web index) is blocked from crawling any pages
from the site. The next rule, which applies to the more specific user agent for Google News,
overrides the blocking of Googlebot and gives permission for Google News to crawl pages from the
website.

**Block different sets of pages from Google web search and Google News:**

```
User-agent: Googlebot
Disallow: /latest_news

User-agent: Googlebot-News
Disallow: /archives
```

The pages blocked from Google web search and Google News can be controlled independently. This
robots.txt file blocks recent news articles (URLs in the /latest\_news folder) from Google web
search, but allows them to appear on Google News. Conversely, it blocks premium content (URLs in
the /archives folder) from Google News, but allows them to appear in Google web search.

**Stop Google web search and Google News from crawling pages:**

```
User-agent: Googlebot
Disallow: /
```

This robots.txt file tells Google that Googlebot, the user agent for our web search crawler,
should not crawl any pages from the site. Because no specific rule for Googlebot-News is
given, our News search will abide by the general guidance for Googlebot and will not crawl pages
for Google News.

For some queries, we display results from Google News in a discrete box or section on the web
search results page, along with our regular web search results. We sometimes do this for Images,
Videos, Maps, and Products, too. This is known as
[Universal search results](https://www.google.com/support/webmasters/bin/answer.py?answer=159206).
Since Google News powers Universal "News" search results, if you block the
`Googlebot-News` user agent then your site's news stories won't be included in
Universal search results.

We are currently testing our support for the new user agent. If you see any problems
[please let us know](https://support.google.com/webmasters/community).
Note that
[it is possible for Google](https://www.youtube.com/watch?v=KBdEwpRQRD0)
to return a link to a page in some situations even when we didn't crawl that page. If you'd like
to
[read more about robots.txt](/search/docs/crawling-indexing/robots/intro), we provide
additional documentation on our website. We hope webmasters will enjoy the flexibility and easier
management that the Googlebot-News user agent provides.
