---
title: "How to use robots.txt"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2008-03-how-to-use-robotstxt"
url: "https://developers.google.com/search/blog/2008/03/how-to-use-robotstxt"
canonical: "https://developers.google.com/search/blog/2008/03/how-to-use-robotstxt"
author: "By Chao Ma, In Hyuk Seok"
published: "2008-03-01T00:00:00+00:00"
updated: "2008-03-01T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:51:50+00:00"
status_code: 200
html_hash: "81c75ab2c4650ae52ac9e6b8123dba9d1dee704b08979e7e7fe89635205fbf7a"
clean_word_count: 659
clean_char_count: 3986
---
# How to use robots.txt

A [robots.txt](https://www.robotstxt.org/)
provides restrictions to search engine robots (known as "bots") that crawl the web. These bots are
automated, and before they access pages of a site, they check to see if a robots.txt file exists
that prevents them from accessing certain pages. If you want to protect some of your contents
from being indexed by search engines, robots.txt is a simple tool for it. In this time, we would
like to discuss how to use it.

## Placing Robots.txt

The robots.txt file is a text file, with one or more records. The robots.txt file must be reside
in the root of the domain and must be exactly named robots.txt. A robots.txt file located in a
subdirectory is not a valid, as bots only check for this file in the root of the domain.

For instance,
`https://www.example.com/robots.txt` is a valid location. But,
`https://www.example.com/mysite/robots.txt` is not.

Example of a robots.txt:

```
User-agent:*
Disallow: /cgi-bin/
Disallow: /tmp/
Disallow: /~name/
```

## Block or remove your entire website using a robots.txt file

To remove your site from search engines and prevent all robots from crawling it in the future,
place the following robots.txt file in your server root:

```
User-agent: *
Disallow: /
```

To remove your site from Google only and prevent just Googlebot from crawling your site in the
future, place the following robots.txt file in your server root:

```
User-agent: Googlebot
Disallow: /
```

Each port must have its own robots.txt file. In particular, if you serve content via both http
and https, you'll need a separate robots.txt file for each of these protocols. For example, to
allow Googlebot to index all http pages but no https pages, you'd use the robots.txt files below.

For your http protocol (`https://example.com/robots.txt`):

```
User-agent: *
Allow: /
```

For the https protocol (`https://yourserver.com/robots.txt`):

```
User-agent: *
Disallow: /
```

Allow all robots complete access

```
User-agent: *
Disallow:
```

(alternative solution: Just create an empty "/robots.txt" file, or don't use one at all.)

## Block or remove pages using a robots.txt file

You can use a robots.txt file to block Googlebot from crawling pages on your site.

For example, if you're manually creating a robots.txt file, to block Googlebot from crawling all
pages under a particular directory (for example, private), you'd use the following robots.txt
entry:

```
User-agent: Googlebot
Disallow: /private
```

To block Googlebot from crawling all files of a specific file type (for example, .gif), you'd use
the following robots.txt entry:

```
User-agent: Googlebot
Disallow: /*.gif$
```

To block Googlebot from crawling any URL that includes a `?` (more specifically, any
URL that begins with your domain name, followed by any string, followed by a question mark,
followed by any string):

```
User-agent: Googlebot
Disallow: /*?
```

While we won't crawl or index the content of pages blocked by robots.txt, we may still crawl and
index the URLs if we find them on other pages on the web. As a result, the URL of the page or
other publicly available information such as anchor text in links to the site can appear in
Google search results. However, no content from your pages will be crawled, indexed, or displayed.

As a part of webmaster tool, Google provides
[robots.txt analysis tool](https://www.google.com/support/webmasters/bin/answer.py&answer=35237).
The tool reads the robots.txt file in the same way Googlebot does and gives you results for
Google user-agents. We strongly suggest to use it. Before creating robots.txt, you should think
about how much information you want to share with people, or to keep private. Remember that search
engine is a good way to have your contents publicly more accessible. By using robots.txt properly,
people will be happy to visit your website through search engine but meanwhile you can still
prevent your private information from being exposed.
