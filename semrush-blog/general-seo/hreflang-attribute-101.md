---
title: "Hreflang Attributes & Tags Explained for Beginners"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "hreflang-attribute-101"
url: "https://www.semrush.com/blog/hreflang-attribute-101/"
canonical: "https://www.semrush.com/blog/hreflang-attribute-101/"
author: "Rachel Handley, Simon Fogg, Christine Skopec"
published: "2019-06-21T14:30:00+00:00"
updated: "2025-01-22T10:07:00+00:00"
categories:
  - "General SEO"
freshness_reasons: []
schema_genre: "General SEO"
fetched_at: "2026-06-12T16:54:01+00:00"
status_code: 200
html_hash: "2b882a5e825e1953a188001fc5acc5f650b33cc49003303873b24eef84df601a"
clean_word_count: 1388
clean_char_count: 9451
---
# Hreflang Attributes & Tags Explained for Beginners

Learn about the role hreflang attributes play in helping multilingual and multiregional websites show the correct language versions to users.

## What Is Hreflang?

Hreflang is an HTML attribute that communicates a webpage’s language—and possibly its target country—to search engines when the page has language or country variants.

For example, the hreflang attribute **hreflang="en-us"** signals that the specified page is written in English and targeted to U.S. audiences.

If you have multiple versions of your pages to serve different languages or countries, you should use hreflang in your [search engine optimization (SEO)](https://www.semrush.com/blog/what-is-seo/) strategy.

## Why Are Hreflang Attributes Important for SEO?

Hreflang attributes are important for SEO because they help ensure search engines display the correct versions of your pages based on users’ languages and locations.

Like this:

![German version of Google shows German results in SERP for "iphone."](https://static.semrush.com/blog/uploads/media/f1/5e/f15e04e14b503c661f833af38a7d4f56/35505a35dc8af3de76bf6128ccd0c1c9/AD_4nXfjxFGCXJK2yc4RT8P638MiwQ4QzitVqU7ulci6D-FnK2-iNNERCGv_hs86vM_uYi_lO4pJuJGIlEQYl-pNMF1VXJLdMpuFfk18MSr40bO-mB-nPncOW4hEO1EtZldzM73UyCnJ.png)

When Google displays the most relevant page version, users are more likely to click your result, have a good experience on your website, and contribute to your business goals.

Hreflang attributes also help search engines find and understand relationships between localized pages.

Without hreflang, search engines may view translated or regionalized pages as [duplicate pages](https://www.semrush.com/blog/duplicate-content/). And this can harm your search visibility.

## How to Implement Hreflang

To implement hreflang, identify a set of pages on your site that share the same content but for different languages or countries. Then assign each page a different identifier, depending on its targeting.

The anatomy of hreflang code is **hreflang="value"**, where **value** is filled in based on one of the following:

- **Language code**: The two-letter [ISO 639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) for the page’s language. For example, **en** for English. You should use this option if the page serves as a default for all speakers of the language.
- **Language and country code**: The [ISO 639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) and [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) for the target language/country, separated by a hyphen (-). For example, **en-us** for English-United States. The country code is only required if your page is region-specific and doesn’t serve as a default for all speakers of the language.
- **X-default**: Use the **x-default** value for the main version of your page. Search engines will display the default if no variant matches the user’s language or language-region.

Finally, follow one or more of the hreflang implementation methods below.

### Hreflang Tags in HTML Headers

You can use hreflang tags in pages’ HTML header elements (<head> sections) to inform search engines about the language/region targeting of a page and its variants.

An hreflang tag specifies a URL and its hreflang attribute, like this:

`<link rel="alternate" href="url" hreflang="value" />`

Every affected page should have an hreflang tag that references the source page **and** its variants.

For example, the tag highlighted below shows that the source page is written in German for audiences in Germany (de-de).

The other hreflang tags show that the page is also available in English for audiences in Ireland (en-ie), French for audiences in Guinea (fr-gn), etc.

![Hreflang tag is shown in the code with list of other hreflang tags for that page.](https://static.semrush.com/blog/uploads/media/f0/7f/f07f56a123daa38d1568449ca5538727/c5671439c220620d6526037b070098d5/AD_4nXcram_OPfb7u3Nvp76cvju7V1uS7b4XtKMQ0qWYRlC175ZW8IjizNPH-Z5bkCWn20bIv26pvLtRI3RTUJdXGVrGoMLTdb8LrGCjbgExaustTjIxehBLkCRP7IfmjN_43ajkRp8X9g.png)

These same hreflang tags are used on all other versions of the page as well.

For example, here’s a snippet of HTML from the English version for audiences in Ireland:

![In the source code, the hreflang attribute shows the Ireland URL and the hreflang value en-ie.](https://static.semrush.com/blog/uploads/media/b1/6c/b16c59dee3ffa7e9bf3d0241bf0a7b4e/3ce82d0ff19e0b643ff8f39ebe70ec60/AD_4nXc5TRbScyMPX9Oooxexix2jIIM05A7o8WyTIjnwCs_lZstqFXxBOM8WHJZwpt7gRT0oH0BHnUjkYCStnzhv41H7ECUbMPyi0oyYR1N97hJgDz2hE1hF1rLbTkcRChj_0RE7FHm3PQ.png)

### Hreflang in the XML Sitemap

You can use hreflang in your website’s [XML sitemap](https://www.semrush.com/blog/xml-sitemap/) to inform search engines about language and region targeting across your website.

The XML sitemap is a file that should list all the URLs you want search engines to index (add to the database of possible search results).

Here’s what you need to do for pages with language/region variants:

- Include a <url><loc> entry for every URL variant
- Within each <url> element, use the <xhtml:link> element to provide the hreflang information for the specified URL **and** its variants

For example, if you have two versions of a page, the corresponding XML code should look something like this:

`<url>
<loc>https://www.example.com/</loc>
<xhtml:link rel="alternate" href="https://www.example.com/" hreflang="x-default" />
<xhtml:link rel="alternate" href="https://www.example.com/gb/" hreflang="en-gb" />
</url>
<url>
<loc>https://www.example.com/gb/</loc>
<xhtml:link rel="alternate" href="https://www.example.com/" hreflang="x-default" />
<xhtml:link rel="alternate" href="https://www.example.com/gb/" hreflang="en-gb" />
</url>`

Note that both URLs reference themselves **and** each other.

### Hreflang in HTTP Response Headers

If you have a non-HTML page (like a PDF), you need to implement hreflang via the HTTP header.

Use this template to tell search engines about the language (and region if you wish) associated with the source page **and** its variants:

`<url1>; rel="alternate"; hreflang="value1", <url2>; rel="alternate"; hreflang="value2" …`

For example, you might add this to the HTTP header of all three listed pages:

`<https://www.example.com/>; rel="alternate"; hreflang="x-default", <https://www.example.com/us/>; rel="alternate"; hreflang="en-us", <https://www.example.com/gb/>; rel="alternate"; hreflang="en-gb"`

Again, note that the variant pages should reference themselves **and** each other.

## Best Practices for Hreflang

Follow these best practices when using hreflang on your website:

### Use Canonical URLs in Hreflang Code

You should only use [canonical URLs](https://www.semrush.com/blog/canonical-url-guide/) in hreflang code to avoid confusing search engines and harming your SEO performance.

A canonical URL is the main address for a webpage and the URL that search engines use in search results. Search engines ignore any alternate URLs to save resources and prevent duplication.

Let’s say you can access the same page via three addresses:

- **Canonical URL**: https://www.example.com/en/
- **Alternate URL**: https://www.en.example.com/
- **Alternate URL**: example.com/en

You should only reference the canonical URL in hreflang code and avoid any alternate URLs.

In practice, this means you should **not** reference:

- URLs that have a [301 redirect](https://www.semrush.com/blog/301-redirects/) pointing to another URL
- URLs that have a [canonical tag](https://www.semrush.com/blog/canonical-url-guide/#what-is-a-canonical-tag) pointing to another URL
- Broken URLs (e.g., URLs that serve a [404 error](https://www.semrush.com/blog/404-error/))

### Keep Your Hreflang Code Updated

Update your hreflang code if you add, remove, or change URLs that have localized variants to avoid outdated code that can confuse search engines and harm your SEO.

Let’s say you implement hreflang via your XML sitemap for your English and Spanish website.

If you later translate your site into German, you need to:

- Add the new URLs (and their hreflang code) to your XML sitemap
- Update XML entries for existing page variants to ensure they reference the German variants

### Audit Your Website for Hreflang Issues

Regularly audit your website for hreflang issues to check for any mistakes that could confuse or mislead search engines—and so harm your SEO.

Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool can help you find and fix the most common hreflang SEO issues, including:

- Invalid hreflang values
- Pages without self-referencing hreflang attributes
- Pages with missing hreflang attributes
- References to broken or non-canonical URLs
- Mismatches between the language code and the page’s language

![Search for hreflang in Site Audit shows how many pages have attribute and value issues as well as how to fix them.](https://static.semrush.com/blog/uploads/media/3a/e0/3ae0553511ab817563195871ab112076/e616025d60f1c76ee4caf72dbd920efb/AD_4nXfuQLMKbr_1AAU6uTldbQ8BJaMh1QSCMziveAhu7qqU2VMjKhC2AQ6v9-iv2vU-LBV563QIi6SCiG1IMidyFXSiwjFUjGxn508eXxSR9KO8Iq_drTHa5aRV0ccQ9HXEFuGiJacR2w.png)

The [SEO Audit](https://www.semrush.com/siteaudit/) tool also helps you find and fix many other kinds of SEO issues. And free users can crawl up to 100 pages per month.
