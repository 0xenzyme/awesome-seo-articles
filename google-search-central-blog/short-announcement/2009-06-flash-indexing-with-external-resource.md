---
title: "Flash indexing with external resource loading"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2009-06-flash-indexing-with-external-resource"
url: "https://developers.google.com/search/blog/2009/06/flash-indexing-with-external-resource"
canonical: "https://developers.google.com/search/blog/2009/06/flash-indexing-with-external-resource"
author: "Written by Janis Stipins, Software Engineer"
published: "2009-06-19T00:00:00+00:00"
updated: "2009-06-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:58:33+00:00"
status_code: 200
html_hash: "ef05d1402630cda10e75afdc2bf47fc9c804700cc31285570e161e0756de094c"
clean_word_count: 256
clean_char_count: 1622
---
# Flash indexing with external resource loading

We just added external resource loading to our
[Flash indexing](/search/blog/2008/06/improved-flash-indexing)
capabilities. This means that when a SWF file loads content from some other file—whether it's
text, HTML, XML, another SWF, etc.—we can index this external content too, and associate it with
the parent SWF file and any documents that embed it.

This new capability improves search quality by allowing relevant content contained in external
resources to appear in response to users' queries. For example, this result currently comes up in
response to the query
[2002 VW Transporter 888](https://www.google.com/search?q=2002+VW+Transporter+888):

![a search result with the query bolded](/static/search/blog/images/import/08aefe8deb980784e67b9fc9c9e7a33a.png)

Prior to this launch, this result did not appear, because all of the relevant content is contained
in an XML file loaded by a SWF file.

To date, when Google encounters SWF files on the web, we can:

- Index textual content displayed as a user interacts with the file. We click buttons and enter
  input, just like a user would.
- Discover links within Flash files.
- Load external resources and associate the content with the parent file.
- Support common JavaScript techniques for embedding Flash, such as `SWFObject` and
  `SWFObject2`.
- Index sites scripted with AS1 and AS2, even if the ActionScript is obfuscated.

If you don't want your SWF file or any of its external resources crawled by search engines, please
use an appropriate [robots.txt rule](/search/docs/crawling-indexing/robots/intro).
