---
title: "How to Submit a Sitemap to Google (in 3 Simple Steps)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "submit-sitemap-to-google"
url: "https://www.semrush.com/blog/submit-sitemap-to-google/"
canonical: "https://www.semrush.com/blog/submit-sitemap-to-google/"
author: "Tushar Pol, Carlos Silva, Christine Skopec"
published: "2021-06-16T21:05:00+00:00"
updated: "2026-01-22T11:06:00+00:00"
categories:
  - "General SEO"
freshness_reasons: []
schema_genre: "General SEO"
fetched_at: "2026-06-12T19:59:48+00:00"
status_code: 200
html_hash: "9d42a8d6907b7adea5223dc1a0e619a2afa5e885ea2ea7c3fb5f747bda6c537a"
clean_word_count: 1857
clean_char_count: 12073
---
# How to Submit a Sitemap to Google (in 3 Simple Steps)

An XML sitemap is a file that lists a site’s webpages for search engines like Google to discover and add to their databases. It helps ensure your pages can appear in search results—traditional organic listings and AI-powered search experiences like Google’s [AI Overviews](https://www.semrush.com/blog/ai-overviews/) and [AI Mode](https://www.semrush.com/blog/google-ai-mode/).

A sitemap’s URL is typically “domain.com/sitemap.xml” or “domain.com/sitemap\_index.xml.”

You can find a domain’s XML sitemap URL by Googling “sitemap site:domain.com filetype:xml.” Like this:

![Google search results for sitemap xml filetype on Semrush domain name](https://static.semrush.com/blog/uploads/media/15/a9/15a92c81f17aea4b1aabe16b10153e6d/a5452ee5a59a3d37933bcdbd8b25edf5/image.png)

If your site doesn’t have a sitemap, create one with a [sitemap generator tool](https://www.semrush.com/free-tools/sitemap-generator/).

Google can find your XML sitemap on its own, but submitting the sitemap to Google ensures it’s found. From there, Google crawls your sitemap and (hopefully) makes your pages show up for users sooner.

Let’s walk through the process of submitting a sitemap to Google.

## How to Submit a Sitemap to Google

To submit an XML sitemap to Google, follow the steps in our guide to [Google Search Console](https://www.semrush.com/blog/google-search-console/) to connect your site, and then continue with the steps below.

### Step 1: Navigate to Your Domain in Google Search Console

Log in to your Google Search Console account and select your site from the drop-down in the top left corner if you have more than one.

![Google Search Console dashboard with arrow pointing to domain property selection menu.](https://static.semrush.com/blog/uploads/media/d0/7d/d07dfb3ec02d0c368b24b9791c86b900/73aecc94eedd197ee6f1ab59724d4d6b/image.png)

### Step 2: Go to the ‘Sitemaps’ Report

Go to the “**Sitemaps**” report in Google Search Console’s “Indexing” section in the left sidebar.

![Google Search Console dashboard with arrow pointing to Sitemaps menu option.](https://static.semrush.com/blog/uploads/media/68/e2/68e2b0d50e28677c770b43404a563852/7b17166ef3e37b5f42b01b45861b52af/image.png)

### Step 3: Add Your Sitemap

To finish submitting your XML sitemap in Google Search Console, paste your sitemap’s URL into the “Add a new sitemap” section and click “**Submit**.”

![Add a new sitemap form with sitemap URL entered and arrow pointing to Submit button.](https://static.semrush.com/blog/uploads/media/4a/65/4a654bd96def6fa2c455a56fcd890638/0b1ae5a188e9cd2ac38241630ffc01b7/image.png)

Google crawls submitted sitemaps as soon as it can. Check the “Sitemaps” report again within a few hours or days to see if Google processed your sitemap successfully, which is indicated with the “Success” status.

![Submitted sitemaps table with Status column highlighted showing success message.](https://static.semrush.com/blog/uploads/media/98/f0/98f05e5e21b5285f4df62fd454de591b/7807b0599c68c79b647c5e11a53924ce/image.png)

## How to Remove and Resubmit Sitemaps

If your [site architecture](https://www.semrush.com/blog/website-structure/) has changed or your sitemap has errors, remove and resubmit your sitemap using these steps:

1. Log in to your Google Search Console account
2. If you own multiple sites, use the drop-down menu in the top left corner to select the correct site
3. Click “**Sitemaps**” under the left sidebar’s “Indexing” section
4. In the “Submitted sitemaps” section, click the line with the sitemap you want to remove
5. Click the three-dot menu icon in the top right corner. Then, click “**Remove sitemap**.”
6. Confirm the removal by clicking the “**Remove**” button in the pop-up window that appears
7. Wait for Google to process your request

Alternatively, delete the sitemap file from your site. Google will [eventually stop](https://youtu.be/4DwVO7ZP7yY?t=33) checking it if it’s unavailable for a certain period.

If your new sitemap has the same URL as the original sitemap, don’t delete your original sitemap. Simply resubmit it using the steps above. Google will reprocess it.

If you don’t have a sitemap (or don’t resubmit it), crawlers can still find your site’s pages. But it could take longer. And some pages could be overlooked.

## Sitemap Best Practices

Follow these best practices to help Google process your sitemaps efficiently:

### Include Only the Essential Information

Your sitemap should contain:

- **The URLs you want to have indexed**: Don’t include pages that you don’t want indexed
- **The “lastmod” value**: This value says when a page was last meaningfully updated. Search engines refer to it to prioritize which pages to crawl.
- **The “**[**hreflang**](https://www.semrush.com/blog/hreflang-attribute-101/)**” values for your pages’ location-specific variants**: If your pages have localized versions, [indicate them in the sitemap](https://developers.google.com/search/docs/specialty/international/localized-versions#sitemap) to help search engines crawl each version

**Don’t** include the following in your sitemap:

- **The “changefreq” and “priority” values**: Google ignores these values
- [**Non-canonical URLs**](https://www.semrush.com/blog/canonical-url-guide/): Skip these URLs because they’re alternative URLs to your preferred pages
- **3xx or 4xx URLs**: You don’t want Google to index or rank these URLs, as they redirect users to different pages (3xx [status code](https://www.semrush.com/blog/http-status-codes/)) or return client-side errors (4xx status code)

### Adhere to the Size Limit

Keep your sitemap within [Google’s size limit](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap#general-guidelines)—meaning 50MB (uncompressed) or 50,000 URLs.

If your sitemap exceeds Google’s size limit, split it into multiple sitemaps.

### Create Multiple Sitemaps If Needed

Create multiple sitemaps if your sitemap exceeds Google’s size limit or to have separate sitemaps for different content types (e.g., a sitemap for pages, a sitemap for posts, and a sitemap for videos).

If you have multiple sitemaps, you’ll need to create a sitemap index file that lists all your sitemaps. Like a table of contents.

Here’s Semrush’s sitemap index, for instance:

![Semrush XML sitemap index listing various URLs.](https://static.semrush.com/blog/uploads/media/24/0b/240b5b048008b5ed3a99f54de51c4ed5/0b671ab673d3f855958f4f08259a4d38/image.png)

Submit the sitemap index URL to Google just like you would a regular sitemap.

## Common Sitemap Issues and How to Fix Them

Common sitemap issues include:

- **Formatting errors**: There are errors in your sitemap file’s format, like missing XML tags
- **Incorrect URLs**: Your sitemap contains URLs that aren’t supposed to be in a sitemap (e.g., redirects and non-canonical URLs)
- **Too large**: Your sitemap has exceeded Google’s size limit

We analyzed 50,000 domains for our [technical SEO checklist](https://www.semrush.com/blog/technical-seo-checklist/) and found that about 31% of those domains had at least one issue with their sitemaps. In other words, sitemap-related issues are quite common. (We captured more data points in our analysis than what made it into the final checklist article.)

Find and fix your sitemap issues by navigating to the “**Sitemaps**” report in Google Search Console.

If your sitemap has a “Couldn’t fetch” or “Sitemap has # errors” status, [Google](https://support.google.com/webmasters/answer/7451001) provides suggested solutions.

Or, run a free [SEO check](https://www.semrush.com/siteaudit/) on your sitemap and load speeds. To detect sitemap errors, broken links, and other [technical SEO](https://www.semrush.com/blog/technical-seo/) issues across your full site, use Semrush Site Audit. Just, [configure](https://www.semrush.com/kb/539-configuring-site-audit) and run your audit.

Once Site Audit has finished, click the “**Issues**” tab and search for “sitemap.” A list of possible issues with your sitemap will appear.

![Semrush Site Audit Issues tab search results for 'sitemap' showing 2 incorrect pages error.](https://static.semrush.com/blog/uploads/media/3d/74/3d74fdcba02d2bfef7a4b4f0ad6af046/81fb7e1a8f3c751952dc1030219e81c6/image.png)

If you have a sitemap issue, click the link with the number of affected pages.

![Close-up of the sitemap.xml error link highlighting two incorrect pages in Semrush Site Audit.](https://static.semrush.com/blog/uploads/media/1b/54/1b54bc839e2bdd2f999f4899ebc7dd0c/40fcec4fd03c76c86e276acb77170502/image.png)

Clicking the link next to the corresponding sitemap issue will open a new report with a full list of affected pages.

![Detailed sitemap error report listing redirected URLs found in sitemap.xml in Semrush.](https://static.semrush.com/blog/uploads/media/a3/9b/a39bf7e8d88fcaca059678ee197b76a4/61ae3a9378238a4c650c5a2570f0c609/image.png)

Then, click the “**Why and how to fix it**” link to get a detailed description of the sitemap issue and recommendations for fixing it.

After you’ve fixed all the sitemap-related issues, run Site Audit again to ensure they’re resolved.

## Frequently Asked Questions

Find answers to some of the most common questions about sitemaps below.

### Does Submitting a Sitemap Guarantee Pages Will Be Indexed?

No, submitting a sitemap doesn't guarantee that Google will index your pages. A sitemap helps search engines discover your content, but Google may choose not to index pages that are [duplicates](https://www.semrush.com/blog/duplicate-content/), low-quality, or marked with [noindex tags](https://www.semrush.com/blog/noindex/).

If pages aren't being indexed (which you can check in Google Search Console) despite appearing in your sitemap, focus on improving content quality, fixing technical errors, and ensuring your pages provide unique value to users.

### How Often Should You Update Your Sitemap?

You should update your sitemap whenever you add, remove, or significantly modify pages on your site.

Most content management systems (CMS) do this automatically when you publish new content. If yours doesn't, you'll need to manually update your XML file and resubmit it to Google Search Console.

### Do You Need a Sitemap if Your Site is Small?

No, you don’t necessarily need to have a sitemap if your website is small, but it’s still recommended because sitemaps become more valuable as your site grows, are helpful if your pages aren't well-connected through [internal links](https://www.semrush.com/blog/internal-links/), and are useful if you frequently add new content.

### What Does the ‘Couldn’t Fetch Sitemap’ Error Mean?

The "Couldn't fetch sitemap" error in Google Search Console means Google was unable to access your sitemap file, typically due to server issues (like downtime or slow response times), incorrect file paths, or access restrictions (such as blocked access in [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) or a password-protected path).

### Do You Need to Submit a Sitemap to Other Search Engines Besides Google?

You don’t necessarily need to submit your sitemap to other search engines given how widely used Google is, but you can optionally submit your sitemap to Bing (via [Bing Webmaster Tools](https://www.bing.com/webmasters/about)).

Bing and other smaller search engines will eventually discover your site through crawling, so you can skip submitting your sitemap to them.

### Can a Bad Sitemap Hurt SEO?

Yes, a bad sitemap that includes [broken URLs](https://www.semrush.com/blog/broken-link/), redirected pages, or pages marked with noindex tags can negatively affect your SEO because it tells search engines to crawl content that shouldn't be prioritized or can't be indexed.

Regularly review your website with Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool to ensure your sitemap is free of errors. The tool lets you set up weekly or monthly audits that automatically scan your sitemap and alert you when issues are detected.
