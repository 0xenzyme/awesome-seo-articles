---
title: "Helping your site look great with Google Chrome"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-03-helping-your-site-look-great-with"
url: "https://developers.google.com/search/blog/2009/03/helping-your-site-look-great-with"
canonical: "https://developers.google.com/search/blog/2009/03/helping-your-site-look-great-with"
author: "Written by Glenn Wilson, Product Manager, Google Chrome"
published: "2009-03-27T00:00:00+00:00"
updated: "2009-03-27T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:57:21+00:00"
status_code: 200
html_hash: "8f26a77f0c235d1f6fdceb73fa4c447fb359ef6720b0e8e24741d37df646401c"
clean_word_count: 654
clean_char_count: 4211
---
# Helping your site look great with Google Chrome

Since launching
[Google Chrome](https://www.google.com/chrome)
last September, we received a number of questions from webmasters and web developers about how
to make their sites look great in Google Chrome. The questions were very insightful and
illuminating for the Chrome team, and I want to respond with a few helpful tips for making your
site look stellar in Google Chrome.

## Detecting Google Chrome

Most sites will render the same in both Safari and Google Chrome, because they're both
[WebKit](https://www.webkit.org/)-based browsers.
If your site looks right in Safari, then it should look right in Google Chrome, too.

Since Chrome is relatively new, many sites have confused Google Chrome with another browser. If
your site doesn't look quite right in Chrome but works fine in Safari, it's possible your site
may just not recognize Chrome's user-agent string.

As platforms and browsers adopt WebKit as their rendering engine, your site can detect and support
them automatically with the right JavaScript checks. Commonly, sites use JavaScript to 'sniff' the
navigator.userAgent property for "Chrome" or "Safari", but you should use
[proper object detection](https://www.quirksmode.org/js/support.html)
if possible. In fact, Gmail has been detecting WebKit properly in Chrome since day one!

If you must detect the user-agent type, you can use this simple JavaScript to detect WebKit:

```
var isWebkit =  navigator.userAgent.indexOf("AppleWebKit") > -1;
```

Or, if you want to check that the version of WebKit is at least a certain version—say, if you want
to use a spiffy new WebKit feature:

```
var webkitVersion = parseFloat(navigator.userAgent.split("AppleWebKit/")[1]) || undefined;
if (webkitVersion && webkitVersion > 500 ) {
  // use spiffy WebKit feature here
}
```

For reference, here are a few browser releases and the version of WebKit they shipped:

| Browser | Version of WebKit |
| --- | --- |
| Chrome 1.0 | 525.19 |
| Chrome 2.0 beta | 530.1 |
| Safari 3.1 | 525.19 |
| Safari 3.2 | 525.26.2 |
| Safari 4.0 beta | 528.16 |

We do not recommend adding "Google" or "Apple" to your `navigator.vendor` checks to
detect WebKit or Google Chrome, because this will not detect other WebKit or Chromium-based
browsers!

You can find more information about detecting WebKit at
[webkit.org](https://trac.webkit.org/wiki/DetectingWebKit).

## Other helpful tips

- Google Chrome doesn't support ActiveX plug-ins, but does support NPAPI plug-ins. This means you
  can show plug-in content like Flash and Java in Google Chrome the same way you do with Firefox
  and Safari.
- If text on your site looks a bit off, make sure you provide the proper content type and
  character encoding information in the HTTP response headers, or at the *beginning* of your
  pages, preferably near the top of the `<head>` section.
- Don't put block elements inside inline elements.

  ```
  <!--  Wrong: -->
  <a>
    <div>This will look wrong.</div>
  </a>

  <!--  Right: -->
  <div>
    <a>This will look right!</a>
  </div>
  ```
- If your JavaScript isn't working in Google Chrome, you can debug using Chrome's built-in
  JavaScript debugger, under the "page" menu
  > 'Developer'
  > 'Debug JavaScript' menu option.

To help webmasters and web developers find more answers, we created a
[support center](https://www.google.com/chrome/intl/en/webmasters.html)
and
[forum](https://www.google.com/support/forum/p/Chrome/label?lid=5e916dca4598a98a)
specifically to answer your questions. Of course, if you find something you think is really a bug
in Chrome, please
[report it to us](https://code.google.com/p/chromium/issues/entry)!

## Help us improve Google Chrome!

If you'd like to help even more, we're looking for sites that may be interested in allowing Google
to use their site as a benchmark for our internal compatibility and performance measurements. If
you're interested in having Google Chrome development optimized against a cached version of your
site, please contact us about details at
[chrome-webmasters@google.com](mailto:chrome-webmasters@google.com).

Please keep the feedback coming, and we'll keep working to improve Google Chrome!
