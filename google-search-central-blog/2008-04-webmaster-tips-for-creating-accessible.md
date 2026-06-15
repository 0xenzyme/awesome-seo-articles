---
title: "Webmaster tips for creating accessible, crawlable sites"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-04-webmaster-tips-for-creating-accessible"
url: "https://developers.google.com/search/blog/2008/04/webmaster-tips-for-creating-accessible"
canonical: "https://developers.google.com/search/blog/2008/04/webmaster-tips-for-creating-accessible"
author: "T.V. Raman"
published: "2008-04-14T00:00:00+00:00"
updated: "2008-04-14T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:52:18+00:00"
status_code: 200
html_hash: "046df8706cd0cc4b0ee158d8338e6db376843bdf94904fd71d86f1a48cbf8316"
clean_word_count: 687
clean_char_count: 4311
---
# Webmaster tips for creating accessible, crawlable sites

![T.V. Raman and Hubbell at home](/static/search/blog/images/import/312e8b49ed09626139973a742369a3a6.jpg)

Hubbell and I enjoying the day at our home in California. You can view my earlier post about
[accessibility](/search/blog/2008/03/tips-for-making-information-universally)
for webmasters, as well as
[additional articles](https://googleblog.blogspot.com/search/label/accessibility)
I've written for the Official Google blog.

One of the most frequently asked questions about
[Accessible Search](https://labs.google.com/accessible/)
is: What can I do to make my site rank well on Accessible Search? At the same time, webmasters
often ask a similar but broader question: What can I do to rank high on Google Search?

Well I'm pleased to tell you that you can achieve two things with one move: critical site
features such as site navigation can be created to work for all users, including our own
Googlebot. Below are a few tips for you to consider.

## Ensure that all critical content is reachable

To *access* content, it needs to be *reachable*. Users and web crawlers reach content
by navigating through hyperlinks, so as a critical first step, ensure that all content on your
site is reachable via plain HTML hyperlinks, and avoid hiding critical portions of your site
behind technologies such as JavaScript or Flash.

Plain hyperlinks are hyperlinks created via an HTML anchor element. Next, ensure that the target
of all hyperlinks (that is, `<a>` elements) are real URLs, rather than using an
empty hyperlink while deferring hyperlink behavior to an `onclick` handler.

In short, avoid hyperlinks of the form:

```
<a href="#" onclick="javascript:void(...)">Product Catalog</a>
```

In preference of simpler links, such as:

```
<a href="https://www.example.com/product-catalog"> Product Catalog</a>
```

## Ensure that content is readable

To be useful, content needs to be *readable* by everyone. Ensure that all important content
on your site is present within the text of HTML documents. Content needs to be available without
needing to evaluate scripts on a page. Content hidden behind Flash animations or text generated
within the browser by executable JavaScript remains opaque to the Googlebot, as well as to most
blind users.

## Ensure that content is available in reading order

Having discovered and arrived at your readable content, a user needs to be able to follow the
content you've put together in its *logical* reading order. If you are using a complex,
multi-column layout for most of the content on your site, you might wish to step back and analyze
how you are achieving the desired effect. For example, using deeply-nested HTML tables makes it
difficult to link together related pieces of text in a logical manner.

The same effect can often be achieved using CSS and logically organized `<div>`
elements in HTML. As an added bonus, you will find that your site renders much faster as a result.

## Supplement all visual content—don't be afraid of redundancy!

Making information accessible to all does not mean that you need to 'dumb down' your site to
simple text. Making your content maximally redundant is critical in ensuring that your content is
maximally useful to everyone. Here are a few simple tips:

- Ensure that content communicated via images is available when those images are missing. This
  goes further than adding appropriate
  [alt attributes](/search/blog/2007/12/using-alt-attributes-smartly)
  to relevant images. Ensure that the text surrounding the image does an adequate job of setting
  the context for why the image is being used, as well as detailing the conclusions you expect a
  person seeing the image to draw. In short, if you want to make sure everyone knows it's a
  picture of a bridge, wrap that text around the image.
- Add relevant summaries and captions to tables so that the reader can gain a high-level
  appreciation for the information being conveyed before delving into the details contained
  within.
- Accompany visual animations such as data displays with a detailed textual summary.

Following these simple tips greatly increases the quality of your landing pages for everyone.
As a positive side-effect, you'll most likely discover that your site gets better indexed!
