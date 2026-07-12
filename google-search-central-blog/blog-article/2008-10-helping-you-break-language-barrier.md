---
title: "Helping you break the language barrier"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-10-helping-you-break-language-barrier"
url: "https://developers.google.com/search/blog/2008/10/helping-you-break-language-barrier"
canonical: "https://developers.google.com/search/blog/2008/10/helping-you-break-language-barrier"
author: "Written by Josh Estelle, Google Translate"
published: "2008-10-14T00:00:00+00:00"
updated: "2008-10-14T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:54:40+00:00"
status_code: 200
html_hash: "5537042ff2a9a2970c557ebd1232eece9af95c16b006dd013a3cd7f879d9c27d"
clean_word_count: 638
clean_char_count: 4115
---
# Helping you break the language barrier

When webmasters put content out on the web it's there for the world to see. Unfortunately, most
content on the web is only published in a single language, understandable by only a fraction of
the world's population.

In a continued effort to make the world's information universally accessible,
[Google Translate](https://translate.google.com/) has a number of
tools for you to automatically translate your content into the languages of the world.

![the google translate widget for websites](/static/search/blog/images/import/0e86138afd61609badd8be5436311bf8.png)

Users may already be translating your webpage using Google Translate, but you can make it even
easier by including our "Translate My Page" gadget, available at
<https://translate.google.com/translate_tools>.

The gadget will be rendered in the user's language, so if they come to your page and can't
understand anything else, they'll be able to read the gadget, and translate your page into their
language.

Sometimes there may be some content on your page that you don't want us to translate. You can now
add `class="notranslate"` to any HTML element to prevent that element from being
translated. For example, you may want to do something like:

```
Email us at <span class="notranslate">sales at mydomain dot com</span>
```

And if you have an entire page that should not be translated, you can add a `meta` tag to the
`<head></head>` of your page and we won't translate any of the content on
that page.

```
<meta name="google" value="notranslate" />
```

**Update on 12/15/2008:** Thanks to chaoskaizer for pointing this out in the comments
:), we also support:

```
<meta name="google" content="notranslate" />
```

Lastly, if you want to do some fancier automatic translation integrated directly into your page,
check out the
[AJAX Language API](https://googleajaxsearchapi.blogspot.com/2008/03/introducing-ajax-language-api-tools-for.html)
we launched last March.

With these tools we hope you can more easily make your content available in all the languages we
support, including
[Arabic](https://translate.google.com/translate_t?tl=ar),
[Bulgarian](https://translate.google.com/translate_t?tl=bg),
[Catalan](https://translate.google.com/translate_t?tl=ca),
[Chinese](https://translate.google.com/translate_t?tl=zh),
[Croatian](https://translate.google.com/translate_t?tl=hr),
[Czech](https://translate.google.com/translate_t?tl=cs),
[Danish](https://translate.google.com/translate_t?tl=da),
[Dutch](https://translate.google.com/translate_t?tl=nl),
[English](https://translate.google.com/translate_t?tl=en),
[Filipino](https://translate.google.com/translate_t?tl=tl),
[Finnish](https://translate.google.com/translate_t?tl=fi),
[French](https://translate.google.com/translate_t?tl=fr),
[German](https://translate.google.com/translate_t?tl=de),
[Greek](https://translate.google.com/translate_t?tl=el),
[Hebrew](https://translate.google.com/translate_t?tl=iw),
[Hindi](https://translate.google.com/translate_t?tl=hi),
[Indonesian](https://translate.google.com/translate_t?tl=id),
[Italian](https://translate.google.com/translate_t?tl=it),
[Japanese](https://translate.google.com/translate_t?tl=ja),
[Korean](https://translate.google.com/translate_t?tl=ko),
[Latvian](https://translate.google.com/translate_t?tl=lv),
[Lithuanian](https://translate.google.com/translate_t?tl=lt),
[Norwegian](https://translate.google.com/translate_t?tl=no),
[Polish](https://translate.google.com/translate_t?tl=pl),
[Portuguese](https://translate.google.com/translate_t?tl=pt),
[Romanian](https://translate.google.com/translate_t?tl=ro),
[Russian](https://translate.google.com/translate_t?tl=ru),
[Serbian](https://translate.google.com/translate_t?tl=sr),
[Slovak](https://translate.google.com/translate_t?tl=sk),
[Slovenian](https://translate.google.com/translate_t?tl=sl),
[Spanish](https://translate.google.com/translate_t?tl=es),
[Swedish](https://translate.google.com/translate_t?tl=sv),
[Ukrainian](https://translate.google.com/translate_t?tl=uk), and
[Vietnamese](https://translate.google.com/translate_t?tl=vi).
