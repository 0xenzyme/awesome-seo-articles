---
title: "Working with multilingual websites"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-03-working-with-multilingual-websites"
url: "https://developers.google.com/search/blog/2010/03/working-with-multilingual-websites"
canonical: "https://developers.google.com/search/blog/2010/03/working-with-multilingual-websites"
author: "Written by Xavier deMorales, Google Search Quality"
published: "2010-03-19T00:00:00+00:00"
updated: "2010-03-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:05:35+00:00"
status_code: 200
html_hash: "8e019c8d098006c6630374431276333aba00c691722a0802e1ddbf0d86898d60"
clean_word_count: 887
clean_char_count: 5523
---
# Working with multilingual websites

A multilingual website is any website that offers content in more than one language. Examples of
multilingual websites might include a Canadian business with an English and a French version of
its site, or a blog on Latin American soccer available in both Spanish and Portuguese.

**Usually, it makes sense to have a multilingual website when your target audience consists of
speakers of different languages.** If your blog on Latin American soccer aims to reach the
Brazilian audience, you may choose to publish it only in Portuguese. But if you'd like to reach
soccer fans from Argentina also, then providing content in Spanish could help you with that.

## Google and language recognition

Google tries to determine the main languages of each one of your pages. **You can help to make
language recognition easier if you stick to only one language per page and avoid side-by-side
translations.** Although Google can recognize a page as being in more than one language, we
recommend using the same language for all elements of a page: headers, sidebars, menus, etc.

Keep in mind that Google ignores all code-level language information, from "lang" attributes to
Document Type Definitions (DTD). Some web editing programs create these attributes automatically,
and therefore they aren't very reliable when trying to determine the language of a webpage.

Someone who comes to Google and does a search in their language expects to find localized search
results, and this is where you, as a webmaster, come in: **if you're going to localize, make it
visible in the search results** with some of our tips below.

## The anatomy of a multilingual site: URL structure

There's no need to create special URLs when developing a multilingual website. Nonetheless, your
users might like to identify what section of your website they're on just by glancing at the URL.
For example, the following URLs let users know that they're on the English section of this site:
`https://example.ca/en/mountain-bikes.html` or
`https://en.example.ca/mountain-bikes.html`. While these other URLs let users
know that they're viewing the same page in French:
`https://example.ca/fr/mountain-bikes.html` or
`https://fr.example.ca/mountain-bikes.html`. Additionally, this URL structure
will make it easier for you to analyze the indexing of your multilingual content.

If you want to create URLs with non-English characters, make sure to use UTF-8 encoding. UTF-8
encoded URLs should be properly escaped when linked from within your content. Should you need to
escape your URLs manually, you can easily find an
[online URL encoder](https://www.google.com/search?q=url+encoder)
that will do this for you. For example, if I wanted to translate the following URL from English to
French, `https://example.ca/fr/mountain-bikes.html`, it might look something like
this: `https://example.ca/fr/vélo-de-montagne.html`. Since this URL contains one
non-English character (é), this is what it would look like properly escaped for use in a link on
your pages: `https://example.ca/fr/v%C3%A9lo-de-montagne.html`.

## Crawling and indexing your multilingual website

We recommend that you do not allow automated translations to get indexed. Automated translations
don't always make sense and they could potentially be viewed as spam. More importantly, the point
of making a multilingual website is to reach a larger audience by providing valuable content in
several languages. If your users can't understand an automated translation or if it feels
artificial to them, you should ask yourself whether you really want to present this kind of
content to them.

If you're going to localize, make it easy for Googlebot to crawl all language versions of your
site. Consider cross-linking page by page. In other words, you can provide links between pages
with the same content in different languages. This can also be very helpful to your users.
Following our previous example, let's suppose that a French speaker happens to land on
`https://example.ca/en/mountain-bikes.html`; now, with one click they can get to
`https://example.ca/fr/vélo-de-montagne.html` where they can view the same content in
French.

To make all of your site's content more crawlable, avoid automatic redirections based on the
user's perceived language. These redirections could prevent users (and search engines) from
viewing all the versions of your site.

And last but not least, keep the content for each language on separate URLs—don't use
cookies to show translated versions.

## Working with character encodings

Google directly extracts character encodings from HTTP headers, HTML page headers, and content.
There isn't much you need to do about character encoding, other than watching out for conflicting
information - for example, between content and headers. While Google can recognize different
character encodings, we recommend that you use UTF-8 on your website whenever possible.

## If your tongue gets twisted...

Now that you know all of this, your tongue may get twisted when you speak many languages, but your
website doesn't have to!

For more information, read our
[post on multi-regional sites](/search/blog/2010/03/working-with-multi-regional-websites)
and stay tuned for our next post, where we'll delve into special situations that may arise when
working with global websites. Until then, don't hesitate to drop by the Help Forum and
[join the discussion](https://support.google.com/webmasters/community/thread?tid=12a5507889c20461)!
