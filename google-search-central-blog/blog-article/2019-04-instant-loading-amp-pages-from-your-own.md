---
title: "Instant-loading AMP pages from your own domain"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2019-04-instant-loading-amp-pages-from-your-own"
url: "https://developers.google.com/search/blog/2019/04/instant-loading-amp-pages-from-your-own"
canonical: "https://developers.google.com/search/blog/2019/04/instant-loading-amp-pages-from-your-own"
author: "Devin Mullins and Greg Rogers"
published: "2019-04-17T00:00:00+00:00"
updated: "2019-04-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:33:58+00:00"
status_code: 200
html_hash: "26f90d1e264a465046e1140ea3db9810e735cd1a3d8259baaa5b2013aa85f025"
clean_word_count: 622
clean_char_count: 4183
---
# Instant-loading AMP pages from your own domain

Today we are rolling out support in Google Search's
[AMP web results](https://blog.google/products/search/search-results-are-officially-ampd/)
(also known as "blue links") to link to
[signed exchanges](/web/updates/2018/11/signed-exchanges),
an emerging new feature of the web enabled by the
[IETF web packaging specification](https://tools.ietf.org/id/draft-yasskin-dispatch-web-packaging-00).
Signed exchanges enable displaying the publisher's domain when content is instantly loaded via
Google Search. This is available in browsers that support the necessary web platform feature—as of
the time of writing, Google Chrome—and availability will expand to include other browsers as they
gain support (for example, the upcoming version of Microsoft Edge).

![An animation showing how signed exchange works from a user's perspective](/static/search/blog/images/import/988812308ab90032ad3884c70f0a0e57.gif)

## Background on AMP's instant loading

One of AMP's biggest user benefits has been the unique ability to instantly load AMP web pages
that users click on in Google Search. Near-instant loading works by requesting content ahead of
time, balancing the likelihood of a user clicking on a result with device and network
constraints—and
[doing it in a privacy-sensitive way](https://blog.amp.dev/2018/07/23/privacy-and-user-choice-in-amps-software-architecture/).

We believe that privacy-preserving instant loading web content is a transformative user
experience, but in order to accomplish this, we had to make trade-offs; namely, the
[URLs](https://developers.googleblog.com/2017/02/whats-in-amp-url)
displayed in browser address bars begin with google.com/amp, as a consequence of being shown in
the Google AMP Viewer, rather than display the domain of the publisher. We heard both user and
publisher feedback over this, and last year we
[identified](https://blog.amp.dev/2018/01/09/improving-urls-for-amp-pages/)
a web platform innovation that provides a solution that shows the content's original URL while
still retaining AMP's instant loading.

## Introducing signed exchanges

A signed exchange is a file format, defined in the
[web packaging specification](https://github.com/WICG/webpackage),
that allows the browser to trust a document as if it belongs to your
[origin](https://en.wikipedia.org/wiki/Same-origin_policy). This allows you to use
first-party cookies and storage to customize content and simplify analytics integration. Your page
appears under your URL instead of the google.com/amp URL.

![an animation showing how the URL stays consistent with the publisher's URL instead of showing an AMP cache URL](/static/search/blog/images/import/5ed16cb94aafd5cfaa0309e6f1a5ae4c.gif)

Google Search links to signed exchanges when the publisher, browser, and the Search experience
context all support it. As a publisher, you will need to publish both the signed exchange version
of the content in addition to the non-signed exchange version. Learn more about how
[Google Search supports signed exchange](/search/docs/crawling-indexing/amp/about-amp).

## Getting started with signed exchanges

Many publishers have already begun to publish signed exchanges since the
[developer preview](https://blog.amp.dev/2018/11/13/developer-preview-of-better-amp-urls-in-google-search/)
opened up last fall. To implement signed exchanges in your own serving infrastructure, follow the
guide
[Serve AMP using Signed Exchanges](https://amp.dev/documentation/guides-and-tutorials/optimize-and-measure/signed-exchange)
available at amp.dev.

If you use a CDN provider, ask them if they can provide AMP signed exchanges.
[Cloudflare](https://www.cloudflare.com/)
has recently
[announced](https://blog.cloudflare.com/announcing-amp-real-url/)
that it is offering signed exchanges to all of its customers without payment.

Check out our resources like the
[webmaster community](https://support.google.com/webmasters/community)
or
[get in touch with members of the AMP Project](https://amp.dev/support/)
with any questions. You can also
[provide feedback on the signed exchange specification](https://github.com/WICG/webpackage/issues).
