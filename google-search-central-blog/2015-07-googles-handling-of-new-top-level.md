---
title: "Google's handling of new top level domains"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-07-googles-handling-of-new-top-level"
url: "https://developers.google.com/search/blog/2015/07/googles-handling-of-new-top-level"
canonical: "https://developers.google.com/search/blog/2015/07/googles-handling-of-new-top-level"
author: "John Mueller"
published: "2015-07-21T00:00:00+00:00"
updated: "2015-07-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:27:02+00:00"
status_code: 200
html_hash: "4bb34a51774fa54fc477be7fdf17ab40ae5483b7f1d6931f175ddd5bf44bb04e"
clean_word_count: 593
clean_char_count: 3562
---
# Google's handling of new top level domains

With the coming of many new generic top level domains
([gTLDs](https://en.wikipedia.org/wiki/Generic_top-level_domain)),
we'd like to give some insight into how these are handled in Google's search. We've heard and seen
questions and misconceptions about the way we treat new top level domains (TLDs), like .guru,
.how, or any of the .BRAND gTLDs, for example:

**Q: How will new gTLDs affect search? Is Google changing the search algorithm to favor these
TLDs? How important are they really in search?**
A: Overall, our systems treat new gTLDs like other gTLDs (like .com and .org). Keywords in a TLD
do not give any advantage or disadvantage in search.

**Q: What about
[IDN](https://en.wikipedia.org/wiki/Internationalized_domain_name)
TLDs such as .みんな? Can Googlebot crawl and index them, so that
they can be used in search?**
A: Yes. These TLDs can be used the same as other TLDs (it's easy to check with a query like
site:みんな). Google treats the Punycode version of a hostname as
being equivalent to the unencoded version, so you don't need to redirect or canonicalize them
separately. For the rest of the URL, remember to use UTF-8 for the path and query-string in the
URL, when using non-ASCII characters.

**Q: Will a .BRAND TLD be given any more or less weight than a .com?**
A: No. Those TLDs will be treated the same as a other gTLDs. They will require the same
geotargeting settings and configuration, and they won't have more weight or influence in the way
we crawl, index, or rank URLs.

**Q: How are the new region or city TLDs (like .london or .bayern) handled?**
A: Even if they look region-specific, we will treat them as gTLDs. This is consistent with our
handling of regional TLDs like .eu and .asia. There may be exceptions at some point down the line,
as we see how they're used in practice. See our help center for more information on
[multi-regional and multilingual sites](/search/docs/specialty/international/managing-multi-regional-sites),
and set
[geotargeting in Search Console](https://support.google.com/webmasters/answer/62399)
where relevant.

**Q: What about real
[ccTLDs](https://en.wikipedia.org/wiki/Country_code_top-level_domain)
(country code top-level domains): will Google favor ccTLDs (like .uk, .ae, etc.) as a local
domain for people searching in those countries?**
A: By default, most ccTLDs (with
[exceptions](https://support.google.com/webmasters/answer/1347922))
result in Google using these to geotarget the website; it tells us that the website is probably
more relevant in the appropriate country. Again, see our help center for more information on
[multi-regional and multilingual sites](/search/docs/specialty/international/managing-multi-regional-sites).

**Q: Will Google support my SEO efforts to move my domain from .com to a new TLD? How do I move
my website without losing any search ranking or history?**
A: We have extensive
[site move documentation](/search/docs/crawling-indexing/site-move-with-url-changes)
in our Help Center. We treat these moves the same as any other site move. That said, domain
changes can take time to be processed for Search (and outside of Search, users expect email
addresses to remain valid over a longer period of time), so it's generally best to choose a domain
that will fit your long-term needs.

We hope this gives you more information on how the new top level domains are handled. If you have
any more questions, you can drop them here, or ask in our
[help forums](https://support.google.com/webmasters/go/community).
