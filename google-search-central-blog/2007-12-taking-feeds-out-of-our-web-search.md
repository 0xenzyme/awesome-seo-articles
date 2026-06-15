---
title: "Taking feeds out of our web search results"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2007-12-taking-feeds-out-of-our-web-search"
url: "https://developers.google.com/search/blog/2007/12/taking-feeds-out-of-our-web-search"
canonical: "https://developers.google.com/search/blog/2007/12/taking-feeds-out-of-our-web-search"
author: "Written by Bogdan Stănescu, Software Engineer"
published: "2007-12-18T00:00:00+00:00"
updated: "2007-12-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:51:10+00:00"
status_code: 200
html_hash: "82ceccb1823d964d830d738dcec00fd24ff5fe89745572114a1193e2520ed8fa"
clean_word_count: 313
clean_char_count: 1891
---
# Taking feeds out of our web search results

As a webmaster, you may have been concerned about your RSS/Atom feeds crowding out their
associated HTML pages in Google's search results. By serving feeds, we could cause a poor user
experience:

1. Feeds increase the likelihood that users see duplicate search results.
2. Users clicking on a feed may miss valuable content available only in the HTML page.

To address these concerns, we prevent feeds from being returned in Google's search results, with
the exception of podcasts (feeds with multimedia enclosures). We continue to allow podcasts,
because we noticed a significant number of them are standalone documents (that is, no HTML page
has the same content) or they have more complete item descriptions than the associated HTML page.
However, if, as a webmaster, you'd like your podcasts to be excluded from Google's search results
(for example, if you have a vlog, its feed is probably a podcast), you can use
[Yahoo's spec for noindex feeds](https://publisher.yahoo.com/rss_guide/faq.php).
If you use [FeedBurner](https://www.feedburner.com/), making your
podcast `noindex` is as simple as checking a box ("Noindex" under the "Publicize" tab).

As a user, you may ask yourself whether Google has a way to search for feeds. The answer is yes;
both [Google Reader](https://www.google.com/reader/) and
[iGoogle](https://www.google.com/ig) allow searching for feeds to
subscribe to.

We're aware that there are a few non-podcast feeds out there with no associated HTML pages, and
thus removing these feeds for now from the search results might be less than ideal. We remain open
to other feedback on how to improve the handling of feeds, and especially welcome your comments
and questions in the
[Crawling, Indexing and Ranking](https://groups.google.com/group/Google_Webmaster_Help-Indexing/topics)
subtopic of our Webmaster Help Group.
