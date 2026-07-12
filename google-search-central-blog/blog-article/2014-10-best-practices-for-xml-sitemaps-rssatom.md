---
title: "Best practices for XML sitemaps and RSS/Atom feeds"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-10-best-practices-for-xml-sitemaps-rssatom"
url: "https://developers.google.com/search/blog/2014/10/best-practices-for-xml-sitemaps-rssatom"
canonical: "https://developers.google.com/search/blog/2014/10/best-practices-for-xml-sitemaps-rssatom"
author: "Alkis Evlogimenos, Google Feeds Team"
published: "2014-10-16T00:00:00+00:00"
updated: "2014-10-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:25:35+00:00"
status_code: 200
html_hash: "9c2c850fa401f9e8597b323fb0c11ecd3334fb0c2cc34ea3e96092a3bbabc584"
clean_word_count: 1029
clean_char_count: 6495
---
# Best practices for XML sitemaps and RSS/Atom feeds

[Submitting sitemaps](https://support.google.com/webmasters/answer/183669)
can be an important part of optimizing websites. Sitemaps enable search engines to discover all
pages on a site and to download them quickly when they change. This blog post explains which
fields in sitemaps are important, when to use XML sitemaps and RSS/Atom feeds, and how to
optimize them for Google.

## Sitemaps and feeds

Sitemaps can be in [XML sitemap](https://www.sitemaps.org),
[RSS](https://en.wikipedia.org/wiki/RSS), or
[Atom](https://en.wikipedia.org/wiki/Atom_(standard)) formats. The
important difference between these formats is that XML sitemaps describe the whole set of URLs
within a site, while RSS/Atom feeds describe recent changes. This has important implications:

- XML sitemaps are usually large; RSS/Atom feeds are small, containing only the most recent
  updates to your site.
- XML sitemaps are downloaded less frequently than RSS/Atom feeds.

For optimal crawling, we recommend using both XML sitemaps and RSS/Atom feeds. XML sitemaps will
give Google information about all of the pages on your site. RSS/Atom feeds will provide all
updates on your site, helping Google to keep your content fresher in its index. Note that
submitting sitemaps or feeds does not guarantee the indexing of those URLs.

Example of an XML sitemap:

```
<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
 <url>
   <loc>https://example.com/mypage</loc>
   <lastmod>2011-06-27T19:34:00+01:00</lastmod>
   <!-- optional additional tags -->
 </url>
 <url>
   ...
 </url>
</urlset>
```

Example of an RSS feed:

```
<?xml version="1.0" encoding="utf-8"?>
  <rss>
   <channel>
     <!-- other tags -->
     <item>
       <!-- other tags -->
       <link>https://example.com/mypage</link>
       <pubDate>Mon, 27 Jun 2011 19:34:00 +0100</pubDate>
     </item>
     <item>
       ...
     </item>
   </channel>
 </rss>
```

Example of an Atom feed:

```
<?xml version="1.0" encoding="utf-8"?>
  <feed xmlns="https://www.w3.org/2005/Atom">
   <!-- other tags -->
   <entry>
     <link href="https://example.com/mypage" />
     <updated>2011-06-27T19:34:00+01:00</updated>
     <!-- other tags -->
   </entry>
   <entry>
     ...
   </entry>
  </feed>
```

"other tags" refer to both optional and required tags by their
respective standards. We recommend that you specify the required tags for Atom/RSS as they will
help you to appear on other properties that might use these feeds, in addition to Google Search.

## Best practices

### Important fields

XML sitemaps and RSS/Atom feeds, in their core, are lists of URLs with metadata attached to
them. The two most important pieces of information for Google are the URL itself and its last
modification time:

#### URLs

URLs in XML sitemaps and RSS/Atom feeds should adhere to the following guidelines:

- Only include URLs that can be fetched by
  [Googlebot](/search/docs/crawling-indexing/googlebot). A common mistake is
  including URLs disallowed by robots.txt—which cannot be fetched by Googlebot, or including
  URLs of pages that don't exist.
- Only include [canonical](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  URLs. A common mistake is to include URLs of duplicate pages. This increases the load on your
  server without improving indexing.

#### Last modification time

Specify a last modification time for each URL in an XML sitemap and RSS/Atom feed. The last
modification time should be the last time the content of the page changed meaningfully. If a
change is meant to be visible in the search results, then the last modification time should be
the time of this change.

- XML sitemap uses  `<lastmod>`
- RSS uses `<pubDate>`
- Atom uses `<updated>`

Be sure to set or update last modification time correctly:

- Specify the time in the correct format:
  [W3C Datetime](https://www.w3.org/TR/NOTE-datetime) for XML sitemaps,
  [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) for Atom and
  [RFC822](https://www.w3.org/Protocols/rfc822/) for RSS.
- Only update modification time when the content changed meaningfully.
- Don't set the last modification time to the current time whenever the sitemap or feed is
  served.

### XML sitemaps

XML sitemaps should contain URLs of all pages on your site. They are often large and update
infrequently. Follow these guidelines:

- For a single XML sitemap: update it at least once a day (if your site changes regularly) and
  [ping](https://www.sitemaps.org/protocol.html#submit_ping) Google
  after you update it.
- For a set of XML sitemaps: maximize the number of URLs in each XML sitemap. The limit is
  50,000 URLs or a maximum size of 10MB uncompressed, whichever is reached first.
  [Ping](https://www.sitemaps.org/protocol.html#submit_ping) Google
  for each updated XML sitemap (or once for the sitemap index, if that's used) every time it is
  updated. A common mistake is to put only a handful of URLs into each XML sitemap file, which
  usually makes it harder for Google to download all of these XML sitemaps in a reasonable time.

### RSS/Atom

RSS/Atom feeds should convey recent updates of your site. They are usually small and updated
frequently. For these feeds, we recommend:

- When a new page is added or an existing page meaningfully changed, add the URL and the
  modification time to the feed.
- In order for Google to not miss updates, the RSS/Atom feed should have all updates in it since
  at least the last time Google downloaded it. The best way to achieve this is by using
  [WebSub](https://www.w3.org/TR/websub/).
  The hub will propagate the content of your feed to all interested parties (RSS readers, search
  engines, etc.) in the fastest and most efficient way possible.

Generating both XML sitemaps and Atom/RSS feeds is a great way to optimize crawling of a site
for Google and other search engines. The key information in these files is the canonical URL and
the time of the last modification of pages within the website. Setting these properly, and
notifying Google and other search engines through sitemaps pings and WebSub, will allow your
website to be crawled optimally, and represented accordingly in search results.

If you have any questions, you can post them here, or to join other webmasters in the
[webmaster help forum section on sitemaps](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:search_console)).
