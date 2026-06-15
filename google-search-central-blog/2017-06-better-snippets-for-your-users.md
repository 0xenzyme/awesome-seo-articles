---
title: "Better Snippets for your Users"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2017-06-better-snippets-for-your-users"
url: "https://developers.google.com/search/blog/2017/06/better-snippets-for-your-users"
canonical: "https://developers.google.com/search/blog/2017/06/better-snippets-for-your-users"
author: "Gary Illyes"
published: "2017-06-02T00:00:00+00:00"
updated: "2017-06-02T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:30:27+00:00"
status_code: 200
html_hash: "e11d3a42e2606f51c33a4587cad766bfdd10e4cea9252aef90c9220a92ed0733"
clean_word_count: 668
clean_char_count: 4075
---
# Better Snippets for your Users

Before buying a book, people like to get a snapshot of how they're about to spend a few hours
reading. They'll take a look at the synopsis, the preface, or even the prologue just to get a
sense about whether they'll like the book.

Search result snippets are much the same; they help people decide whether or not it makes sense
to invest the time reading the page the snippet belongs to.

![](/static/search/blog/images/import/a3f3a2a8c5f03740db386420a021abfb.jpg)

The more descriptive and relevant a search result snippet is, the more likely that people will
click through and be satisfied with the page they land on. Historically, snippets came from 3
places:

1. The content of the page
2. The meta description
3. DMOZ listings

The content of the page is an obvious choice for result snippets, and the content that can be
extracted is often the most relevant to people's queries. However, there are times when the
content itself isn't the best source for a snippet. For instance, when someone searches for a
publishing company for their book, the relevant home pages in the result set may contain only a
few images describing the businesses and a logo, and maybe some links, none of which are
particularly useful for a snippet.

The logical fallback in cases when the content of a page doesn't have much textual content for
a search result snippet is the meta description. This should be short blurbs that describe
accurately and precisely the content in a few words.

Finally, when a page doesn't have much textual content for snippet generation and the meta
description is missing, unrelated to the page, or low quality, our fallback was
[DMOZ, also known as The Open Directory Project](https://en.wikipedia.org/wiki/DMOZ).
For over 10 years, we relied on DMOZ for snippets because the quality of the DMOZ snippets were
often much higher quality than those provided by webmasters in their meta description, or were
more descriptive than what the page provided.

With DMOZ [now closed](https://www.dmoz.org/), we've stopped using its
listings for snippeting, so it's a lot more important that webmasters provide good meta
descriptions, if adding more content to the page is not an option.

**What makes a good meta description?**

Good meta descriptions are short blurbs that describe accurately the content of the page. They
are like a pitch that convince the user that the page is exactly what they're looking for. For
more tips, we have a handy
[help center article](/search/docs/appearance/snippet) on the topic. Remember
to make sure that both your desktop and your mobile pages include both a title and a meta
description.

**What are the most common problems with meta descriptions?**

Because meta descriptions are usually visible only to search engines and other software,
webmasters sometimes forget about them, leaving them completely empty. It's also common, for
the same reason, that the same meta description is used across multiple (and sometimes many)
pages. On the flip side, it's also relatively common that the description is completely
off-topic, low quality, or outright spammy. These issues tarnish our users' search experience,
so we prefer to ignore such meta descriptions.

**Is there a character limit for meta descriptions?**

There's no limit on how long a meta description can be, but the search result snippets are
truncated as needed, typically to fit the device width.

**What will happen with the `NOODP` robots rule?**

With DMOZ (ODP) closed, we stopped relying on its data and thus the `NOODP` rule is already
no-op.

**Can I prevent Google from using the page contents as snippet?**

You can prevent Google from generating snippets altogether by specifying the
[`nosnippet` robots rule](/search/docs/crawling-indexing/robots-meta-tag#nosnippet).
There's no way to prevent using page contents as snippet while allowing other sources.

As always, if you have questions, ask in the
[forums](https://support.google.com/webmasters/community) or find us
on [Twitter](https://twitter.com/googlesearchc/)!
