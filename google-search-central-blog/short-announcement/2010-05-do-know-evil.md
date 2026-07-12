---
title: "Do know evil"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2010-05-do-know-evil"
url: "https://developers.google.com/search/blog/2010/05/do-know-evil"
canonical: "https://developers.google.com/search/blog/2010/05/do-know-evil"
author: "Bruce Leban, Software Engineer"
published: "2010-05-04T00:00:00+00:00"
updated: "2010-05-04T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:06:25+00:00"
status_code: 200
html_hash: "dc54d030b92fa15ece958165734134060db09c892dfc4d50e1092a8d6f7cbea5"
clean_word_count: 332
clean_char_count: 2259
---
# Do know evil

*Cross-posted on the
[Google Online Security Blog](https://googleonlinesecurity.blogspot.com/2010/05/do-know-evil-web-application)*

We want Googlers to have a firm understanding of the threats our services face, as well as how to
help protect against those threats. We work toward these goals in a variety of ways, including
security training for new engineers, technical presentations about security, and other types of
documentation. We also use codelabs—interactive programming tutorials that walk participants
through specific programming tasks.

One codelab in particular teaches developers about common types of web application
vulnerabilities. In the spirit of the thinking that "it takes a hacker to catch a hacker," the
codelab also demonstrates how an attacker could exploit such vulnerabilities.

We're releasing this codelab, entitled "Web Application Exploits and Defenses," today in
coordination with
[Google Code University](https://code.google.com/edu) and
[Google Labs](https://www.googlelabs.com/)
to help software developers better recognize, fix, and avoid similar flaws in their own
applications. The codelab is built around Gruyere, a small yet full-featured microblogging
application designed to contain lots of security bugs. The vulnerabilities covered by the lab
include cross-site scripting (XSS), cross-site request forgery (XSRF) and cross-site script
inclusion (XSSI), as well as client-state manipulation, path traversal and AJAX and configuration
vulnerabilities. It also shows how simple bugs can lead to information disclosure,
denial-of-service and remote code execution.

The maxim, "given enough eyeballs, all bugs are shallow" is only true if the eyeballs know what to
look for. To that end, the security bugs in Gruyere are real bugs—just like those in many
other applications. The Gruyere source code is published under a Creative Commons license and is
available for use in whitebox hacking exercises or in computer science classes covering security,
software engineering or general software development.

To get started, visit
<https://google-gruyere.appspot.com/>.
An instructor's guide for using the codelab is now available on
[Google Code University](https://code.google.com/edu/security/index).
