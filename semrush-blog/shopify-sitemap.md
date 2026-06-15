---
title: "Shopify Sitemap: What It Is & How to Submit One"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "shopify-sitemap"
url: "https://www.semrush.com/blog/shopify-sitemap/"
canonical: "https://www.semrush.com/blog/shopify-sitemap/"
author: "Vishal Dave"
published: "2021-06-04T20:10:00+00:00"
updated: "2023-10-17T11:22:00+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2023_aging"
  - "time_sensitive_title"
schema_genre: "General SEO"
fetched_at: "2026-06-12T19:45:32+00:00"
status_code: 200
html_hash: "7328f544e24491609753494256067f97b116686b73ac3f4bec9fc732503b0961"
clean_word_count: 2394
clean_char_count: 17945
---
# Shopify Sitemap: What It Is & How to Submit One

There are lots of ways you can improve your Shopify website’s SEO.

But one of the best things you can do is leverage your sitemap. Which is especially easy if you have a Shopify website.

In this post, we’ll go over how to find and submit your Shopify sitemap. And a method to keep your sitemap updated and optimized for better search engine visibility.

Let’s start with the basics.

## What Is a Sitemap & Why Does Your Shopify Store Need One?

A sitemap is a file that lists all the important pages on your website.

It acts as a directory for search engine crawlers (and for users, depending on the format) to help them easily navigate your website. And ensure they understand your website’s architecture and the relationships between the pages.

Here are the two main types of sitemaps:

- **XML sitemap:** A sitemap that’s used by search engine crawlers to discover pages
- **HTML sitemap:** A sitemap that looks like a standard webpage with all important pages listed to help users easily navigate the website

