---
title: "Redirects: What They Are & How to Use Them"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "redirects"
url: "https://www.semrush.com/blog/redirects/"
canonical: "https://www.semrush.com/blog/redirects/"
author: "Kelly Lyons, Yannick Weiler, Mariya Delano, Simon Fogg"
published: "2020-07-20T11:00:00+00:00"
updated: "2024-12-12T19:11:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T18:52:22+00:00"
status_code: 200
html_hash: "fb3559d536c793a978af612cf4ea0e050e865d6375b60560bc16c11d729451e0"
clean_word_count: 3707
clean_char_count: 27188
---
# Redirects: What They Are & How to Use Them

## What Is a Redirect?

A URL redirect (sometimes called “URL forwarding”) sends users and search engines to a different URL than the one they initially requested.

You can use redirects to move a webpage to a new address so that both visitors and search engines automatically reach the correct page.

Common redirect types include 301 (moved permanently), 302 (moved temporarily), and meta refresh.

## Why Are Redirects Important?

Redirects are important for two key reasons:

### Redirects Ensure a Good User Experience

Redirects ensure visitors don’t land on broken or duplicate pages.

For example, consider a blog post about “the best SEO courses in 2024” at “yourgreatsite.com/blog/best-seo-courses-in-2024.”

If you update the blog post in 2025, you might want to remove the year and publish it under “yourgreatsite.com/blog/best-seo-courses.”

Changing the URL makes the old URL inaccessible.

