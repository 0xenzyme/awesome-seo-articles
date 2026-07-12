---
title: "Introducing schema.org: Search engines come together for a richer web"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-06-introducing-schemaorg-search-engines"
url: "https://developers.google.com/search/blog/2011/06/introducing-schemaorg-search-engines"
canonical: "https://developers.google.com/search/blog/2011/06/introducing-schemaorg-search-engines"
author: "Kavi Goel, Pravir Gupta"
published: "2011-06-02T00:00:00+00:00"
updated: "2011-06-02T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:13:47+00:00"
status_code: 200
html_hash: "d0055b3caf708e80096155e6df4c40d22886a6d62fad920d87e34f75711692f6"
clean_word_count: 905
clean_char_count: 5840
---
# Introducing schema.org: Search engines come together for a richer web

Today we're announcing [schema.org](https://schema.org/), a new initiative from Google,
Bing and Yahoo! to create and support a common set of schemas for structured data markup on web
pages. Schema.org aims to be a one stop resource for webmasters looking to add markup to their
pages to help search engines better understand their websites.

At Google, we've supported structured markup for a couple years now. We
[introduced rich snippets](https://googleblog.blogspot.com/2009/05/more-search-options-and-other-updates)
in 2009 to better represent search results describing
[people](/search/docs/appearance/structured-data/intro-structured-data) or containing
[reviews](/search/docs/appearance/structured-data/review-snippet). We've since expanded
to new kinds of rich snippets, including
[products](/search/docs/appearance/structured-data/product),
[events](/search/docs/appearance/structured-data/event),
[recipes](/search/docs/appearance/structured-data/recipe), and more.

![Example Google rich result for recipes](/static/search/blog/images/import/c2875c84a96beda6b694c0ceb8448114.png)

*Example of a rich snippet: a search result enhanced by structured markup. In this case, the rich
snippet contains a picture, reviews, and cook time for the recipe.*

Adoption by the webmaster community has grown rapidly, and today we're able to show rich snippets
in search results more than ten times as often as when we started two years ago.

We want to continue making the open web richer and more useful. We know that it takes time and
effort to add this markup to your pages, and adding markup is much harder if every search engine
asks for data in a different way. That's why we've come together with other search engines to
support a common set of schemas, just as we came together to support a common standard for
[Sitemaps](/search/blog/2006/11/joint-support-for-sitemap-protocol)in 2006. With
schema.org, site owners can improve how their sites appear in search results not only on Google,
but on Bing, Yahoo! and potentially other search engines as well in the future.

Now let's discuss some of the details of schema.org relevant to you as a webmaster.

## 1) Schema.org contains a lot of new markup types.

We've added more than 100 new types as well as ported over all of the existing rich snippets
types. If you've looked at adding rich snippets markup before but none of the existing types
were relevant for your site, it's worth taking another look. Here are a few popular types:

- Creative works:
  [CreativeWork](https://schema.org/CreativeWork),
  [Book](https://schema.org/Book),
  [Movie](https://schema.org/Movie),
  [MusicRecording](https://schema.org/MusicRecording),
  [Recipe](https://schema.org/Recipe),
  [TVSeries](https://schema.org/TVSeries)
- Embedded non-text objects:
  [AudioObject](https://schema.org/AudioObject),
  [ImageObject](https://schema.org/ImageObject),
  [VideoObject](https://schema.org/VideoObject)
- [Event](https://schema.org/Event)
- [Organization](https://schema.org/Organization)
- [Person](https://schema.org/Person)
- [Place](https://schema.org/Place),
  [LocalBusiness](https://schema.org/LocalBusiness),
  [Restaurant](https://schema.org/Restaurant)
- [Product](https://schema.org/Product),
  [Offer](https://schema.org/Offer),
  [AggregateOffer](https://schema.org/AggregateOffer)
- [Review](https://schema.org/Review),
  [AggregateRating](https://schema.org/AggregateRating)

Or, view a
[full list of all schema.org types](https://schema.org/docs/full).
The new markup types may be used for future rich snippets formats as well as other types of
improvements to help people find your content more easily when searching.

## 2) Schema.org uses microdata.

Historically, we've supported three different standards for structured data markup: microdata,
microformats, and RDFa. We've decided to focus on just one format for schema.org to create a
simpler story for webmasters and to improve consistency across search engines relying on the
data. There are arguments to be made for preferring any of the existing standards, but we've found
that microdata strikes a balance between the extensibility of RDFa and the simplicity of
microformats, so this is the format that we've gone with.

To get an overview of microdata as well as the conventions followed by schema.org, take a look at
the schema.org [Getting Started](https://schema.org/docs/gs)
guide.

## 3) We'll continue to support our existing rich snippets markup formats.

If you've already done markup on your pages using microformats or RDFa, we'll continue to support
it. One caveat to watch out for: while it's OK to use the new schema.org markup or continue to
use existing microformats or RDFa markup, you should avoid mixing the formats together on the
same web page, as this can confuse our parsers.

## 4) Test your markup using the rich snippets testing tool.

It's very useful to test your web pages with markup to make sure we're able to parse the data
correctly. As with previous rich snippets markup formats, you should use the
[rich snippets testing tool](https://www.google.com/webmasters/tools/richsnippets)
for this purpose. Note that while the testing tool will show the marked up information that was
parsed from the page, rich snippets previews are not yet shown for schema.org markup. We'll be
adding this functionality soon.

The [schema.org](https://schema.org/) website and the rich snippets testing tool are in
English. However, Google shows rich snippets in search results globally, so there's no need to
wait to start marking up your pages.

To learn more about rich snippets and how they relate to schema.org, check out the
[Rich snippets schema.org FAQ](https://www.google.com/support/webmasters/bin/answer.py?answer=1211158).
