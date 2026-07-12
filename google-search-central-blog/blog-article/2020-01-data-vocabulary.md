---
title: "Sunsetting support for data-vocabulary"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2020-01-data-vocabulary"
url: "https://developers.google.com/search/blog/2020/01/data-vocabulary"
canonical: "https://developers.google.com/search/blog/2020/01/data-vocabulary"
author: "Moshe Samet"
published: "2020-01-21T00:00:00+00:00"
updated: "2020-01-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:35:50+00:00"
status_code: 200
html_hash: "1b40eada5ea047ed64e842adb39c98ef5381d87e3e1f1def433f7322289a979a"
clean_word_count: 606
clean_char_count: 4215
---
# Sunsetting support for data-vocabulary

Structured data schemas such as [schema.org](https://schema.org/) and
[data-vocabulary.org](https://data-vocabulary.org/)
are used to define shared meaningful structures for markup-based applications on the Web. With
the increasing usage and popularity of schema.org we decided to focus our development on a
single SD scheme. As of April 6, 2020, data-vocabulary.org markup will no longer be eligible for
[Google rich result features](/search/docs/appearance/structured-data/search-gallery).

As a preparation for the change and starting today, Search Console will issue warnings for pages
using the data-vocabulary.org schema so that you can prepare for the sunset in time. This will
allow you to easily identify pages using that markup and replace the data-vocabulary.org
markup with schema.org.

## A bit more about structured data

Google uses
[structured data](/search/docs/appearance/structured-data/intro-structured-data)
standardized formats and shared schemas to provide information about a page and the things
described by the page. This information is used for two main purposes

1. Understand the content of the page
2. Enable special search result features and enhancements

## What are structured data formats?

Structured data formats like JSON-LD, RDFa and Microdata define a small number of fixed
structures that can be used to encode descriptive data. They typically build upon lower-level
standards like JSON and HTML. To learn more about the supported and recommended formats, please
check out our
[developers guide](/search/docs/appearance/structured-data/intro-structured-data#structured-data-format).

## What are structured data schemas?

Alongside the structured data formats, structured data schemas work like a kind of dictionary,
defining terms for types of thing (for example, `Person`,
`Event`, `Organization`), and for
properties and relationships (for example, `name`,
`worksFor`). By maintaining this separation between format and
schema, it is possible for users of different formats to take advantage of the same, widely
shared, schemas.

## Data-vocabulary schema

Google's "Data Vocabulary" project was an important milestone in the development of structured
data on the Web, because it led to our collaboration with other search engines to create
schema.org. However it is now very outdated and it is generally preferable to use more widely
shared vocabulary from Schema.org. Therefore data-vocabulary.org markup will stop being
eligible for Google search result features and enhancements.

Please note that this is the only consequence of this change. Pages using data-vocabulary schema
will remain valid for all other purposes.

In order to be eligible for Google rich result features we recommend converting your
data-vocabulary.org structured data to schema.org.

For example, here is how you would change the data vocabulary to schema.org

### Data-vocabulary.org

```
<div itemscope itemtype="https://data-vocabulary.org/Breadcrumb">
<a href="https://www.example.com/dresses" itemprop="url">
<span itemprop="title">Dresses</span></a>
>
</div>
<div itemscope itemtype="https://data-vocabulary.org/Breadcrumb">
<a href="https://www.example.com/dresses/real" itemprop="url">
<span itemprop="title">Real Dresses</span></a>
>
</div>
```

### Schema.org

```
<ol itemscope itemtype="https://schema.org/BreadcrumbList">
  <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
    <a itemprop="item" href="https://example.com/dresses"><span itemprop="name">Dresses</span></a>
    <meta itemprop="position" content="1" /></li>
  <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
    <a itemprop="item" href="https://example.com/dresses/real"><span itemprop="name">Real Dresses</span></a>
    <meta itemprop="position" content="2" /></li>
</ol>
```

You can test any code snippet live on
[Rich Results Test](https://search.google.com/test/rich-results)
by pasting it into the search box. Try it out! And if you have any questions or comments, check out the
[Google Webmasters community](https://support.google.com/webmasters/threads?thread_filter=(category:structured_data)).

---
