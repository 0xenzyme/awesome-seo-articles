---
title: "Site Audit Issues Update (September 2021)"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "high"
slug: "site-audit-issues-update-september-2021"
url: "https://ahrefs.com/blog/site-audit-issues-update-september-2021/"
canonical: "https://ahrefs.com/blog/site-audit-issues-update-september-2021/"
author: "Rebekah Bek"
published: "2021-09-20T01:49:53+00:00"
updated: "2023-01-30T21:44:07+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2023_aging"
  - "product_or_tool_content"
  - "time_sensitive_title"
  - "title_year_2021_before_2026"
fetched_at: "2026-06-12T12:10:01+00:00"
status_code: 200
html_hash: "75a881cf6b243c0fb9dd9526416a40726ccfc751e33b97bdb0ebfdcdc2ed8018"
clean_word_count: 932
clean_char_count: 5829
---
# Site Audit Issues Update (September 2021)

Don’t be alarmed if you notice changes in your Health scores this week – we’ve added new issues related to page speed and updated some existing issues.

Now, many issues are more intelligent and help you prioritize better so you can focus on what really has an impact and ignore some of the noise.

Here’s a list of what’s new, what we fixed and why. Use the sidebar or the menu below to jump straight into a particular section.

Contents:

1. [Performance issues update](#performance-issues)
2. [Other important changes](#other-changes)
3. [Lowered importance level](#lowered-importance)
4. [Bug fixes](#bug-fixes)

## 1. Performance issues update

[Core Web Vitals (CWV)](https://ahrefs.com/blog/core-web-vitals/) are the speed metrics that are part of Google’s Page Experience signals used to measure user experience. They measure visual load with Largest Contentful Paint (LCP), visual stability with Cumulative Layout Shift (CLS), and interactivity with First Input Delay (FID).

Since these metrics have been officially used for ranking pages since June 2021, we’ve added **3 new warnings** based on CWV CrUX data:

- Pages with poor CLS
- Pages with poor FID
- Pages with poor LCP

If you have CWVs turned off or if no field data is available for your website, these issues will not be triggered. We also trigger the current “Slow page” warning if CWV is off.

## 2. Other important changes

#### Links / Page has links to broken page (indexable & non indexable)

We now only include **404 and 410 URLs** in this issue.

Previously, we considered links to any client (4xx) and server (5xx) error to be broken. But technically, only 404 and 410 links are truly broken as such URLs do not exist. All other status codes indicate that we’re unable to crawl them for some reason. So we removed them from the computation of this issue to get rid of false positives.

If you’re looking to filter by status code, you can still do this in Link Explorer or by customising the filters within an individual error/warning report.

#### **Localization / All hreflang related issues**

We now **ignore hreflangs on non-canonical pages**.

Since pages that aren’t canonical may not be eligible for ranking, it doesn’t matter whether they have hreflangs, which pages their hreflangs lead to or whether they receive reciprocal hreflangs. We’ve now updated the computation of these issues to get rid of false positives.

#### **Redirects / Redirect chain too long (new issue)**

Previously, we had a single “Redirect chain” issue. We’re now **splitting this into two issues** to distinguish between short and long redirects:

- “Redirect chain” (Importance: Notice) for redirect chains **URLs ≤ 5**
- “Redirect chain too long” (Importance: Error) for redirect chains **URLs > 5**

We lowered the importance level for “Redirect chain” because redirect chains aren’t an issue in general.

Only chains longer than 5 hops are a real problem because Google follows only 5 hops in a session – if there are more, their crawler will typically resume where they left off. But the longer the chain, the less likely they are to consolidate signals to the final destination.

## 3. Lowered importance level

#### **Links / Page has nofollow and dofollow incoming internal link (indexable)**

- Importance: Error → **Notice**

This is a fairly common situation if there are some “noindex, nofollow” pages on a website, so we’ve lowered the importance level of this issue to reflect this.

#### **Links / Page has nofollow incoming internal links only (indexable)**

- Importance: Error → **Warning**

It doesn’t matter if certain pages like privacy or terms of service rank or not, so people might nofollow internal links on these pages. We’ve lowered the importance level since it’s not a critical issue.

#### **Localization / Self-reference hreflang annotation missing**

- Importance: Error → **Warning**

Having a self-referencing hreflang isn’t a requirement, so it doesn’t warrant an “error” status. With that said, it’s still good practice to add self-referencing hreflangs in general.

#### **On page / Meta description tag missing or empty (indexable)**

- Importance: Error → **Warning**

There are many times when spending time on writing meta descriptions doesn’t make sense. Plus, according to [our data study](https://ahrefs.com/blog/meta-description-study/), Google only uses the page’s meta description in search results 37% of the time. We’ve lowered the importance level of this issue to reflect this.

#### **Performance / HTML file size too large**

- Importance: Error → **Warning**

We lowered the importance level of this issue since there’s no strong reason to claim that having a large HTML file size is a critical error. With that said, we kept it as a warning since a large html size of 250-300KB or more is usually accompanied by different performance issues. This warning could be a good prompt to investigate them.

#### **Links / Redirected page has no incoming internal links (indexable)**

- Importance: Error → **Warning**

We have no strong reasons to claim that it is critical to have a page linked via a redirect, even if it is the only link. While it may not be the best practice, it doesn’t warrant an “error” status.

## 4. Bug fixes

#### **Links / Canonical URL has no incoming internal links**

We removed the “Is self canonical = No” condition from this issue. This was a bug that excluded some problematic pages from the issue.

#### **Duplicate pages without canonical**

We added a “Is Noindex = false” condition to this issue. Previously, we were flagging  “noindex” pages for not having “a rel=canonical”.

–

That’s all we have for today.

Liked this update? Feel free to share our Twitter thread:

https://twitter.com/ahrefs/status/1446159185901723649?s=21
