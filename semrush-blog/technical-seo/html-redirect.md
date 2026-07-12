---
title: "How to Set Up an HTML Redirect (+ Alternatives)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "html-redirect"
url: "https://www.semrush.com/blog/html-redirect/"
canonical: "https://www.semrush.com/blog/html-redirect/"
author: "Tushar Pol, Christine Skopec, Simon Fogg"
published: "2023-07-24T08:57:00+00:00"
updated: "2025-02-12T09:15:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "time_sensitive_title"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T16:57:05+00:00"
status_code: 200
html_hash: "ab096599f03ed5f64888299bfa6678200f115b4340a798bd8f5f4836a954daee"
clean_word_count: 1594
clean_char_count: 10843
---
# How to Set Up an HTML Redirect (+ Alternatives)

Setting up an HTML redirect to another page is easy.

In fact, you can do it in just a few minutes (even if you're not a technical expert).

In this guide, we’ll walk you through exactly how to set up redirects using HTML step by step. Plus, we'll share some alternative redirect methods that are even better.

Before we dive in, let's cover the basics.

## What Is an HTML Redirect?

An HTML redirect is a way to automatically send visitors from one URL to another using a simple HTML tag (called **meta refresh**), which you can add to the <head> section of your HTML.

Here’s a quick example of what that tag might look like:

`<meta http-equiv="refresh" content="0; URL=https://example.com/new-page" />`

In this example, the browser will refresh the existing page immediately and redirect the user to the new URL (https://example.com/new-page).

You might use an HTML redirect (also called a meta redirect) when:

- **Migrating pages**: You've moved a page to a new URL and want to automatically forward visitors to the new location
- **Merging content**: You want to combine multiple pages into one to prevent those pages from competing with each other and to consolidate traffic
- **Running temporary campaigns**: You're running a temporary promotional page that displays a countdown (like "Sale starts in 5 minutes!") and needs to automatically redirect users to a different page when the timer reaches zero
- **Running A/B tests**: You want to split test different versions of a page by randomly redirecting a portion of your traffic to a variant page
- **Managing user flow**: You're creating a simple splash page (an introductory screen) or interstitial that should automatically forward visitors to the main content after a few seconds

HTML redirects can be handy if you don’t have access to your server settings. However, they're not as good as server-side redirects, which offer better performance (faster load times) and more control over the redirect process, including the ability to handle different types of [HTTP status codes](https://www.semrush.com/blog/http-status-codes/).

That said, if you need a quick fix to reroute visitors without modifying server configurations, an HTML redirect can be just what you need.

## How to Redirect a Page to Another Page in HTML

Simply paste the below code into the <head> section of the page you want to redirect and replace the “content” and the “URL” values.

`<meta http-equiv="refresh" content="0; URL=https://example.com/new-page"/>`

Here’s an overview of the main components:

- **http-equiv=“refresh”** tells the browser to redirect the page
- **content=“0;** specifies how many seconds to wait before redirecting. Setting this to "0" creates an instant redirect, while any other number (like "5") creates a delayed redirect that waits the designated number of seconds before sending users to the new page.
- **URL=“URL=https://www.yoururl.com/newpage”** tells the browser which URL to send users to

Just make sure you’re careful when choosing between an instant and a delayed redirect.

[Google interprets instant redirects as permanent](https://developers.google.com/search/docs/crawling-indexing/301-redirects) (meaning you don’t plan to use the redirected page again) and delayed redirects as temporary.

## HTML Redirect Best Practices

When implementing an HTML redirect to a new page, follow these best practices:

- **Avoid redirect chains.** Never redirect to a page that’s already been redirected. These chains not only frustrate users, but also harm your SEO. Instead, always redirect to the final destination page.
- **Redirect to relevant pages.** Send users to pages that match their likely intent. For example, if a product page is temporarily unavailable, redirect to a similar product page rather than an unrelated category page. To help users continue their journeys naturally and reduce your [bounce rates](https://www.semrush.com/blog/bounce-rate/).
- **Give context.** Since HTML redirects require the original page to load first, add a brief message telling users why they’re being redirected like "This collection has been updated. Taking you to our latest designs." This context helps users understand what's happening and reduces confusion.
- **Include backup links.** Older browsers might not support meta refresh tags, so it’s a good idea to display a fallback link with a message like "If you’re not redirected automatically, click here." This ensures everyone can reach their destination, even if the automatic redirect fails.
- **Set appropriate timing.** If you’re using delayed redirects, make sure they’re timed sensibly to avoid losing users before the redirect happens. A five-second delay works well for most situations.

## Why to Avoid HTML Redirects When Possible

Although HTML redirects can be convenient, there are a few reasons to avoid them if you can:

- **Poor user experience**: HTML redirects require the browser to first load the original page, process the meta refresh tag, and then load the destination page. This double-loading makes your site feel sluggish and can frustrate visitors.
- **SEO implications**: Search engines need to process both pages, which leads to slower [crawling](https://www.semrush.com/blog/what-are-crawlability-and-indexability-of-a-website/) of your site. Plus, HTML redirects pass along less link equity from the original page compared to other types of redirects.
- **Inconsistent browser support**: Some older browsers might handle meta refresh tags differently or even ignore them. This inconsistency can lead to unpredictable behavior for your visitors.
- **Security concerns**: Meta refresh redirects are easier for malicious actors to manipulate compared to server-side redirects. They're commonly used in [phishing attacks](https://en.wikipedia.org/wiki/Phishing), which is why some browsers flag pages with meta refreshes as potentially suspicious.

## Better Alternatives to HTML Redirects

Instead of implementing redirects with HTML, consider using more reliable alternatives like server-side 301 and 302 redirects.

301 and 302 redirects are faster than HTML redirects, are less likely to hurt your SEO performance, and have less impact on the user experience.

Here's what each redirect means and when to use them:

### 301 Redirects

[301 redirects](https://www.semrush.com/blog/301-redirects/) are permanent redirects that tell search engines a page has moved forever.

Use these redirects when:

- You've permanently moved a page to a new URL
- You're moving to a new domain
- You're consolidating multiple pages into one page

![A deleted page is 301 redirected to the new page.](https://static.semrush.com/blog/uploads/media/69/95/6995c7919837a61370830bc2f19d1598/8e4ce2775f2a2fc7cfbd12f47f695758/AD_4nXe2Cae5cCor1q7a2d3NJfL8q_TCp82zOG_5ecnDzEgx0zmmFVsVG_aptdabOEFyyZlBL3chb7DLEmfOLvLeE38TLu4vPn3r8rRv6VcpYJ6MNMxqv_GAppWyP_uZYtXqLqj15fCAlw.png)

With a 301 redirect, you’re telling search engines the old page no longer exists.

With this method, you pass on much of the link equity from the old page to the new page. And search engines know to update the old link with the new one in the search results.

### 302 Redirects

302 redirects are temporary redirects that tell search engines a page has moved for the short term.

Use 302 redirects when:

- You're A/B testing different page versions
- You're doing temporary maintenance on a page
- You need to redirect users based on their locations or devices
- You're running a short-term promotion or campaign

Because 302 redirects are only temporary, search engines may not update search results with the new link.

This means you need to keep track of your 302 redirects and remove them when you no longer need them.

## Easily Audit Your Redirects

If your site has redirects, you’ll want a fuss-free way to audit them and make sure they’re working as intended.

You can use a spreadsheet for tracking, but spreadsheets can be tedious to manage.

Plus, if you forget to add a redirect to your sheet, you might forget about it (and forget to remove it if needed).

An easier way is to use Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool.

To start, enter your domain name and click “**Start Audit**.”

![An example domain is entered into the tool.](https://static.semrush.com/blog/uploads/media/50/a6/50a65dd51b0343ac2b13b4398c89fa45/f90f3a591f0ee31fc1ecc6b555451ae1/AD_4nXeneWVMPiWGuNgtYgdxsW1AyRXSPBd1sBCvg2B3LB4CiSpXX1ZJD0jPxaNy1y9Xgc1YLd6G7qaRIY_wZgSovReCzgs8JoialktUWk3xvHYIlYSVS0L6TeSXz7yYRfY7d3tSX_3k3A.png)

The tool will prompt you to set up a project and configure your [audit settings](https://www.semrush.com/kb/539-configuring-site-audit). After that, the tool will automatically start auditing your website.

Once the audit is complete, you’ll see an overview report like this.

Then, click the number beside “**Redirects**.”

![Under Crawled Pages, redirects are listed with a blue, hyperlinked number.](https://static.semrush.com/blog/uploads/media/45/c4/45c436f6fa7ca689c8f68af9db8f7125/971f00a8cb21d1ae6d394a27c1e7433a/AD_4nXdalhbKaKKbAHEorkN7rPHh7K0cgZSN4I2VBfeQhQ_zABk2fUlWfcG03RhSYNbNqt16qSNBxQTSX6GJYMTyKaOKWpCIIvp6fkE5hg0_--W-CmwfLJQAkxl0aqnN0okVIigUSUv4fA.png)

Here, you’ll see a list of the redirects on your site, so you can make sure each page has the right type of redirect.

![A list of page URLs has a 301 redirect status code.](https://static.semrush.com/blog/uploads/media/71/52/7152dac0b5c586ed1e350c46c89757a0/1da6316f82a0c62fc2bf8a3969458530/AD_4nXesuv-DzilScxDWdC1OtW5gIqnbDExDDm-vaQ8PBDMOQfCjBYKcbwst3rIvKBMg7-tx5eKAZk2rnEzDJB6PAq0f90PNI6Ea7LY53ufskw-vXjVI6ffEKD-CJLDDC6TGWAvy1xONDQ.png)

Site Audit also helps you spot redirect chains.

Here’s how:

Under the "Issues" tab, search for "redirect chain" and click on the number of redirect chains and loops found.

![For this example, 10 redirect chains and loops were discovered during the site audit.](https://static.semrush.com/blog/uploads/media/65/6d/656dc7c8321669c0aa3d1da24be2ec8c/01cb28723e7ac3a85346daf81eafd7c1/AD_4nXeHRdhpaziHrlzIjmwUmThMGcvZeGTmQyVZjnfTnT_ST74B1czFmzaJ0rykS3ojmFGjIjRYg7zJfxBPyM3Ma6J24SSP7MQNzs0tVEsFL_hIAf0kQoZ05ZXD5C1DE7DhVK71-1z4_Q.png)

Use this report to identify—and then fix—pages with multiple redirects to give users a better experience on your site.

![The report lists page URL with redirect link, the initial redirect URL, the final destination URL, and more.](https://static.semrush.com/blog/uploads/media/82/59/825933a1b62740da4bbdbd2d30e821fc/d1168e2301a7c61fa950181d1a5636dc/AD_4nXcI3pmny6GuCN5rnRF7fYjjJFG8t9hHo6hwvpQGLMjQ5HYMXnAA9oWXeABSGJL5GKC9qt49K1qDKJvPK9rIKgSQ_OGPUkbIUYXOMlHB_y44iYAZBTNU-Lza2Eb6dD-w6xbKxplc.png)

When you use Site Audit, you can be confident that users always end up where they’re supposed to.
