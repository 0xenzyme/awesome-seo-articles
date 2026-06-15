---
title: "Using RSS/Atom feeds to discover new URLs"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2009-10-using-rssatom-feeds-to-discover-new"
url: "https://developers.google.com/search/blog/2009/10/using-rssatom-feeds-to-discover-new"
canonical: "https://developers.google.com/search/blog/2009/10/using-rssatom-feeds-to-discover-new"
author: "Written by Raymond Lo, Guhan Viswanathan, and Dave Weissman, Crawl and Indexing Team"
published: "2009-10-30T00:00:00+00:00"
updated: "2009-10-30T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:01:53+00:00"
status_code: 200
html_hash: "aa9a8a91225c0e620b64ad7ed043d999d022b11d834b43c9a3642c9bafcad070"
clean_word_count: 224
clean_char_count: 1346
---
# Using RSS/Atom feeds to discover new URLs

Google uses numerous sources to find new webpages, from links we find on the web to
[submitted URLs](https://www.google.com/addurl/). We aim to
discover new pages quickly so that users can find new content in Google search results soon after
they go live. We recently launched a feature that uses RSS and Atom feeds for the discovery of
new webpages.

RSS/Atom feeds have been very popular in recent years as a mechanism for content publication.
They allow readers to check for new content from publishers. Using feeds for discovery allows us
to get these new pages into our index more quickly than traditional crawling methods. We may use
many potential sources to access updates from feeds including Reader, notification services, or
direct crawls of feeds. Going forward, we might also explore mechanisms such as
[PubSubHubbub](https://code.google.com/p/pubsubhubbub/)
to identify updated items.

In order for us to use your RSS/Atom feeds for discovery, it's important that crawling these files
is not disallowed by your [robots.txt](/search/docs/crawling-indexing/robots/intro).
To find out if Googlebot can crawl your feeds and find your pages as fast as possible, test your
feed URLs with the
[robots.txt tester in Google Webmaster Tools](https://support.google.com/webmasters/answer/6062598).
