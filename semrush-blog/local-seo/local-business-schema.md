---
title: "What Is Local Business Schema Markup? And How to Add It"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "local-business-schema"
url: "https://www.semrush.com/blog/local-business-schema/"
canonical: "https://www.semrush.com/blog/local-business-schema/"
author: "Alex Lindley, Christine Skopec"
published: "2023-06-15T14:59:00+00:00"
updated: "2025-07-29T09:21:00+00:00"
categories:
  - "Local SEO"
freshness_reasons: []
schema_genre: "Local SEO"
fetched_at: "2026-06-12T17:30:56+00:00"
status_code: 200
html_hash: "7b3c289cbc6f126bf62ba5b2d67c224bdd139a54739d883c1733081fba02892e"
clean_word_count: 2274
clean_char_count: 17508
---
# What Is Local Business Schema Markup? And How to Add It

## What Is Local Business Schema?

Local business schema is a type of code you add to your website to give search engines business details like your name, address, phone number, and operating hours.

While schema (also called structured data and schema markup) doesn’t create your [Google Business Profile](https://www.semrush.com/blog/google-my-business/) or directly control how your business appears on Maps, it reinforces that information.

![A Google Business Profile highlighted on the right-hand side of the SERP.](https://static.semrush.com/blog/uploads/media/df/b9/dfb9d472d0da71f952ca3699cf50e2c4/e81defeffffa2460a6385df1f2621e6e/AD_4nXc9QlpBBZdSQg-GJY9UgyMAJrIQwZqYNfmJON6ZfDki9yMfUc-p8rc5jqpWcTkq5eA8wg9iElEuLmhV5efn3Gxk00DM3n-VN8kKK5FEi2k2K9Q7_mCUo2kvg3qzISa3qIRixHKt.jpeg)

Local business schema differs from [organization schema](https://www.semrush.com/blog/schema-markup-for-company-corporations/) in that it's specifically meant for businesses with physical locations that want to optimize for [local search](https://www.semrush.com/blog/what-is-local-seo/).

## Why Should You Use Local Business Schema?

Local business schema makes it easier for search engines to understand and highlight your business.

Specifically, local business schema is useful for:

### Improving Local Search Visibility

Local business schema helps search engines understand your business so they can better match you to relevant queries.

For example, local business schema could help a business show for “bakery new orleans,” even if those words don’t explicitly appear anywhere in the actual listing.

![SERP with "“bakery new orleans" entered as the term and the local results which don't explicitly use the search terms highlighted.](https://static.semrush.com/blog/uploads/media/56/32/56325b7ee182458057e84c9d5d5eae27/70d6c3c06cae4c3290f04d82c9595774/AD_4nXdyN-Fmauv4QUVEnX0vSJyrs13pBaF7lnh787VVRg75nsYRhRucJgnaRtBH4jBQuNdOVBNrPzhfc5fgHdJs-emgQom5d5PHdQsnEIH94gxoOsSzYPRKYeI1RMBw0R57BA1S0NEndw.jpeg)

### Securing Rich Results

Using local business schema makes your site eligible for enhanced search result features called [rich results](https://www.semrush.com/blog/rich-snippets/).

These rich results can display details like:

- Star ratings from customer reviews
- Opening hours
- Business photos
- Price range

These extra details can make your [organic search result](https://www.semrush.com/blog/organic-seo/) more informative and visually appealing, which can improve [click-through rates](https://www.semrush.com/blog/click-through-rate/).

While schema doesn’t guarantee these features will appear, using structured data makes you eligible for them.

### Increasing Visibility in AI Tools

Structured data can help AI-powered platforms—like [ChatGPT](https://www.semrush.com/blog/chatgpt-search-insights/) and [Google’s AI Mode](https://www.semrush.com/blog/ai-mode-comparison-study/)—better interpret and summarize your website content.

In one [experiment by Aiso](https://www.getaiso.com/blog/schema_markup_experiment_blog_post), pages that used schema markup were more likely to appear in AI-generated summaries. This suggests structured data helps these systems extract key business information more effectively.

## Common Local Business Schema Properties

Before you add schema to your site, it’s helpful to understand which properties to include and what each conveys.

These are the most common properties in local business markup:

|  |  |
| --- | --- |
| **Property** | **What It Does** |
| *name* | Communicates your official business name |
| *address* | Provides your full physical address |
| *telephone* | Lists your main business phone number for contact |
| *openingHours* | Shows your general hours of operation (e.g., Mo-Fr 09:00-18:00) |
| *openingHoursSpecification* | Adds more detailed information about hours, such as if hours vary for different days of the week |
| *url* | Provides the link to your official business website |
| *image* | Specifies a photo of your storefront, logo, or another key image. Whether it’s displayed depends on how and where it's used. |
| *geo* | Supplies latitude and longitude to pinpoint your location |
| *sameAs* | Provides URLs to official or authoritative profiles (like your LinkedIn, Wikipedia, or social media pages) that confirm your business’s identity |
| *review* | Lets you manually include full details of an individual customer review. Like the author, date, rating, and review text. |
| *aggregateRating* | Indicates the average star rating and total number of reviews |
| *priceRange* | Indicates your typical pricing level (e.g., $$) |
| *paymentAccepted* | Lists payment types you accept |
| *currenciesAccepted* | Specifies which currencies you take (e.g., EUR) |
| *hasMap* | Links to your business location on a map |

## How to Generate Local Schema

In this section, I’ll show how to generate local business schema using two methods:

- Google’s Structured Data Markup Helper
- ChatGPT

I’ll use the same real-world example for both: [Little Collins](https://www.littlecollinsnyc.com/), a cafe in Midtown Manhattan.

### Using Google’s Structured Data Markup Helper to Generate Local Schema

Go to Google’s [Structured Data Markup Helper](https://www.google.com/webmasters/markup-helper/u/0/) and choose the circle next to “Local Businesses” from the category list.

Enter the URL of the page that contains your key business information (e.g., your homepage, about page, or contact page), then click “**Start Tagging.**”

![Structured Data Markup Helper start page with "Local Businesses" selected, a domain entered, and "Start Tagging" clicked.](https://static.semrush.com/blog/uploads/media/c1/dd/c1dd578cdf4e0c751e530e69bccdaebf/fb9a3052746dc39a3c391ed0862e26b2/AD_4nXcQ8cfo9bfl1jmuhH4KBmNES4c5daWA07qqQESTyEEGLHGcWFqLa7Kmc8a_5Z3GOLfGuquBOpEOTg6PVhoY2oRA9vcmvEj_dIxfGGJ8o9fupl9kB6XN2MqR1KoIQLoBIvQt8CL2Og.jpeg)

You’ll see your site on the left and a “Records” panel on the right.

![The "Records” panel appearing on the right-hand side of Structured Data Markup Helper highlighted.](https://static.semrush.com/blog/uploads/media/f9/4c/f94caec2ae3a245cc8f7818ee97eca83/4c6eb4168cedbb63aa8e3d892d4cea70/AD_4nXdzjtnDiq44tkXXZCWgho1lh3LXu4lv_xKcso-pQi4JAbRf2Q4HNkKPwEKWNLHIKyt81FwvUVrztBfU218XcioMMIyyqLyAGAdkuWng2UFSTt0YtY_43OFsXziWkOWzzEl9Fia4KQ.jpeg)

To tag information:

- Highlight a piece of text (like your address or business name)
- Choose the appropriate tag from the drop-down menu that appears

In the example below, I tagged “708 3rd Ave” as the “Street address.”

Theright-hand “Records” panel updates automatically with each tag.

![Tagging information by highlighting a piece of text and choosing an appropriate tag from the drop-down menu on Structured Data Markup Helper.](https://static.semrush.com/blog/uploads/media/74/3f/743fa7d82054fb1de85a9ad8385b6e69/4ce643b0a561ce841e1815244db3478d/AD_4nXfYlUrr2pRpnlfiBIXgVi9uOMvF4g8AHzPpKNq6-VCzXpL2z3yp6-t85LTVcyhZJDXvdZpRcB7JEbz5V-fGDKyvS2WHmZLioCsZLIIf3k7HFlhTiXJZtqeZD0rHSGHnlcaK-ZnsLQ.jpeg)

Once you’ve finished tagging, click “**Create HTML**.”

!["Create HTML", after tagging information, clicked on the right-hand side of the Structured Data Markup Helper.](https://static.semrush.com/blog/uploads/media/01/74/0174cf72266d16eb6e759e22f75adb1b/bc553221052e7751c953cd25f97a28c2/AD_4nXcmzp6fQ-lhT7RISXatpKM4DnRd2H9Pryk1lIhRta-3yiFLb6ip_Gwyo2idvML3dXeMjoh6JIO1snfjuoe_L0PNpzYnQWtkB63vvyiq8poMcm1wX3mOtLxAnOUlLd0i848pWOMcNw.jpeg)

The tool will then generate JSON-LD code that you can copy and paste.

![JSON-LD Markup code generated on Structured Data Markup Helper.](https://static.semrush.com/blog/uploads/media/11/6e/116ec7e5ad8f269de0df1a27796dc906/3053a868b2ddfbc964642fa1289e8b56/AD_4nXf7PaOX-wWaIoHDXinqIa0FNUkbaDlh1b1HZbgdnC8MmXh1dSVQS-eMDKyrNh7IFR8nljAvxMQDHwKFoO4yx7Mkb_zgaFl8cfdS_OK0suRGTsatIgsTq9Lu7O92lsiI58THB9UN7g.jpeg)

The tool can only tag what’s visible on a single webpage. And many businesses have info (like social links, hours, or reviews) spread across multiple pages or formatted in a way that’s tricky to tag.

That’s why I usually prefer generating schema with a tool like ChatGPT.

### Using ChatGPT to Generate Local Schema

Start by writing out your key business details, including your website, contact info, hours, and even a sample customer review.

Here’s an example prompt I entered using the same cafe:

*“Create local business schema in JSON-LD format for Little Collins, a café located at 708 3rd Ave, New York, NY 10017. The phone number is (212) 308-1969. The email is info@littlecollinsnyc.com. The website is www.littlecollinsnyc.com. Opening hours are: Monday 7am–6pm, Tuesday–Friday 7am–8pm, and weekends 7:30am–6pm. Also include a customer review: “Best coffee in Midtown! Friendly staff and great vibe.” – Sarah M.”*

ChatGPT then returns your schema in JSON-LD format, so it’s ready to copy:

![Local business schema generated in JSON-LD format using ChatGPT.](https://static.semrush.com/blog/uploads/media/24/dd/24dd3912344ab04c759cdac3f553b354/f9dc3404885646c17eb5636fe1c961a5/AD_4nXdnTx2R9CcuPySEkE1jX939D8GDIuhzriLss0LmQU5UaukMDgPFv0ZVI81LUuyNBwh5cZ1ZyZjvVnhfCyPy-bYJSR0Ruimba-sLXjc4CHe_rD1Lw2pbEEW_KsSXB2J8bKL3UzvQ9Q.jpeg)

One thing I like about using ChatGPT is that it often includes helpful suggestions.

Like this recommendation to add an "image" field with a proper logo or storefront photo. And the suggestion to wrap reviews in a "reviewRating" block to follow best practices from Schema.org.

![The "Notes" section showing helpful suggestions to improve the local schema markup on ChatGPT.](https://static.semrush.com/blog/uploads/media/32/8e/328e6615025ae9e3f01ea0ecca2d44de/b02443e1b97b2fc037f518bc156b70ff/AD_4nXfyQCRjTHnByffUgmzhJ8eBoYd2oc9L41HDQ8R9Czfhkr488FBC2D9Pbpxs_hm5X7en8Co6BuhhIL8DNtpi0MVmCdgWI6_q5nyvxR5Gtgvhg-PT1aGnyVc74WJ4iUHHpTsSsF5W.jpeg)

I also like how, once you’ve generated your schema, it’s easy to tweak or expand.

With Google’s Structured Data Tool, making changes usually means starting over and re-tagging the entire page.

With ChatGPT, you can just enter a follow-up like:

*“Now add my social profile URLs:*[*https://www.instagram.com/littlecollinsnyc/*](https://www.instagram.com/littlecollinsnyc/) *and*[*https://www.facebook.com/littlecollinsnyc/.”*](https://www.facebook.com/littlecollinsnyc/.%E2%80%9D)

ChatGPT will instantly return an updated version of the schema with those fields included. No rework required.

![Updating local business schema with social profile URLs on ChatGPT.](https://static.semrush.com/blog/uploads/media/79/90/799055ec1e8b33cfc15fc7343604699f/23189637ae5880422e31b1aca76a4648/AD_4nXfqvNKPSSw4H2-yQEuwvDJjT1iMVOSxkZBqAhlTnBIb9v2CjBmH41IafPLcThqqT_NM3J3slo-V8coD4YnIifrGQNvZIQ5sCpwlIfTYGaxIlqkq70lk7bc9PszCz4xKVXhgOfj6vg.jpeg)

## How to Add Local Business Schema to Your Website

There are two main ways to add local business schema to your site:

### Use a Plugin to Add Schema in WordPress

If you’re using [WordPress](https://www.semrush.com/blog/wordpress-seo/) and prefer a code-free setup, [SEO plugins](https://www.semrush.com/blog/wordpress-seo-plugins/) make it easy to implement local business schema.

Popular options include:

- [Schema Pro](https://wpschema.com/)
- [Rank Math](https://rankmath.com/)
- [Yoast Local SEO](https://yoast.com/wordpress/plugins/local-seo/)

For example, Yoast Local SEO lets you add key business details without ever touching your site’s code.

![Yoast Local SEO with input fields to add key business details to implement local business schema.](https://static.semrush.com/blog/uploads/media/4e/54/4e54974b27e277bb0170bd6a2ac01137/35359847953c6e712d74fa759a137339/AD_4nXdCFYsZ6vTn1eMiQrJkn9k7ceLMiGnGQwoZLlH2NnRvh8Vpgp4vG4KRRpcaAPkb7WdbiS_TwF_63lzHsYHOmfHgSs3Tzeg0dYMO8yNmW7tmzZgLodqpygIo3F0JRCFzj6e4qkNlEQ.jpeg)

Just be aware that you need [Yoast SEO Premium](https://yoast.com/wordpress/plugins/seo/) and the [Yoast Local SEO](https://yoast.com/wordpress/plugins/local-seo/) add-on to access local SEO features in Yoast.

Plugins are convenient. But they may limit how much you can customize.

### Add Local Business Schema Manually

Adding the schema manually is often the better choice if you want full control.

Back up your website before editing. If you’re not comfortable working with code, it’s safest to ask a developer for help.

Then:

1. Generate your schema using either Google’s Structured Data Markup Helper or ChatGPT
2. Copy the code
3. Paste it into the <head> section of the page where your business info lives—typically your homepage, about page, or contact page

Here’s what that looks like:

![Adding local business schema manually by pasting the code into the <head> section of a local website.](https://static.semrush.com/blog/uploads/media/44/fe/44fec9f6890883543e5604b698100ce0/1858a30d12272e026fc737ecd4b0a7f0/AD_4nXfTk4AwVXufmFHXV6-aosSfScNlUyWe5nLiGc9U-KOa8oUI0eiCtuCOJsyqI_X7ARQriphioV9hY7-e5--MQXOmYrq4L1HPjDm70-b8HaCHEpXJxtP5nsf8S59aylTWfFi760X-ng.jpeg)

## How to Add Local Business Schema for Multiple Locations

If your business has multiple physical locations, the best practice is to create a dedicated page for each one. And add separate local business schema to each of those pages.

Each location page should include:

- The branch’s specific address
- Phone number
- Opening hours
- Geographic coordinates (if available)
- Any other location-specific info (like reviews or social links)

Once your location pages are live, generate unique schema for each one using Google’s Structured Data Markup Helper or ChatGPT.

## How to Validate Your Local Business Schema

Check that the local business schema added to your site is valid to make sure search engines can understand it.

### Use Schema.org’s Validator

Use Schema.org’s official validator to check your markup by entering the live page URL.

Go to the [Schema Markup Validator](https://validator.schema.org/).

Select the “**Fetch URL**” tab, enter your page’s URL, and click “**Run test**.”

![The "Fetch URL" tab of the Schema Markup Validator with a URL entered and "Run test" clicked.](https://static.semrush.com/blog/uploads/media/eb/51/eb5113f76b56cdb8e13417483f39d2d4/f8e1c57f55ebf2d6a057bcc5e3c072fa/AD_4nXcyiMEiEaKEFtoEp7RtTSmClN3EDuCM2sUH0wJCLsf-Gz54cBJXKY1FwMAOnQg4aWo0kK_0d5CVyjy4A-ChjP9w1TkVKGm9brGr43EOVePQuVYx5PhoF4MSWX8n0P9VnOE9V4FIOw.jpeg)

Ideally, you’re looking for a “0 Errors” and “0 Warnings” result:

![Schema Markup Validator showing a page with no errors or warnings.](https://static.semrush.com/blog/uploads/media/30/ff/30ffc0d3b0d31dc64e98e00c81e10770/044925502e8263e398bcf09fddce2257/AD_4nXfuEU7OPv8DkGIdpQEPYKZVj9Ubnb0n7B_-kv_LM7JJOvAumnTn549nMFxAX2Ch88ElaskL85JAYWIwEgYyXduG505G4yzNPNzKQP_dCZ5B9YL9BAOfhTYFOKxVitk5lwk5D1XS8A.jpeg)

If there are any issues, the tool will highlight them. So you can identify and fix problems quickly.

### Use Site Audit

Our free [website audit](https://www.semrush.com/siteaudit/) flags structured data errors quickly. To validate structured data across your full site and dig into your overall technical health, use Semrush Site Audit.

Start by [configuring a new site audit](https://www.semrush.com/kb/539-configuring-site-audit).

Once the audit is complete, go to the “**Overview**” tab. Scroll to the “Markup” section and click “**View details**.”

![Site Audit report with "View details" under "Markup" clicked.](https://static.semrush.com/blog/uploads/media/ed/41/ed41feaeb8a6c4fee3bdf4258907fbfb/7e7dca7a01471a0ae3941f2b54db9538/AD_4nXdjb98vHOcTDmBMtoou85LjWm102d8jyTNIwg7LxZAoMfCuCR2d6_v9OTTFr1pj2nqlPMAA0NeXePqVF-W_s6IwW5udfgM32QKe4-Jnbj55sfzS9ixfTeFpdvl7B_mhJFKF8Hr8.jpeg)

Here you’ll see:

- How many pages have markup
- The types of markup found (JSON-LD, Microdata, etc.)
- Pages with invalid or missing structured data

![Markup report on Site Audit showing different data like pages with markup, pages by markup type, and structured data by pages.](https://static.semrush.com/blog/uploads/media/eb/aa/ebaa2e0b01214a734eae068d7ea17e8a/c28cd1c06bf3cd99180c64a03379cd8c/AD_4nXfSfZTHsydKlqJLFvRGGmrAsdia4sx-PUT5kK7X3l2XVH_pIxkwZoMlb_325eEeHlfgOuFS32Tu2eslMGRAJr-BHKngSJW48rXKZ7PGOei4GRsWZpYofBPL6aXIYv37hZT-_6aLzg.jpeg)

Scroll to the “Structured Data Items” table and look for “Local Business” in the “Item” column.

If there are any invalid lines related to your local business schema, they’ll appear here. And you can click the number that appears in the “Invalid” column to see the affected pages and which fields need to be fixed.

In this case, there aren’t any issues.

!["Local Business" highlighted in the Structured Data Items report on Site Audit.](https://static.semrush.com/blog/uploads/media/28/c9/28c92f6d26f5bd2b63c151f8989e60f7/6b40551aac1738ee295c20471d3594a9/AD_4nXfcf8OEg3fubzax_-A5BvbWuFr47cozPWKFPD0UhphFEsQSctjlFpZtP-oHwZjqoSTzA1kiarrF4JLT5vaUj9aDyZceEE7WUtfn37EqLR1oNcpEQcTV9B0Ad2I5c043uIzOskcpKw.jpeg)

Fix any errors on your site if needed, then run the audit again to confirm they’ve been resolved.

## Improve Your Local Business’s Online Visibility

Adding local business schema is a solid step you can take toward increasing your visibility in local search and AI-driven platforms.

But schema is just one piece of the puzzle:

The Semrush [Local Toolkit](https://www.semrush.com/local-business/) includes everything you need to grow your digital footprint, attract more local customers, and track performance.
