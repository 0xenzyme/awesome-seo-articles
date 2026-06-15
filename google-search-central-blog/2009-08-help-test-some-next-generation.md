---
title: "Help test some next-generation infrastructure"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-08-help-test-some-next-generation"
url: "https://developers.google.com/search/blog/2009/08/help-test-some-next-generation"
canonical: "https://developers.google.com/search/blog/2009/08/help-test-some-next-generation"
author: "Matt Cutts"
published: "2009-08-10T00:00:00+00:00"
updated: "2009-08-10T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:59:45+00:00"
status_code: 200
html_hash: "cf93183d2c4c0bb343fcf1eb7e9220d475867f12f85fd2e7a9dc12e18d6fefbc"
clean_word_count: 384
clean_char_count: 2286
---
# Help test some next-generation infrastructure

To build a great web search engine, you need to:

1. Crawl a large chunk of the web.
2. Index the resulting pages and compute how reputable those pages are.
3. Rank and return the most relevant pages for users' queries as quickly as possible.

For the last several months, a large team of Googlers has been working on a secret project: a
next-generation architecture for Google's web search. It's the first step in a process that will
let us push the envelope on size, indexing speed, accuracy, comprehensiveness and other
dimensions. The new infrastructure sits "under the hood" of Google's search engine, which means
that most users won't notice a difference in search results. But web developers and power
searchers might notice a few differences, so we're opening up a web developer preview to collect
feedback.

Some parts of this system aren't completely finished yet, so we'd welcome feedback on any issues
you see. We invite you to visit the web developer preview of Google's new infrastructure at
<https://www2.sandbox.google.com/>
and try searches there.

Right now, we only want feedback on the **differences** between Google's current search results
and our new system. We're also interested in higher-level feedback ("These types of sites seem to
rank better or worse in the new system") in addition to "This specific site should or shouldn't
rank for this query." Engineers will be reading the feedback, but we won't have the cycles to
send replies.

Here's how to give us feedback: Do a search at
<https://www2.sandbox.google.com/>
and look on the search results page for a link at the bottom of the page that says "Dissatisfied?
Help us improve." Click on that link, type your feedback in the text box and then include the word
**caffeine** somewhere in the text box. Thanks in advance for your feedback!

You can change these two values appropriately:

```
hl=language
```

```
gl=country_code
```

Examples:

German language in Germany: `&hl=de&gl=de`

<https://www2.sandbox.google.com/search?hl=de&gl=de&q=alle+meine+entchen>

Spanish language in Mexico: `&hl=es&gl=mx`

<https://www2.sandbox.google.com/search?hl=es&gl=mx&q=de+colores>

And please don't forget to add the word "caffeine" in the feedback text box.
:)
