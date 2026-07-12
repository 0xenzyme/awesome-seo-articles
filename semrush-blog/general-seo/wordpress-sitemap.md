---
title: "WordPress Sitemap: How to Create, Check, and Submit One"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "wordpress-sitemap"
url: "https://www.semrush.com/blog/wordpress-sitemap/"
canonical: "https://www.semrush.com/blog/wordpress-sitemap/"
author: "Asif Ali, Vlado Pavlik, Lidia Infante, Simon Fogg"
published: "2021-09-07T13:30:00+00:00"
updated: "2024-12-10T16:43:00+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2024_watch"
  - "time_sensitive_title"
schema_genre: "General SEO"
fetched_at: "2026-06-12T21:25:06+00:00"
status_code: 200
html_hash: "938a7440696cc52b6323ea9612d50468bfead384f70b01398ae07f51479a7106"
clean_word_count: 1558
clean_char_count: 12601
---
# WordPress Sitemap: How to Create, Check, and Submit One

## What Is a WordPress Sitemap?

A WordPress sitemap is an XML file that lists every URL on a website that should appear in search results.

An XML sitemap helps search engines crawl a website more efficiently.

A typical XML sitemap might look like this:

![sitemap in xml format](https://static.semrush.com/blog/uploads/media/eb/31/eb31f86862ceaac811b5b3859d368a5e/c2e523888dddfaeeae925b64b3f83b10/AD_4nXeH8NX9MF8DQOzBW28n-wvWe2slvC10zVwE4j-5YKIaNA7sgO65-1q6Qm4y9eJ3GO_Obs1tuOm6IhaTiNPwpZOCSgbmHW11Mxs_9lCd7l0wt4o8x3beNJPiA9dsMssP5FupzKGz.jpeg)

As of [WordPress version 5.5](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/), WordPress will automatically generate a basic sitemap.

To access this sitemap, add "/wp-sitemap.xml" to the website address. For example:

https://www.yourdomain.com/**wp-sitemap.xml**

This WordPress sitemap URL updates each time you publish or update a page.

However, the default XML sitemap only provides basic functionality. Many WordPress site owners use a plugin to create a more robust and customizable sitemap.

### WordPress XML vs. HTML Sitemaps

XML sitemaps are designed for search engines, not human visitors. Users can’t see them when they browse your site.

HTML sitemaps are designed for human visitors. These sitemaps consist of webpages that display a hierarchical list of selected pages on your site. They function like a table of contents and help users navigate your content.

Below is an example of a typical HTML sitemap:

![HTML sitemap listing links to pages](https://static.semrush.com/blog/uploads/media/fd/18/fd18e9a00d710ffc0f6ecf0094f77bb1/4517420b2cfacf9a2aaf3f5e254eaf2e/AD_4nXeaXL1Zlf1rznR8cbtxnFKW8KwVSe_AplgK6S09LmE0A4Uo9JK7x4lnslLEX6JAHIKc-NYcqBTTxlwr4EuMGfCUEI-jTh6vfIKOQB3QrOoryBBZWXop00Xu9SShU4mXMq_cOlvv.png)

## Why Are Sitemaps Important for WordPress Websites?

Sitemaps are important for WordPress websites because they help search engines find and index the website’s URLs.

Sitemaps also make crawling more efficient and show when pages have been updated, allowing search engines to understand your site’s structure.

While not [strictly required](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview), using an XML sitemap is a technical SEO best practice. It’s especially useful for WordPress sites with complex structures that include many posts, pages, or custom post types.

A sitemap is particularly helpful if:

- Your site is new and has few backlinks
- Your site has many pages (500-plus)
- Your site features numerous images or videos
- Your internal linking isn’t strong

Even if these conditions don’t apply, a sitemap can still provide extra details for search engine crawlers. For example, it can show when you last updated a page or list available language versions of your content.

By default, WordPress provides a basic XML sitemap. However, using a plugin offers more customization and additional features. We’ll explain how to do this next.

## How to Create a WordPress XML Sitemap with a Plugin

You can create a WordPress XML sitemap using a dedicated plugin. There are two main categories of WordPress sitemap plugins:

- All-in-one SEO plugins
- Specialized sitemap plugins

Two popular options in these categories are **Yoast SEO** and **XML Sitemap Generator** for Google. This guide will explain how to generate a sitemap in WordPress using both plugins.

### Generating a Sitemap with the Yoast SEO Plugin

[Yoast SEO](https://wordpress.org/plugins/wordpress-seo/) is a well-known all-in-one SEO plugin that also creates an XML sitemap.

![Yoast SEO plugin overview](https://static.semrush.com/blog/uploads/media/52/7c/527c550ba45e5ccff3f2faf7457f2df1/fdf383918b97f6ce51820538fd1fbe57/AD_4nXdM7c4O4Pk9CdMxXR--ZHE736pohOVtstynklY66mdp2_uWJ05rs-ia0BDrPOsQF4WmPqf9GTDNMkOj3JsDnN287sxg5XjaY6LNbPx7qIVJFCvUt1H612tzrcJYgQs59XtUMpUcZg.png)

To install Yoast SEO, open the WordPress dashboard and select “**Plugins**” > “**Add New**.” Search for “Yoast SEO” and click **“Install Now**.” Then click “**Activate**.”

![Yoast SEO plugin installed and Activate button highlighted](https://static.semrush.com/blog/uploads/media/f4/c5/f4c54c41f5774b32b6ea078ea37c876d/c5a9da7e20e35a5f45c1994e57756164/AD_4nXe_Ejq5xGoUdFsA3UCgv-IK6jfQwqUGCNlRyyV8cUOtna-C7BC2uxHM5xfhhPaoGUksYQH_Rp1WkZN6MwbYHZQ0KADfS2VH4OaTMb1MsVvaxSkRCbKrTcoShI87gQTsf6z1XCxlxw.png)

Open Yoast SEO settings and locate the “XML sitemaps” section. Click “**View the XML sitemap**” to see your new WordPress sitemap in a new tab.

![Yoast SEO plugin APIs settings section with View the XML sitemap button highlighted](https://static.semrush.com/blog/uploads/media/62/3c/623c606c3caae1fa8a6c6bd962a20438/759a9d89b7347850cace89f2e096cd5f/AD_4nXfpsIIhlqiUeJgfPn0VaXmfBKVIRePfXBe1p1SMrynPbUy_nhqCf3gWNNPpaMLwYXrO9CzlF-v3PEV5f9Ccya_BAVZaj0BM6dTRicjCXTPsIM9b32aFLxJwoag8DIdxKvTMXz1vPg.png)

You can also view the sitemap by appending “sitemap\_index.xml” to your domain: yourdomainname.com/**sitemap\_index.xml**

This sitemap includes multiple sitemaps for different content types. By default, Yoast SEO creates separate sitemaps for posts and pages.

Below is an example of a post sitemap:

![Posts sitemap generated by Yoast showing list of URLs with images and last modified date](https://static.semrush.com/blog/uploads/media/c1/2e/c12e1a7b5e24966196deb13b78ca7c76/1065975cd282ec85ab8312ee5ed5c040/AD_4nXctAXgImUhMZak56OfvwJS2UadXqnxGDm35WieaeDfC6cNo67mfA626Kw18dtnOKrkicySv3xecq2dCkfJPnHR5EYJ37FGFZMc5k0PYtw4ChTVRWkDqlPR0kqcTnjKCSiXw3rr00g.png)

The Yoast SEO plugin follows established sitemap best practices:

- It adds a link to the XML sitemap in the [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) file
- It splits large sitemaps into smaller ones and links them in a sitemap index (for example, separate sitemaps for pages, posts, and categories)
- It includes image information in the sitemap
- It adds a “lastmod” date for each URL, indicating the most recent update
- It automatically removes “[noindex](https://www.semrush.com/blog/robots-meta/)” pages from the sitemap

### Generating a Sitemap with the ‘XML Sitemap Generator for Google’ Plugin

The [XML Sitemap Generator for Google](https://wordpress.org/plugins/google-sitemap-generator) plugin is another free and simple option for creating a WordPress XML sitemap.

![XML sitemap generator for Google WordPress plugin](https://static.semrush.com/blog/uploads/media/d3/f5/d3f5662e5a2478d4e29dfc8c67b90ea6/fd15a3790901d80db609c5c32f4401a0/AD_4nXcBT6G7E18WEeE926eQc5o12lq2VT3MqwQdMha-FA7baJ_DPKHOCaSYfA5PWhzE5zEblopgseKb3k9C0a20me5ZT2hb29w5nhGcuoBykHQ7jStV5owxLB0AStl54tpL9fGYWRp4tg.png)

After installing the plugin, it immediately generates the sitemap.

To adjust settings, go to “**Settings**” > “**XML-Sitemap**.” The default settings are generally sufficient, but you can modify them if needed.

![xml sitemap settings](https://static.semrush.com/blog/uploads/media/ac/c1/acc116fa5af3b956a096a3d2d5575ae2/f39f0a0a2be0e9d757c680c7e83d479a/AD_4nXf_F9nS6Vl1lNCZoZ3xFCa_6hDdaUpWtJiEI8sXLAYRocLYVYG79JDRPYfALYUczZPne6xNJoN8A1ixMUx4WDZC4ij9MMl4of7hwEgzJhV4MOOoWSuzTKvV4ROCtYViRihb5cddHA.jpeg)

To view the sitemap, click the link at the top of the plugin’s settings page.

The sitemap URL will be https://yourdomain.com/**sitemap.xml**.

Below is an example of what the sitemap looks like:

![XML sitemap index generated by plugin showing URLs of sub sitemaps and last modified dates](https://static.semrush.com/blog/uploads/media/a6/ea/a6ea6ecafbf04bfb12f6342a19a3c167/21b7f557af514218fb738221b2017927/AD_4nXf91WxJ5SOQSyuPTxJtx5WoZzEve6eE7dUAJezHdxyZnhidyBdbHlVusevKx4tJ9Mj_hPOCQFjhZ-wvbYMjnJxf4SEyI3e_PTmC9GD0pC-O8bAIF1kKwUKVcH_Dq0-eJjDEIWqXuw.png)

## How to Submit Your WordPress XML Sitemap to Search Engines

After setting up your sitemap, submit it to Google and Bing. This step is optional, but it can help search engines discover and crawl your site more quickly.

### Submitting Your Sitemap to Google

1. Log in to your Google Search Console account.
    (If you don’t have an account, see the [Google Search Console guide](https://www.semrush.com/blog/google-search-console/) for instructions.)
2. In the left menu, click on “**Indexing**” and then select “**Sitemaps**”
3. Enter the URL of your sitemap and click “**Submit**.”

![google search console sitemaps](https://static.semrush.com/blog/uploads/media/40/4f/404ff41faa71d87b79d3ace39a75963d/90bc2b16acebe2255fdbc03eeee5d6ec/AD_4nXcQ0QCJzT7fVAvsX52aR9YnukwcXGNeUSz_wyGM6kP_Va7EAeZRTIRpixP4hosPn5iX19kuOA9ksv7zmme-5XtdiTvBTZ6w3hL_cpkD3DHmb9e11ZHSlfHaXEgNwebS8pC3rWoauw.jpeg)

Google may take several days to process your sitemap. When indexing finishes, the "Sitemap" report will show a green "Success" status.

If you’re using the default WordPress sitemap or a plugin-generated sitemap, you shouldn’t encounter issues. If Google finds errors, follow the on-screen instructions to fix them.

![Submitted sitemaps table in search console with Success status highlighted](https://static.semrush.com/blog/uploads/media/cc/b5/ccb5295317438387bc9276026ca30b6a/e6edda455888171e36a862ca74a1e13b/AD_4nXeOfQnILILLnnpEipleGk0577wM8XGdnWqwoODPXbXFxMmb5gSfW1QuK4pX87sKYa-n1w3oY_VKRaaBv6HxqjJ6yW_YjKsn29JhrjojAhzs9r9pScWCWyE1yWH4-MjHjlflOLOpGw.png)

### Submitting Your Sitemap to Bing

1. Log in to your Bing Webmasters Tools account
2. In the left sidebar, select “**Sitemaps**”
3. Click “**Submit sitemap**”
4. Enter the URL of your sitemap and click “**Submit**”

![Sitemap URL entered and Submit button highlighted](https://static.semrush.com/blog/uploads/media/91/62/9162b8a6401e246a21dbc3a066fec3c3/a66624fd2af9d2fbbb08242657e06abe/AD_4nXeJ1CtL7LB0KSqJJw0_Sqg-jQPK7qpiAXHT5KDX1hRtrHoIQXO06Dmh5mUY7Io4LgY07pSS9ktBB-aKRdwhR8NKHUmbC6koeMcXyxO_uodkDCTDwFhCWOpxQyFNTuyoEBN2t9CzDw.png)

Bing may also take a few days to process your sitemap. Once it finishes, you’ll see a "Success" status.

![Sitemap details table with Success status highlighted](https://static.semrush.com/blog/uploads/media/ab/ca/abca932723ac8c01a4934447384d2d41/a1a32522d8665e834e95c3df207063c6/AD_4nXc3Kb0ifGXZIjYG2YrvT-L6t2pNS6O8hVc41g2OxtLhS4e23YEggrX_vVtdDAgMsscZmzUql7jHeexYOKAceWXzAFeDSWo-MaiFhB4U-i0W-LpV8_OMkjNkKi8zwq5xhAyWq-cXMQ.png)

## How to Check Your WordPress XML Sitemap

To confirm that your WordPress sitemap works correctly, use a website crawler such as Semrush [Site Audit](https://www.semrush.com/features/site-audit/) tool.

After the crawl finishes, the tool will alert you. Go to the “**Issues**” tab to see a list of all detected site errors.

![site audit issues report](https://static.semrush.com/blog/uploads/media/ac/ad/acad232fd14fedb126153205709401fb/363e3173f1d35f7f6b65a69b9d5581da/AD_4nXeOls7N2Z0abrg1kOkxxGaw79wflZoH9YPfcsElPb5NVsozcihDVpVbm2BfYvGKZnaG3oA86FhcXL3vOzrbgs0l03j0SyWm9my3gQPgI0q1z6hl0VnLKtH6uY1b2-bPWt2pT1_YlA.jpeg)

Type “sitemap” into the search bar. Site Audit will highlight any sitemap-related errors and categorize them by priority.

![site audit sitemap errors](https://static.semrush.com/blog/uploads/media/78/d7/78d7c165111aedc32c8568f84dfd1e30/47d6916b3631794f2ac0ffce1c989318/AD_4nXcgmO7ReqUa-WTjqK1dYqU_XzYYWEUGSJuMqtXwZ0cPnaDOnVuIAyUDSxv7IppJMzbE-PTlEtN6-T98lnBCYOL1MoIkDs20DyTimCF2HOLDkSZGGgYVyyktEjc3oDxnzOByAKUp.jpeg)

Some common sitemap issues include:

- Sitemap not detected
- Sitemap format errors
- Sitemap contains incorrect pages
- Sitemap file is too large

If you find a sitemap issue, click the “**Why and how to fix it**” link. This provides an explanation and recommended solutions.

![site audit how to fix sitemap](https://static.semrush.com/blog/uploads/media/10/1c/101cf2ca59c6d2559b71b84a2cbbf4f4/ac9f459d4057004d25705a5ebf559372/AD_4nXeNKPcsfmbS1UAF0VglEKsYVDmVVc4hQAL9Ec3eahmdZqQrOY3BNtiwWeDMzjpTV7yMSHIvm9mOWpBUI3id0axYuQKCYPDp33q4QJy9lBtZaUaUQrY2k1A0s8sOP7WjozKa9oU2yA.jpeg)

To learn more about improving the technical health of your site, review our [technical SEO audit guide](https://www.semrush.com/blog/technical-seo-audit/).

## Make Your WordPress Website Easy to Crawl for Search Engines

Search engines will eventually find and index your pages on their own.

However, you can help them discover and crawl your pages faster by providing an XML sitemap with current URLs from your WordPress site.

Choose from several free or paid WordPress sitemap plugins to generate your sitemap. After creating one, test it using Semrush’s [Site Audit](https://www.semrush.com/siteaudit/). Sign up now for a free trial.
