---
title: "How Google Search handles multilingual searches"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2023-09-multilingual-searches"
url: "https://developers.google.com/search/blog/2023/09/multilingual-searches"
canonical: "https://developers.google.com/search/blog/2023/09/multilingual-searches"
author: "Danny Sullivan"
published: "2023-09-08T00:00:00+00:00"
updated: "2023-09-08T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
fetched_at: "2026-06-14T13:42:33+00:00"
status_code: 200
html_hash: "5f45a3a60475ae4d7187e475caa79be3114deed9e26488b35dc47685f711dfd3"
clean_word_count: 765
clean_char_count: 4956
---
# How Google Search handles multilingual searches

In many countries and regions around the world, people commonly speak and search in more than one language. To best serve them, Google uses a variety of ways to automatically determine what is the best language or languages to show search results in.

## How Google automatically determines the language for search results

It is understandable that some people might assume Google Search will only show results that match their language settings, but this is not as helpful as it sounds.

Browsers, mobile devices, and computers all have their own separate language settings. This means it's possible that someone has their browser set to one language, and their mobile device or computer set to a different language.

Google Search also has a language setting, but this is for [display language](https://support.google.com/websearch/answer/3333234) —
the language used for the buttons and menu text that appears around the search results. The search results themselves are not forced to match the display language. This is for a good reason. About half the people searching with Google are multilingual and often search in a language that doesn't match their settings.

Instead, Google Search considers all these settings and other factors to [automatically determine what languages](https://support.google.com/websearch/answer/13511324) would be most helpful to show results in. This means multilingual searchers don't have to constantly change one or more language settings to get results in the different languages they may use.

For example, someone in France can search in French, English, or Arabic and expect to get results in the appropriate language. Similarly, due to typing difficulty on some keyboards, a person in India might search in Hindi using Latin rather than देवनागरी (Devanāgarī) characters but want and receive Hindi results written either way.

Sometimes, helpful results can be shown even if they are in a language that's different from a person's settings or the language they searched in. This may happen if our systems recognize a search is coming from a location where more than one language is commonly used and understood.

## How to filter results to a particular language

While our automated systems don't filter results to a single language, the language results filter we offer can help with this.

The filter works well to narrow web results to a selected language or languages. However, it isn't perfect. It might not work if language can't be detected reliably, such as on pages written in more than one language. It might also not work with some search features.

Our [language results filter](https://support.google.com/websearch/answer/13485060) help page explains how to enable and use the filter. Here's an example of how it looks for someone in German who has enabled it ("Werkzeug" means "Tool" in German):

![Screenshot showing the language settings in German](/static/search/blog/images/language-settings-2023-09.png)

Filtering results by language can also be done before performing a search by using our [Advanced Search page](https://www.google.com/advanced_search). Either option provides the flexibility to filter on a one-time basis as needed.

## How content producers should consider multilingual searchers

We encourage publishers in areas where several languages are commonly used to make content in those different languages rather than in just one that is widely understood. People appreciate content written in their preferred languages, and Google itself would like to show it when it is available.

Those producing multilingual content should also ensure they are following our technical guidance, as covered in this help page: [Tell Google about localized versions of your page](/search/docs/specialty/international/localized-versions).

## How we keep improving language matching

While we get language intent right most of the time, language preferences are complex around the world. That's why to best serve multilingual people, we're continuing to experiment with features like [bilingual search](https://blog.google/intl/en-in/company-news/inside-google/google-for-india-2022-product-announcements/) and the recently announced ability to [toggle SGE generative AI responses between English and Hindi](https://blog.google/products/search/google-search-generative-ai-india-japan/).

Over the past few months, we've also released a series of updates to improve our language matching systems, including the latest update about two weeks ago. Collectively, these should better match results to the language someone searches in, while still allowing for the flexibility multilingual searchers need to access results in multiple languages.

We will also keep improving how our automated systems determine the language of results to show, so that we continue to list the most helpful information we can to people in the languages they prefer.
