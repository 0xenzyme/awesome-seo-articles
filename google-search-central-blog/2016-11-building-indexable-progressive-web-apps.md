---
title: "Building Indexable Progressive Web Apps"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2016-11-building-indexable-progressive-web-apps"
url: "https://developers.google.com/search/blog/2016/11/building-indexable-progressive-web-apps"
canonical: "https://developers.google.com/search/blog/2016/11/building-indexable-progressive-web-apps"
author: "Tom Greenaway, Developer Advocate"
published: "2016-11-09T00:00:00+00:00"
updated: "2016-11-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2016_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:29:39+00:00"
status_code: 200
html_hash: "dc300ee3d1dcce5459c499f60cc5ffb318b34755ae550ba683d4ba6ef36d5015"
clean_word_count: 2388
clean_char_count: 15917
---
# Building Indexable Progressive Web Apps

[Progressive Web Apps](/web/progressive-web-apps)
(PWAs) are taking advantage of new technologies to bring the best of mobile sites and native
applications to users—and they're one of the most exciting new ideas on the web. But to truly
have an impact, it's important that they're indexable and linkable. Every recommendation presented
in this article is an existing best practice for indexability—regardless of whether you're
building a Progressive Web App or a simple static website. Nonetheless, we have collated these
best practices to provide a checklist to guide you:

![](/static/search/blog/images/import/3d5869cbe082155ba5f53fd3fd5faedb.jpg)

## Make Your Content Crawlable

**Why?** Historically, websites would always generate or render their HTML on the server which
is the simplest way to ensure your content is directly linkable. Web applications popularised the
concept of client-side rendering in which content is updated dynamically on the page as the users
navigates without requiring the page to be reloaded.

The modern approach is hybrid rendering, in which server-side rendering is used when a user
navigates directly to a URL and client-side rendering is used after the initial page load for
subsequent navigation and asynchronous requests.

