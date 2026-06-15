---
title: "Hreflang: The Easy Guide for Beginners"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "hreflang-tags"
url: "https://ahrefs.com/blog/hreflang-tags/"
canonical: "https://ahrefs.com/blog/hreflang-tags/"
author: "Joshua Hardwick"
published: "2019-06-07T00:12:50+00:00"
updated: "2026-06-06T22:03:19+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
fetched_at: "2026-06-12T11:40:40+00:00"
status_code: 200
html_hash: "0d68e9d7350a7a4c0a38121c3957fd95f4846ad66c396dcd15f788a80460d2d1"
clean_word_count: 5490
clean_char_count: 33815
---
# Hreflang: The Easy Guide for Beginners

If your website has content in multiple languages, then you must understand and use the hreflang attribute. In this post, we’ll cover everything from the basic concept, to implementation, to troubleshooting common issues.

Hreflang is a simple HTML attribute, but it can be challenging to get to grips with.

Google’s John Mueller described hreflang as “one of the most complex aspects of SEO” because it gets “really hard quickly.”

> TBH hreflang is one of the most complex aspects of SEO (if not the most complex one). Feels as easy as a meta-tag, but it gets really hard quickly.— John (@JohnMu) [February 19, 2018](https://twitter.com/JohnMu/status/965507331369984002?ref_src=twsrc%5Etfw)

When we ran a [study on hreflang](https://ahrefs.com/blog/hreflang-study/) across 374,756 domains, we found that 67% of the hreflang implementations had issues. Here are the most common issues:

But don’t let that put you off. Hreflang isn’t that complicated to understand, and you can **automate** it to a large extent. (We’ll talk about that later on.)

Here’s everything you’ll learn in this guide:

- [What the hreflang attribute is](#what-is-hreflang)
- [Why hreflang matters for SEO](#why-hreflang-matters)
- [What hreflang looks like](#hreflang-syntax)
- [How to construct a hreflang tag](#how-to-construct-hreflang)
- [How to implement hreflang](#how-to-implement-hreflang)
- [How to semi-automate hreflang implementation](#how-to-automate-hreflang)
- [How to find and fix hreflang issues](#how-to-find-and-fix-hreflang-issues)
- [Problems Google may ignore](#hreflang-issues-google-ignores)
- [Why you should be careful redirecting users](#redirecting-users-issues)

New to technical SEO? Check out our

[Beginner’s guide to technical SEO](https://ahrefs.com/blog/technical-seo/)

## What is hreflang?

Hreflang is an HTML attribute used to specify the language and geographical targeting of a webpage. If you have multiple versions of the same page in different languages, you can use the hreflang tag to tell search engines like Google about these variations. This helps them to serve the correct version to their users.

For example, if we Google “apple official website” in the US, this is the first result:

If we do the same in Spain, we see this version of the page:

Hreflang makes this possible.

## Why does hreflang matter for SEO?

If you’ve spent time translating your content into multiple languages, then you’ll want search engines to show the most appropriate version to their users.

Both Google and [Yandex](https://yandex.com/support/webmaster/yandex-indexing/locale-pages.html) look at hreflang tags to help do this.

Bing [says](https://twitter.com/facan/status/1304120691172601856) hreflang is a weak signal for them and that they mostly rely on the [content-language HTML attribute](https://www.w3.org/International/questions/qa-html-language-declarations), links, and who’s visiting your site to discern language. However, they still recommend that you use it in their [official documentation](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a).

Sidenote.

 Baidu doesn’t look at hreflang tags. They rely on the content-language HTML attribute.

Catering to the native tongue of search engine users also improves their experience. That often results in fewer people clicking away from your page and back to the search results (i.e., higher [dwell time](https://ahrefs.com/seo/glossary/dwell-time)), a lower [bounce rate](https://ahrefs.com/blog/bounce-rate/), a higher time on page, etc.—all that other good stuff that we believe has a positive impact on SEO and rankings.

But as Google’s Gary Illyes alludes to in [this video](https://youtu.be/6ewntnqltI4?t=335), hreflang tags can also have a direct effect on rankings because pages in a hreflang cluster share each other’s ranking signals in certain scenarios. For example, duplicate pages may consolidate signals. Hreflang is one of [~40 canonicalization signals](https://ahrefs.com/blog/canonicalization/). This leads to an interesting trade-off where having the same content may create a stronger page because of the duplicate consolidation, but then the wrong page might show in the SERPs. It’s why I mostly push for a single page for each language with dynamic personalization based on the country.

The page that is the best match will determine the ranking position, but search engines will try to swap and show the most relevant page for a user in the SERPs. That doesn’t mean that all the pages in the cluster share signals, but for ones like a brand term or a term used in multiple languages, then the ranking will be based on the top page, but swapped to show the most relevant page. i.e. a search for “Ahrefs” in Japan would probably have the English version of the page as the one with the highest ranking which would determine the position, but in the re-ranking process would swap to show the Japanese page. “Link building” is also a term used in multiple languages, so our English page on the topic is probably the strongest and the one that would determine the ranking position for a user searching in Spanish, but then the page shown in the SERPs would likely be swapped to show our Spanish page for them.

That in itself should be a compelling enough reason to implement hreflang where appropriate.

Still, there’s one other reason why hreflang attributes are important: **duplicate content**.

Say that you have two versions of your page: one targeting UK readers with British English spellings, and one targeting US readers with American English spellings. These two pages are almost identical, and thus, Google may see them as duplicate content and choose one version to index.

Hreflang tags help Google to understand the relationship between these pages. They will try to show the correct version shown in search results, but it is not guaranteed. Hreflang tags are a signal, not a directive. It’s still best practice to localize the content of pages that use the same language within an hreflang cluster. You can do this by localizing pricing (e.g., USD vs. GBP), language variants (e.g., trashcan vs. bin for US vs. the UK), and so forth. This is not a concern for translated pages since they are not considered duplicates by Google.

## What does a hreflang tag look like?

Hreflang tags use simple and consistent syntax:

`<link rel="alternate" hreflang="x" href="https://example.com/alternate-page" />`

Here’s what each part of that code means in plain English:

1. link rel=“alternate”: The link in this tag is an alternate version of this page.
2. hreflang=“x”: It’s alternate because it’s in a different language, and that language is *x*.
3. href=“https://example.com/alternate-page”: The alternate page can be found at this URL.

## How to construct a hreflang tag

Constructing a hreflang tag is as simple as looking up the code for your chosen language and filling in the tag. Hreflang supports any two-letter ISO 639-1 language code. (See a full list of them [here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).)

**Example:**

Say that we wanted to add a hreflang tag from [the English version of our blog post about free keyword tools](https://ahrefs.com/blog/free-keyword-research-tools/) to [the German version](https://ahrefs.com/blog/de/kostenlose-keyword-recherche-tools/). This is the hreflang tag we’d end up with:

`<link rel="alternate" hreflang="de" href="https://ahrefs.com/blog/de/kostenlose-keyword-recherche-tools/" />`

All we did was fill in the language code (de for Germany) and URL.

### Targeting a locale (optional)

While it’s fine to specify a language and leave it there, hreflang tags also support the addition of a region or country. This is also a two-letter code, but this time it’s in the ISO 3166-1 alpha-2 format ([full list](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). You only need to add this when you wish to target speakers of a particular language in a particular locale. For example:

**English speakers in the UK:**

`<link rel="alternate" hreflang="en-gb" href="https://example.com/uk/hello" />`

**English speakers in the US:**

`<link rel="alternate" hreflang="en-us" href="https://example.com/us/hello" />`

You can see that the syntax here is: hreflang=“language-country.”

Why you might need to specify both

Imagine that you run an ecommerce store selling a single product. Your store ships to both the US and the UK, both of which are predominantly English-speaking countries. However, customers in the US want to buy in dollars, whereas customers in the UK want to buy in pounds.

To solve this problem, you create two versions of your product page. One displays the price in dollars, the other in pounds.

Pricing aside, these two pages are identical, so you need to use hreflang tags to signal to search engines why the two versions exist.

There may also be times when you need to do things the other way around: i.e., target speakers of multiple languages in the same country.

For example, imagine that you have a blog post about budget road trips in Canada. Canada has two official languages: English and French. [56.9% and 21.3%](https://en.wikipedia.org/wiki/Languages_of_Canada) of Canadians speak English and French respectively, so it’s probable that you’ll benefit from having two variants of this post.

## The basics of hreflang implementation

Hreflang tags are reasonably simple to implement, and we’ll discuss three methods for doing that in a moment. But no matter which method you opt for, there are three golden rules that you must remember at all times.

### Rule #1: Hreflang tags are bidirectional

It’s critical to understand that hreflang tags work in pairs. In other words, if you add a hreflang tag to an English page pointing to the Italian variant, then the Italian variant **must** return the favor with a hreflang tag pointing to the English page.

This proves to search engines that you have control over both pages, and that they’re each in agreement about their relationship to one another. These pairs form a cluster of pages, referred to as an hreflang cluster.

It’s similar to setting a relationship status on Facebook. You could easily declare yourself as in a relationship with Jennifer Aniston or Brad Pitt, but unless they do the same, nobody is going to believe you.

As such, when the tags are broken, or the relationship hasn’t been fully established yet, you may see the wrong page, multiple pages, or the wrong title for the right URL shown in the search results.

### Rule #2: Self-referential hreflang attributes are good practice

Google [states](https://support.google.com/webmasters/answer/189077?hl=en) that “each language version must list itself as well as all other language versions.” In plain English, that means that every page should have a self-referential hreflang tag—i.e., one that points back to itself.

So, if we want to add a hreflang tags between an English page (https://example.com/hello) and an Italian page (https://example.com/ciao), each should have the following hreflang tags:

`<link rel="alternate" hreflang="it" href="https://example.com/ciao" />`
 `<link rel="alternate" hreflang="en" href="https://example.com/hello" />`

The first specifies the URL of the alternate Italian version of the page, and the second is a self-referencing tag that points back to the page itself.

The Italian page would also need both of these hreflang tags.

Sidenote.

 Google’s John Mueller did [recently](https://twitter.com/JohnMu/status/1012702315474632704) say that “self referential hreflang is optional - but good practice.” It’s mostly a holdover from a time when you would copy all of the tags between pages. I wouldn’t worry too much if you don’t have the self-referencing tags, but best practices say to have them.

### Rule #3: X-default tags are recommended, but not mandatory

The hreflang x-default tag specifies the default or fallback page that gets shown to users when no other language variant is appropriate. You don’t have to use them, but Google [recommends](https://support.google.com/webmasters/answer/189077?hl=en) that you do. This is what one looks like:

`<link rel="alternate" hreflang="x-default" href="https://example.com/" />`

There’s no validation on Google’s end for x-default. Many SEOs believe that each cluster has only 1 x-default tag, but in reality each page could technically have its own x-default.

PRO TIP

Hreflang tags work on a best-match basis. In other words, Google returns the version of content that it deems to be the best match based on various signals like the user’s country and language settings.

To illustrate how this works, imagine that Google is returning a result for an English-speaking user located in Spain.

Google first looks for a language-country match (e.g., en-es) and returns that page if it exists.

If not, it looks for a language code match (e.g., en).

If that doesn’t exist, Google will fallback to the x-default version.

## How to implement hreflang tags

There are three ways to implement the hreflang attribute:

1. HTML tags
2. HTTP headers
3. Sitemaps

### 1. Implementing hreflang tags using HTML

If you’re new to hreflang, then using basic HTML tags is probably the easiest and quickest way to implement. All you need to do is add any appropriate hreflang tags (as discussed above) in the <head> tag of your web page.

#### Example:

We recently launched the Ahrefs blog in several different languages, including [German](https://ahrefs.com/de/), [Russian](https://ahrefs.com/ru/), [Chinese](https://ahrefs.com/zh/), and [Spanish](https://ahrefs.com/es/). We’re now slowly translating English versions of the posts on our main blog into these languages. One of the posts we’ve already translated into both Chinese and German is [our list of the best free keyword research tools](https://ahrefs.com/blog/free-keyword-research-tools/).

Here are the URLs for all three variants:

**English:** `https://ahrefs.com/blog/free-keyword-research-tools/`
 **German**: `https://ahrefs.com/blog/de/kostenlose-keyword-recherche-tools/`
 **Chinese:** `https://ahrefs.com/blog/zh/free-keyword-research-tools/`

To implement hreflang tags correctly for this setup, we’d add this code to the <head> section of each of our pages:

```
<link rel="alternate" hreflang="en" href="https://ahrefs.com/blog/free-keyword-research-tools/" />
<link rel="alternate" hreflang="de" href="https://ahrefs.com/blog/de/kostenlose-keyword-recherche-tools/" />
<link rel="alternate" hreflang="zh" href="https://ahrefs.com/blog/zh/free-keyword-research-tools/" />
<link rel="alternate" hreflang="x-default" href="https://ahrefs.com/blog/free-keyword-research-tools/" />
```

The issue with this method is that it gets pretty time-consuming and messy very easily.

Case in point, if we were to also translate our list of free keyword research tools into Spanish, then we’d have to go back and add another hreflang tag to **all other variations** of that page.

There are [no limits to the number of hreflang tags](https://twitter.com/Modestos_/status/915514391537356800) you can have on a page.

### 2. Implementing hreflang HTTP headers

For non-HTML pages such as PDFs, it’s not possible to implement hreflang by placing tags in the <head> of the HTML. Reason being, there is no HTML. In such cases, you can use HTTP headers to specify the relative language of document variants. This method also works fine with normal webpages but is more commonly used with other content types.

#### Example

Imagine that we convert each version (English, Spanish, German) of our free keyword research tools post to PDF.

Here’s what the HTTP header should look like for each of those files:

```
HTTP/1.1 200 OK
Content-Type: application/pdf
Link: <https://ahrefs.com/blog/free-keyword-research-tools.pdf>; rel="alternate";hreflang="x-default",
<https://ahrefs.com/blog/free-keyword-research-tools.pdf>; rel="alternate";hreflang="en",
<https://ahrefs.com/blog/de/kostenlose-keyword-recherche-tools.pdf>; rel="alternate";hreflang="de",
<https://ahrefs.com/blog/zh/free-keyword-research-tools.pdf>; rel="alternate";hreflang="zh"
```

### 3. Implementing hreflang in your XML sitemap

Sitemaps can include relevant markup to specify the hreflang of a page and its variants. For this, you can use the xhtml:link attribute.

#### Example

If we run with our original example (the three HTML variants of our list of free keyword tools), then this is the full markup for our sitemap:

```
<url>
<loc>https://ahrefs.com/blog/free-keyword-research-tools/</loc>
<xhtml:link rel="alternate" hreflang="x-default" href="https://ahrefs.com/blog/free-keyword-research-tools/" />
<xhtml:link rel="alternate" hreflang="en" href="https://ahrefs.com/blog/free-keyword-research-tools/" />
<xhtml:link rel="alternate" hreflang="de" href="https://ahrefs.com/blog/de/kostenlose-keyword-recherche-tools/" />
<xhtml:link rel="alternate" hreflang="zh" href="https://ahrefs.com/blog/zh/free-keyword-research-tools/" />
</url>
<url>
<loc>https://ahrefs.com/blog/de/kostenlose-keyword-recherche-tools/</loc>
<xhtml:link rel="alternate" hreflang="x-default"
href="https://ahrefs.com/blog/free-keyword-research-tools/" />
<xhtml:link rel="alternate" hreflang="en" href="https://ahrefs.com/blog/free-keyword-research-tools/" />
<xhtml:link rel="alternate" hreflang="de" href="https://ahrefs.com/blog/de/kostenlose-keyword-recherche-tools/" />
<xhtml:link rel="alternate" hreflang="zh" href="https://ahrefs.com/blog/zh/free-keyword-research-tools/" />
</url>
<url>
<loc>https://ahrefs.com/blog/zh/free-keyword-research-tools/</loc>
<xhtml:link rel="alternate" hreflang="x-default"
href="https://ahrefs.com/blog/free-keyword-research-tools/" />
<xhtml:link rel="alternate" hreflang="en" href="https://ahrefs.com/blog/free-keyword-research-tools/" />
<xhtml:link rel="alternate" hreflang="de" href="https://ahrefs.com/blog/de/kostenlose-keyword-recherche-tools/" />
<xhtml:link rel="alternate" hreflang="zh" href="https://ahrefs.com/blog/zh/free-keyword-research-tools/" />
</url>
```

This may look like the least efficient and most nightmarish way to implement hreflang attributes, but often the opposite is true. Reason being, everything is defined in a single file. There’s no need to edit multiple HTML documents each time you make a slight change or delete a page.

What’s more, the additional overhead in headers and the added code in HTML means that a large number of hreflang tags can have an impact on your site speed whereas implementing through your sitemap does not cause the same slowdown.

## How to semi-automate hreflang implementation

Earlier in this guide, I showed a tweet from Google’s John Mueller where he stated that the hreflang attribute is the most complex part of SEO. Here it is again for good measure:

> TBH hreflang is one of the most complex aspects of SEO (if not the most complex one). Feels as easy as a meta-tag, but it gets really hard quickly.— John (@JohnMu) [February 19, 2018](https://twitter.com/JohnMu/status/965507331369984002?ref_src=twsrc%5Etfw)

His reason for this is that it “gets really hard really quickly.”

This is definitely true for large multilingual sites. However, given that you’re here reading what is effectively a beginner’s guide to hreflang tags, my guess is that your website isn’t one of a multinational brand with tens of thousands of customers, but rather a small-to-medium-sized site with some multilingual content.

If that’s the case, then I have good news:

**Generating and implementing your hreflang tags can be automated to a large extent.**

To do it, make a copy of [this Google Sheets template](https://docs.google.com/spreadsheets/d/1Ve8xOhq2Og-J6PdKiLuJ3ySeR3Gvdhw9dCzJLKNzdkg/copy), then follow the instructions below.

### 1. Choose your languages and localities

Head over to the “Setup” tab in the Google Sheet. Select the default language (or language-locale) for your website, along with up to four other variations.

For example, if we were setting up this sheet for the Ahrefs blog, we would specify English as our default, then Spanish, German, Russian, and Chinese as the four alternative variations.

### 2. Paste in your URLs

Head to the “URLs” tab. You should see up to five columns, each of which will have a header cell corresponding to the languages chosen in the previous step. There is also a column for “x-default” values.

Paste URLs into the sheet as appropriate.

For example, if we were doing this for the Ahrefs blog, we would paste any English posts (our primary/default language) in the first column. Then, we would paste the URLs of the relevant translated versions into the other columns.

Do this for all relevant international pages on your website.

### 3. Download the hreflang XML sitemap

Head to the “Results” tab where you will find auto-generated code for an XML sitemap.

Copy everything in column A. Paste it into an XML document.

Upload this to your website, then submit to Google via Search Console.

### 4. Log changes in the sheet

Whenever you add or remove a translated page from your website, log that change in this Google sheet. If you remove a page, delete that URL. If you add a new translated version of a page to your website, add that to the appropriate column.

The sheet will regenerate the sitemap code on the fly. You just need to copy/paste it into your sitemap in place of the old code.

## How to audit your site for hreflang issues

No matter how much you try to stay on top of hreflang attributes, some mistakes will almost always slip through the net. For that reason, it’s crucial to regularly audit your website for [hreflang issues](https://ahrefs.com/blog/hreflang-study/) and nip them in the bud as soon as possible.

The easiest way to do that is to crawl your website using [Ahrefs’ Site Audit tool](https://ahrefs.com/site-audit) regularly.

To make it easy to understand and showcase hreflang issues, we added a visualization for the hreflang clusters, as well as more data about all the tags we saw and the location. This helps you easily see and explain errors, rather than having complex spreadsheets that you need to explain.

Site Audit is a cloud-based crawler that checks your site for hundreds of SEO-related issues, including those related to hreflang.

Here are the nine hreflang related issues Site Audit may find, and how to fix them:

### 1. Self-reference hreflang annotation missing

This warning triggers when a self-referencing hreflang tag is absent from one or more pages.

#### Why it’s an issue

To reiterate our point from earlier, Google [states](https://support.google.com/webmasters/answer/189077?hl=en) that “each language version must list itself as well as all other language versions,” so it’s important to use a self-referencing hreflang tag whenever you add a hreflang tag to a web page.

#### How to fix

Review the affected pages, then add a self-referencing hreflang tag to each of them using your chosen method.

### 2. Hreflang annotation invalid

This warning triggers when one or more URLs have hreflang tags with invalid language or locale codes.

#### Why it’s an issue

Search engines ignore any invalid hreflang tags, meaning that they may overlook alternate versions of your page. This is bad for SEO because it means search engines may not be able to show the most appropriate version of your page to users.

#### How to fix

Review the affected page. Check the “Is valid hreflang” column to see the invalid hreflang tags for each page. Remove these in favor of hreflang tags that use valid language or language-location code formats.

### 3. Page referenced for more than one language in hreflang

This warning triggers when one or more URLs are referenced for more than one language in hreflang annotations. For example:

`<link rel="alternate" hreflang="en" href="http://example.com/page.html" />`
 `<link rel="alternate" hreflang="de" href="http://example.com/page.html" />`

#### Why it’s an issue

Each piece of content should only serve one language or language-location. Having two or more contradicting references will confuse search engines, and they may end up ignoring both hreflang attributes.

#### How to fix

Review the affected pages, then inspect the URLs that reference the page in their hreflang attributes for errors. Remove the incorrect hreflang attribute to leave only one correct attribute per language.

### 4. Missing reciprocal hreflang (no return-tag)

This issue triggers when confirmation (return) links are missing for the pages declared in hreflang annotations.

#### Why it’s an issue

Hreflang tags are bidirectional (i.e., if page A links to page B in hreflang annotations, page B must link to page A in return).

#### How to fix

Review the affected pages. Add bidirectional hreflang tags where necessary.

Here’s another way to check for this issue…

Head to the International targeting report in [Google Search Console](https://ahrefs.com/blog/google-search-console/) and select the “Language” tab. Any issues relating to missing return tags are flagged.

This report also flags issues where nonexistent language or language+country codes are used.

### 5. Hreflang to non-canonical

This issue triggers when one or more page’s reference a non-canonical URL in their hreflang tags.

#### Why it’s an issue

Rel=“alternate” hreflang=“x” will instruct search engines to show the translated (localized) version of a page while rel=canonical attribute will flag that this is not the authoritative (canonical) version. These two attributes contradict each other and confuse search engines.

#### How to fix

Review the affected pages. Modify their hreflang annotations so that they point to canonical URLs only. Or, if you find a page with a rogue canonical tag, remove that from the page to ensure that the hreflang attribute is properly understood and followed by search engines.

Got multiple versions of pages in the same language?

Google may see them as duplicates and choose only one URL as the canonical.

For example, let’s say that you have two product pages, one for the US (“en-us”) and one for the UK (“en-gb”). The content on both pages is almost identical, with the only difference being that prices are in US dollars on one page and British pounds on the other.

If Google chooses one of these as the canonical, it’ll exclude all except for one from the index.

If you suspect this might be happening for a particular page, use the [URL inspection tool](https://support.google.com/webmasters/answer/9012289?hl=en) in Search Console to see how Google views that page.

### 6. Hreflang and HTML lang mismatch

This issue triggers when there is an inconsistency between the declared hreflang and HTML language attribute for one or more URLs.

#### Why it’s an issue

Google doesn’t use the HTML language attribute, but other search engines and browsers do. It’s important to keep these two attributes consistent with one another.

#### How to fix

Review the affected pages. Change the HTML language attribute to ensure consistency with the declared hreflang attribute.

### 7. Hreflang to broken page

This issue triggers when one or more page’s reference broken URLs in their hreflang annotations.

#### Why it’s an issue

Google and other search engines cannot show its users content that doesn’t exist. For that reason, hreflang attributes pointing to dead pages will most likely be overlooked by Google and other search engines.

#### How to fix

Review the affected pages. Change the hreflang annotations to ensure that they link to working pages.

### 8. More than one page for the same language in hreflang

This issue is triggered when one or more URLs reference two or more page’s for the same language (or language-location) in their hreflang annotations.

#### Why it’s an issue

Referencing multiple pages for the same language (or language-location) in hreflang annotations only serves to confuse search engines. They will often ignore or misinterpret such directives.

#### How to fix

Review the affected pages. Remove one of the hreflang annotations so that only one page is referenced for each language.

### 9. X-default hreflang annotation missing

This issue is triggered when there is no x-default hreflang annotation on the page.

#### Why it’s an issue

Although x-default hreflang attributes are optional, Google [recommends](https://support.google.com/webmasters/answer/189077?hl=en) them as a way for you to “control the page when no languages match.” SEO best practice is to use x-default tags for all hreflang annotations.

#### How to fix

Review the affected pages. Make sure each of them has an “x-default” hreflang attribute set. Ensure that this points to a page not specific to one language or region.

…….

To keep on top of hreflang issues that may arise over time, consider scheduling a daily, weekly or, monthly crawl in [Ahrefs’ Site Audit tool](https://ahrefs.com/site-audit). You can do that in your project settings.

New issues will show in the *Localization* report for the associated project after each scheduled crawl, so make sure to check this periodically.

### Using Ahrefs’ Site Explorer to check for incorrect rankings

Paste a domain, subdomain, subfolder path for the language you want to check into [Ahrefs’ Site Explorer](https://ahrefs.com/site-explorer), then go to the “Organic search” tab on the “Overview” report.

Look at the list of countries by search traffic. Are they what you would expect to see?

Here, the German version of our website (*ahrefs.com/de)* ranks in Germany and other German-speaking countries like Austria and Switzerland, which is to be expected. But it’s also getting traffic from the United States and India, which seems odd.

Checking different versions of your site like this is a good starting point when looking for potential issues with hreflang tags.

## Problems with hreflang that Google may ignore

While it’s still wise to follow best practices, there are times when search engines may ignore certain issues. Usually, this happens when a search engine sees the same issue over and over again and believes they can account for it on their end.

Here are a few confirmed hreflang tag issues that Google “fixes” for you:

### 1. Underscore instead of a dash

Gary Illyes mentions in [this Twitter thread](https://twitter.com/dsottimano/status/867315538057474049) that Google’s parsers account for this common error.

### 2. en-UK instead of en-GB

John Mueller covered this in [his AMA](https://www.reddit.com/r/TechSEO/comments/87pxsu/i_am_john_mueller_webmaster_trends_analyst_at/) (Ask Me Anything) on Reddit. Because the UK is a reserved code, they can correct for this issue.

### 3. Hreflang not having a self-reference

Google’s John Mueller [recently](https://twitter.com/JohnMu/status/1012702315474632704) stated that the self-referential hreflang is optional—but good practice.

### 4. Relative vs Absolute URLs

## Be careful redirecting users

Websites will in many cases auto-redirect users based on some combination of cookies, IP address, and/or browser language. This can result in a poor and frustrating experience for users, and is often problematic for search engines trying to index your content. Amongst other things, it can break the connections needed for your hreflang tags.

Here’s what [Google says](https://support.google.com/webmasters/answer/182192?hl=en):

> Do not use IP analysis to adapt your content. IP location analysis is difficult and generally not reliable. Furthermore, Google may not be able to crawl variations of your site properly. Most, but not all, Google crawls originate from the US, and we do not attempt to vary the location to detect site variations. Use one of the explicit methods shown here (hreflang, alternate URLs, and explicit links).

Always treat search engine crawlers as you would a user from any location. If you’re treating the search engine bot different than you would a user, that is considered [cloaking](https://support.google.com/webmasters/answer/66355?hl=en) and is a violation of Google’s Webmaster Guidelines.

What you can do is use the same detection logic to suggest a better version of the page for the user on a small banner.

Be careful not to take up too much space with this banner. If it’s too large, the banner could be seen as an [interstitial](https://webmasters.googleblog.com/2016/08/helping-users-easily-access-content-on.html).

## A few more warnings

Encoding characters in URLs with UTF-8 is fine for Google, but there may be a point of failure in your tech stack where it is not supported.

You can’t have hreflang tags in the body because they could be used for hijacking. The tags can be forced into the body section under certain conditions. This is known as breaking the <head> and can be caused by things like iframes or tags not closed in the <head> section, or can be from injecting different things with JavaScript. Use [DOM breakpoints](https://developers.google.com/web/updates/2015/05/view-and-change-your-dom-breakpoints) to troubleshoot.

To see these, you may need to run through one of Google’s tools to see the rendered DOM or “Right Click” > Inspect in Chrome and search the Elements panel of Chrome DevTools.

Don’t block pages with hreflang tags with robots.txt. If Google can’t crawl the pages, then the hreflang tags won’t be seen.

Don’t noindex the pages with hreflang tags. They need to be indexed.

## Final thoughts

Hreflang isn’t *that* complicated. You just need to stay organized, automate the implementation as much as you can, stay on top of any issues that will inevitably arise, and fix those issues as quickly as possible.

Any questions? Let me know in the comments or [on Twitter](https://twitter.com/joshuachardwick?lang=en).
