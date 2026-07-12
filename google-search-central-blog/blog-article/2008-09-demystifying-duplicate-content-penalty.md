---
title: "Demystifying the \"duplicate content penalty\""
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-09-demystifying-duplicate-content-penalty"
url: "https://developers.google.com/search/blog/2008/09/demystifying-duplicate-content-penalty"
canonical: "https://developers.google.com/search/blog/2008/09/demystifying-duplicate-content-penalty"
author: "Susan Moskwa, Webmaster Trends Analyst"
published: "2008-09-12T00:00:00+00:00"
updated: "2008-09-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:54:04+00:00"
status_code: 200
html_hash: "0758fc99019ba3a6c0438389090c27a9e8bdd7a77c8d6e2cdd7a8bb5d4904069"
clean_word_count: 1156
clean_char_count: 7391
---
# Demystifying the "duplicate content penalty"

Duplicate content. There's just something about it. We
[keep](/search/blog/2006/12/deftly-dealing-with-duplicate-content)
[writing](/search/blog/2007/06/duplicate-content-summit-at-smx)
[about](/search/blog/2007/09/google-duplicate-content-caused-by-url)
[it](/search/blog/2008/06/duplicate-content-due-to-scrapers), and people keep asking
about it. In particular, I still hear a lot of webmasters worrying about whether they may have a
"duplicate content penalty."

Let's put this to bed once and for all, folks: There's no such thing as a "duplicate content
penalty." At least, not in the way most people mean when they say that.

There are some penalties that are related to the idea of having the same content as another
site—for example, if you're scraping content from other sites and republishing it, or if
you republish content without adding any additional value. These tactics are clearly outlined
(and discouraged) in our
[Webmaster Guidelines](/search/docs/essentials):

- Don't create multiple pages, subdomains, or domains with substantially
  [duplicate content](/search/docs/advanced/guidelines/duplicate-content).
- Avoid... "cookie cutter" approaches such as affiliate programs with
  [little or no original content](/search/docs/advanced/guidelines/thin-content).
- If your site participates in an
  [affiliate program](/search/docs/essentials/spam-policies#thin-affiliate-pages), make sure
  that your site adds value. Provide unique and relevant content that gives users a reason to
  visit your site first.

(Note that while scraping content from others is discouraged, having others scrape you is a
different story;
[check out this post](/search/blog/2008/06/duplicate-content-due-to-scrapers)
if you're worried about being scraped.)

But most site owners whom I hear worrying about duplicate content aren't talking about scraping or
domain farms; they're talking about things like having multiple URLs on the same domain that point
to the same content. Like
`www.example.com/skates.asp?color=black&brand=riedell`
and `www.example.com/skates.asp?brand=riedell&color=black`. Having this type of
duplicate content on your site can potentially affect your site's performance, but it doesn't
cause penalties. From our article on
[duplicate content](/search/docs/advanced/guidelines/duplicate-content):

Duplicate content on a site is not grounds for action on that site unless it appears that the
intent of the duplicate content is to be deceptive and manipulate search engine results. If your
site suffers from duplicate content issues, and you don't follow the advice listed above, we do
a good job of choosing a version of the content to show in our search results.

This type of non-malicious duplication is fairly common, especially since many CMSs don't handle
this well by default. So when people say that having this type of duplicate content can affect
your site, it's not because you're likely to be penalized; it's simply due to the way that web
sites and search engines work.

Most search engines strive for a certain level of variety; they want to show you ten different
results on a search results page, not ten different URLs that all have the same content. To this
end, Google tries to filter out duplicate documents so that users experience less redundancy. You
can find details in
[this blog post](/search/blog/2007/09/google-duplicate-content-caused-by-url), which
states:

1. When we detect duplicate content, such as through variations caused by URL parameters, we group
   the duplicate URLs into one cluster.
2. We select what we think is the "best" URL to represent the cluster in search results.
3. We then consolidate properties of the URLs in the cluster, such as link popularity, to the
   representative URL.

Here's how this could affect you as a webmaster:

- In step 2, Google's idea of what the "best" URL is might not be the same as your idea. If you
  want to have control over whether
  `www.example.com/skates.asp?color=black&brand=riedell` or
  `www.example.com/skates.asp?brand=riedell&color=black` gets shown in our search
  results, you may want to take action to mitigate your duplication.
  One way of letting us know which URL you prefer is by including the preferred URL in your
  [Sitemap](/search/docs/crawling-indexing/sitemaps/overview).
- In step 3, if we aren't able to detect all the duplicates of a particular page, we won't be
  able to consolidate all of their properties. This may dilute the strength of that content's
  ranking signals by splitting them across multiple URLs.

In most cases Google does a good job of handling this type of duplication. However, you may also
want to consider content that's being duplicated across domains. In particular, deciding to build
a site whose purpose inherently involves content duplication is something you should think twice
about if your business model is going to rely on search traffic, unless you can add a lot of
additional value for users. For example, we sometimes hear from Amazon.com affiliates who are
having a hard time ranking for content that originates solely from Amazon. Is this because Google
wants to stop them from trying to sell
[Everyone Poops](https://www.amazon.com/Everyone-Poops-My-Body-Science/dp/0916291456)?
No; it's because *how the heck are they going to outrank Amazon* if they're providing
the exact same listing? Amazon has a lot of online business authority (most likely more than
a typical Amazon affiliate site does), and the average Google search user probably wants the
original information on Amazon, unless the affiliate site has added a significant amount of
[additional value](/search/docs/essentials/spam-policies#thin-affiliate-pages).

Lastly, consider the effect that duplication can have on your site's bandwidth. Duplicated
content can lead to inefficient crawling: when Googlebot discovers ten URLs on your site, it has
to crawl each of those URLs before it knows whether they contain the same content (and thus before
we can group them as described above). The more time and resources that Googlebot spends crawling
duplicate content across multiple URLs, the less time it has to get to the rest of your content.

In summary: Having duplicate content can affect your site in a variety of ways; but unless you've
been duplicating deliberately, it's unlikely that one of those ways will be a penalty. This means
that:

- You typically don't need to submit a reconsideration request when you're cleaning up innocently
  duplicated content.
- If you're a webmaster of beginner-to-intermediate savviness, you probably don't need to put
  too much energy into worrying about duplicate content, since most search engines have ways of
  handling it.
- You can help your fellow webmasters by not perpetuating the myth of duplicate content penalties!
  The remedies for duplicate content are entirely within your control. Here are some good places
  to start:
  - [Avoid creating duplicate content](/search/docs/advanced/guidelines/duplicate-content)
  - [Deftly dealing with duplicate content](/search/blog/2006/12/deftly-dealing-with-duplicate-content)
  - [Duplicate content summit at SMX Advanced](/search/blog/2007/06/duplicate-content-summit-at-smx)
  - [Google, duplicate content caused by URL parameters, and you](/search/blog/2007/09/google-duplicate-content-caused-by-url)
