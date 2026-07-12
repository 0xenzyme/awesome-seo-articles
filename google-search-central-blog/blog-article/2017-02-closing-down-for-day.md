---
title: "Closing down for a day"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2017-02-closing-down-for-day"
url: "https://developers.google.com/search/blog/2017/02/closing-down-for-day"
canonical: "https://developers.google.com/search/blog/2017/02/closing-down-for-day"
author: "John Mueller"
published: "2017-02-28T00:00:00+00:00"
updated: "2017-02-28T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:30:05+00:00"
status_code: 200
html_hash: "135dd9bc4f247b9cd06a023dbdf659edfce91952aba48dca63fd42b588cc5e6f"
clean_word_count: 531
clean_char_count: 3248
---
# Closing down for a day

Even in today's "always-on" world, sometimes businesses want to take a break. There are times when
even their online presence needs to be paused. This blog post covers some of the available options
so that a site's search presence isn't affected.

![](/static/search/blog/images/import/17a8b2eec8b1a4d0fb0189abd79d513e.png)

## Option: Block cart functionality

If a site only needs to block users from buying things, the simplest approach is to disable that
specific functionality. In most cases, shopping cart pages can either be blocked from crawling
through the
[robots.txt file](/search/docs/crawling-indexing/robots/intro), or blocked from indexing with a
[robots `meta` tag](/search/docs/crawling-indexing/block-indexing). Since search engines
either won't see or index that content, you can communicate this to users in an appropriate way.
For example, you may disable the link to the cart, add a relevant message, or display an
informational page instead of the cart.

## Option: Always show interstitial or pop-up

If you need to block the whole site from users, be it with a "temporarily unavailable" message,
informational page, or popup, the server should return a
[`503` HTTP result code](/search/blog/2011/01/how-to-deal-with-planned-site-downtime)
("`Service Unavailable`"). The `503` result code makes sure that Google
doesn't index the temporary content that's shown to users. Without the `503` result
code, the interstitial would be indexed as your website's content.

Googlebot will retry pages that return `503` for up to about a week, before treating it
as a permanent error that can result in those pages being dropped from the search results. You can
also include a
[`Retry after` header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37)
to indicate how long the site will be unavailable. Blocking a site for longer than a week can have
negative effects on the site's search results regardless of the method that you use.

## Option: Switch whole website off

Turning the server off completely is another option. You might also do this if you're physically
moving your server to a different data center. For this, have a temporary server available to
serve a
[`503` HTTP result code](/search/blog/2011/01/how-to-deal-with-planned-site-downtime)
for all URLs (with an appropriate informational page for users), and switch your DNS to point to
that server during that time.

1. Set your
   [DNS TTL](https://en.wikipedia.org/wiki/Time_to_live#DNS_records)
   to a low time (such as 5 minutes) a few days in advance.
2. Change the DNS to the temporary server's IP address.
3. Take your main server offline once all requests go to the temporary server.
4. Your server is now offline ...
5. When ready, bring your main server online again.
6. Switch DNS back to the main server's IP address.
7. Change the DNS TTL back to normal.

We hope these options cover the common situations where you'd need to disable your website
temporarily. If you have any questions, you can drop by our webmaster help forums!

PS: If your business is active locally, make sure to reflect these closures in the
[opening hours](https://support.google.com/business/answer/6303076)
for your local listings too!
