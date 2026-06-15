---
title: "What Is Schema Markup? & How to Add It to Your Site"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "schema-markup"
url: "https://www.semrush.com/blog/schema-markup/"
canonical: "https://www.semrush.com/blog/schema-markup/"
author: "Zach Paruch, Carlos Silva, Christine Skopec"
published: "2023-12-19T09:04:00+00:00"
updated: "2026-02-02T14:54:00+00:00"
categories:
  - "General SEO"
freshness_reasons: []
schema_genre: "General SEO"
fetched_at: "2026-06-12T19:00:21+00:00"
status_code: 200
html_hash: "bdb0e68c25cb11603057c2d9f203c17f50e4a9bf9b2ab93a65cca4b691fa5084"
clean_word_count: 3384
clean_char_count: 23175
---
# What Is Schema Markup? & How to Add It to Your Site

Google, Bing, and AI platforms like ChatGPT all need to understand your content before they can surface it to users. They've gotten better at this over time but can still benefit from explicit signals that remove any ambiguity.

Schema markup is one way to explicitly label your content to tell search systems exactly what they're looking at. Whether that's a product, a review, an event, or a local business.

This guide walks through what schema markup is, the most useful types, and how to implement it step by step.

## What Is Schema Markup in SEO?

Schema markup (a type of structured data) is code you add to your website to help search engines, and potentially AI systems, understand your content better.

Schema markup looks like this:

