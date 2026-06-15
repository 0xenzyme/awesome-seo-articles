---
title: "Clarifications about the SharedArrayBuffer object message"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2021-03-sharedarraybuffer-notes"
url: "https://developers.google.com/search/blog/2021/03/sharedarraybuffer-notes"
canonical: "https://developers.google.com/search/blog/2021/03/sharedarraybuffer-notes"
author: "Eiji Kitamura"
published: "2021-03-19T00:00:00+00:00"
updated: "2021-03-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:38:31+00:00"
status_code: 200
html_hash: "402bb0114cf2638f18116ae3e39664605becf5c2aecb15e555e5484691897621"
clean_word_count: 520
clean_char_count: 3566
---
# Clarifications about the SharedArrayBuffer object message

Some of you might have received an email from Google Search Console with the subject "New requirements for `SharedArrayBuffers`".
We received feedback that the message was confusing, and wanted to give some more insight into the issue, so that you can decide which next steps are appropriate.
We also updated [the guide on enabling cross-origin isolation](https://web.dev/articles/cross-origin-isolation-guide) to include additional details.

## Why did I receive the message?

You received the message because we've detected that JavaScript on your website was using the [`SharedArrayBuffer`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) object at the time of the message.
The usage might be due to frameworks, libraries, or other third-party content included within your website.

## What is the `SharedArrayBuffer`?

`SharedArrayBuffer` is a JavaScript object to share a memory space across threads on a website.
It was used by websites before the vulnerability called [Spectre](/web/updates/2018/02/meltdown-spectre) was found.
However, because Spectre was a CPU level vulnerability and it's unlikely to be fixed in the foreseeable future, browsers decided to disable the `SharedArrayBuffer` object.

While Chrome re-enabled it on desktop with [Site Isolation](https://security.googleblog.com/2018/07/mitigating-spectre-with-site-isolation.html) as a temporary remedy, [cross-origin isolation](https://web.dev/articles/coop-coep) was standardized as a way to safely enable the `SharedArrayBuffer` object.
Starting with version 92, planned to be released in late May 2021, Chrome will gate the `SharedArrayBuffer` object behind cross-origin isolation.
Firefox enabled the `SharedArrayBuffer` object on a cross-origin isolated environment as well in version 76.
We hope other browsers will follow soon.

## Finding `SharedArrayBuffer` object usage on your site

You have two options:

1. Use [Chrome DevTools](/web/tools/chrome-devtools) and inspect important pages.
2. (Advanced) Use the [Reporting API](/web/updates/2018/09/reportingapi) to send deprecation reports to a reporting endpoint.

Learn how to take the above approaches at [Determine where the `SharedArrayBuffer` object is used on your website](https://web.dev/articles/cross-origin-isolation-guide).

## Next steps

For next steps, we recommend:

1. Determine where the `SharedArrayBuffer` object is used on your website.
2. Decide if the usage is necessary.
3. Fix the issue by either removing the functionality, or by [enabling cross-origin isolation](https://web.dev/articles/cross-origin-isolation-guide).

If you haven't heard about the `SharedArrayBuffer` object, and you received a Search Console message about it, it's highly likely a third-party resource on your website is using it.
Once you determine which pages are affected, and who the owner of the resource is, reach out to the resource provider and ask them to fix the issue.

After Chrome 92 is released, the `SharedArrayBuffer` object without cross-origin isolation will no longer be functional.
In practice, this means that Chrome users on your site may experience degraded performance similar to other situations where the `SharedArrayBuffer` object is not supported.

We hope this clarification was useful, even if you didn't receive the message.
If you have any questions, we'd recommend posting in the [Search Central help community](https://support.google.com/webmasters/community) to get input from other experts.
