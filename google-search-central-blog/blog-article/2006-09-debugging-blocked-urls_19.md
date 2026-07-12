---
title: "Debugging blocked URLs"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-09-debugging-blocked-urls_19"
url: "https://developers.google.com/search/blog/2006/09/debugging-blocked-urls_19"
canonical: "https://developers.google.com/search/blog/2006/09/debugging-blocked-urls_19"
author: null
published: "2006-09-19T00:00:00+00:00"
updated: "2006-09-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:46:25+00:00"
status_code: 200
html_hash: "919a71bc93d08475cb462ee77124433d225df4f01919d7ef3d69901fce7d26c1"
clean_word_count: 777
clean_char_count: 4356
---
# Debugging blocked URLs

Vanessa's been posting a lot lately, and I'm starting to feel left out. So here my tidbit of
wisdom for you: I've noticed a couple of webmasters confused by
"[blocked by robots.txt](https://support.google.com/webmasters/answer/7440203#submitted_but_blocked)"
errors, and I wanted to share the steps I take when debugging
[robots.txt](/search/docs/crawling-indexing/robots/intro) problems:

## A handy checklist for debugging a blocked URL

Let's assume you are looking at crawl errors for your website and notice a URL restricted by
robots.txt that you weren't intending to block:

```
https://www.example.com/amanda.html    URL restricted by robots.txt     Sep 3, 2006
```

## Check the robots.txt analysis tool

The first thing you should do is go to the
[robots.txt analysis tool](https://www.google.com/webmasters/tools/robots-testing-tool)
for that site. Make sure you are looking at the correct site for that URL, paying attention that
you are looking at the right protocol and subdomain. (Subdomains and protocols may have their own
robots.txt file, so `https://www.example.com/robots.txt` may be different from
`https://example.com/robots.txt` and may be different from
`https://amanda.example.com/robots.txt.`) Paste the blocked URL into the "Test URLs
against this robots.txt file" box. If the tool reports that it is blocked, you've found your
problem. If the tool reports that it's allowed, we need to investigate further.

At the top of the robots.txt analysis tool, take a look at the
[HTTP status code](/search/docs/crawling-indexing/http-network-errors).
If we are reporting anything other than a `200 (Success)` or a
`404 (Not found)` then we may not be able to reach your robots.txt file, which stops
our crawling process. (Note that you can see the last time we downloaded your robots.txt file at
the top of this tool. If you make changes to your file, check this date and time to see if your
changes were made after our last download.)

## Check for changes in your robots.txt file

If these look fine, you may want to check and see if your robots.txt file has changed since the
error occurred by checking the date to see when your robots.txt file was last modified. If it
was modified after the date given for the error in the crawl errors, it might be that someone
has changed the file so that the new version no longer blocks this URL.

## Check for redirects of the URL

If you can be certain that this URL isn't blocked, check to see if the URL redirects to another
page. When Googlebot fetches a URL, it checks the robots.txt file to make sure it is allowed to
access the URL. If the robots.txt file allows access to the URL, but the URL returns a redirect,
Googlebot checks the robots.txt file again to see if the destination URL is accessible. If at any
point Googlebot is redirected to a blocked URL, it reports that it could not get the content of
the original URL because it was blocked by robots.txt.

Sometimes this behavior is easy to spot because a particular URL always redirects to another
one. But sometimes this can be tricky to figure out. For instance:

- Your site may not have a robots.txt file at all (and therefore, allows access to all pages),
  but a URL on the site may redirect to a different site, which does have a robots.txt file. In
  this case, you may see URLs blocked by robots.txt for your site (even though you don't have a
  robots.txt file).
- Your site may prompt for registration after a certain number of page views. You may have the
  registration page blocked by a robots.txt file. In this case, the URL itself may not redirect,
  but if Googlebot triggers the registration prompt when accessing the URL, it will be redirected
  to the blocked registration page, and the original URL will be listed in the crawl errors page
  as blocked by robots.txt.

## Ask for help

Finally, if you still can't pinpoint the problem, you might want to post on our
[forum](https://support.google.com/webmasters/community)
for help. Be sure to include the URL that is blocked in your message. Sometimes its easier for
other people to notice oversights you may have missed.

Good luck debugging! And by the way—unrelated to robots.txt—make sure that you don't
have `noindex` `meta` tags at the top of your web pages; those also result in Google not
showing a web site in our index.
