---
title: "Accessing search query data for your sites"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-10-accessing-search-query-data-for-your"
url: "https://developers.google.com/search/blog/2011/10/accessing-search-query-data-for-your"
canonical: "https://developers.google.com/search/blog/2011/10/accessing-search-query-data-for-your"
author: "Anthony Chavez, Product Manager"
published: "2011-10-18T00:00:00+00:00"
updated: "2011-10-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:15:30+00:00"
status_code: 200
html_hash: "f9ec40bb7d5e18aa231381e45bf2a28a117441e8e606c60b1fdbf10278ccb3f2"
clean_word_count: 413
clean_char_count: 2716
---
# Accessing search query data for your sites

SSL encryption on the web has
[been](https://googleblog.blogspot.com/2010/05/search-more-securely-with-encrypted.html)
[growing](https://gmailblog.blogspot.com/2010/01/default-https-access-for-gmail.html)
[by](https://blog.facebook.com/blog.php?post=486790652130)
[leaps](https://www.eff.org/https-everywhere)
[and](https://blog.wikimedia.org/2011/10/03/native-https-support-enabled-for-all-wikimedia-foundation-wikis/)
[bounds](https://blog.twitter.com/2011/03/making-twitter-more-secure-https).
As part of our commitment to provide a more secure online experience, today we announced that SSL
Search on
[https://www.google.com](https://www.google.com/)
will become the
[default experience for signed in users](https://googleblog.blogspot.com/2011/10/making-search-more-secure)
on google.com. This change will be rolling out over the next few weeks.

What is the impact of this change for webmasters? Today, a web site accessed through organic
search results on
[https://www.google.com](https://www.google.com/)
(non-SSL) can see both that the user came from
[google.com](https://www.google.com/)
and their search query. (Technically speaking, the user's browser passes this information via the
[HTTP referrer field](https://en.wikipedia.org/wiki/HTTP_referrer).)
However, for organic search results on SSL search, a web site will only know that the user came
from
[google.com](https://www.google.com/).

Webmasters can still access a
[wealth of search query data](https://www.google.com/support/webmasters/bin/answer.py?answer=35252)
for their sites via
[Webmaster Tools](https://search.google.com/search-console).
For sites which have been
[added and verified in Webmaster Tools](https://support.google.com/webmasters/answer/34592),
webmasters can do the following:

- View the top 1000 daily search queries and top 1000 daily landing pages for the past 30 days.
- View the impressions, clicks, clickthrough rate (CTR), and average position in search results
  for each query, and compare this to the previous 30 day period.
- Download this data in CSV format.

In addition, users of
[Google Analytics](https://www.google.com/analytics/)'
Search Engine Optimization reports have access to the
[same search query data available in Webmaster Tools](/search/blog/2011/10/webmaster-tools-search-queries-data-is)
and can take advantage of its rich reporting capabilities.

We will continue to look into further improvements to how search query data is surfaced through
Webmaster Tools. If you have questions, feedback or suggestions, please let us know through the
[Webmaster Tools Help Forum](https://support.google.com/webmasters/community/thread?tid=6e82ce3ec2a33b60).
