---
title: "The Ultimate Fate of Supplemental Results"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-12-ultimate-fate-of-supplemental-results"
url: "https://developers.google.com/search/blog/2007/12/ultimate-fate-of-supplemental-results"
canonical: "https://developers.google.com/search/blog/2007/12/ultimate-fate-of-supplemental-results"
author: "Yonatan Zunger, Search Quantity Team"
published: "2007-12-19T00:00:00+00:00"
updated: "2007-12-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:51:12+00:00"
status_code: 200
html_hash: "cc335fbe05731d452f079cdf40113c1c2c470f8e3e927280cdb282af071565b5"
clean_word_count: 423
clean_char_count: 2584
---
# The Ultimate Fate of Supplemental Results

In 2003, Google introduced a "supplemental index" as a way of showing more documents to users.
Most webmasters will probably snicker about that statement, since supplemental docs were famous
for refreshing less often and showing up in search results less often. But the supplemental
index served an important purpose: it stored unusual documents that we would search in more
depth for harder or more esoteric queries. For a long time, the alternative was to simply not
show those documents at all, but this was always unsatisfying—ideally, we would search all of
the documents all of the time, to give users the experience they expect.

This led to a major effort to rethink the entire supplemental index. We improved the crawl
frequency and decoupled it from which index a document was stored in, and once these
"supplementalization effects" were gone, the "supplemental result" tag itself—which only
served to suggest that otherwise good documents were somehow suspect—
[was eliminated a few months ago](/search/blog/2007/07/supplemental-goes-mainstream).
Now we're coming to the next major milestone in the elimination of the artificial difference
between indices: rather than searching some part of our index in more depth for obscure queries,
we're now searching the whole index for every query.

From a user perspective, this means that you'll be seeing more relevant documents and a much
deeper slice of the web, especially for non-English queries. For webmasters, this means that
good-quality pages that were less visible in our index are more likely to come up for queries.
Hidden behind this are some truly amazing technical feats; serving this much larger of an index
doesn't happen easily, and it took several fundamental innovations to make it possible. At this
point it's safe to say that the Google search engine works like nothing else in the world. If
you want to know how it actually works, you'll have to come join Google Engineering; as usual,
it's all triple-hush-hush secrets.\*

---

\* Originally, I was going to give the stock Google answer, "If I told you, I'd have to kill you."
However, I've been informed by management that killing people violates our "Don't be evil" policy,
so I'm forced to replace that with sounding mysterious and suggesting that good engineers come and
join us. Which I'm dead serious about; if you've got the technical chops and want to work on some
of the most complex and advanced large-scale software infrastructure in the world,
[we want you here](https://careers.google.com/jobs/).
