---
title: "Robots Refresher: Future-proof Robots Exclusion Protocol"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "low"
slug: "2025-03-robots-future"
url: "https://developers.google.com/search/blog/2025/03/robots-future"
canonical: "https://developers.google.com/search/blog/2025/03/robots-future"
author: "Gary Illyes"
published: "2025-03-28T00:00:00+00:00"
updated: "2025-03-28T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:44:51+00:00"
status_code: 200
html_hash: "92a163c454afce6324843eb9eed15b28a6f7b1a806996fb72e2cb5395801b75d"
clean_word_count: 630
clean_char_count: 3759
---
# Robots Refresher: Future-proof Robots Exclusion Protocol

In the previous posts about the Robots Exclusion Protocol (REP), we explored what you can already
do with its various components — namely robots.txt and the URI level controls.
In this post we will explore how the REP can play a supporting role in the ever-evolving relation
between automatic clients and the human web.

The REP — specifically robots.txt — became a standard in 2022 as
[RFC9309](https://datatracker.ietf.org/doc/html/rfc9309).
However, the heavy lifting was done prior to its standardization: it was the test of time between
1994 and 2022 that made it popular enough to be adopted by billions of hosts and virtually all
major crawler operators (excluding adversarial crawlers such as malware scanners). It is a
straightforward and elegant solution to express preferences with a simple yet versatile syntax.
In its 25 years of existence it barely had to evolve from its original form, it only got an
`allow` rule if we only consider the rules that are universally supported by crawlers.

That doesn't mean that there are no other rules; any crawler operator can come up with their own
rules. For example, rules like "`clean-param`" and "`crawl-delay`" are not
part of RFC9309, but they're supported by some search engines — though not Google Search.
The "`sitemap`" rule, which again is not part of RFC9309, is supported by all major
search engines. Given enough support, it could become an official rule in the REP.

Because the REP can in fact get "updates". It's a widely supported protocol and it should grow
with the internet. Making changes to it is not impossible, but it's not easy; it shouldn't be
easy, exactly because the REP is widely supported. Like with any change to a standard, there has
to be a consensus that changes benefit the majority of the users of the protocol, both on the
publishers' and the crawler operators' side.

Due to its simplicity and wide adoption, the REP is an excellent candidate for carrying new
crawling preferences: billions of publishers are already familiar with robots.txt and its syntax
for example, so making changes to it comes more naturally for them. On the flip side, crawler
operators already have robust, well tested parsers and matchers (and Google also open sourced its
own [robots.txt parser](https://github.com/google/robotstxt)),
which means it's highly likely that there won't be parsing issues with new rules.

The same goes for the REP URI level extensions, the `X-robots-tag` HTTP header and its
meta tag counterpart. If there is a need for a new rule to carry opt-out preferences, they're
easily extensible. How though?

The most important thing you, the reader, can do is to talk about your idea publicly and gather
supporters for that idea. Because the REP is a public standard, no one entity can make unilateral
changes to it; sure, they can implement support for something new on their side, but that won't
become THE standard. But talking about that change and showing to the ecosystem — both
crawler operators and the publishing ecosystem — that it's benefiting everyone will drive
consensus, and that paves the road to updating the standard.

Similarly, if the protocol is lacking something, talk about it publicly. `sitemap`
became a widely supported rule in robots.txt because it was useful for content creators and search
engines alike, which paved the road to adoption of the extension. If you have a new idea for a
rule, ask the consumers of robots.txt and creators what they think about it and work with them to
hash out potential (and likely) issues they raise and write up a proposal.

If your driver is to serve the common good, it's worth it.

---

## Check out the rest of the Robots Refresher series:
