---
title: "Canonical URLs: SEO Best Practices, Common Issues, and How to Fix Them"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "canonical-url-guide"
url: "https://www.semrush.com/blog/canonical-url-guide/"
canonical: "https://www.semrush.com/blog/canonical-url-guide/"
author: "Alex Lindley, Carlos Silva, Christine Skopec"
published: "2020-05-15T17:19:00+00:00"
updated: "2025-12-19T11:08:00+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "time_sensitive_title"
schema_genre: "General SEO"
fetched_at: "2026-06-12T14:18:30+00:00"
status_code: 200
html_hash: "89064307adca8c3077d8cf7a20b506c3a4727d3e40cfe99ae27ffbf1730931de"
clean_word_count: 3890
clean_char_count: 26465
---
# Canonical URLs: SEO Best Practices, Common Issues, and How to Fix Them

Canonical URLs are the main versions of pages that search engines index and rank in search results when multiple URLs load the same or very similar content.

Having the proper canonical URL strengthens the ranking potential for the page you want users to find.

This guide explains how canonicalization works, how to use canonical tags correctly, when to choose alternatives to canonical tags, and how to ensure Google consistently selects your preferred URLs.

## What Is a Canonical URL?

A canonical URL is the preferred version of a webpage that search engines index and show in search results when multiple URLs lead to the same or very similar content.

For example, both of these URLs may display the same blog page:

- **Canonical URL**: https://example.com/blog/
- **Duplicate URL**: https://example.com/blog/?page=1

You can guide Google’s choice by using canonical tags and other signals. If those signals conflict or Google believes a different version better serves users, it may still select a different canonical URL than the one you declared.

### How Canonicalization Works

Canonicalization works by selecting one canonical URL to use for indexing and ranking from a set of duplicate or near-duplicate URLs.

There are several signals you can rely on to indicate to Google which URL you prefer as the canonical (just be aware Google can still choose a different page as the canonical version):

- Protocol (HTTPS vs. HTTP)
- Use of redirects
- rel="canonical" tags
- Which URLs are included in the sitemap

Duplicate URLs might still be crawled, but they rarely appear in search results unless a specific context—such as device type or region—makes them more relevant.

### Common Scenarios That Create Duplicate URLs

