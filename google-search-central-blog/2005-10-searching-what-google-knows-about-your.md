---
title: "Searching what Google knows about your site"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2005-10-searching-what-google-knows-about-your"
url: "https://developers.google.com/search/blog/2005/10/searching-what-google-knows-about-your"
canonical: "https://developers.google.com/search/blog/2005/10/searching-what-google-knows-about-your"
author: "Vanessa Fox"
published: "2005-10-12T00:00:00+00:00"
updated: "2005-10-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:43:57+00:00"
status_code: 200
html_hash: "b871ba5db3eacc132b5fe5853e360c05f8971104354be6e7db8fe9c986934a02"
clean_word_count: 535
clean_char_count: 3339
---
# Searching what Google knows about your site

So, you've
[submitted your Sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap#addsitemap).
How can you tell what Google knows about your site?

You can use Google's advanced search features to get a list of:

- search results from your site
- pages that link to your site
- pages that refer to your site's URL

You can also see information that we have about your site.

You can do many of these advanced searches (amazingly enough) by clicking the
[Advanced Search](https://www.google.com/advanced_search) link on
[www.google.com](https://www.google.com/). You can also use our
[advanced search operators](https://www.google.com/help/operators.html)
in your query. If you are using operators, remember that there should not be a space between the
operator and the URL. Note that we use brackets to indicate the words in the search box. The
query itself should not include the brackets.

## Results from your site (`site:` operator)

To find pages from your site, use the `site:` operator. For instance,
`site:www.google.com`. You can also type the URL in the **Domain** field of the
Advanced Search page.

![domain field on the advanced search page](/static/search/blog/images/import/3ba3c3d977da0ba6f26c54c077d47c8a.jpg)

You can also use this feature to search through any site. Simply enter the search query followed
by the `site:` operator and the site you want to search through. For instance, to
search for admission information on the Stanford University web site, type
`admission site:www.stanford.edu`. And, you can use this feature to search through
sites from specific top-level domains. For instance, to search for information about Zürich on
Swiss sites in the .ch domain, type `Zürich site:.ch`.

## Pages that link to your site (`link:` operator)

To find pages that link to your site, use the `link:` operator. For instance,
`link:www.google.com`. You can also type the URL in the **Links** field of the
Advanced Search page.

![links field on the advanced search page](/static/search/blog/images/import/996990a93735b245c67a782714857d86.jpg)

## Pages that refer to your site's URL (`allinurl:` operator)

To find pages that include your site's URL, use the `allinurl:` operator. For instance,
`allinurl:www.google.com`.

## Information Google has about your site (`info:` operator)

To see information that Google knows about your site, use the `info:` operator. For
instance, `info:www.google.com`. That query results in the following:

![result for an info: query](/static/search/blog/images/import/f0260f19114eb931e3b93da6b0569495.jpg)

Some questions you may have about these results...

## I submitted my Sitemap but I don't see all the pages listed. When will they be indexed?

We [can't guarantee if or when](https://search.google.com/search-console)
we'll index pages we receive from Sitemaps submissions. We use Sitemaps as another view into your
site to augment our regular crawling methods. Also, we don't want the
[Googlebot](/search/docs/crawling-indexing/googlebot) to overwhelm your bandwidth, so
we may not crawl it all at one time.

## Some of my results are labeled "Supplemental". What does that mean?

That means that pages are part of our auxiliary index. You can read more about that in our
[webmaster guidelines](/search/docs/essentials).
