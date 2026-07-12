---
title: "More query stats; verification enhancements"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2005-12-more-query-stats-verification"
url: "https://developers.google.com/search/blog/2005/12/more-query-stats-verification"
canonical: "https://developers.google.com/search/blog/2005/12/more-query-stats-verification"
author: "Vanessa Fox"
published: "2005-12-13T00:00:00+00:00"
updated: "2005-12-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T12:44:21+00:00"
status_code: 200
html_hash: "814f3094d4fbe14ba99642939e916ed269acb5bbda29aa29da06af0b66103578"
clean_word_count: 399
clean_char_count: 2402
---
# More query stats; verification enhancements

We've made a few improvements that we wanted to let you know about.

## Expanded query stats

We've expanded the number of
[query stats](https://support.google.com/webmasters/answer/9008080#query_stats)
that we show you (both top search queries and top search query clicks). Note that the exact number
of stats you see depends on how often your site comes up in search results. A large site that has
been around for a while will generally have more stats than a new, smaller site.

## Verification enhancements

We've also been working on the
[verification process](https://support.google.com/webmasters/answer/9008080).
Last month, we posted to the
[Group](https://support.google.com/webmasters/community)
that we were looking for your input on how to improve this process. Yesterday, we told you that we
[added support for lowercase verification filenames](/search/blog/2005/12/lowercase-verification-filenames).
Now, we've added another improvement. Some of you have received one of the following messages
when you try to verify:

**Our system has experienced a temporary problem.**

Or:

**The system is currently busy. Please try again in a few minutes.**

In the past, you've had to manually try again later. Now, instead of seeing one of those messages,
you'll see this message:

**The system is currently busy. We will process this verification as soon as possible. Please
check back later for an updated status.**

We'll add your verification request to a queue and try it for you later, so that you don't have to
keep trying manually.

If you receive another error that might be due to a temporary issue (for instance, if we can't
reach your server due to a DNS timeout), we'll show you the error, but we'll also add your
verification request to the queue.

- While your request is in the queue, you'll see "PENDING" as the status in the Verify tab.
- Once we've processed the request successfully, we will display your site as verified and you can
  access your stats.
- If we aren't able to successfully process the request, you'll see "NOT VERIFIED" as the status
  in the Verify tab. If you see this, check that your verification file is in the correct
  location, is named exactly as we ask, that your robots.txt file doesn't block access, and that
  your server is up and responding to requests. Then, try your verification request again.
