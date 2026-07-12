---
title: "How to verify Googlebot"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-09-how-to-verify-googlebot"
url: "https://developers.google.com/search/blog/2006/09/how-to-verify-googlebot"
canonical: "https://developers.google.com/search/blog/2006/09/how-to-verify-googlebot"
author: null
published: "2006-09-20T00:00:00+00:00"
updated: "2006-09-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:46:31+00:00"
status_code: 200
html_hash: "8c1102caa19053aaefb46e4b776cfb06fbc5cfe15d17679fde6016de13998e80"
clean_word_count: 328
clean_char_count: 1857
---
# How to verify Googlebot

Lately I've heard a couple smart
[people](https://www.crazyguyonabike.com/) ask that
search engines provide a way know that a bot is authentic. After all, any spammer could name
their bot "Googlebot" and claim to be Google, so which bots do you trust and which do you block?

The common request we hear is to post a list of Googlebot IP addresses in some public place. The
problem with that is that if/when the IP ranges of our crawlers change, not everyone will know
to check. In fact, the crawl team migrated Googlebot IPs a couple years ago and it was a real
hassle alerting webmasters who had hard-coded an IP range. So the crawl folks have provided
another way to authenticate Googlebot. Here's an answer from one of the crawl people (quoted
with their permission):

> Telling webmasters to use DNS to verify on a case-by-case basis seems like the best way to go. I
> think the recommended technique would be to do a reverse DNS lookup, verify that the name is in
> the googlebot.com domain, and then do a corresponding forward DNS->IP lookup using that
> googlebot.com name. For example:
>
> ```
> > host 66.249.66.1
> 1.66.249.66.in-addr.arpa domain name pointer crawl-66-249-66-1.googlebot.com.
>
> > host crawl-66-249-66-1.googlebot.com
> crawl-66-249-66-1.googlebot.com has address 66.249.66.1
> ```
>
> I don't think just doing a reverse DNS lookup is sufficient, because a spoofer could set up
> reverse DNS to point to `crawl-a-b-c-d.googlebot.com`.

This answer has also been provided to our help-desk, so I'd consider it an official way to
authenticate Googlebot. In order to fetch from the "official" Googlebot IP range, the bot has to
respect robots.txt and our internal hostload conventions so that Google doesn't crawl you too
hard.

(Thanks to N. and J. for help on this answer from the crawl side of things.)
