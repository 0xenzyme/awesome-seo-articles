---
title: "What’s a 302 Redirect? And When Should You (Actually) Use It?"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "302-redirect"
url: "https://www.semrush.com/blog/302-redirect/"
canonical: "https://www.semrush.com/blog/302-redirect/"
author: "Semrush Team"
published: "2023-07-17T09:16:00+00:00"
updated: "2023-07-17T09:16:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T13:17:12+00:00"
status_code: 200
html_hash: "401661fd191654c666460a118d0df2180af5e0c4f8627230c7d6d0d6c69db1ec"
clean_word_count: 4196
clean_char_count: 27907
---
# What’s a 302 Redirect? And When Should You (Actually) Use It?

A 302 redirect is a temporary way to divert users from one page on your site to a different page.

It’s important for SEO because it allows you to send traffic to a different page while maintaining the keyword rankings and link value of the original page.

In this guide, we’ll explain when, why, and how to use 302s properly.

## How Do 302 Redirects Work?

A 302 redirect is sort of like an out-of-office message.

It’s not a permanent change of address. But it helps make sure users and bots can still access your site if a specific page or resource is unavailable.

A 302 can improve user experience (UX) on your website by making sure users don’t land on pages that are outdated, missing functionality, or under construction.

This HTTP response status code (302 - Found) indicates a page has been moved. Anyone trying to access this page is automatically [redirected](https://www.semrush.com/blog/redirects/) to the new page while the 302 is in effect.

## 301 Redirects vs. 302 Redirects

Should you use a 301 or a 302 redirect? It's a common question.

Here's the difference:

**A [301 redirect](https://www.semrush.com/blog/301-redirects/) is a permanent redirect**.

**A 302 redirect is a temporary redirect**.

!["Do you need to implement a redirect?" infographic](https://static.semrush.com/blog/uploads/media/13/49/13490d6c02fec443fc29b78cb1340996/nG4lF8cOxsJMMZFlg1A_UkB2J4bOudufP3p7ZBIqEYNRx7ayMyaA89odP1jPZwSjfvXSCfXQGQ68SM8MtS5Ldk3QisSWrn-VKtT_yvWnla9Epm__VeCmJQXCXcYtLg6_R55Tl4dyGn0Wl3x2el7zYq4.png)

Implement a 301 redirect to make **permanent** changes to your website. For example, if you permanently move the content from **example.com/page-1** to **example.com/page-2**.

You want to tell users and search engine bots that your old page no longer exists and they can find the content at a new address.

Otherwise, a 302 redirection works for temporary use cases.

For example, you’d use a 302 for things like: A/B testing, temporary sale pages, or website maintenance.

We’ll cover more examples of [when to use a 302](#when-to-use-a-302-redirect) below.

### 302 vs. 301 for SEO

From an SEO perspective, 301 redirects are helpful for consolidating and preserving “link equity” or “link juice,” as it’s sometimes called. A 301 prompts search engines to treat backlinks pointing to the old page as if they now point to the new page.

Because of this, it’s best practice to use a 301 redirect for addressing SEO issues like combining duplicate content or making permanent URL changes.

But using a 302 instead is generally not catastrophic.

[Google treats both types of redirect](https://twitter.com/JohnMu/status/1380037034077794304) in almost the same way, according to Google Search Advocate John Mueller. They use other signals to determine if the original URL or the new URL should be canonical.

If it becomes clear that a “temporary redirect” is meant to be permanent, they can usually figure that out over time and treat it accordingly.

## When to Use a 302 Redirect

The most important word when it comes to 302 redirects?

**Temporary**.

If you’re ever unsure whether a 302 is the right choice, just ask yourself if you’re implementing a temporary change or a permanent change.

There’s no exact amount of time that constitutes “temporary.” But Google recommends using a permanent redirect when, “you're sure that the redirect won't be reverted.”

This means you likely should use a 302 in any other case.

For example:

### Website Maintenance or Redesign

You’re working on a big update to your page at **www.example.com/my-page** and don’t want anyone to see it before it’s ready.

Use a 302 redirect to send visitors elsewhere while it’s under construction.

### A/B Testing

You’re testing a new version of a landing page to see if it outperforms the existing page.

You’ll want to send a certain percentage of your traffic from the existing page (**example.com/page-1**) to the test version (**example.com/page-2**).

![infographic showing A/B Testing, where half of the traffic is sent to page A and other half of the traffic is sent to page B](https://static.semrush.com/blog/uploads/media/30/61/30611420dcf1817a32bbc999d0f41acb/FDTnsFcrn0cwIOxmjHRiEdHcfiy9YtQTyBbvTpjUqvyy215w6pWPqra3o5zaB8Xm9m9kZA0ln-jwzaYVFK2njXLeglzD2CIxqbiSmKbAJ_vIDwbmH3fzDWmDlMqWWpD8Pw2SzT2fH-YydJJe1jP5v6I.png)

Use a 302 redirect because this is a temporary experiment and the page hasn’t moved permanently.

### Temporary Promotional Pages

You’re running a limited-time sale and built a special page just for that purpose.

When someone clicks on “Shoes,” you want to send them to your new special promotion page (**example.com/shoe-sale**) while the sale is running.

Again: Temporary = 302.

(Just be sure to remove the redirect when the sale ends.)

### Live Testing

You’re creating a new website flow where users will take a different path to find information or perform an action. You want to test the new flow from the live website before it’s launched permanently.

Use a 302 to send traffic from **example.com/page** to **example.com/page-test** and get feedback or collect data temporarily.

Then either permanently redirect or replace the contents of the page once you’re ready to deploy this update.

## How to Implement a 302 Redirect

If you’ve read through these scenarios and determined that 302 is the right call, it’s time to implement it properly.

Be careful to follow the instructions closely and only make changes that you’re confident you can fix if something goes wrong!

### WordPress

Implementing a 302 [WordPress redirect](https://www.semrush.com/blog/wordpress-redirects/) is easy with the right plugin. But even without a plugin, you can implement them directly—with the right knowledge.

#### Yoast SEO Premium Plugin

The [Yoast SEO](https://yoast.com/) redirect manager allows you to quickly add or remove 302 redirects. You’ll need a Yoast Premium subscription.

![Redirects page in Yoast SEO](https://static.semrush.com/blog/uploads/media/1c/fb/1cfb122f36b4e9c54f216e6971e1df86/B1geX9VIR-o7s3EbKNowlpxb5hwEdTXiZEeg-jtSfp9F7fh2oORenk7MLfF3a4B34zD6cDduNOTWUu7R9XC3A34UxcnCYsXxEYNCC_WSDloJNXV6rTluOact_HQH1eQXNxQPJ2reZBdt8UtVG7cEXlk.png)

From the WordPress sidebar:

“**Yoast SEO**” > “**Redirects**.”

Then fill in the fields:

**Type** = 302

**Old** **URL** = The URL of the original page without the root domain (e.g., “/page-1”)

**URL** = The URL of the new page without the root domain (e.g., “/page-2”)

Click “**Add** **Redirect**.”

#### Redirection Plugin

[Redirection](https://wordpress.org/plugins/redirection/) is another extremely popular WordPress plugin that makes it simple to implement or remove 302s.

From the WordPress sidebar:

“**Tools**” > “**Redirection**.”

From the “Redirects” page, find the “Add new redirection” form.

![“Add new redirection” form in Yoast SEO](https://static.semrush.com/blog/uploads/media/94/7c/947c3ebc87001dd6506bd16d813f4bc4/46Zt77TvGC_qVHdpID46WQHgnw4wDiGjpxf9sbducBw1Jx-HT9G8ySNCCTrfeT7s6SuWO1k4RU1CbG0C8KMm_ozqa1ZK6NQcDsLKzxxmT-IKI8G6hi0Y-6SeUO0g1NqJsBRN1lbNejP1GUWubqg1tHk.png)

Fill in the fields:

**Source** **URL** = The URL of the original page without the root domain (e.g., “/page-1”)

**Target** **URL** = The URL of the new page without the root domain (e.g., “/page-2”)

**HTTP** **code** = 302

Then click “**Add** **Redirect**.”

#### Rank Math Plugin

[Rank Math](https://rankmath.com/) is another popular SEO plugin that makes it easy to implement a 302.

From the WordPress sidebar:

“**Rank** **Math**” > “**Redirections**.”

From the “Redirections” page, click “**Add** **New**.”

![“Add Redirections” page in Rank Math Plugin](https://static.semrush.com/blog/uploads/media/aa/74/aa745aeb5ea5acbf9635b1f05e04b051/R9vV_9sm093vCEh2vgKGNyHLNo0SaY2c2ucPqBmtNkvlI3B43583S_3--Yxy-kyDW0my9gFCS60LL5jN6UX844OgrgbvXDWhposJZBrX5I1olR-k3fnIFuhip7SfA-Kxpj1KbwBK-maecHJmuRu97R8.png)

**Source URLs** = The URL of the original page without the root domain (e.g., “/page-1”)

**Destination URL** = The URL of the new page without the root domain (e.g., “/page-2”)

**Redirection Type** = 302 Temporary Move

Then click “**Add** **Redirection**.”

#### PHP Redirects

***Warning:** This option will require you to edit your theme files and PHP code. It’s only recommended for advanced WordPress users comfortable with making these types of edits.*

If you don’t want to add one of these plugins, you can implement the redirect manually.

It’s possible to implement a 302 redirect either server side (see [Apache](#apache), [Nginx](#nginx), and [Windows Server](#windows-server-with-asp-net) options below) or directly in the PHP header.

You would add some code like this to the very top of your PHP header before any HTML or echo functions:

`<?php
// Check if the requested page is page-1
if ($_SERVER['REQUEST_URI'] === '/page-1') {
// Redirect from example.com/page-1 to example.com/page-2
header("HTTP/1.1 302 Found");
header("Location: http://example.com/page-2");
exit;
}
?>`

In this example, we’re redirecting from **example.com/page-1** to **example.com/page-2**.

As you can probably imagine, implementing or maintaining more than a few of these specific redirects in PHP could get a bit messy. But it’s doable.

### Apache

***Warning:** This 302 redirect method is only meant for experts. Mistakes here can cause big problems for your website. If you’re not an expert, proceed with extreme caution or reach out to an expert who can help.*

If your website is hosted on an Apache server, then you can implement redirects by editing the [.htaccess file](https://www.semrush.com/blog/301-redirect-htaccess/) in your WordPress root directory.

First, make sure that [mod\_rewrite](https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html) is enabled. Then use the RewriteEngine to configure your redirects.

#### Redirect a Single Page

If you just need to redirect one page to a new page, you can write code like this:

`RewriteEngine On
RewriteRule ^page-1$ /page-2 [R=302,L]`

This will redirect a page that exactly matches the URL **/page-1** to **/page-2**.

It’s worth noting that you could also use [mod\_alias](https://httpd.apache.org/docs/2.4/mod/mod_alias.html) for simplified redirects:

`Redirect 302 /page-1 /`page-2

#### Redirect an Entire Directory

If you want to temporarily redirect an entire directory, you can do that either by redirecting each page to a specific new URL within the new directory:

`RewriteEngine On
RewriteRule ^old-directory/(.*)$ /new-directory/$1 [R=302,L]`

This code, for example, would redirect **/old-directory/page-1** to **/new-directory/page-1**.

Or you can redirect *all pages* within that directory to a single new page:

`RewriteEngine On
RewriteRule ^old-directory/(.*)$ /new-page [R=302,L]`

This RewriteRule would redirect both **/old-directory/page-1** and **/old-directory/page-2** to the new URL, **/new-page**.

### Nginx

***Warning:** This 302 redirect method is only meant for experts. Mistakes here can cause big problems for your website. If you’re not an expert, proceed with extreme caution or reach out to an expert who can help.*

Nginx redirects are configured in the [.conf file](https://docs.nginx.com/nginx/admin-guide/basic-functionality/managing-configuration-files/), typically found in the root directory of your server.

#### Redirect a Single Page

`server {
listen 80;
server_name example.com;
location /page-1 {
rewrite ^ /page-2 redirect;
 }
}`

This will redirect **/page-1** to **/page-2**.

#### Redirect an Entire Directory

Redirect all pages from one directory to a new page in a new directory.

`server {
listen 80;
server_name example.com;
location ~* ^/old-directory/ {
rewrite ^/old-directory/(.*)$ /new-directory/$1 redirect;
}
}`

E.g., **/old-directory/page-1** redirects to **/new-directory/page-1** and **/old-directory/page-2** redirects to **/new-directory/page-2**.

Redirect all pages from one directory to a single new location:

`server {
listen 80;
server_name example.com;
location ~* ^/old-directory/ {
rewrite ^/old-directory/(.*)$ /new-page redirect;
}
}`

E.g., both **/old-directory/page-1** and **/old-directory/page-2** redirect to the new URL, **/new-page**.

### Windows Server with ASP.NET

***Warning:** This 302 redirect method is only meant for experts. Mistakes here can cause big problems for your website. If you’re not an expert, proceed with extreme caution or reach out to an expert who can help.*

On a Windows server, redirects are configured in the [web.config file](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/web-config?view=aspnetcore-7.0).

#### Redirect a Single Page

`<configuration>
<system.webServer>
<rewrite>
<rules>
<rule name="Redirect page-1 to page-2" stopProcessing="true">
<match url="^page-1$" />
<action type="Redirect" url="/page-2" redirectType="Found" />
</rule>
</rules>
</rewrite>
</system.webServer>
</configuration>`

This will redirect **/page-1** to **/page-2**.

#### Redirect an Entire Directory

Redirect all pages from one directory to a new page in a new directory.

`<configuration>
<system.webServer>
<rewrite>
<rules>
<rule name="Redirect old-directory to new-directory" stopProcessing="true">
<match url="^old-directory/(.*)" />
<action type="Redirect" url="/new-directory/{R:1}" redirectType="Found" />
</rule>
</rules>
</rewrite>
</system.webServer>
</configuration>`

E.g., **/old-directory/page-1** redirects to **/new-directory/page-1** and **/old-directory/page-2** redirects to **/new-directory/page-2**.

Redirect all pages from one directory to a single new location:

`<configuration>
<system.webServer>
<rewrite>
<rules>
<rule name="Redirect old-directory to new-page" stopProcessing="true">
<match url="^old-directory/(.*)" />
<action type="Redirect" url="/new-page" redirectType="Found" />
</rule>
</rules>
</rewrite>
</system.webServer>
</configuration>`

E.g., both **/old-directory/page-1** and **/old-directory/page-2** redirect to the new URL, **/new-page**.

## The Impact of 302 Redirects on SEO

### Positive SEO Impacts

Keep in mind that 302 redirects are not intended to fix or improve technical SEO issues your website is experiencing.

A 302 redirect is intended to improve the user experience in temporary situations.

Unlike a 301, **temporary redirects are not considered best practice** for:

- Consolidating duplicate content
- Correcting canonical URL issues
- Redirecting www to non-www versions of the same page
- Tidying up your site’s architecture

But implementing a 302 can preserve your links and rankings when a webpage is temporarily unavailable or under maintenance. Without using a 302, your page could be indexed with usability issues or incomplete content, which could hurt your SEO.

But it can have a negative impact if implemented incorrectly.

### Negative SEO Impacts

In theory, using 302s incorrectly could create issues for your website’s SEO.

For instance, it could cause the wrong version of a page to be indexed and appear in the SERPs (search engine results pages).

In reality?

The negative impacts would likely be small and temporary.

Google [treats a 302 redirect](https://developers.google.com/search/docs/crawling-indexing/301-redirects) as, “a weak signal that the redirect target should be canonical.”

In plain language: When there’s a 302, Google will usually show the **original URL** in the SERPs rather than the new URL.

This is what you expect from a 302.

But, if there are other signals that indicate the new URL is actually the “main” version of this content (the [canonical URL](https://www.semrush.com/blog/canonical-url-guide/)), it could be treated more like a permanent redirect.

In this case, Google would show the **new URL** in the SERPs instead of the original.

So, even if a 302 is incorrectly applied, there’s a pretty good chance that Google will figure it out anyway.

But it could still cause a temporary issue with your site, rankings, and traffic.

Plus it’s best practice to use the correct type of redirection if possible.

## 5 Common Issues with 302 Redirects

### 1: Using a 302 for Permanent Changes

Perhaps the most common mistake is using a 302 for a permanent change.

As we’ve discussed, 302s are meant to be temporary.

If you use a 302 to redirect a page and the change becomes permanent, it’s best practice to update the redirect to a 301.

You can easily identify any pages with 302s using Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool.

From the left-hand menu, click “**Site** **Audit**” under “On Page & Tech SEO.”

If your site isn’t already listed under “Projects,” input your root domain to have Semrush crawl and audit your website.

![search bar in Semrush’s Site Audit tool](https://static.semrush.com/blog/uploads/media/0e/2d/0e2d4bdda97e4294c0d90228466fdc94/iUjR-mXq7Qwh6bDdfOL7C3OCOB6wO5rVdJne82oPi9PpnEOkn8KvHzOO4xsvribFNA1bv7qEYGbCh1pe3z7YxV7VwxsXtxgqjTb9P4J9je_N8nj7kmYHKOuEWWzahD_JEWhSvP2MOqssSFr40Ci0FPw.png)

Once the audit is complete, click on the “Project” name and look for the “Crawled Pages” report underneath “Site Health.”

Click the number shown on the “Redirects” line to open a report of pages that return a redirect HTTP status code.

![“Redirects” line highlighted in “Crawled Pages” report](https://static.semrush.com/blog/uploads/media/99/e3/99e3846241b2e1ad13afe6b511df1e59/EEczfZKFIhE1dRvrZi_vKx5Bua-Wzg0aJ0gKwdNT5ioxddWamqdFMveLjV0mchYaTPH7gs4W8jKngaHvcu6sJPRbxK-LlyOerGsv33XhcOOWQ1wvLAlwsADeLAs7DJ-HwvYNJiscQtFh3pkthOV20gQ.png)

Review the list of URLs with redirects and see if any of them return a 302.

![list of URLs highlighted in the report showing the type of redirect, i.e. 301, 302 redirect](https://static.semrush.com/blog/uploads/media/f1/58/f1584517b65a359d67ef033aec78f5e0/WircgLJ8cDcuy7uSWS-FgCUsFFsJkFLaizrbDt3C5OMDX9hc2g6AFrKCKzxz3Wr_xQRWOUANk9cwXVC-fOlKnbflKRqBxePKXlHnVTAMV2_-44vk6ngejIESlCY1x97zSTahhvjvm3W5eAP4tQAi-z0.png)

***Pro tip:** You can apply an HTTP Status Code filter to this report to only see pages that return a “3xx temporary” status code.*

If there are 302 redirects that shouldn’t exist, that likely means they’ve been configured by another member of your team or someone who worked on the site in the past.

If the redirection isn’t necessary or is configured incorrectly (e.g., it's a permanent change rather than temporary), you’ll need to investigate how they’re implemented to make adjustments.

Refer to the steps in the “[How to Implement a 302 Redirect](#how-to-implement-a-302-redirect)” section above.

You can begin by looking in your WordPress or CMS admin panel. If you’re not able to find the 302s listed in the report, then consider consulting with someone who can check for server-side implementation.

***Note:** You also want to avoid using a 301 for changes that are only temporary. You can identify these issues by using the Site Audit tool that we just went through. If you identify a page that’s been redirected permanently in error, remove the 301 and implement a temporary redirect instead.*

### 2: Redirect Chains

Redirect chains occur when one page has a 302 that points to another page, which has a 302 that points to another page.

Like this:

**/page-1** has a 302 that points to **/page-2**.

**/page-2** has a 302 that points to **/page-3**.

The user bounces from one page to the next. And then the next. (And then the next.)

This can create site performance issues like slow page load speeds.

Plus, it’s just bad practice.

Using the Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool, you can easily identify redirect chains you need to fix.

From within Semrush:

Click “**Site** **Audit**” underneath “On Page & Tech SEO.”

Click on your site’s URL under “Project.” Or input your domain to create a project if it’s not already listed.

![search bar in Semrush’s Site Audit tool](https://static.semrush.com/blog/uploads/media/0e/2d/0e2d4bdda97e4294c0d90228466fdc94/iUjR-mXq7Qwh6bDdfOL7C3OCOB6wO5rVdJne82oPi9PpnEOkn8KvHzOO4xsvribFNA1bv7qEYGbCh1pe3z7YxV7VwxsXtxgqjTb9P4J9je_N8nj7kmYHKOuEWWzahD_JEWhSvP2MOqssSFr40Ci0FPw.png)

(If you create the project from scratch, you’ll type in your root domain and Semrush will crawl and audit your site. Once the crawl is complete, click on the site’s URL under “Project.”)

From the “Project Dashboard,” click “**View full report**” under the “Site Audit” section.

Now click the “**Issues**” tab:

![“Issues” tab in Site Audit tool with "27 redirect chains and loops" result](https://static.semrush.com/blog/uploads/media/99/c0/99c0cea91ef6cbd2aebc9d3a68be849c/P9HUefNpUrCqKQwA_LGtfV5WkUlvD_RQHK137_JEh-gmNHzJjh39swIP-HUO5kSV05ume3c6lt9WAsi7lGkpT4bqOKIxQPdoj5XNROOphuoX5UGkhQHCrcYgmxfS8QiYPhe-cQ9K7QxsNr-r2ZwpyG8.png)

The “Errors” list will show you all of the issues Semrush found on your site. In this list, you’ll find an entry for “redirect chains and loops” if any were detected.

Click on the list item to open the full report.

Once you’ve identified any redirect chains, you can simply update the 302 redirects that are in place to point to the final target URL and skip the additional redirect steps.

### 3: Redirect Loops (Too Many Redirects)

If you have an incorrectly configured redirect, you may run into a redirect loop.

A redirect loop is when your 302s keep sending users back and forth between two or more pages.

!["What is a redirect loop?" infographic by Semrush](https://static.semrush.com/blog/uploads/media/c4/5b/c45b469e41e29946dfa0800557dc4847/274Bcz3adbMC20GBWfEYOZAh8FVON23GjoDfVxv3ieF_isIKfZCxFrNelUdblDiuvha20RYPu_2NuNUqa1Hl_ByUT5FPoZzTjVsSyo3vwwvX4fRper0JeW-0Qo9ZRIvPSVinsSqvhO2qhK3sM9f7WoQ.png)

For example:

**/page-1** has a 302 that points to **/page-2**.

**/page-2** has a 302 that points back to **/page-1**.

The browser won’t know which page to show. You’ll receive an ERR\_TOO\_MANY\_REDIRECTS or “too many redirects” error and see a page that looks like this in Google Chrome:

![example of "This page isn’t working" error](https://static.semrush.com/blog/uploads/media/a8/4d/a84de8ecf4b19205d2354150f0a11f67/r9Db4js8f4O7P2xQHZj5fswjytbNX5qE-_1YoccTI1OMDFEViHISDZLutXT0gecBKM0bPGV_6L_gAGmRCahUruRbuV5I6DdAAMY91uPnL765hruPLaHI7vsA1VEFbDiveI9u-tlFqCuDD9yQG8AbvYw.png)

You can identify and troubleshoot this problem using the Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool.

From the left-hand menu, click “**Site** **Audit**” under “On Page & Tech SEO.”

If your site’s not listed on the “Site Audit” page, type in your root domain to run a crawl and audit.

![search bar in Semrush Site Audit tool](https://static.semrush.com/blog/uploads/media/0e/2d/0e2d4bdda97e4294c0d90228466fdc94/iUjR-mXq7Qwh6bDdfOL7C3OCOB6wO5rVdJne82oPi9PpnEOkn8KvHzOO4xsvribFNA1bv7qEYGbCh1pe3z7YxV7VwxsXtxgqjTb9P4J9je_N8nj7kmYHKOuEWWzahD_JEWhSvP2MOqssSFr40Ci0FPw.png)

Once the crawl is complete, click on the site’s URL under “Project.”

(If your site’s already listed under “Project,” click the URL.)

From the “Project Dashboard,” click “**View full report**” under the “Site Audit” section.

Now click the “**Issues**” tab:

![“Issues” tab in Site Audit tool with "27 redirect chains and loops" result](https://static.semrush.com/blog/uploads/media/f7/55/f7554a14e538fcb1fe2d86fa75b8f6fb/DSQyTlRmDiwh18SGdh7-Dm0jY4T0bgb1FagpXd5cEsSmTh6pKQ2siExa5ILS4jtJJ8abGipSm0VIPtMim6oUFuMgB-gU5TLcPJ5M50Xm-3iFlRw9sMmumsyG8rNqBPZOAIAokBeZLcNQ5qY0aIkhHDQ.png)

The “Errors” list will show you if Semrush detected a redirect chain or loop.

Click the list to see the full list and find any redirect loops.

If you’ve implemented 302 redirects and you’re receiving this error, it probably means there is a problem with the configuration.

Here are some things to look for:

- **Conflicting redirects**. Did you accidentally create redirects that attempt to send users from one page to multiple different pages? Or do you have redirects that point toward each other? Review the redirects closely for situations where they may create a conflict.
- **Conflicting plugins**. If you’re using a redirect plugin or third-party tool, it’s possible that the plugins are conflicting with one another. Try disabling them one at a time and see if it fixes the issue.

If you haven’t implemented a redirect and you’re receiving this error, then it may be a local or client-side problem. This means that the redirect is configured correctly on the server but something on the user’s side is causing an issue.

Try:

- **Clear browser cache and cookies**. It’s possible for a redirect directive to be cached even if it’s no longer used. Caching issues can also stem from a CDN or other network configuration that might require additional troubleshooting.
- **Disable browser extensions**. In some cases, your browser extensions can trigger redirects and break specific pages.

### 4: Leaving 302 Redirects in Place

Simply put: Don’t forget to remove 302s after they’re no longer needed.

Keeping it in place for an extended period of time could lead search engines to treat it as a permanent redirect. It could also create a poor user experience.

Run a regular Site Audit with Semrush to make sure you don’t forget to remove any redirects after a temporary website change.

### 5: Losing URL Parameters During Redirect

In some cases, you need a redirect to pass specific URL parameters or tracking codes to the new URL where you’re sending your visitors.

For example, if you’re using a specific UTM convention for tracking visitors as they move across your website. Or if your search and filter functionality passes specifications through URL parameters.

Depending on how you’ve implemented the redirects, they may or may not pass parameters from the original URL to the new destination.

To fix this, you’ll need to adjust the configuration on your redirect plugin and/or use [Regular Expressions (RegEx)](https://redirection.me/support/matching-a-url/) to parse the parameters from the original URL. Then pass them on when the user is redirected.

## FAQs About 302 Redirects

### What Is the Difference Between a 302 Redirect and a 301 Redirect?

A 302 redirect is for temporary changes to your website like a page that’s under construction or A/B testing. A 301 redirect is for permanent changes like a content being moved from an old URL to a new URL.

### What Is the Benefit of a 302 Redirect?

The primary use for a 302 redirect is to improve your site’s user experience. You can temporarily send users to a new URL to make sure they don’t land on pages that are outdated, incomplete, or under construction. It can also preserve the rankings and link value of the original URL while the redirect is in place.

### How Can I Set Up a 302 Redirect On My Website?

If you’re using WordPress and most common CMSs, you can implement a 302 using a plugin or extension. In other cases, you’ll need to configure the redirect on the server side.

### How Does Google Handle 302 Redirects?

Google treats a 302 redirect in much the same way as a 301. However, in cases where it’s seen as a temporary change, they will continue to show the original URL (not the new URL) in the SERP.

In this case, they won’t pass PageRank or links to the new URL unless it becomes clear that the change is most likely permanent.

### Can 302 Redirects Hurt My SEO?

Yes. If you incorrectly use a 302 redirect, it can negatively impact your search rankings and traffic. For example, it could cause the wrong version of your page to be indexed and lead to a drop in rankings and traffic.

If you’re worried about redirects hurting your rankings or looking to troubleshoot redirection issues on your site, the first step is to run an audit.

Use the Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool to identify incorrect redirect configurations, redirect loops and chains, and hundreds of other issues that could be holding your site back.