Many sites generate [duplicate URLs](https://www.semrush.com/blog/duplicate-content/) unintentionally, often through these common causes:

- **Protocol variants**: HTTP and HTTPS versions of the same page
- **Domain variants**: www and non-www versions of the same page
- **Trailing slash differences**: Versions of the same page with and without a final slash (e.g., /page vs. /page/)
- [**URL parameters**](https://www.semrush.com/blog/utm-tracking-codes-google-analytics/): Tracking, sorting, or filtering parameters (e.g. ?utm\_source=email, ?sort=price)
- **Session IDs**: Temporary identifiers added during user sessions
- **Device-specific URLs**: Separate mobile URLs like m.example.com and example.com
- **Pagination**: Content is split across different pages but each page is highly similar(e.g. /blog vs. /blog?page=1)

Understanding which scenarios apply to your site makes it easier to apply canonicalization correctly.

## What Is a Canonical Tag?

A canonical tag is an [HTML element](https://www.semrush.com/blog/html-tags-for-seo/) that tells search engines which URL is your preferred version for ranking when multiple pages contain the same or very similar content.

Search engines use canonical tags as one of a handful of signals to decide which page to index and show in search results.

The canonical tag belongs in the <head> section of your HTML and looks like this:

`<link rel="canonical" href="https://example.com/preferred-url-here/" />`

![split screen showing an article and its HTML code, highlighting "Alternate URL" and "Canonical Tag"with arrows](https://static.semrush.com/blog/uploads/media/9e/40/9e40e7c2278baae229a17608b15a73dd/ec9d9f885c15e5c162ff6d5aa0f3da35/image.png)

### How Canonical Tags Work

Canonical tags work by clearly identifying the version of a page you want to rank when duplicates exist.

If example.com/product/blue?sort=price is a duplicate and shows the same content as example.com/products/blue, you'd place this tag pointing to the main URL in the head section of the duplicate URL as well as in the head section of the main URL:

`html<link rel="canonical" href="https://example.com/products/blue" />`

This tells search engines to treat the non-filtered URL as the canonical version and consolidate all ranking signals to that page.

![an illustration of canonical tag pointing from an alternate page to a preferred one](https://static.semrush.com/blog/uploads/media/d1/d0/d1d05eb318f7654fd5ee490f3aada997/3fed4bc7cf6ae29453f417688c662443/image.png)

### What Self-Referencing Canonical Tags Are

A self-referencing canonical tag is a canonical tag that points to the main page’s own URL.

Every canonical page should include a self-referencing canonical tag—even if it has no obvious duplicates.

![split screen of an article and developer tools displaying HTML code highlighting a self-referencing canonical link](https://static.semrush.com/blog/uploads/media/15/c3/15c3f2360e4869afa820d31b63cbe3c2/07a42dc4fcea75418eb4f859636763aa/image.png)

Google's [John Mueller has confirmed](https://www.youtube.com/live/MD6ABXMMuaI?t=1734s) that self-referencing canonicals clarify your preferred URLs. These tags make canonicalization more predictable, especially when other signals (redirects, protocol, and inclusion in sitemaps) don’t all align.

## Why Use Canonical Tags?

Using canonical tags is one of the clearest ways to tell search engines which version of duplicate or similar pages you want to be indexed and ranked.

When you use canonical tags, it allows you to influence:

- **Which URL appears in search results**: Google uses canonical tags as a signal of which URL to show in search results. This keeps alternates out of search results and prevents [keyword cannibalization](https://www.semrush.com/blog/keyword-cannibalization-guide/) (i.e., when multiple pages compete for the same terms and harm each other’s rankings).
- **How link equity is consolidated**: Canonical tags help direct all link equity to your preferred page version, even when you have [backlinks](https://www.semrush.com/blog/what-are-backlinks/) that point to alternate versions

![an illustration of backlinks, alternate URLs and canonical URLs connection](https://static.semrush.com/blog/uploads/media/d6/8f/d68f641d465650f6719457a011d8d60e/b7edec263a65a1a283701d986b7e84e0/image.png)

- **Simplify analytics and reporting**: Canonical tags can consolidate data to a single URL, giving you cleaner performance metrics and clearer attribution for campaigns, keywords, and conversions
- **Reduce wasted crawl budget**: Canonical tags help Google prioritize important URLs and reduce redundant crawling. This is especially useful for large sites with many pages.

## How to Implement Canonical Tags

The most common way to implement canonical tags is by adding a rel="canonical" [link element](https://www.semrush.com/blog/html-link-tag/) to the <head> section of your HTML. This tag identifies the preferred version of a page when duplicates exist:

`<link rel="canonical" href="https://example.com/preferred-url-here/" />`

Most CMS platforms allow you to set canonical tags without touching code. Below is how canonicalization works on major platforms.

### Magento 2

Magento 2 supports automatic canonical tags for both product and category pages when enabled in your configuration settings.

Log in to your admin panel, then go to "**Stores**" > "**Settings**" > "**Configuration**."

Open "**Catalog**" > "**Catalog**" and go to the "Search Engine Optimization" section.

![“Search Engine Optimization” section in Magento 2](https://static.semrush.com/blog/uploads/media/8c/79/8c79085f4d3a7cfcf67ca3b970375b04/2f8e1ad4e19a10cb468f03d349fc0ef6/image.png)

Set "Use Canonical Meta Tags For Categories" to "Yes." Magento will automatically add canonical tags to alternate category pages.

Also set "Use Canonical Meta Tags For Products" to "Yes." Magento will automatically add canonical tags to alternate product pages.

### Shopify

Shopify automatically adds canonical tags to product pages, collections, and blog posts.

Most stores won’t need custom changes, but you can add your own canonical tags if your store is more complex.

#### Adding Canonical Tags Manually

If you need a custom canonical structure, go to your Shopify admin, and navigate to “**Online Store**” > “**Themes**."

Select the three dots and click "**Edit****Code**."

![Shopify interface showing the "Themes" section, with a dropdown menu highlighting the "Edit code" option](https://static.semrush.com/blog/uploads/media/6a/8a/6a8a2c52e2079879beabaac3e40ff2f2/511d4a8b91d9c4dcd8167125b95a38d1/image.png)

In the left sidebar, click the file you want to edit. For site-wide changes, choose "**theme.liquid**."

![Shopify interface showing code editor with "theme.liquid" file open and HTML code displayed](https://static.semrush.com/blog/uploads/media/a0/d5/a0d582d4dcc878ee540de2095eee833c/171521a839e8a507c87f8283c097b983/image.png)

Add or modify the canonical tag using Shopify’s metafields. This may require developer support.

#### Adding Canonical Tags Using Apps

Apps like [Canonical Tag URL Wizard](https://apps.shopify.com/canonical-tag-url-manager) let you set canonicals without editing theme code.

Install the app, access it from your Shopify admin, and use the app to set custom canonical tags.

### WordPress

WordPress requires a [WordPress plugin](https://www.semrush.com/blog/wordpress-seo-plugins/) to manage canonical tags. Let’s go over two options:

#### Yoast SEO Plugin

If you're using the [Yoast SEO](https://wordpress.org/plugins/wordpress-seo/) plugin, open any page or post in the editor, go to the Yoast SEO panel, and open the "**Advanced**" tab.

Enter the preferred URL in the "Canonical URL" field.

![“Advanced” tab in Yoast SEO options](https://static.semrush.com/blog/uploads/media/df/b0/dfb0c9733e733e226983514955989876/b9becaac209a0a47f1b8b8023aedbbbd/image.png)

Yoast automatically adds a self-referencing canonical when the field is left blank.

#### Rank Math SEO Plugin

If you're using the [Rank Math SEO plugin](https://wordpress.org/plugins/seo-by-rank-math/), open any page or post, go to the "Rank Math SEO" box, and open the "**Advanced**" tab.

Enter the canonical URL in the "Canonical URL" field.

![“Advanced” tab in “Rank Math SEO” box](https://static.semrush.com/blog/uploads/media/e2/d8/e2d8298bd255e1f108b424af07e59a75/8639ab4fc1620a0cc9487078d9feddd6/image.png)

Rank Math also generates a self-referencing canonical by default.

### Wix

Wix automatically adds self-referencing canonical tags across your site. You can override them for specific page types or individual pages.

#### Adjusting Canonical Tags in Global Settings

Go to "**Site & Mobile App**" > "**Website & SEO**" > "**SEO & GEO**."

![Wix navigation sidebar with the "SEO & GEO" menu option highlighted](https://static.semrush.com/blog/uploads/media/a5/c8/a5c8ee0407dc60c9104d46e2357297a8/2c53dc705bf4845e7f9aaca1dc22d3e2/image.png)

Scroll down to "Tools & Settings" and select "**Go to SEO Settings**."

![Wix dashboard showing "Tools and settings" for SEO, with a highlighted "Go to SEO Settings" button](https://static.semrush.com/blog/uploads/media/26/f5/26f5d7f1658329e5ebc17754c7b6b1eb/46c47fe11782014f3d21cc332ed72cff/image.png)

Choose the page type (e.g., "Main Pages") you want to adjust the canonical tags for.

![SEO settings panel with the "Main pages" option highlighted by a purple border](https://static.semrush.com/blog/uploads/media/9a/b6/9ab69ada92b34b88c8ed290cc8ae4cdf/ae410deb687b670b2e00f5d05057cf96/image.png)

Select the “**Customize defaults**” tab and click "**Edit**" next to "Additional Meta Tags."

![SEO settings for Main Pages, with the last section, "Additional meta tags" highlighted in a purple box](https://static.semrush.com/blog/uploads/media/d6/55/d655793fb33d31fe7de0cc3889f8ea65/23af58c129ac21a85d33ff79c7e8959e/image.png)

Add or adjust canonical variables using "**+ Add Variable.**"

![Wix user interface showing options for editing canonical tags](https://static.semrush.com/blog/uploads/media/83/e1/83e1faba0408d97b159e0e34978a9e85/931539b3f1eaf5800403b9141d07997a/image.png)

#### Adjusting Canonical Tags on Individual Pages

To adjust canonical tags for individual pages, open the editor, go to "**Pages & Menu**" > "**Store Pages**."

Select a page, click the three-dot icon, and choose "**SEO Basics**."

![Wix website editor displaying "Store Pages" under "Site Pages and Menu," with "SEO Basics" selected for the shop page](https://static.semrush.com/blog/uploads/media/54/a9/54a9661efc86ea56c86b34a18c5f00b7/f0b66ccfcc333eec6db51d9cacfceee9/image.png)

Go to "**Advanced SEO**" > "**Additional Tags**" and add or modify the canonical tag.

![canonical tags in the Wix website editor for the shop page](https://static.semrush.com/blog/uploads/media/d7/18/d71844fea2631a3bd612e09d0af8117d/7f3889c7b6b386bb913095eb8cf453a4/image.png)

## Other Ways to Specify Canonical URLs for SEO

Canonical tags are the most common way to declare a preferred URL, but you can also use [redirects](https://www.semrush.com/blog/redirects/), HTTP headers, sitemaps, and cross-domain configurations to signal which version of a page should be indexed.

Let’s quickly cover the different canonicalization methods and when to use each:

|  |  |  |
| --- | --- | --- |
| Method | When to Use | Limitations |
| rel="canonical" tag | You have duplicate URLs but need to keep the duplicates | Doesn’t work for non-HTML files |
| Redirect | You’re retiring old URLs or consolidating domains | Both versions won’t be accessible |
| rel="canonical" HTTP header | You have non-HTML files or can’t modify HTML | Require server access and is more technical |
| Sitemap | You want to support other canonicalization signals | Not sufficient as a standalone method |

### Using Redirects

[Redirects](https://www.semrush.com/blog/redirects/) send Google and users from one page to another and are good for deduplication when you don’t need to keep alternate versions of a page but don’t want to delete the URLs altogether.

For example, when you have HTTP and HTTPS versions of the same page.

Google prefers HTTPS versions, which means redirecting the HTTP version to the HTTPS one can improve your SEO.

Google recommends using [3xx redirects](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls#redirects-method) (server-side redirects) for the quickest results.

An example is the 301 redirect. Learn more about 301 redirects in our [301 redirect guide](https://www.semrush.com/blog/301-redirects/).

### Using rel="canonical" HTTP Headers

Use a rel="canonical" HTTP header to specify the canonical URL for non-HTML documents.

For example, if you have DOCX and PDF versions of the same document online, using the rel="canonical" HTTP header lets you indicate your preferred version. However, you must be able to modify your server’s configuration to do this.

In the .htaccess file, specify the canonical URL by adding the following code (adjusted for your chosen document):

`Header add Link: <https://www.example.com/downloads/filename.pdf>; rel="canonical"`

### Using Sitemaps

Submit only canonical URLs (non-duplicated pages) in your [sitemap](https://www.semrush.com/blog/website-sitemap/) and exclude alternate URLs to indicate your suggested canonical URLs

Leave alternate versions out of your sitemap, which can include pages like:

- Parameterized URLs
- Paginated content (/page/2, /page/3)
- HTTP versions if HTTPS is canonical

## Canonical Tag Best Practices

Canonical tags work best when they’re implemented correctly and are aligned with your other site signals. So, follow these guidelines for the best results:

### Use Self-Referencing Canonical Tags

Every page should include a canonical tag that points to its own URL, even when no duplicates exist.

For example, if https://example.com/blog/ is your canonical page, include this in its <head> section:

`<link rel="canonical" href="https://example.com/blog/" />`

### Specify One Canonical URL Per Page

Specify only one canonical URL per page to avoid confusing Google.

Multiple canonical tags—or a mix of HTML and HTTP-header canonicals—create conflicting signals that Google may disregard.

Accidental duplication is common when canonicals set via your CMS settings overlap with manually added ones. So, audit your pages and plug-ins to ensure only one canonical is generated.

### Specify the Correct Protocol

If your site uses HTTPS, all canonical URLs must also use HTTPS.

Correct:

`<link rel="canonical" href="https://example.com/blog/" />`

Incorrect:

`<link rel="canonical" href="http://example.com/blog/" />`

[HTTPS](https://www.semrush.com/blog/what-is-https/) is generally best, so check out our guide to learn more about [redirecting from HTTP to HTTPS](https://www.semrush.com/blog/redirect-http-to-https/).

### Specify Whether to Use Trailing Slash URLs

Ensure consistent use of trailing slashes (i.e., “/” at the end of URLs) on your pages and reference your canonical URL correctly by including the trailing slash if needed.

Otherwise, Google could treat the below URLs as separate pages:

- **Trailing slash**: https://example.com/
- **Non-trailing slash**: https://example.com

### Specify Non-WWW or WWW URLs

Search engines treat www and non-www domains as separate, so your canonical tags should always reference one.

If you don’t consistently stick with non-WWW or WWW, these URLs can be seen as duplicates:

- **WWW URL**: https://www.example.com/
- **Non-WWW URL**: https://example.com/

### Use Absolute URLs

Canonical tags should always include the full URL, including protocol and domain, to eliminate ambiguity.

Correct (absolute URL):

`html<link rel="canonical" href="https://example.com/blog/" />`

Incorrect (relative URL):

`html<link rel="canonical" href="/blog/" />`

## Common Mistakes to Avoid When Implementing Canonical Tags

The most common canonical URL tag issues include pointing to redirected pages, using canonical tags for non-duplicate pages, placing tags in the wrong places, and sending mixed signals—and these increase the odds that Google will choose a different canonical URL than the one you intended.

### Pointing Canonical Tags to Redirected Pages

A canonical tag should never point to a URL that immediately redirects because it creates conflicting signals.

If page A redirects to page B, all canonical tags should point directly to page B. Pointing to page A tells Google “this page is preferred,” while the redirect says “this page is gone.” Since those contradict one another, Google will decide on its own.

### Using Canonical Tags for Non-Duplicate Content

Canonical tags should only be used when two URLs contain the same or extremely similar content—not to consolidate authority across unrelated or loosely related pages.

If the content isn’t a true duplicate, a canonical tag sends the wrong message. Google is highly likely to ignore these canonicals.

Even similar items—like two models of headphones—should have their own self-referencing canonical tags, so each product remains eligible to rank.

### Placing Canonical Tags in the Wrong Place

Canonical tags must appear inside the <head> section of the page’s HTML.

If the canonical tag is added anywhere other than the <head> section, search engines may not recognize it.

To verify placement, go to any page's URL, right-click, and select "**View page source**."

![Semrush Blog article with the browser context menu in the foreground and a light purple arrow pointing to "View page source"](https://static.semrush.com/blog/uploads/media/ca/6f/ca6f4dbe179dd63ccd19d025cfdbcdb0/cd8d39fbf1174b1a566161a88a586a16/image.png)

Then press Command + F (Mac) or Ctrl + F (PC) and search for "canonical." And ensure the tag appears between <head> and </head>.

![article HTML code with the <link rel="canonical"> tag highlighted](https://static.semrush.com/blog/uploads/media/e6/2a/e62acae05d872a22ecf292826a07673f/3436c1f12614385211ae3b27e41c0d0f/image.png)

If it appears anywhere else in the HTML, you'll need to move it to the <head> section. You may need to work with a developer to do this.

### Conflicting Canonical and Hreflang Tags

Multilingual sites often use both canonical tags and [hreflang tags](https://www.semrush.com/blog/hreflang-attribute-101/) (HTML that specifies a page’s language and sometimes its location), which can be confusing to search engines.

- **Canonical tags** tell search engines which page version is preferred
- **Hreflang tags** tell search engines which language a page uses to ensure the right version is shown to users in different countries

![diagram showing an hreflang tag with language value (en-us) in red, country value (us) in green, and URL in purple](https://static.semrush.com/blog/uploads/media/5b/f4/5bf4f1a7d658cc1b1d34b6cad3dadaa5/04b221ee25d9aae52af37619e9f5930a/image.png)

Suppose you have a page about the same topics in three languages:

- **English**: https://example.com/topic
- **Spanish**: https://example.com/es/tema
- **French**: https://example.com/fr/sujet

A common mistake is listing “https://example.com/topic” as the canonical URL on each page. That sends conflicting messages to Google and could result in the wrong language version being shown to users in a given country.

To implement both tags correctly, each page should declare itself as the main version in its language and list all available language versions, including itself.

On the English page, use:

`<link rel="canonical" href="https://example.com/topic" />
<link rel="alternate" hreflang="en" href="https://example.com/topic" />
<link rel="alternate" hreflang="es" href="https://example.com/es/tema" />
<link rel="alternate" hreflang="fr" href="https://example.com/fr/sujet" />`

On the Spanish page, use:

`<link rel="canonical" href="https://example.com/es/tema" />
<link rel="alternate" hreflang="en" href="https://example.com/topic" />
<link rel="alternate" hreflang="es" href="https://example.com/es/tema" />
<link rel="alternate" hreflang="fr" href="https://example.com/fr/sujet" />`

On the French page, use:

`<link rel="canonical" href="https://example.com/fr/sujet" />
<link rel="alternate" hreflang="en" href="https://example.com/topic" />
<link rel="alternate" hreflang="es" href="https://example.com/es/tema" />
<link rel="alternate" hreflang="fr" href="https://example.com/fr/sujet" />`

## How to Audit Canonical Tags on Your Site

To audit your canonical tags, you can use Google Search Console (GSC) and Semrush [SEO Audit](https://www.semrush.com/siteaudit/) tool.

### How to Check Canonical URLs with Google Search Console

[Google Search Console](https://search.google.com/search-console)’s URL Inspection tool shows you whether Google chose the same canonical URL you declared.

Here’s how to check any page’s specified canonical:

1. Open Google Search Console
2. Enter the URL you want to inspect into the search bar
3. Open the "**Page indexing**" section
4. Look for "Google-selected canonical"

![Google Search Console showing “URL Inspection” report with the “Google-selected canonical" in the “Page indexing” section](https://static.semrush.com/blog/uploads/media/8d/69/8d6911a545acc8f8dd9eb37553500979/8d368a379fcded1a67ee1967678ff336/image.png)

Compare the "Google-selected canonical" to the "User-declared canonical" to make sure they match. If the results differ, Google chose a different canonical.

If Google selects a different canonical than the one you prefer, review all signals—canonical tags, redirects, etc.—to ensure they consistently point to the same URL.

### How to Check Canonical Tags with Site Audit

To identify canonical problems across your entire site, including [duplicate content issues](https://www.semrush.com/blog/duplicate-title-tags/), use the Semrush Site Audit tool

Follow the prompts to configure your crawl, run the audit, go to the "**Issues**" tab, and search "canonical" to show relevant findings

![Site Audit tool "Issues" tab highlighting canonical issues found on a website](https://static.semrush.com/blog/uploads/media/0c/65/0c65fa2ee3bb8a234070747916aee578/8b362a432312aecf44e4b9a6dcc4f6f5/image.png)

Look for issues like:

- # pages have duplicate content issues
- # pages have multiple canonical URLs
- # pages with a broken canonical link
- # AMP pages have no canonical tag

![results page displaying 17,764 pages with duplicate content issues for specific URLs](https://static.semrush.com/blog/uploads/media/35/04/3504fcff9be6a6693b3339694a89849c/d21a5b4366391832ec53e7e4cfdb3a1f/image.png)

After fixing canonical issues, rerun Site Audit using the gear icon in the upper right. And confirm that the canonical-related errors no longer appear in the “**Issues**” tab

![highlighted gear icon in the upper-right corner, showing a dropdown menu with an option to rerun the campaign](https://static.semrush.com/blog/uploads/media/04/7a/047a3334b1ef6405a954bf74d5ecd98a/e8b9072ecc19c9dfde8a58bc48969c4e/image.png)

## Keeping Your Canonical Signals Aligned

Consistent canonicalization signals ensure authority is consolidated to the right URLs and make indexing more predictable.

And regular audits help you catch canonical issues early, so you can intervene. Get started with our [free SEO Checker](https://www.semrush.com/siteaudit/).

## FAQs About Canonical URLs

### What Is an Example of a Canonical URL?

A common example is when both of the following URLs load the same content but one is specified as the main version:

- example.com/product?id=123
- example.com/products/blue-widget

To signal that example.com/products/blue-widget is the preferred version, you would add a this canonical tag to both pages:

`<link rel="canonical" href="https://example.com/products/blue-widget" />`

### How Do I Make a URL Canonical?

You typically make a URL canonical by adding a rel="canonical" tag in the page’s <head> section pointing to the preferred version.

Most CMS platforms—including WordPress, Shopify, and Wix—make it easy to specify canonical URLs without editing code directly.

### How Do I Know If My URL Is Canonical?

To know if your URL is canonical, use Google Search Console's [URL Inspection tool](https://support.google.com/webmasters/answer/9012289?hl=en). If the “Google-selected canonical” matches your declared canonical URL, Google accepted your preference.

### Do Canonical Tags Improve Rankings?

Canonical tags don’t directly improve rankings, but they work with other canonical signals to consolidate link equity that increases the odds of your preferred page ranking.