[XML sitemaps](https://www.semrush.com/blog/xml-sitemap) provide additional information about URLs, such as when they were last updated and whether there’s an alternative version.

Here’s an XML sitemap example:

![An XML sitemap example from Screaming Frog](https://static.semrush.com/blog/uploads/media/8b/c6/8bc647b62176f7db0384d527c067211a/VpeyCFDDCjpOICXavc4syKrJdV7DvZ8rUcXUGAIJ3lOZtEyQHJW8Nc4LnKRsjWy8BUJMR1O-ckF2I0AfY5xBVz-jH3ffT9xT_83wcpdouyVmG_UczmdOFwgGgR0QkkyJDzu_S2VlVe3z8ajBux9KIHs.jpeg)

And here’s an [HTML sitemap](https://www.semrush.com/blog/html-sitemap) example.

![An HTML sitemap example from Apple](https://static.semrush.com/blog/uploads/media/fa/63/fa6321a8d670296879e1105d5889aa09/T9fZvQ6Dfsf_K6Be6q2o8--szkP687Y9Jx34q5LdRKysE3aHuGzc7HuoL4e0tetzmkCI6ZlVS6MkY5w6UQ8NYCAqCk5UpmNptbzk5RkJ-5T94E1QDY0lKfc8ZfD-gXIzOMBj2ffLU-gGs4-QDwle0gY.jpeg)

HTML sitemaps can also improve your internal linking. Which contributes to your overall SEO performance.

But for most Shopify stores, the header navigation bar contains links to all important pages. Meaning there’s rarely any practical need for an HTML sitemap if you have a Shopify website.

So, we’ll focus only on XML sitemaps for the rest of this article.

## Do You Need to Know How to Create a Sitemap in Shopify?

Luckily, there’s no need to dig into how to add a sitemap in Shopify. Because anyone who uses the platform already has an XML sitemap.

The Shopify platform auto-generates and modifies your XML sitemap. And also supports region-specific sitemaps for international sites.

### Can You Edit Your Auto-Generated Shopify Sitemap?

Shopify-created sitemaps can’t typically be modified.

They’re automatically generated and modified based on your store’s content. And Shopify is restrictive about changing them.

You can use third-party Shopify apps to edit the existing Shopify XML sitemaps. And other external tools to create one from scratch. But we’ll get into those options later.

## How to Find Your Shopify Sitemap

Your Shopify XML sitemap is in your site’s root directory.

Simply visit https://example.com/sitemap.xml in a browser to access your Shopify XML sitemap. (Just replace “example.com” with your Shopify store’s domain.)

For example, here’s clothing brand Hiut Denim’s Shopify XML sitemap:

![Hiut Denim’s Shopify XML sitemap](https://static.semrush.com/blog/uploads/media/ae/a1/aea1d1c68f97354f7d8a52dce136e2fb/AxsG08qe30T-8GZyfHMSQj1x1_-4d1gRy7ZFt2ytj_v6XXn5iB0yWukDrBzdIUMO1u1-N0JxKm6Ndf3S-ltM09iPnTaU1_bu9VJk8rhEbbOygvmnY9KqgWYPdWGjYQa5BmyZF9It8KuDwXaXj40C4qo.jpeg)

This is the main sitemap. Which is called the parent sitemap or sitemap index. And it links to all the child sitemaps, which contain the URLs of the pages.

You can submit your sitemap index to search engines instead of submitting each separate sitemap. Because search engines can access those individual sitemaps through the links in the sitemap index.

Here’s what one of Hiut Denim’s child sitemaps looks like:

![Hiut Denim’s child sitemaps looks like](https://static.semrush.com/blog/uploads/media/be/a1/bea11b6cdf733280366192ce0772b7e7/uTzx_rG6szr9gvuMwe5c5H4mwBOK74oJwxkYAe3DIUhN-6CTRdeW219AdRF9dsB-rNEVhedrBSp83ka-L4OIkStlHLKYD4e-xYi0Zq8Xk2gCFjrwen4aiKcteuSl_Z5Be6s7JUyjPdLFeIO1zhP9FFQ.jpeg)

## Understanding the Contents of a Shopify Sitemap

The Shopify sitemap.xml file is a sitemap index. Which contains links to your store’s other sitemaps.

It contains sitemaps for the following:

- **Products (/sitemap\_products\_1.xml):** contains URLs of all the product pages and their media
- **Collections (/sitemap\_collections\_1.xml):** contains URLs of all the collection pages and their media
- **Blog posts (/sitemap\_blogs\_1.xml):** contains URLs of all the blog posts and their media
- **Pages (/sitemap\_pages\_1.xml):** contains URLs of all other pages and their media

Each XML sitemap has a limit of 50,000 URLs. So, Shopify will automatically create additional ones if this limit is exceeded.

That means the next product sitemap would be sitemap\_products\_2.xml.

And here’s what a Shopify product sitemap looks like:

![Shopify's product sitemap](https://static.semrush.com/blog/uploads/media/c4/f4/c4f4be5f6d05bfb1cf1959317a87ce24/tgcxr_lTtU0SB_r4WZrlWRCEu8b131dh3j0PadHiyQ5HIzhvOtDWk7D3-aopYo0rkzWxid86VL_aUMRl7OwxbfGd1oZCD-3Sn0Fg-vTMj-LAEmAABynTgYf6IY1dXB9OVnOEHv1z_psSwDPOuRkH6DQ.jpeg)

In the sitemap, each URL is defined by the <url> tag. Which contains the following information:

- **<loc>:** The location (URL) of the webpage or image file
- **<lastmod>:** The date and time when the content was last modified
- **<changefreq>:** An indication of how often the content is likely to change (e.g., daily, weekly, etc.)

For the products sitemap, each entry also contains an <image:image> tag for the product image. It contains the following information:

- **<image:loc>:** The location (URL) of the product’s primary image
- **<image:caption>:** The product image’s caption, if present
- **<image:title>:** The product image’s title, if present

## How to Add a Custom Sitemap to Shopify

There are a few ways to customize your sitemap.

The first is a workaround that involves creating and uploading a static Shopify XML sitemap. Then creating a 301 redirect to it from one of your webpages.

This gives you more control over which pages are included. But you have to be extremely careful to avoid leading search engine crawlers astray.

Here are some common mistakes to avoid:

- Creating a blank sitemap without any URLs
- Omitting important pages and content
- Including URLs with status codes other than 200 (i.e., redirects, 404 pages, etc.)
- Including [non-canonical URLs](https://www.semrush.com/blog/canonical-url-guide/) (meaning alternative versions)
- Exceeding the sitemap limit (i.e., 50,000 URLs or 50 MB)

And ensure that the sitemap.xml is valid. Meaning it follows the [sitemap protocol](https://www.sitemaps.org/protocol.html) set by Sitemaps.org. For example, the sitemap should:

- Begin with <urlset> and end with </urlset> tags
- Specify the namespace (protocol standard)
- Contain <url> tag for each URL, with a <loc> tag inside it

You can also use apps to modify sitemaps. There are plenty of them in the Shopify App Store.

![Shopify App Store's results for "sitemap"](https://static.semrush.com/blog/uploads/media/34/8f/348fed266f8fe8e9d1f1a23e1ae495df/JN4ZuZC76nfYklcPklTAVe7fxmAWty0Pg-Ylyw_q01Jor2PIGOuWN_99xeID_wo5C1tZ9Sik-AGEEo9KYGXZv2QiKI6Jqb4RxhJepeY8DMPPuv4tweMfQge_USjNeOxqJg7F4zvQwIpToPDYga5CjxI.jpeg)

But it’s usually better to stick to the default sitemaps and settings.

Why? Because Shopify auto-updates the sitemaps regularly, keeping them up to date. And reducing the risk of errors.

## How to Submit Your Shopify Sitemap to Search Engines

Let’s go over how to submit a Shopify sitemap to Google and Bing.

### Submit a Shopify Sitemap to Google

You can submit your Shopify sitemap through Google Search Console (GSC). But first, you’ll need to create a new property for your Shopify store and verify it.

To add and verify your Shopify store, start by navigating to [Google Search Console](https://search.google.com/search-console/).

Here, you can verify the property in two ways:

- **Domain:** Covers all URLs and subdomains
- **URL Prefix:** Covers all the URLs with the specific prefix

The **URL Prefix** method is easiest and most suitable for Shopify. Because all the URLs share the same prefix (e.g., https://yourdomain.com/).

In the “URL Prefix” field, enter your Shopify homepage URL and click “**Continue**.”

!["Welcome to Google Search Console" window](https://static.semrush.com/blog/uploads/media/ea/20/ea208a702049d5d02d9782617b36893b/vIqOBO0HjZhhexfBRKlDrr14ZSGxbEVCMQpxNBWOxHdYiYsH9xuMmgMh9SfvzUtOrRvA5JiY24T67qgA-faQ7BWIkqhl0PWUZednkmqyXeSB2gCMA1hyQ5BpPO8IszmeIhVtuIwgWYtY24VB7Nk2ESk.jpeg)

Now, you’ll need to verify the site’s ownership.

There are multiple ways to do that. For example, you can use existing Google Analytics or Tag Manager setup. But the simplest option is to add a meta tag in the Shopify store.

To do this, expand the “**HTML tag**” section and copy the meta tag.

!["Verify ownership" screen in Google Search Console](https://static.semrush.com/blog/uploads/media/3c/b3/3cb386f716cd66a42b117decd2a1271a/yw0-EGnZwfl-6pakluJzWnndnFtN1jPe1nPJw5VJdaJ9rLuCtIjqmyvHlCH3ny5BiXXjcPBxz-nmBCj-LIYvJcElU6lvGHzXlw1Sf06KVQrddUbab7EXLGTbK6-mtZBWwUx0HsNyX6SSDJSEVJDYX5w.jpeg)

Now, go to your Shopify admin. In the left-side menu, navigate to “**Sales channels**” > “**Online Store**” > “**Themes**.”

![Navigating to "Themes" in Shopify admin menu](https://static.semrush.com/blog/uploads/media/1a/bb/1abb7d9700224edffd43d01a7f0e769a/SxQLzTkALIvXSV8T1hdPigUUcDH-KXzaD6zPOg3DUXwuh6_XzRyYpY-lQeSAUbA6Tnq_rlUifrTQkVOrS0kB_fU7Hme_iyZWyxqhaFbQ1fnj-KawmtxDarNKY_G0A-tGoAEsWCLo4k4D0mAb2PDHRdA.jpeg)

In the Shopify themes, click on the three dots beside the “Customize” button to open the menu. And click “**Edit** **code**.”

![Menu in Shopify themes](https://static.semrush.com/blog/uploads/media/1a/e6/1ae6b320913ee814912292f96d8914a5/5PK75cJP2DreTqcGVs3ASX51taPv5iCt36BQdE_el8dcJvQdkP8kLta6KoEkkYsPLG2Zp_yMDglHPjkYDW7_XY0spzq95LXPMPW6LJ14UjqijOn3rGuEXoXRoUwZIxwWJufLF9BdCjydkQpEOIGfU28.jpeg)

Open the theme.liquid file under the “**Layout**” drop-down menu.

!["theme.liquid" file selected under the “Layout” drop-down menu](https://static.semrush.com/blog/uploads/media/e2/ca/e2ca2cf56d20a72ea905631780ce9abf/sHo60bkUZm9tb8lzFBPYqWO8AhAHuHs_ryEZSNK885NRxDGM8z8yzvAeuxZSvRx0iDivE7wCDGHVFd0C5NuafXZH_VxazfG5kGNa_cwhsrqRrkQXafB4mu8LV8bsIyv7c_XkR3PEEJviEfljBqDYcRI.jpeg)

Once you’re in the Shopify theme.liquid file, paste the Google search console site verification code inside the <head> tag as shown below.

![Shopify theme.liquid file with Google search console site verification code added](https://static.semrush.com/blog/uploads/media/cf/4f/cf4f5679a2ed172d627654bb394b882b/04IWeK8LQvXt1QTD4IJ93QRlyoAdNG-e1v-_ISzQnYqytnRwEpZkgUquGFN9Slc5Rmnk6TT48fYbDXDdJXRu6cblpfWcVwUlMtvLH8KUq8SOWpObf32GQtTRBm9CEnZ4oFGifXWO5c1PYAkb8ig_Hu8.jpeg)

And click “**Save**” at the top in the right corner.

***Note:** Making changes to your theme file can lead to serious website issues if you make mistakes. If you’re uncomfortable with this step, reach out to a developer who can help.*

Now, you’ll need to return to the Google Search Console setup and verify the meta tag.

Click the “**Verify**” button inside the “HTML tag” section from where you copied the code.

You’ll get a confirmation message once the verification is complete. Once you’ve successfully set up your Shopify site in Google Search Console, you can see its presence on Google and track its performance.

You can now submit your sitemap by going to “**Indexing**” > “**Sitemaps**” in GSC.

![Navigating to “Sitemaps” in GSC menu](https://static.semrush.com/blog/uploads/media/49/1e/491e586a7eb1b00ac79a33a61f9e1bbe/dNi1sEKSEFMMZXLoIKGnlsQmMl7LFlTrHtkm7HjtZBtQhr1N-VPkXLRx9kSHxbz_KZ6d-IRfPSayvbdEOUtXl28unkdR-Uw6Y1G-q5IGZbrjdt5StrWJBknzaI3V7GlzVERHSFIVME1Yh4L6xK2ve0c.jpeg)

Enter the sitemap address under the “Add a new sitemap” section and click “**Submit**.”

![“Add a new sitemap” section in GSC](https://static.semrush.com/blog/uploads/media/b6/60/b6608e78eff01af629423139f68c2cf0/PivhAhb3Xs8q4uhYqUberbZvJXFBLUKbPzQZAzGXJRLJ8CVCItVZm_eOCPH7jB2eomeSbbcxQIFyYv6vQNYLDSiItfqS42QYbPh8rObtN6rHEAMXf9MnkEm6Bwj2CkIwlnrdW9m3swlKiJMevnnVA6Y.jpeg)

When your submission is successful, you’ll get this message.

!["Sitemap submitted successfully" message](https://static.semrush.com/blog/uploads/media/64/7e/647e6a9bc0c71586b4d2f89a37d64d5f/GyIWLErDOu_pABXZP2Fchu_f16xpm6PHXtEVyouHD-X6cXBmVaDDeP5QV35pfiGfqQDHbWV8Xb5Rs-5jsTLJWgdgJumWH0P5ULygVXk8meccUGMYBGIRpSPxiegSTBL8RbE9-WwhgJcCz0E6BT6XqSA.jpeg)

***Further reading:** [How to Submit a Sitemap to Google (in 4 Simple Steps)](https://www.semrush.com/blog/submit-sitemap-to-google/)*

### Submit a Shopify Sitemap to Bing

Bing Webmaster Tools helps you understand your site’s presence on the Bing search engine.

You can submit your Shopify sitemap to Bing and help it understand your website—it tells the search engine which pages you’d like to get indexed.

For that, you’ll need a verified site.

Go to [Bing Webmaster Tools](https://www.bing.com/webmaster/tools) and log into your account.

If you’ve already verified the site on GSC, you can import details and sitemaps directly. Otherwise, you can follow the manual verification steps below.

Enter your Shopify domain and click “**Add**.”

!["Welcome to Bing Webmaster Tools" window](https://static.semrush.com/blog/uploads/media/84/71/84714201ae4f5a4149945a1a974f373c/nev8kizWrIZsOugQssFDc25-3UOYMACYmz86S29JitJU4vgSbMGnLPDXGKPF7GP7WFaEmX_Hn0gpX3A5YxgtjN9V19bwbfRcsvmtyEro4KU613fmFat3nUiVy663hHn3AbRH1SclGasLK7fROcwKi2g.jpeg)

In the verification, expand the “HTML Meta Tag” section and copy the verification code.

There are other verification methods, such as adding an XML file. But the “HTML Meta Tag” option is the easiest one.

!["Add & verify site" screen in Bing Webmaster Tools](https://static.semrush.com/blog/uploads/media/0f/37/0f37b1ff1578144b32fc478c38c25f0c/7qEIugFiEOWOVC2DItaOQrzAojoHHPoG1gTF2IUadp9LiXGzES4NVvDohwEm9H7NkkReE9P4vjmGaKnIxFNxVe2W3NAwwHTKbTPhcoRVK1VmMOM_A4-7BwwCKqpyI9I1cads8kmgPSSTVPxHDXwqboQ.jpeg)

Now, follow the steps mentioned for the Google verification in the previous section on adding the meta code to the Shopify theme.liquid file. And verify the site.

Once the verification is successful, you can submit your Shopify sitemap to Bing.

Click “**Sitemaps**” in the left-hand menu of Bing Webmaster Tools.

![“Sitemaps” selected in the left-hand menu of Bing Webmaster Tools](https://static.semrush.com/blog/uploads/media/c1/0e/c10eb75784d2588ed86bc50c0c0d2727/hOoHYeQSwF7Kg97vUXcFX0bOQIuzY5RAzqmliEAfMiJGtRq8CgodK1WG_xVT2sMgkbMHz5h9hNRVQKgaffvzy4ZDKJ2axlpjCAs5o7B3xuFx3iE0UXaZ-0YVxwGChgLqvAcdrcF4bVs9soHKvEFwtN8.jpeg)

In the top right corner, click “**Submit sitemap**.”

![“Submit sitemap” button highlighted in the top right corner](https://static.semrush.com/blog/uploads/media/ae/a7/aea76bc7efcf06c59aa47f28ac7edddf/xq66Po159h_Bw9AG-vllB3BSSx_407ZazRFRnLiUmJNU7qcku6K6deEJp3zfBBt0OUYEZIt2vruCs-V4z-xEd9yjEMMunsrqhFg-kt2UYkIA97Jqa1ctB-ehAeZFgKYjNlPqbfL3DC-gVXtJyqZrLO0.jpeg)

Enter the address of the Shopify sitemap in the pop-up window and click “**Submit**.”

![“Submit sitemap” section in Bing Webmaster Tools](https://static.semrush.com/blog/uploads/media/37/85/37850e9cf57448cf30bb48be55707a39/SZZfOBRyc2zu55aJ59D2LTgm-QAYTOdWWHtYp2PmKusrCiW5HfSIvcZhPljsV2DXxhBYZvamcZtxAvFHnm-dYgyV1V0x78aivDMsSjI3R3gOD7ht3BS_fHtF3ZGxtEndhsm8sZAtN6pOTYfTvosVc20.jpeg)

Many merchants face the “Couldn’t fetch” error while submitting a Shopify sitemap.

If this happens, you need to check whether your site is accessible to the public (meaning it’s not protected by a password).

Simply open the sitemap URL in a private browser window to see if you can access it.

## Monitoring and Updating Your Shopify Sitemap

Your Shopify sitemap plays a crucial part in your SEO performance. And keeping it up to date and optimized for search engines is essential.

This can be challenging if you’re using custom sitemaps.

The Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool can help you find and fix all the critical issues in your sitemap.

Open the tool and follow the [Site Audit configuration steps](https://www.semrush.com/kb/539-configuring-site-audit) to create a project and run a site audit.

Once the audit is complete, you’ll see a high-level look of your site’s technical SEO health in the “Overview” report.

![Site Audit overview dashboard](https://static.semrush.com/blog/uploads/media/3d/5f/3d5f402c48cfcd8bfe458743a4e7c248/OBgz7ivdHhPhOslk2xIJEaXnIPETfTmMmEVEyqaKxfvmRCSqJiKc7V0KOGp5PPjEof5pWSuJ03iwAlZBAOHLZboeQTO26Ed6i2Dm7eBnzGjbNz3sHzreC5CVlhFG1s3T3lyO9MEiM4Bw4091SdxglwI.jpeg)

Now, click the “**Issues**” tab and enter “sitemap” in the search bar at the top.

![Sitemap errors identified in Site Audit under "Issues" tab](https://static.semrush.com/blog/uploads/media/54/35/5435b6ef0f6e84b7925e63aa7957c739/B_lzwbrsQap5URfCKz6YlecHD06x4PM2fkU7EKwnui_jGbViH3_0i61EKQG2rYGIUcqZ5vAawa13MbkIi6_9MpF_EIj6TmUsHxGkRj4RqwviiuP3Cq_3aNa6MPYWqudQLmeO2V9cAtAP3KIllOagCHc.jpeg)

The tool will now show you any sitemap-related issues. Like these:

- Sitemap.xml not found
- Sitemap.xml files have format errors
- Incorrect pages found in sitemap.xml
- Sitemap.xml files are too large
- Sitemap.xml not indicated in robots.txt
- HTTP URLs in sitemap for HTTPS

Hover over “Why and how to fix it” to learn more about an issue. And find out what steps you can take to address it.

Staying on top of any issues will help you maintain your Shopify site’s health and SEO performance.
