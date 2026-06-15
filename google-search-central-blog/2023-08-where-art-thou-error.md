---
title: "The comedy of errors"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2023-08-where-art-thou-error"
url: "https://developers.google.com/search/blog/2023/08/where-art-thou-error"
canonical: "https://developers.google.com/search/blog/2023/08/where-art-thou-error"
author: "Gary Illyes"
published: "2023-08-24T00:00:00+00:00"
updated: "2023-08-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
fetched_at: "2026-06-14T13:42:31+00:00"
status_code: 200
html_hash: "48bec0dade7c7152a97ff59e53559729dadfaee39643b8206201b8981e2a7326"
clean_word_count: 1097
clean_char_count: 6505
---
# The comedy of errors

Every now and then we get questions about errors that we may have shown for sites in Search
Console, and every now and then we encounter folks who seem to be confused about where an error
came from. This is understandable: there are many issues that can arise when accessing websites,
but all of them, without exception, map to a certain system that makes the access possible. In
this illustrated short story we will try to shed some light on the errors and perhaps make them
look a little less scary. Let's dig in!

## Prologue

I like books, so when I was little, while people dreamt of becoming astronauts and firefighters, I
wanted to open a library. In a castle. But then I started thinking about all the problems people
might encounter while getting to my new library and while browsing the books on the shelves. You
see, my castle is located in a far off place and I've been making additions to it every year
(hello moat), causing problems for the local cartographer.

## Chapter 1: DNS errors

Since we're talking about a castle, the location is a little obscure and hard to find. No worries
though: people can use maps. But what if it's an outdated map without my moat, or it's an old map
and most of the letters have rubbed away?

![stick figure is examining a map and can't find the path to the library](/static/search/blog/images/sticks/stick-no-path.jpg)

This is what DNS errors are (contrary to popular belief, unrelated to
Dungeons N Snakes or
Dangerous Navigation System): your clients consult a map (a DNS
server), but they cannot find the location for various reasons. The reason may be that the map
doesn't even have the location of the library (so called
[`NXDOMAIN`](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6)
error in DNS terms) or the language is not legible for the user (loosely,
[`FormErr`](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6)
in DNS terms).

DNS errors are most often caused by some setting—or lack of thereof—on the DNS server.
This means that unless you manage the DNS server yourself (you draw the map for your patrons), you
will have to contact your DNS provider (or local cartographer) to fix the errors. If you don't
know who your DNS provider is, try to ask your hosting provider or wherever you registered your
domain name.

While there may be issues on the client's side, too, for example if they forgot their spectacles
and can't see the letters on the map, it's more likely that the issue is with the map itself.

## Chapter 2: network errors

Once our brave patron knows the path to the castle library, actually getting there can be really
quite an adventure: navigating dungeons, crossing the sea of piranhas in my moat, and yes,
sometimes fighting dragons.

![stick figure can't go to the library because the bridge is broken](/static/search/blog/images/sticks/stick-broken-bridge.jpg)

Network errors are like obstacles for our patrons: network components between the client (browser,
crawlers, etc.) and the server are blocking the traffic. The blocking may be accidental, for
example if a major router goes down, or intentional, like a firewall blocking traffic.

Debugging the situation is as unpleasant as stubbing a toe, unfortunately: you need to identify
which component in the route from the client to the server is doing the blocking. Unfortunately
there can be dozens of independent components in the route, most of them managed by neither the
client or the server, and there's no shortcut for spotting which component is blocking the path.
Fortunately, though, the blocking is usually caused by a firewall either right before the server
or at your CDN's end; getting in touch with your hosting provider or CDN is the right thing to do
if you're not comfortable messing with your firewall.

## Chapter 3: server errors

Even if our patrons reach the library, the library itself may have issues, though. For example,
maybe the library cards are water damaged and it's impossible to find books anymore, or even worse
the dragon the patrons were fighting enroute to the library may have set the whole building
ablaze.

![stick figure can't use the library because it's in flames](/static/search/blog/images/sticks/stick-fire.jpg)

These are essentially your server errors: there's something wrong with the service that makes it
impossible for visitors to get the content (book) they're looking for. If you can't figure out
what's causing it, get in touch with your server manager or your hosting provider. Unfortunately
the clients can't do anything about it though; they'll have to leave without checking out a book.

## Chapter 4: client errors

Once in the library, sometimes our bookworm patrons may ask for novels that are either not
available (because another reader already checked them out) or simply not allowed to access
(because they're locked in the forbidden section). These are client errors: they requested the
wrong thing in some sense, though the wrong thing might just be something that you don't have on
the shelves right now.

![stick figure is at the library looking for book number 7, but can't find it. It seems to be not on the shelves, or in an illegible font.](/static/search/blog/images/sticks/stick-no-book.jpg)

Other times, the tome they seek is in the forbidden section of the library and the patron needs to
satisfy some criteria, for example recite a passphrase to enter the section.

![stick figure is at the library, but not allowed to check out the book because it's behind a forbidden door](/static/search/blog/images/sticks/stick-no-entry.jpg)

In a nutshell, all client errors are technically down to the client to fix: you can help them by
redirecting the URL (recommending an alternative book), but most often the clients' request is
just impossible to fulfill.

## Epilogue

Alls well that ends well: if clients can jump through all these hoops to get in the library, find
the book and check it out, they can finally enjoy reading about their favorite sparkling vampire.
Or your content, if you're a site owner.

If you're craving a deeper explanation of errors and how they relate to Google Search,
[check out our documentation](/search/docs/crawling-indexing/http-network-errors). If
you like my stick figures or have ideas about where they should go next, chat with us on our
[@googlesearchc](https://twitter.com/googlesearchc) handle or in
our [community forums](https://goo.gle/sc-forum).
