---
title: "New open source robots.txt projects"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2020-09-new-open-source-robotstxt-projects"
url: "https://developers.google.com/search/blog/2020/09/new-open-source-robotstxt-projects"
canonical: "https://developers.google.com/search/blog/2020/09/new-open-source-robotstxt-projects"
author: "Edu Pereda, Gary Illyes"
published: "2020-09-21T00:00:00+00:00"
updated: "2020-09-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:37:37+00:00"
status_code: 200
html_hash: "09f2e6ce16bcc4ac84c904bc568f50bee644976d65347fb1fcb675bcd01fdaf0"
clean_word_count: 475
clean_char_count: 2887
---
# New open source robots.txt projects

Last year we released the
[robots.txt parser and matcher](https://github.com/google/robotstxt) that we use in
our production systems to the open source world. Since then, we've seen people build new tools
with it,
[contribute](https://github.com/google/robotstxt/pulls?q=is%3Apr+is%3Amerged) to the
open source library (effectively improving our production systems- thanks!), and release new
language versions like [golang](https://github.com/google/robotstxt/issues/29) and
[rust](https://github.com/google/robotstxt/issues/31), which make it easier for
developers to build new tools.

With the intern season ending here at Google, we wanted to highlight two new releases related to
robots.txt that were made possible by two interns working on the Search Open Sourcing team,
[Andreea Dutulescu](https://www.linkedin.com/in/andreea-nicoleta-dutulescu) and
[Ian Dolzhanskii](https://www.linkedin.com/in/ian-dolzhanskiy-6297a119b/).

## Robots.txt Specification Test

First, we are releasing a
[testing framework](https://github.com/google/robotstxt-spec-test/) for robots.txt
parser developers, created by Andreea. The project provides a testing tool that can validate
whether a robots.txt parser follows the Robots Exclusion Protocol, or to what extent. Currently
there is no official and thorough way to assess the correctness of a parser, so Andreea built a
tool that can be used to create robots.txt parsers that are following the protocol.

## Java robots.txt parser and matcher

Second, we are releasing an official
[Java port of the C++ robots.txt parser](https://github.com/google/robotstxt-java),
created by Ian. Java is the
[3rd most popular programming language](https://madnight.github.io/githut/#/pull_requests/2020/2)
on GitHub and it's extensively used at Google as well, so no wonder it's been the most requested
language port. The parser is a 1-to-1 translation of the C++ parser in terms of functions and
behavior, and it's been thoroughly tested for parity against a large corpora of robots.txt
rules. Teams are already planning to use the Java robots.txt parser in Google production
systems, and we hope that you'll find it useful, too.

As usual, we welcome your contributions to these projects. If you built something with the
[C++ robots.txt parser](https://github.com/google/robotstxt) or with these new
releases, let us know so we can potentially help you spread the word! If you found a bug, help
us fix it by opening an issue on GitHub or directly contributing with a pull request. If you
have questions or comments about these projects, catch us on
[Twitter](https://twitter.com/googlesearchc)!

It was our genuine pleasure to host Andreea and Ian, and we're sad that their internship is
ending. Their contributions help make the Internet a better place and we hope that we can
welcome them back to Google in the future.