Our
[server-side PWA sample](https://github.com/google/indexable-pwa-samples#server-sample)
demonstrates pure server-side rendering, while our
[hybrid PWA sample](https://github.com/google/indexable-pwa-samples#hybrid-sample)
demonstrates the combined approach.

If you are unfamiliar with the **server-side** and **client-side** rendering terminology,
check out these articles about
[client and server side rendering](https://openmymind.net/2012/5/30/Client-Side-vs-Server-Side-Rendering/), and
[server side rendering in react and node.js.](https://www.smashingmagazine.com/2016/03/server-side-rendering-react-node-express/)

**Best practices:**

Use server-side or hybrid rendering so users receive the content in the initial payload of their
web request.

Always ensure your URLs are independently accessible:

```
https://www.example.com/product/25/
```

The above should deep link to that particular resource.

If you can't support server-side or hybrid rendering for your Progressive Web App and you decide
to use client-side rendering, we recommend using the Google Search Console "Fetch as Google
tool" to verify your content successfully renders for our Search crawler.

Don't redirect users accessing deep links back to your web app's home page.

Additionally, serving an error page to users instead of deep linking should also be avoided.

## Provide Clean URLs

**Why?** Fragment identifiers (`#user/24601/` or `#!user/24601/`) were an
effective workaround for browsers to AJAX new content from a server without reloading the page.
This design is known as client-side rendering.

However, the fragment identifier syntax isn't compatible with some web tools, frameworks and
protocols such as [Facebook's Open Graph protocol](https://ogp.me/).

The [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) enables
us to update the URL without fragment identifiers while still fetching resources asynchronously
and therefore avoiding page reloads—it's the best of both worlds. The AJAX crawling scheme
(with its `#!` / escaped-fragment URLs) made sense at its time, but is now no longer
recommended.

Our [hybrid PWA and client-side PWA samples](https://github.com/google/indexable-pwa-samples)
demonstrate the History API.

**Best practices:**

Provide clean URLs without fragment identifiers (`#` or `#!`) such as:

```
    https://www.example.com/product/25/
```

If using client-side or hybrid rendering be sure to support browser navigation with the History
API.

### Avoid:

Using the `#!` URL structure to drive unique URLs is discouraged:

```
    https://www.example.com/#!product/25/
```

It was introduced as a workaround before the advent of the History API. It is considered a
separate pattern to the purely `#` URL structure.

Using the `#` URL structure without the accompanying `!` symbol is
unsupported:

https://www.example.com/#product/25/

This URL structure is already a concept in the web and relates to deep linking into content on a
particular page.

## Specify Canonical URLs

**Why?** The best way to eliminate confusion for indexing when the same content is available
under multiple URLs (be it the same or different domains) is to mark one page as the canonical,
and all other pages that duplicate that content to refer to it.

**Best practices:**

Include the following tag across all pages mirroring a particular piece of content:

```
<link rel="canonical"  href="https://www.example.com/your-url/" />
```

If you are supporting Accelerated Mobile Pages be sure to correctly use its counterpart
`rel="amphtml"` instruction as well.

### Avoid:

Avoid purposely duplicating content across multiple URLs and not using the
`rel="canonical"` link element.

For example, the `rel="canonical"` link element can reduce ambiguity for URLs with
tracking parameters.

Avoid creating conflicting canonical references between your pages.

## Design for Multiple Devices

**Why?** It's important that all your users get the best experience possible when viewing your
website, regardless of their device.

Make your site
[responsive in its design](/web/fundamentals/design-and-ui/responsive/fundamentals)
—fonts, margins, paddings, buttons and general design of your site should scale dynamically
based on screen resolutions and device viewports.

Small images scaled up for desktop or tablet devices give a poor experience. Conversely, super
high resolution images take a long time to download on mobile phones and may impact mobile scroll
performance.

Read more about
[UX for PWAs](https://medium.com/@owencm/designing-great-uis-for-progressive-web-apps-dd38c1d20f7#.c0avg96qb).

**Best practices:**

Use
[`srcset` attribute](/web/fundamentals/design-and-ui/media/images/images-in-markup)
to fetch different resolution images for different density screens to avoid downloading images
larger than the device's screen is capable of displaying.

Scale your font size and line height to ensure your text is legible no matter the size of the
device. Similarly ensure the padding and margins of elements also scale sensibly.

Test
[various screen resolutions](/web/tools/chrome-devtools/iterate/device-mode/emulate-mobile-viewports)
using the
[Chrome Developer Tool's Device Mode](/web/tools/chrome-devtools/iterate/device-mode)
feature and
[Mobile Friendly Test tool](https://search.google.com/test/mobile-friendly).

Don't show different content to users than you show to Google. If you use
[redirects or user agent detection](https://support.google.com/webmasters/answer/2604723)
(a.k.a. browser sniffing or
[dynamic serving](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)) to alter the
design of your site for different devices it's important that the content itself remains the
same.

Use the Search Console "Fetch as Google" tool to verify the content fetched by Google matches
the content a user sees.

For usability reasons, avoid using fixed-size fonts.

## Develop Iteratively

**Why?** One of the safest paths to take when adding features to a web application is to make
changes iteratively. If you add features one at a time you can observe the impact of each
individual change.

Alternatively many developers prefer to view their progressive web application as an opportunity
to overhaul their mobile site in one fell swoop—developing the new web app in an isolated
environment and swapping it with their existing mobile site once ready.

When developing features iteratively try to break the changes into separate pieces. For example,
if you intend to move from server-side rendering to hybrid rendering then tackle that as a single
iteration—rather than in combination with other features.

Both approaches have their own pros and cons. Iterating reduces the complexity of dealing with
search indexability as the transition is continuous. However, iterating might result in a slower
development process and potentially a less innovative overhaul if development is not starting from
scratch.

In either case, the most sensitive areas to keep an eye on are your canonical URLs and your site's
robots.txt configuration.

**Best practices:**

Iterate on your website incrementally by adding new features piece by piece.

For example, if don't support HTTPS yet then start by migrating to a secure site.

**Avoid:**

If you've developed your progressive web app in an isolated environment, then avoid launching it
without checking the rel-canonical links and robots.txt are setup appropriately.

Ensure your rel-canonical links point to the real site and that your robots.txt configuration
allows crawlers to crawl your new site.

It's logical to prevent crawlers from indexing your in-development site before launch but don't
forget to unblock crawlers from accessing your new site when you launch.

## Use Progressive Enhancement

**Why?** Wherever possible it's important to detect browser features before using them. Feature
detection is also better than testing for browsers that you believe support a given feature.

A common bad practice in the past was to enable or disable features by testing which browser the
user had. However, as browsers are constantly evolving with features this technique is strongly
discouraged.

Service Worker is a relatively new technology and it's important to not break compatibility in the
pursuit of progress—it's a perfect example of when to use progressive enhancement.

**Best practices:**

Before registering a Service Worker check for the availability of its API:

```
if ('serviceWorker' in navigator) {
...
```

Use per API detection method for all your website's features.

Never use the browser's user agent to enable or disable features in your web app. Always check
whether the feature's API is available and gracefully degrade if unavailable.

Avoid updating or launching your site without testing across multiple browsers! Check your site
analytics to learn which browsers are most popular among your user base.

## Test with Search Console

**Why?** It's important to understand how Google Search views your site's content. You can use
[Search Console](https://search.google.com/search-console) to
[fetch individual URLs from your site](https://support.google.com/webmasters/answer/6066468)
and see how Google Search views them using the "Crawl > Fetch as Google" feature. Search
Console will process your JavaScript and render the page when that option is selected; otherwise
only the raw HTML response is shown.

Google Search Console also analyses the content on your page in a variety of ways including
detecting the presence of Structured Data, Rich Cards, Sitelinks and Accelerated Mobile Pages.

**Best practices:**

Monitor your site using Search Console and explore its features including Fetch as Google.

Provide a sitemap via Search Console **Crawl > Sitemaps**.
It can be an effective way to ensure Google Search is aware of all your site's pages.

## Annotate with Schema.org structured data

**Why?** [Schema.org](https://schema.org/) structured data is a
flexible vocabulary for summarizing the most important parts of your page as machine-processable
data. This can be as general as simply saying that a page is a `NewsArticle`, or as
specific as detailing the location, band name, venue and ticket vendor for a touring band, or
summarizing the ingredients and steps for a recipe.

The use of this metadata may not make sense for every page on your web application but it's
recommended where it's sensible. Google extracts it after the page is rendered.

There are a variety of data types including `NewsArticle`, `Recipe`, and
`Product` to name a few. You can also explore all the
[supported data types here](/search/docs/appearance/structured-data/search-gallery).

**Best practices:**

Verify that your Schema.org meta data is correct using Google's
[Structured Data Testing Tool](/search/docs/advanced/structured-data).

Check that the data you provided is appearing and there are no errors present.

Avoid using a data type that doesn't match your page's actual content. For example don't use
`Recipe` for a T-Shirt you're selling—use `Product` instead.

## Annotate with Open Graph and Twitter Cards

**Why?** In addition to the Schema.org metadata it can be helpful to add support for Facebook's
Open Graph protocol and Twitter rich cards as well.

These metadata formats improve the user experience when your content is shared on their
corresponding social networks.

If your existing site or web application utilises these formats it's important to ensure they are
included in your progressive web application as well for optimal virality.

**Best practices:**

Test your Open Graph markup with the
[Facebook Object Debugger Tool](https://developers.facebook.com/tools/debug/).

Familiarise yourself with
[Twitter's metadata format](https://dev.twitter.com/cards/overview).

Don't forget to include these formats if your existing site supports them.

## Test with Multiple Browsers

**Why?** Clearly from a user perspective it's important that a website behaviors the same
across all browsers. While the experience might adapt for different screen sizes we all expect a
mobile site to work the same on similarly sized devices whether it's an iPhone or an Android
mobile phone.

While the web can be perceived as fragmented due to number of browsers in use around the world,
this variety and competition is part of what makes the web such an innovative platform.
Thankfully, web standards have never been more mature than they are now and modern tools enable
developers to build rich, cross browser compatible websites with confidence.

**Best practices:**

Use cross browser testing tools such as
[BrowserStack.com](https://www.browserstack.com/),
[Browserling.com](https://www.browserling.com/) or
[BrowserShots.org](https://browsershots.org/) to ensure your PWA is
cross browser
compatible.

## Measure Page Load Performance

**Why?** The faster a website loads for a user the better their user experience will be.
Optimizing for page speed is already a well known focus in web development but sometimes when
developing a new version of a site the necessary optimizations are not considered a high priority.

When developing a progressive web application we recommend measuring the performance of your page
load speed and optimizing before launching the site for the best results.

**Best practices:**

Use tools such as
[Page Speed Insights](https://pagespeed.web.dev/) and
[Web Page Test](https://webpagetest.org)
to measure the page load performance of your site. While Googlebot has a bit more patience in
rendering,
[research has shown](https://www.thinkwithgoogle.com/articles/mobile-page-speed-load-time)
that 40% of consumers will leave a page that takes longer than three seconds to load.

Read more about our web page performance recommendations and the
[critical rendering path here](/web/fundamentals/performance/critical-rendering-path).

Avoid leaving optimization as a post-launch step. If your website's content loads quickly before
migrating to a new progressive web application then it's important to not regress in your
optimizations.

We hope that the above checklist is useful and provides the right guidance to help you develop
your Progressive Web Applications with indexability in mind.

As you get started, be sure to check out our
[Progressive Web App indexability samples](https://github.com/google/indexable-pwa-samples)
that demonstrate server-side, client-side, and hybrid rendering. As always, if you have any
questions, please reach out on our
[Webmaster Forums](https://support.google.com/webmasters/go/community).
