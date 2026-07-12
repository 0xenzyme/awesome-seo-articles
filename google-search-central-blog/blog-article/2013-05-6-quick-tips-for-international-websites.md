---
title: "6 Quick Tips for International Websites"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2013-05-6-quick-tips-for-international-websites"
url: "https://developers.google.com/search/blog/2013/05/6-quick-tips-for-international-websites"
canonical: "https://developers.google.com/search/blog/2013/05/6-quick-tips-for-international-websites"
author: "Jens O. Meiert, Tony Ruscoe"
published: "2013-05-31T00:00:00+00:00"
updated: "2013-05-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2013_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:21:43+00:00"
status_code: 200
html_hash: "d189c0068a89b8a6a20867f0b66b126956cdd447a895ce20fe4892387eed6012"
clean_word_count: 700
clean_char_count: 4604
---
# 6 Quick Tips for International Websites

*Note from the editors: After previously looking into various ways to handle
[internationalization for Google's web-search](/search/docs/specialty/international/managing-multi-regional-sites),
here's a post from Google Web Studio team members with tips for web developers.*

Many websites exist in more than one language, and more and more websites are made available for
more than one language. Yet, building a website for more than one language doesn't simply mean
translation, or localization (L10N), and that's it. It requires a few more things, all of which
are related to internationalization (I18N). In this post we share a few tips for international
websites.

## Make pages I18N-ready in the markup, not the style sheets

Language and directionality are inherent to the contents of the document. If possible you should
hence always use markup, not style sheets, for internationalization purposes. Use
`@lang` and `@dir`, at least on the `html` element:

```
<html lang="ar" dir="rtl">
```

Avoid coming up with your own solutions like special classes or IDs.

As for I18N in style sheets, you can't always rely on CSS: The CSS spec defines that conforming
user agents
[may ignore properties like `direction` or `unicode-bidi`](https://www.w3.org/TR/CSS21/visuren.html#direction).
(For XML, the situation changes again. XML doesn't offer special internationalization markup, so
here it's advisable to use CSS.)

## Use one style sheet for all locales

Instead of creating separate style sheets for LTR and RTL directionality, or even each language,
bundle everything in one style sheet. That makes your internationalization rules much easier to
understand and maintain.

So instead of embedding an alternative style sheet like

```
<link href="default.rtl.css" rel="stylesheet">
```

just use your existing

```
<link href="default.css" rel="stylesheet">
```

When taking this approach you'll need to complement existing CSS rules by their international
counterparts:

## Use the `[dir='rtl']` attribute selector

Since we recommend to stick with the style sheet you have (tip #2), you need a different way of
selecting elements you need to style differently for the other directionality. As RTL contents
require specific markup (tip #1), this should be easy: For most modern browsers, we can simply use
`[dir='rtl']`.

Here's an example:

```
aside {
  float: right;
  margin: 0 0 1em 1em;
}

[dir='rtl'] aside {
  float: left;
  margin: 0 1em 1em 0;
}
```

## Use the `:lang()` pseudo class

To target documents of a particular language, use the `:lang()` pseudo class. (Note
that we're talking documents here, not text snippets, as targeting snippets of a particular
language makes things a little more complex.)

For example, if you discover that bold formatting doesn't work very well for Chinese documents
(which indeed it does not), use the following:

```
:lang(zh) strong,
:lang(zh) b {
  font-weight: normal;
  color: #900;
}
```

## Mirror left- and right-related values

When working with both LTR and RTL contents it's important to mirror all the values that change
directionality. Among the properties to watch out for is everything related to borders, margins,
and paddings, but also position-related properties, `float`, or
`text-align`.

For example, what's `text-align: left` in LTR needs to be
`text-align: right` in RTL.

There are tools to make it easy to "flip" directionality. One of them is
[CSSJanus](https://cssjanus.commoner.com/), though it has been written
for the "separate style sheet" realm, not the "same style sheet" one.

## Keep an eye on the details

Watch out for the following items:

- Images designed for left or right, like arrows or backgrounds, light sources in
  `box-shadow` and `text-shadow values`, and JavaScript positioning and
  animations: These may require being swapped and accommodated for in the opposite directionality.
- Font sizes and fonts, especially for non-Latin alphabets: Depending on the script and font, the
  default font size may be too small. Consider tweaking the size and, if necessary, the font.
- CSS
  [specificity](https://www.w3.org/TR/CSS21/cascade.html#specificity):
  When using the `[dir='rtl']` (or `[dir='ltr']`) hook (tip #2), you're
  using a selector of higher specificity. This can lead to issues. Just have an eye out, and
  adjust accordingly.

If you have any questions or feedback, check the
[Internationalization Webmaster Help Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:international_seo)),
or leave your comments here.
