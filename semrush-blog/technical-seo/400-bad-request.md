---
title: "What Is a 400 Bad Request? Definition, Causes, & How to Fix"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "400-bad-request"
url: "https://www.semrush.com/blog/400-bad-request/"
canonical: "https://www.semrush.com/blog/400-bad-request/"
author: "Vlado Pavlik, Christine Skopec"
published: "2021-09-20T20:22:00+00:00"
updated: "2025-04-07T08:45:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T13:18:14+00:00"
status_code: 200
html_hash: "80eea6413f0922aeff892d868135bcfb3ccf334e0b288e59eabccbce57077a49"
clean_word_count: 1720
clean_char_count: 12002
---
# What Is a 400 Bad Request? Definition, Causes, & How to Fix

## What Is a 400 Error?

A 400 bad request error is when a browser sends a request to a web server, and the server can’t understand or process it correctly.

It’s a type of [HTTP response status code](https://www.semrush.com/blog/http-status-codes/). And codes starting with 4xx usually indicate an error on the client side—meaning the issue is coming from what’s making the request (browser, app, etc.).

There are many different messages servers use to indicate a 400 status code, including:

- 400 Bad Request
- HTTP 400 Bad Request
- HTTP Status 400—Bad Request
- 400 Bad Request Error
- HTTP Error 400
- Bad Request: Error 400
- HTTP Error 400—Bad Request

The error looks something like this, depending on your browser:

![400 bad request error page with error highlighted](https://static.semrush.com/blog/uploads/media/c6/da/c6da840adfee1db2a862a321c5362c3e/00614b39995985b3afbcc5864939294f/AD_4nXeJuIMBkO0X_Har800tAfF3qM3-YvKvcgqYp7ZqKsbB1Sc-2wMoOsEGef52xbc8N3jB7iPqZ2T9eb89D0ZpBuaLd8E6pH_v1-HWpGsf8hhdjeRcokoGxDt1ia9MKjxoo-X1RJrN6Q.png)

Let’s dive into the common causes of 400 bad requests and how to fix them.

## HTTP 400 Error Causes & How to Fix Them

Here are the most common causes of 404 bad request errors—and their solutions:

### 1. URL String Errors or Other Invalid Syntax

One of the most common causes of a 400 Bad Request error is a problem in the URL—like extra spaces or special characters such as“&,” “%”, and “#.”

Sometimes, the URL is too long and complex. Browsers have character limits (e.g., up to [~2,000 characters](https://saturncloud.io/blog/what-is-the-maximum-length-of-a-url-in-different-browsers/) on Chrome), and exceeding these limits can trigger 400 errors.

![Arrow pointing to unsupported special character in URL causing the 400 bad request error](https://static.semrush.com/blog/uploads/media/a3/32/a33280c25a9a0cbbfc033671578312ce/f55084da61bee5bf185bc8492b001a1c/AD_4nXePS14woGuXz4j-yd9LPtrYNjnkDyJczDs7eJsfQ1BYy66ERvxJcEf8mH0-iE-dseapt2mk-G2kp3alHh_obBZ5VUcI4pU0hfXUsHX6WXZkxhQcLlIOV1z5fh8ip7Iuk4ZQgUpCvA.png)

Errors can also be due to invalid syntax outside of the URL that breaks standard rules.

This often happens when there's a missing or incorrect HTTP header in the request, which prevents the server from interpreting or processing it.

For example, the below GET request (which asks for data from the specified resource) has an improperly formatted header:

`GET / HTTP/1.1

Host example.com

User-Agent: Mozilla/5.0

Accept: text/html`

In this case, the Host header is missing a colon.

#### How to Fix It

**If you’re a regular site visitor**:

- **Double-check the URL**: Review the URL and remove any extra spaces, typos, or invalid characters

**For website owners and developers**:

- **Use a URL encoder**: If the URL contains special characters (e.g., when accessing files with spaces in their names or including symbols like "&" in search queries like "search?term=salt&pepper"), use a [URL Encoder](https://www.urlencoder.org/) to convert those characters into a format that servers can properly interpret
- **Debug dynamically generated URLs**: If you used an API or script to automatically generate the URL, it might be creating links with incorrect parameter formatting, improper character encoding, or exceeded length limits. Use a tool like Postman’s [Link Checker](https://www.postman.com/postman/the-exploratory/request/wyz3y87/check-url) to identify exactly what about your URL is causing the problem.
- **Use developer tools to identify the error**: If you’re not sure what’s causing the error, open your browser's developer console (Crtl + Shift + I in Chrome), go to the "Network" tab, attempt the request, and look for the red 400 error. Click on it to see what’s causing issues.

![Chrome web developer tools Network tab open and Headers tab selected with Status Code error highlighted for 400 bad request error page](https://static.semrush.com/blog/uploads/media/f4/c3/f4c394a7d9984f50db4fa19f30591dd3/0d75e78549e0a3f1bdf6473b3fa8579a/AD_4nXcx5i4K-asWI6s96irI2nvbti-3yEHkp262jPHE2GHdRpd5cfG5pBx6cZ3fX8987pRp_NrvJvnGccCwaeIxtGWT6yXG7zpp5POu6kQ8PDElYTyJ1NefAxmzYA6qXnHN7CkiOWjgoQ.png)

### 2. Corrupt or Invalid Cookies

When cookies (small data files websites store on your device) expire or get damaged, they can cause 400 errors.

#### How to Fix It

**If you’re a regular site visitor**:

- **Clear cookies or go incognito**: Clear your browser cache or launch a private session to remove existing cookies
- **Disable extensions**: Temporarily turn off extensions that might interfere with cookies
- **Check for browser updates**: Make sure you’re using the latest version because outdated browsers may handle cookies differently

**For website owners and developers**:

- **Verify website code**: If you’re a developer or site owner, check that your cookie implementation follows current standards and security practices. Meaning cookies need to use proper syntax, security settings, and domain settings (rules that determine which websites can use the cookie), and stay under the 4KB size limit.

### 3. Browser Extensions

Browser extensions can interfere with how your browser communicates with website servers in ways that lead to 400 bad requests.

For example, ad blockers might prevent necessary scripts that a website requires to function properly from loading. Or, privacy extensions might modify or block cookies that the site needs for processing a request correctly.

#### How to Fix It

- **Disable and check extensions**: Turn off all extensions, then enable them one by one to identify the culprit, and check the extension’s settings
- **Update extensions**: Click the extensions icon in your browser toolbar. Then, look for update options to get the latest version. In Chrome, you’ll need to toggle on "Developer mode" and click the “**Update**” button.

![Chrome extensions management page with Developer mode toggled on and arrow pointing to Update button](https://static.semrush.com/blog/uploads/media/8f/00/8f00baddde9523bf7acc5768f1e17ad4/ed1aa021a755ff3311a1efcd31126ded/AD_4nXfOU_UjjIaV1hhPyZGd7c-x_iGFUMZVHb2H2zIMXCknTyj8m4gmeauA60y-UPRT7wEZrHaKfDRr_MO_BhFKjEC-O76Vp3OLE2xGIrMWqrPj1NPymG44aBwh46FGrM_jmo3xyjwHrA.png)

### 4. Outdated DNS Cache

The domain name system (DNS) translates domain names (such as “www.yoursite.com”) into IP addresses (e.g., 192.168.1.1).

Your device stores these records in its DNS cache. But these records can become outdated if a site’s IP address changes.

When this occurs and you visit that same site, your computer sends the request to the old IP address that no longer exists instead of the new IP address.

#### How to Fix It

To remove outdated records that could be causing 400 errors, flush your DNS cache.

Here’s how to do it on Windows:

Open the “**Start**” menu and type “cmd” in the search bar.

With “Command Prompt” selected, click “**Run as Administrator**.”

![Windows 11 Start menu with 'cmd' typed in search bar and Run as administrator option for Command Prompt highlighted](https://static.semrush.com/blog/uploads/media/2a/c4/2ac4fef86a2b9ce42d667546c2dac131/589f64d19ea561708cdc5035937d498b/AD_4nXcWXD0Y9unnM6NZABD9xyHpBTHP4d6mrpbt2mfveqaQugVpSIail613nnQqdZnG_549TLmBiuQ084Y2Ma94b4_fCPw7prGEnmJkb5aE8hMyR5zlkuJ_IqyZwGNDzl1wRiFK0Efh3A.jpeg)

You may be prompted to allow access. If so, select “**Yes**.”

In the Command Prompt window that opens, enter the command “ipconfig /flushdns” and press the “Enter” key.

You’ll then see a message confirming the DNS Resolver Cache has been successfully flushed:

![Administrator mode command prompt window showing success message for DNS resolver cache flush command](https://static.semrush.com/blog/uploads/media/98/e3/98e31cdac87efa6430f3f6a2c01ad648/eb5b82e698cdddeb10cf6926140a4ca5/AD_4nXchChNziLdZi85nQIC4sC1zmOv2BAV9pfty6Ej1Ijg847jSy9W3DC97_wbHmwXfzI7OSzn55KIIb_Ukbhtgq3cOdoR8tzVdmhwAYd9qR3PZkt3cYIjfT3qutbpy94F6ALGbvFuC4g.png)

Now, try accessing the page again to see if the problem has been resolved.

### 5. Server Issues

Sometimes, 400 errors can actually be caused by the server. This happens when the server is configured incorrectly and interprets valid requests as invalid.

For example, a server might be set up to reject requests containing certain words that it wrongly identifies as security threats. Or, it might have outdated rules that don't work with modern browsers.

#### How to Fix It

**If you’re a regular site visitor**:

- Contact the website owner or support team to report the issue
- Try accessing the site later, as temporary server problems often resolve on their own

**For website owners and developers**:

- **Server error logs**: Review web server logs for specific details about what's triggering the 400 errors
- **Configuration files**: Examine server configuration files (like .htaccess for Apache or nginx.conf for Nginx) for mistakes or rules that might be too restrictive
- **Adjust security settings**: Temporarily disable or modify web application firewall rules to see if they're blocking legitimate traffic
- **Check server resources**: Make sure your server isn't running out of memory or processing power, which can cause it to reject requests it would normally accept
- **Update server software**: Ensure you're running the latest version of your web server software to avoid known bugs that might cause 400 errors

### 6. File Size Limits

A common reason for getting a 400 error is if you try to upload a file that’s too large to your website.

For example, uploading an image, video, or document file over the size limit to a WordPress site can lead to a 400 error.

In WordPress, you can check your file size limit by clicking on “**Media**” > “**Library,**” and then “**Add New Media File**” in the left-hand column.

You should then see something like this:

![WordPress admin dashboard with Media Library page open, Add New Media File button clicked, and Maximum upload file size limit highlighted.](https://static.semrush.com/blog/uploads/media/07/a8/07a8504a3779f42175c07ff82bdac7fd/f7e9da53eece1637c9695dd9855fe8e8/AD_4nXf9PKPOfvfzHaM9cPleIknRCdhojYNGIL_zb9C2x9lsBl3e7Ebe6wQQfeaj62ZAsnGvb1c-c2iSwVLLzBTi8b_eOY8sSnhMb3rEYRKEgt_ARTDsAtXog1WNt9UswoaQNOrFm4r1.png)

#### How to Fix It

Reduce the file size to below your limits to ensure the server can complete your request.

Host your videos on [YouTube](https://www.youtube.com/) or [Vimeo](https://vimeo.com/), upload your audio files to [SoundCloud](https://soundcloud.com/), or compress your images using a tool like [Compress Image](https://www.iloveimg.com/compress-image) to stay within your limits more easily.

## Find & Fix 4xx Errors on Your Site

Ideally, you’ll want to audit your site to find errors like 400 bad requests **before**they affect performance and annoy site visitors.

Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool can help.

Open the tool, follow the configuration settings, and go to the “**Issues**” tab. Type “4xx” into the search bar to find a list of 4XX errors, then click on the pages.

![Semrush Site Audit Issues page with '4xx' in search bar and errors section showing 4 pages returned 4xx status code row](https://static.semrush.com/blog/uploads/media/a0/50/a050b5386702d420391d544ba666ff3f/5c8897237b6dd291de26f525a47dc68a/AD_4nXcmKCIYNz0meaphjPKbW0qHtrhn_THRoc3UgGw7QEAVT02rPIaD--VoA9HCquoOy_JWJ1JWoaTyj0B6sMLx91Oxe8UVx46i3I-3W_2jvPVBkqKqADNvUN4nFvWtrYLFlnANTasaDg.png)

You’ll find a list of the pages affected and their error codes (the tool shows more than just 400 errors):

![List of pages that returned 4xx status code](https://static.semrush.com/blog/uploads/media/b3/17/b317875725ab325835324346e41b23bf/c310747a9a56b6eabb8c5f987790a633/AD_4nXe17g0IMBGpJVHGVbJw4NF9Q2Fx45wXVplPKUUcuoQ4peRvu2xYtbSraxoIHC4dyK_ikWiXWWprzH_82vGIR7nxkb-lww5k62E6SMSzNwKtgtBKGr_2lHim_K2UJ-HK63FGhRAE2A.png)

Then, apply what you learned in this article to fix the errors.
