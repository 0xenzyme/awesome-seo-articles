---
title: "HTML Link Tags Explained (+ All Attributes and Values)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "html-link-tag"
url: "https://www.semrush.com/blog/html-link-tag/"
canonical: "https://www.semrush.com/blog/html-link-tag/"
author: "Dana Nicole, Bartłomiej Barcik, Martha Vassallo"
published: "2021-05-20T04:08:00+00:00"
updated: "2024-03-12T09:27:00+00:00"
categories:
  - "On-page SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "On-page SEO"
fetched_at: "2026-06-12T16:56:45+00:00"
status_code: 200
html_hash: "be114b165e00b2e22c2ac5703e83f1899f2cdb1554311e22ab33bde1c05abf41"
clean_word_count: 2398
clean_char_count: 17400
---
# HTML Link Tags Explained (+ All Attributes and Values)

HTML <link> tags help define relationships between resources on your website.

In this post, we’ll explore what HTML link tags are, how to use them, and common mistakes to avoid when adding them to your site or webpage.

## What Is an HTML Link Tag?

The HTML <link> tag is an [HTML tag](https://www.semrush.com/blog/html-tags-list/) (a piece of code) that establishes connections between the document you’re on and its external resources (files or other assets).

You should place HTML link tags in an HTML document’s <head> section. Like this:

`<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
   <!-- The content of your webpage goes here -->
</body>
</html>`

Browsers that currently support HTML link tags include:

- Chrome
- Edge
- Safari
- Opera
- Firefox

Browsers that don’t support HTML link tags might not render them properly. Meaning they might ignore the tag altogether and display nothing at all.

## 7 Uses of the HTML Link Tag

Let’s look at a few common examples of link tags in HTML.

### 1. Link an External Style Sheet

An external style sheet is a file with Cascading Style Sheets (CSS) code. This code defines the styles and layout of a webpage—like background color.

For a style sheet to work, you must link it to the page you’d like to style. Otherwise, the browser won’t know about it and won’t display as you’ve intended.

Here’s how you can use the HTML link tag to link to the style sheet:

`<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
   <!-- The content of your webpage goes here -->
</body>
</html>`

### 2. Display a Favicon

A favicon is a small icon displayed in the browser’s tab or bookmark.

Here’s one:

![Semrush favicon](https://static.semrush.com/blog/uploads/media/44/b6/44b6da61d3f1b5528b27d3bc3aeed12d/70fe88531aa9961ec2fb7ae96f5489f1/oxy4e_KPYWdnD1ibBL6wmZSXNgiPYgBUBuGNC487DeY3esY9GzKTABl9iLCDeMplyn55pRj_CVgUSmoq5YMdNT6Raa_OBrJL5B1DGRj4JRFZomqdXOWGWW349YoHxT1gniHgSxEZ20kOEu9AUL47Vn4.png)

Use the HTML link tag like in the example below to display your favicon across various browsers:

`<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="icon" href="favicon.png">
</head>
<body>
    <!-- The content of your webpage goes here -->
</body>
</html>`

### 3. Set a Canonical URL

A [canonical URL](https://www.semrush.com/blog/canonical-url-guide/) indicates the primary version of a webpage when [duplicate content](https://www.semrush.com/blog/duplicate-content/) exists across the site. And tells search engines which page to prioritize and rank in organic (unpaid) search results.

To specify a canonical page, use the HTML link tag like this:

`<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="canonical" href="https://www.example.com/canonical-page">
</head>
<body>
   <!-- The content of your webpage goes here -->
</body>
</html>`

### 4. Set the Language of a Page

The [hreflang attribute](https://www.semrush.com/blog/hreflang-attribute-101/) specifies the language and (optionally) intended region of a document. Which is useful if you have content in different languages.

Why?

Because with the hreflang attribute, search engines can display the most relevant search results to users in different countries.

For example, if you Google “semrush blog” in the United States, you’ll see this result:

![Google's result for “semrush blog” in the United States](https://static.semrush.com/blog/uploads/media/85/a5/85a5a11f0ff401ed307e96c56c836773/e82832dfd0406956516b9d94f2de3c45/tDZNMHJ7S5CepaTmuvE02dBl8kSbMuTKz55HXuM2D5ovVQoUbiVnAUYEFW-1s0KUGz71CvH7ASF-OdZeqtdzYPzuE3sxEKD8x-yj3tgqA2dCS_JY4ZjK5onOCa2OahKw39wHuFiY-UWf1kJPtZwQVf4.png)

But if you’re in Spain, you’ll see this:

![Google's result for “semrush blog” in Spain](https://static.semrush.com/blog/uploads/media/fb/27/fb273625130d4a5098333927633dab83/60a773c2bf91244c7d0232fc5500c4c9/45GIMX_LXGmF-MLPGTYGxECusC9z0HeYAZlGWRUTU2PUp-J0llTO8IyUiuue5ErEFknQwrSFRGycBxGrfvtS5W4FNgY6Ph-JOQTIYszdnilqrSyawSupCzeSSSvdnu6NlwIyD7YIQ5hK0NOHjP4ZOQU.png)

You can define pages for different countries and languages using the HTML link tag as shown below (this one has alternate Spanish and French versions):

`<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="alternate" hreflang="en" href="https://example.com/page">
    <link rel="alternate" hreflang="es" href="https://example.com/es/page">
    <link rel="alternate" hreflang="fr" href="https://example.com/fr/page">
</head>
<body>
   <!-- The content of your webpage goes here -->
</body>
</html>`

### 5. Preload Specific Resources

Preloading instructs browsers to request and store a resource in its cache right when (or soon after) the page starts loading. Which can improve a website’s performance, speed, and user experience.

A common preload request is for fonts. And you can set a font to preload with an HTML link tag like this:

`<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Preload fonts -->
    <link rel="preload" as="font" type="font/woff2" href="your-font.woff2">

    <!-- Link to the external style sheet using the font -->
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
   <!-- The content of your webpage goes here -->
</body>
</html>`

You can set resources to preload on a page-by-page basis.

### 6. Connect Your RSS Feed

A Really Simple Syndication (RSS) feed is a way for websites to share content and updates.

And users can subscribe to different websites through RSS feed readers like this one:

![A Really Simple Syndication (RSS) feed](https://static.semrush.com/blog/uploads/media/c9/2b/c92ba1e1cc810404823c03a6add122e3/b1142e0085efab7e16fc395636b26c73/Elzg25Ct0sVqWBsAoIuPbb184DKQ8iSeZ8SFCc-l0iRAJXTGoFx3sa7IJz5S8JfpuKynCdAkKQuzNDZUIVRc9JjvXPX14cEZEHW5q75nsoKgHSQPZc9zzrlOjsA6jcc_a4SOTJp9C3BZfoD0quK_LeQ.png)

This lets them see when sites publish new content.

Use the HTML link tag to link to your RSS feed so a user can subscribe to your feed.

`<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="alternate" type="application/rss+xml" title="RSS Feed" href="rss-feed.xml">
</head>
<body>
   <!-- The content of your webpage goes here -->
</body>
</html>`

### 7. Link to External Fonts

HTML link tags let you link to external fonts (like those in Google Fonts) to use on your site.

Here’s the code to use:

`<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Link to an external font from Google Fonts -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans">
</head>
<body>
   <!-- The content of your webpage goes here -->
</body>
</html>`

## Additional HTML Link Tag Attributes and Values

Link tag **attributes** provide additional information and go between the opening and closing tag.

And **values** indicate the specific content assigned to an attribute.

![Link tag attributes and values](https://static.semrush.com/blog/uploads/media/7a/f8/7af84a380846ace996df870da4a8acf2/5d7a45f1198189f241c1aa857aa1a595/t8uCldUdNChvFgCVUsiljAU0IUFgIpuyfKJDNzkfwRTOt8ayT93hkZbzsoBHtDmYeg4ffBbq7lHgs9V9N1IS3II8ppx_huOYlYChhF_m5JVhyZ4uqw1rkqJ2E6oPEou3bvybFHJOpQCubjM9mtUUxw4.png)

Both attributes and their values guide the HTML link tag in performing its designated tasks. In other words, they tell it how to behave.

Here are current HTML link tag attributes and their common values:

|  |  |  |  |
| --- | --- | --- | --- |
| **Attribute** | **Values** | **Definition** | **Example** |
| as | audio  document  embed  fetch  font  image  object  script  style  track  video  worker | Specifies the type or role of the linked resource. It’s required when using the “preload” attribute. | <link rel="preload" as="audio" href="audio.mp3"> |
| crossorigin | anonymous  use-credentials | Indicates whether the browser should fetch the crossorigin request as anonymous—i.e., without sending credentials (like cookies) | <link rel="stylesheet" href="https://example.com/styles.css" crossorigin="anonymous"> |
| fetchpriority | high  low  auto | Helps browsers prioritize how to fetch resources. Which can improve your site’s performance when handled correctly. | <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans" fetchpriority=”high”> |
| href | URL | Indicates the URL in absolute or relative terms of the linked resource | <link rel="stylesheet" href="https://example.com/styles.css"> |
| hreflang | You may use [ISO 639-1](https://www.iso.org/iso-639-language-code) or the [ISO 3166-1 alpha-2](https://www.iso.org/glossary-for-iso-3166.html) country and language codes | Indicates the language (and possibly the intended country) of the linked resource | <link rel="alternate" hreflang="fr" href="https://example.com/fr/page"> |
| imagesizes | Height x width  or  Percent of viewport width (vw) | Helps preload responsive images. Used only with rel="preload" and as="image." | <link rel="preload" as="image" href="example.jpg" imagesrcset="example\_300px.jpg 300w, example\_600px.jpg 600w, example\_1200px.jpg 1200w" imagesizes="50vw"> |
| imagesrcset | URL | Specifies a list of images. The browser will select the most appropriate image to display. Used only with rel="preload" and as="image." | <link rel="preload" as="image" href="example.jpg" imagesrcset="example\_300px.jpg 300w, example\_600px.jpg 600w, example\_1200px.jpg 1200w" imagesizes="50vw"> |
| integrity | cryptographic hash value | Provides a hash value for verifying the integrity of the linked resource. Which can give you an extra layer of security when loading resources. | <link rel="stylesheet" href="styles.css" integrity="sha256-BBq2K8ntPke0J1Xy2ftV07cHJZaMjRZEmmgvsq81IB4="> |
| media | all  print  screen  speech  aspect-ratio  color  color-index  grid  height  monochrome  orientation  resolution  scan  width | Specifies the type of device or screen size that the linked resource is designed for | <link rel="stylesheet" href="styles-mobile.css" media="screen and (max-width: 600px)"> |
| referrerpolicy | no-referrer  no-referrer-when-downgrade  origin  origin-when-cross-origin  unsafe-url | Specifies how much referrer information to include when fetching the resource | <link rel="stylesheet" href="styles.css" referrerpolicy="no-referrer"> |
| rel | alternate  author  canonical  dns-prefetch  help  icon  license  next  pingback  preconnect  prefetch  preload  prerender  prev  search  stylesheet | Specifies the relationship between the current document and the linked resource | <link rel="icon" href="favicon.png"> |
| sizes | Any height x width size | Used to indicate sizes of icons. It can only be used with rel=”icon.” | <link rel="icon" type="image/png" sizes="16x16" href="favicon.png"> |
| title | text | Defines the default or alternate style sheet to keep track of linked style sheets. It does not affect how the browser applies them. | <link rel="stylesheet" href="styles.css" title="Main Style Sheet"> |
| type | Various media types like:  text/css  text/javascript  image/svg+xml | Describes the media type for the linked resource | <link rel="stylesheet" href="styles.css" type="text/css"> |

## Common Mistakes to Avoid When Implementing Link Tags

Here are mistakes people frequently make when adding the <link> tag to their site. By avoiding them, you can ensure that your link tags work well and that browsers can read them.

### Adding the Tag to Page’s Body Section

The HTML link tag belongs in the <head> section of your HTML document.

Why?

Because according to [semantic HTML](https://www.semrush.com/blog/semantic-html5-guide/#types-of-html-semantic-tags), the <head> section of an HTML document is where metadata should go. (Metadata is information that describes data. And HTML link tags are considered metadata elements.)

An HTML link tag may not work as expected if you add it to the <body>.

For instance, placing your style sheet HTML link tag in the <body> section could cause a delay in loading the style of that web page.

You can check where your link tag is by viewing your page’s source code. Right-click on the page in the browser and select “**View Page Source**.”

![“View Page Source" button](https://static.semrush.com/blog/uploads/media/0e/69/0e69c6ff58da579285b32e016b11f2bb/bb6800e89e6cd385092c713af407ed16/yLqe7HwBSATRmrE8rtM5Rb5TGhLKCytp_FbfOe32DLnw3kRXox0ZaVdmban2UbAx2k-gi3dxLvzYVXttBiP2WExLshRm9D51h9mWE9zae5Io3rwO8ZlhU1eM1Rq8hHlroRosjpF4Mh2vNhYgH1nmf74.png)

Then, press Ctrl+F (Command+F on Mac) and search <head>.

![Searching for <head> in page's source code](https://static.semrush.com/blog/uploads/media/59/5c/595c04976c86f666856c3c021a0db196/acd3def3914e6a8c7c858d0c6f7cc4dc/9Oca32FUlkED8hcLZGjzEp_mZ18ws3D6TkTktdHHCpvYuw7bmPbElUjcI0lvyh-mU1DDtgmy7aiRH7HeE929_Aks5QmCtRpUvsF_wHqDcquQGQIpoM1kh-cOVjaqVb7tN73ELGtnyPAKXEk2IqXDkVA.png)

(You can also search </head> to find where the <head> section ends.)

Look through the code to ensure the link tags in your HTML are within the <head> and </head> tags. If they aren’t, either move them or reach out to your web developer for help.

### Using Incorrect Attributes or Values

You can only use specific values associated with each attribute. And some attributes can only work with other attributes.

For example, if you use “rel=preload” in your link tag, you **must** also use the as attribute.

Refer to our list of HTML link tag attributes and their values above to ensure you’re using the right ones.

### Incorporating Deprecated Attributes

Deprecated—meaning outdated—attributes may not work. Because modern browsers typically phase out support for them.

Organizations like the World Wide Web Consortium (W3C) may decide to deprecate attributes for various reasons. Like changing technology.

For example, the rev attribute was previously used to show the reverse relationship between the current document and the linked document. For example:

`<link rev="made" href="related-document.html">`

This HTML link tag indicated that the linked document (related-document.html) was made by the current document.

But because the rev attribute only accounts for reverse relationships, the [W3C deprecated it](https://www.w3.org/TR/2010/WD-html5-20100304/obsolete.html). It now advises people to use the rel attribute instead, which is more flexible.

Here’s how you’d rework the example above using the current rel attribute:

`<link rel="author" href="related-document.html">`

Other deprecated attributes for the HTML link tag include:

- **charset**: Defines the encoding of the linked resource
- **methods**: Provides information about the functions or actions that could be performed on a linked object
- **target**: Specifies whether the linked document should load in a window or frame

Check your code for any of these attributes. And replace them with something more suitable if needed.

## Check for HTML Link Tag Issues on Your Site

Use a diagnostic tool like Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) to track technical issues on your site. Including ones that arise from mistakes within your HTML link tags.

Here’s how.

Open [Site Audit](https://www.semrush.com/siteaudit/). Enter your domain URL and click “**Start Audit**.”

![Site Audit tool](https://static.semrush.com/blog/uploads/media/52/fb/52fb39255dafddd109f6bb0ed8004f72/630101d461a399d1ab7228c546803479/GiwIGdkt5bRnH0M5osYEvH-SwJy6xm_gvhrOTewmP7aDziMqir_ITrS7_9UfvaeB3Lp-HkMrLZ1Uic2xkPlbZxYGUZrniAR9f8M-5GX2xQUTySIm1nxXqbtL2p4k_IwnWHNRFx-Vx1YcrUZ3BWoAH1g.png)

This opens a menu where you can configure all your settings.

Next, click “**Start Site Audit**.”

!["Site Audit Settings" window](https://static.semrush.com/blog/uploads/media/f3/d1/f3d1092e18639da1d2701e411c86f6db/7393e5b6380825ab657474f556659c26/o-NjwN5KYZuSBGS9o7mincLzdyM3dm9vgKajgUJ86pAkBKJg7bYMYvk47fGWQGU8BvVt0JS0e1J3BHugf2fVBSaGs1kzOzydsKahl9MWY2rwUecNoef9gRoQF0Bgx4bnjATLY-hnL_TIw6ptmRmCzfU.png)

Once your audit is complete, you’ll receive a detailed report of what you need to improve.

Click on the “**Issues**” tab.

![Site Audit's overview dashboard with "Issues" tab highlighted](https://static.semrush.com/blog/uploads/media/27/2c/272c593eb35346bad209596ce7c86674/84b6a4dc551d26ff1fd554e41f9b19ea/JFwyuX4Cu5Uvw1qfx5w1RsFIUZy80pSimswS_MxVJdk2YSDtuLK_ag6gg6RJsLcH3yzNfSdRlw1mA7sT6KpTki_q2F14cjW_J9MyURUv5S68WSt_s8-0tqE5PZOAIkQOmj7ypXhCqkGr_e2JQXQWEeA.png)

This displays a list of technical issues with your site.

For example, pages with duplicate content—which would benefit from an HTML link tag with a canonical attribute.

![A list of errors found in Site Audit tool](https://static.semrush.com/blog/uploads/media/56/1f/561f31949a1ca490b83e57d1067c7ad7/764406597c2accaa217eb543bf62303e/ElzldC43fDzO2Fdu9hLUCs22zZXqdFPc438BnsdAlekJMKFl8rXlGKq_FqRgEA69LpQuMWWoL0Br9doMlMJd7Z9H6hSCNXf4gbR0wyCDcxK_xwy53ZwwgssIa46-vghftx9g0L6ocz7k_RNEN_tnkiY.png)

Site Audit also spots hreflang errors, canonical tag errors, and slow pages. (Slow pages might benefit from using the fetchpriority attribute within your HTML link tag.)

You can click “**Why and how to fix it**” next to each issue to better understand and address the problem.

Cleaning up these issues helps you create a great user experience on your site. And optimize your pages so search engines can easily crawl, index, and rank them in search results.

Try Site Audit for free.
