---
title: "Tips for hosting providers and webmasters"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-12-tips-for-hosting-providers-and"
url: "https://developers.google.com/search/blog/2011/12/tips-for-hosting-providers-and"
canonical: "https://developers.google.com/search/blog/2011/12/tips-for-hosting-providers-and"
author: "Pierre Far"
published: "2011-12-06T00:00:00+00:00"
updated: "2011-12-06T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:17:02+00:00"
status_code: 200
html_hash: "954eb9b06ad7a0d73dfef11937bb578e2fb193a3f0908c8f994279daa441575b"
clean_word_count: 1318
clean_char_count: 8628
---
# Tips for hosting providers and webmasters

Some webmasters on our forums ask about hosting-related issues affecting their sites. To help
both hosting providers and webmasters recognize, diagnose, and fix such problems, we'd like to
share with you some of the common problems we've seen and suggest how you can fix them.

- **Blocking of Googlebot crawling**. This is a very common issue usually due to a
  misconfiguration in a firewall or DoS protection system and sometimes due to the content
  management system the site runs. Protection systems are an important part of good hosting and
  are often configured to block unusually high levels of server requests, sometimes
  automatically.
  Because, however, Googlebot often performs more requests than a human user, these protection
  systems may decide to block Googlebot and prevent it from crawling your website. To check for
  this kind of problem, use the
  [Fetch as Googlebot function](https://www.google.com/support/webmasters/bin/answer.py?answer=158587)
  in Webmaster Tools, and check for other
  [crawl errors](https://support.google.com/webmasters/answer/9679690)
  shown in Webmaster Tools.

  We offer several tools to webmasters and hosting providers who want more control over
  Googlebot's crawling, and to improve crawling efficiency:

- We have detailed help about how you control Googlebot's crawling using the
  [robots exclusion protocol](/search/docs/crawling-indexing/robots/intro) and
  [configuring URL parameters](https://www.google.com/support/webmasters/bin/answer.py?answer=1235687).
- If you're worried about rogue bots using the Googlebot user-agent, we offer a way to
  [verify whether a crawler is actually Googlebot](/search/docs/crawling-indexing/verifying-googlebot).
- If you would like to change how hard Googlebot crawls your site, you can verify your website
  in Webmaster Tools and
  [change Googlebot's crawl rate](https://www.google.com/support/webmasters/bin/answer.py?answer=48620).
  Hosting providers can verify ownership of their IP addresses too.
- We have more information in our
  [crawling and indexing FAQ](/search/help/crawling-index-faq).

- **Availability issues**. A related type of problem we see is websites being
  unavailable when Googlebot (and users) attempt to access the site. This includes DNS issues,
  overloaded servers leading to timeouts and refused connections, misconfigured content
  distribution networks (CDNs), and many other kinds of errors. When Googlebot encounters such
  issues, we report them in Webmaster Tools as either
  [URL unreachable errors](https://www.google.com/support/webmasters/bin/answer.py?answer=35147)
  or
  [crawl errors](https://support.google.com/webmasters/answer/9679690).
- **Invalid SSL certificates**. For SSL certificates to be valid for your website,
  they need to match the name of the site. Common problems include expired SSL certificates and
  servers misconfigured such that all websites on that server use the same certificate. Most web
  browsers will try warn users in these situations, and Google tries to alert webmasters of this
  issue by sending a message via Webmaster Tools. The fix for these problems is to make sure to
  use SSL certificates that are valid for all your website's domains and subdomains your users
  will interact with.
- **Wildcard DNS**. Websites can be configured to respond to all subdomain
  requests. For example, the website at example.com can be configured to respond to requests to
  foo.example.com, made-up-name.example.com and all other subdomains.

  In some cases this is desirable to have; for example, a user-generated content website may
  choose to give each account its own subdomain. However, in some cases, the webmaster may not
  wish to have this behavior as it may cause content to be duplicated unnecessarily across
  different hostnames and it may also affect Googlebot's crawling.

  To minimize problems in wildcard DNS setups, either configure your website to not use them, or
  configure your server to not respond successfully to non-existent hostnames, either by
  refusing the connection or by returning an HTTP `404` header.
- **Misconfigured virtual hosting**. The symptom of this problem is that multiple
  hosts and/or domain names hosted on the same server always return the contents of only one site.
  To rephrase, although the server hosts multiple sites, it returns only one site regardless of
  what is being requested. To diagnose the issue, you need to check that the server responds
  correctly to the `Host` HTTP header.
- **Content duplication through hosting-specific URLs**. Many hosts helpfully offer
  URLs for your website for testing/development purposes. For example, if you're hosting the
  website https://a.com/ on the hosting provider example.com, the host may offer access to your
  site through a URL like https://a.example.com/ or https://example.com/~a/. Our recommendation is
  to have these hosting-specific URLs not publicly accessible (by password protecting them); and
  even if these URLs are accessible, our algorithms usually pick the URL webmasters intend. If
  our algorithms
  [select the hosting-specific URLs](https://www.google.com/support/webmasters/bin/answer.py?answer=1716747&topic=20985),
  you can influence our algorithms to pick your preferred URLs by implementing
  [canonicalization techniques](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  correctly.
- **Soft error pages**. Some hosting providers show error pages using an HTTP
  `200` status code (meaning "Success") instead of an HTTP error status code. For
  example, a "Page not found" error page could return HTTP `200` instead of
  `404`, making it a
  [`soft 404` page](/search/docs/crawling-indexing/troubleshoot-crawling-errors#soft-404-errors);
  or a "Website temporarily unavailable" message might return a `200` instead of
  correctly returning a `503` HTTP status code. We try hard to detect soft error
  pages, but when our algorithms fail to detect a web host's soft error pages, these pages may
  get indexed with the error content. This may cause ranking or
  [cross-domain URL selection](https://www.google.com/support/webmasters/bin/answer.py?answer=1716747&topic=20985)
  issues.

  It's easy to check the status code returned: simply check the HTTP headers the server returns
  using any one of a number of tools, such as
  [Fetch as Googlebot](https://www.google.com/support/webmasters/bin/answer.py?answer=158587).
  If an error page is returning HTTP `200`, change the configuration to return the
  correct HTTP error status code. Also, keep an eye out for `soft 404` reports in Webmaster Tools,
  on the Crawl errors page in the Diagnostics section.
- **Content modification and frames**. Webmasters may be surprised to see their
  page contents modified by hosting providers, typically by injecting scripts or images into the
  page. Web hosts may also serve your content by embedding it in other pages using
  `frame` or `iframe` HTML elements. To check whether a web host is
  changing your content in unexpected ways, simply check the source code of the page as served
  by the host and compare it to the code you uploaded.

  Note that some server-side code modifications may be very useful. For example, a server using
  Google's
  [`mod_pagespeed` Apache module](https://code.google.com/speed/page-speed/docs/module)
  or other tools may be returning your code minified for page speed optimization.
- **Spam and malware**. We've seen some web hosts and bulk subdomain services become
  major sources of malware and spam. We try hard to be granular in our actions when protecting our
  users and search quality, but if we see a very large fraction of sites on a specific web host
  that are spammy or are distributing malware, we may be forced to take action on the web host as
  a whole. To help you keep on top of malware, we offer:

- [Safe Browsing Alerts for Network Administrators](https://googleonlinesecurity.blogspot.com/2010/09/safe-browsing-alerts-for-network),
  useful for hosting providers
- [Malware notifications](/search/docs/monitor-debug/security/malware)
  in Webmaster Tools for individual websites
- A [Safe Browsing API](/safe-browsing) for developers

We hope this list helps both hosting providers and webmasters diagnose and fix these issues.
Beyond this list, also think about the qualitative aspects of hosting like quality of service and
the helpfulness of support. As always, if you have questions or need more help, please ask in our
[Webmaster Help Forum](https://support.google.com/webmasters/community).
