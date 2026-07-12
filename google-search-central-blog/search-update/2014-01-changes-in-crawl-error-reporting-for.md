---
title: "Changes in crawl error reporting for redirects"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2014-01-changes-in-crawl-error-reporting-for"
url: "https://developers.google.com/search/blog/2014/01/changes-in-crawl-error-reporting-for"
canonical: "https://developers.google.com/search/blog/2014/01/changes-in-crawl-error-reporting-for"
author: "John Mueller"
published: "2014-01-22T00:00:00+00:00"
updated: "2014-01-22T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:23:31+00:00"
status_code: 200
html_hash: "4d0b00f75071c522512bdeb913fc115c596aa399188015eff45e53d06e608e7f"
clean_word_count: 373
clean_char_count: 2217
---
# Changes in crawl error reporting for redirects

In the past, we have seen occasional confusion by webmasters regarding how
[crawl errors](https://support.google.com/webmasters/answer/35120)
on redirecting pages were shown in
[Webmaster Tools](https://search.google.com/search-console).
It's time to make this a bit clearer and easier to diagnose! While it used to be that we would
report the error on the original—redirecting—URL, we'll now show the error on the
final URL—the one that actually returns the error code.

Let's look at an example:

![](/static/search/blog/images/import/251bc989fcec52740b6f82fa08e1c07d.png)

URL A redirects to URL B, which in turn returns an error. The type of redirect, and type of error
is unimportant here.

In the past, we would have reported the error observed at the end under URL A. Now, we'll instead
report it as URL B. This makes it much easier to diagnose the crawl errors as they're shown in
Webmaster Tools. Using tools like
[cURL](https://www.google.com/search?q=curl) or your favorite
[online server header checker](https://www.google.com/search?q=http+header+viewer),
you can now easily confirm that this error is actually taking place on URL B.

This change may also be visible in the total error counts for some websites. For example, if your
site is moving to a new domain, you'll only see these errors for the new domain (assuming the old
domain redirects correctly), which might result in noticeable changes in the total error counts
for those sites.

Note that this change only affects how these crawl errors are shown in Webmaster Tools. Also,
remember that having crawl errors for URLs that should be returning errors (for example, they
don't exist)
[does not negatively affect the rest of the website's indexing or ranking](/search/blog/2011/05/do-404s-hurt-my-site)
(also as [discussed on Google+](https://plus.google.com/+JohnMueller/posts/RMjFPCSs5fm)).

We hope this change makes it a bit easier to track down crawl errors, and to clean up the
accidental ones that you weren't aware of! If you have any questions, drop by in the
[Google Webmaster Help Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:search_console)).
