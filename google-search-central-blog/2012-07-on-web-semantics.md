---
title: "On web semantics"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-07-on-web-semantics"
url: "https://developers.google.com/search/blog/2012/07/on-web-semantics"
canonical: "https://developers.google.com/search/blog/2012/07/on-web-semantics"
author: "Jens O. Meiert"
published: "2012-07-16T00:00:00+00:00"
updated: "2012-07-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:19:41+00:00"
status_code: 200
html_hash: "f7147b21f6b14f5408d03676973583026193e816b44c9b4c82a9c0ce2eb2f4de"
clean_word_count: 1100
clean_char_count: 7177
---
# On web semantics

In web development context, semantics refers to semantic markup, which means markup used according
to its meaning and purpose.

Markup used according to its purpose means using heading elements (for instance, `h1`
to `h6`) to mark up headings, paragraph elements (`p`) for paragraphs, lists
(`ul`, `ol`, `dl`, also `datalist` or
`menu`) for lists, tables for data tables, and so on.

Stating the obvious became necessary in the old days, when the Web consisted of only a few web
sites and authors used tables to code entire sites, table cells or paragraphs for headings, and
thought about other creative ways to achieve the layout they wanted. (Admittedly, these authors
had fewer instruments at their disposal than authors have today. There were times when coding a
three column layout was literally impossible without using tables or images.)

Up until today authors were not always certain about what HTML element to use for what functional
unit in their HTML page, though, and "living" specs like HTML 5 require authors to keep an eye on
what elements will be there going forward to mark up what otherwise calls for "meaningless"
fallback elements like `div` or `span`.

To know what elements HTML offers, and what meaning these elements have, it's necessary to consult
the HTML specs. There are indices—covering
[all HTML specs and elements](https://meiert.com/en/indices/html-elements/)—that make it
a bit simpler to look up and find out the meaning of an element. However, in many cases it may be
necessary to check what
[the HTML spec](https://www.whatwg.org/specs/web-apps/current-work/multipage/)
says.

For example, take
[the `code` element](https://www.whatwg.org/specs/web-apps/current-work/multipage/text-level-semantics.html#the-code-element):

> The `code` element represents a fragment of computer code. This could be an XML element
> name, a filename, a computer program, or any other string that a computer would recognize.

## Author-controlled semantics

HTML elements carry meaning as defined by the HTML specs, yet ID and class names can bear meaning
too. ID and class names, just like
[microdata](https://www.whatwg.org/specs/web-apps/current-work/multipage/microdata.html),
are typically under author control, the only exception being
[microformats](https://microformats.org/). (We will not cover
microdata or microformats in this article.)

ID and class names give authors a lot of freedom to work with HTML elements. There are a few basic
rules of thumb that, when followed, make sure this freedom doesn't turn into problems:

- Keep use of IDs and classes to a minimum.
- [Use functional ID and class names](https://google.github.io/styleguide/htmlcssguide#CSS);
  if that is not possible, use generic ID and class names.
- [Use names that are as short as possible but as long as necessary.](https://google.github.io/styleguide/htmlcssguide#CSS)

## Advantages of using semantic markup

Using markup according to how it's meant to be used, as well as modest use of functional ID and
class names, has several advantages:

- It's the *professional* thing to do.
- It's more accessible.
- It's more maintainable.

## Special cases

"Neutral" elements, elements with ambiguous meaning, and presentational elements constitute
special cases.

`div` and `span` offer a "generic mechanism for adding structure to
documents." They can be used whenever there is no other element available that matches what the
contents in question represent.

In the past a lot of confusion was caused by the `b`, `strong`,
`i`, and `em` elements. Authors cursed `b` and `i` for
being presentational, and typically suggested a 1:1 replacement with `strong` and
`em`. Not to stir up the past, here's what HTML 5 says, granting all four elements a
*raison d'être*:

|  |  |  |
| --- | --- | --- |
| [`b`](https://www.whatwg.org/specs/web-apps/current-work/multipage/text-level-semantics.html#the-b-element) | "a span of text to be stylistically offset from the normal prose without conveying any extra importance, such as key words in a document abstract, product names in a review, or other spans of text whose typical typographic presentation is boldened" | `<p>The <b>frobonitor</b> and <b>barbinator</b> components are fried.` |
| [`strong`](https://www.whatwg.org/specs/web-apps/current-work/multipage/text-level-semantics.html#the-strong-element) | "strong importance for its contents" | `<p><strong>Warning.</strong> This dungeon is dangerous.` |
| [`i`](https://www.whatwg.org/specs/web-apps/current-work/multipage/text-level-semantics.html#the-i-element) | "a span of text in an alternate voice or mood, or otherwise offset from the normal prose, such as a taxonomic designation, a technical term, an idiomatic phrase from another language, a thought, a ship name, or some other prose whose typical typographic presentation is italicized" | `<p>The term <i>prose content</i> is defined above.` |
| [`em`](https://www.whatwg.org/specs/web-apps/current-work/multipage/text-level-semantics.html#the-em-element) | "stress emphasis of its contents" | `<p><em>Cats</em> are cute animals.` |

Last but not least, there are truly presentational elements. These elements will be supported by
user agents (browsers) for forever but shouldn't be used anymore as
[presentational markup is not maintainable](https://meiert.com/en/blog/20090617/maintainability-guide/#toc-markup),
and should be handled by style sheets instead. Some popular ones are:

- `center`
- `font`
- `s`
- `u`

## How to tell whether you're on track

A quick and dirty way to check the semantics of your page and understand how it might be
interpreted by a screen reader is to disable CSS, for example using the Web Developer Toolbar
extension available
[for Chrome](https://chrome.google.com/webstore/detail/bfbameneiokkgbdmiekhjnmfkcnldhhm)
and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/web-developer/).
This only identifies issues around the use of CSS to convey meaning, but can still be helpful.

Other methods range from peer reviews (coding best practices) to user testing (accessibility).

## Do's and Don'ts

The following table gives a high level overview of some of the bad practices when it comes to
writing HTML, along with the correct alternatives and a short explanation.

| Don't | Do | Reason |
| --- | --- | --- |
| ``` <p class"heading">foo</p> ``` | ``` <h1>foo</h1> ``` | For headings there are heading elements. |
| ``` <p><font size="2">bar</font></p> ``` | ``` <p>bar</p> p { font-size: 1em; } ``` | Presentational markup is expensive to maintain. |
| ``` <table>   <tr>     <td class="heading">baz</td>   </tr>   <tr>     <td>scribble</td>   </tr> </table> ``` | ``` <h1>baz</h1> <p>scribble</p> ``` | Use table elements for tabular data. |
| ``` <div class="newrow">foo</div> <div>1</div> <div class="newrow">bar</div> <div>2</div> ``` | ``` <table>   <tr>     <th>foo</th>     <td>1</td>   </tr>   <tr>     <th>bar</th>     <td>2</td>   </tr> </table> ``` | Use table elements for tabular data. |
| ``` foo bar.<br><br>baz scribble. ``` | ``` <p>foo bar.</p> <p>baz scribble.</p> ``` | Denote paragraphs by paragraph elements, not line breaks. |
