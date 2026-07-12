---
title: "Reorganizing internal vs. external backlinks"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-08-reorganizing-internal-vs-external"
url: "https://developers.google.com/search/blog/2011/08/reorganizing-internal-vs-external"
canonical: "https://developers.google.com/search/blog/2011/08/reorganizing-internal-vs-external"
author: "Susan Moskwa"
published: "2011-08-31T00:00:00+00:00"
updated: "2011-08-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:14:44+00:00"
status_code: 200
html_hash: "d18e2d16408ae8ddfc16bee3d1aef2d0a9b234ddf28a9caa09ad6e02c447292c"
clean_word_count: 580
clean_char_count: 3579
---
# Reorganizing internal vs. external backlinks

Today we're making a change to the way we categorize link data in
[Webmaster Tools](https://search.google.com/search-console).
As you know, Webmaster Tools lists links pointing to your site in two separate categories:
[links coming from other sites](https://www.google.com/support/webmasters/bin/answer.py?answer=55281),
and
[links from within your site](https://www.google.com/support/webmasters/bin/answer.py?answer=138752).
Today's update won't change your total number of links, but will hopefully present your backlinks
in a way that more closely aligns with your idea of which links are actually from your site vs.
from other sites.

You can manage many different types of sites in Webmaster Tools: a plain domain name
(`example.com`), a subdomain (`www.example.com` or
`cats.example.com`), or a domain with a subfolder path
(`www.example.com/cats/` or `www.example.com/users/catlover/`). Previously,
only links that started with your site's exact URL would be categorized as internal links: so if
you entered `www.example.com/users/catlover/` as your site, links from
`www.example.com/users/catlover/profile.html` would be categorized as internal, but
links from `www.example.com/users/` or `www.example.com` would be
categorized as external links. This also meant that if you entered `www.example.com`
as your site, links from `example.com` would be considered external because they don't
start with the same URL as your site (they don't contain `www`).

Most people think of `example.com` and `www.example.com` as the same site
these days, so we're changing it such that now, if you add either `example.com` or
`www.example.com` as a site, links from both the www and non-www versions of the
domain will be categorized as internal links. We've also extended this idea to include other
subdomains, since many people who own a domain also own its subdomains—so links from
`cats.example.com` or `pets.example.com` will also be categorized as
internal links for `www.example.com`.

|  |  |  |
| --- | --- | --- |
| **Links for `www.google.com`** | External links | Internal links |
| Previously categorized as... | `www.example.com/`  `www.example.org/stuff.html`  `scholar.google.com/`  `sketchup.google.com/`  `google.com/` | `www.google.com/`  `www.google.com/stuff.html`  `www.google.com/support/webmasters/` |
| Now categorized as... | `www.example.com/`  `www.example.org/stuff.html` | `scholar.google.com/`  `sketchup.google.com/`  `google.com/`  `www.google.com/`  `www.google.com/stuff.html`  `www.google.com/support/webmasters/` |

If you own a site that's on a subdomain (such as
[`search.google.com/`](https://search.google.com/)) or
in a subfolder
([`www.google.com/support/webmasters/`](https://support.google.com/webmasters))
and don't own the root domain, you'll still only see links from URLs starting with that subdomain
or subfolder in your internal links, and all others will be categorized as external links.
We've made a few backend changes so that these numbers should be even more accurate for you.

Note that, if you own a root domain like `example.com` or `www.example.com`,
your number of external links may appear to go down with this change; this is because, as
described above, some of the URLs we were previously classifying as external links will have moved
into the internal links report. Your total number of links (internal + external) should not be
affected by this change.

As always, join our
[Webmaster Help Forum](https://support.google.com/webmasters/community)
if you have questions!
