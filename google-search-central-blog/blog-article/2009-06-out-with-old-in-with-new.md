---
title: "Out with the old, in with the new"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-06-out-with-old-in-with-new"
url: "https://developers.google.com/search/blog/2009/06/out-with-old-in-with-new"
canonical: "https://developers.google.com/search/blog/2009/06/out-with-old-in-with-new"
author: "Sagar Kamdar, Product Manager, Webmaster Tools Team"
published: "2009-06-11T00:00:00+00:00"
updated: "2009-06-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:58:43+00:00"
status_code: 200
html_hash: "19b077aaacabcff2f85dde4acc344fabc3e2dacad73309965645256525a4e908"
clean_word_count: 451
clean_char_count: 2690
---
# Out with the old, in with the new

We launched a
[preview of our new Webmaster Tools interface three weeks ago](/search/blog/2009/04/spring-time-design-refresh),
and received a lot of valuable feedback. Most of you liked the update, appreciating features such
as the one-stop dashboard, more top search query data, and the improved menu and navigation.

You offered some constructive feedback as well:

- You missed the option to switch listing 25, 50, or 100 rows in features such as links to your
  site. We did not add the option back to select how many rows you would like to see but increased
  our default to 100!
- Top search query information differed between the old and new versions. We expected this since
  we went through a lot of re-engineering to improve the new top search queries backend. We
  reviewed many of the issues posted on our forums, and verified that the new backend is far more
  accurate and reliable.
- Initially, the Sitemaps downloaded and indexed URL counts differed between the two versions. We
  resolved this issue quickly.
- Backlinks numbers between the old and the new user interface (UI) may differ since our new UI
  shows the original anchor (not following redirects) as it's linked on the web. Let's say
  example.com links to https://google.com, then https://google.com `301` redirects to https://www.google.com/:
  - In the new UI—only verified site owners of google.com will see examples.com's
    backlink (because we show the original link prior to any redirects)
  - In the old UI—verified site owners of www.google.com could see example.com's backlink
- The new site switcher lists only five sites, and some of you who manage a large number of sites
  found this limiting. We appreciate the feedback and will work on addressing this limitation in a
  future release.

From today, only the new user interface will be available
(<https://google.com/webmasters/tools>)!
You'll see that in addition to fixing many of the issues users addressed, we took some time to
launch a new feature:
[Change of Address](https://www.google.com/support/webmasters/bin/answer.py?answer=83106).
The Change of Address feature lets you notify Google when you are moving from one domain to
another, enabling us to update our index faster and hopefully creating a smoother transition for
your users.

![the change of address feature in webmaster tools](/static/search/blog/images/archived_changeofaddress.jpg)

Thanks to all the users that took time to give us feedback on the new user interface. To those
users using it for the first time today, we hope you enjoy it. As always,
[your feedback](https://support.google.com/webmasters/community)
is appreciated.
