---
title: "301 Redirects: How to Use Them & How They Affect SEO"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "301-redirects"
url: "https://www.semrush.com/blog/301-redirects/"
canonical: "https://www.semrush.com/blog/301-redirects/"
author: "Carlos Silva, Christine Skopec"
published: "2020-05-08T15:32:00+00:00"
updated: "2026-02-18T11:52:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T13:16:31+00:00"
status_code: 200
html_hash: "aab726e066e130a0a630ed8f4bb3702e086da4ea1446e55d2bb682975265718e"
clean_word_count: 3227
clean_char_count: 20625
---
# 301 Redirects: How to Use Them & How They Affect SEO

Regularly updating your website to remove outdated content or update your URLs is key for maintaining online visibility. In these cases, it’s important to use 301 redirects to ensure search systems and users end up in the right place.

This guide will explain what 301 redirects are, how they impact your SEO, and how to use them properly.

Let’s begin.

## What Is a 301 Redirect?

A 301 redirect is an HTTP status code that sends users and search systems from the requested URL to a different URL and indicates that the move is permanent.

If **/old-page/** has a 301 redirect to **/replacement-page/**, then anyone who attempts to visit **/old-page/** automatically ends up on **/replacement-page/**.

![A 301 redirect points from an old page to a replacement page.](https://static.semrush.com/blog/uploads/media/82/e8/82e869a06ab55b56310a02eb1eaeaf53/7c10d31652c74f44826a8ff47f672099/image.png)

### How a 301 Redirect Works

A 301 redirect works by telling browsers and search systems that a page has permanently moved to a new URL.

When a browser or crawler requests an old URL that’s since been redirected, the server replies with a 301 status code and provides the new address. The browser or crawler then loads the new page.

Usually, 301 redirects happen so quickly that visitors don't even notice they clicked on an old page but landed on a new one. And the address bar updates automatically.

## How Do 301 Redirects Affect Your SEO?

Using 301 redirects generally doesn’t affect your SEO because they transfer search engine rankings and ranking signals from old pages to replacement pages and also send traffic from the old URL to the new one.

Search engines like Google typically transfer almost all of the old page's ranking power to the new page. This means you can usually retain the “SEO value” of the original URL (i.e., the authority the page has gained through [backlinks](https://www.semrush.com/blog/what-are-backlinks/)).

Because 301 redirects also ensure users reach the correct pages instead of broken or suboptimal pages, those users are more likely to engage positively with your site. Which is good for SEO and marketing in general.

It’s worth noting that 301 redirects can negatively impact your [page speed](https://www.semrush.com/blog/page-speed/), but generally the effect is minor. And if you’re redirecting from a deleted or low-value page to a new, high-value page, the benefits typically outweigh this potential risk.

Just be aware that search engines take time to update their indexes and recognize the redirects you put in place. After you set one up, it can take weeks or even months for your pages to see ranking changes.

### How Do 301 Redirects Affect AI Visibility?

Using 301 redirects usually doesn’t affect whether an AI system can surface your content.

That said, it’s possible AI systems might cite old versions of your pages based on AI training data in ways that might be confusing. This could affect the user experience.

But ultimately, if the redirect is designed to take a user from an outdated or low-value page to a more valuable page, the redirect is still probably worth it. But this does mean it’s even more important to ensure your redirects lead to relevant pages.

AI tools like ChatGPT also sometimes include broken links in their responses. This means pages you delete but don’t redirect could also still be cited in AI responses. Redirecting these pages to a relevant page (where one exists) is especially important for ensuring a positive user experience.

But if there is no suitable page to redirect to, 404 (or 410 for permanently removed content) is typically still the correct response.

## Use Cases for 301 Redirects

These are the most common use cases for 301 redirects:

### Deleting a Page That Has a Replacement

When you delete a page, you can add a 301 redirect from the deleted page to a replacement page to potentially pass on search visibility and traffic.

But you should only redirect to an equivalent or near-equivalent page that’s likely to satisfy the same needs as the deleted page.

For example, you can preserve search visibility and traffic by adding 301 redirects from:

- Discontinued product pages to replacement product pages
- Old blog posts to new blog posts on similar topics
- Niche service information pages to broader service information pages

**Don’t** add a 301 redirect to an irrelevant page (e.g., from an old blog post to your homepage). Because these kinds of redirects can confuse users and search systems.

If you want to delete a page that has no good replacement, you should generally return the [404 Page Not Found](https://www.semrush.com/blog/404-error/) error. To show users and search engines that the page is no longer available.

Semrush’s 404 error page looks like this:

![The page says "We got lost. It looks like this page doesn't exist. Try going back or click the button below and we'll take you home."](https://static.semrush.com/blog/uploads/media/d5/86/d5869f4c07608ef7d5cbe01579547be6/905d91d7ecbd78e01321cd55329348fd/image.png)

### Migrating Your Site to a New Domain

Implementing 301 redirects is an important part of any website migration project (e.g., if you’re switching to a new domain name as part of a rebrand).

- If you’re keeping the same [website structure](https://www.semrush.com/blog/website-structure/) on your new domain, you can implement a mass redirect to send visitors from the old domain to the corresponding path on the new domain (e.g., **olddomain.com/path** > **newdomain.com/path**)
- If you’re changing your website structure, you’ll need to create a redirect map that matches up each old URL with its replacement URL (e.g., **olddomain.com/old-path** > **newdomain.com/new-path)**

For migrations involving hundreds or thousands of pages, create a comprehensive redirect map before you perform the migration. Export your old site's URL structure, map each URL to its new equivalent, and test the redirects in a staging environment before going live.

See our [website migration checklist](https://www.semrush.com/blog/website-migration-checklist/) for a full guide on how to properly implement redirects during a migration.

### Migrating from One Platform to Another

When migrating from one content management system or website platform to another, 301 redirects are essential for preserving your search visibility and traffic.

For example, ecommerce platform Shopify typically uses URL structures like **/products/product-name** and **/collections/category-name**.

