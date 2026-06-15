---
title: "Îñţérñåţîöñåļîžåţîöñ"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-09-internationalization"
url: "https://developers.google.com/search/blog/2011/09/internationalization"
canonical: "https://developers.google.com/search/blog/2011/09/internationalization"
author: "Kathryn Cullen"
published: "2011-09-11T00:00:00+00:00"
updated: "2011-09-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:14:58+00:00"
status_code: 200
html_hash: "c147b467a62edd52e88f130a96fa4f67fe79bcb6c9741874c56bdc80b5633bbb"
clean_word_count: 1383
clean_char_count: 8923
---
# Îñţérñåţîöñåļîžåţîöñ

So you're going global, and you need your website to follow. Should be a simple case of getting
the text translated and you're good to go, right? Probably not. The Google Webmaster Team
frequently builds sites that are localized into over 40 languages, so here are some things that we
take into account when launching our pages in both other languages and regions.

*(Even if you think you might be immune to these issues because you only offer content in
English, it could be that non-English language visitors are
[using tools like Google Translate to view your content in their language](https://translate.google.com/translate?sl=en&tl=ja&u=http%3A%2F%2Finvestor.google.com%2F).
This traffic should show up in your analytics dashboard, so you can get an idea of how many
visitors are not viewing your site in the way it's intended.)*

## More languages != more HTML templates

We can't recommend this enough: reuse the same template for all language versions, and always try
to keep the HTML of your template simple.

Keeping the HTML code the same for all languages has its advantages when it comes to maintenance.
Hacking around with the HTML code for each language to fix bugs doesn't scale–keep your page code
as clean as possible and deal with any styling issues in the CSS. To name just one benefit of
clean code: most translation tools will parse out the translatable content strings from the HTML
document and that job is made much easier when the HTML is well-structured and valid.

## How long is a piece of string?

If your design relies on text playing nicely with fixed-size elements, then translating your text
might wreak havoc. For example, your left-hand side navigation text is likely to translate into
much longer strings of text in several languages–check out the difference in string lengths
between some [English](https://www.google.com/intl/en/privacy/)
and
[Dutch](https://www.google.com/intl/nl/privacy/) language
navigation for the same content. Be prepared for navigation titles that might wrap onto more than
one line by figuring out your line height to accommodate this (also worth considering when you
create your navigation text in English in the first place).

Variable word lengths cause particular issues in form labels and controls. If your form layout
displays labels on the left and fields on the right, for example, longer text strings can flow
over into two lines, whereas shorter text strings do not seem associated with their form input
fields–both scenarios ruin the design and impede the readability of the form. Also consider the
extra styling you'll need for right-to-left (RTL) layouts (more on that later). For these reasons
we design forms with labels above fields, for easy readability and styling that will translate
well across languages.

![Screenshots of Chinese and German versions of web forms](/static/search/blog/images/archived_form-i18n.png)

Also avoid fixed-height columns–if you're attempting to neaten up your layout with box backgrounds
that match in height, chances are when your text is translated, the text will overrun areas that
were only tall enough to contain your English content. Think about whether the UI elements you're
planning to use in your design will work when there is more or less text–for instance,
[horizontal](https://www.google.co.il/about/corporate/company/) vs.
[vertical](https://www.google.com/ads/tv/getstarted) tabs.

## On the flip side

Source editing for bidirectional HTML can be problematic because many editors have not been built
to support the Unicode bidirectional algorithm
([more research on the problems and solutions](https://www.sw.it.aoyama.ac.jp/2008/pub/IUC32-bidi/)).
In short, the way your markup is displayed might get garbled:

```
     <p>
      ابةتث
      <img src="foo.jpg" alt=" جحخد" />
      < ذرزسش!
     </p>
```

Our own day-to-day usage has shown the following editors to currently provide decent solutions for
bidirectional editing: particularly Coda, and also Dreamweaver, IntelliJ IDEA and JEditX.

When designing for RTL languages you can build most of the support you need into the core CSS and
use the directional attribute of the `html` element (for backwards compatibility) in
combination with a class on the `body` element. As always, keeping all styles in one
core stylesheet makes for better maintainability.

Some key styling issues to watch out for: any elements floated right will need to be floated left
and vice versa; extra padding or margin widths applied to one side of an element will need to be
overridden and switched, and any text-align attributes should be reversed.

We generally use the following approach, including using a class on the body tag rather than a
`html[dir=rtl]` CSS selector because this is compatible with older browsers:

Elements:

```
    <body class="rtl">
      <h1>
        <a href="https://www.blogger.com/">
          <img alt="Google" src="https://www.google.com/images/logos/google_logo.png" />
        </a> Heading
      </h1>
```

Left-to-right (default) styling:

```
    h1 {
      height: 55px;
      line-height: 2.05;
      margin: 0 0 25px;
      overflow: hidden;
    }
    h1 img {
      float: left;
      margin: 0 43px 0 0;
      position: relative;
    }
```

Right-to-left styling:

```
    body.rtl {
      direction: rtl;
    }
    body.rtl h1 img {
      float: right;
      margin: 0 0 0 43px;
    }
```

(See this in action in
[English](https://www.google.com/intl/en/privacy/) and
[Arabic](https://www.google.com/intl/ar/privacy/).)

One final note on this subject: most of the time your content destined for right-to-left language
pages will be bidirectional rather than purely RTL, because some strings will probably need to
retain their LTR direction–for example, company names in Latin script or telephone numbers. The
way to make sure the browser handles this correctly in a primarily RTL document is to wrap the
embedded text strings with an inline element using an attribute to set direction, like this:

```
<h2>‫עוד ב- <span dir="ltr">Google</span>‬</h2>
```

In cases where you don't have an HTML container to hook the dir attribute into, such as title
elements or JavaScript-generated source code for message prompts, you can use this equivalent to
set direction where &#x202B; and &#x202C;‬ are Unicode control
characters for right-to-left embedding:

```
<title>&#x202B;‫הפוך את Google לדף הבית שלך‬&#x202C;</title>
```

Example usage in JavaScript code:

```
var ffError = '\u202B' +'כדי להגדיר את Google כדף הבית שלך ב\x2DFirefox, לחץ על הקישור \x22הפוך את Google לדף הבית שלי\x22, וגרור אותו אל סמל ה\x22בית\x22 בדפדפן שלך.'+ '\u202C';
```

(For more detail, see the W3C's articles on
[creating HTML for Arabic, Hebrew and other right-to-left scripts](https://www.w3.org/International/tutorials/bidi-xhtml/)
and
[authoring right-to-left scripts](https://www.w3.org/TR/i18n-html-tech-bidi/#ri20030218.135304584).)

## It's all Greek to me...

If you've never worked with non-Latin character sets before (Cyrillic, Greek, and a myriad of
Asian and Indic), you might find that both your editor and browser do not display content as
intended.

Check that your editor and browser encodings are set to UTF-8 (recommended) and consider adding a
`<span>` element and the `lang` attribute of the `html`
element to your HTML template so browsers know what to expect when rendering your page–this has
the added benefit of ensuring that all Unicode characters are displayed correctly, so using HTML
entities such as `&eacute;` (é) will not be necessary, saving valuable bytes! Check
[the W3C's tutorial on character encoding](https://www.w3.org/International/tutorials/tutorial-char-enc/en/all.html)
if you're having trouble–it contains in-depth explanations of the issues.

## A word on naming

Lastly, a practical tip on naming conventions when creating several language versions. Using a
standard such as the
[ISO 639-1 language codes](https://en.wikipedia.org/wiki/ISO_639-1)
for naming helps when you start to deal with several language versions of the same document.

Using a conventional standard will help users understand your site's structure as well as making
it more maintainable for all webmasters who might develop the site, and using the language codes
for other site assets (logo images, PDF documents) is handy to be able to quickly identify files.

See previous Webmaster Central posts for advice about URL structures and other issues surrounding
[working with multi-regional websites](/search/blog/2010/03/working-with-multi-regional-websites)
and
[working with multilingual websites](/search/blog/2010/03/working-with-multilingual-websites).

That's a summary of the main challenges we wrestle with on a daily basis; but we can vouch for the
fact that putting in the planning and work up front towards well-structured HTML and robust CSS
pays dividends during localization!
