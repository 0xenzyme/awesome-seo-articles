---
title: "How to Set Up 301 Redirects in an .htaccess File"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "301-redirect-htaccess"
url: "https://www.semrush.com/blog/301-redirect-htaccess/"
canonical: "https://www.semrush.com/blog/301-redirect-htaccess/"
author: "Connor Lahey, Christine Skopec"
published: "2021-09-17T14:20:00+00:00"
updated: "2025-06-03T10:41:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T13:16:10+00:00"
status_code: 200
html_hash: "2ac2b94888b70de27482e8c48afadacd62c1f463a1265a9ffc5f0839a6482173"
clean_word_count: 1673
clean_char_count: 12275
---
# How to Set Up 301 Redirects in an .htaccess File

Implementing a 301 redirect in your [.htaccess file](https://www.semrush.com/blog/htaccess-file/) (a text file for configuring aspects of websites hosted on Apache servers) is a useful way to permanently redirect one URL to another in a way that preserves ranking authority.

Using .htaccess files to implement 301 redirects lets you execute complex patterns, like pattern-based redirects (redirects that automatically match and forward groups of similar URLs using a single rule).

## When to Use a 301 Redirect

Use a 301 redirect any time you need to send users to a different page and want to keep your traffic and SEO intact.

Some of the most common scenarios for 301 redirects are when you're consolidating duplicate pages into one main page and when you're migrating from [HTTP to HTTPS](https://www.semrush.com/blog/http-vs-https/).

Here are some others:

### Fixing Keyword Cannibalization

Implementing 301 redirects can be a good way to address [keyword cannibalization](https://www.semrush.com/blog/keyword-cannibalization-guide/): when multiple pages compete for the same keyword, which can hurt your rankings.

[Alex Meyerhans](https://www.linkedin.com/in/alexmeyerhans/), CEO of Meyer Digital Media, recommends merging the content into one page and using a 301 redirect to point the old page to the new one when other optimization efforts haven’t worked:

> Sometimes you can fix keyword cannibalization via on-page optimization to de-optimize the page that shouldn't rank. And many times, that solves keyword cannibalization. But sometimes it won't. Then, it's time to merge the content from the offending page into the desired one, and 301 that page.

### Preserving SEO from Outdated Pages

Using a 301 redirect to send traffic and search engines from outdated pages with strong backlinks to new pages is helpful for maintaining the original pages’ rankings.

SEO Specialist [Artturi Jalli](https://www.linkedin.com/in/artturi-jalli-29619413a/) shares an example:

> If you had a ‘Black Friday 2024’ page and now focus on ‘Black Friday 2025,’ a 301 from the old to the new ensures link equity and continuity.

### Improving UX and SEO for Tag or Category Pages

Redirecting default tag/category pages to curated landing pages can improve [SEO and user experience](https://www.semrush.com/blog/ux-and-seo/) (UX).

[Cameron Martel](https://www.linkedin.com/in/cameronmartel/), Managing Partner at Monochrome Marketing and CMO of FutureFund, suggests doing this.

> Tags/categories are often featured prominently in website UX (top of posts, blog feeds, etc.), but typically lead to experiences that are sub-optimal for ranking. By 301ing these URLs to custom landing pages, we can better control user experience and improve internal traffic flow to landing pages.

### Deleting a Page

If you remove a page from your site, a 301 redirect sends visitors to a related page to help maintain the user experience.

However, if there’s no relevant page to redirect visitors to, it might be better to serve a 404 or 410 instead of misleading Google and users.

## How to Use a Hosting Panel to Set Up a 301 Redirect with an .htaccess File

Two common ways to set up 301 redirects are through your hosting panel (like cPanel) or with a file transfer protocol (FTP) client. The latter is more advanced.

We’ll walk through using cPanel.

### 1. Find the .htaccess File

The .htaccess file is usually located in the root folder—the main directory—of your website.

To get there in cPanel, first click “**File Manager**.”

!["File Manager" clicked on cPanel.](https://static.semrush.com/blog/uploads/media/0b/4e/0b4e0f1bb10405b9de4dbcc68ba77230/82e4738db35d97a07dde9d2aeb00c5bd/AD_4nXeLSm4qf696SDGQCpkaDSafVaKNSPS3MX0IavatHsV5eyiQ1fTOivfnTri9KQxYKBRF5HXjdGBRuMETuOi885Pk2bJWVeHmIHp9MWfjbilDUaBG95XIpSnk8puuBuP_QdCshUexsw.png)

Find and open your site’s root folder (often titled “public\_html”).

![A site's root folder opened by clicking "public_html" on File Manager.](https://static.semrush.com/blog/uploads/media/6f/0c/6f0ce2d98078bc669117d6e18077df55/8bb8f93406a95504166e81aa7aac3615/AD_4nXeQY9teGxHUOJjt_8DXCcpIzBAJ0XpNLvNy0577V8D9My9FoURju_GLOPu_mKb8Mr1UAdpugsVdtUPrX-3yqS31GgsKncHX3CVvm5FnAEgT4poEg1sU7ALjStScKlHtIrICqDxKNw.png)

Locate your .htaccess file, right click, and select “**Edit**.”

![".htaccess" clicked and "Edit" selected from the window.](https://static.semrush.com/blog/uploads/media/2c/0a/2c0a6798bd4273c9cf4cbafd8638724f/e8e610be790078dcdb3bb9d10bf89f98/AD_4nXc3G4DL6s0OKhbKh07r3kZ4-P-tRuKbBCvY6RKUF5TrpT9cLmvyqvygGBFbEBSnvUkd9Eda4270gQJCVUHAn4wJyWjnpIVdjn1lzstX1AoidwTAEU41mhgDdoCBW5dG480PFzT-.png)

### 2. Edit and Save the .htaccess File

Redirects only work if the rewrite engine (a feature in Apache that allows redirects) is turned on.

Look for the following code near the top of the file. Or add it to your .htaccess file if it’s not already there:

`<IfModule mod_rewrite.c>
RewriteEngine On
</IfModule>`

Then, write any redirect rules below “RewriteEngine On” but above “</IfModule> (we’ll go over a few options later). And save the .htaccess file to apply your redirects.

## How to Use a WordPress Plugin to Set Up a 301 Redirect with an .htaccess File

You can access your .htaccess file and set up [redirects directly in WordPress](https://www.semrush.com/blog/wordpress-redirects/) using a plugin as long as your site runs on Apache.

We’ll show how to do this using the [Yoast SEO](https://yoast.com/wordpress/plugins/seo/) plugin.

### 1. Install Yoast

Head to your plugins and search for “Yoast.”

Click “**Install Now**” and then “**Activate**.”

![WordPress plugins library with "yoast" entered and "Install Now" clicked next to the Yoast SEO plugin.](https://static.semrush.com/blog/uploads/media/b1/52/b1523041354f80753d0c29c5d24fd3a2/24f3af80ab62be515439939d46a41b0e/AD_4nXfuH50UqGgY0yBXfhiIQGysqpXTceTYnEavXQsy2d9wkiEsIijaJ4slpk14RAxAFKZu92WBgx02Ek5D_ASx-DdHiVNEAZ5fo5KvJBjKcWgrNwKhj1H7rn1GtvEyf8cfBaPj3GmYGQ.jpeg)

### 2. Locate Your .htaccess File

Yoast lets you access your .htaccess file within your WordPress dashboard.

Go to “**Yoast SEO**,” select “**Tools**,” and click “**File editor**.”

!["File editor" clicked from the "Tools" tab on Yoast SEO.](https://static.semrush.com/blog/uploads/media/e8/39/e839913c0ce000b77b0f59b6c3ab34af/fc252af6f5dffe122c93a58101745e69/AD_4nXc8EkJ73iC9WnKf04t4ivrq56WOgIFADnX4wd-3uwi8d9S414r5vuDnxOmpsrgRx6rHyZRBjnkMCsTW2QqMTIqF3iUCwiEqRxTPOiuXRuxAXwKeo-Uk-z_MUtjv1z8PMVCF0yyJwQ.jpeg)

### 3. Edit and Save the .htaccess File

Check that the RewriteEngine is enabled and add the following code to your .htaccess file if not:

`<IfModule mod_rewrite.c>
RewriteEngine On
</IfModule>`

Add your redirect rules before the </IfModule> tag. You can add multiple rules within this block of code.

Then, click “**Save changes to .htaccess**” when you’re done.

![Code entered along with redirect rules on the ".htacess file" window using Yoast SEO.](https://static.semrush.com/blog/uploads/media/32/a4/32a4e513d2c70c87794c34298f99f0a8/a4580a63f0cc10a43caa9fd05d955de9/AD_4nXfP0_H9gs23VWq7eX3-4Bk6DjhsizsRrH9AVEdSqr_JLTVvEKOd8wygz-UQsQOx_GyoVPu9LT7eYMpE8t3Tpmrl9FU9DycRUbHnVx_VL_PsgJP0gkG7GzM0g7xLabHkUvCQ-MisfQ.jpeg)

## Common 301 Redirect Rules

Add these redirect rules into your .htaccess file to implement 301 redirects. Make sure to replace the placeholder URLs with your own.

### Redirecting a Single URL

Add this 301 redirect to your .htaccess file if you need to redirect one page to another.

`RewriteRule ^old-page/?$ https://www.yourdomain.com/new-page/ [R=301,L]`

### Redirecting a Single Folder

Use this rule when you need to redirect whole sections of your site (like redirecting “/blog” to “/news”).

`RewriteRule ^blog/(.*)$ /news/$1 [R=301,L]`

### Redirecting WWW to Non-WWW URLs

Redirecting www to non-www URLs helps prevent duplicate content issues by ensuring search engines don’t see www and non-www versions as separate pages with identical content.

`RewriteCond %{HTTP_HOST} ^www\.yourdomain\.com [NC]
RewriteRule ^(.*) https://yourdomain.com/$1 [R=301, L]`

### Redirecting a Website to a New Domain

Use this .htaccess rule to redirect your entire website to another domain.

`RewriteCond %{HTTP_HOST} ^old-domain\.com$ [OR]
RewriteCond %{HTTP_HOST} ^www\.old-domain\.com$
RewriteRule ^(.*)$ https://new-domain.com/$1 [R=301,L]`

### Redirecting HTTP to HTTPS

HTTPS (the encrypted version of HTTP) is a ranking factor, and forcing HTTP to HTTPS helps secure your site and improve your SEO.

`RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://yourdomain.com/$1 [R=301,L]`

## How to Check Your 301 Redirects and Fix Issues

Proper 301 redirects help you avoid [redirect chains and loops](https://www.semrush.com/blog/too-many-redirects/), broken links, and incorrect redirect types—like accidentally using a [302 redirect](https://www.semrush.com/blog/302-redirect/)—which leads to better SEO and a smoother experience for users.

Use Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool to check for redirect issues. And keep your redirects working as intended.

[Configure Site Audit](https://www.semrush.com/kb/539-configuring-site-audit) and open your project.

Click “**Issues**” and search “redirects.”

Look under “Errors,” “Warnings,” and “Notices” to check if your 301 redirects might be hurting your site. If there’s an issue, click the number beside the problem for more information.

![Issues tab on Site Audit with "redirects" entered and "4 redirect chains and loops" highlighted.](https://static.semrush.com/blog/uploads/media/48/c0/48c05febc926feea61e6c5232573cd75/e389cda95aec1a9160ce2aa77ee65b54/AD_4nXedxue4N0HGgNll1L1xvDdx_qMn-KeQDsy1jc3wGx2eDQ8TsZNCFMxVqkf0yF1_I8ZMjy8YfFjnfWajK7FHqS8b2r7GLLB8t49Wt1Jl5NZ9-wy58lDtVcr-jUg3VJ2Nuvlh1psF.jpeg)

Site Audit also tracks each redirect you set up. So you don’t need to manually track each one—and risk forgetting some.

On the Site Audit homepage under “Crawled Pages,” click the number beside “Redirects.”

![Site Audit Overview with the number next to Redirects under Crawled Pages clicked.](https://static.semrush.com/blog/uploads/media/84/f4/84f45164a66e67cf22e81f1dfc0b6586/70115831a63dc49e51784980181ca305/AD_4nXdcaPUIsfClGXTEPeJoHD4G_3WswXrfTVaGNLH4iE2XgHppt8AF7QOlHMWWZfzRQT94GS3oiOat1sOGp5YDt-CSYubf2VXG5bHJK3iWG9Co1-uFWgyGt2JzIGJna_74qwvTOnXI.jpeg)

You’ll see a list of pages with redirects.

![Crawled Pages on Site Audit showing a list of a domain's pages with redirects.](https://static.semrush.com/blog/uploads/media/ff/e3/ffe3f1969667ad3b863c7c218201d19e/ecc1904906e63d4690617dae8a3d59ea/AD_4nXe6bYJngYW1Ly0LR9P0tbWnxBEYzXn4egbcG_ql2f7pUkn11LmS8LhHz4CwcooNR_1y_qxw6zXJFIv-ZudF4Ng3pcf4DOVMEzFaSZI8kFu2fRhbTlSdqNOg4sQquzEb9q-dvHuuAA.jpeg)

Double-check that each redirected page is using the correct redirect type. Such as a 301 redirect for permanent moves instead of a 302 redirect for temporary moves.

## Stay on Top of Site Issues

Schedule regular audits to receive alerts whenever you have technical site issues. So you can fix issues and keep your SEO strong.

Click the gear icon and select the “**Schedule:**” option in the drop-down.

![The gear icon clicked and "Schedule:" selected from the drop-down on the Site Audit tool.](https://static.semrush.com/blog/uploads/media/be/45/be458e1832bb1fb819c1a6fca5438354/ee87f6fbceef82d84e8a5a92c88371ca/AD_4nXfN0V2VrWQRS7jjDSMi3PwT7EpQY4P1RxqSO9TGQbOnx2C2hcnvp0DuJXbBRbCR6yY4LwDUyj25Wd7oPa5qR6ShBGiAVv4COD77Q05LrKr4lsgRXEckyTZB15RP81hnPrbXO4UWNg.jpeg)

Select how often you’d like the audit to run. And check the box next to “Send an email every time an audit is complete” if you want email alerts. Click “**Save changes**.”

![Scheduling frequency selected, "Send an email once an audit is complete" checked, and "Save changes" clicked on Site Audit settings.](https://static.semrush.com/blog/uploads/media/6e/92/6e92b5ad940ce7daa5c155bd42ea4dd3/5d8cefcd3b27cb15f4caeb31d1a31bd9/AD_4nXcxBgcXk1TNO2qY8RMFZPhmvj22nMvA9lbaSs77QxT6HZBZxJSC0V1aNGrNqSMcx2QWA00LFfuxSwIL9wZA0-2K8I1yotu1yzjuxV1eGjjEIRTovpy1mxIufLExSuzKumKT7DDeHw.jpeg)

Now, you don’t need to manually check or track redirects. Site Audit does the heavy lifting for you.

Try Site Audit today.
