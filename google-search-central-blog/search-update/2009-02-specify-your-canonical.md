---
title: "Specify your canonical"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2009-02-specify-your-canonical"
url: "https://developers.google.com/search/blog/2009/02/specify-your-canonical"
canonical: "https://developers.google.com/search/blog/2009/02/specify-your-canonical"
author: "Written by Joachim Kupke, Senior Software Engineer, and Maile Ohye, Developer Programs Tech Lead"
published: "2009-02-12T00:00:00+00:00"
updated: "2009-02-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:57:05+00:00"
status_code: 200
html_hash: "c512e4dfa9c745a11014ad8428faae72e349c4de09cb1266f88478d26580b874"
clean_word_count: 903
clean_char_count: 5892
---
# Specify your canonical

Carpe diem on any
[duplicate content worries](/search/blog/2008/09/demystifying-duplicate-content-penalty):
we now support a format that allows you to publicly specify your preferred version of a URL. If
your site has identical or vastly similar content that's accessible through multiple URLs, this
format provides you with more control over the URL returned in search results. It also helps to
make sure that properties such as link popularity are consolidated to your preferred version.

Let's take our old example of a
[site selling Swedish fish](https://bp2.blogger.com/_o5Na_9269nA/RuleCxWoOXI/AAAAAAAAAuU/akzGuAnW5nQ-h/swedish-fish.jpg).
Imagine that your preferred version of the URL and its content looks like this:
`https://www.example.com/product.php?item=swedish-fish`

![](/static/search/blog/images/import/c77d86a626dbe2a0c4f5fdda3b55689f.png)

However, users (and Googlebot) can access Swedish fish through multiple (not as simple) URLs. Even
if the key information on these URLs is the same as your preferred version, they may show slight
content variations due to things like sort parameters or category navigation:
`https://www.example.com/product.php?item=swedish-fish&category=gummy-candy`

![](/static/search/blog/images/import/a055763a2c0194375fba7211bc010368.png)

Or they have completely identical content, but with different URLs due to things such as a
tracking parameters or a session ID:
`https://www.example.com/product.php?item=swedish-fish&trackingid=1234&sessionid=5678`

![](/static/search/blog/images/import/c77d86a626dbe2a0c4f5fdda3b55689f.png)

Now, you can simply add this `<link />` tag to specify your preferred version:
`<link rel="canonical" href="https://www.example.com/product.php?item=swedish-fish" />`
inside the  `<head>` section of the duplicate content URLs:

```
https://www.example.com/product.php?item=swedish-fish&category=gummy-candy
https://www.example.com/product.php?item=swedish-fish&trackingid=1234&sessionid=5678
```

and Google will understand that the duplicates all refer to the canonical URL:
`https://www.example.com/product.php?item=swedish-fish`. Additional URL properties, like
PageRank and related signals, are transferred as well.

This standard can be adopted by any search engine when crawling and indexing your site.

Of course you may have more questions.
[Joachim Kupke](https://research.google.com/pubs/author3778),
an engineer from our Indexing Team, is here to provide us with the answers:

**Is `rel="canonical"` a hint or a command?**
It's a hint that we honor strongly. We'll take your preference into account, in conjunction with
other signals, when calculating the most relevant page to display in search results.

**Can I use a relative path to specify the canonical, such as
`<link rel="canonical" href="product.php?item=swedish-fish" />`?**
Yes, relative paths are recognized as expected with the `<link />` tag. Also, if
you include a `<base />` link in your document, relative paths will resolve
according to the base URL.

**Is it okay if the canonical is not an exact duplicate of the content?**
We allow slight differences, for example, in the sort order of a table of products. We also
recognize that we may crawl the canonical and the duplicate pages at different points in time,
so we may occasionally see different versions of your content. All of that is okay with us.

**What if the `rel="canonical"` returns a `404`?**
We'll continue to index your content and use a heuristic to find a canonical, but we recommend
that you specify existent URLs as canonicals.

**What if the `rel="canonical"` hasn't yet been indexed?**
Like all public content on the web, we strive to discover and crawl a designated canonical URL
quickly. As soon as we index it, we'll immediately reconsider the
`rel="canonical"` hint.

**Can `rel="canonical"` be a redirect?**
Yes, you can specify a URL that redirects as a canonical URL. Google will then process the
redirect as usual and try to index it.

**What if I have contradictory `rel="canonical"` designations?**
Our algorithm is lenient: We can follow canonical chains, but we strongly recommend that you
update links to point to a single canonical page to ensure optimal canonicalization results.

**Can this link tag be used to suggest a canonical URL on a completely different domain?**

No. To migrate to a completely different domain, permanent (`301`) redirects are more
appropriate. Google currently will take canonicalization suggestions into account across
subdomains (or within a domain), but not across domains. So site owners can suggest
`www.example.com` vs. `example.com` vs. `help.example.com`, but
not `example.com` vs. `example-widgets.com`.

**Sounds great—can I see a live example?**
Yes,
[wikia.com](https://wikia.com/)
helped us as a trusted tester. For example, you'll notice that the source code on the URL
`https://starwars.wikia.com/wiki/Nelvana_Limited` specifies its
`rel="canonical"` as: `https://starwars.wikia.com/wiki/Nelvana`.

The two URLs are nearly identical to each other, except that `Nelvana_Limited`, the
first URL, contains a brief message near its heading. It's a good example of using this feature.
With `rel="canonical"`, properties of the two URLs are consolidated in our index and
search results display wikia.com's intended version.

You can ask additional questions in our comments below. And if you're unable to implement a
canonical designation link, no worries; we'll still do our best to select a preferred version of
your duplicate content URLs, and transfer linking properties,
[just as we did before](/search/blog/2007/09/google-duplicate-content-caused-by-url).

For more information, please see our Help Center articles on
[canonicalization](/search/docs/crawling-indexing/consolidate-duplicate-urls)
and
[rel=canonical](/search/docs/crawling-indexing/consolidate-duplicate-urls).