![The schema markup code for a blog post by Semrush.](https://static.semrush.com/blog/uploads/media/42/88/428834d33c2ce83559c3a3423037f41e/6853c4170847a801eceb4f6c1c864cdc/image.jpeg)

[Schema.org](https://schema.org) serves as the reference website that publishes documentation and guidelines for implementing schema markup.

Adding schema markup to your pages also makes your content eligible to have search engines like Google show enhanced search results known as [rich snippets](https://www.semrush.com/blog/rich-snippets/) (also called rich results). Like star ratings, prices, and whether a product is in stock.

When rich snippets appear, users can find valuable information directly within search results.

For example, Dell’s product page for computers, monitors, and other tech solutions uses schema markup. And Google displays information like price range, product availability, delivery fee, and more in the page’s search result.

![Dell search result with price, product availability, delivery status, return information, and sitelinks](https://static.semrush.com/blog/uploads/media/31/2d/312debc5dd28ce1a615f244c2442571b/c4c90febd8d0e8fdd7f4526ed277c98f/image.png)

Just know that adding schema markup doesn’t guarantee rich results. Ultimately, [it’s up to Google to decide](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) whether to show rich formats.

## How Does Schema Markup Work?

Schema markup works when crawlers scan your website’s HTML and see tags from Schema.org’s standardized vocabulary clearly labeling your content in a way that search systems can understand.

For example, schema markup explicitly tells search engines that "$299 is the price of this specific product." So, they don’t have to infer what $299 means.

The explicit communication from schema markup helps search engines categorize your content more accurately and determine when to display it as a rich result.

## Why Is Schema Markup Important for SEO?

Schema markup is important for search engine optimization ([SEO](https://www.semrush.com/blog/what-is-seo/)) because it helps search engines understand your content better, which increases the odds that your content will show for more relevant keywords.

But know that schema markup isn’t a direct ranking factor.

Structured data also makes your content eligible to display as richer, more engaging search results that offer these benefits:

- **Enhanced click-through rates (CTRs)**: Rich results may see higher CTRs compared to standard blue links given users can preview key information directly in search results
- **Improved SERP real estate**: Rich snippets take up more visual space on search engine results pages ([SERPs](https://www.semrush.com/blog/serp/)), pushing competitors further down the page
- **Better user experience**: Rich results display relevant details upfront, which helps users more readily see if you meet their [search intent](https://www.semrush.com/blog/search-intent/) in a way that makes them want to visit your content

Without schema markup, your page will probably only show as a blue link with a description below it. And if your competitors are using schema markup and getting rich snippets, then your link won’t stand out.

For example, compare these two pages ranking for “small microwave under $200” that appear right next to each other in the search results:

![Google SERP for the term “small microwave under $200” showing a simple blue link result and a rich result with a rating, price, and delivery options.](https://static.semrush.com/blog/uploads/media/8d/b7/8db79e1c5b77e18edb000448599629db/079dca7fabee7ac2a1e73ac8532b3075/image.jpeg)

The Home Depot result is minimal. But the Target result stands out by showing a star rating, explicitly saying there are options between $18 and $200 (which reflects the search intent), and including mention of free delivery and returns.

## Is Schema Markup Important for AI Visibility?

Schema markup may be important for AI visibility, but there’s limited evidence showing it definitively improves your likelihood of showing up in AI responses.

In its [guide to succeeding in AI search](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search), Google says:

> *“Make sure structured data matches the visible content.”*

But this guidance only briefly mentions schema markup as being useful for sharing information in a machine-readable way that Google’s systems consider. And because the page says the guidance is for “success in Google Search all around,” there’s no direct statement that using structured data helps specifically with AI visibility.

[Microsoft has a similar page](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers) about optimizing content for inclusion in Bing’s AI answers. Here, the advice is more explicit:

> *“Schema is a type of code that helps search engines and AI systems understand your content.”*

We can’t definitively say schema markup helps with AI visibility—there’s no similar guidance from the companies behind popular AI tools. It’s unclear if AI systems like ChatGPT or Claude use schema markup in the same ways that search engines do.

However, there’s evidence that AI tools like [ChatGPT use Google](https://www.semrush.com/blog/chatgpt-definitely-uses-google/). If structured data helps Google match your pages to relevant queries, it would also help AI tools match your pages to relevant queries if those AI tools are using Google.

Regardless of the direct or indirect effects, adding schema markup is an [SEO best practice](https://www.semrush.com/blog/seo-best-practices/). So, it’s beneficial to add proper schema markup to your content where relevant anyway.

## Common Types of Schema Markup

Google supports [dozens of schema markup types](https://developers.google.com/search/docs/appearance/structured-data/search-gallery), but you don’t need to use them all.

In this section, we’ll explore some of the most commonly used types of schema.

### Organization Markup

[Organization schema markup](https://developers.google.com/search/docs/appearance/structured-data/organization) tells search engines more about your business, such as its name, logo, address, and contact details.

[Organization schema](https://www.semrush.com/blog/schema-markup-for-company-corporations/) helps your organization’s details appear in a knowledge panel in Google search results (if your business has a knowledge panel).Like so:

![Knowledge Panel appears when searching for a company name.](https://static.semrush.com/blog/uploads/media/ba/93/ba936952bdcd3fba4bf10e5f123f454c/d3e362cd63dd76fdd77e3b668a9951ea/image.png)

### Product Snippet Markup

[Product snippet markup](https://developers.google.com/search/docs/appearance/structured-data/product-snippet) is one of [two types of product schema markup](https://developers.google.com/search/docs/appearance/structured-data/product) and is used to provide search engines with extra product details for pages where users **cannot make a purchase**—like product review pages.

This type of markup allows search engines to display information in search results, such as:

- **Ratings and reviews**: Aggregated customer reviews and opinions
- **Pros and cons**: Key advantages and disadvantages of the product (only available for [editorial product review pages](https://developers.google.com/search/docs/appearance/structured-data/product-snippet))
- **Price and availability**: Basic pricing information without direct purchase options

Product snippet markup is particularly valuable for editorial websites, affiliate marketers, and ecommerce platforms showcasing products but not selling them directly.

If a tech review site publishes an in-depth review and adds product snippet schema markup to the page,Google can choose to display star ratings, review summaries, and pros and cons directly in the search results.

![A product snippet markup for the term "macbook pro" with the star rating along with pros and cons highlighted.](https://static.semrush.com/blog/uploads/media/93/11/93115bd34f9d9aa81cf0595cf1e7e0f5/949037b1d1a215e3370d69efef5c5428/image.jpeg)

### Merchant Listing Markup

[Merchant listing markup](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) is the second type of product markup specifically for product pages, but it’s for pages where users **can make a purchase***.*

Merchant listing markup can display key purchase-related details, such as:

- **Pricing and discounts**: Regular prices, sale prices, and promotions
- **Stock availability**: Indicates if the item is in stock, on back order, or out of stock
- **Shipping and returns**: Delivery estimates, shipping fees, and return policies

Ecommerce websites and online retailers that want to give potential buyers purchase-related information directly in search results are great candidates for merchant listing markup.

![Products with more information listed in Google search results](https://static.semrush.com/blog/uploads/media/12/2d/122d6a17f46e5fbe0fae431b34520e63/c1167c92b723480b323bbb425d47c0a8/image.png)

### Review Schema Markup

[Review schema markup](https://www.semrush.com/blog/review-schema/) can display star ratings, review summaries, and other review-related details in search results.

Google supports review snippets for [various structured data types](https://developers.google.com/search/docs/appearance/structured-data/review-snippet), including:

- Product
- Local business
- Movie
- Book
- Software app
- Recipe

Review markup typically appears in one of two formats: a single rating and an aggregate rating.

A single rating shows just one reviewer’s rating along with their name:

![Google SERP for the term "F1 movie review" showing a result with a single rating along with a reviewer's name and a rating.](https://static.semrush.com/blog/uploads/media/48/a4/48a4651db50d61bcd54d9e2acb62fc14/ed1bfc406e3c2ff0f56fe18dd1bfe8f7/image.jpeg)

An aggregate rating shows an average score based on multiple user reviews and the total number is indicated in parentheses:

![Aggregate review in Google Search results.](https://static.semrush.com/blog/uploads/media/44/b5/44b50bc044f8f439f16a18c763d6a4b2/64f4b9b01ad13d4c27a15a8b16f169d9/image.png)

### Article Markup

[Article markup](https://developers.google.com/search/docs/appearance/structured-data/article) helps search engines understand news articles, [blog posts](https://www.semrush.com/blog/seo-blog-post/), and sports articles and makes your pages eligible for a rich snippet in Google Search and [Google News](https://www.semrush.com/blog/google-news-seo/).

When you use article markup, it can influence how article headlines, author names, and publication dates appear in search results. Like this:

![Articles about the Oscars in Google Search Results in the "Top Stories" SERP feature](https://static.semrush.com/blog/uploads/media/4c/14/4c1477af35cfdd44a6fe137f05c30c9d/1a163aa6f7033a6737be89d327090647/image.png)

### Local Business Markup

[Local business markup](https://developers.google.com/search/docs/appearance/structured-data/local-business) gives search engines key information about a physical business, including its address, phone number, and operating hours.

Brick-and-mortar shops, restaurants, service providers, or other businesses aiming to attract local customers can all benefit from local business markup. It can help Google understand what to show in your business profile that appears in relevant local Search and Maps results.

![A Google Business Profile for Bestia](https://static.semrush.com/blog/uploads/media/ff/38/ff38269b5a23554254c52ec2adcab10d/95b73146dd2fcdf2110956ecd8600d89/image.png)

***Further reading****:* [*Local SEO: What Is It & How to Do It*](https://www.semrush.com/blog/what-is-local-seo/)

## How to Add Schema Markup to Your Website

You can manually insert schema into your HTML or rely on plugins if your site runs on a [content management system](https://www.semrush.com/blog/best-cms-for-seo/) (CMS) like [WordPress](https://www.semrush.com/blog/wordpress-seo/).

Here’s how to generate and add schema markup to your site:

### 1. Select Your Schema from Google’s Structured Data Markup Helper

Go to Google’s [Structured Data Markup Helper](https://www.google.com/webmasters/markup-helper/u/0/), choose a schema type, enter your URL, and click “**Start Tagging**.”

![Structured Data Markup Helper with "Articles" selected, the URL field highlighted, and "Start Tagging" clicked.](https://static.semrush.com/blog/uploads/media/68/0d/680d2016ee44812927d301d2c86203a3/c5fa43eb858a0b3ff38cd6df0bdecc20/image.jpeg)

Your webpage will appear on the left. Data items for markup will appear on the right.

![Structured Data Markup Helper showing a webpage on the left and data items for markup on the right.](https://static.semrush.com/blog/uploads/media/7c/83/7c8351395e8dfd3ea2f16a90b660743a/f5133fcc64083624d34be461039df0aa/image.jpeg)

### 2. Mark Up Your Page

Using the tool, highlight the section on your page that you’d like to mark up.

For example, for an article, highlight the title and choose the “**Title**” data item from the menu that pops up.

![The title of a page highlighted and the “Title” data item clicked from the menu that pops up on Structured Data Markup Helper.](https://static.semrush.com/blog/uploads/media/78/f3/78f3018653e1a031c31d3529ec3e1935/ae0963f1f12a3e57d8ff2526a605d629/image.jpeg)

The tool will then take the article’s title and place it next to “Title” on the right-hand side.

![The marked-up "Title" highlighted on the right-hand side of the Structured Data Markup Helper.](https://static.semrush.com/blog/uploads/media/d6/6a/d66a89f5f927c3552b007d4a0d736309/475cbccf04e8239cb0a200676606ca3b/image.jpeg)

Continue adding as many relevant markup properties as you can.

### 3. Generate the HTML

When you’re done marking up your page, click on the “**Create HTML**” button at the top right of the screen.

![The "Create HTML" button clicked on the top right of the Structured Data Markup Helper.](https://static.semrush.com/blog/uploads/media/16/a4/16a492b97a1682ad4b5f01d684cc226f/b13da5e39dda7218e29a868bd93605ed/image.jpeg)

You'll receive JSON-LD markup by default ([Google’s recommended format](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data#:~:text=In%20general%2C%20Google%20recommends%20using,less%20prone%20to%20user%20errors).)), but you can switch to Microdata using the drop-down menu.

![The dropdown to choose between JSON-LD or Microdata on the Structured Data Markup Helper.](https://static.semrush.com/blog/uploads/media/e6/6c/e66cfc903d5fd6753926de8045a56453/9cf7f455a6dec19b28bdc9f44a8b8b58/image.jpeg)

### 4. Add the Schema Markup to Your Website

Now that you have your code, add the schema markup to your webpage’s HTML <head> section.

You can easily copy the markup from the tool.

![Markup code selected and copied on the Structured Data Markup Helper.](https://static.semrush.com/blog/uploads/media/38/43/3843b0f2478423afe1019c0917d54921/19cfb023d5e25f98c945478b89a387fe/image.jpeg)

If you’re using a CMS like WordPress, you can use a plugin like SchemaPro, Rank Math, or Yoast to add schema markup without editing HTML.

For example, [Yoast SEO](https://www.semrush.com/blog/yoast-seo/) generates organization schema using your business name, logo, and other details in the plugin’s settings. And it inserts the schema into your website’s code.

![Organization schema helper in Yoast](https://static.semrush.com/blog/uploads/media/80/a9/80a95025eb64663ca59dc98f06571c8f/956a1a59c18b90f865dd0523e3f312d8/image.png)

### 5. Validate the Markup

Validate the schema markup using Google’s [Rich Results Test](https://search.google.com/test/rich-results).

Enter your URL or paste the generated schema markup into the tool, and it’ll confirm if your markup is valid.

![Rich results test start page](https://static.semrush.com/blog/uploads/media/74/7f/747fd557933417312c2265d013153014/c51663dc00e2fc2f46a991a3a2f5a030/image.png)

Errors, warnings, and detected schema markup will show up on the right side of the screen:

![Detected schema markup along with schema issues highlighted on the right-hand side of Google’s Rich Results Test.](https://static.semrush.com/blog/uploads/media/54/5f/545f0b05476737b5aee5ca4cfb1d8114/b767019e68869e562b426f5f3088a517/image.jpeg)

If you need to fix any errors, edit your code directly on the left side of the page.

After you make changes, click the “**Run Test**” button at the bottom of the page:

![The "Code input" section on Google’s Rich Results Test with the “Run Test” button at the bottom of the page highlighted.](https://static.semrush.com/blog/uploads/media/73/a9/73a9a58e6a9ffbadcd98d5317f66832f/e1bcc2e731c79c3705d83da813879327/image.jpeg)

## How to Generate Schema Markup with AI Tools

Generating structured data with AI tools like ChatGPT, Google Gemini, and Claude is as easy as entering a prompt, but it’s not foolproof and still needs to be implemented on your site.

For example, I asked ChatGPT to generate JSON-LD schema for our post about the [Google 3 Pack](https://www.semrush.com/blog/google-3-pack/).

![A prompt to generate a JSON-LD schema markup for a page along with the result generated on ChatGPT.](https://static.semrush.com/blog/uploads/media/6c/22/6c22f35afa23e0e6b7380b10e16a366b/82399f42964db8331b415d424d155f31/image.jpeg)

I then used the Rich Results Test to validate the schema. The tool detected both the article and breadcrumb structured data. But it detected non-critical issues with the article schema.

![Rich Results Test for a page detecting non-critical issues with article schema.](https://static.semrush.com/blog/uploads/media/37/63/3763761b824d7d903fd253c542ed7866/faf95d218be6ef3ce34be8eac193b41a/image.jpeg)

The ChatGPT-generated schema has an invalid datetime value and is missing time zone information in the datePublished property.

![Rich Results Test showing that a ChatGPT-generated schema with missing time & timezone information from the datePublished property.](https://static.semrush.com/blog/uploads/media/2b/46/2b46ea36863d35de58551108ec738dc4/13b5fd55bdd20b10e58aff7587f9b132/image.jpeg)

This is information ChatGPT was unable to find just by crawling the page.

The ChatGPT output also lacks a dateModified property, which tells search engines when the page was last updated. This is not an issue necessarily, but it’s information that our current schema markup **does** include:

![The "dateModified" property highlighted on the source code of a page.](https://static.semrush.com/blog/uploads/media/e5/38/e538680a4c13e1d48928650f1d57d0b8/29d9508a7b8d9f774405d9fe7b490f4b/image.jpeg)

To be fair, Google’s Structured Data Markup Helper also doesn’t include most optional properties.

The takeaway? You should validate any schema markup before implementing it.

## Schema Markup Best Practices

Follow these best practices to ensure your schema markup is effective and compliant with [Google’s structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies):

- **Focus on pages that benefit from rich results**: Add schema to pages like product listings, reviews, articles, and local business pages, as these are more likely to show enhanced search results
- **Only use relevant schema**: Make sure the schema type accurately matches your page
- **Keep the markup up to date**: Regularly check and update your schema—especially for details that change over time, such as product prices or business hours
- **Add as much relevant information as possible**: If your schema type supports multiple details, fill out as many as you can. For example, local business schema can include opening hours, accepted payment methods, and location details.
- **Ensure schema matches other online listings**: Make sure your schema details are consistent with similar details on your [Google Business Profile](https://www.semrush.com/blog/google-my-business/), social media, and other websites
- **Use the most specific schema type**: Use the most precise schema subtype for organizations (e.g., Restaurant instead of just LocalBusiness)
- **Always test your structured data**: If your schema contains errors, Google may issue a [structured data manual action](https://support.google.com/webmasters/answer/9044175), making the page ineligible for rich results. While this won’t affect [SEO rankings](https://www.semrush.com/blog/seo-ranking/), it can reduce your visibility in search results.

## How to Check Your Website’s Schema Markup

Regularly auditing your site’s schema markup ensures it remains accurate.

Get a quick schema review with our free [SEO audit](https://www.semrush.com/siteaudit/).

To automate the process across your entire site, Semrush Site Audit helps you find and fix schema-related issues at scale.

After you [set up a full audit of your site](https://www.semrush.com/kb/539-configuring-site-audit), click the “**View details**” button under “Markup.”

You’ll get a markup score that indicates how much of your schema data is valid or invalid. The higher your score, the fewer errors you have.

![Markup report generated by Site Audit with the markup score highlighted](https://static.semrush.com/blog/uploads/media/d1/27/d127270ae500f58e9cd7cded21f051dc/e459a360166cff0cf8ce0d7e268279be/image.png)

To see a full list of errors, scroll down to the “Structured Data Items” section. And click on the “**View all invalid items**” button.

![structured data items in site audit, indicating whether structured data is valid or not](https://static.semrush.com/blog/uploads/media/a6/99/a6990fffb983c9ee836972c677be3c1c/3483c831586397f676da1a481df2e7b9/image.png)

Click on any entry in the “Affected Fields” column to see specific errors for a given page.

![affected fields for structured data issues](https://static.semrush.com/blog/uploads/media/ca/59/ca59c74bc60da71ce0bcdd43190454d5/4238693e8ea1a0971e7f80c9181a55d0/image.png)

If any errors show up for your site, revisit the [Structured Data Markup Helper](https://www.google.com/webmasters/markup-helper/u/0/) to generate new markup, then validate it again with the [Rich Results Test](https://search.google.com/test/rich-results).
