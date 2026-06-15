---
title: "More about changing domain names"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-01-more-about-changing-domain-names"
url: "https://developers.google.com/search/blog/2006/01/more-about-changing-domain-names"
canonical: "https://developers.google.com/search/blog/2006/01/more-about-changing-domain-names"
author: "Vanessa Fox"
published: "2006-01-27T00:00:00+00:00"
updated: "2006-01-27T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:44:32+00:00"
status_code: 200
html_hash: "b18871c9bc05f8d73c12fbbe44b91fc7634c56ce220665f93d2dcc5e80a22647"
clean_word_count: 471
clean_char_count: 2716
---
# More about changing domain names

Recently, someone asked me about
[moving from one domain](/search/blog/2005/11/changing-domains) to another. They had
read that
[Google recommends using a `301` redirect](/search/docs/crawling-indexing/site-move-with-url-changes)
to let Googlebot know about the move, but they weren't sure if they should do that. They wondered
if Googlebot would follow the `301` to the new site, see that it contained the same
content as the pages already indexed from the old site, and think it was duplicate content (and
therefore not index it). They wondered if a `302` redirect would be a better option.

I told them that a `301` redirect was exactly what they should do. A
[`302`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.3)
redirect tells Googlebot that the move is temporary and that Google should continue to index the
old domain. A
[`301`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.2)
redirect tells Googlebot that the move is permanent and that Google should start indexing the new
domain instead. Googlebot won't see the new site as duplicate content, but as *moved*
content. And that's exactly what someone who is changing domains wants.

They also wondered how long it would take for the new site to show up in Google search results.
They thought that a new site could take longer to index than new pages of an existing site. I told
them that if they noticed that it took a while for a new site to be indexed, it was generally
because it took Googlebot a while to learn about the new site. Googlebot learns about new pages to
crawl by following links from other pages and from Sitemaps. If Googlebot already knows about a
site, it generally finds out about new pages on that site quickly, since the site links to the
new pages.

I told them that by using a `301` to redirect Googlebot from the old domain to the new
one and by submitting a Sitemap for the new domain, Googlebot could much more quickly learn about
the new domain than it might otherwise. They could also let other sites that link to their site
know about the domain change so that other sites could update their links.

The crawling and indexing processes are completely automated, so I couldn't tell them exactly when
the domain would start showing up in results. But letting Googlebot know about the site (using a
`301` redirect and a Sitemap) is an important first step in that process.

You can find out more about
[submitting a Sitemap in our documentation](/search/docs/crawling-indexing/sitemaps/build-sitemap)
and you can find out more about how to use a `301` redirect by doing a Google search
for [`301` redirect](https://www.google.com/search?q=301+redirect).
