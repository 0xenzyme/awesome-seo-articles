---
title: "Making form-filling faster, easier and smarter"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-01-making-form-filling-faster-easier-and"
url: "https://developers.google.com/search/blog/2012/01/making-form-filling-faster-easier-and"
canonical: "https://developers.google.com/search/blog/2012/01/making-form-filling-faster-easier-and"
author: "Ilya Sherman, Software Engineer"
published: "2012-01-25T00:00:00+00:00"
updated: "2012-01-25T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:17:22+00:00"
status_code: 200
html_hash: "e83c7ceaf48ec6055428ec71d62fd7e1d2230d23b237b0454dc47592b11fa29c"
clean_word_count: 408
clean_char_count: 2710
---
# Making form-filling faster, easier and smarter

One of the biggest bottlenecks on any conversion funnel is filling out an online form – shopping
and registration flows all rely on forms as a crucial and demanding step in accomplishing the
goals of your site. For many users, online forms mean repeatedly typing common information like
our names and addresses on different sites across the web – a tedious task that causes many to
give up and abandon the flow entirely.

Chrome's Autofill and other form-filling providers help to break down this barrier by remembering
common profile information and pre-populating the form with those values. Unfortunately, up to
now it has been difficult for webmasters to ensure that Chrome and other form-filling providers
can parse their form correctly. Some
[standards exist](https://www.rfc-editor.org/rfc/rfc4112.html);
but they put onerous burdens on the implementation of the website, so they're not used much in
practice.

Today we're pleased to announce support in Chrome for an experimental new "autocomplete type"
attribute for form fields that allows web developers to unambiguously label `text`
and `select` fields with common data types such as 'full-name' or 'street-address'.
With this attribute, web developers can drive conversions on their sites by marking their forms
for auto-completion without changing the user interface or the backend.

![How autocomplete might look like implemented on a web page](/static/search/blog/images/import/8d612515c15bef0d9dc9b9a1728c8198.png)

Just add an attribute to the input element, for example an email address field might look like:

```
<input type="text" name="field1" x-autocompletetype="email" />
```

We've been working on this design in collaboration with several other autofill vendors. Like any
early stage proposal we expect this will change and evolve as the web standards community provides
feedback, but we believe this will serve as a good starting point for the discussion on how to
best support autofillable forms in the HTML5 spec. For now, this new attribute is implemented in
Chrome as `x-autocompletetype` to indicate that this is still experimental and not yet
a standard, similar to the `webkitspeech` attribute we
[released](https://chrome.blogspot.com/2011/04/everybodys-talking-and-translating-with.html)
last summer.

For more information, you can read the
[full text of the proposed specification](https://wiki.whatwg.org/wiki/Autocompletetype),
ask questions on the
[Webmaster help forum](https://support.google.com/webmasters/community),
or you can share your feedback in the
[standardization discussion](https://lists.whatwg.org/htdig.cgi/whatwg-whatwg.org/2011-December/034198.html)!
