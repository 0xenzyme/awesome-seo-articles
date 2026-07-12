---
title: "What Is AMP? A Beginner’s Guide to AMP Pages & SEO"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "amp-pages"
url: "https://www.semrush.com/blog/amp-pages/"
canonical: "https://www.semrush.com/blog/amp-pages/"
author: "Carlos Silva"
published: "2021-03-24T08:05:00+00:00"
updated: "2023-06-05T18:00:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T13:44:19+00:00"
status_code: 200
html_hash: "afcaa6df6fb5b971ea71a44c7159e19e9d2a31f12f58f00946657d87ff827961"
clean_word_count: 2057
clean_char_count: 13595
---
# What Is AMP? A Beginner’s Guide to AMP Pages & SEO

## What Is AMP?

AMP (previously known as Accelerated Mobile Pages) is an open-source HTML framework that helps
create fast-loading mobile-optimized webpages.

So, an AMP page is, essentially, a stripped-down version of a
regular webpage.

And it can look like this:

![regular mobile page vs accelerated mobile page infographic](https://static.semrush.com/blog/uploads/media/3b/26/3b2634f621365e73c8eb314999ee11b1/image.png)

Google spearheaded the open-source project to compete against Facebook Instant Articles and Apple News.

Both of which allowed publishers to create content that loaded fast and was easy to consume.

Google first
served AMP pages in mobile search results in 2016. And they were restricted to a “Top Stories” section at the top of
the SERPs.

Like this:

![AMP pages in mobile search](https://static.semrush.com/blog/uploads/media/08/cb/08cbcf75c7164b62ce62395b4f004998/image.png)

It was originally designed for news publishers. But has since expanded to include all types of webpages.

## How Does AMP Work?

The AMP framework consists of three basic components:

1. AMP HTML
2. AMP JavaScript
3. AMP Cache

### AMP HTML

AMP HTML is HTML with certain restrictions to ensure pages load quickly. It removes or modifies
some elements and attributes that can slow down webpages.

A simple HTML file can look like this:

![a simple HTML file example](https://static.semrush.com/blog/uploads/media/49/37/493759ef9fd20f85d224ebc4012b5544/image.png)

Fundamentally, AMP HTML documents must:

- Start with `<!doctype html>` (to send information to the browser
  about what type of document to expect)
- Include a top-level `<html ⚡>` or `<html
  amp>` tag (to indicate it’s an AMP HTML page)
- Include `<head>` and `<body>` tags (to define the document’s content, i.e. headings,
  paragraphs, images, hyperlinks, tables, etc.)
- Include a `<link rel="canonical" href="URL">` (to indicate the
  regular HTML version of the page or to link to itself if no regular page exists)
- Include a `<meta charset="utf-8">` tag (to specify the character
  encoding)
- Include a `<meta name="viewport" content="width=device-width">` tag
  (to give the browser instructions on how to control the page's dimensions)
- Include a `<script async src="https://cdn.ampproject.org/v0.js"><script>` tag
  (to add extensions to the base library)
- Include the [AMP
  boilerplate code](https://github.com/ampproject/amphtml/blob/main/docs/spec/amp-boilerplate.md) (`head > style[amp-boilerplate]` and `noscript > style[amp-boilerplate]`) in the head tag

For more details regarding special tags, attributes, and templates, check out AMP’s official [AMP HTML documentation](https://amp.dev/documentation/guides-and-tutorials/learn/spec/amphtml#ampd).

### AMP JavaScript

JavaScript is tricky because too much JS can make webpages slow and unresponsive.

However, AMP’s [JavaScript
library](https://amp.dev/documentation/guides-and-tutorials/develop/custom-javascript#enhance-amp-components) contains frameworks and components that let you build pages quickly without writing JS or importing
third-party libraries.

All of which are crucial to the reader’s experience.

### AMP Cache

The AMP
Cache is a proxy-based content delivery network (CDN) that pre-fetches and pre-renders AMP pages before they’re
requested by users.

And it’s game-changing for site speed.

Why?

Because it lets your site load
multiple parts from different servers at once. And it also allows visitors to load your site from the server that is
closest to them.

Meaning your website loads super fast for more people.

And there are currently two
main AMP Cache providers:

- [Google AMP Cache](https://developers.google.com/amp/cache/)
- [Bing AMP Cache](https://www.bing.com/webmaster/help/bing-amp-cache-bc1c884c)

These platforms cache your pages when you use the AMP format.

For example, cache providers can discover
your AMP page via the `<html ⚡>` or `<html
amp>` tag and cache its content.

Or a publisher can manually add the page to the AMP Cache (only
applicable to the [Google AMP Cache](https://developers.google.com/amp/cache/update-cache)).

Other
platforms can access cached AMP pages via their URL.

For example, if you put /amp at the end of any news story
on The Guardian, you’ll see the AMP version.

Like this:

![AMP page from The Guardian](https://static.semrush.com/blog/uploads/media/e0/9f/e09fd987082475926c8685ebd07172a0/image.png)

**Pro tip:** *If you’re not sure if your site has AMP pages, you can check using Semrush’s
[Site Audit Tool](https://www.semrush.com/siteaudit/).*

Start by adding your domain name and
clicking “**Start Audit**.”

![Site Audit Tool](https://static.semrush.com/blog/uploads/media/83/d6/83d6cb73a1c2c4745e691a67f771ac4d/image.png)

Then, head to the “**Statistics**” tab in your dashboard and you’ll see a row that says “AMP
Links.”

Like this:

![“Statistics” tab in Site Audit Tool](https://static.semrush.com/blog/uploads/media/d1/d6/d1d6fcfd461183fe60acb36905fefae3/image.png)

## What Are the Advantages and Limitations of AMP Pages?

While
AMP can improve your page’s performance and user experience, it also has certain disadvantages.

Let’s take a
look at the pros and cons of AMP pages:

### AMP Advantages

- Page loading is almost instant
- Pages are easy to build
- Improves user experience on mobile
- Allows custom designs
- Multiple platforms, including Google and Bing support it

### AMP Limitations

- Google no longer displays the AMP badge icon to indicate AMP content
- Design elements are very restricted
- AMP pages allow only one advertisement tag per page

![Advantages and Limitations of AMP Pages infographic](https://static.semrush.com/blog/uploads/media/51/a9/51a9c46257a31c9990e13ce02b8881c4/image.png)

## How to Set Up AMP on Your Website

You can create AMP pages by following the HTML markup or by using
a CMS (through a plugin or custom functionality).

### Create Your HTML AMP Page

#### Basic Code

To
start, here’s the markup of a basic AMP page:

`<!doctype html>
<html amp lang="en">
<head>
<meta charset="utf-8">
<script async src="https://cdn.ampproject.org/v0.js"></script>
<title>Hello, AMPs</title>
<link rel="canonical"
href="https://amp.dev/documentation/guides-and-tutorials/start/create/basic_markup/">
<meta name="viewport"
content="width=device-width,minimum-scale=1,initial-scale=1">
<style amp-boilerplate>body{-webkit-animation:-amp-start 8s
steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s
steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes
-amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes
-amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes
-amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes
-amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes
-amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style
amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-
animation:none;animation:none}</style></noscript>
</head>
<body>
<h1 id="hello">Hello AMPHTML World!</h1>
</body>
</html>`

As you can see, the body content is straightforward, but there’s additional code in the head.

**Tip:**
*use AMP’s [snippet
“playground”](https://playground.amp.dev/?url=https%3A%2F%2Fpreview.amp.dev%2Fdocumentation%2Fguides-and-tutorials%2Fstart%2Fcreate%2Fbasic_markup.example.1.html%3Fformat%3Dwebsites) to dabble with and practice with the code.*

#### Adding Images

If you want to add
an image, you need to replace the regular HTML tag with the AMP equivalent.

In this case, the `<amp-img>` tag instead of `<img>`.

To test it out, copy and paste the following code into your
page’s <body>.

`<amp-img src="https://source.unsplash.com/random/600x400" width="600"
height="400"></amp-img>`

#### Adding Style

The next step is adding style.

Any styling has to be done using CSS properties.
But, AMP states that all CSS be included within a custom tag, called the `<style
amp-custom>` in the `<head>` of the document.

For
example, try adding the following style to your page:

`<style amp-custom>
h1 {
margin: 1rem;
}
 body {
background-color: green;
}
</style>`

#### JavaScript

AMP allows custom JavaScript through the `<amp-script>` component.

It lets you write and run your own JS in a
way that maintains AMP's performance guarantees. And build pages quickly without coding JavaScript or using external
libraries.

For more in-depth information, read AMP’s [guide to using custom
JavaScript](https://amp.dev/documentation/guides-and-tutorials/develop/custom-javascript/) and follow their [AMP JS tutorial](https://amp.dev/documentation/guides-and-tutorials/develop/custom-javascript) to get
started.

#### Review and Validate

A valid AMP page means it follows strict guidelines that ensure it’s
eligible for caching and it creates a great user experience.

Before validating your AMP page, make sure you
follow these best practices:

- If you’re optimizing for Google, follow their [guidelines for AMP pages](https://developers.google.com/search/docs/crawling-indexing/amp)
- Link your AMP pages to their [canonicals](https://amp.dev/documentation/guides-and-tutorials/optimize-and-measure/discovery?referrer=ampproject.org)
  (non-AMP version, or the AMP page itself)
- Use the same [structured
  data markup](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) in the AMP and canonical pages
- Verify the structure data works by using the [Rich Results
  Test](https://search.google.com/test/rich-results)
- Verify your [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) file doesn’t block
  your AMP page
- Follow international SEO [hreflang](https://www.semrush.com/blog/hreflang-attribute-101/) guidelines

And when you’re ready to review, use the [AMP Test Tool](https://search.google.com/test/amp) to make
sure your page meets all requirements.

![AMP Test Tool](https://static.semrush.com/blog/uploads/media/8b/35/8b35f9e83c328314912e71254cf4235c/image.png)

For a more detailed guide, check out [AMP’s official
tutorial](https://amp.dev/documentation/guides-and-tutorials/learn/validation-workflow/validate_amp) for validating AMP pages.

And if you’re new to web development, use [AMP’s courses](https://amp.dev/documentation/courses/) or Google’s [AMP foundations
codelab](https://codelabs.developers.google.com/codelabs/accelerated-mobile-pages-foundations/#0).

### Create Your AMP Page With a CMS

If you manage your content through a CMS, you can use [Drupal](https://www.drupal.org/project/amp), [Joomla](https://extensions.joomla.org/tags/amp/), or [WordPress](https://wordpress.org/plugins/amp/).

For example, let’s see what this looks like using [AMP for WP](https://wordpress.org/plugins/accelerated-mobile-pages/).

![AMP for WP plugin](https://static.semrush.com/blog/uploads/media/16/55/1655acb801ae768c5ccd2e044a98e35b/image.png)

After activating the plugin on WordPress, you can begin creating your Accelerated Mobile Pages.

Start
by adding a new page or new post.

!["Add New" page in Menu](https://static.semrush.com/blog/uploads/media/ff/cc/ffccfbcb8e764f13982b85837b32b33f/image.png)

Then click “**Start the AMP Page Builder**.”

![“Start the AMP Page Builder” button highlighted](https://static.semrush.com/blog/uploads/media/80/b9/80b9cc1a37072a8769e44eb4fec148ef/image.png)

You can choose to use pre-built layouts or build your own using drag-and-drop elements.

![AMP Page Builder drag-and-drop elements](https://static.semrush.com/blog/uploads/media/75/e0/75e09117f4a2a916c9288337559c5342/image.png)

Then click **the gear icon** to edit the elements of your page.

![the gear icon highlighted](https://static.semrush.com/blog/uploads/media/ef/60/ef6091501746d54e75741a6cd78aa043/image.png)

And save each module as you go.

!["Save Module" button](https://static.semrush.com/blog/uploads/media/80/ae/80aef290e4d8e486964d8b4b4151081a/image.png)

Once you publish the page, you’ll see the AMP version of the page by adding “amp” to the end of your page’s
URL.

![AMP version of the page example](https://static.semrush.com/blog/uploads/media/f6/32/f632433362bf1381436f735ffa6e5212/image.png)

## Monitor and Improve Your AMP Pages

One of the best ways to monitor and improve your AMP pages is to
periodically audit your site. It’ll help keep track of any HTML, templating, and style and layout issues.

Start by running your site through our [Site Audit](https://www.semrush.com/siteaudit/) tool.

**Tip:** *[Create a free Semrush account](https://www.semrush.com/signup/) and crawl up
to 100 URLs of any domain, subdomain, or subfolder.*

![Site Audit Tool](https://static.semrush.com/blog/uploads/media/02/da/02da5d9bec05ea94c867a784f0859173/image.png)

Once you crawl your site, head to the “**Statistics**” tab. You’ll see issues in the row
labeled “AMP Links.”

![“Statistics” tab in Site Audit](https://static.semrush.com/blog/uploads/media/1c/7c/1c7cc6184d318e1d7905a759c0123d8f/image.png)

The tool checks for over 40 of the most common [errors](https://www.semrush.com/blog/fixing-amp-validation-errors/) related to AMP pages. And tells you
how to fix them.

![Why and how to fix issues with AMP pages section](https://static.semrush.com/blog/uploads/media/ca/a2/caa273281ab9ccf43806d0273ed9ebf2/image.png)

Resolve any issues as soon as possible. They can affect how search engines serve your content to
searchers.
