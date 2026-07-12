---
title: "Sitemaps ping endpoint is going away"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2023-06-sitemaps-lastmod-ping"
url: "https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping"
canonical: "https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping"
author: "Gary Illyes"
published: "2023-06-26T00:00:00+00:00"
updated: "2023-06-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
fetched_at: "2026-06-14T13:42:17+00:00"
status_code: 200
html_hash: "faaad0efc3742b4943a1991e0d771490b7a46447160717df3452bcb313eaf75b"
clean_word_count: 737
clean_char_count: 4644
---
# Sitemaps ping endpoint is going away

[The Sitemaps Protocol was introduced in 2005](https://googleblog.blogspot.com/2005/06/webmaster-friendly.html)
to help search engines with the discovery of new URLs, and also to help with scheduling new crawls
of already discovered URLs. It's a wildly popular protocol that hasn't changed for over 15 years.
While the general idea is still useful, some aspects have become less practical in today's internet.

To that end, we're announcing deprecation of the sitemaps "ping" endpoint and providing additional
recommendations for the use of the `lastmod` element.

## Sitemap ping

The sitemap protocol defines an
[unauthenticated REST method](https://sitemaps.org/protocol.html#submit_ping)
for submitting sitemaps to search engines. Our internal studies—and also other
[search engines such as Bing](https://blogs.bing.com/webmaster/may-2022/Spring-cleaning-Removed-Bing-anonymous-sitemap-submission)—tell
us that at this point these unauthenticated sitemap submissions are not very useful. In fact,
in the case of Google Search, the vast majority of the submissions lead to spam. To wit, we're
deprecating our support for sitemaps ping and the endpoint will stop functioning in 6 months. You
can still
[submit your sitemaps through robots.txt and Search Console](/search/docs/crawling-indexing/sitemaps/overview),
but the HTTP requests ("pings") to the deprecated REST endpoint will result in a `404`
error. Any existing code or plugins which use this endpoint will not cause problems for Google
Search; you don't need to make any changes (but using the endpoint will also not do anything
useful).

## The `lastmod` element

Over the years we've observed a varying level of usefulness of the `lastmod` element
across the sites that provide it. This may have been the result of the kind of content that's
published, or perhaps the content management system, but nowadays `lastmod` is indeed
useful in many cases and we're using it as a signal for scheduling crawls to URLs that we
previously discovered.

For the `lastmod` element to be useful, first it needs to be in a supported date format
(which is documented on
[sitemaps.org](https://sitemaps.org/protocol.html#lastmoddef));
Search Console will tell you if it's not once you submit your sitemap. Second, it needs to
consistently match reality: if your page changed 7 years ago, but you're telling us in the
`lastmod` element that it changed yesterday, eventually we're not going to believe you
anymore when it comes to the last modified date of your pages.

You can use a `lastmod` element for all the pages in your sitemap, or just the ones
you're confident about. For instance, some site software may not be able to easily tell the last
modification date of the homepage or a category page because it just aggregates the other pages on
the site. In these cases it's fine to leave out `lastmod` for those pages.

And when we say "last modification", we actually mean "last **significant**
modification". If your CMS changed an insignificant piece of text in the sidebar or footer, you
don't have to update the `lastmod` value for that page.
However if you changed the primary text, added or changed structured data, or updated some links, do
update the `lastmod` value.

```
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
      <lastmod>2005-01-01</lastmod>
      <loc>http://www.example.com/</loc>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
  </url>
</urlset>
```

Example of a simple sitemap with all the possible elements; source:
[sitemaps.org](https://sitemaps.org/protocol.html)

Going on a small tangent, if you look at the `xmlns` attribute in the sitemap snippet,
you'll see that the URI is on HTTP, and not on HTTPS. This is working as intended: it's a
reference for parsers about the elements in the XML. Please don't file more documentation feedback
about this.

## `changefreq` and `priority`

Google still doesn't use the `changefreq` or `priority` elements at all.
`changefreq` specifically is also conceptually overlapping with `lastmod`.
The `priority` element is a heavily subjective field and based on our internal studies,
it generally doesn't accurately reflect the actual priority of a page relative to other pages on a
site.

Want to read more about sitemaps? Check out
[our documentation](/search/docs/crawling-indexing/sitemaps/overview), but also
[sitemaps.org](https://sitemaps.org),
and if you want to just chat with us about sitemaps, you can find us in the
[Google Search Central forums](https://goo.gle/sc-forum) and on
[Twitter](https://twitter.com/GoOgLeSeArChC).
