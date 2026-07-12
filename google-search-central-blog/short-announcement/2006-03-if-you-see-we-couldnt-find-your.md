---
title: "If you see a \"we couldn't find your verification file\" error when you try to verify"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-03-if-you-see-we-couldnt-find-your"
url: "https://developers.google.com/search/blog/2006/03/if-you-see-we-couldnt-find-your"
canonical: "https://developers.google.com/search/blog/2006/03/if-you-see-we-couldnt-find-your"
author: "Vanessa Fox"
published: "2006-03-09T00:00:00+00:00"
updated: "2006-03-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:44:56+00:00"
status_code: 200
html_hash: "9b5f73afa624d9d721e6df3caaf78d4f4fd29d0162c3cd2cb6cd94d96b7d0df1"
clean_word_count: 259
clean_char_count: 1485
---
# If you see a "we couldn't find your verification file" error when you try to verify

When you
[verify site ownership](https://support.google.com/webmasters/answer/9008080),
we check to see if the verification file exists on your webserver. We also make sure that your
server returns a status of `404 (not found)` when we request a file that doesn't exist.
We do this to make sure that when we check to see if the verification file exists, we're getting
the right response because it does exist and not because the server is misconfigured.

Some of you have gotten the following message when trying to verify your site:
**"We couldn't find your verification file. Make sure it is named correctly and is
uploaded to the correct location."** But when you check the file in a browser, it does
exist.

We have looked into this and have found that we are displaying the incorrect error message. What
is actually happening in this case is that when we request a file that doesn't exist, we are
getting a response other than `404` or `200`. (If we get a response of
`200`, we display a
[different error message](/search/blog/2005/09/verifying-your-site-trouble-with-404).)

We are working to display the correct response for these cases. In the meantime, if you see this
message when you try to verify and your verification does exist in the correct location, check
your webserver configuration and make sure that it returns a status of `404` when a
request is made for a non-existent page.