However, some users may have bookmarked the old URL or shared it on social media. The old URL may also still appear on [search engine results pages (SERPs)](https://www.semrush.com/blog/serp/) for some time.

If users click on the old URL without being redirected, they’ll see a 404 error response.

![A browser with the url “yourgreatsite.com/blog/best-golf-courses-in-michigan-2023” in the browser bar and “Whoops! 404” displayed on the webpage](https://static.semrush.com/blog/uploads/media/f7/a3/f7a346d42a5812ca66856a9703fdff10/a30738bcb92ac33f88ce343d24bf7b3c/AD_4nXeULyCEjULMJy0aZGl4J61dKgy3xw8nsSUymmBWQ5aW09mFHAj8AjhIrp1ABVUm-VoXCMHStSyR-a-Ce4NfXgaGmwwsU8L9kKJ1LUjzWxlEnJ11VmbX5l21Xvakf3A4vef_4BR8vw.png)

If visitors expect a certain page and end up on an error page instead, they’ll likely have a poor experience and leave.

Use redirects to prevent confusion or frustration.

Before setting a redirect, ensure the old page has a meaningful replacement. If there’s truly no relevant replacement, provide an informative 404 page.

### Redirects Can Preserve Search Performance

Redirects can transfer ranking authority from an old page to a newer version to maintain rankings and traffic.

Imagine that the old URL “yourgreatsite.com/blog/best-seo-courses-in-2024” accumulated numerous backlinks and consistently brought in a large volume of monthly traffic.

By applying a redirect to a newer, updated page, you can effectively transfer the original page’s ranking signals and traffic value to its replacement.

## When to Use Redirects

Sites typically use redirects in the following situations:

- Moving a webpage’s URL (from URL A to URL B)
- Deleting a page
- Adding category tags or parent pages that change URLs
- Migrating a website to a new domain
- Adjusting URL naming conventions
- Merging two or more duplicate webpages
- Switching a site [from HTTP to HTTPS](https://www.semrush.com/blog/redirect-http-to-https/)

You can apply a web redirect to a single URL, a group of URLs, or an entire domain.

## Types of Redirects

There are two main types of redirects—**permanent** and **temporary**—that serve different purposes.

Users can’t tell the difference. However, search engines treat permanent and temporary redirects differently.

Use **permanent redirects** when you don’t expect to display the old page again (e.g., use a permanent redirect if you combine duplicate pages). Permanent redirects tell search engines to remove the old URL from search results and display the new one.

Use **temporary redirects** when a webpage only needs to be redirected for a short period. For instance, if you have a page dedicated to a limited-time holiday sale or a one-off event, you can temporarily redirect visitors to an alternate page once the sale or event concludes.

Now, we’ll examine the main redirect types:

### HTTP Redirects

HTTP redirects use a special code in the HTTP response that instructs the browser to go to a different webpage.

The redirection process works like this:

The browser requests the old (redirected) URL, and the server automatically displays the webpage for the new URL (the redirect target).

From the user’s perspective, HTTP redirects are seamless.

Technically, HTTP redirects are **server-side redirects**. The web server handles the redirect **before** the website loads.

The server returns a 3xx HTTP code when it receives a request for the redirected URL. These 3xx codes instruct the browser that the requested URL has been redirected and indicate the new page’s location.

Common 3xx codes include:

#### 301 Redirects (Moved Permanently)

[301 redirects](https://www.semrush.com/blog/301-redirects/) tell search engines that the move from one URL to another is permanent, which helps to pass link equity and preserve the original URL’s ranking strength.

For example, consider a site with two pages about a similar topic. If one page is outdated, there’s no need to keep both pages.

![old page redirects to new page at different url](https://static.semrush.com/blog/uploads/media/72/63/726330f3fce155161907401fda588cb2/14e75e5d4c59f2f5b0c2326095c41bf8/AD_4nXfl_TG5QUg9dyR6ySRI-bvxSXaJQAX1pmGDJrYRMLVFKsu0vcKF9yjd4FHEMHqIjAuQLkqkkrgG99rKlHbz9fNk3nKXlu6dKYKxss20KbtsVzMoDkI0Vwmp60DtNF51Ve53BkpK.png)

In the case of having duplicate pages where one is outdated, delete the outdated page and use a 301 redirect to the new page’s URL.

#### 302 Redirects (Found & Moved Temporarily)

[302 redirects](https://www.semrush.com/blog/302-redirect/) tell search engines that the redirect is temporary.

Use a 302 redirect in these cases:

- You temporarily move a page to a new URL
- You need to take a page offline briefly for maintenance
- You want to A/B test new design or copy

Google will [continue to index](https://developers.google.com/search/docs/crawling-indexing/301-redirects#temporary-server-side-redirects) the original URL, and the redirect won’t pass ranking strength to the new page.

Because ranking strength doesn’t transfer to the new page, using a temporary redirect by mistake can harm search rankings.

Check for redirect issues by running a site audit with [Site Audit.](https://www.semrush.com/siteaudit/)

Go to the “**Issues**” tab and type “redirect” into the search bar to see the number of URLs with temporary redirects.

![Results for "redirect" under the "Issues” tab in Site Audit](https://static.semrush.com/blog/uploads/media/97/21/9721da89e6526857fe7d943a71ca6031/59e707b9a7175553f042b5538248ee9c/AD_4nXd4kuXu0U6Sdoe_QIdlI7lPULqRgAnFXJEY7-LZU4wecNbPpY6g1NXCaWjalmkLrNpAGPW1V_YnLPn1R_3-JJDHAT5WR4Vzuw9RGLTHuM_RCWcr1NuTEOXe0954HMxKKhm4ehfbsw.png)

Review the affected URLs to confirm if they should remain temporary redirects.

Only use a 302 redirect if you intend to restore the original URL later.

If you’ve used a 302 redirect accidentally, change it to a 301 redirect.

#### Other HTTP Redirects

In most cases, only 301 and 302 redirects are needed, but there are some less common HTTP redirects:

- **303 redirect (see other)**: Sends users to another relevant page when the old one is unavailable, often after a user has completed a form submission
- [**307 redirect**](https://www.semrush.com/blog/307-redirect/) **(moved temporarily) and** [**308 redirect**](https://www.semrush.com/blog/308-permanent-redirect/) **(moved permanently)**: Similar to 302 and 301 respectively. These two types of redirects were primarily needed for older browsers.

### Meta Refresh Redirects

Meta refresh redirects occur at the page level (client side)—not at the server level like HTTP requests.

If you need to implement redirects, use HTTP redirects instead of meta refreshes whenever possible for better SEO.

Meta refresh redirects are often slower and can hurt the user experience. These redirects can also cause search engines to index the wrong page.

Google recommends meta refresh redirects only if you [can’t use a server-side redirect](https://developers.google.com/search/docs/crawling-indexing/301-redirects#metarefresh).

There are two types of meta refresh redirects:

#### Instant Meta Refresh Redirects

Instant meta refresh redirects trigger as soon as the browser loads the page, and Google treats these as permanent redirects.

Instant meta refresh redirects look like this:

`<meta http-equiv="refresh" content="0; url=https://www.semrush.com/">`

#### Delayed Meta Refresh Redirects

Delayed meta refresh redirects trigger after a specified number of seconds, and Google treats these as temporary redirects.

Here is an example delayed meta refresh redirect that triggers after five seconds:

`<meta http-equiv="refresh" content="5; url=https://www.semrush.com/">`

### JavaScript Redirects

[JavaScript redirects](https://www.semrush.com/blog/javascript-redirect/) are another type of client-side redirect but aren’t recommended for SEO because Google may fail to [render the JavaScript](https://www.semrush.com/blog/js-rendering/) on the page or encounter errors when doing so.

If the code doesn’t render or there’s another issue, Google may not notice the redirect and could continue indexing the outdated URL. If the old URL is the one indexed, it could continue to appear in search results and possibly harm your search rankings.

In fact, Google explicitly advises against using JavaScript redirects:

![Google says "only use javascript redirects if you can't do server-side or meta refresh redirects. while google attempts to render every url googlebot crawled, rendering may fail for various reasons. this means that if you set a javascript redirect, google might never see it if rendering of the content failed.](https://static.semrush.com/blog/uploads/media/39/d3/39d3dfa508bb7059484d4e42a19b5d62/f3c07ec89aa29ecfe67a897661a44803/AD_4nXd5omVQGnqUiJ7pj4-FDOewwbIJofSKmVMbng0WtSzOA5l9iG7oP_kAF96bmbSLLpzc9krjD2MEUTiLPyJ11U617wkYPifdFwSWNbJo3XUqC7ntaJd9cNl8VuWXh1eCRUZVXmyxpw.png)

Here’s an example of a JavaScript redirect in HTML code:

`window.location.replace("https://example.com");`

## How to Implement Redirects

You can set up HTTP redirects in several ways, including the below options:

### Use WordPress Plugins

You can use plugins like [Yoast](https://wordpress.org/plugins/wordpress-seo/) to set up [redirects on WordPress](https://www.semrush.com/blog/wordpress-redirects/).

First, download the Yoast plugin from the WordPress store and activate it.

Next, select “**Redirects**” from the Yoast menu:

![Yoast SEO in WordPress toolbar and Redirects highlighted](https://static.semrush.com/blog/uploads/media/1e/54/1e54b9f2707efde2919d82b3d0b8ab2e/1a5b760a5b83309808a4bf14a3df32ce/AD_4nXfd6V8Po_Iev5VkkX2brrMw552l0IODBIYlpdRXS8kj50myH4KS_eHhSpJ8hnKu93FMDszezs3KxIwtyflR9uOmmcJX-Tv3LQddtuXT1dXywE-AhEXge4CHeyx96GvmdeLXCRuhMQ.png)

Choose the type of redirect you want to use.

Enter the slug (the end portion of the URL) of the old URL and the new URL you want to redirect to.

Make sure you spell the slugs correctly. Otherwise, the redirect may fail.

Click “**Add Redirect**” to activate the redirect.

### Use Wix

If you use Wix, set up redirects directly in the CMS.

Scroll down to the bottom of your website’s control panel and click on “**SEO**” under “Website & SEO.”

![Wix SEO in navigation](https://static.semrush.com/blog/uploads/media/a7/fc/a7fc4762de7f20bde46a88075c590f75/099eeb768bb01924a8a4bb8aaa570981/AD_4nXcVle52FOJhEZMoBYYvusfK9FxgkMwUqAN4XoJhSksoPdA6xLdKoi7Rg31wYRW0Wee1NSRAyfxN3qgjsd9udXD6YKFHcctAqsz1asvME4pllwfcSAYBMF4yIgLKVHE-ILbdwp3V.png)

Scroll down and click “**Go to URL Redirect Manager**” under the “URL Redirect Manager” option.

![URL Redirect Manager highlighted](https://static.semrush.com/blog/uploads/media/19/23/1923c92f43b2c8719b8e232c9aa8bb20/9b29099edb3f9f108376faefb225afe4/AD_4nXclak6V8xid1a3TSFxdpfZR-PuBVQqyLNpkDvdBHbAB8GUvhC49IPuA3bmcR7L5LKTjMU2_wRKrpcKTc7edsfgI8saaQw5RZHm4ibVCnOI--J7UUka2PVvDMQ5L8R028RNBEsSj.png)

Click “**+ Create New Redirect**.”

A pop-up will appear.

Select your redirect type, add the old URL, and add the target URL.

Click “**Save**” or “**Save & Add Another**” to finish.

![Wix add redirect pop up](https://static.semrush.com/blog/uploads/media/89/e1/89e15dc12f469082fb09f2275ae07391/357c74a8716bf0ed02e1e663c96f1e0d/AD_4nXek15qWyM6blvRpiarjV9xgFq824hTTSntBe-8K_GC5c9SIhB-3BcsGitqCJgmnHvIlKQyDVl7mMY62OjYn9opwnT6eZKR5rDztP188TzJjLciaPgbXy17YnbRtwsUuFPmNoSQfuA.png)

### Use an .htaccess File

You can also set up redirects manually using an [.htaccess file](https://www.semrush.com/blog/301-redirect-htaccess/).

This file uses plain text and may look like the below image:

![.htaccess file example](https://static.semrush.com/blog/uploads/media/d4/e5/d4e5b067a06711ee3ff1ea1b537f6434/a4898ff1f55d54b077b44a0aa67b8d2b/AD_4nXdY3GsO9vHU0eVlFbo6VZbTHLf7mSNiy8QXAIkqW2r0_aON6mlFQfo5mCXX4l5s4k58uSJzVMaZQo7jt2aD9ALR21_vna-HZdPwfH63W4OKLuzEkK3PIKvVs9tqgBy-vROh9_9HXA.jpeg)

Apache servers use .htaccess files (though other servers can, too).

First, locate the RewriteEngine in the [mod\_rewrite module](https://httpd.apache.org/docs/current/mod/mod_rewrite.html) (in Apache).

This module should be enabled by default. If not, add it with the below code:

`<IfModule mod_rewrite.c>
RewriteEngine On
</IfModule>`

Place your redirect rules directly below “RewriteEngine On.”

#### Redirect a Single URL

To redirect one URL, specify the redirect type and replace “/oldpage/” and “/newpage/” with the actual page slugs:

`Redirect 301 /oldpage/ https://www.example.com/newpage/`

#### Redirect a Single Folder

To redirect a folder, use the below code and replace “folder” and “location” with your desired values:

`RewriteRule ^folder/(.*)$ /location/$1 [R=301,NC,L]`

#### Redirect to Another Domain

To redirect to a new domain, use this code:

`RewriteRule ^(.*)$ http://www.example.com/$1 [R=301,L]`

#### Redirect Non-WWW to WWW

Redirect non-www URLs to their www versions to indicate that the www versions are correct.

Redirect a non-www URL to a www URL using this code:

`RewriteCond %{HTTP_HOST} !^www\. [NC]
RewriteRule ^(.*)$ http://www.%{HTTP_HOST}/$1 [R=301,L]`

Choosing a single, consistent version (www) helps Google understand which version is canonical.

#### Redirect WWW to Non-WWW

Use this code if you prefer non-www URLs:

`RewriteCond %{HTTP_HOST} ^www\.(.*)$ [NC]
RewriteRule ^(.*)$ http://%1/$1 [R=301,L]`

Non-www URLs may be simpler for users to type. However, using non-www may limit your control over certain cookies.

#### Redirect HTTP to HTTPS

To redirect [HTTP pages to HTTPS pages](https://www.semrush.com/blog/redirect-http-to-https/), use this code:

`RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://www.example.com/$1 [R=301,L]`

Before redirecting from HTTP to HTTPS, make sure you’ve purchased and implemented a secure sockets layer (SSL) certificate.

## 5 Redirect Best Practices

We’ve covered how to set up various redirects.

Now, let’s discuss best practices for redirects:

### 1. Redirect to Content That’s a Close Match

When you set up a redirect, ensure the new page’s content closely matches the old page’s content and satisfies the same user intent.

If no close match exists, use a 404 page instead.

See what Google’s John Mueller says about whether 404 errors should always be redirected:

![Youtube video thumbnail](https://i.ytimg.com/vi/Fj42gKDQxYI/hq720.jpg)

"If the user clicked on your site in search of a knife, they would be frustrated to only see spoons. It's a terrible user experience, and doesn't help in search."

Not following this guideline can lead Google to treat a page as a soft 404.

A soft 404 usually happens when the server sends a “200 OK” [status code](https://www.semrush.com/blog/http-status-codes/), but the page contains a “webpage not found” message.

Google can also treat a redirected page as a soft 404 if the new page is irrelevant.

You can identify soft 404s using Google Search Console.

Go to the “**Pages**” tab under “**Indexing**.”

![Google Search Console Pages report](https://static.semrush.com/blog/uploads/media/13/97/13977b7b1f61832236c337660efd0201/69ed4f8f64a6ffec07a676e5d865160a/AD_4nXch1vYabjggZIQS_ouclJHRTawZH1pCmsjXOML0xIe3u_3UEf_LwG-C4s1PMMw2w9YSlTmnl6H304xfUYGuRUqU8oFRvkXnf7rmn0mYyY8Usj2wxNAvCIJJneYVOe-jeoPL1QY9Jg.png)

Scroll down to “Why pages aren’t indexed” and look for “Soft 404” in the “Reason” column.

![soft 404 error highlighted](https://static.semrush.com/blog/uploads/media/ef/85/ef85f1b0bf611ac7014f2a9b18321f2c/477068c31f2e860472e503ffef1fe23d/AD_4nXfmMQNz51Jg79r41ntFOgNy0AM6Z67mw4hNSoYwiOU9oTvdBKMLBPXsrn5857JCehK5wD5qUHvLTczZoJneqSQPkz8NFMJb6NF_0ChADwE3XbPpwZh3GEQcGSonpmT6CEltb0H-.png)

Fix the soft 404 errors you find.

If any soft 404 relates to redirects, update the redirect to point to a relevant page.

### 2. Avoid Redirect Chains & Loops

A **redirect chain** occurs when more than one redirect exists between the original URL and the final URL.

For example, if “www.yoursite.com/about-the-company/” redirects to “www.yoursite.com/about-us/” and “www.yoursite.com/about-us/” later redirects to “www.yoursite.com/about/,” you have a chain.

![a redirect chain example shows url a redirects to url b which redirects to url c](https://static.semrush.com/blog/uploads/media/15/c9/15c94ed29ab39a248709103847446b67/693a1e18b29d96853078d9066b47d821/AD_4nXfLQ0BEdNjuU40M6whSGAzw4GZMm36nwwZm9WhExa37mHVysHeHfLNDETo8iLflL8Q_0tYk_1l0tWLVun6mWHy6KscitQzzADZkbj_zU_ZPpKxeF8UQqjKwFrRv87bYmGJoc27qjA.jpeg)

[Google can follow](https://developers.google.com/search/docs/crawling-indexing/http-network-errors#http-status-codes) about 10 redirect “hops,” but long chains can delay crawling, lead to losses in link equity, and slow page load time.

Fix chains by redirecting the original URL directly to the final URL.

![Corrected redirect chain with both url a and url b redirecting to url c](https://static.semrush.com/blog/uploads/media/55/3f/553ffa5c116fcdf2f597e3db45a2e62c/fda838c3de824b99eb46538bff45e81c/AD_4nXfiDrnseiXeHMKU7utkyGVioVF5LEGE2TizIC8M-G53qhPXbaFmv_T7zA-UZnsQL5PdOp6IlxRQgVSvByYdqMR5PU2bl67nI8fNhcGwRyApUV7HQxIQGJ9zTSi0Ij1XAN_X-Vl8ww.jpeg)

A **redirect loop** happens when the first URL redirects to the second URL and the second URL redirects back to the first URL, creating an infinite cycle.

![Redirect loop shows url x redirects to url y which redirects to url x](https://static.semrush.com/blog/uploads/media/72/3a/723a036079c3283948ef373d2ff94361/898590a60de3c610f864647286e104d1/AD_4nXdeDfKYMmyWpTezCj27ZncbT0tO_Nj62oD2u1orGZqxYwQ4IKOTLfg1qBkXehwc45M39BTmTuw-lDAnoVdOX-W8PHnUeTTov79A91L-eSJiue6GzhQAVqSnQMMI4OqBn3Oypo-oRw.jpeg)

This loop prevents the redirect from working.

Fix redirect loops by choosing the correct final page and ensuring that the final page doesn’t redirect elsewhere.

Use [Site Audit](https://www.semrush.com/siteaudit/) to identify redirect chains and loops.

Open the “**Issues**” tab and search “redirect chain.”

Click on the “**# redirect chains and loops**” issue to get a full report of pages with redirect chain or loop errors.

![Redirect chains and loops in Site Audit](https://static.semrush.com/blog/uploads/media/ff/78/ff78211260b01e25f4df37ca27b8c903/a004f09ec54b91a489ecbcd6fa08b9ff/AD_4nXe1c2Y7fxmCPxMmZrFvCa0hy4hIuR_YmThv2YBQa_6mTFel79Pwe3tOA-dV_q3CcgjGqsmheGpwytdW2YjRAdlkuB87hALqspPg7hz8Il4J3j8OrrtiyPzMC_2YJQl_D-970g2Thg.jpeg)

The report contains a list of pages, their redirect type, and the number of redirects.

![List of page urls with redirect link in Site Audit](https://static.semrush.com/blog/uploads/media/69/4c/694c74f574a9711af7a503713b1af97d/2632d739e4e062a0c92a404b99ca174d/AD_4nXcRIA6I937jX8-2596GprVH9wY5nuobZhwZ07qThDUksV7QeEbR6O6FpnSBBXVWFnqXCvgmhtMJHlFF9VEEAkP9fVJkH4DNoJTps36f47ARA8zPlaJbeOUz7ntlydzt9qMptLPxHw.jpeg)

Fix each redirect issue in your CMS

To summarize:

- **Fix chains** by redirecting the old URL straight to the final URL.
- **Fix loops** by selecting the correct URL and removing other redirects

### 3. Avoid Linking to Redirected Pages

If you redirect an old page to a new page, check whether any internal links still point to the old URL because extra redirects add complexity and can cause chains (even if users don’t notice).

In other words, linking to a redirected page adds another (unnecessary) step:

![Linking to a page with a redirect shows blog post linking internally to an old page which redirects to the new page](https://static.semrush.com/blog/uploads/media/ae/6d/ae6db335846b9157a6a49812e82584aa/42fd4b7ccef47c8c84b85777224e541f/AD_4nXcECncoyxOAJS9b9DX6JBLxE9EEjjsHEh7dbj3SJRE4QQea88h5RyxGAGX_io6d3kan34Jn7_RuCmpvtegGl_dM8uz01j_qNbGv-QFq6bUaUGBsvR3IOEPdO5dn6UQ7vg4oYP0l.jpeg)

Update old internal links to point directly to the new URL.

![Avoid linking to a page that redirects to another. the blog post links internally to the new page](https://static.semrush.com/blog/uploads/media/27/b6/27b6682c6eee844f323ee57613f9f23a/3849f9ed950993716c931bdda48d4e75/AD_4nXd62XYF0G0xe96jy4W3scrKLzstQ2N5-jbTE9bLUNStZ2DIHd8M1eT_4JMLX5h5nxZHdBplPdBzilTMSl5zlisqaA9sWhjUlJLZ4hrdyBUv8Q-RaecLjc5Qpfz5O29O2SlBpVZwQA.jpeg)

To find links that point to redirected URLs, open [Site Audit](https://www.semrush.com/siteaudit/) and go to the “**Crawled Pages**” tab.

![Site Audit Crawled Pages report](https://static.semrush.com/blog/uploads/media/46/6a/466a01229d0da81abc9d2c889379bca4/0848f65fa8e97de5db9c0b2060836896/AD_4nXcEBHJu8UNCaL-Bas-mW1GT4W9VFzHh-IZoQaBymQLkr6hPMDXDuBCSzT-WduMjKw8deA_OBYLKuO7Y_NgFbMkOozR0QWSkHBC44cWiozHGRcp84QXlGrILHDQhxjnIR2CyhquZog.png)

Enter the old URL that’s been redirected into the search bar and click the search icon.

![Add your page to Crawled Pages search bar](https://static.semrush.com/blog/uploads/media/b0/18/b018487b1ab16c50407ca69722f7b54d/f5fd011978e48b98ed2f3928cc524df8/AD_4nXc8S-6q82VvEext0h3I2Q__PPlEFi0ssKSYtfQUR-tb8onLQ2Mltz3PXx7Rmw8GZ1azBbcBCP8jxv3R9WU1UbBByzB8vulCIrUYb2e2Tvv_Y12WAknXndsdHh8ewOmx0V1Sc6_S.png)

Click the old URL in the report.

![Crawled Pages report for one redirected URL](https://static.semrush.com/blog/uploads/media/ac/a9/aca9fc5832006b75d4edb5e33396fe7c/e376e066a45b48416703f19844b2328d/AD_4nXdVBUps3gjYOH7-IFuLZPx1w--lsYh45w6-CYnkoJVRempmju_ot0m38FyQ5zsGimYlD2Cg78Ov6v-DAmS0cQkkHoRlu13ObtYVsomI6wreF1kFMw24hiB3gMs4IfJ_hylSvHUOcQ.png)

Click the number under “Incoming Internal Links” to see all the internal links pointing to your old URL and update them to the new URL.

### 4. Redirect to Avoid Duplicate Content

Sites often have multiple versions of the same page, which can cause [duplicate content](https://www.semrush.com/blog/duplicate-content/) issues because search engines treat those different versions as being different sites.

For example, “http://example.com” and “https://example.com.”

Prevent duplicate content problems by using 301 redirects to point all variants to a single, preferred URL.

Use redirects to handle the following scenarios that may otherwise lead to duplicate content issues:

- Non-www and www URLs
- HTTP and HTTPS URLs
- Trailing-slash (/) and non-trailing-slash URLs
- Capitalized and lower-case URLs

Find duplicate content in the [Site Audit](https://www.semrush.com/siteaudit/) tool’s “**Issues**” tab.

Type “duplicate” in the search bar to find relevant errors.

Click the “**# pages have duplicate content issues**” error for details.

![Pages with duplicate content issues](https://static.semrush.com/blog/uploads/media/56/8f/568fa986a4da3a37126e8b463a2d4d9a/55df0065a4d90131347a144b80fca081/AD_4nXcFNtYEWHCm9m629-n-v9ZatmEv82WKrasDPm6He0WUwathXVR4QTPrDPyDqsSxpS59ck03vLSSLs8_aP_Q3ca7pZ3Iwxx_OcXsVwLIFGVi1R0ht7cGjWOtGQgRR_6jHaDa5ltX0A.jpeg)

You’ll see a list of pages that you may need to redirect and how many duplicate pages exist.

![Page URLs with duplicate content issues in Site Audit](https://static.semrush.com/blog/uploads/media/4f/bf/4fbf214814ad3b8182fb96f82c7d9a5c/b53f808d319945fd937fd4ae5c0e1262/AD_4nXe5G1_IDsvlH_MLtN2mmkBSOq_Owtl5ItNeRulqk9iSzDfWBOLAc5mondOHhxm4zaZYHpnGSqRSA2pIlr7iiqamKDm3DcB4CxbPEk4Ab_bJp_AW9WXmzlOG7Bo7SvmWV6B-yv7FUw.jpeg)

Click on the drop-down arrow on the right side of each listing to see the duplicate pages.

![Examples of pages with duplicate content](https://static.semrush.com/blog/uploads/media/cd/75/cd75ce9eb78b2260e0cb8c5078065467/1a0e9b21b6cce46c248da65a8eb4392d/AD_4nXcQCzgwGs3VGf30IfIeGHf0QQmyxcaZPZjICWSEQl-4Xw_ofd-CoGmcjDZ8Mowgyu9lxnZovLuPmwo6EWYPHud0apbqafgwfvk2nR3jQSFgF8BWfBOt5FRt-yUwyc2d_euxRnFomQ.jpeg)

Redirect each duplicate page as needed.

### 5. Fix 404s to Regain Lost Link Authority

Google ignores backlinks pointing to 404 pages, and these lost links mean lost ranking authority.

Use [Backlinks](https://www.semrush.com/analytics/backlinks/) to find 404 pages with inbound links pointing to them.

Go to the “**Indexed Pages**” tab and check the box beside “Broken Pages.”

![Broken Pages in Backlink Analytic's indexed pages report](https://static.semrush.com/blog/uploads/media/42/a4/42a4ac6caaad12f8a03f4d8f84ae9ec6/8820c70b1925863c7c6e19e1d849abf7/AD_4nXd8NJt1x_U8PlhI2NGIx00xLk_JkylBtH8CHQGekyJrIdDfSfi-Fwipj9iU-AQGxOBSRZuJdlZSi5-yTd_nDv1yGNXhBg97wBo5fN1UYT5y2GOCgb96DKTbr-KKkyRcAiOt1V9Y.png)

You’ll see a list of missing URLs that have links going to them.

![redirect errors in broken indexed pages with internal links noted](https://static.semrush.com/blog/uploads/media/07/a7/07a70a1f3a356e3c02bf54eba2d3357d/83a2fd4b93dc7728520458de278b87b3/AD_4nXfuqMtANKg5lZPKY47fXPJL82HBwmXZQPPsbu7DXSGDmNwR2CR4Qm4SPXn2-xYSUdFb4o0FIuzxlCCinAyKc6F495Zvn9tKb85ruUIhnSQSsxA-ZvHS7R_S7ykmiL-qiJFn8CYKfg.png)

Use 301 redirects to point the missing URLs to relevant pages that closely match the old content to reclaim lost authority.

## Redirect FAQs

### Do Redirects Pass Page Authority?

Yes, permanent redirects can pass authority from the old page to the new page if their content closely matches.

However, a redirect may not pass 100% of the original page’s authority.

If you have a good reason to redirect a page, implementing the redirect is best practice.

### Are Redirects Bad for SEO?

No, redirects aren’t inherently bad for SEO.

Google’s guideline is simple:

- If the old page no longer exists and has no suitable replacement, don’t redirect
- If the page moved to a new location, a redirect makes sense

If you redirect users to an irrelevant page, Google may treat it like a 404.

### How Long Should You Keep Redirects in Place?

Google recommends keeping 301 redirects in place for at least one year.

In a [video from Google Search Central](https://www.youtube.com/watch?v=ml7cQHkUc2Q&t=40s), John Mueller from Google said:

> When a URL changes, our systems need to see the change in the form of a redirect for at least a few times in order to record that change. To be certain that a redirect has been seen a few times, we recommend keeping the redirect in place for at least one year.

For users, keeping redirects indefinitely is best for ensuring users never encounter errors that cause them to leave your site.

### How Do I Test Redirects?

You test redirects by copying the old URL, pasting it into your browser, and hitting enter to see if you’re taken to the new URL.

If so, the redirect works.

If not, check for typos or errors in your redirect setup.
