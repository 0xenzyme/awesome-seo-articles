---
title: "Testing robots.txt files made easier"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2014-07-testing-robotstxt-files-made-easier"
url: "https://developers.google.com/search/blog/2014/07/testing-robotstxt-files-made-easier"
canonical: "https://developers.google.com/search/blog/2014/07/testing-robotstxt-files-made-easier"
author: "Asaph Arnon"
published: "2014-07-16T00:00:00+00:00"
updated: "2014-07-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:25:09+00:00"
status_code: 200
html_hash: "c4646af78b8ce7664cd384d5a2f223fceebcbb1d5f04a2879364d32ed998bced"
clean_word_count: 407
clean_char_count: 2444
---
# Testing robots.txt files made easier

To crawl, or not to crawl, that is the robots.txt question.

Making and maintaining correct robots.txt files can sometimes be difficult. While most sites have
it easy (tip: they often don't even need a robots.txt file!), finding the rules within a
large robots.txt file that are or were blocking individual URLs can be quite tricky. To make that
easier, we're now announcing an updated
[robots.txt testing tool](https://www.google.com/webmasters/tools/robots-testing-tool)
in Webmaster Tools.

You can find the updated testing tool in
[Webmaster Tools](https://search.google.com/search-console)
within the Crawl section:

![](/static/search/blog/images/import/a07bca2e6fdd2dfb53b8bb39a7d2405e.png)

Here you'll see the current robots.txt file, and can test new URLs to see whether they're
disallowed for crawling. To guide your way through complicated rules, it will highlight the
specific one that led to the final decision. You can make changes in the file and test those too,
you'll just need to upload the new version of the file to your server afterwards to make the
changes take effect. Our developers site has
[more about robots.txt rules and how the files are processed](/search/docs/crawling-indexing/robots/intro).

Additionally, you'll be able to review older versions of your robots.txt file, and see when access
issues block us from crawling. For example, if Googlebot sees a `500` server error for
the robots.txt file, we'll generally pause further crawling of the website.

Since there may be some errors or warnings shown for your existing sites, we recommend
double-checking their robots.txt files. You can also combine it with other parts of Webmaster
Tools: for example, you might use the updated
[Fetch as Google tool](https://support.google.com/webmasters/answer/158587)
to render important pages on your website. If any blocked URLs are reported, you can use this
robots.txt tester to find the rule that's blocking them, and, of course, then improve that.
A common problem we've seen comes from old robots.txt files that block CSS, JavaScript, or mobile
content—fixing that is often trivial once you've seen it.

We hope this updated tool makes it easier for you to test and maintain the robots.txt file. Should
you have any questions, or need help with crafting a good set of rules, you can drop by our
[webmaster's help forum](https://support.google.com/webmasters/go/community)!
