---
title: "Alt Text for SEO: How to Optimize Your Images"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "alt-text"
url: "https://ahrefs.com/blog/alt-text/"
canonical: "https://ahrefs.com/blog/alt-text/"
author: "Joshua Hardwick"
published: "2020-03-27T00:32:45+00:00"
updated: "2025-06-23T16:07:16+00:00"
categories:
  - "On-Page SEO"
freshness_reasons: []
fetched_at: "2026-06-12T11:15:24+00:00"
status_code: 200
html_hash: "68c3936036ecbc60724e8aea30d1f794cb023d472bd79d07c89c2897b43eebe9"
clean_word_count: 1973
clean_char_count: 11768
---
# Alt Text for SEO: How to Optimize Your Images

Alt text (alternative text) describes an image on a web page. It lives in the HTML code and is not usually visible on the page itself.

But what’s so important about alt text? And how can you use it to improve SEO and user experience?

In this guide, you’ll learn:

- [Why alt text is important](#why-alt-text-is-important)
- [How to add alt text to images](#how-to-add-alt-text-to-images)
- [Why you shouldn’t add alt text to all images](#should-you-add-alt-text-to-all-images)
- [How to write good alt text](#how-to-write-good-alt-text)
- [Examples of good and bad alt text](#alt-text-examples)
- [How to find and fix issues with alt attributes](#how-to-fix-alt-text)

New to on-page SEO? Check out our

[Beginner’s guide to on-page SEO](https://ahrefs.com/blog/on-page-seo/)

## Why is alt text important?

Alt text matters for four main reasons.

1. Improves accessibility
2. Can improve ‘topical relevance’
3. Can help you rank in Google Images
4. Serves as anchor text for image links

### 1. Alt text improves accessibility

[Millions of people](https://www.cdc.gov/visionhealth/basics/ced/fastfacts.htm) are visually-impaired, and many use screen readers to consume online content. These work by converting on-screen content, including images, to audio.

Images without alt text cause problems for screen readers because there’s no way to communicate the content of the image to the user. Usually, they skip over these images, or worse, read out long and unhelpful image filenames.

[](http://creativecommons.org/licenses/by/4.0/)

Google talks about the importance of alt text for users with screen readers in their [SEO starter guide](https://support.google.com/webmasters/answer/7451184?hl=en).

### 2. Alt text can improve ‘topical relevance’

Google looks at the words on a page to understand what it’s about.

For example, if the page mentions poodles, labradors, and retrievers, then Google knows it’s about dog breeds.

[](http://creativecommons.org/licenses/by/4.0/)

How does this relate to images?

Because sometimes, context is ‘locked away’ in images that Google can’t read.

[](http://creativecommons.org/licenses/by/4.0/)

While Google can almost certain tell that these are images of dogs without alt text, the specific breed may be less obvious—and that’s where alt text comes in.

[](http://creativecommons.org/licenses/by/4.0/)

### 3. Alt text can help you rank in Google Images

Google Images is the world’s second-largest search engine. It’s responsible for [20.45% of all online searches](https://sparktoro.com/blog/less-than-half-of-google-searches-now-result-in-a-click/), putting it ahead of YouTube, Bing, and [other search engines](https://ahrefs.com/blog/alternative-search-engines/) combined.

This means there’s an opportunity to drive traffic from Google Images.

Just look at the number of clicks we’ve had to the Ahrefs Blog from Google Images in the past three months:

Sidenote.

This is only a small percentage of our traffic because we’re an SEO blog. People generally don’t search for the information we publish using Image search. It’s a completely different story for those in visual niches like fashion or food where people often find content using image search.

Google’s John Mueller says that alt text is an important part of optimizing for Google Images:

> Alt text is extremely helpful for Google Images -- if you want your images to rank there. Even if you use lazy-loading, you know which image will be loaded, so get that information in there as early as possible & test what it renders as.— John (@JohnMu) [September 4, 2018](https://twitter.com/JohnMu/status/1036901608880254976?ref_src=twsrc%5Etfw)

### 4. Alt text serves as anchor text for image links

[Anchor text](https://ahrefs.com/blog/anchor-text/) refers to the clickable words that link one webpage to another. Google uses it to understand more about the web page and what it’s about.

[](http://creativecommons.org/licenses/by/4.0/)

But not all links are text; some are images.

Google states:

> If you do decide to use an image as a link, filling out its **alt text helps Google understand more about the page you’re linking to**. Imagine that you’re writing anchor text for a text link.

[](http://creativecommons.org/licenses/by/4.0/)

## How to add alt text to images

Simply add an alt attribute to the `<img>` tag in the HTML code.

**Image with an alt tag:**

`<img src=“pie.jpg” alt=“steak and ale pie”>`

If you’re using a modern CMS, it should be possible to add alt text without having to dig into the HTML code.

For example, in WordPress, there’s a field for alt text when adding an image to a page or post:

Things are similar in other CMS’.

Here are instructions for some of the most popular ones:

- [Adding alt text to images in Squarespace](https://support.squarespace.com/hc/en-us/articles/206542357-Adding-alt-text-to-images)
- [Adding alt text to images in Shopify](https://help.shopify.com/en/manual/using-themes/change-the-layout/accessibility/adding-alt-text)

## Should you add alt text to all images?

No, this is a common misconception.

If the image exists for decorative purposes and doesn’t carry important information, then there’s no need to add alt text.

For example, some websites have icons to separate content:

These are only there to look pretty, so you shouldn’t add alt text. Doing so will only annoy visitors with screen readers, and won’t add any “SEO value” to the page.

The same goes for generic or stock images like this:

Having alt text that reads “bath and candle” isn’t useful for visually-impaired readers because it’s information they don’t need to know. It would be better to have the screen reader ignore it completely.

But, here’s an important point…

If an image doesn’t require alt text, best practice is to add an empty alt attribute. This is because some screen readers read out filenames in the absence of an alt attribute, whereas most will skip those with empty ones.

Here’s what that looks like:

`<img src="spacer.gif" alt="">`

Learn more in [this guide from WebAIM](https://webaim.org/techniques/alttext/).

## How to write good alt text

Alt text isn’t rocket science.

Follow these five best practices, and you should be good.

- **Be concise**. Lengthy alt text is annoying for those using screen readers. Use as few words as possible. (Use the [longdesc attribute](https://www.w3schools.com/TagS/att_img_longdesc.asp) if a long description is necessary.)
- **Be accurate.** Focus on describing the image.
- **Avoid keyword stuffing.** This is not a place to shoehorn keywords.
- **Avoid stating that it’s an image.** There’s no need to include “Image of…” or “Picture of…” in descriptions. Both Google and screen readers can work that out for themselves.
- **Avoid redundancy.** Don’t repeat information that already exists within the context of the image. For example, if you have a photo of Steve Jobs and the text directly below the image reads “Steve Jobs,” there’s no need to add this description to the alt tag. Google should understand that the caption is effectively the alt text.

You should also remember to add alt text to form buttons. Otherwise, screen readers might pass over them and some visitors won’t be able to interact with your website.

## Good and bad alt text examples

Let’s make sure we understand what works and what doesn’t with a few examples.

[](https://commons.wikimedia.org/wiki/File:Cheesecake_with_strawberry_and_whipped_cream.jpg "A R / CC BY-SA (https://creativecommons.org/licenses/by-sa/2.0)")

**Bad:** `<img src=“cheesecake.png” alt=“picture of cheesecake”>`
 **Okay**: `<img src=“cheesecake.png” alt=“cheesecake”>`
 **Good**: `<img src=“cheesecake.png” alt=“strawberry cheesecake”>`
 **Best**: `<img src=“cheesecake.png” alt=“strawberry cheesecake with cream”>`

[](https://commons.wikimedia.org/wiki/File:Steve_Jobs_Headshot_2010-CROP.jpg "Matthew Yohe / CC BY-SA (https://creativecommons.org/licenses/by-sa/3.0)")

**Bad**: `<img src=“steve-jobs.png” alt=“steve jobs apple iphone ipad mac”>`
 **Okay**: `<img src=“steve-jobs.png” alt=“steve jobs”>`
 **Good**: `<img src=“steve-jobs.png” alt=“apple founder, steve jobs”>`
 **Best**: `<img src=“steve-jobs.png” alt=“apple founder, steve jobs, holding the iphone 4”>`

[](https://commons.wikimedia.org/wiki/File:Orange_AD30HTC_and_PPC412.jpg "Zumwalder / Public domain")

**Bad**: `<img src=“amp.png” alt=“image4">`
 **Okay**: `<img src=“amp.png” alt=“orange amplifier”>`
 **Good**: `<img src=“amp.png” alt=“orange amplifier - 30 watts”>`
 **Best**: `<img src=“amp.png” alt=“orange AD30HTC - 30 watt amplifier”>`

Note the inclusion of the model number in that final example. This is good practice, especially for images on e-commerce product pages.

## How to find and fix issues with alt attributes

Lots of tools are capable of crawling your site and finding missing alt attributes, including [Ahrefs’ Site Audit](https://ahrefs.com/site-audit).

But having missing alt text isn’t always an issue because not all images require alt text.

For example, take a look at these missing alt attributes:

It’s clear from the filenames that they don’t need alt text. They’re decorative, which means we’d want a screen reader to pass right over them.

So, rather than crawling your site and obsessing over every missing alt attribute (most sites have quite a lot of missing ones), a better idea is to audit and improve alt tags for pages that already get traffic.

There are two reasons for this:

1. **They have visually-impaired readers.** [2.4% of US citizens](https://www.nfb.org/resources/blindness-statistics) have a vision disability. That’s one in roughly every 42 people meaning that on average, if your page gets 10,000 visitors a month, 240 of them can’t consume your content properly.
2. **They could possibly get more traffic.** Alt text can help images rank better in Google Images, and that leads to more traffic. Even just a 1% increase to a page with 10,000 monthly visits is an extra 100 visitors.

Here’s the process:

### Step #1. Find your most visited pages from organic search

Check [Ahrefs’ Web Analytics](https://ahrefs.com/web-analytics):

Or the “Top pages” report in [Ahrefs’ Site Explorer](https://ahrefs.com/site-explorer).

### Step #2. Audit your alt attributes

Install the free [Alt Text Tester Chrome extension](https://chrome.google.com/webstore/detail/alt-text-tester/koldhcllpbdfcdpfpbldbicbgddglodk?hl=en), load up the page with the most traffic, then activate the extension.

You should see the alt text displayed whenever you roll over an image.

If the alt attribute is missing, you’ll see a warning.

Check the alt text for a few images on the page. You’ll soon get a feel for whether they’re optimized well, poorly, or not at all.

For example, it only takes a few seconds of scrolling this post to see that all of the images are well-optimized…

… whereas the same isn’t true for this page on The Mirror:

### Step #3. Repeat for more pages

Repeat this process for the most visited pages on your website. This should give you a sense of whether your alt text optimization is sound or needs work.

Because most websites get the bulk of their traffic to just a handful of pages, this shouldn’t take too long.

For example, just ten posts on the Ahrefs blog account for 51% of monthly organic traffic…

… so we can easily audit and optimize alt text for most of our high-traffic pages in minutes.

## Final thoughts

Optimizing alt text is important, but it’s not the be-and-end-all of image SEO. You should also optimize filenames, serve responsive images, consider lazy loading, and much more.

Learn more in [our list of 12 actionable image SEO tips](https://ahrefs.com/blog/image-seo/).
