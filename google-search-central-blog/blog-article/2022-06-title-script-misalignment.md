---
title: "How Google generates titles for documents with language or script misalignment"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2022-06-title-script-misalignment"
url: "https://developers.google.com/search/blog/2022/06/title-script-misalignment"
canonical: "https://developers.google.com/search/blog/2022/06/title-script-misalignment"
author: "Koji Kojima"
published: "2022-06-03T00:00:00+00:00"
updated: "2022-06-03T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:40:42+00:00"
status_code: 200
html_hash: "19d8fa0a9894bf8f2429714a7bf493f33510bcf91c6ed73143d0cc12e8b94139"
clean_word_count: 445
clean_char_count: 2640
---
# How Google generates titles for documents with language or script misalignment

This week, we introduced an algorithmic improvement that identifies documents where the title
element is written in a different language or script from its content, and chooses a title that
is similar to the language and script of the document. This is based on the general principle
that a document’s title should be written by the language or script of its primary contents.
It's one of the reasons where
[we might go beyond title elements](/search/blog/2021/09/more-info-about-titles#examples-of-going-beyond-title-elements)
for web result titles.

## Multilingual titles

Multilingual titles repeat the same phrase with two different languages or scripts.
The most popular pattern is to append an English version to the original title text.

> गीतांजलि की जीवनी - Geetanjali Biography in Hindi

In this example, the title consists of two parts (divided by a hyphen), and they express the
same contents in different languages (Hindi and English). While the title is in both languages,
the document itself is written only in Hindi. Our system detects such inconsistency and might use
only the Hindi headline text, like:

> गीतांजलि की जीवनी

## Latin scripted titles

Transliteration is when content is written from one language into a different language that uses
a different script or alphabet. For example, consider a page title for a song written in Hindi
but transliterated to use Latin characters rather than Hindi’s native Devanagari script:

> jis desh me holi kheli jati hai

In such a case, our system tries to find an alternative title using the script that’s predominant on the page, which in this case could be:

> जिस देश में होली खेली जाती है

## Summary

In general, our systems tend to use the title element of the page. In cases with multi-language
or transliterated titles, our systems may seek alternatives that match the predominant language of the
page. This is why it's a good practice to provide a title that matches the language and/or the
script of the page's main content.

We welcome further feedback in our [forum](https://support.google.com/webmasters/community),
including existing threads on this topic in
[English](https://support.google.com/webmasters/thread/122879386/your-feedback-on-titles-shown-in-search-results)
and
[Japanese](https://support.google.com/webmasters/thread/125182163/%E6%A4%9C%E7%B4%A2%E7%B5%90%E6%9E%9C%E3%81%AB%E8%A1%A8%E7%A4%BA%E3%81%95%E3%82%8C%E3%82%8B%E3%82%BF%E3%82%A4%E3%83%88%E3%83%AB%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%83%95%E3%82%A3%E3%83%BC%E3%83%89%E3%83%90%E3%83%83%E3%82%AF?hl=ja).
