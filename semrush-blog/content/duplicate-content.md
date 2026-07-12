---
title: "What Is Duplicate Content? + How to Fix It for Better SEO"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "duplicate-content"
url: "https://www.semrush.com/blog/duplicate-content/"
canonical: "https://www.semrush.com/blog/duplicate-content/"
author: "Tushar Pol, Christine Skopec"
published: "2020-12-23T14:30:00+00:00"
updated: "2025-02-19T11:07:00+00:00"
categories:
  - "Content"
freshness_reasons: []
schema_genre: "Content"
fetched_at: "2026-06-12T15:07:19+00:00"
status_code: 200
html_hash: "e94858595a0a4ef8f20b757d805454a3e560b589de29a639ce203e732c9d7af3"
clean_word_count: 1673
clean_char_count: 12126
---
# What Is Duplicate Content? + How to Fix It for Better SEO

## What Is Duplicate Content?

Duplicate content is when identical or highly similar content appears at more than one URL on the internet, affecting the rankings of one or more of the pages.

This issue can happen on your own website (internal duplicate content) or across different websites (external duplicate content).

For a page to qualify as a duplicate, it must have:

- Noticeable overlap in wording, structure, and format with another piece
- Little to no original information
- No added value for the reader compared to a similar page

## How Does Duplicate Content Affect SEO?

Duplicate content can harm your search rankings—regardless of whether duplication occurs internally or externally.

With internal duplication, your own pages cannibalize each other's ranking potential. And with external duplication, there's a risk that another site's copy could rank instead of your original content.

You may also encounter additional internal challenges:

