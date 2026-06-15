---
title: "Open Graph Meta Tags: Everything You Need to Know"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "open-graph-meta-tags"
url: "https://ahrefs.com/blog/open-graph-meta-tags/"
canonical: "https://ahrefs.com/blog/open-graph-meta-tags/"
author: "Michal Pecánek"
published: "2020-01-14T22:51:13+00:00"
updated: "2021-06-29T16:52:29+00:00"
categories:
  - "Content Marketing"
  - "General SEO"
freshness_reasons:
  - "date_2021_very_old"
fetched_at: "2026-06-12T11:54:59+00:00"
status_code: 200
html_hash: "210513440274d72be481bf8695c2b505f9959f746806307734f9c11a05ed1bdb"
clean_word_count: 1961
clean_char_count: 12092
---
# Open Graph Meta Tags: Everything You Need to Know

Are you wondering how to make your content more clickable, shareable, and noticeable on social media?

Open Graph meta tags are the solution.

Here’s how [one of our posts](https://ahrefs.com/blog/amazon-affiliate-websites/) looks when shared on Facebook **with** Open Graph meta tags:

And here’s how it looks**without**:

In this guide, you’ll learn:

- [What Open Graph meta tags are](#what-are-open-graph-tags)
- [Why Open Graph tags are important](#why-are-open-graph-tags-important)
- [Which Open Graph tags to use](#which-open-graph-tags-to-use)
- [How to set up Open Graph tags](#how-to-set-up-open-graph-tags)
- [How to test and debug Open Graph tags](#how-to-test-and-debug-open-graph-tags)
- [How to audit Open Graph tags](#how-to-audit-open-graph-tags)

## What are Open Graph meta tags?

Open Graph meta tags are snippets of code that control how URLs are displayed when shared on social media.

They’re part of Facebook’s [Open Graph protocol](https://ogp.me/) and are also used by other social media sites, including LinkedIn and Twitter (if Twitter Cards are absent).

You can find them in the `<head>` section of a webpage. Any tags with `og:` before a property name are Open Graph tags.

Here are some examples from [our guide to becoming an SEO expert](https://ahrefs.com/blog/seo-expert/):

```
<meta property="og:title" content="How to Become an SEO Expert (8 Steps)" />
<meta property="og:description" content="Get from SEO newbie to SEO pro in 8 simple steps." />
<meta property="og:image" content="https://ahrefs.com/blog/wp-content/uploads/2019/12/fb-how-to-become-an-seo-expert.png" />
```

This is how those tags look on Facebook:

## Why are Open Graph tags important?

People are arguably more likely to see and click shared content with optimized OG tags, which means more social media traffic to your website.

There are three reasons for this:

1. They make content more eye-catching in social media feeds.
2. They tell people what the content is about at a glance.
3. They help Facebook understand what the content is about, which can help increase your brand visibility through search.

Let’s touch more on that last point, as it tends to get overlooked.

Here are the results of a Facebook search for “alternative search engines”:

It brings up popular articles that people have already shared on Facebook. Each title and image comes from Open Graph tags.

Even if there are no articles returned for the search, Facebook still shows matching content shared in groups or pages you follow, or by friends.

Sidenote.

 Open Graph tags also help create a snippet when someone sends you a link through direct messages using apps that support the Open Graph protocol—naturally Facebook’s Messenger and WhatsApp, but also iMessage and [Slack](https://medium.com/slack-developer-blog/everything-you-ever-wanted-to-know-about-unfurling-but-were-afraid-to-ask-or-how-to-make-your-e64b4bb9254).

## Which Open Graph tags should you use?

Facebook lists 17 OG tags in their [official documentation](https://developers.facebook.com/docs/sharing/webmasters/), plus dozens of object types. We’re not going to discuss all of these. Only four are required for Facebook to understand the basics of your page, and there are a couple of others that sometimes help.

Let’s go through these.

### og:title

The title of your page.

#### Syntax

```
<meta property="og:title" content="Open Graph Meta Tags: Everything You Need to Know" />
```

#### Best practices

- Add it to all “shareable” pages.
- Focus on accuracy, value, and clickability.
- Keep it short to prevent overflow. There’s no official guidance on this, but 40 characters for mobile and 60 for desktop is roughly the sweet spot.
- Use the raw title. Don’t include branding (e.g., your site name).

### og:url

The URL of the content.

#### Syntax

```
<meta property="og:url" content="https://ahrefs.com/blog/open-graph-meta-tags/" />
```

#### Best practices

- Use the [canonical URL](https://ahrefs.com/blog/canonical-tags/). It helps consolidate all connected data, such as likes, across all the duplicate URLs posted.

### og:image

The URL of an image for the social snippet.

Note that this is perhaps **the most essential Open Graph tag** because it occupies the most social feed real estate.

#### Syntax

```
<meta property="og:image" content="https://ahrefs.com/blog/wp-content/uploads/2020/01/fb-open-graph-1.jpg" />
```

#### Best practices

- Use custom images for “shareable” pages (e.g., homepage, articles, etc.)
- Use your logo or any other branded image for the rest of your pages.
- Use images with a 1.91:1 ratio and [minimum recommended dimensions](https://developers.facebook.com/docs/sharing/webmasters/images) of 1200x630 for optimal clarity across all devices.

### og:type

The type of object you’re sharing. (e.g., article, website, etc.)

#### Syntax

```
<meta property="og:type" content="article" />
```

#### Best practices

- Use [article](https://ogp.me/#type_article) for articles and [website](https://ogp.me/#type_website) for the rest of your pages.
- Describe object types [further](https://ogp.me/#types) where appropriate (optional).

### og:description

A brief description of the content.

#### Syntax

```
<meta property="og:description" content="Learn about 13 features that set Ahrefs apart from the competition." />
```

#### Best practices

- Complement the title to make the snippet as appealing and click-worthy as possible.
- Copy your meta description here if it makes sense.
- Keep it short and sweet. Facebook recommends 2-4 sentences, but that often truncates.

### og:locale

Defines the content language.

#### Syntax

```
<meta property="og:locale" content="en_GB" />
```

#### Best practices

- Use only for content not written in American English (en\_US). Facebook assumes content without this tag is written in this language.

## How to set up Open Graph tags

Choose your website platform from the list below, or follow [these manual instructions](#setting-open-graph-tags-manually).

- [WordPress](#setting-open-graph-tags-in-wordpress)
- [Shopify](#setting-open-graph-tags-in-shopify)
- [Wix](#setting-open-graph-tags-in-wix)
- [Squarespace](#setting-open-graph-tags-in-squarespace)

### Setting Open Graph tags in WordPress

Install [Yoast’s SEO plugin](https://wordpress.org/plugins/wordpress-seo/). Go to the editor for a post or page, then scroll down. You should see a Yoast SEO box. Hit the “Social” tab, then “Facebook.”

Fill this in to set the `og:title`, `og:description`, and `og:image` tags.

There’s no need to set `og:url` manually. Yoast does this for you. It also adds other useful OG tags like image dimensions.

Sidenote.

 If you don’t set up an OG image and the post has a featured image, Yoast will use that by default. It will also add other Open Graph and Twitter Card tags that would be just a waste of time setting up manually—site name, image dimensions, etc.

It’s also best practice to set a sitewide `og:image` tag. This is shown when no custom tag is set for a shared URL.

You’ll find the option to do this in Yoast’s settings.

*Yoast > Social > Facebook*

Make sure the toggle is set to “Enabled,” then upload an appropriate image. Brand images work best here.

### Setting Open Graph tags in Shopify

Most Shopify themes pull OG tags from variables such as your [title tag](https://ahrefs.com/blog/title-tag-seo/) for `og:title` and featured image for `og:image`.

The only tag you can customize through Shopify’s UI is a sitewide `og:image`.

Go to *Online Store > Themes > Customize > Theme settings > Customize > Social media > select an appropriate image*.

If you want to see how it’s set up, go to *Online Store > Themes > Actions > Edit code > Snippets > social-meta-tags.liquid* in the scrollbar. You can edit the code if you need to.

### Setting Open Graph tags in Wix

Wix pulls common OG tags from other variables, like the page’s meta title and description.

You can customize the OG title, description, and image for each page in the “Social share” settings.

You can also set a custom sitewide OG image. Go to *Settings > Social Share* on the main menu.

Overall, Wix makes adding OG tags easy, as there’s no need to hardcode anything.

### Setting Open Graph tags in Squarespace

Squarespace uses the page title and meta description for `og:title` and `og:description`.

You can set a custom `og:image` on a page by page basis.

Just go to *Page Settings > Social Image > Upload*.

If you need to add other OG tags and customize the default settings, go to *Page Settings > Advanced > Page Header Code Injection*. Read the following section on adding the tags manually and copy-paste the code there.

### Setting Open Graph tags manually

If you’re comfortable digging into website code, adding OG tags is as straightforward as pasting them into the `<head>` section of your web page.

Consider using a markup generator tool like [Mega Tags](https://megatags.co/) or [Web Code Tools](https://webcode.tools/open-graph-generator/article) to help reduce syntax errors.

## How to test and debug Open Graph tags

Now that you’ve deployed all the tags, you need to make sure they’re working as expected and are ready for sharing.

For that, use these tools:

- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/sharing/)
- [Twitter Card Validator](https://cards-dev.twitter.com/validator)
- [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/inspect/)

They all work the same. They pull tags from the page and show how it looks when shared.

Testing also helps prevent [issues](https://www.facebook.com/help/community/question/?id=169558846791129) where OG tags aren’t displayed or pulled correctly.

TIP

Use `og:image:width` and `og:image:height` tags to ensure a perfect snippet the first time someone shares it. In WordPress, Yoast adds them automatically. This is their syntax:

```
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
```

Here’s what the FB Sharing Debugger looks like in action:

The most important thing is how the snippet looks. If you miss or incorrectly set up less important tags, it’s not a big deal. You can ignore warnings about unimportant tags like `fb:app_id`

If something looks amiss and you update the tags, use the “Scrape Again” button to pull fresh data. If you don’t see the change after the crawl, use the [Batch Invalidator](https://developers.facebook.com/tools/debug/sharing/batch/) to clear the cache and repeat.

Repeat this process with the Twitter Card Validator and LinkedIn Post Inspector to ensure that your content looks as intended across all networks.

Sidenote.

 I’ve found that only Twitterbot follows [robots.txt](https://ahrefs.com/blog/robots-txt/) directives. Both Facebook and LinkedIn crawlers can scrape and show the content even if you disallow crawling. This was surprising, but even just for the sake of Twitter, make sure that all the URLs you share can be crawled.

## How to audit Open Graph tags

If you already have a site with hundreds of pages and aren’t sure which already have Open Graph tags, you can use a tool like [Ahrefs’ Site Audit](https://ahrefs.com/site-audit) to check your pages in bulk.

Just run a crawl, then go to the Social tags report to see all issues related to Open Graph and Twitter Card tags.

Click on a flagged warning to see the explanation and advice on how to fix it.

Click “View affected URLs,” and you’ll see the issue(s) affecting each URL along with relevant metrics. One of those metrics is organic traffic, which you can use to sort the table and prioritize URLs to fix.

Remember, pages that get lots of traffic are most likely to be shared.

## Final thoughts

OG tags are important for your social media presence, but there’s no need to spend a lot of time on them.

Focus on getting the basics down. Add tags, check social media previews, and debug.

Did we miss anything? Leave a comment or ping me on [Twitter](https://twitter.com/michalpecanek).
