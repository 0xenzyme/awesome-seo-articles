---
title: "Rich Snippets: What Are They & How Do You Get Them?"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "rich-snippets"
url: "https://ahrefs.com/blog/rich-snippets/"
canonical: "https://ahrefs.com/blog/rich-snippets/"
author: "Chris Haines"
published: "2023-09-15T02:45:35+00:00"
updated: "2024-10-17T16:34:03+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T11:59:53+00:00"
status_code: 200
html_hash: "ad2de41a3517e593faa32a631f00a8b4ce73fc4f9678f38dd94b216929ba3625"
clean_word_count: 1721
clean_char_count: 10622
---
# Rich Snippets: What Are They & How Do You Get Them?

Rich snippets (also known as rich results) are search results pulled from code called [schema markup](https://ahrefs.com/blog/schema-markup/). They provide extra information beyond the standard “blue link,” which helps get more clicks to your content.

![Example of Google result with and without schema markup](https://ahrefs.com/blog/wp-content/uploads/2023/09/rich-snippets.png)

Rich snippets aren’t a [Google ranking factor](https://ahrefs.com/blog/google-ranking-factors/), but they can make your website’s search results stand out from the crowd.

So what exactly are rich snippets, how are they different from other SERP features, and how can you get them to show for your site?

## The difference between rich snippets, rich results, and SERP features

Rich snippets, rich results, and SERP features are sometimes used interchangeably by SEOs, which can cause confusion.

So what are the differences?

- **Rich snippets** – Google’s glossary states that [rich snippets are now known as rich results](https://support.google.com/webmasters/answer/7506798?ctx=glossary&sjid=15061488783067687978-EU).
- **Rich results** – [Google says](https://search.google.com/test/rich-results) rich results can include carousels, images, or other non-textual elements and that they are experiences that go beyond the standard blue link.
- **SERP features** – Provide additional and related information on the search query. Examples include the local pack, videos, and the knowledge panel.

## Types of rich snippets with examples

Google supports [different types of rich results](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) within its search results. Let’s take a look at some of the most popular types.

### [Review](https://developers.google.com/search/docs/data-types/review-snippet)

One of the most prominent examples of rich snippets is the `Review` snippet, which adds a yellow star rating to the search results with additional information about the reviews.

Here’s an example of what a Review snippet can look like, with the snippets highlighted.

![Review snippet example, via google.com

Review snippets can appear for the following content types:

- Book
- Course
- Event
- How-to
- Local business (for sites that capture reviews about other local businesses)
- Movie
- Product
- Recipe
- Software app

### [Product](https://developers.google.com/search/docs/data-types/product)

`Product` rich snippets are useful if you have an e-commerce website. They provide more information to your potential customers about your products—like whether the product is currently in stock, its shipping information, and its price.

Here’s an example of what a Product snippet result can look like in the search results, with the snippets highlighted.

![Product snippet example, via google.com

### Recipe

`Recipe` rich snippets give more information about the recipe on the page, such as how long it takes to prepare, its ingredients, and reviews.

Here’s an example of what a recipe result can look like in Google in the **Recipes** carousel.

![Recipes carousel example, via google.com

### [Event](https://developers.google.com/search/docs/appearance/structured-data/event)

`Event` snippets highlight the date and location of your events. They’re useful if you have ticketed events like concerts or shows.

Here’s an example of an Event snippet.

![Events snippet example, via google.com

Sidenote.

[FAQ](https://developers.google.com/search/docs/appearance/structured-data/faqpage) and [HowTo](https://developers.google.com/search/docs/appearance/structured-data/how-to) results are not included in this list, as Google announced it was reducing the visibility for them on [August 8, 2023](https://developers.google.com/search/blog/2023/08/howto-faq-changes), to provide a “cleaner and more consistent” [search experience](https://ahrefs.com/blog/search-experience-optimization/).

## How to get rich snippets for your pages

To be eligible for rich snippets, you’ll need to add [schema markup](https://ahrefs.com/blog/schema-markup/) to your pages and ensure you follow [Google’s structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies).

But before attempting to add the code, check whether your CMS has added it already.

To do this, head to a page where you think there should be markup, open up Ahrefs’ [SEO Toolbar](https://ahrefs.com/seo-toolbar), and go to the “Structured data” tab.

If there’s no structured data on the page, you’ll get a message that looks like the one below.

![Checking for structured data using Ahrefs' SEO Toolbar

You can double-check this by running a page through the [Rich Results Test tool](https://search.google.com/test/rich-results).

If no markup is present on the page, the rich results test will display the message “No items detected.”

!["No items detected" message, via Rich Results Test

Assuming there are no rich results detected, you’re safe to add the code.

Here’s how you do it.

### 1. Generate the code

If you use a popular content management system (CMS) like WordPress, adding schema to your website is as easy as installing a schema plugin like [this one](https://wordpress.org/plugins/schema-and-structured-data-for-wp/).

If you already use a plugin like Rank Math, you can use [its guide](https://rankmath.com/kb/woocommerce-product-schema/) to generate and customize your schema.

If you don’t use one of the more popular CMSes, you may have to generate the code yourself.

Tip

If you are not confident with code, it’s worth talking to a developer or [SEO consultant](https://ahrefs.com/blog/seo-consultant/) to help you implement these changes.

I’m using [Merkle’s Schema Markup Generator](https://technicalseo.com/tools/schema-markup-generator/) to generate Product schema markup. But you can use [Google’s Structured Data Markup Helper](https://www.google.com/webmasters/markup-helper/) or even [ChatGPT](https://twitter.com/lilyraynyc/status/1672206990678925312?s=20) as well.

![Schema markup generator, via merkle.com

To generate the code, simply fill out the prompts from the tool.

Once you’ve finished, copy the JSON-LD code; this is the code format [Google recommends](https://developers.google.com/search/docs/guides/intro-structured-data) for schema markup.

Sidenote.

Remember to only add code for content that’s visible to users and adheres to [Google’s guidelines](https://developers.google.com/search/docs/data-types/faqpage) for the selected schema type.

### 2. Check and validate the markup

Once you’ve generated the code, it’s just a matter of checking if it’s valid. If it’s not valid, your page won’t be eligible for rich results.

If you generated your code with a plugin or through your CMS, you can check it by:

- Opening the [SEO Toolbar](https://ahrefs.com/seo-toolbar) on the page you want to check.
- Going to the **Structured data** tab.
- Clicking on **Validate** and then the **Rich Results Test.**

![Accessing Rich Results Test, via Ahrefs' SEO Toolbar

Clicking this will take you to Google’s Rich Results Test. If it’s valid, you’ll see a green tick.

Once you’ve confirmed it’s present and valid, you can skip to step #3 below.

If you’ve manually added your schema code, you’ll need to make two checks:

- Check the code is valid before you implement it
- Check the code is valid after it’s added to your website

To see if your code snippet is valid, select “Code” on the [Rich Results Test](https://search.google.com/test/rich-results) and paste your code snippet in.

![Code selector, via Google's Rich Results Test

If it’s valid, you’ll see a green tick appear under the subheadings “Detected items.”

![Code test example, via Rich Results Test

Once you’ve validated your code, you can upload it to your website. Add it to the `<head>` or `<body>` of your website. [Google has confirmed either is fine](https://www.youtube.com/watch?v=lI6EtxjoyDU).

Once the code is added, you can run the page URL through the Rich Results Test to double-check it’s valid on-site.

This time, select “URL,” and enter a URL you want to test.

![URL selector, via Rich Results Test

If it’s valid, you’ll see a green tick.

![Valid items detection, via Rich Results Test

### 3. Monitor marked-up pages for performance and errors using Ahrefs

There are two reasons monitoring your marked-up pages is important:

- **Websites break easily** – Even if your code is valid on day #1, it can break later on. There may be code on other pages that isn’t valid as well.
- **Existing code may be invalid** – Old schema markup may be invalid and need fixing.

The best way to run a check is by using Ahrefs’ [Site Audit](https://ahrefs.com/site-audit)—you can access this for free using [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools).

Here’s how to check your website.

Once you’ve run your audit, head to the **All issues** report in Site Audit. If there are structured data issues, you’ll see a message like the one below.

![Structured data issues, via Ahrefs' Site Audit

Clicking on this issue will show all [structured data](https://ahrefs.com/blog/schema-markup/) issues on your website. There are 1,332 results in this example. I prioritize fixes for pages by sorting “Organic traffic” from high to low.

To do this, click on the “Organic traffic” header, then click “View issues” in the “Structured data issues” column to get more details about it.

![All filter results, via Ahrefs' Site Audit

Although you can check rich results status using Google Search Console (GSC), the advantage of using [Site Audit](https://ahrefs.com/site-audit) is that you can find and diagnose invalid schema code before it gets picked up by Google by scheduling regular crawls.

That way, when you go to GSC, you’ll see nothing but green “Valid items” that are eligible for Google’s rich results, as you’ve already fixed any invalid code.

!["Valid items" message, via Google Search Console

## Final thoughts

Rich snippets often get more clicks than traditional “blue link” results. But whether they’re worth implementing for your website depends on the type of content you have.

You don’t need to be a coding expert to get rich snippets for your website—but it takes some work to get started. Even once everything is set up, there’s [no guarantee](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) they’ll show. Tools like Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) are helpful here, as they can help you validate and monitor your code.
