---
title: "Pagination and SEO: A Complete Guide to Best Practices"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "pagination-seo"
url: "https://www.semrush.com/blog/pagination-seo/"
canonical: "https://www.semrush.com/blog/pagination-seo/"
author: "Carlos Silva, Sydney Go"
published: "2024-01-26T14:45:00+00:00"
updated: "2025-02-21T10:55:00+00:00"
categories:
  - "On-page SEO"
freshness_reasons:
  - "time_sensitive_title"
schema_genre: "On-page SEO"
fetched_at: "2026-06-12T18:28:30+00:00"
status_code: 200
html_hash: "9fa7712c3bce7cd16ee1bcfc34b8be324a363de4107275191d35cdd7f446e621"
clean_word_count: 2589
clean_char_count: 20363
---
# Pagination and SEO: A Complete Guide to Best Practices

## What Is Pagination in SEO?

In SEO, pagination is a way to split your content across multiple pages to help speed up your site and ensure users can easily click through long lists of products, blog posts, or search results.

Think of Amazon's product pages.

Instead of showing 10,000 coffee makers on a single page, pagination breaks the list into chunks—with a limited number of items per page.

Like this:

![Amazon's search results for coffee maker, shows 1-48 of over 40,000 results on page one.](https://static.semrush.com/blog/uploads/media/1e/aa/1eaa040392cb79bbbd8c7272df2d50e0/ddf4227f43e02891e57a0dd5d40229e2/AD_4nXe6AGlIucaGKzNi447U5n1B1VSDDsmYmaDEBdPdLaDCqlvB1edzx9XIw8aphPEF-qg_KC6DN2aWnDIM3h0uGfxpAjTO_SWtNeSItEK1Ja5YgUBB92quZ6bpiGXXYv4IH0UQFT-KeA.png)

Sites that benefit most from pagination include:

- Ecommerce stores with large product catalogs
- News sites with extensive article archives
- Forums with many discussion threads
- Blog category pages with many posts
- Photo galleries with lots of images

Pagination exists because loading thousands of items on a single page creates two major problems:

1. Slow [page speed](https://www.semrush.com/blog/page-speed/), which frustrates users and hurts rankings
2. Poor user experience from endless scrolling through unorganized content

When implemented correctly, pagination helps search engines understand how your pages connect. And makes it easier for users to find what they're looking for.

## Is Pagination Good for SEO?

Pagination is good for SEO when implemented correctly.

Search engines like Google [recommend pagination](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading#selecting-the-best-ux-pattern-for-your-site) as one of the ways to organize large sets of content and improve the user experience.

Here's why pagination can help your SEO:

- **Improved page speed**: Breaking up large content sets reduces page load time. A single page with 1,000 products will probably load much slower than a page with just 20 products.
- **Clear site architecture**: Pagination creates a logical structure for your content. This can help search engines understand the relationship between pages in a section.
- **Better internal linking**: Paginated pages naturally link to each other. This can help distribute link equity (the value and authority a link passes from one page to another) throughout your site and strengthen your internal linking structure.

However, pagination only benefits SEO if you follow best practices like those in [Google's pagination guidelines](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading).

## SEO Best Practices for Implementing Pagination

Here’s an overview of some of the best practices to follow if you decide to implement pagination on your site:

### 1. Self-Canonicalize Each Page

Each page in your pagination sequence should include a [canonical tag](https://www.semrush.com/blog/canonical-url-guide/) (an HTML snippet that tells search engines which is the preferred version of a webpage) pointing to itself to indicate the page is unique.

Here's how to add self-referencing canonicals:

For page one:

`<link rel="canonical" href="https://example.com/shop/" />`

For page two:

`<link rel="canonical" href="https://example.com/shop/?page=2" />`

For page three:

`<link rel="canonical" href="https://example.com/shop/?page=3" />`

And so on for each paginated page.

![A self-referencing canonical tag is added in the <head> of each paginated page.](https://static.semrush.com/blog/uploads/media/57/41/574113f0eb6b0116bfb8673b3c55752a/9359752221c9d5f849f2f8522905cbb5/AD_4nXeXGsWWm5amrqd92fMrQPM4ulnD257UP9qN0KVIhJn0SfXltYyHMYstClHIuDwwqcITiylEPtTfelGMljE2LJlArcG1yBzijPJedzYuuaUXJMCrnyhm5ZTfPMxkye2667z1-7AS5A.png)

Self-canonicalization also helps search engines better understand your site structure and prevents [duplicate content](https://www.semrush.com/blog/duplicate-content/) issues.

For a quick check on your canonical tag, use our free [SEO checker](https://www.semrush.com/siteaudit/). To scan canonical tags across your entire site, use Semrush Site Audit.

![Under Crawled Pages, advanced filters, choose with rel="canonical" is self-canonical.](https://static.semrush.com/blog/uploads/media/36/37/3637780369c0aeade44d08fe3c8ea0e4/962ec462c4c4af8cb15c75d8df1e31ea/AD_4nXdci5tRbUKUQcnxmBVsT-r_aY_jiwZapvFaU88mva0RGOkohi17FDR1SA6RAPQdjMqgZdR5QjKwICdjWijFLn71SbDhMnUcdwtJzgVgESShXs262wW_Q3t_ov-nCxc9Sr4h4d_xjQ.png)

### 2. Use Clear, Descriptive URLs

Using URLs that are clear and descriptive makes paginated pages easy for search engines and users to understand.

Your URLs should clearly indicate pagination and follow a consistent, logical pattern.

Here are the two most SEO-friendly URL structures for pagination:

Query parameters:

- **example.com/products?page=2**
- **example.com/products?page=3**

Directory structure:

- **example.com/products/page/2**
- **example.com/products/page/3**

Avoid these common URL mistakes:

- Using random strings (/products/p2x9401)
- Skipping numbers (/products/page2 followed by /products/page4)
- Mixing formats (/products?page=2 and /products/page-3)

**Choose one URL structure and stick with it across your site.**

[Google recommends](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading#use-urls-correctly) using query parameters because they're easier to track in [Google Search Console](https://search.google.com/search-console/about). But both formats work well, as long as they are implemented consistently.

### 3. Avoid URL Fragment Identifiers

URL fragment identifiers are parts of a URL that come after the # symbol. They typically look like this:

**https://example.com/category/#page1**

Search engines generally ignore fragments because they point to a specific section on a page—not a unique piece of content.

Instead, use [query parameters](https://www.semrush.com/blog/url-parameters/#what-are-url-parameters).

Query parameters are elements added to the end of a URL that come after a question mark (?). They can make it easier for search engines to crawl paginated content.

Like this:

**https://example.com/blog/?page=2**

![URL example of pagination SEO reads https://www.example.com/blog/?page=2. The key is page and the value is 2.](https://static.semrush.com/blog/uploads/media/a5/6d/a56da687646d9d5f1e1b689e0cdba7af/82bf0a808b880e2a51303d6d150bd6da/AD_4nXeCHneYNuq9tbK2cjNcTJkuY64GXWehu6uWB0B4UTA32XOeEUDnSRPYHYB5LamAuLj41IDx8eHJfGoCBxJIDLKCzogjNHgy7OiAkGB_DJUgcTMTt9G9Y6UnnjwHWT4NSOhaYAo9vA.png)

### 4. De-Optimize Paginated Pages

De-optimizing paginated pages means removing traditional SEO elements from pages two and beyond, so only your first page targets your main [keywords](https://www.semrush.com/blog/what-are-keywords/) and ranks in search results.

Think of your first page as your ranking page. All other pages exist to help users navigate your content, not compete in search results.

Focus on usability rather than rankings for pages two and beyond.

Follow these tips to de-optimize all pages but the preferred page for ranking:

- Use simple, non-optimized [title tags](https://www.semrush.com/blog/title-tag/) and [meta descriptions](https://www.semrush.com/blog/meta-description/)
- Write generic, non-descriptive [H1 tags](https://www.semrush.com/blog/h1-tag/)
- Keep keyword use minimal to avoid competing with the main page

This best practice helps make sure your paginated pages support—rather than compete with—your first page.

### 5. Avoid Noindexing Paginated Pages

A [noindex](https://www.semrush.com/blog/noindex/) tag tells search engines like Google to avoid indexing a specific webpage to prevent it from appearing in search results.

Noindex tags may hurt pagination because:

- Link value stops flowing through your pages
- Search engines may not be able to discover new content through pagination links
- Crawlers might skip important pages entirely

Instead of noindex, use:

- Self-referencing canonical tags on each page
- Clear navigation links between pages
- Proper URL structure
- De-optimized SEO elements

Search engines should be able to crawl and process all pages in your pagination sequence. Blocking access with noindex may prevent them from understanding your site's full structure and all your important content.

## Pagination Alternatives

Pagination isn’t the only way to organize large sets of content—certain alternatives might work better based on your site’s structure and your user experience goals.

There are three alternatives to pagination:

**Infinite scroll** automatically loads new content as users reach the bottom of a page, creating a seamless scrolling experience without pagination links.

It works better than pagination for:

- Social media feeds that users want to browse continuously
- News sites with frequently updated content
- Mobile-focused websites, where tapping pagination links is cumbersome

**Load more** adds a button users can click to display additional content on the same page.

It works better than pagination for:

- Large ecommerce category pages
- Search results pages, where users want control over content loading
- Sites that want to track user engagement with specific content chunks

**View all** displays the entire collection on a single page instead of splitting it across multiple pages.

It works better than pagination for:

- FAQ pages, where users need to search through all content at once
- Documentation pages that benefit from full-text search
- Printer-friendly content that needs to be viewed in its entirety

## Tools to Find and Fix Pagination Issues

The right tools make finding and fixing pagination issues easier.

Here are several of the best options:

### Site Audit

[Site Audit](https://www.semrush.com/siteaudit/) helps you find (and learn how to fix) over 140 site issues that can impact SEO, including pagination issues.

For example, it can:

- Identify missing or incorrect canonical tags
- Flag crawlability and indexability issues
- Uncover duplicate content

[Configure the tool](https://www.semrush.com/kb/539-configuring-site-audit), run an audit, and head to the “**Issues**” tab.

To find canonical errors specifically, search “canonical.”

![Canonical errors listed include multiple canonical URLs, duplicated content issues, broken canonicals, and more.](https://static.semrush.com/blog/uploads/media/62/34/62348fc2a310b90c78248cc70be1518d/02bc2afb6a0b232800f0d47cccb3c688/AD_4nXdZ-GCly63Ec42YUFFiIH_fv9zHAvSVq_Wd7CWvbDuNTr5LKevTgSIFBweRkJGe_1yEXO_pS4wpQ0Ka5SvJx8Dej1NyiXKJnhygVNBFNFEmMZmzpzr6b56tQ1wAEo6hEVW2ASiDTw.png)

The tool will show any canonical-related errors on your site.

Click “**Why and how to fix it**” to see additional information about a problem and how to address it

![For each issue, a pop up shows more explanation.](https://static.semrush.com/blog/uploads/media/28/91/2891e57103b4443182cc2feaf0e9b64f/84b1940083fe47a64da947016b6e5c05/AD_4nXfoyp2nK44KXgj7vMRAYFIeGlTNPX_xwppQ5cuRfpavzADeSzJKpZGm9V2wg8CU38n9P0P0UJsV0YExt-6TCczC6KLAlIwSCsj9BUCK-ck2atK9J9j3Ct9hLRp3fAjsNnBUstk-.png)

Use the “**Crawlability**” thematic report in the “**Overview**” tab to see if your site has any crawlability or indexability issues.

Some of these could be due to pagination errors.

![Crawlability report is shown in Site Audit.](https://static.semrush.com/blog/uploads/media/3f/fe/3ffe84c91ff3b8979587feab73774424/6ebce1040c3d75869777865b5071c44b/AD_4nXdRRKXPGV1wVmW8CmvkYsYIRzk073KKkyQny8jqEUfeWD8CusDBke8iS-6CsIytSWUwq5Mwxjm9ZgaII-5eWWwFwXLwaFgfR1nagBC0RZtgJAcrRYpA1oN2GhEVtJpSKIKgD8pNdg.png)

The tool will provide a detailed breakdown.

Like this:

![Crawlability report shows a breakdown of site indexability, page crawl depth, crawl budget waste, and more.](https://static.semrush.com/blog/uploads/media/c2/41/c24100b5ed8b8970a5de113345568b2b/99a76bd4cc5aea909301cb60dd569f3f/AD_4nXfyeISg3tGq5641yvoOu9vAp0z4OqDKejb4RUMDlMFH5qjsChnsKKQnHf9StOUCKLs605bpkkXThvHC-0ctXWW6rMLnMFvjo4-1s6I3vsEgQ2zlzj1anxZ2bMfFtcEJbWYyUYaoog.png)

### Google Search Console

[Google Search Console (GSC)](https://search.google.com/search-console/about) provides valuable insights into how Google crawls and indexes the pages on your site, including your paginated pages.

GSC lets you:

- See if Google has indexed your paginated URLs
- Track crawl stats to reveal whether pagination is consuming too much crawl budget
- Find mobile usability issues on paginated pages

Use the “URL Inspection” feature to check the status of specific paginated URLs.

![URL Inspection tool allows you to enter the paginated page URL to see its index status.](https://static.semrush.com/blog/uploads/media/b8/b8/b8b8f6cff56e5c3ef97e4d4f58ead9d8/233b5900fdcb83e647e1a6e390fd0a38/AD_4nXcaWlyxrlk5ddrbS7Sc5P6ChUiQ27uUtx1UUBJAZbAwrFns5f5g8vkA1gEDUbRlV4Mz5DC_8I3fOLZ7S4z9ikW0DZkDJj98ob7X2zOKqxXEDyfYbH-aQLC_jAyJFodEa7KfI1ButA.png)

Go to “**Indexing**” > “**Pages**” to see a report of the known pages on your site. You’ll see which pages are indexed, plus which aren’t and why.

![AD_4nXc5NlDveInFPwDKRR0dbJwryixNRqoMI1ulzS6LWJF0ijlF0UFlcRfTe4upQ4_VprTtQLThkktLxZhyqU8FOMlz9EXXOeHVtYIUgVPedFf071VKYYwK8uM2g18WTTBu6dh8oM8u3g?key=ELws5aXz7HEeJBI-4X0_iiLj](https://static.semrush.com/blog/uploads/media/01/6d/016d51f35c1bc1ab86715073950f5570/9f3d381a6b5a895b39724d3e77fd3be6/AD_4nXc5NlDveInFPwDKRR0dbJwryixNRqoMI1ulzS6LWJF0ijlF0UFlcRfTe4upQ4_VprTtQLThkktLxZhyqU8FOMlz9EXXOeHVtYIUgVPedFf071VKYYwK8uM2g18WTTBu6dh8oM8u3g.png)

Then, find mobile usability issues in the “Mobile” report under “**Core Web Vitals**” in the “Experience” tab.

![A line graph shows change over time in Core Web Vitals.](https://static.semrush.com/blog/uploads/media/ae/ad/aeadc70d5a48848eecbffb1987095f70/27a076ecaeeb530856fe7580eee462c0/AD_4nXdNvJzEAqcveSyFZlCmSpkejG6okJn2DVxywRpFVzYEqOI9bAwlYo0Q0h0VCC_DJcJUVvaarabuvZV7MWD6S1p4aiHNYA7evo-vuFTeU6iYr9Mou3bRV9DUJXKNvypE4hzIOJ4Q6w.png)

### Google Analytics

[Google Analytics 4 (GA4)](https://analytics.google.com/analytics/) shows you how visitors interact with your paginated content.

With GA4 you can:

- Track user flow through page sequences
- See average engagement times for your pages
- Find where people leave your site

And plenty more.

To start, head to “**Engagement**” > “**Pages and screens**.”

Then, enter the identifier for your paginated pages in the search bar.

![/blog/, for example, is entered into the search bar below the line graph.](https://static.semrush.com/blog/uploads/media/09/0e/090e760182fcc735243fc917741f25f6/a0364275f4a6c8ab2eac1b0c30921a8c/AD_4nXcw4dR0rllzcTR-smDW1q_w-aP8TzsxFJqQVF9bfuOMcQOqs-zIj8Ixv0Vid9RjhxUFkA1myLxxTJMchTPNTVGWIIIGMRNWtG1xj2LCUA7Hl8gdUcOhfbx-9VIt9KLnv6AXj4ZMkg.png)

You’ll see information about your paginated pages, such as which pages get the most views and how much time people spend on them.

Use this information to determine the effectiveness of your paginated pages.

For example, compare the [average engagement time](https://www.semrush.com/blog/average-time-on-page-google-analytics/) (the average time your site was in focus in a user's browser) across different pages.

![Average engagement time column shows how many seconds visitors spend on each paginated page.](https://static.semrush.com/blog/uploads/media/7a/58/7a5827c64231819e7bc0094101764e31/3f03bc29525993defb32df6af520b091/AD_4nXft1Yf2B6OymrAI0Ds-tO-4zipBK-DuOjw24YGol3RTIh7ZN7vMl_DHzBP4LNmECa5Ijinzy0VPXPpIPVSDmsH1xAflh2w1wgpS45VtsJFcN7n6MCb1iO1L5mSKJSZ0PqPjS-qMEw.png)

Look for anomalies. And try to understand why people might spend more—or less—time on certain pages.

***Further reading****:*[*Google Analytics for Beginners: Getting Started with GA4*](https://www.semrush.com/blog/google-analytics/)

### Log File Analyzer

[Log File Analyzer](https://www.semrush.com/log-file-analyzer/) lets you evaluate your server log files, which provide raw data on how search engines interact with your site (including paginated pages).

[Analyzing your server log files](https://www.semrush.com/blog/log-file-analysis/) can help you:

- See which paginated pages search engines crawl most often
- Identify unnecessary crawler activity on low-priority pages
- Check the HTTP status codes for each page

To start, get a copy of your site’s log file.

Log files are stored on your web server, so you’ll need access to it to download a copy.

The most common way to access the server is through a free file transfer protocol client like [FileZilla](https://filezilla-project.org/). (If you don’t know how to do this, ask your tech team.)

Then, use Log File Analyzer.

Browse or drag and drop your file into the tool and click “**Start Log File Analyzer**.”

![AD_4nXdbZN1YiH1HVaAZyxRKAUlsQcaIQT0BxBrVLGvAbciG85Dw32Q_C3FbMAVLcep73jK6kioAQrHmqkuNB4Kj0VONB6hQ2Lh_T-fxkfaMvXVarHUfmvbW6lIpy1_rq0GdSxjlEcJDug?key=ELws5aXz7HEeJBI-4X0_iiLj](https://static.semrush.com/blog/uploads/media/99/9e/999e4fc442543a8a763705945800b7b6/6f836d097c7c86e682beca034b736c75/AD_4nXdbZN1YiH1HVaAZyxRKAUlsQcaIQT0BxBrVLGvAbciG85Dw32Q_C3FbMAVLcep73jK6kioAQrHmqkuNB4Kj0VONB6hQ2Lh_T-fxkfaMvXVarHUfmvbW6lIpy1_rq0GdSxjlEcJDug.png)

You’ll see a chart displaying Googlebot activity, such as daily hits, status codes, and requested file types.

![A line graph shows bot activity, and pie charts shows status codes and file type breakdowns.](https://static.semrush.com/blog/uploads/media/84/29/8429f95519aa8ce3104ab3b6da14340b/7799e04224e950e588882c808b5ebf15/AD_4nXffXofk5Rtj8ilxgaOPry7CkgysSRZVLPvXONCzyasz39Tpq8urf71zENeyLrOT3spy8GQ6MUoQtm-X5Tcz3xcniCfEU_uwRtMtBfXEDFqLt7ZwkPrmI7Go2OMD1Nrt2v202d_WqA.png)

Scroll down to see a table with insights for specific pages and folders.

![Hits by Page table lists page paths, file types, bot hits, and crawl frequency for each.](https://static.semrush.com/blog/uploads/media/d4/c8/d4c89bb2ed14248097951dd7c3ea4829/8575e180786d8407025e1cd963cd8e5a/AD_4nXdyrkrkFrmGjzTemxr3FDSou4d46_8pnUUOQwiB3Qe2Z53fu3lllWc0d9SmVbsriss3Fm68uwZPBDHfyT7a5L9x91cK628weWQRQ_bBFxSVrn959JFqUM8OQSHBzlSwWjjqccLn-Q.png)

Sort the table by the “**Crawl Frequency**” to see how Google spends its [crawl budget](https://www.semrush.com/blog/crawl-budget/) on your pages.

![AD_4nXfcI8IqS6gTJ2Km2yO53Rkxflt3FW-KhdF4zefLLotwVcPnTvDHt9Q6wo7MzuXJ5PnyF4h9h7vRPc8IfQ60pSfC5P6IUFlq5LtmK0ZLYoerY8xQTUkzPgXTBHtMo2-x84TFYML8?key=ELws5aXz7HEeJBI-4X0_iiLj](https://static.semrush.com/blog/uploads/media/c9/b9/c9b9e9cb443e55bbd9edd55b3936fd5c/79a05ccc977bd2b29a45b563361c601e/AD_4nXfcI8IqS6gTJ2Km2yO53Rkxflt3FW-KhdF4zefLLotwVcPnTvDHt9Q6wo7MzuXJ5PnyF4h9h7vRPc8IfQ60pSfC5P6IUFlq5LtmK0ZLYoerY8xQTUkzPgXTBHtMo2-x84TFYML8.png)

***Further reading****:*[*Log File Analysis for SEO: What It Is & How to Do It*](https://www.semrush.com/blog/log-file-analysis/)

## Get the SEO Benefits of Pagination

Properly implemented pagination can support your SEO goals because it helps users (and search engines) find and consume content easily.

The next step is to audit your current pagination setup.

Here's your action plan:

First, run a complete [SEO audit](https://www.semrush.com/siteaudit/#sorting/update_asc/page/1/).

Focus on pagination-related issues like:

- Duplicate content across paginated pages
- Broken pagination links
- Crawl efficiency problems
- Improper canonical tags

![Site Audit issues lists shows all errors, warnings, and notices for a domain.](https://static.semrush.com/blog/uploads/media/e9/fc/e9fc1cf238fc6c67bca4039e3ef9d2d4/8da91a4f8ebcde08515623c705c49684/AD_4nXfmgZQfORR0K_PXcxZQxbb6rEx-hJzT4rPQOgbvj7viuKC5DjApZ4VyXhI1OwkFFmTrZMSWqeCW-3nFXMcb0jqhXaMFUoR9BmkinSERgZTwd-vQ3X08YZaBtls9qC7VD3E569yKxQ.png)

Next, analyze user behavior data.

Look at how visitors navigate through your paginated content. Pay special attention to

- Where users leave your website
- Which pages get the most engagement
- Pages with high bounce rates

Finally, test alternative solutions.

Consider adding infinite scroll if you have a much larger portion of mobile users. Or try "Load more" buttons in key sections. And compare how these changes impact performance.

Get started by running your first audit today. Focus on fixing technical issues first. Then move on to user experience improvements.
