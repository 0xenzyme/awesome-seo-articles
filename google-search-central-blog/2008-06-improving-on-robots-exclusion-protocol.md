---
title: "Improving on Robots Exclusion Protocol"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2008-06-improving-on-robots-exclusion-protocol"
url: "https://developers.google.com/search/blog/2008/06/improving-on-robots-exclusion-protocol"
canonical: "https://developers.google.com/search/blog/2008/06/improving-on-robots-exclusion-protocol"
author: "Written by Prashanth Koppula, Product Manager"
published: "2008-06-03T00:00:00+00:00"
updated: "2008-06-03T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:53:08+00:00"
status_code: 200
html_hash: "aea8c1aec78825a2685da033991cc5d4e3b2d8148a07f3db248819b5c764ccd7"
clean_word_count: 1333
clean_char_count: 8685
---
# Improving on Robots Exclusion Protocol

Web publishers often ask us how they can maximize their visibility on the web. Much of this has
to do with search engine optimization—making sure a publisher's content shows up on all the
search engines.

However, there are some cases in which publishers need to communicate more information to search
engines—like the fact that they *don't* want certain content to appear in search
results. And for that they use something called the
[Robots Exclusion Protocol (REP)](https://googleblog.blogspot.com/2007/01/controlling-how-search-engines-access.html),
which lets publishers control how search engines access their site: whether it's controlling the
visibility of their content across their site (via robots.txt) or down to a much more granular
level for individual pages (via `meta` tags).

Since it was introduced in the early '90s, REP has become the de facto standard by which web
publishers specify which parts of their site they want public and which parts they want to keep
private. Today, millions of publishers use REP as an easy and efficient way to communicate with
search engines. Its strength lies in its flexibility to evolve in parallel with the web, its
universal implementation across major search engines and all major robots, and in the way it
works for any publisher, no matter how large or small.

While REP is observed by virtually all search engines, we've never come together to detail how
we each interpret different tags. Over the last couple of years, we have worked with Microsoft
and Yahoo! to bring forward standards such as
[Sitemaps](https://www.sitemaps.org/)
and offer additional tools for webmasters. Since the original announcement, we have, and will
continue to, deliver further improvements based on what we are hearing from the community.

Today, in that same spirit of making the lives of webmasters simpler, we're releasing detailed
documentation about how we implement REP. This will provide a common implementation for
webmasters and make it easier for any publisher to know how their REP rules will be handled
by three major search providers—making REP more intuitive and friendly to even more
publishers on the web.

So, without further ado...

## Common REP rules

The following list are all the major REP features currently implemented by Google, Microsoft,
and Yahoo!. With each feature, you'll see what it does and how you should communicate it.

Each of these rules can be specified to be applicable for all crawlers or for specific
crawlers by targeting them to specific user-agents, which is how any crawler identifies itself.
Apart from the identification by user-agent, each of our crawlers also supports Reverse DNS based
authentication to allow you to verify the identity of the crawler.

### Robots.txt rules

|  |  |  |
| --- | --- | --- |
| **Rule** | **Impact** | **Use cases** |
| [`Disallow`](/search/docs/crawling-indexing/robots/intro) | Tells a crawler not to index your site—your site's robots.txt file still needs to be crawled to find this rule, however disallowed pages will not be crawled | 'No Crawl' page from a site. This rule in the default syntax prevents specific path(s) of a site from being crawled. |
| [`Allow`](/search/docs/crawling-indexing/overview-google-crawlers) | Tells a crawler the specific pages on your site you want indexed so you can use this in combination with Disallow | This is useful in particular in conjunction with Disallow clauses, where a large section of a site is disallowed except for a small section within it |
| [`$` Wildcard Support](/search/docs/crawling-indexing/robots/robots_txt#url-matching-based-on-path-values) | Tells a crawler to match everything from the end of a URL—large number of directories without specifying specific pages | 'No Crawl' files with specific patterns, for example, files with certain filetypes that always have a certain extension, say pdf |
| [`*` Wildcard Support](/search/docs/crawling-indexing/robots/robots_txt#url-matching-based-on-path-values) | Tells a crawler to match a sequence of characters | 'No Crawl' URLs with certain patterns, for example, disallow URLs with session ids or other extraneous parameters |
| [`Sitemaps` Location](/search/docs/crawling-indexing/sitemaps/overview) | Tells a crawler where it can find your Sitemaps | Point to other locations where feeds exist to help crawlers find URLs on a site |

### HTML `meta` rules

|  |  |  |
| --- | --- | --- |
| **Rule** | **Impact** | **Use cases** |
| [`noindex` `meta` tag](/search/docs/crawling-indexing/block-indexing) | Tells a crawler not to index a given page | Don't index the page. This allows pages that are crawled to be kept out of the index. |
| [`nofollow` `meta` tag](/search/docs/advanced/guidelines/qualify-outbound-links) | Tells a crawler not to follow a link to other content on a given page | Prevent publicly writeable areas to be abused by spammers looking for link credit. By using `nofollow` you let the robot know that you are discounting all outgoing links from this page. |
| [`nosnippet` `meta` tag](/search/docs/crawling-indexing/robots-meta-tag#nosnippet) | Tells a crawler not to display snippets in the search results for a given page | Present no snippet for the page on Search Results |
| [`noarchive` `meta` tag](/search/docs/crawling-indexing/robots-meta-tag#noarchive) | Tells a search engine not to show a "cached" link for a given page | Do not make available to users a copy of the page from the Search Engine cache |
| [`noodp` `meta` tag](/search/docs/crawling-indexing/robots-meta-tag#preventdmoz) | Tells a crawler not to use a title and snippet from the Open Directory Project for a given page | Do not use the ODP (Open Directory Project) title and snippet for this page |

These rules are applicable for all forms of content. They can be placed in either the HTML
of a page or in the HTTP header for non-HTML content, for example, PDF, video, etc. using an
`X-Robots-Tag`. You can read more about it here:
[`X-Robots-Tag` Post](https://googleblog.blogspot.com/2007/07/robots-exclusion-protocol-now-with-even.html)
or in
[our series of posts](https://googleblog.blogspot.com/2007/02/robots-exclusion-protocol.html)
about using robots and `meta` tags.

## Other REP rules

The rules listed above are used by Microsoft, Google, and Yahoo!, but may not be implemented
by all other search engines. In addition, the following rules are supported by Google, but
are not supported by all three as are those above:

**`unavailable_after` `meta` tag** - Tells a crawler
[when a page should "expire"](https://googleblog.blogspot.com/2007/07/robots-exclusion-protocol-now-with-even,html),
that is, after which date it should not show up in search results.

**`noimageindex` `meta` tag** - Tells a crawler
[not to index images for a given page](/search/docs/crawling-indexing/robots-meta-tag#noimageindex)
in search results.

**`notranslate` `meta` tag** - Tells a crawler
[not to translate the content on a page into different languages](/search/docs/crawling-indexing/robots-meta-tag#notranslate)
for search results.

Going forward, we plan to continue to work together to ensure that as new uses of REP arise, we're
able to make it as easy as possible for webmasters to use them. So stay tuned for more!

## Learn more

You can find out more about robots.txt in our
[documentation](/search/docs/crawling-indexing) and at
[Google's Webmaster help center](/search/docs/fundamentals/how-search-works#crawling),
which contains lots of helpful information, including:

- [How to create a robots.txt file](/search/docs/crawling-indexing/robots/create-robots-txt)
- [Descriptions of each user-agent that Google uses](/search/docs/crawling-indexing/overview-google-crawlers)
- [How to use pattern matching](/search/docs/crawling-indexing/robots/robots_txt#url-matching-based-on-path-values)
- [How often we recrawl your robots.txt file](/search/docs/crawling-indexing/robots/submit-updated-robots-txt#refresh-googles-robots.txt-cache)

We've also done several posts in our [webmaster blog](/search/blog) about robots.txt
that you may find useful, such as:

- [Using robots.txt files](/search/blog/2006/02/using-robotstxt-file)
- [All about Googlebot](/search/blog/2006/08/all-about-googlebot)

There is also a
[useful list of the bots](https://www.robotstxt.org/db)
used by the major search engines.

To see what our colleagues have to say, you can also check out the blog posts published by
[Yahoo!](https://www.ysearchblog.com/archives/000587) and
[Microsoft](https://blogs.msdn.com/webmaster/archive/2008/06/03/robots-exclusion-protocol-joining-together-to-provide-better-documentation.aspx).
