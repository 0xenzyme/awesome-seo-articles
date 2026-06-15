---
title: "How to best evaluate issues with your Accelerated Mobile Pages"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2016-09-how-to-best-evaluate-issues-with-your"
url: "https://developers.google.com/search/blog/2016/09/how-to-best-evaluate-issues-with-your"
canonical: "https://developers.google.com/search/blog/2016/09/how-to-best-evaluate-issues-with-your"
author: "Tomo Taylor, AMP Community Manager"
published: "2016-09-19T00:00:00+00:00"
updated: "2016-09-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2016_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:29:15+00:00"
status_code: 200
html_hash: "a476b23070aec55a1c028a72add466a252cf53abe6976f4428b08bb4c672763b"
clean_word_count: 637
clean_char_count: 4125
---
# How to best evaluate issues with your Accelerated Mobile Pages

![](/static/search/blog/images/import/4a5fbd415bbcb8b8d7db9c7463693cf9.png)

As you #AMPlify your site with
[Accelerated Mobile Pages](https://amp.dev/), it's important to
keep an eye periodically on the validation status of your pages, as only valid AMP pages are
eligible to show on Google Search.

When implementing AMP, sometimes pages will contain
[errors](https://amp.dev/documentation/guides-and-tutorials/learn/validation-workflow/validation_errors) causing them to not be indexed by
Google Search. Pages may also contain warnings that are elements that are not best practice or are
going to become errors in the future.

[Google Search Console](https://search.google.com/search-console) is a tool that lets you
check which of your AMP pages Google has
[identified as having errors](https://support.google.com/webmasters/answer/7450883). Once you know
which URLs are running into issues, there are a few handy tools that can make checking the
validation error details easier.

## Browser Developer Tools

To use Developer Tools for validation:

1. Open your AMP page in your browser
2. Append `#development=1` to the URL, for example,
   `https://localhost:8000/released.amp.html#development=1`.
3. Open the [Chrome DevTools console](https://developer.chrome.com/docs/devtools) and check
   for validation errors.

Developer Console errors will look similar to this:

![](/static/search/blog/images/import/57535a78da3f9120733393d677c357e4.png)

## AMP Browser Extensions

With the AMP Browser Extensions (available for
[Chrome](https://chromewebstore.google.com/detail/amp-validator/nmoffdblmcmgeicmolmhobpoocbbmknc?pli=1) and
[Opera](https://addons.opera.com/en/extensions/details/amp-validator/)), you can quickly identify and debug
invalid AMP pages. As you browse your site, the extension will evaluate each AMP page visited and
give an indication of the validity of the page. The following table shows the different icons that
the extensions may show based on the validity of the AMP markup.

|  |  |
| --- | --- |
| Red AMP icon indicating invalid AMP document. | When there are errors within an AMP page, the extension's icon shows in a red color and displays the number of errors encountered. |
| Green AMP icon indicating valid AMP document. | When there are no errors within an AMP page, the icon shows in a green color and displays the number of warnings, if any exist. |
| Blue AMP icon indicating AMP HTML variant if clicked. | When the page isn't AMP but the page indicates that an AMP version is available, the icon shows in a blue color with a link icon, and clicking on the extension will redirect the browser to the AMP version. |

Using the extensions means you can see what errors or warnings the page has by clicking on the
extension icon. Every issue will list the source line, source column, and a message indicating
what is wrong. When a more detailed description of the issue exists, a "Learn more" link will take
you to the relevant page on [ampproject.org](https://ampproject.org/).

![](/static/search/blog/images/import/98fb8c02f48684130b7633eb4c0b98c9.png)

## AMP Web Validator

The AMP Web Validator, available at
[validator.ampproject.org](https://validator.ampproject.org/), provides a simple
web UI to test the validity of your AMP pages.

![](/static/search/blog/images/import/a8274120fd1e934172e63057fd491df5.png)

To use the tool, you enter an AMP URL, or copy/paste your source code, and the web validator
displays error messages between the lines. You can make edits directly in the web validator which
will trigger revalidation, letting you know if your proposed tweaks will fix the problem.

What's your favourite way to check the status of your AMP Pages? Share your feedback in the
comments below or on our
[Google Webmasters Google+ page](https://workspaceupdates.googleblog.com/2023/04/new-community-features-for-google-chat-and-an-update-currents%20.html). Or as usual,
if you have any questions or need help, you can post in our
[Webmasters Help Forum](https://support.google.com/webmasters/community).
