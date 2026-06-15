---
title: "What Are Crawl Errors & How Do They Affect SEO?"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "site-crawler-errors"
url: "https://www.semrush.com/blog/site-crawler-errors/"
canonical: "https://www.semrush.com/blog/site-crawler-errors/"
author: "Cecilia Meis"
published: "2021-06-10T16:30:00+00:00"
updated: "2025-08-06T09:28:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T19:47:37+00:00"
status_code: 200
html_hash: "1ac246b42b12a6fcda31a881b9a95b9db88ce6863e94b5f94d3a3e22cfe3d108"
clean_word_count: 1500
clean_char_count: 10729
---
# What Are Crawl Errors & How Do They Affect SEO?

If you want your site to rank, you need to ensure search engines can crawl your pages. But what if they can’t?

This article explains what crawl errors are, why they matter for SEO, and how to find and fix them.

## What Are Crawl Errors?

Crawl errors occur when [website crawlers](https://www.semrush.com/blog/website-crawler/) (like Googlebot) encounter problems accessing and indexing a site’s content, which can impact your ability to rank in the search results—decreasing your organic traffic and overall SEO performance.

![A simple graphic showing how Google crawls and indexes websites.](https://static.semrush.com/blog/uploads/media/25/ad/25ad146f0423365dba2db0ce9c69595c/8a54d57576943505f985842ab385dcaa/AD_4nXffWl5QRJJ_IK7NKDAJgttYXph9fQEBdejzxUiXjpEajzmxm09s9xvVR9UQMGWOORpYKzTtlf9ZWiGX0jK95nrU9Og8ZOgNexcQuHS9ESpODtiGiMqpOk1wE0Aq0gSUBt5wO1W4mg.png)

Check for crawl errors by reviewing reports in Google Search Console (GSC) or using an SEO tool that provides technical site audits.

## Types of Crawl Errors

Google organizes [crawlability errors](https://www.semrush.com/blog/crawlability-issues/) into two main categories:

- **Site Errors**: Problems that affect your entire website
- **URL Errors**: Problems that affect specific webpages

### Site Errors

Site errors, such as “502 Bad Gateway,” prevent search engines from accessing your website. This blockage can keep bots from reaching any pages, which can harm your rankings.

#### Server Errors

Server errors occur when your web server fails to process a request from a crawler or browser and can be caused by hosting issues, faulty plugins, or server misconfigurations.

Common server errors include:

**500 Internal Server Error**:

- Indicates something is broken on the server, such as a faulty plugin or insufficient memory. This can make your site temporarily inaccessible.
- **To fix**: Check your server’s error logs, deactivate problematic plugins, or increase server resources if needed

**502 Bad Gateway**:

- Occurs when a server depends on another server that fails to respond (often due to high traffic or technical glitches). This can slow load times or cause site outages.
- **To fix**: Verify your upstream server or hosting service is functioning, and adjust configurations to handle traffic spikes

**503 Service Unavailable**:

- Appears when the server cannot handle a request, usually because of temporary overload or maintenance. Visitors see a “try again later” message.
- **To fix**: Reduce server load by optimizing resources or scheduling maintenance during off-peak hours

**504 Gateway Timeout**:

- Happens when a server response takes too long, often due to network issues or heavy traffic, which can cause slow loading or no page load at all
- **To fix**: Check server performance and network connections, and optimize scripts or database queries

#### DNS Errors

DNS (Domain Name System)—the system that translates domain names into IP addresses so browsers can locate websites—errors occur when search engines can't resolve your domain, often due to incorrect DNS settings or issues with your DNS provider.

Common DNS errors include:

**DNS Timeout**:

- The DNS server took too long to respond, often due to hosting or server-side issues, preventing your site from loading
- **To fix**: Confirm DNS settings with your hosting provider, and ensure the DNS server can handle requests quickly

**DNS Lookup**:

- The DNS server can’t find your domain. This often results from misconfigurations, expired domain registrations, or network issues.
- **To fix**: Verify domain registration status and ensure DNS records are up to date

#### Robots.txt Errors

A [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) error can occur when bots cannot access your robots.txt file due to incorrect syntax, missing files, or permission settings, which can lead to crawlers missing key pages or crawling off-limit areas.

Troubleshoot this issue using these steps:

- Place the robots.txt file in your site's root directory (the main folder at the top level of your website, typically accessed at yourdomain.com/robots.txt)
- Check file permissions to ensure bots can read the robots.txt file
- Confirm the file uses valid syntax and formatting

### URL Errors

URL errors, like “404 Not Found,” affect specific pages rather than the entire site, meaning if one page has a crawl issue, bots might still be able to crawl other pages normally.

URL error can hurt your site’s overall SEO performance. Because search engines may interpret these errors as a sign of poor site maintenance. And can deem your site untrustworthy, which can hurt your rankings.

#### 404 Not Found

A 404 Not Found error means the requested page doesn’t exist at the specified URL, often due to deleted content or URL typos.

**To fix**: Update links or set up a 301 redirect if a page has moved or been removed. Ensure internal and external links use the correct URL.

#### Soft 404

A soft 404 occurs when a webpage appears missing but doesn’t return an official 404 status code, often due to thin content (content with little or no value) or empty placeholder pages. Soft 404s waste crawl budget and can lower site quality.

**To fix**: Add meaningful content or return an actual 404/410 error if the page is truly missing.

#### Redirect Errors

Redirect errors, such as loops or chains, happen when a URL points to another URL repeatedly without reaching a final page. This often involves incorrect redirect rules or plugin conflicts, leading to poor user experience and sometimes preventing search engines from [indexing content](https://www.semrush.com/blog/what-are-crawlability-and-indexability-of-a-website/).

**To fix**: Simplify redirects. Ensure each redirect points to the final destination without going through unnecessary chains.

#### 403 Forbidden

A 403 Forbidden error occurs when the server understands a request but refuses access, often due to misconfigured file permissions, incorrect IP restrictions, or security settings. If search engines encounter too many, they may assume essential content is blocked, which can harm your rankings.

**To fix**: Update server or file permissions. Confirm that correct IP addresses and user roles have access.

#### Access Denied

Access Denied errors happen when a server or security plugin explicitly blocks a bot’s request, sometimes due to firewall rules, bot-blocking plugins, or IP access restrictions. If bots can’t crawl key content, your pages may not appear in relevant search results.

**To fix**: Adjust firewall or security plugin setting to allow known search engine bots. Whitelist relevant IP ranges if needed.

## How to Find Crawl Errors on Your Site

Use server logs or tools like Google Search Console and [Semrush Site Audit](https://www.semrush.com/siteaudit/) to locate crawl errors.

Below are two common methods.

### Google Search Console

Google Search Console (GSC) is a free tool that shows how Google crawls, indexes, and interprets your site.

Open GSC and click “**Pages**” under “Indexing.” Look for pages listed under “Not Indexed,” or with specific error messages (like 404, soft 404, or server errors).

![Pages report in Google Search Console, showing why pages aren't indexed](https://static.semrush.com/blog/uploads/media/7f/ac/7face15545872fcfcb5df936e4288b42/8579d602ec0b6e7111c0b4e87e9710d3/AD_4nXcAxLqj1VtLzGqSXsDWde4UyfQgarU4bQ7dtF8D2TMT6HxkUheFwyZrGHh25zAhCmIkIYIAX96_9pvwA7kha29vCUF1CmJ6N8fIaf57ZXgWUY1KghvWcBg-g3iASSeQDoEVkQ-cCg.png)

Click an error to see a list of affected pages.

![Specific error report, in this case "Not found (404)" that shows specific URLs with that error](https://static.semrush.com/blog/uploads/media/94/53/9453a289a1999c624b55355a5fcd12bd/d9c84792e240bfa843a1dc4c72dc8dfc/AD_4nXdmaWA4Sflw0x36v3JeJimyly0EcKCuRq6H284XJy7aPqXurB7SxwtydoS2dTjp-Wn2nLIF4nazRRt93Ql7VDyDKP1ochnkD35bNgX4yyx04XbaDqFj-2s1DGRHMm1fiwicSagS.png)

### Semrush Site Audit

To find crawl errors using Semrush’s [Site Audit](https://www.semrush.com/siteaudit/), create a project, [configure the audit](https://www.semrush.com/kb/539-configuring-site-audit), and let Semrush crawl your site. Errors will be listed under the “Crawlability” report, and you can view errors by clicking “**View details**.”

![Crawlability report in Site Audit's Overview page](https://static.semrush.com/blog/uploads/media/f5/49/f5498685144ba7b42af11abdec1bfb61/fc9433e55d855d20108b082757fb7b3b/AD_4nXdC1dPUrz_CsfvuU8ym3Itl3aZ0b_6Sq18WT_4p1100DFEybHzGzsdAeNwfPyJeKufpRpQHgV6Um4oY72yNN370wQTmhmE7Wb0Xf7ZulY0KAsx5GCuRP-2_-4BcytQLEhkMWq8Pvw.png)

Review the “Crawl Budget Waste” widget. And click the bar graph to open a page for more details.

![Site Audit's Crawlability report with the "Blocked from crawling" error highlighted](https://static.semrush.com/blog/uploads/media/69/10/6910c4052f2560a5783acccc895153c3/6c79b4a8850b3e7b66e7010db3f07b32/AD_4nXdl3VttjEqMUwrwrrfNSHWSVSWDP2O3kv3cOTal7bhFsrDAu-7H-eOVQ2aC4IlSQkL8u8JWc0maYNnYHjBmijq95iZeGzlzHFQjvScLkx6zyv0UdQ4HyA9IHKsmEx-cxsAz7mjU.png)

Then Click “**Why and how to fix it**” to learn more about each error.

![Report for the error "pages are blocked from crawling" with the "Why and how to fix it" widget open](https://static.semrush.com/blog/uploads/media/f5/6d/f56df29163b0fa6c95434f0908044cc0/4f68fe4e5fe10b8fb96f9f7bb97d024a/AD_4nXfhwFNmpgf7GKiyoXtVFvKL501D6AwVEDJOaRpc2UOU20UrDFZ-GqsMJaECIZsd8fYQbFJk1uugRuQkUqDGvRh_WEmwKnvr36Xi9WdSvPqlfDqCK2JXPHSLqp8QSJozy7O4iav2aw.png)

## Fix Site Errors and Improve Your SEO

Fixing crawl errors, [broken links](https://www.semrush.com/blog/broken-link/), and other technical issues helps search engines access, understand, and index your site’s content. So your site can appear in relevant search results.

Site Audit also flags other issues, such as missing [title tags](https://www.semrush.com/blog/title-tag/) (a webpage’s title), so you can address all [technical SEO](https://www.semrush.com/blog/technical-seo/) elements and maintain strong SEO performance.

Simply open Site Audit and click “**Issues**.” Site Audit groups errors by severity (errors, warnings, and notices), so you can prioritize which ones need immediate attention. Clicking the error gives you a full list of affected pages. To help you resolve each issue.

![Issues report in Site Audit](https://static.semrush.com/blog/uploads/media/6d/7e/6d7ee5c61a5b578611f66d78fafc2d3d/116cc4c4893c74f1e80be4d25ebd9e2b/AD_4nXfvGf9PtD8TfiEkAUDC2LKdVG8b_WnkTtgfij6oBdztk2xnYgpVsg61mUXnmMgOUZQCvKCb2U7gtIz3UrSz2WeM3OjkoaH_HsBz6gcz9K5oWnisVuHUNIhNkzk37IFbfHVyCR-SNg.png)

Ready to fix and find errors on your site? Try Site Audit today.
