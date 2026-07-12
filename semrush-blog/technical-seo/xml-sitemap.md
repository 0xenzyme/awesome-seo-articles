---
title: "XML Sitemap: What It Is And How To Generate One"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "xml-sitemap"
url: "https://www.semrush.com/blog/xml-sitemap/"
canonical: "https://www.semrush.com/blog/xml-sitemap/"
author: "Alex Lindley, Carlos Silva"
published: "2015-08-14T15:16:00+00:00"
updated: "2026-01-05T10:53:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T21:25:26+00:00"
status_code: 200
html_hash: "cf9b384d72d9919d58c0b0e913f412b1d44996b0c9313aa1898a166d4d35cb06"
clean_word_count: 3441
clean_char_count: 23357
---
# XML Sitemap: What It Is And How To Generate One

An XML sitemap plays a foundational role in technical SEO by supporting how search engines discover and process your website’s URLs.

A sitemap.xml file is relatively simple, but how you generate, structure, and maintain it can directly affect crawl efficiency and indexing coverage.

This guide explains how XML sitemaps work, when they matter most, and how to create and manage them correctly. By the end, you’ll know how to generate a reliable website sitemap XML file and keep it aligned with SEO best practices as your site evolves.

## What Is an XML Sitemap?

An XML sitemap is a file (usually named “sitemap.xml”) that lists the [URLs](https://www.semrush.com/blog/what-is-a-url/) on your website that you want search engines to discover, crawl, and index.

In addition to URLs, an XML sitemap can include metadata that helps search engines understand page freshness and content updates, like:

- When a page on your site was last meaningfully updated
- Image or video data via sitemap extensions

Search engines use XML sitemaps to improve crawling and indexing efficiency, especially when your site has a lot of pages or complex navigation. A well-maintained XML sitemap helps search engines:

- Discover URLs on your site that may not be easily found through internal links
- Prioritize crawling updated or important pages
- Reduce the risk of important pages being missed during indexing

AnXML sitemap is a crawler-focused file. It’s different from an [HTML sitemap](https://www.semrush.com/blog/html-sitemap/), which is designed for visitors and serves as a navigational page.

## What Does an XML Sitemap Look Like?

An XML sitemap is a text file written in Extensible Markup Language (XML), a structured format search engines can easily read and process. The sitemap lists URLs on your website inside a <urlset> element, with one <url> entry per page you want search engines to crawl.

Here’s a basic [sitemap example](https://www.semrush.com/blog/sitemap-examples/) (this includes optional tags):

`<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.example.com/</loc>
    <lastmod>2024-03-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://www.example.com/about/</loc>
    <lastmod>2024-03-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.example.com/products/</loc>
    <lastmod>2024-03-21</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>`

The core [sitemap protocol](https://www.sitemaps.org/protocol.html) supports these tags:

- <urlset>: Wraps the entire sitemap file
- <url>: Wraps one URL entry
- <loc>: The URL you want indexed (required)
- <lastmod>: The last meaningful content update (optional)
- <changefreq>: How often content tends to change (optional)
- <priority>: Relative importance from 0.0 to 1.0 (optional)

You can also use [sitemap extensions](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) or create separate sitemaps for specific content types, including:

- Image sitemaps
- Video sitemaps
- News sitemaps

### What Does a Sitemap Index Look Like?

A sitemap index is a file that lists multiple sitemap files. You typically use a sitemap index when your site needs more than one sitemap (for example, because of sitemap limits or because you segment sitemaps by content type).

Here’s what a sitemap index looks like:

`<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://www.example.com/sitemap-pages.xml</loc>
    <lastmod>2025-12-11</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://www.example.com/sitemap-products.xml</loc>
    <lastmod>2025-12-11</lastmod>
  </sitemap>
</sitemapindex>`

![Sitemap Index of "apple.com" listing multiple sitemap files.](https://static.semrush.com/blog/uploads/media/af/1f/af1f410af57981d4f501e705ead17f5b/cf5b1cde3d80c05f59f09cb1b3763157/image.jpeg)

## Do You Need an XML Sitemap?

Yes, you need an XML sitemap if you want search engines to reliably discover and index the important pages on your website.

Providing an XML sitemap gives search engines a clear, direct view of which URLs you consider important, improving crawl efficiency and indexing coverage.

An XML sitemap is technically optional, but without one, search engines primarily rely on internal and external links to discover your URLs. This can delay or reduce crawl coverage, especially on sites with complex navigation or limited link depth.

An XML sitemap is particularly useful if your site has:

- A lot of pages (for example, hundreds to thousands of URLs, or any site that regularly adds new pages)
- New or frequently updated content
- Pages that are not well-connected through internal links
- Rich media or specialized content you want indexed

In practice, XML sitemaps become increasingly important as your site grows beyond a few dozen pages, especially if new URLs are added regularly or not all pages are easily reachable through internal links.

## How to Create an XML Sitemap Automatically

You can create an XML sitemap automatically by using your website platform’s built-in sitemap features or by using an XML sitemap generator.

Automatic sitemap generation is the easiest way to generate sitemap XML files. Automatic generation is the recommended approach for most sites because it keeps your sitemap up to date as URLs change.

### Use Your Platform's Built-In Features

Many website platforms generate an XML sitemap automatically, including ecommerce platforms like [Shopify](https://www.semrush.com/blog/shopify-seo/), so your first step should be to check whether one already exists.

To check, visit “https://yourdomain.com/sitemap.xml”

If you see a structured list of URLs or sitemap files, your platform has already generated a sitemap. Review which URLs are included. Then move on to validation and submission.

If no sitemap appears, here are a few platform-specific options:

#### WordPress

WordPress generates an XML sitemap by default (since WordPress 5.5) at “https://yourdomain.com/wp-sitemap.xml”—but customization options are limited.

The core sitemap includes posts, pages, categories, tags, and author archives.

If you need more control, SEO plugins like [Yoast SEO](https://www.semrush.com/blog/yoast-seo/) and Rank Math can replace or extend the default sitemap by allowing you to:

- Include or exclude specific content types
- Remove low-value archives or taxonomies
- Control sitemap structure for large sites

You can also [customize your WordPress sitemap](https://www.semrush.com/blog/wordpress-sitemap/) with advanced settings through these plugins.

When using an SEO plugin, your sitemap is often a sitemap index at “https://yourdomain.com/sitemap\_index.xml” (e.g., Yoast SEO and Rank Math use sitemap\_index.xml).

The sitemap updates automatically when you publish or update content.

#### Drupal

Drupal requires a module to generate an XML sitemap.

To create one:

1. Install the [XML Sitemap module](https://www.drupal.org/project/xmlsitemap)
2. Configure which content types and taxonomies to include
3. Access your sitemap at “https://yourdomain.com/sitemap.xml”

Once configured, the sitemap updates automatically as content changes.

#### Joomla

Joomla requires an extension to generate an XML sitemap.

To create one:

1. Install an extension like [OSMap](https://extensions.joomla.org/extension/osmap/)
2. Select which content types and menu items to include
3. Access your sitemap at “https://yourdomain.com/sitemap.xml”

The sitemap updates automatically when you publish new content, depending on extension settings.

### Use a Sitemap Generator Tool

You can use a [sitemap generator tool](https://www.semrush.com/blog/sitemap-generator-tools/) to make sitemap XML files. These tools are most useful when your platform doesn’t generate a sitemap automatically or when you need more control over which URLs are included.

Sitemap generator tools typically work by [crawling your site](https://www.semrush.com/blog/website-crawler/), identifying indexable URLs, and exporting an XML file you can upload or submit directly.

|  |  |  |
| --- | --- | --- |
| **Tool** | **Best For** | **Available Plans** |
| [**Semrush Sitemap Generator**](https://www.semrush.com/free-tools/sitemap-generator/) | Quick sitemap creation for any site | Free |
| [**Semrush Site Audit**](https://www.semrush.com/siteaudit/) | Sitemap validation and ongoing monitoring | Paid (trial available) |
| [**Yoast SEO**](https://yoast.com/wordpress/plugins/seo-free/) | Automated sitemap generation for WordPress | Free & Premium |
| [**XML Sitemap Generator for Google**](https://wordpress.org/plugins/google-sitemap-generator/) | WordPress sites needing more control | Free |
| [**Screaming Frog**](https://www.screamingfrog.co.uk/seo-spider/) | Technical users and large sites | Free (limited), paid plans available |
| [**XML-Sitemaps.com**](https://www.xml-sitemaps.com/) | Small to medium sites | Free (limited), paid plans available |
| [**SEOptimer**](https://www.seoptimer.com/sitemap-generator) | Configurable crawls with basic controls | Free (limited), paid plans available |

When choosing a sitemap generator, focus on how well it fits your site’s size and workflow:

- **Site size**: Many free tools cap crawls at 500 URLs
- **Update behavior:** Some tools generate one-time files, while others update automatically
- **URL control:** The ability to exclude noindex pages, parameters, or duplicates
- **Validation**: Built-in checks for formatting errors and non-200 URLs
- **Specialized sitemaps**: Support for image, video, or news sitemaps
- **Ease of use**: Browser-based tools are simpler, desktop crawlers offer more control

For most sites, a generator tool is fastest when you need a one-time sitemap or a crawl-based comparison. For ongoing monitoring, a tool like Semrush [Site Audit](https://www.semrush.com/siteaudit/) is better suited.

## How to Create an XML Sitemap Manually

You can create an XML sitemap manually by writing and uploading a sitemap.xml file, but this approach is only practical if you need full control over how you make sitemap XML entries.

Manual sitemap creation makes sense if your site has a limited number of stable URLs (e.g., a few dozen pages) or if you need full control over every entry. For most sites, this method is slower and more error-prone than automated options.

To hand-code an XML sitemap:

1. Create a new text file and save it as “sitemap.xml”
2. Add the required XML structure and sitemap namespace following the [sitemap protocol](https://www.sitemaps.org/protocol.html)
3. List each [canonical URL](https://www.semrush.com/blog/canonical-url-guide/) using <url> and <loc> tags
4. Add <lastmod> (last modified) only if you can keep it accurate
5. Validate your XML syntax before uploading
6. Upload the file to your website's root directory so it’s accessible at “https://yourdomain.com/sitemap.xml”

Optional tags like <changefreq> and <priority> are part of the sitemap protocol, but search engines like Google ignore them, so maintaining those values usually provides little benefit.

For most websites, using your platform's built-in sitemap features or a sitemap generator tool is faster, more reliable, and easier to maintain as your site changes.

## How to Validate Your Sitemap

A valid XML sitemap must load successfully, follow the sitemap protocol, and include only indexable, canonical URLs.

Validate your sitemap before submitting it to Google to avoid crawl errors and indexing issues.

Here are the most common XML sitemap validation issues, along with their typical causes and fixes:

- **Sitemap not found**: The sitemap file isn’t accessible at the expected URL
  - **Fix**: Make sure sitemap.xml exists in your site’s root directory (for example, “https://yourdomain.com/sitemap.xml”) and that the file is publicly accessible
- **XML formatting errors**: The sitemap contains invalid XML, such as unclosed tags or unescaped characters
  - **Fix**: Validate the XML syntax, close all tags correctly, and escape special characters (for example, use & instead of &)
- **File too large**: The sitemap exceeds protocol limits (50 MB uncompressed or 50,000 URLs)
  - **Fix**: Split the sitemap into multiple files and reference them using a sitemap index
- **Non-200 URLs in sitemap**: The sitemap includes URLs that return [redirects or errors](https://www.semrush.com/blog/http-status-codes/) (such as [301](https://www.semrush.com/blog/301-redirects/) or [404](https://www.semrush.com/blog/broken-link/))
  - **Fix**: Remove non-200 URLs and regenerate the sitemap so it includes only live, indexable pages
- **Non-canonical URLs included**: The sitemap lists duplicate URLs, parameterized URLs, or alternate versions of pages
  - **Fix**: Include only [canonical URLs](https://www.semrush.com/blog/canonical-url-guide/) and exclude duplicates or parameter variations
- **HTTP URLs on HTTPS site**: The sitemap lists HTTP URLs even though your site uses HTTPS
  - **Fix**: Regenerate the sitemap to include only [HTTPS URLs](https://www.semrush.com/blog/http-vs-https/)
- **Sitemap not referenced in robots.txt**: Your sitemap isn't listed in your [robots.txt file](https://www.semrush.com/blog/beginners-guide-robots-txt/)
  - **Fix**: Adding a line like “Sitemap: https://yourdomain.com/sitemap.xml” to your robots.txt file can help crawlers find it
- **Orphaned pages in sitemap**: The sitemap includes pages that have no [internal links](https://www.semrush.com/blog/internal-links/) pointing to them
  - **Fix**: Add internal links to important pages or remove [orphaned URLs](https://www.semrush.com/blog/orphan-pages/) from the sitemap

You can use Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool to identify sitemap-related issues automatically.

To check sitemap issues, run a Site Audit for your site and go to the "**Issues**" tab when the report is ready.

Search for “sitemap” to view sitemap-related warnings and errors.

![Site Audit Issues with "sitemap" entered showing a list of sitemap-related errors and warnings.](https://static.semrush.com/blog/uploads/media/02/a4/02a48322ce44f0f25500b196466d5dcf/3a3dcd8c1c363d39c7212e48e7549ea0/image.jpeg)

Click "**Why and how to fix it**" on each error for specific steps.

Click “**Rerun campaign**” to rerun the audit after fixing issues to confirm they’re working correctly.

![Site Audit Issues with the "Rerun campaign" button clicked.](https://static.semrush.com/blog/uploads/media/68/8f/688f02a0c8d2c0919094bbf48d7fdf9c/0e8517ca52052ccfa51eb303d522b1c9/image.jpeg)

This approach helps you validate your sitemap and catch related [technical SEO](https://www.semrush.com/blog/technical-seo/) issues that affect crawlability and indexing.

## How to Submit Your XML Sitemap to Google

[Submitting your XML sitemap to Google](https://www.semrush.com/blog/submit-sitemap-to-google/) lets you monitor sitemap status, catch errors, and see how Google processes your URLs in Google Search Console (GSC).

To submit your XML sitemap, open GSC and select your property.

Go to “Sitemaps” in the left-hand navigation. Enter your sitemap’s URL into the “Add a new sitemap” section and click “**Submit**.”

![Add a new sitemap section on Google Search Console with "Submit" clicked.](https://static.semrush.com/blog/uploads/media/37/9e/379e6ba77733fe34d282030467464518/326f5d9e562951eed91e75f94224ce3f/image.jpeg)

You should then see your sitemap in the “Submitted sitemaps” section.

When Google has crawled your sitemap, you’ll see a “Success” notice in the “Status” column.

![Submitted sitemaps on Google Search Console with "Success" in the "Status" column highlighted.](https://static.semrush.com/blog/uploads/media/d6/a7/d6a7c04f44ff43057b3417e0cdfe1ac4/295d4914e2c066f34fa107c6451a8932/image.jpeg)

Google automatically recrawls submitted sitemaps over time to check for changes. If you make significant updates to your site structure or sitemap contents, you can resubmit the same sitemap URL to ask Google to recrawl it sooner.

Submitting a sitemap doesn’t guarantee indexing. But it helps Google discover your URLs and report issues that could affect crawling and indexing.

## Advanced XML Sitemap Types

Advanced XML sitemap types help search engines better understand large sites, media-heavy pages, or international content by providing additional structure beyond a standard page sitemap.

You only need these sitemap types in specific situations. For many sites, a single-page sitemap is enough.

|  |  |  |  |
| --- | --- | --- | --- |
| **Sitemap Type** | **What It Is** | **When to Use It** | **Common Use Cases** |
| **Sitemap Index** | A file that lists multiple sitemap files | When your site exceeds sitemap limits or you segment sitemaps by content type | Large ecommerce sites, enterprise websites, multi-section sites |
| **Image Sitemap** | A sitemap that includes image metadata alongside page URLs | When images play a key role in search discovery | Ecommerce product images, photography portfolios, image galleries |
| **Video Sitemap** | A sitemap that includes video metadata like thumbnails, titles, and descriptions | When you want Google to discover and index video content | Video tutorials, product demos, courses, media sites |
| **News Sitemap** | A sitemap designed for timely news content | When you publish eligible content for Google News | News publishers, media outlets, press sites |
| **Multilingual Sitemap (Hreflang)** | A sitemap that defines language and regional page variants | When managing multilingual or multi-regional sites at scale | International businesses, global ecommerce, multilingual blogs |

Use advanced sitemap types only when they solve a specific indexing or scale problem. For example:

- Use a **sitemap index** once your site reaches sitemap size limits or needs logical segmentation
- Use **image or video sitemaps** when media visibility matters beyond standard page indexing
- Use **hreflang sitemaps** when managing many language or region variants becomes difficult to maintain in page-level markup

If your site is small or primarily text-based, these advanced formats are optional and often unnecessary.

## XML Sitemap Best Practices

XML sitemap best practices ensure your sitemap includes only indexable, canonical URLs and follows the technical rules search engines expect.

Most platforms and tools generate compliant sitemaps by default, but reviewing these guidelines helps you avoid common crawl and indexing issues.

### Include Only the URLs You Want Indexed

Your XML sitemap should reference only URLs that you want search engines to crawl and index.

Include URLs that:

- **Are intended for indexing**: Exclude staging URLs, internal search results, checkout or confirmation pages, and other non-indexable URLs
- **Return a 200 status code**: Don’t include URLs that return redirects (like [301 redirects](https://www.semrush.com/blog/301-redirects/)), client errors (like [404 errors](https://www.semrush.com/blog/what-does-error-404-not-found-mean/)), or other [HTTP status codes](https://www.semrush.com/blog/http-status-codes/) that indicate errors
- **Use fully qualified, absolute URLs**: Each <loc> value should include the full URL, including the protocol (for example, “https://www.semrush.com/blog/”)
- **Are** [**canonical URLs**](https://www.semrush.com/blog/canonical-url-guide/): Include only the preferred version of each page. Exclude duplicate URLs, parameterized variants, and alternate versions.

### Follow Technical Sitemap Requirements

Your sitemap file should also meet these technical requirements:

- **Use UTF-8 encoding**: This system ensures search engines can understand all the characters you’re using. Special characters must be properly escaped (for example, use & instead of &).
- **Stay within sitemap limits**: Each sitemap file must be under 50 MB (uncompressed) and contain no more than 50,000 URLs. Use multiple sitemaps and a sitemap index if needed.
- **Specify the correct XML namespace**: A namespace is like a label that tells the search engine what rules your sitemap follows. Most sitemaps use “http://www.sitemaps.org/schemas/sitemap/0.9” to follow the standard sitemap protocol.
- **Include language and region variants where applicable**: For multilingual or multi-regional sites, reference alternate versions using [hreflang](https://www.semrush.com/blog/what-is-hreflang-and-how-does-it-work/) (either in-page or via sitemap). Learn more in [this resource from Google](https://developers.google.com/search/docs/specialty/international/localized-versions).

### Reference Your Sitemap in Robots.txt

Linking to your sitemap in your [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) file helps search engines discover it more easily. This is a website file that tells search engines which pages they should and shouldn’t crawl.

For example: “Sitemap: https://yourdomain.com/sitemap.xml”

## Ensure Your XML Sitemap Is Up to Code

Use Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) to identify XML sitemap issues. Keeping your sitemap XML accurate over time helps search engines crawl and index new URLs more efficiently.

Site Audit checks for sitemap errors like invalid URLs, non-200 status codes, incorrect formats, and mismatches between your sitemap and actual site structure. It also surfaces related technical issues—like [broken links](https://www.semrush.com/blog/broken-link/) and orphan pages—that can undermine sitemap effectiveness.

Create a free Semrush account to audit your site and keep your [website sitemap](https://www.semrush.com/blog/website-sitemap/) aligned with SEO best practices.

## FAQs About XML Sitemaps

### What Is a Sitemap XML?

A sitemap XML (often “sitemap.xml”) lists the URLs on your website that you want search engines to discover and crawl. It helps search engines understand your site structure and prioritize important pages during crawling.

### Where Is Sitemap.xml Located?

In most cases, sitemap.xml is located in your site’s root directory and accessible at “https://yourdomain.com/sitemap.xml.” Some platforms use a different default location, such as “wp-sitemap.xml” on WordPress.

### How Do I Generate a Sitemap XML?

Automatic sitemap generation is the recommended approach for most sites. You can generate a sitemap XML automatically using your website platform’s built-in sitemap features or an XML sitemap generator tool.

### Do I Need to Update Sitemap.xml Manually?

In most cases, you don’t need to update sitemap.xml manually. If your sitemap is generated by your content management system (CMS) or an XML sitemap generator, it updates automatically as URLs change. Manual updates are only necessary for hand-coded sitemaps.

### What’s the Difference Between an XML Sitemap and an HTML Sitemap?

An XML sitemap is designed for search engines and helps with crawling and indexing. An HTML sitemap is designed for users and helps with on-site navigation. XML sitemaps support SEO processes. HTML sitemaps support usability.
