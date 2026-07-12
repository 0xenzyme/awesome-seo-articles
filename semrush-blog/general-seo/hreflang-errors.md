---
title: "9 Common Hreflang Errors (and How to Fix Them)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "hreflang-errors"
url: "https://www.semrush.com/blog/hreflang-errors/"
canonical: "https://www.semrush.com/blog/hreflang-errors/"
author: "Boris Mustapic"
published: "2024-01-18T11:49:00+00:00"
updated: "2024-01-18T11:49:00+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "General SEO"
fetched_at: "2026-06-12T16:54:22+00:00"
status_code: 200
html_hash: "d252f5931a6f7d1c82c10e04a3d346567ed1e789180025c8fb208f19448513e4"
clean_word_count: 2364
clean_char_count: 15592
---
# 9 Common Hreflang Errors (and How to Fix Them)

Running into issues with hreflang? In this article, we go over the most common ones and show you how to fix hreflang tags with errors.

## What Is the Purpose of Hreflang?

[Hreflang attributes](https://www.semrush.com/blog/hreflang-attribute-101/) are pieces of HTML that specify the language and targeted region of a webpage.

Proper use of hreflang tags is crucial for websites that host multiple versions of webpages in different languages.

Search engines (like Google) use hreflang tags to serve the correct version of a page to users. For example, a user searching for a term like “Semrush blog" in the U.S. will see the U.S. version of the blog.

![The U.S. version of Semrush blog on Google's SERP](https://static.semrush.com/blog/uploads/media/2f/28/2f28b69b358718f098f2efb99bcdb9cf/e985c26d9c9a8c6c8bc79240a1a6833d/j42jr6qiRzYqS1-ntK6uR_mP-HnsZma-FVh6Sas2TdFB2NCsvIpvJcOo6TuH9TBUpjj3Kd9C7z1ZCeDZ484PPUMcxaIYgecjD--JWtMa74VmA34kEcWAr2Nz03bE1TngZ-ks1ouhJlQg0vd8J0XfsVM.png)

But a user from Spain performing the same search will see the Spanish version of the blog instead. Note the “es” subdomain in the image below.

![The Spanish version of Semrush blog on Google's SERP](https://static.semrush.com/blog/uploads/media/67/8a/678a7f5ca9a8c36e3f511a073eeb141e/f4fac51f2c45d98dd072747e6b7ce917/7O0anCOi22LDsK7JnrgiNj-BtKhtJ0ZxriVu9pzYnvnXqAnlxdOmVLoDWC4guDIUuzYYourYyFcDTBC39-dQ7hONOrNej8oIkkIfcwHtlH5hMsXtID2PbCGgPZZKizdIVdNmplg58B2IIrvJzOotLWo.png)

This is possible thanks to hreflang tags.

For a webpage that has two alternate versions—one aimed at a U.S. audience and another at a Spanish audience—an hreflang tag might look like this:

`<link rel="alternate" hreflang="en-us" href="https://website.com/en" />
<link rel="alternate" hreflang="es-es" href="https://website.com/es" />`

Here’s what the different parts of the above code mean:

- **link rel="alternate":** indicates that the URL referred to in the code is an alternate version of a webpage (i.e., one of several versions)
- **hreflang="en-us":** the [ISO code for the language](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) used on the page, followed by the [ISO code for the country](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) at which that webpage is aimed (the country/region code is not always required)
- **href="https://website.com/en":** the URL of the alternative webpage

## The 9 Most Common Hreflang Errors

**A lot** can go wrong when implementing hreflang. Especially for large, complex websites.

Here’s a list of the most common hreflang tag errors and how to fix them.

## 1. Missing Self-Referencing Hreflang Annotation

It might not be obvious, but you need to include a self-referencing hreflang tag for each page. In other words, every page needs to not only reference its alternative versions, but also itself.

If you don’t do this, search engines might ignore your hreflang tags altogether.

**How to fix:** Always use a self-referencing hreflang tag. For example, if you have an English and Spanish version of a page, the code for the English version of the page needs to not only reference the Spanish version as an alternative, but also itself.

It would look like this:

`<link rel="alternate" hreflang="en" href="https://example.com/en" />
<link rel="alternate" hreflang="es" href="https://example.com/es" />`

The same would be required on the Spanish version of the page.

## 2. Return Tag Errors

Return tag errors happen due to a lack of cross-referencing between alternate versions of a page.

Hreflang tags are reciprocal. For example, if you have three alternative versions of a webpage (e.g., in English, Spanish, and Italian), each page needs to **link to all the other pages** within its hreflang attributes.

If you don’t do this, Google might ignore your hreflang tags.

**How to fix:** Ensure all alternative pages link to each other in their hreflang attributes. Below is how that would look for a page in English, Spanish, and Italian.

English page:

`<link rel="alternate" hreflang="en" href="https://example.com/en" />
<link rel="alternate" hreflang="es" href="https://example.com/es" />
<link rel="alternate" hreflang="it" href="https://example.com/it" />`

Spanish page:

`<link rel="alternate" hreflang="es" href="https://example.com/es" />
<link rel="alternate" hreflang="en" href="https://example.com/en" />
<link rel="alternate" hreflang="it" href="https://example.com/it" />`

Italian page:

`<link rel="alternate" hreflang="it" href="https://example.com/it" />
<link rel="alternate" hreflang="en" href="https://example.com/en" />
<link rel="alternate" hreflang="es" href="https://example.com/es" />`

Note that the order in which the alternates are listed above doesn’t matter, but it can make it easier to understand which page each set is for.

## 3. Using the Wrong Country or Language Codes

Hreflang tags need to adhere to the [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) when specifying the language used on a page. If you’re also specifying a region or country within a tag, you must follow the [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

The language and country code need to be **separated by a dash** (do not use underscores).

It’s also important to remember that you can use a language code on its own, but a country code can only be used in combination with a language code.

**How to fix:** Check the official lists (linked above) for language and region codes and make sure you’re using the right ones for your pages.

## 4. Not Using Canonical Tags and Hreflang Tags Together Correctly

You can use [canonical tags](https://www.semrush.com/blog/canonical-url-guide/) to indicate the primary version of a webpage to search engines. A lot of hreflang errors come from using canonical tags and hreflang attributes together incorrectly.

For example, using canonical tags as if they were the self-referencing link in an hreflang tag. Or including the hreflang attribute in the canonical tag, rather than within its own link tag.

Here’s an example of incorrect canonical tag use with hreflang:

Let’s say you have versions of a webpage in three different languages: English, Spanish, and Italian.

You made sure to include return tags in each of them, with each alternative page referencing the other alternative pages. But you included a canonical tag pointing back to the English version of the page in all three cases.

**Incorrect:**

English page:

`<link rel="canonical" href="https://example.com/en" />
<link rel="alternate" hreflang="en" href="https://example.com/en" />
<link rel="alternate" hreflang="es" href="https://example.com/es" />
<link rel="alternate" hreflang="it" href="https://example.com/it" />`

Spanish page:

`<link rel="canonical" href="https://example.com/en" />
<link rel="alternate" hreflang="es" href="https://example.com/es" />
<link rel="alternate" hreflang="en" href="https://example.com/en" />
<link rel="alternate" hreflang="it" href="https://example.com/it" />`

Italian page:

`<link rel="canonical" href="https://example.com/en" />
<link rel="alternate" hreflang="it" href="https://example.com/it" />
<link rel="alternate" hreflang="en" href="https://example.com/en" />
<link rel="alternate" hreflang="es" href="https://example.com/es" />`

This would cause confusion for search engines and could result in search results showing the English version of your page to Spanish and Italian users. Instead, it should look like we have it below.

**Correct:**

English page:

`<link rel="canonical" href="https://example.com/en" />
<link rel="alternate" hreflang="en" href="https://example.com/en" />
<link rel="alternate" hreflang="es" href="https://example.com/es" />
<link rel="alternate" hreflang="it" href="https://example.com/it" />`

Spanish page:

`<link rel="canonical" href="https://example.com/es" />
<link rel="alternate" hreflang="es" href="https://example.com/es" />
<link rel="alternate" hreflang="en" href="https://example.com/en" />
<link rel="alternate" hreflang="it" href="https://example.com/it" />`

Italian page:

`<link rel="canonical" href="https://example.com/it" />
<link rel="alternate" hreflang="it" href="https://example.com/it" />
<link rel="alternate" hreflang="en" href="https://example.com/en" />
<link rel="alternate" hreflang="es" href="https://example.com/es" />`

**How to fix:** Make sure each version of your webpage has a self-referencing canonical tag.

## 5. Not Using Absolute URLs

Using relative URLs instead of absolute URLs in your hreflang tags can cause indexing issues and result in search engines misinterpreting your hreflang tags.

Here’s why:

Relative URLs only provide a partial path to a page, while search engines need the full path (also known as an absolute URL) to properly locate a page.

**Incorrect:**

`<link rel="alternate" hreflang="en" href="/en/page-name" />
<link rel="alternate" hreflang="en" href="/es/page-name" />`

**Correct:**

`<link rel="alternate" hreflang="en" href="https://example.com/en/page-name" />
<link rel="alternate" hreflang="es" href="https://example.com/es/page-name" />`

**How to fix:** Always use the absolute URL in hreflang tags—including http/https.

## 6. Adding Hreflang Tags to Blocked or Broken Pages

There are certain pages on your website that you don’t want search engines to crawl or index. Like checkout and “thank you” pages.

This is usually accomplished by adding the URLs of these pages to your website’s [robots.txt file](https://www.semrush.com/blog/beginners-guide-robots-txt/) or using noindex tags.

But sometimes you might inadvertently noindex one or more alternative pages you are referencing in your hreflang tags. If this happens, it can cause issues because search engines won’t be able to follow the hreflang instructions on the blocked page.

This means they won’t be able to follow the return link on that page that references the alternative versions of the page. This is also true if the link is to a page that doesn’t exist (also known as [error 404)](https://www.semrush.com/blog/what-does-error-404-not-found-mean/).

In this case, Google may ignore the hreflang tags associated with all versions of that page.

**How to fix:** Only add indexable, crawlable pages to your hreflang tags. Likewise, don’t add hreflang tags to pages that are blocked from crawling and indexing.

## 7. Missing or Wrong ‘x-default’ Tag

The "x-default" tag serves to tell search engines that a particular page is the default page that should be shown when the website doesn’t have a page that matches the searcher’s language or region.

If you don’t specify a default page by using the "x-default" tag, you’ll have no control over which version of the page a search engine shows the user if there isn’t one that matches their language or region.

**Incorrect:**

`<link rel="alternate" hreflang="en" href="https://example.com/en" />
<link rel="alternate" hreflang="es" href="https://example.com/es" />
<link rel="alternate" hreflang="it" href="https://example.com/it" />`

**Correct:**

`<link rel="alternate" hreflang="en" href="https://example.com/en" />
<link rel="alternate" hreflang="es" href="https://example.com/es" />
<link rel="alternate" hreflang="it" href="https://example.com/it" />
<link rel="alternate" hreflang="x-default" href="https://example.com/" />`

**How to fix:** Make sure to use an "x-default" tag to specify a default page within your hreflang tags.

## 8. Alternate Versions of a Page Pointing to the Same URL

Hreflang tags rely on distinct URLs to work properly. You can’t have multiple alternate versions of a page pointing to the same URL since that would give search engines no way of knowing which is the best URL to serve to searchers.

**Incorrect:**

`<link rel="alternate" hreflang="en" href="http://www.example.com/page" />
<link rel="alternate" hreflang="es" href="http://www.example.com/page" />`

**Correct:**

`<link rel="alternate" hreflang="en" href="http://www.example.com/en/page" />
<link rel="alternate" hreflang="es" href="http://www.example.com/es/page" />`

Likewise, you shouldn’t have instances of the same alternate language version pointing to multiple different pages. Like this:

`<link rel="alternate" hreflang="en" href="http://www.example.com/en/page" />
<link rel="alternate" hreflang="en" href="http://www.example.com/es/page" />`

**How to fix:** Review your hreflang tags to ensure each alternate version points to a unique URL.

## 9. Hreflang Outside <head> Section

If you’re adding hreflang attributes with HTML tags, they should go inside the <head> section of your webpage.

If you add them elsewhere, search engines might not interpret them properly.

**How to fix:** This one is fairly simple—just make sure you add hreflang tags in the <head> section of each relevant page.

## Fix Your Hreflang Errors with the Semrush Site Audit Tool

Our [free SEO audit](https://www.semrush.com/siteaudit/) can quickly flag hreflang issues. To fix hreflang errors across your entire website, use Semrush Site Audit.

From the Site Audit tool page, enter your domain name and click the “**Start Audit**" button. (If you’ve used the tool before, you’ll click “**+ Create Project**” instead.)

![Site Audit tool search bar](https://static.semrush.com/blog/uploads/media/14/b1/14b1b6dd54bf261f1aedbc960a001564/8644534a8d20d55d72ff7fb1f756bfcd/P1tXOPeW5lzEbHwrm1azITrF1KBHk9ijJewJi1Bynr-0SX2Ngzn4Uy5qRCnVdzfelaHI5LWxtuPV2HD0-GGzrYWLTdiSssSkTS-w3lhV9aO90Q_8ElDESlQ887oj-uECABpzSzqH9svnmS37cohX4wg.png)

You can then change the crawler settings, disallow specific URLs, and more. In most cases, you can keep the default audit settings and click the “**Start Site Audit**" button to start the audit.

!["Site Audit Settings" window](https://static.semrush.com/blog/uploads/media/03/9d/039d14cffb97a533083a9de7b8a76578/1cca6f832466db01b3d0d71b6eb5330b/1cXMN4xIdMhlITaT_Rl3MXa3hSYm2LUbrdwUHogzv3nSCRsYdFOADxrY2m4xDoGMYsXOJYg6wa1JifNDWLVxY6Pu3OgBwcrNVKcrscfD3TO4fBCtPQK0msuDZKFnJnpUgVR97CQvEFP6Kf-D82Ena5Q.png)

The tool will then audit your website and generate a detailed report. To see any hreflang errors the tool discovered, go to the “**Issues**" tab and type in “hreflang" in the search bar.

![“hreflang" entered in the search bar under "Issues" report](https://static.semrush.com/blog/uploads/media/6e/3e/6e3ed35edd9b75e83a89e8fdd9e85c66/ca64d150e3f65362e69825b4e8ab8f8c/57GHN3KbgVYC5GtTOyGmFjmeatZ25vOXIOjiAcTSCb1Q6BO4VY85nica0nZ93pKnwAWxJyWs3iWKKHDcxld7k5FDyR8swyDpnp34mH4OmKtbJJGYsMRfGRMnCs_Aa1dqOKehaDDScXUwkD-XcUcEw6g.png)

You’ll then see a list of all the hreflang errors on your website. Next to each error will be a link titled “**Why and how to fix it**." Clicking on this will show you a tooltip that explains the error and how you can address it.

Clicking on the linked part of each error (e.g., “**1,589 issues**” in the image below) will take you to the list of pages with that specific error present.

![“1,589 issues with hreflang values" error highlighted under a list of hreflang issues in Site Audit](https://static.semrush.com/blog/uploads/media/9c/95/9c95bd867edae9b1444ba6b415a614c0/679f07d72ac51b1d27f0c4519869a32a/Hv4lrzTMrYl_y_wS0yy13PkRfUsTvOlhazJxFaXDLp1cZTECINzYjyp5DMgayZzWnwX81MEcXApiMUwkmLqxKVR0ioKQtdxdhtt2UYGWIlO92ssyOP7Rig9C_Cl21uil_hAg2bCSFC3fnjEX_lUgTMo.jpeg)

Go through the list of errors and fix them one by one. This will ensure that search engines can interpret your hreflang tags correctly and display the right version of your website to searchers every time.
