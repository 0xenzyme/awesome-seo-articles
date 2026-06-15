---
title: "Handling legitimate cross-domain content duplication"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-12-handling-legitimate-cross-domain"
url: "https://developers.google.com/search/blog/2009/12/handling-legitimate-cross-domain"
canonical: "https://developers.google.com/search/blog/2009/12/handling-legitimate-cross-domain"
author: "John Mueller"
published: "2009-12-15T00:00:00+00:00"
updated: "2009-12-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:03:11+00:00"
status_code: 200
html_hash: "ac751bc93dc3b061a563873318b2a84b3fd80e875c3c47a7bc95bed63e0a165a"
clean_word_count: 748
clean_char_count: 4871
---
# Handling legitimate cross-domain content duplication

We've recently discussed several ways of
[handling duplicate content on a single website](/search/blog/2009/10/reunifying-duplicate-content-on-your);
today we'll look at ways of handling similar duplication across different websites, across
different domains. For some sites, there are legitimate reasons to duplicate content across
different websites—for instance, to migrate to a new domain name using a web server that
cannot create server-side redirects. To help with issues that arise on such sites, we're
announcing our support of the
**cross-domain `rel="canonical"` link element**.

![diagram showing rel-canonical in action by one page pointing to the other](/static/search/blog/images/archived_hot-shot-googlebot.png)

## Ways of handling cross-domain content duplication:

- **Choose your preferred domain**
  When confronted with duplicate content, search engines will generally take one version and
  filter the others out. This can also happen when multiple domain names are involved, so while
  search engines are generally pretty good at choosing something reasonable, many webmasters
  prefer to make that decision themselves.
- **Reduce in-site duplication**
  Before starting on cross-site duplicate content questions, make sure to
  [handle duplication within your site](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  first.
- **Enable crawling and use `301` (permanent) redirects where possible**
  Where possible, the most important step is often to use appropriate
  [`301` redirects](/search/docs/crawling-indexing/301-redirects).
  These redirects send visitors and search engine crawlers to your preferred domain and make it
  very clear which URL should be indexed. This is generally the preferred method as it gives clear
  guidance to everyone who accesses the content. Keep in mind that in order for search engine
  crawlers to discover these redirects, none of the URLs in the redirect chain can be disallowed
  via a
  [robots.txt file](/search/docs/crawling-indexing/robots/intro).
  Don't forget to handle your www / non-www preference with appropriate redirects and in
  [Webmaster Tools](https://www.google.com/support/webmasters/bin/answer.py?answer=44231).
- **Use the cross-domain `rel="canonical"` link element**
  There are situations where it's not easily possible to set up redirects. This could be the case
  when you need to move your website from a server that does not feature server-side redirects.
  In a situation like this, **you can use the
  [`rel="canonical"` link element](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  across domains** to specify the exact URL of whichever domain is preferred for indexing. While
  the `rel="canonical"` link element is seen as a hint and not an absolute command,
  we do try to follow it where possible.

## Still have questions?

**Do the pages have to be identical?**
No, but they should be similar. Slight differences are fine.

**For technical reasons I can't include a 1:1 mapping for the URLs on my sites. Can I just
point the `rel="canonical"` at the home page of my preferred site?**
No; this could result in problems. A mapping from old URL to new URL for each URL on the old site
is the best way to use `rel="canonical"`.

**I'm offering my content / product descriptions for syndication. Do my publishers need to use
`rel="canonical"`?**
We leave this up to you and your publishers. If the content is similar enough, it might make
sense to use `rel="canonical"`, if both parties agree.

**My server can't do a `301` (permanent) redirect. Can I use
`rel="canonical"` to move my site?**
If it's at all possible, you should work with your webhost or web server to do a
`301` redirect. Keep in mind that we treat `rel="canonical"` as a hint,
and other search engines may handle it differently. But if a `301` redirect is
impossible for some reason, then a `rel="canonical"` may work for you. For more
information, see our
[guidelines on moving your site](/search/docs/crawling-indexing/site-move-no-url-changes).

**Should I use a `noindex` robots
[`meta` tag](/search/docs/advanced/crawling/special-tags)
on pages with a `rel="canonical"` link element?**
No, since those pages would not be equivalent with regards to indexing—one would be allowed
while the other would be blocked. Additionally, it's important that these pages are not
disallowed from crawling through a robots.txt file, otherwise search engine crawlers will not
be able to discover the `rel="canonical"` link element.

We hope this makes it easier for you to handle duplicate content in a user-friendly way. Are
there still places where you feel that duplicate content is causing your sites problems? Let us
know in the
[Webmaster Help Forum](https://support.google.com/webmasters/community/thread?tid=07603d23e8071644)!
