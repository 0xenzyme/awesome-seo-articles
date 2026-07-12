---
title: "Setting the preferred domain"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-09-setting-preferred-domain"
url: "https://developers.google.com/search/blog/2006/09/setting-preferred-domain"
canonical: "https://developers.google.com/search/blog/2006/09/setting-preferred-domain"
author: null
published: "2006-09-12T00:00:00+00:00"
updated: "2006-09-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:46:37+00:00"
status_code: 200
html_hash: "f0c628f7c8293a021208c0df49b1ab35677100eceec03bd0691ee80a85784a16"
clean_word_count: 606
clean_char_count: 3486
---
# Setting the preferred domain

Based on your input, we've recently made a few changes to the preferred domain feature of
Webmaster Tools. And since you've had some questions about this feature, we'd like to answer
them.

The
[preferred domain feature](https://www.google.com/support/webmasters/bin/answer.py?answer=44231&topic=9025)
enables you to tell us if you'd like URLs from your site crawled and indexed using the www
version of the domain (`https://www.example.com`) or the non-www version of the domain
(`https://example.com`). When we initially launched this, we added the non-preferred
version to your account when you specified a preference so that you could see any information
associated with the non-preferred version. But many of you found that confusing, so we've made the
following changes:

- When you set the preferred domain, we no longer will add the non-preferred version to your
  account.
- If you had previously added the non-preferred version to your account, you'll still see it
  listed there, but you won't be able to add a Sitemap for the non-preferred version.
- If you have already set the preferred domain and we had added the non-preferred version to your
  account, we'll be removing that non-preferred version from your account over the next few days.

Note that if you would like to see any information we have about the non-preferred version, you
can always add it to your account.

Here are some questions we've had about this preferred domain feature, and our replies.

**Once I've set my preferred domain, how long will it take before I see changes?** The time
frame depends on many factors (such as how often your site is crawled and how many pages are
indexed with the non-preferred version). You should start to see changes in the few weeks after
you set your preferred domain.

**Is the preferred domain feature a filter or a redirect? Does it simply cause the search results
to display on the URLs that are in the version I prefer?** The preferred domain feature is not
a filter. When you set a preference, we:

- Consider all links that point to the site (whether those links use the www version or the
  non-www version) to be pointing at the version you prefer. This helps us more accurately
  determine PageRank for your pages.
- Once we know that both versions of a URL point to the same page, we try to select the preferred
  version for future crawls.
- Index pages of your site using the version you prefer. If some pages of your site are indexed
  using the www version and other pages are indexed using the non-www version, then over time,
  you should see a shift to the preference you've set.

**If I use a `301` redirect on my site to point the www and non-www versions to the
same version, do I still need to use this feature?** You don't have to use it, as we can
follow the redirects. However, you still can benefit from using this feature in two ways: we can
more easily consolidate links to your site and over time, we'll direct our crawl to the preferred
version of your pages.

**If I use this feature, should I still use a `301` redirect on my site?** You don't
need to use it for Googlebot, but you should still use the `301` redirect, if it's
available. This will help visitors and other search engines. Of course, make sure that you point
to the same URL with the preferred domain feature and the `301` redirect.

You can find more about this in our
[webmaster help center.](https://support.google.com/webmasters/)
