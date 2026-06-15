---
title: "Google's robots.txt parser is now open source"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2019-07-repp-oss"
url: "https://developers.google.com/search/blog/2019/07/repp-oss"
canonical: "https://developers.google.com/search/blog/2019/07/repp-oss"
author: "Edu Pereda, Lode Vandevenne, Gary Illyes"
published: "2019-07-01T00:00:00+00:00"
updated: "2019-07-01T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:34:39+00:00"
status_code: 200
html_hash: "5a00e52d7444dbbea3636c706c472927710e38f0ab00d3fd20be861ac990a999"
clean_word_count: 335
clean_char_count: 2023
---
# Google's robots.txt parser is now open source

For 25 years, the [Robots Exclusion Protocol (REP)](https://www.robotstxt.org/norobots-rfc.txt)
was only a de-facto standard. This had frustrating implications sometimes. On one hand, for
webmasters, it meant uncertainty in corner cases, like when their text editor included
[BOM](https://en.wikipedia.org/wiki/Byte_order_mark) characters in
their robots.txt files. On the other hand, for crawler and tool developers, it also brought
uncertainty; for example, how should they deal with robots.txt files that are hundreds of
megabytes large?

![Googlebot unboxing a website](/static/search/blog/images/import/6226c69ab2a45ed52a0a7cb7289d02f4.png)

Today, [we announced](/search/blog/2019/07/rep-id) that we're spearheading the effort
to make the REP an internet standard. While this is an important step, it means extra work for
developers who parse robots.txt files.

We're here to help: we [open sourced](https://github.com/google/robotstxt)
the C++ library that our production systems use for parsing and matching rules in robots.txt
files. This library has been around for 20 years and it contains pieces of code that were written
in the 90's. Since then, the library evolved; we learned a lot about how webmasters write
robots.txt files and corner cases that we had to cover for, and added what we learned over the
years also to the internet draft when it made sense.

We also included a testing tool in the open source package to help you test a few rules. Once
built, the usage is very straightforward:

`robots_main <robots.txt content> <user_agent> <url>`

If you want to check out the library, head over to our GitHub repository for the
[robots.txt parser](https://github.com/google/robotstxt). We'd love
to see what you can build using it! If you built something using the library, drop us a comment on
[Twitter](https://twitter.com/googlesearchc), and if you have comments
or questions about the library, find us on
[GitHub](https://github.com/google/robotstxt).
