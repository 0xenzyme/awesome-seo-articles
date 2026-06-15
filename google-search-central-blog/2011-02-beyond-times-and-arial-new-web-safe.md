---
title: "Beyond Times and Arial - The New Web Safe Fonts"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-02-beyond-times-and-arial-new-web-safe"
url: "https://developers.google.com/search/blog/2011/02/beyond-times-and-arial-new-web-safe"
canonical: "https://developers.google.com/search/blog/2011/02/beyond-times-and-arial-new-web-safe"
author: "Written by David Wurtz, Product Manager, Google Web Fonts"
published: "2011-02-18T00:00:00+00:00"
updated: "2011-02-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:11:00+00:00"
status_code: 200
html_hash: "32dc459b77ed727044a039acdbc05102d313b4d426ec0a08e94cd28048bfc243"
clean_word_count: 441
clean_char_count: 2533
---
# Beyond Times and Arial - The New Web Safe Fonts

In the past, when you created a website or web app, you were largely limited to a few select
"web safe" fonts such as Times and Arial. If you deviated from these fonts, you were required to
use Adobe Flash or to embed text in images, which introduced a whole new set of trade offs. For
example, images aren't semantic, cannot be translated into other languages automatically, and can
be much larger in file size than text. In addition, text in images cannot be copied to a user's
clipboard, read with screen-reading software, or easily indexed by search engines.

The good news is, with
[Google Web Fonts](https://www.google.com/webfonts)
it is now possible to use hundreds of web safe fonts on your web pages.
[Launched last May](https://googlecode.blogspot.com/2010/05/introducing-google-font-api-google-font.html),
Google Web Fonts allows you to simply choose the font(s) you'd like to use on your webpage, blog,
or web app, and embed the snippet of HTML and CSS. In about 30 seconds, you can have beautiful
fonts on your pages that will render correctly in the large majority of popular
[modern web browsers](https://code.google.com/apis/webfonts/faq.html#Browsers_Supported).
No longer will you need to use images or Flash to embed the font of your choice.

Unlike Times and Arial, which are references to fonts installed on a user's local machine, web
fonts are served via a browser request (much like an image would be served). That means you can
push any web font to a user's machine. Users will be delighted when they realize these fonts
behave just as any other text in Arial would behave.

![Some example web fonts, offered by the Google Web Fonts service](/static/search/blog/images/import/1deaf17c4cefe22ebad39edf1c576507.jpg)

The adoption of the web font technology has been rapid. Google Web Fonts now serves roughly 50
million daily requests[1], across roughly 800,000 unique websites[2], and is growing at about 30%
each month. Here at Google, we're excited about the potential for web fonts to change the very
fabric of the web. Beautiful typography makes the web more pleasant to browse, expressive, and
interesting.

Here's to a beautiful Web!

[1] A request is a single call to the Google Font API for one or more fonts.

[2] We count a unique website as unique domains, except that "www" subdomains are not counted. For
example, www.myblog.com and myblog.com would count as one domain. However, sam.myblog.com and
sally.myblog.com would count as two domains.
