---
title: "Answers to Friday questions"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-01-answers-to-friday-questions"
url: "https://developers.google.com/search/blog/2006/01/answers-to-friday-questions"
canonical: "https://developers.google.com/search/blog/2006/01/answers-to-friday-questions"
author: "Vanessa Fox"
published: "2006-01-13T00:00:00+00:00"
updated: "2006-01-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:44:29+00:00"
status_code: 200
html_hash: "7479b86288ab5cd9d5546036296e76d20fda55e3a50fabb89a5d01d2867c918e"
clean_word_count: 448
clean_char_count: 2499
---
# Answers to Friday questions

Today, we wanted to review a few things that we get a lot of questions about.

## I tried to verify and I got a message that said "pending verification". Why

If we can't process the verification request right away, we'll add it to a queue and process it as
soon as possible. While your request is in this queue, the status will show as pending. Once we
successfully process your request, your site will show as verified. If the request is
unsuccessful, you'll see a status of "not verified". You can read more about
[reasons the request might not be successful](/search/blog/2005/12/more-query-stats-verification)
or take a look at our
[documentation](https://support.google.com/webmasters/answer/9008080).

## I submitted my Sitemap and it now as a status of "Timed out downloading robots.txt". I don't have a robots.txt file on my site. What happened

Any time we access your site, we first check to see if you have a robots.txt file that restricts
our access. If we get a timeout from your server when we do this check, you'll see this message.
This is probably a temporary problem. Once your server is accessible again, we will be able to see
that you don't have a robots.txt file, and will then access your Sitemap. If you continue to see
this error, make sure that your webserver is up and responding to requests.

## I submitted my sitemap at https://www.example.com/mysite/ and verified it. But now you are asking me to verify at https://www.example.com/. I can't verify at that location because I don't have access. Why are you asking me to do this

Some stats we can only show if you
[verify at the root level](/search/blog/2005/12/verifying-site-located-in-subdirectory).
If you don't have access to this location, we will
[show you all the information we are able to](https://support.google.com/webmasters/answer/9008080)
(such as errors we had crawling your site). Verification doesn't impact Sitemap submission or
indexing in any way, and there is no penalty if you can't verify at the root level.

## I've submitted my Sitemap, verified my site, and you've downloaded my Sitemap, but many of my stats show "Data is not available at the time time". Why?

We show you stats about what we know about your site. If we haven't yet crawled and indexed much
of your site, we may not have many stats to show you. As we crawl more of your site and learn
more about it,
[you'll start to see more stats](/search/blog/2005/11/if-you-dont-see-full-range-of-stats).
