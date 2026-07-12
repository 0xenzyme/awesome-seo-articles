---
title: "How to Speed Up Your WordPress Website in 20 Minutes"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "speed-up-wordpress"
url: "https://ahrefs.com/blog/speed-up-wordpress/"
canonical: "https://ahrefs.com/blog/speed-up-wordpress/"
author: "Joshua Hardwick"
published: "2020-10-22T16:00:57+00:00"
updated: "2023-10-05T08:11:05+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
  - "time_sensitive_title"
fetched_at: "2026-06-12T12:10:50+00:00"
status_code: 200
html_hash: "3456c570fc33e01c75c0298b1c41f7b204e70613d67876ab3823e43cf9e58a01"
clean_word_count: 2112
clean_char_count: 12655
---
# How to Speed Up Your WordPress Website in 20 Minutes

Everyone knows that page speed is important. It’s a confirmed [Google ranking factor](https://ahrefs.com/blog/google-ranking-factors/) on desktop and mobile, impacts user experience, and can have a direct effect on your bottom line.

But slow WordPress websites are a common issue.

Here’s the mobile score for a page of mine in [PageSpeed Insights](https://ahrefs.com/blog/pagespeed-insights/).

Before optimization.

If we run the entire website through Ahrefs’ [Site Audit](https://ahrefs.com/site-audit)—which shows page load time for all pages—we see that this isn’t the only slow-loading page either. None of them load massively fast, with an average load time of 570ms.

Before optimization.

Now here’s that same page after around 20 minutes of page speed optimization:

After optimization.

And the rest of the pages in Site Audit:

After optimization.

The difference is night and day. The score from PageSpeed Insights is near-perfect, and every page loads pretty fast.

In this guide, I’ll show you exactly how I did this in a few simple and easy steps.

1. [Remove unused plugins](#remove-plugins)
2. [Switch DNS providers to Cloudflare](#dns-provider)
3. [Install a caching plugin](#caching)
4. [Minify your code](#minification)
5. [Combine CSS and JavaScript files](#combine-css-js)
6. [Eliminate render-blocking resources](#render-blocking-resource)
7. [Lazy-load images and videos](#lazy-loading)
8. [Optimize Google Fonts](#google-fonts)
9. [Enable preloading](#preloading)
10. [Use a CDN](#cdn)
11. [Optimize your images](#optimize-images)

important

Many of the recommended optimizations below use [WPRocket](https://wp-rocket.me/), a paid plugin for speeding up your WordPress website. I’ve listed free alternatives where possible, but it’s important to note that plugins can sometimes conflict with each other and cause issues. You should always test how they affect your site in a staging environment before pushing any changes to your live site. Learn how to set up a staging site [here](https://www.wpbeginner.com/wp-tutorials/how-to-create-staging-environment-for-a-wordpress-site/).

## Step 1. Remove unused plugins

Unless you have a brand new WordPress website, chances are you’ve installed a bunch of plugins that you don’t use over the years. Some of these can impact page speed, so it’s worth deactivating and uninstalling anything you don’t need as a starting point.

Just be careful when doing this. If you’re not sure whether something is needed, leave it there.

## Step 2. Switch DNS providers to Cloudflare

Websites are files on hard drives (servers) connected to the internet. And every device connected to the internet has an IP address (e.g., 123.123.12.1).

Because IP addresses are tough to memorize, domain names are mapped to IP addresses using DNS, which stands for Domain Name System. You can think of this as the phonebook of the web. When you type a domain into your browser, a DNS lookup occurs to find the server’s IP address.

But here’s the thing: most people use the free DNS providers from their domain registrar, which is usually slow.

If this is you, switch to a faster DNS provider like [Cloudflare](https://www.cloudflare.com/).

To do this, sign up for a free Cloudflare account. Click “Add a site,” enter your domain name, and click the button.

Select the free plan, then click “Confirm plan.”

Cloudflare will now give you a chance to review your DNS settings before continuing. If there are no warnings, it’s usually safe to continue.

Now all that’s left to do is to swap your nameservers with your domain registrar. The way you do this varies between registrars, so don’t hesitate to ask their support if you’re unsure how to do it.

Here’s the process if you’re using Google Domains:

## Step 3. Install a caching plugin

Caching is a process that temporarily stores files so they can be delivered to visitors more efficiently.

There are two main types:

- **Browser caching:** Saves’ common’ files like logos on the users’ hard drive so they don’t have to re-download them on repeat visits.
- **Server caching:** Saves a fully-constructed, ‘static’ version of a page on the server so it doesn’t have to be rebuilt every time a new visitor requests it.

[WP Rocket](https://wp-rocket.me/) makes it simple to enable caching. Just buy, install, and activate it. Basic caching (server and browser) is on by default. If your site is responsive, head to the cache settings and check the box to enable caching for mobile devices, too.

Looking for a free option? Try [W3 Total Cache](https://wordpress.org/plugins/w3-total-cache/).

## Step 4. Minify your code

Minification removes whitespace and comments from code to reduce file sizes. And smaller files result in faster loading times.

If you’re using WPRocket, tick the checkboxes to minify CSS and JavaScript in settings.

If you’re not using WPRocket, install and activate [Autoptimize](https://wordpress.org/plugins/autoptimize/) and do the same.

Just know that you should always test how this affects your website before deploying live. Minifying can often lead to broken code, especially when it comes to Javascript.

## Step 5. Combine CSS and JavaScript files

Most WordPress websites include multiple CSS and JavaScripts files. Some are for themes, others are for plugins, and you might have some custom ones, too.

Combining these files may speed things up, but it depends on your server setup.

- **With HTTP/1.1**, CSS and JavaScript files are loading consecutively. That means one file needs to load fully before the next one can start loading.
- **With HTTP/2**, files load concurrently. That means multiple CSS and JavaScript files can begin loading at the same time.

If your server uses HTTP/1.1, combining files speeds things up because fewer files need to be loaded. If it uses HTTP/2, combining files won’t necessarily make much difference because files can load at the same time anyway.

To see which version your site uses, plug your domain into [Key CDN’s tester](https://tools.keycdn.com/http2-test).

If HTTP/2 isn’t supported, it’s worth combining CSS and JavaScript files.

To do this in WPRocket, tick the checkboxes to “Combine JavaScript files” and “Combine CSS files” in the settings.

If you’re using Autoptimize, there are two checkboxes to “aggregate” files. Just know these can sometimes ‘break’ things on your site, so it’s worth double-checking that everything still looks and functions the same once enabled. And remember to clear the cache beforehand and check for changes in an incognito window. Otherwise, the changes might not be reflected in what you see.

## Step 6. Eliminate render-blocking resources

Rendering is the process of turning code into a visible web page.

The key word there is ‘visible’ because a web page doesn’t always need to fully load before it’s visible.

For that reason, it makes sense to prioritize loading resources for ‘above the fold’ content.

You can do this by deferring the loading of non-critical CSS and JavaScript files needed for ‘below the fold’ content until later. To do that in WPRocket, check the boxes to “Load JavaScript deferred” and “Optimize CSS delivery.”

If you’re not using WPRocket, you’ll need two plugins: [Autoptimize](https://wordpress.org/plugins/autoptimize/) and [Async JavaScript](https://wordpress.org/plugins/async-javascript/).

In the settings for Autoptimize, check the box to “Inline and Defer CSS.” Then, in the settings for Async JavaScript, hit “Enable Async JavaScript.

If you previously saw the “eliminate render-blocking resources” issue in PageSpeed Insights, this will usually fix that problem.

## Step 7. Lazy-load images and videos

Lazy-loading improves page speed by deferring the loading of images and videos until they’re visible on the screen. If you’re running WordPress 5.5+, image lazy-loading is [enabled by default](https://make.wordpress.org/core/2020/07/14/lazy-loading-images-in-5-5/), but not for video.

If you’re using WPRocket, solve this by ticking the “Enable for iframes and videos” box under LazyLoad settings.

If you’re not using WPRocket, the free [Lazy Load for Videos](https://wordpress.org/plugins/lazy-load-for-videos/) plugin does much the same thing.

## Step 8. Optimize Google Fonts

Many themes use Google Fonts, and these fonts have to be downloaded from Google’s server every time someone visits your website. That can be a time-consuming process because your server has to make HTTP requests, download a CSS file, then download the font from the location referenced in the stylesheet. And it has to do this for every font on the page.

If you’re using WPRocket, it automatically optimizes Google Fonts requests. Otherwise, [Swap Google Fonts Display](https://wordpress.org/plugins/swap-google-font-display/) is a good starting point.

## Step 9. Enable preloading

Preloading allows you to define essential resources, so browsers know the priority of files to load.

For example, let’s say that your code looks like this:

```
<html>
<head>
<script type=”text/javascript” src=”somefile.js”></script>
<link rel=”stylesheet” href=”/style.css”>
</head>
<body>
Content
</body>
</html>
```

Based on this code, the JavaScript file would need to load first because of the hierarchy. That’s not ideal because the CSS file is almost certainly more critical than the JavaScript code.

The simplest way to solve this is to add another line of code, like this:

```
<link rel="preload" href="/style.css" as="style">
```

That tells browsers to prioritize the CSS file over the JavaScript file, regardless of hierarchy.

You can add preload attributes manually by editing the code, but that can get messy and confusing unless you know what you’re doing. It’s much easier just to install WPRocket, which does this automatically out of the box.

## Step 10. Use a CDN

Content delivery networks (CDN) are groups of servers distributed all over the world. Each of these stores a copy of your website so it’s quicker for users to connect when requesting web pages.

For example, let’s say your web host’s server is in the UK. If someone visits your site from the US and you’re not using a CDN, the connection between their device and your server will be slow. If someone visits from the US and you use a CDN, their device will connect to the closest server, which helps things connect faster.

There are lots of CNS providers, so all you need to do is choose one, enable it in WPRocket, and enter the CNAME.

## Step 11. Optimize your images

Lazy-loading solves many problems related to images, but it doesn’t do anything to help images that load above the fold. The bigger they are, the more they’ll negatively impact loading times.

To solve this, compress your images with a plugin like [Shortpixel](https://wordpress.org/plugins/shortpixel-image-optimiser/). Just install it, activate it, go to the settings, enter your API key, click “Save and Go to Bulk Process, then click “Restart optimizing.”

If you find that these are too low quality, head to the settings, and change the compression type to glossy or lossless.

## The results

Let’s look at how these optimizations impacted our page speed according to a couple of popular tools.

Here are the before and after stats for my post in Google’s PageSpeed Insights:

And here’s the same from GTMetrix:

You can see that the page previously fully loaded in 5.9 seconds with a 1.89mb page size and 67 requests. After the optimizations, all three metrics are down. The page size is 695 kilobytes, fully loaded time is 4 seconds, and the number of requests has shrunk by nearly 50%.

If we check all pages on the website in Ahrefs’ [Site Audit](https://ahrefs.com/site-audit), we see around a 40% improvement in average and 95th percentile load time.

## Final thoughts

Everything above worked well for my site, and it’s worked well for other sites too. However, it’s important to remember that every WordPress configuration is different. You might have more plugins, a clunkier theme, slower hosting, or more third-party tracking scripts, all of which slow your website down.

If your page speed could still do with some improvements after making these optimizations, then it’s likely that you need custom work done on your site. So it’s worth hiring a developer or page speed expert to take a look at things a bit more closely.

Or, if you want more details on specific issues, check out [our complete page speed guide](https://ahrefs.com/blog/core-web-vitals/).

Did we miss anything important from this guide? Ping me [on Twitter](https://twitter.com/joshuachardwick?lang=en).
