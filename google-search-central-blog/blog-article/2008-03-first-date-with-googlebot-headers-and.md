---
title: "First date with the Googlebot: Headers and compression"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-03-first-date-with-googlebot-headers-and"
url: "https://developers.google.com/search/blog/2008/03/first-date-with-googlebot-headers-and"
canonical: "https://developers.google.com/search/blog/2008/03/first-date-with-googlebot-headers-and"
author: "Maile Ohye"
published: "2008-03-06T00:00:00+00:00"
updated: "2008-03-06T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:51:37+00:00"
status_code: 200
html_hash: "89a8e576e7076f9d695b05be1ddc82d54a4ce04cfc5fad776244381c49ed1eeb"
clean_word_count: 1339
clean_char_count: 8454
---
# First date with the Googlebot: Headers and compression

![googlebot with flowers](/static/search/blog/images/import/943b5c3cf4d4c8c6d377fd2a731e0a1f.jpg)

**Name/User-Agent**: Googlebot
**IP Address**:
[Learn how to verify Googlebot](/search/docs/crawling-indexing/verifying-googlebot)
**Looking For**: Websites with unique and compelling content
**Major Turn Off**: Violations of the
[Webmaster Guidelines](/search/docs/essentials)
[Googlebot](/search/docs/crawling-indexing/googlebot) —what a dreamboat. It's
like they know us `<head>`, `<body>`, and soul. They're probably
not looking for anything exclusive; they see billions of other sites (though we share our data
with other bots as well), but tonight we'll really get to know each other as website and crawler.

I know, it's never good to over-analyze a first date. We're going to get to know Googlebot a bit
more slowly, in a series of posts:

1. Our first date (tonight!): Headers Googlebot sends, file formats they "notice," whether it's
   better to compress data
2. Judging their response: Response codes (`301`, `302`), how they handle
   redirects and `If-Modified-Since`
3. Next steps: Following links, having them crawl faster or slower (so they don't come on too
   strong)

And tonight is just the first date...

---

**Googlebot:** ACK

**Website:** Googlebot, you're here!

**Googlebot:** I am.

```
GET / HTTP/1.1
Host: example.com
Connection: Keep-alive
Accept: */*
From: googlebot(at)googlebot.com
User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +https://www.google.com/bot.html)
Accept-Encoding: gzip,deflate
```

**Website:** Those headers are so flashy! Would you crawl with the same headers if my site
were in the U.S., Asia or Europe? Do you ever use different headers?

**Googlebot:** My headers are typically consistent world-wide. I'm trying to see what a page
looks like for the default language and settings for the site. Sometimes the
`User-Agent` is different, for instance AdSense fetches use
`Mediapartners-Google`:

```
User-Agent: Mediapartners-Google
```

Or for image search:

```
User-Agent: Googlebot-Image/1.0
```

Wireless fetches often have carrier-specific user agents, whereas Google Reader RSS fetches
include extra info such as number of subscribers.

I usually avoid cookies (so no `Cookie:` header) since I don't want the content
affected too much by session-specific info. And, if a server uses a session id in a dynamic URL
rather than a cookie, I can usually figure this out, so that I don't end up crawling your same
page a million times with a million different session ids.

**Website:** I'm very complex. I have many file types. Your headers say
`Accept: */*`. Do you index all URLs or are certain file extensions automatically
filtered?

**Googlebot:** That depends on what I'm looking for. If I'm indexing for regular web search,
and I see links to MP3s and videos, I probably won't download those. Similarly, if I see a JPG, I
will treat it differently than an HTML or PDF link. For instance, JPG is much less likely to
change frequently than HTML, so I will check the JPG for changes less often to save bandwidth.
Meanwhile, if I'm looking for links as Google Scholar, I'm going to be far more interested in the
PDF article than the JPG file. Downloading doodles (like JPGs) and videos of skateboarding dogs
is distracting for a scholar—do you agree?

**Website:** Yes, they can be distracting. I'm in awe of your dedication. I love doodles (JPGs)
and find them hard to resist.

**Googlebot:** Me, too; I'm not always so scholarly. When I crawl for image search, I'm very
interested in JPGs. And for news, I'm mostly looking at HTML and nearby images.

There are also plenty of extensions (exe, dll, zip, dmg...), that tend to be big and less useful
for a search engine.

