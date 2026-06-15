---
title: "How search results may differ based on accented characters and interface languages"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-08-how-search-results-may-differ-based-on"
url: "https://developers.google.com/search/blog/2006/08/how-search-results-may-differ-based-on"
canonical: "https://developers.google.com/search/blog/2006/08/how-search-results-may-differ-based-on"
author: null
published: "2006-09-01T00:00:00+00:00"
updated: "2006-09-01T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:46:10+00:00"
status_code: 200
html_hash: "236199b3feb2640a8df162554a328bba1e569778029ab396462df621b94add8c"
clean_word_count: 523
clean_char_count: 3354
---
# How search results may differ based on accented characters and interface languages

When a searcher enters a query that includes a word with accented characters, our algorithms
consider web pages that contain versions of that word both with and without the accent.
For instance, if a searcher enters "México", we'll return results for
pages about both "Mexico" and "México".

![Search results for both mexico and méxico](/static/search/blog/images/import/242f819ee9205edd13023c75f500402f.png)

Conversely, if a searcher enters a query without using accented characters, but a word in that
query could be spelled with them, our algorithms consider web pages with both the accented and
non-accented versions of the word. So if a searcher enters "Mexico",
we'll return results for pages about both "Mexico" and
"México".

![Search results for both mexico and méxico](/static/search/blog/images/import/7b5d44ca08a85f58e83c9e70460765fc.png)

## How the searcher's interface language comes into play

The searcher's interface language is taken into account during this process. For instance, the
set of accented characters that are treated as equivalent to non-accented characters varies
based on the searcher's interface language, as language-level rules for accenting differ.

Also, documents in the chosen interface language tend to be considered more relevant. If a
searcher's interface language is English, our algorithms assume that the queries are in English
and that the searcher prefers English language documents returned.

This means that the search results for the same query can vary depending on the language
interface of the searcher. They can also vary depending on the location of the searcher (which
is based on IP address) and if the searcher chooses to see results only from the specified
language. If the searcher has personalized search enabled, that will also influence the search
results.

The example below illustrates the results returned when a searcher queries
"Mexico" with the interface language set to Spanish.

![Search results for both mexico and méxico](/static/search/blog/images/import/033f25fac4ac6cf0fce7085fc4263fc8.png)

Note that when the interface language is set to Spanish, more results with accented characters
are returned, even though the query didn't include the accented character.

## How to restrict search results

To obtain search results for only a specific version of the word (with or without accented
characters), you can place a `+` before the word. For instance, the search
"+Mexico" returns only pages about
"Mexico" (and not "México"). The search
"+México" returns only pages about
"México" and not "Mexico". Note that you
may see some search results that don't appear to use the version of word you specified in your
query, but that version of the word may appear within the content of the page or in anchor text to
the page, rather than in the title or description listed in the results. (You can see the top
anchor text used to link to your site by choosing **Statistics**
> **Page analysis** in
[Webmaster Tools](https://search.google.com/search-console).)

The example below illustrates the results returned when a searcher queries
"+Mexico".

![Search results for both mexico when the query is preceded by a plus sign](/static/search/blog/images/import/be559ca44799387188953010bf70fc76.png)