- **Diluted backlink power**: [Backlinks](https://www.semrush.com/blog/what-are-backlinks/) are links on other sites pointing to your site that pass ranking power to your pages. If you have identical pages that each get backlinks from different websites, you're splitting your ranking power instead of concentrating it on one main URL.
- **Wasted crawl budget**: Search engines have limited time and resources (called crawl budget) to explore your site. When they crawl multiple versions of the same content, that can prevent important pages from being crawled and indexed—especially if your website is large.

## Common Causes of Duplicate Content

It’s helpful to understand what causes duplicate content in the first place, so you can take steps to prevent it.

Here are some of the most common culprits:

1. [**URL parameters**](https://www.semrush.com/blog/url-parameters/): Every time your site adds parameters to a URL (for tracking, sorting, or filtering), it creates multiple URLs that have the same core content. For example, “domain.com/shoes” and “domain.com/shoes?size=9” will show very similar content.
2. **Domain name variations**: Your content might be accessible through multiple versions of your domain, including HTTP vs. HTTPS versions of your site, with or without "www" in front of your domain name, and with or without a forward slash at the end of URLs. So, a single page could exist at several distinct locations.
3. **Scraped or syndicated content**: If other websites republish your content (with or without permission), it creates duplicate versions on different domains
4. [**Pagination**](https://www.semrush.com/blog/pagination-seo/): If you split content across multiple pages (like in an article series or product catalog), each page will have a separate URL but very similar content

## How to Fix Duplicate Content Issues

Let's see what you can do to prevent and fix duplicate content issues.

### Implement 301 Redirects

One reliable way to fix duplicate content one your own site is by using a [301 redirect to](https://www.semrush.com/blog/301-redirects/) permanently move one URL to another.

![In this example, URL A and URL B are duplicate content. Both pages are redirected to URL C.](https://static.semrush.com/blog/uploads/media/bc/b7/bcb7917e6a4fa3c2b8942098417c3903/6de97733904aab8713b10ae933a521e5/AD_4nXck9LyujBTRDDXleHgxyhc062ockr4MwGr92aakj7j1Ryv2DwL9d6eyqgI32t8LfKRmCkA18MIGjY_MlmnJaD_t5vAfPxxKySMnV9pN5mTqcnbUpvlzFR-WbKb3Y2cCNAkjSYcf.png)

This method is best for duplicates you don't need to keep, such as when:

- Moving all HTTP traffic to HTTPS
- Standardizing your domain format by choosing www or non-www
- Consolidating duplicate pages into a single page

Most hosting providers and content delivery networks (CDNs) offer easy ways to set up 301 redirects.

If you're using Apache servers, you can implement [redirects in your .htaccess file](https://www.semrush.com/blog/301-redirect-htaccess/) (a file for configuring certain website details). It’s just a matter of writing a directive.

For WordPress users, plugins like [Redirection](https://wordpress.org/plugins/redirection/) and [Yoast SEO](https://wordpress.org/plugins/wordpress-seo/) can handle redirects for you—just a few clicks and you’re done.

To add a redirect with Yoast SEO, just install the plugin, activate it, and then select “**Redirects**” from the Yoast menu in the left sidebar.

![AD_4nXd07-yVELQxp0pM-JZjgkFggnaExqM4Hh3__3bMxU5Moqx4YdGerwUqtspfLlHLxd6DL_NiiqogOMdn9VRt1hZPbvEa2erfLE7E063YwQEYKhNucW3UTQOKOc1qUZxCqy8dkFeW?key=wiZ03fpr-0y0UlL0MKTQRps4](https://static.semrush.com/blog/uploads/media/bc/60/bc603521188e570ae148e448f3423f23/0a228c2eea091d0487f18daae169f9b1/AD_4nXd07-yVELQxp0pM-JZjgkFggnaExqM4Hh3__3bMxU5Moqx4YdGerwUqtspfLlHLxd6DL_NiiqogOMdn9VRt1hZPbvEa2erfLE7E063YwQEYKhNucW3UTQOKOc1qUZxCqy8dkFeW.png)

You can then select your redirect type and specify both the old and new URL.

![The redirect type here is 301 move permanently with the old http URL redirecting to the https URL.](https://static.semrush.com/blog/uploads/media/39/80/39805068655b4a51ada8c19ea454c2ae/6decb47146c004d34c37327c751f9eca/AD_4nXdNYoNaKP2IMqhW6bm8C53pXzM1PrQR0s7bkHhcPKK5I-TAIjv2TxHOHgAHY3x_nOCzUtzVGeTxBuFhmMumpkEdYGP-e_e0WgQ8X6p8eY4Domkikc6WlbN7m4R1XRRmk9XN5U4U9A.png)

### Use Canonical Tags

A [canonical tag](https://www.semrush.com/blog/canonical-url-guide/) is a snippet of HTML that specifies the main (canonical) URL for duplicate or highly similar content to ensure only the main version is indexed and that search engines will consolidate backlink power to that version.

Here’s what a canonical tag looks like:

`<link rel="canonical" href="https://domains.com/shoes" />`

The “href” attribute should point to the main version of the page you want search engines to prioritize.

When should you use canonical tags? Here are a few scenarios:

- You have duplicate content because of parameterized versions of URLs
- Your content is split into multiple pages (pagination)

For the first case, duplicate versions should have a canonical tag pointing to the main version. And the main version should have a self-referencing canonical tag (one pointing to itself).

For pages in a paginated series, each page should have a self-referencing canonical tag. This means each page points to itself, helping search engines understand that each page is a unique part of a series rather than duplicates of a single page.

To implement canonical tags, simply add the tag to the <head> section of the page’s HTML.

If you use WordPress, SEO plugins like [Yoast SEO](https://yoast.com/wordpress/plugins/seo/) and [RankMath](https://wordpress.org/plugins/seo-by-rank-math/) will let you set a canonical tag through their settings.

Here’s how to do it with Yoast:

Just open the page you’d like to set the canonical tag for, navigate to its SEO settings, click “**Advanced**” to expand the menu, and then enter the canonical URL in the designated field.

![Canonical URL is the final field in the Advanced settings.](https://static.semrush.com/blog/uploads/media/b1/b8/b1b86f4bb966bf500329872727e710ab/84513b3e2aab057fe50a063c48ebd3c2/AD_4nXeD0SvQxYmhUpct37C4du_ABE__zAdw0BgKpPX8Mm1yAGdNzv7ToIl_d0j3WWHcm7fMXkoxdPU-LJRC5FwAjWi1lgXPdHVhlA53fmPZk4QBVIgyVEFux_xtxOHJEPbb3SSTJwLbmg.png)

### Use Noindex Tags

A [noindex tag](https://www.semrush.com/blog/noindex/) is an HTML directive that tells search engines not to include a particular page in their index—meaning it won’t appear in search results.

This approach is especially useful for handling syndicated content—when your content is published on other websites (with your permission).

In cases like this, ask publishers to add a noindex tag to the syndicated versions to ensure only your original content appears in search results.

Here's what a noindex tag looks like:

`<meta name="robots" content="noindex" />`

You can ask publishing partners to add this tag to the <head> section of the syndicated pages.

They can also use popular SEO plugins like Yoast SEO or RankMath to add the noindex directive without touching any code. (Note that this only works for WordPress sites.)

### Differentiate Content

Sometimes, the best solution for duplicate content on your own site is simply to make each page unique.

Here's how to differentiate similar content:

- Rewrite the content with unique insights and perspectives
- Add practical examples and actionable steps your readers can follow
- Include original research, expert quotes, or data to support your points
- Run your content through [SEO Writing Assistant](https://www.semrush.com/swa/) to identify any text you may have inadvertently copied, so you can make it original

![SEO Writing assistant grades Originality by doing a duplicate content check.](https://static.semrush.com/blog/uploads/media/c4/53/c453617fc79d664dfb9aca036b0c676c/f0d3b81e3767d0f651e3dcf385099911/AD_4nXcDWo0PWjL-ix9YrY7mArdVcP99WsRX4QSurmirky7QL9XJrIIogXU2wYveYbWAyJppU6Z4prR_fkvb5G45mziNIDWYa_xoPfKTXh-zwTBjI6hyFpKqhFaBz5zhzUJ4XhCa9kz5.png)

### Request Removal from Other Sites

Sometimes, websites may copy and republish your content without permission (known as content scraping).

While Google's algorithms are generally good at identifying and prioritizing the original source, you may want to take action if unauthorized copies of your content appear in search results.

First, contact the website owner directly and request removal of your content. Many website owners will comply to avoid legal issues.

If direct contact doesn't work, you can submit aDigital Millennium Copyright Act (DMCA) takedown request through [Google's legal troubleshooter tool](https://support.google.com/legal/troubleshooter/1114905?sjid=5686041358045546252-NC).

After submitting your complaint, it usually takes a few days for Google to process the request and remove the content from search results.

## Find Duplicate Content Issues On Your Site

Before you can fix duplicate content on your site, you need to find where it exists.

[Google Search Console](https://search.google.com/search-console/about) (GSC) provides a free way to identify duplicate content issues through its indexation reports.

![The why pages aren't indexed report shows one reason as "duplicate, Google chose different canonical than user."](https://static.semrush.com/blog/uploads/media/2b/fc/2bfcf75c5fd08acc44634b532540cb10/7b8d68dc466a2d7bb340eaf4c99e8522/AD_4nXefos1qoaEAcK6_5x-dC09pFBSNuIV-J43vLPnVXAuGF2iMyhrL9J9YKnNuFtRnPUpWdp5GpeVcXu-7QoZsUme61FBzBphicpPaxahznNJcY0OXl4b-APRXKPpZh6QDwvz1WnN_.jpeg)

If you want to do a more thorough analysis, you'll want to use a dedicated auditing tool like Semrush’s [Site Audit](https://www.semrush.com/siteaudit/).

To get started, open the tool, enter your domain name in the search bar, and click “**Start Audit**.”

![AD_4nXeKH5fxawTuJtRP6vegLVglnWo0LV-MAXbMigsprdYDVvsu1M6EZYaArMfVQ1ttNh_E67kKuoZNFgf31Es1vVsnbHzRleWTCHIu9iSs5v_4igl86FnV43-z02pNBCW2prG9XWZRdQ?key=wiZ03fpr-0y0UlL0MKTQRps4](https://static.semrush.com/blog/uploads/media/4e/a8/4ea828e48ebb4039ec1cb484cfe4eca8/bf4c72a9fdff4aacd47ab7b3bea79670/AD_4nXeKH5fxawTuJtRP6vegLVglnWo0LV-MAXbMigsprdYDVvsu1M6EZYaArMfVQ1ttNh_E67kKuoZNFgf31Es1vVsnbHzRleWTCHIu9iSs5v_4igl86FnV43-z02pNBCW2prG9XWZRdQ.png)

After configuring the basic [audit settings](https://www.semrush.com/kb/539-configuring-site-audit), wait for the audit to complete.

Once it’s done, go to the "**Issues**" tab and search for "duplicate.”

The tool will flag pages that are at least 85% identical, along with duplicate title tags and meta descriptions.

![Search for duplicate in Site Audit reveals issues like duplicate content, no redirect or canonical from http to https, and more.](https://static.semrush.com/blog/uploads/media/29/e8/29e84b28214556e76ac6d7bd2e2dcfb0/634af21041034208e6d98c7be04beace/AD_4nXeO5mOM6DJD5_yzn69F7WvCvcoqGLrrvdFC2_L1MhUMdLIsARUib28iRevMZ7W7ptOR52RPS_ipkw7eQSSS5sv7UosFE28XY5UkwRxDzD6HheIiJMG7A56Xo25ZmKB-grYr2O9tkw.png)

Click through to find the affected pages. And then use the appropriate fix for the situation.