Meanwhile, the WordPress plugin WooCommerce often uses **/product/product-name** and **/product-category/category-name**.

Your redirect mapping from Shopify to WooCommerce could look like:

- **Old**: https:/store.example.com/products/blue-widget
- **New**: https://www.example.com/product/blue-widget/

As with standard domain migrations, it’s best to set up a redirect map before you start to avoid issues later on.

### Changing URL Slugs

If you change a URL slug, add a 301 redirect from the old URL to the new URL.

The [URL slug](https://www.semrush.com/blog/what-is-a-url-slug/) is the last part of the page address that serves as a unique identifier of that page.

For example, you might want to fix a typo in the URL slug. Like this:

- **Redirect from**: https://www.semrush.com/blog/031-redirect/
- **Redirect to**: https://www.semrush.com/blog/301-redirect/

Or make your URL slugs shorter and more descriptive. Like this:

- **Redirect from**: https://www.semrush.com/blog/h25j-kb3t2b2t-po9/
- **Redirect to**: https://www.semrush.com/blog/301-redirects/

### Moving a Page to Different URL Path

If you move a page to a different URL path, add a 301 redirect from the old URL to the new URL.

For example, if you introduce a new product category and move existing products to this category, you might set up redirects like this:

- **Old URL**: https://www.example.com/old-category-name/product-name
- **New URL**: https://www.example.com/new-category-name/product-name

### Consolidating Duplicate or Similar Pages

You can use 301 redirects to consolidate duplicate or similar pages on your website.

Consolidating pages using a 301 redirect allows you to prevent confusion for users and search systems, combine the SEO strength of multiple pages, and streamline website maintenance.

Duplicate pages are generally caused by:

- WWW and non-WWW URLs (e.g., www.example.com and example.com)
- [HTTP and HTTPS URLs](https://www.semrush.com/blog/http-vs-https/) (e.g., http://www.example.com and https://www.example.com)
- Trailing slash and non-trailing slash URLs (e.g., example.com/ and example.com)
- Case sensitivity (e.g., example.com/blog/ and example.com/Blog/)
- Session IDs or parameters (e.g., example.com/page?sid=123 and example.com/page)
- Index files (e.g., example.com/page and example.com/page/index.html)
- Multiple paths to the same page (e.g., example.com/page and example.com/category/page)

It’s also smart to consolidate pages that serve very similar purposes for users.

Let’s say your website has three blog posts about the same topic. You could combine these posts into a single, comprehensive guide and add 301 redirects pointing from the old URLs to the new URL accordingly.

To find pages that might be worth consolidating, use Semrush’s [Position Tracking](https://www.semrush.com/position-tracking/) tool.

The “**Cannibalization**” report shows which pages on your site show for the same terms. This suggests that the pages are similar and could be competing with each other for search visibility (an issue known as [keyword cannibalization](https://www.semrush.com/blog/keyword-cannibalization-guide/)).

![Cannibalization report shows affected keywords and cannibal pages.](https://static.semrush.com/blog/uploads/media/f6/3a/f63aace3097243f090311cdf4f8217e0/26f001807eed8d31afc524d6176ebcc1/image.png)

If you find pages with very similar purposes when using Position Tracking, consider combining them and implementing 301 redirects.

## When NOT to Use 301 Redirects

Here are three instances when you shouldn’t use 301 redirects, and what you should do instead:

- **Temporary content moves**: If you're moving a page temporarily (e.g., for seasonal promotions), use a [302 redirect](https://www.semrush.com/blog/302-redirect/). This tells search engines to keep the original URL in their index.
- **A/B testing**: When split-testing page variations, use 302 redirects or JavaScript-based redirects. Using 301s can cause search engines to consolidate your test variations, skewing your results.
- **Removing a page that has no suitable substitute**: If a page is truly gone with no replacement, serve a proper 404 error. Don't redirect to your homepage or a generic category page—this is confusing for users and search systems.

## How to Do a 301 Redirect

To do a 301 redirect, you need to use the redirect settings in your website editor, use a suitable website plugin, or get a web developer’s help.

Exactly how you implement a 301 redirect depends on how your website is set up.

Here are a few of the most common situations:

### How to Do a 301 Redirect on WordPress

To set up 301 redirects on WordPress websites, you can use plugins.

There are dedicated redirect plugins like [Redirection](https://en-gb.wordpress.org/plugins/redirection/) and [301 Redirects](https://wordpress.org/plugins/eps-301-redirects/) for WordPress websites. These plugins are typically straightforward to use, allowing you to set the old URL and map it to the new URL.

![301 redirect plugin interface with URL path entered and custom destination set to semrush.com URL.](https://static.semrush.com/blog/uploads/media/c7/26/c726550729a002ca1441010e39692144/68e21669df9f4aeede94d5153470d900/image.png)

You can also set up redirects for a WordPress site with a paid version of the [Yoast SEO plugin](https://www.semrush.com/blog/yoast-seo/). Simply choose the “301 Moved Permanently” option, add your old URL and replacement URL, then click “**Add redirect**.”

![Yoast SEO redirect settings showing a 301 redirect from /old-page-url/ to /new-page-url/ with Add Redirect button highlighted.](https://static.semrush.com/blog/uploads/media/be/94/be94fd38a98187b4369badda5cef551c/66c3996f68a0835d83eb65577155a103/image.png)

### How to Set Up Redirects in Other Content Management Systems and Website Platforms

Here are basic 301 URL redirect instructions for some other content management systems:

- **Adobe Commerce**: Go to “**Marketing**” > “**SEO & Search**” > “**URL Rewrites**” to use the [custom URL rewrites](https://experienceleague.adobe.com/en/docs/commerce-admin/marketing/seo/url-rewrites/url-rewrite-custom) feature. You can also [set up automatic redirects](https://experienceleague.adobe.com/en/docs/commerce-admin/marketing/seo/url-rewrites/url-redirect-product-automatic) to handle product or category URL changes.
- **Drupal**: Install and use the [Redirect module](https://www.drupal.org/project/redirect)
- **HubSpot**: Go to “**Settings**” > “**Content**” > “**Domains & URLs**” > “**URL Redirects**” to use the [URL redirects tool](https://knowledge.hubspot.com/domains-and-urls/create-and-manage-url-redirects)
- **Joomla**: Install and use one of these [URL redirection plugins](https://extensions.joomla.org/category/site-management/url-redirection/)
- **Shopify**: Go to “**Content**” > “**Menus**” > “**View URL Redirects**” > “**Create URL redirect**” to use the built-in [URL redirect feature](https://help.shopify.com/en/manual/online-store/menus-and-links/url-redirect)
- **Squarespace**: Open the developer tools panel and click “**URL mappings**” to use the [URL mappings](https://support.squarespace.com/hc/en-us/articles/205815308-URL-mappings) feature
- **Webflow**: Go to “**Site settings**” > “**Publishing**” > “**301 redirects**” to use the [built-in redirect feature](https://help.webflow.com/hc/en-us/articles/33961294898835-Set-301-redirects-to-maintain-SEO-ranking)
- **Wix**: Go to your SEO Dashboard > “**Tools and settings**” > “**URL Redirect Manager**” to use the [URL Redirect Manager](https://support.wix.com/en/article/setting-up-a-301-redirect-for-a-page-on-your-site)

### How to Set Up 301 Redirects Using an .htaccess File

You can set up 301 redirects using .htaccess if your website runs on an Apache server, but only do so if you’re confident that you won’t make mistakes that could harm your SEO performance.

Find and edit your .htaccess file in your web host’s file manager, specifically inside your site’s root folder (often titled “public\_html”).

![.htaccess file with 301 redirect rules for non-WWW, HTTPS, and a specific page URL.](https://static.semrush.com/blog/uploads/media/bd/10/bd10129d0057aaea86a039a2aebd2d44/6c758204f2f890e29e7a7c9461ac4d16/image.png)

Once you’re in your .htaccess file, make sure you have the following lines to turn RewriteEngine on:

`<IfModule mod_rewrite.c>
RewriteEngine On
</IfModule>`

You can then add rules depending on your specific redirect needs. To redirect a single URL, it would look like this:

`RewriteRule ^old-page/?$ https://www.yourdomain.com/new-page/ [R=301,L]`

See our full guide to [.htaccess 301 redirects](https://www.semrush.com/blog/301-redirect-htaccess/) for a more detailed walkthrough.

If you need to set up 301 redirects in bulk, it’s usually best to get a web developer’s help.

## Best Practices for 301 Redirects

Follow these best practices to ensure your 301 redirects work properly and support your SEO goals:

### Update Links That Point to Redirected URLs

Wherever possible, update any [internal links](https://www.semrush.com/blog/internal-links/) that point to a redirected URL so they point directly to the replacement URL instead.

Also update any other links beyond your website that you control, such as those in your social media profiles and directory listings.

For example, if **/old-page/** redirects to **/replacement-page/**, find links that go to **/old-page/** and change those links to **/replacement-page/**.

Avoiding unnecessary link redirects can:

- Reduce load times (although this is unlikely to be a huge effect)
- Improve crawl efficiency (i.e., help search systems explore your site)
- Prevent redirect chains (i.e., redirects that lead to redirects, which can confuse crawlers and cause loading delays)

### Remove Redirecting URLs from Your XML Sitemap

Remove redirecting URLs from your [XML sitemap](https://www.semrush.com/blog/xml-sitemap/) to ensure you’re sending clear signals to search systems.

The XML sitemap should only include URLs you want to show in search results. Because search systems use the file to help decide which pages to [crawl and index](https://www.semrush.com/blog/what-are-crawlability-and-indexability-of-a-website/).

You might also need to add your replacement URLs to your XML sitemap if you’re redirecting to entirely new URLs.

### Only Redirect to Canonical URLs

You should only redirect to a [canonical URL](https://www.semrush.com/blog/canonical-url-guide/), which is the primary address for a webpage.

(You can specify canonicals with the rel=“canoncial” link attribute.)

For example, if your blog is available via https://example.com/blog/ **and** https://example.com/blog/?page=1, Google will try to select one URL as the canonical version that will show in search results. And you should focus your SEO efforts on this canonical version.

In practice, this means you should **not** redirect to a URL that:

- Has a canonical tag pointing to another URL
- Has a 301 redirect to another URL

### Avoid Redirect Chains and Loops

If you redirect to a page that has a 301 redirect in place, you risk creating a redirect chain that slows users and search engines down. Or creating an infinite redirect loop.

Redirect chains occur when multiple redirects are stacked in sequence (e.g., page A > page B > page C). This forces browsers and search systems to make multiple requests before reaching the final destination.

These redirect “hops” can potentially impact how the link equity flows from the first page to the redirected URL. They can also increase the page load time.

![Redirect chain diagram showing URL A redirects to B, then B redirects to C.](https://static.semrush.com/blog/uploads/media/e0/84/e084292cec510804e7158efce3f6dabc/6f03feb4f61426aa6151f872a8d6e6d3/image.png)

A redirect loop occurs when you redirect from one page to another page that redirects back to the original page. For example, URL X redirects to URL Y, which redirects back to URL X, and so on.

This creates an infinite loop that confuses search engines and provides a poor user experience, usually resulting in a [“too many redirects” error](https://www.semrush.com/blog/too-many-redirects/).

![Redirect loop diagram showing URL X redirects to Y and Y redirects back to X.](https://static.semrush.com/blog/uploads/media/37/5a/375ad6edb2574b087ada6eacb6306b69/0c09845b6b62c8926037f0dbdaf71159/image.png)

Redirect chains and loops waste [crawl budget](https://www.semrush.com/blog/crawl-budget/)—the time and resources a crawler will devote to your site before moving on. This means some of your important pages can be missed.

You can identify redirects on your website, along with redirect chains and loops, using Semrush Site Audit, the premium version of our [free SEO checker](https://www.semrush.com/siteaudit/), by clicking the “**Issues**” tab and searching for “redirects.” If there’s an issue, click the number beside the problem to see a list of the affected pages.

![Site audit issues report showing 38,264 URLs with a permanent redirect highlighted under Notices.](https://static.semrush.com/blog/uploads/media/1b/b4/1bb499b6743f399ec499765df6f71e0d/4e23e709ddca1d0eec6dc44253effabb/image.png)

The solution is straightforward: update all 301 redirects to point directly to the final destination URL.

## Find 301-Related Issues on Your Website

Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool makes it easy to find 301-related issues on your website.

Use the tool to:

- Monitor the 301 redirects, canonical tags, and temporary redirects on your website
- Find internal links that point to redirected or broken URLs
- Identify duplicate content issues (where you might want to add 301 redirects)
- Check for overly long URLs that may need updating
- Ensure your website prioritizes HTTPS over HTTP
- Look for redirect chains and loops

Site Audit also checks for dozens of other SEO and AI search issues and provides advice on how to fix each one. Try it today.
