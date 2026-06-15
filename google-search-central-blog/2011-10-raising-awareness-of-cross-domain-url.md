---
title: "Raising awareness of cross-domain URL selections"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-10-raising-awareness-of-cross-domain-url"
url: "https://developers.google.com/search/blog/2011/10/raising-awareness-of-cross-domain-url"
canonical: "https://developers.google.com/search/blog/2011/10/raising-awareness-of-cross-domain-url"
author: "Pierre Far"
published: "2011-10-31T00:00:00+00:00"
updated: "2011-10-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:15:46+00:00"
status_code: 200
html_hash: "999cdf39e664a4436428da6072150c413cd4916c1c4733abcf07734d48b00947"
clean_word_count: 1208
clean_char_count: 8068
---
# Raising awareness of cross-domain URL selections

A piece of content can often be reached via several URLs, not all of which may be on the same
domain. A common example we've talked about over the years is having the same content available
on more than one URL, an issue known as
[duplicate content](/search/docs/advanced/guidelines/duplicate-content).
When we discover a group of pages with duplicate content, Google uses algorithms to select one
representative URL for that content. A group of pages may contain URLs from the same site or
from different sites. When the representative URL is selected from a group with different sites
the selection is called a cross-domain URL selection. To take a simple example, if the group of
URLs contains one URL from a.com and one URL from b.com and our algorithms select the URL from
b.com, the a.com URL may no longer be shown in our search results and may see a drop in
search-referred traffic.

Webmasters can greatly influence our algorithms' selections using one of the currently supported
mechanisms to indicate the preferred URL, for example using
[`rel="canonical"` elements](/search/docs/crawling-indexing/consolidate-duplicate-urls)
or
[`301` redirects](/search/docs/crawling-indexing/301-redirects).
In most cases, the decisions our algorithms make in this regard correctly reflect the webmaster's
intent. However, in some rare cases we've also found many webmasters are confused as to why it
has happened and what they can do if they believe the selection is incorrect.

To be transparent about cross-domain URL selection decisions, we're launching new Webmaster Tools
messages that will attempt to notify webmasters when our algorithms select an external URL instead
of one from their website. The details about how these messages work are in our
[Help Center article about the topic](https://www.google.com/support/webmasters/bin/answer.py?answer=1716747&topic=20985),
and in this blog post we'll discuss the different scenarios in which you may see a cross-domain
URL selection and what you can do to fix any selections you believe are incorrect.

## Common causes of cross-domain URL selection

There are many scenarios that can lead our algorithms to select URLs across domains.

In most cases, our algorithms select a URL based on signals that the webmaster implemented to
influence the decision. For example, a webmaster following
[our guidelines](/search/docs/crawling-indexing/site-move-no-url-changes)
and
[best practices](/search/blog/2008/04/best-practices-when-moving-your-site)
for moving websites is effectively signalling that the URLs on their new website are the ones
they prefer for Google to select. If you're moving your website and see these new messages in
Webmaster Tools, you can take that as confirmation that our algorithms have noticed.

However, we regularly see webmasters ask questions when our algorithms select a URL they did not
want selected. When your website is involved in a cross-domain selection, and you believe the
selection is incorrect (that is, not your intention), there are several strategies to improve the
situation. Here are some of the common causes of unexpected cross-domain URL selections that we've
seen, and how to fix them:

1. **Duplicate content, including multi-regional websites**: We regularly see
   webmasters use substantially the same content in the same language on multiple domains,
   sometimes inadvertently and sometimes to geotarget the content. For example, it's common to see
   a webmaster set up the same English language website on both example.com and example.net, or a
   German language website hosted on a.de, a.at, and a.ch.Depending on your website and your users,
   you can use one of the currently-supported canonicalization techniques to signal to our
   algorithms which URLs you wish selected. Please see the following articles about this topic:

- [Canonicalization](/search/docs/crawling-indexing/consolidate-duplicate-urls),
  specifically
  [`rel="canonical"` elements](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  and
  [`301` redirects](/search/docs/crawling-indexing/301-redirects)
- [Multi-regional and multilingual sites](/search/docs/specialty/international/managing-multi-regional-sites)
  and more about
  [working with multi-regional websites](/search/blog/2010/03/working-with-multi-regional-websites)
- [About `rel="alternate" hreflang="x"`](/search/docs/specialty/international/localized-versions)

2. **Configuration mistakes**: Certain types of misconfigurations can lead our
   algorithms to make an incorrect decision. Examples of misconfiguration scenarios include:

1. **Incorrect canonicalization**: Incorrect usage of
   [canonicalization techniques](/search/docs/crawling-indexing/consolidate-duplicate-urls)
   pointing to URLs on an external website can lead our algorithms to select the external URLs to
   show in our search results. We've seen this happen with misconfigured content management
   systems (CMS) or CMS plugins installed by the webmaster. To fix this kind of situation, find
   how your website is incorrectly indicating the canonical URL preference (for example, through
   incorrect usage of a `rel="canonical"` element or a `301` redirect) and
   fix that.
2. **Misconfigured servers**: Sometimes we see hosting misconfigurations where
   content from site a.com is returned for URLs on b.com. A similar case occurs when two
   unrelated web servers return identical
   [`soft 404` pages](/search/docs/crawling-indexing/troubleshoot-crawling-errors#soft-404-errors)
   that we may fail to detect as error pages. In both situations we may assume the same content
   is being returned from two different sites and our algorithms may incorrectly select the
   a.com URL as the canonical of the b.com URL.You will need to investigate which part of your
   website's serving infrastructure is misconfigured. For example, your server may be returning
   HTTP `200 (success)` status codes for error pages, or your server might be
   confusing requests across different domains hosted on it. Once you find the root cause of
   the issue, work with your server admins to correct the configuration.

3. **Malicious website attacks**: Some attacks on websites introduce code that can
   cause undesired canonicalization. For example, the malicious code might cause the website to
   return an
   [HTTP `301` redirect](/search/docs/crawling-indexing/301-redirects)
   or insert a cross-domain
   [`rel="canonical"` `link` element](/search/docs/crawling-indexing/consolidate-duplicate-urls)
   into the HTML `<head>` or HTTP header, usually pointing to an external URL
   hosting malicious content. In these cases our algorithms may select the malicious or spammy URL
   instead of the URL on the compromised website.In this situation, please follow our
   [guidance on cleaning your site](https://web.dev/articles/hacked)
   and submit a reconsideration request when done. To identify
   [cloaked](/search/docs/essentials/spam-policies#cloaking)
   attacks, you can use the
   [Fetch as Googlebot](https://www.google.com/support/webmasters/bin/answer.py?answer=158587)
   function in Webmaster Tools to see your page's content as Googlebot sees it.

In rare situations, our algorithms may select a URL from an external site that is hosting your
content without your permission. If you believe that another site is duplicating your content in
violation of copyright law, you may contact the site's host to request removal. In addition, you
can request that Google remove the infringing page from our search results by
[filing a request under the Digital Millennium Copyright Act](https://www.google.com/support/bin/answer.py?answer=1386831).

And as always, if you need help in identifying the cause of an incorrect decision or how to fix
it, you can see our
[Help Center article](https://www.google.com/support/webmasters/bin/answer.py?answer=1716747&topic=20985)
about this topic and ask in our
[Webmaster Help Forum](https://support.google.com/webmasters/community).
