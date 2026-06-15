---
title: "#NoHacked 3.0: Fixing common hack cases"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2017-12-nohacked-30-fixing-common-hack-cases"
url: "https://developers.google.com/search/blog/2017/12/nohacked-30-fixing-common-hack-cases"
canonical: "https://developers.google.com/search/blog/2017/12/nohacked-30-fixing-common-hack-cases"
author: null
published: "2017-12-18T00:00:00+00:00"
updated: "2017-12-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:31:19+00:00"
status_code: 200
html_hash: "ccff09480f682428e46901cd44f1be054ebd841d42ae8d1eb6fad19b74198df0"
clean_word_count: 352
clean_char_count: 2386
---
# #NoHacked 3.0: Fixing common hack cases

So far on [#NoHacked](https://twitter.com/googlesearchc), we have
shared some tips on detection and prevention. Now that you are able to detect hack attack, we
would like to introduce some common hacking techniques and guides on how to fix them!

- [Fixing the Cloaked Keywords and Links Hack](/web/fundamentals/security/hacked/fixing_the_cloaked_keywords_hack)

  ![](/static/search/blog/images/import/14be39d0f8fc1c34e6bd3827ae6fc15e.png)

  The cloaked keywords and link hack automatically creates many pages with nonsensical
  sentences, links, and images. These pages sometimes contain basic template elements from the
  original site, so at first glance, the pages might look like normal parts of the target site
  until you read the content. In this type of attack, hackers usually use cloaking techniques to
  hide the malicious content and make the injected page appear as part of the original site or a
  `404` error page.
- [Fixing the Gibberish Hack](/web/fundamentals/security/hacked/fixing_the_gibberish_hack)

  ![](/static/search/blog/images/import/6b7aad9d4a010bac36aa608097005d81.png)

  The gibberish hack automatically creates many pages with nonsensical sentences filled with
  keywords on the target site. Hackers do this so the hacked pages show up in Google Search.
  Then, when people try to visit these pages, they'll be redirected to an unrelated page, like a
  porn site for example.
- [Fixing the Japanese Keywords Hack](/web/fundamentals/security/hacked/fixing_the_japanese_keyword_hack)

  ![](/static/search/blog/images/import/c8281e86294ff5c3fdcfd2fc0dc0526c.png)

  The Japanese keywords hack typically creates new pages with Japanese text on the target site
  in randomly generated directory names. These pages are monetized using affiliate links to
  stores selling fake brand merchandise and then shown in Google Search. Sometimes the accounts
  of the hackers get added in Search Console as site owners.

Lastly, after you clean your site and fix the problem, make sure to
[file for a reconsideration request](https://support.google.com/webmasters/answer/35843)
to have our teams review your site.

![](/static/search/blog/images/import/d0778a4bb285702e6ce19daf93b37b0a.png)

If you have any questions, post your questions on
[our Webmaster Help Forums](https://support.google.com/webmasters/community/)!
