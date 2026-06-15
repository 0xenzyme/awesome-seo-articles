---
title: "How did you do on the Webmaster Quiz?"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-02-how-did-you-do-on-webmaster-quiz"
url: "https://developers.google.com/search/blog/2010/02/how-did-you-do-on-webmaster-quiz"
canonical: "https://developers.google.com/search/blog/2010/02/how-did-you-do-on-webmaster-quiz"
author: "Charlene Perez"
published: "2010-02-03T00:00:00+00:00"
updated: "2010-02-03T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:04:46+00:00"
status_code: 200
html_hash: "abc27b31640142ba5bd656c297cd736d4662a0c491a0506474113f837c17de14"
clean_word_count: 656
clean_char_count: 3976
---
# How did you do on the Webmaster Quiz?

Thanks to all of you who took our
[webmaster quiz](/search/blog/2010/01/test-your-webmaster-know-how)
and waited patiently to see how well you did! Today, we're pleased to present the
[Webmaster Quiz answers](https://spreadsheets.google.com/pub?key=tdICoB7zY-yl8cSHY9CLyFw&single=true&gid=2&output=html)!
We hope this quiz has provided some clarity on common issues users ask about in the Webmaster
Help Forum. We'll go over a few of the questions and answers here, but if some of the answers
lead you to ask more questions, we encourage you to
[continue the discussion in the forum](https://support.google.com/webmasters/community/thread?tid=714f1d51d53e5747)!

You have moved your site to a new domain name. For users and search engines, the preferred way
to permanently redirect traffic is:
**Correct answer:** a) `301` redirect
**Explanation:** A
[`301` redirect](/search/docs/crawling-indexing/301-redirects)
is preferred because it tells search engines, "Ok, this is the new domain I want you to show to
users from now on," as opposed to something like a `302` redirect, which tells search
engines, "Hey, this is only a temporary redirect—so, uh, I might change the URL soon, okay?"
In addition to implementing a `301` redirect, the
[Change of Address feature](https://www.google.com/support/webmasters/bin/answer.py?answer=83106)
in Webmaster Tools can help Google find your new site.

Your server is going to be moved and unavailable for a day. What should you do?
**Correct answer:** c) Return "Network Unavailable (`503`)" with a helpful message
to all requests
**Explanation:**
Maybe not as commonly known to webmasters, but very useful if your site is down! This tells
crawlers to come back later, rather than crawling and indexing your "Down for maintenance"
pages when you respond with `200` rather than `503`. Check out the Help
Center to learn more about
[HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

Your website is not in the index five days after you've put it online; what should you do?
**Correct answer:** b) Continue working on the site
**Explanation:** This one is a bit tricky. There could be a number of reasons why your site
is not indexed. For example, a site's robots.txt file may contain a rule to inadvertently
block crawlers from searching its contents. But the main take-away from this question is that
if your site is pretty new, it may just be a matter of time before it gets indexed. You should
continue to focus on improving your site for your users.

You need to remove 192 PDF files from the `/private-files/` folder which have gotten
indexed. What's the fastest way to do this?
**Correct answer:** d) Disallow the folder in robots.txt and request removal of the whole
folder in Webmaster Tools.
**Explanation:** Before removing a directory that you don't want indexed, you need to include
the `Disallow` rule in your robots.txt file to tell search bots not to crawl it
anymore.

You have a country-coded domain name called example.es. To associate your site with Spain, you
need to:
**Correct answer:**
c) None of this is necessary. Google should already associate a domain ending in .es with
Spain.
**Explanation:** Some country-coded domains may overlap with international ones, like .tv
—which could also be a site from Tuvalu. But these sort of cases are rare and if they do
arise, don't be shy to seek out help on the
[forum](https://support.google.com/webmasters/community).

Great job to everyone who took the quiz and tested their know-how! And last but certainly not
least, kudos to the top scorers! Congratulations on a quiz well done!

**40/40:**

- ChrisRaimondi
- theopeek
- beussery

**39/40:**

- Petro
- pornel
- Ian Macfarlane
- g1smd
- Mattman
- thinkpragmatic
- GLV
- GoalGorilla
- rssmarketer

**38/40:**

- BartVB
- Kim Minh Kaplan
- Ippi
- Erik Dafforn
- scole01
- Konstantin
- John
- fer.vazquez
- eMBe
- Todd Nemet
- p.jaroszynski
- ph0b