**Website:** If you saw my URL, `https://www.example.com/page1.LOL111`, would you
(whimper whimper) reject it just because it contains an unknown file extension?

**Googlebot:** Website, let me give a bit more background. After actually downloading a file, I
use the `Content-Type` header to check whether it really is HTML, an image, text, or
something else. If it's a special data type like a PDF file, Word document, or Excel spreadsheet, I
'll make sure it's in the valid format and extract the text content. Maybe it has a virus; you
never know. If the document or data type is really garbled, there's usually not much to do besides
discard the content.

So, if I'm crawling `https://www.example.com/page1.LOL111` with an unknown file
extension, it's likely that I would start to download it. If I can't figure out the content type
from the header, or it's a format that we don't index (for example, mp3), then it'll be put aside.
Otherwise, we proceed indexing the file.

**Website:** My apologies for scrutinizing your style, Googlebot, but I noticed your
`Accept-Encoding` headers say:

```
Accept-Encoding: gzip,deflate
```

Can you explain these headers to me?

**Googlebot:** Sure. All major search engines and web browsers support gzip compression for
content to save bandwidth. Other entries that you might see here include `x-gzip` (the
same as `gzip`), `deflate` (which we also support), and
`identity` (none).

**Website:** Can you talk more about file compression and
`Accept-Encoding: gzip,deflate`? Many of my URLs consist of big Flash files and
stunning images, not just HTML. Would it help you to crawl faster if I compressed my larger files?

**Googlebot:** There's not a simple answer to this question. First of all, many file formats,
such as swf (Flash), jpg, png, gif, and pdf are already compressed (there are also specialized
Flash optimizers).

**Website:** Perhaps I've been compressing my Flash files and I didn't even know? I'm obviously
very efficient.

**Googlebot:** Both Apache and IIS have options to enable gzip and deflate compression, though
there's a CPU cost involved for the bandwidth saved. Typically, it's only enabled for easily
compressible text HTML/CSS/PHP content. And it only gets used if the user's browser or I (a search
engine crawler) allow it. Personally, I prefer `gzip` over `deflate`. Gzip
is a slightly more robust encoding—there is consistently a checksum and a full header,
giving me less guess-work than with deflate. Otherwise they're very similar compression
algorithms.

If you have some spare CPU on your servers, it might be worth experimenting with compression
(links:
[Apache](https://www.sitepoint.com/article/web-output-mod_gzip-apache),
[IIS](https://www.microsoft.com/technet/prodtechnol/WindowsServer2003/Library/IIS/502ef631-3695-4616-b268-cbe7cf1351ce.mspx?mfr=true)).
But, if you're serving dynamic content and your servers are already heavily CPU loaded, you might
want to hold off.

**Website:** Great information. I'm really glad you came tonight—thank goodness my
[robots.txt](/search/docs/crawling-indexing/robots/intro) allowed it. That file can be like an
over-protective parent!

**Googlebot:** Ah yes; meeting the parents, the robots.txt. I've met plenty of intense ones.
Some are really just HTML error pages rather than valid robots.txt. Some have infinite redirects
all over the place, maybe to totally unrelated sites, while others are just huge and have
thousands of different URLs listed individually. Here's one unfortunate pattern. The site is
normally eager for me to crawl:

```
User-Agent: *
Allow: /
```

Then, during a peak time with high user traffic, the site switches the robots.txt to something
restrictive:

```

User-Agent: *
Disallow: /
```

The problem with the above robots.txt file-swapping is that once I see the restrictive robots.txt,
I may have to start throwing away content I've already crawled in the index. And then I have to
recrawl a lot of content once I'm allowed to crawl the site again. At least a 503 response code
would've been temporary.

I typically only re-check robots.txt once a day (otherwise on many virtual hosting sites, I'd be
spending a large fraction of my fetches just getting robots.txt, and no date wants to "meet the
parents" that often). For webmasters, trying to control crawl rate through robots.txt swapping
usually backfires. It's better to
[set the rate to "slower"](https://support.google.com/webmasters/answer/48620)
in Webmaster Tools.

**Googlebot:** Website, thanks for all of your questions, you've been wonderful, but I'm going
to have to say "FIN, my love."

**Website:** Oh, Googlebot... ACK/FIN.
:)

---
