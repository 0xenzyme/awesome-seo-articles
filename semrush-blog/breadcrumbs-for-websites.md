---
title: "What Are Breadcrumbs? SEO Implications & Best Practices"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "breadcrumbs-for-websites"
url: "https://www.semrush.com/blog/breadcrumbs-for-websites/"
canonical: "https://www.semrush.com/blog/breadcrumbs-for-websites/"
author: "Vlado Pavlik, Christine Skopec"
published: "2021-09-14T14:57:00+00:00"
updated: "2025-07-30T10:29:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "time_sensitive_title"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T14:13:44+00:00"
status_code: 200
html_hash: "b15d64a3baac826ed24adccb929fa6e615cd5fbbd2adb35f681aceb573489ba2"
clean_word_count: 1947
clean_char_count: 14683
---
# What Are Breadcrumbs? SEO Implications & Best Practices

## What Are Breadcrumbs?

Breadcrumbs are navigational elements that create a trail to help users and search engine crawlers better understand the page and where it is on the website. And they typically appear at the top of a webpage.

Here’s an example of what breadcrumbs can look like:

![Eddie Bauer men’s pants page showing breadcrumb path Men > Bottoms > Pants above the product list.](https://static.semrush.com/blog/uploads/media/be/d1/bed1a5ae976a143229a0c0e3c9c921c1/eed26df27f3e0b838abb99571a9d3d4c/AD_4nXeK3Efl7xzzG-OZQKjwOAL3TNnYMGaWLCxLzdkg-SV1z9dihzMDJPBiKMLxOqmo4F4Vw-jpcDVPSfhTFsjniQRBXkLBv0Q_LsjyJfgT7ADJ4bQpDmct1-1AWnqEJxXB7qzu0GcIEg.png)

Breadcrumb navigation gets its name from the Hansel and Gretel fairytale that involves characters creating a breadcrumb trail to retrace their steps.

However, breadcrumbs don’t necessarily reflect the user’s journey to the page. For example, a user may follow a direct link to the Eddie Bauer men’s pants page shown above. But they’ll still see the same breadcrumb links.

Most websites should implement breadcrumbs, especially if they contain multiple subsections.

## Why Do Breadcrumbs Matter for SEO?

Breadcrumbs don’t directly affect rankings, but implementing them can still benefit your SEO. Here’s how they impact your website:

### Improving Internal Linking and Crawlability

Breadcrumb navigation uses [internal links](https://www.semrush.com/blog/internal-links/) that guide both users and search engines through your website. This makes pages easier to discover and surface in search results.

[Kirill Sajaev](https://www.linkedin.com/in/kirill-sajaev-14549715/), Founder of SEO agency AUQ, says his team uses breadcrumbs to improve navigation and crawlability for clients with many service and tool pages that don’t nicely fit into the top navigation or footer.

Each individual tool page is included in a category, and each category is included in the main tools list (which is added to the website footer). Like so:

- Main tools list page
  - Tool category page
    - Individual tool page

Kirill notes that this approach is incredibly helpful for getting pages indexed by Google:

> “The primary users of these breadcrumbs are Google spiders, which is useful because we can also add schema markup to these crumbs. So, even if our URL structure isn’t ideal, we can always specify exactly how Google should think about our content.”

If you implement breadcrumbs using [BreadcrumbList schema](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb), it might also impact your website’s visibility in AI search.

[Zach Paruch](https://www.linkedin.com/in/zachparuch/), SEO Content Strategist at Semrush, explains that structured data seems to play a role in an LLM’s ability to read and understand content.

> “These 'chains' make it easier for LLMs to grasp and recall the content—and serve it when users ask questions related to it.”

### Improving User Experience

Breadcrumbs allow users to quickly orient themselves on your website, which simplifies navigation to improve the user experience (UX) and reduce the likelihood of bounces.

This also has SEO implications.

Google’s [Navboost](https://www.semrush.com/blog/navboost/), a part of the ranking algorithm, uses real user behavior to influence rankings. Which includes whether users quickly return to search results from a webpage.

So, when users spend more time on your website, it indicates that your website’s content is useful. And it could rank higher as a result.

Just know better engagement isn’t a guarantee. If you’re on the fence about implementing breadcrumbs site-wide, conduct an A/B test to see if they have a meaningful impact on user engagement.

[Anton Shaban](https://www.linkedin.com/in/shabananton/), Head of SEO at MEDvidi, found breadcrumbs weren’t very beneficial for the MEDvidi blog.

> “Fewer than 0.5% of visitors clicked the breadcrumb links, so we removed them.”

## Types of Breadcrumbs for Websites

Before you add breadcrumbs to your website, consider which type you’re going to implement:

### Hierarchy-Based Breadcrumbs

Hierarchy-based breadcrumbs tell a user where they are on your site based on your [website structure](https://www.semrush.com/blog/website-structure/). This type typically shows the current page, the subpage the current page falls under, and so on until it reaches the homepage.

Here’s an example from ASOS:

![ASOS site showing a breadcrumb path Home > Women > Skirts > Pleated Skirts, with each item underlined.](https://static.semrush.com/blog/uploads/media/6b/62/6b62bea5122794f0ec5e0170cd67fd9a/e53c2542129961b2790b11ae4c65b9ab/AD_4nXd_XrAJu1nttNYOjJtoH9ZPTvgrvX8MmqySTOa8Y5kzkA9PZa0Nn4YpTvV-Tx-mGtbFf1MMtM6k0GXQZLNbLoqQjud-k_F9IUBmhNG8TvKI-7GfdkDv1EH_uo_D0JUP7NJevG25.png)

Hierarchical breadcrumbs are helpful for users who come from organic search. Because they allow users to discover other relevant content easily.

### Attribute-Based Breadcrumbs

Attribute-based breadcrumbs display what the items on the page have in common. They often appear on ecommerce sites alongside hierarchical breadcrumbs.

Here’s an example:

![Walmart category page with “All filters,” price range, and “Great Value” attribute-based breadcrumbs highlighted.](https://static.semrush.com/blog/uploads/media/28/cb/28cb42d4504c91bca12bdfd95c2fca2f/c91af312209c92af2f3562014704d289/AD_4nXcod6KHBnj0sYlHWygeAUD4Abi9TPsm5ZQwPBJ5T0265iH_Kj5fqVDA5w4MraaiVECbxjwhq-xqjniZ8oiX-nmkSstteMy3iyhCsMLHyResr8bZ_Ly7QfudoS9dJQgkqaAm73yx.png)

### Path-Based Breadcrumbs

History- or path-based breadcrumbs display your unique path to a specific page. Instead of outlining the website hierarchy, they only show the pages you have visited so far.

It would be hard to find a website with path-based breadcrumbs today. And if a website does use them, it’s usually as a back button that takes you to the previous page you were on.

![Adidas page with an arrow pointing to the “Back” link above a breadcrumb trail showing Home > Women > Running > Shoes.](https://static.semrush.com/blog/uploads/media/7d/ae/7dae29aede3dc61e70d01571f72ec738/367e8a6ffc74024e724b60c10d1331f4/AD_4nXfAp7pCDozmpJPesTWVHhjcgnWmhsPvwnxfhskyNV1f3fkJmtDcNPnjic60FA8CqQopjLQdh9STqz3dXUvYHEhWb5p3U75beTW_U5tNB8wcptrNyX1d95itZSmkznyiuRPD8ZRlBg.png)

We don’t recommend either option because users can do the same using their web browser.

That’s why you don’t often see these kinds of breadcrumbs. Website designers favor breadcrumb navigation types with more functionality.

## 5 Best Practices for Breadcrumbs

When designing breadcrumb navigation for your website, follow the best practices below.

### 1. Make Them Easy to See

Breadcrumbs should be easy to see without being obtrusive, and that usually means putting them in the upper left corner of the page.

Here’s an example from Plaid’s blog:

![Plaid article with breadcrumb trail highlighted: Resources > Lending > The Value of Cash Flow Data for Better Loan Servicing.](https://static.semrush.com/blog/uploads/media/de/64/de64b490dca46f6252fdc24ed1380338/12f852ddef51d5a476d4c3dabb332a56/AD_4nXeDheipZdfOy4vqcQGVRYNc1HFxooly4xpsI8ztNQYGOucPP-pGyMk56U0auZnCGbqei9J-NYw-Pw2Nv5wl1In0pZ8jbXqo9HEcT0rInmqBD7fBbZrbogZ3hyUapSpVL0191hHT0g.png)

### 2. Include the Full Path

Your breadcrumb navigation should include the full path from the homepage or main category page to the current destination. (There may be more steps depending on your site structure.) This allows visitors to retrace their steps and return to important parts of your site quickly.

This is especially important on mobile because the main navigation is often hidden behind a hamburger menu. Here’s an example:

![Bloomingdale’s mobile page with breadcrumb trail showing Women > Dresses > Summer Dresses above a product listing.](https://static.semrush.com/blog/uploads/media/b0/4f/b04fd6f3fa4d33a0104eb1ca6bfce868/1627962a84026da52151df1a7e3f9602/AD_4nXcVCXIKN31OsGHv5ATV4SnHu7JS9uuldV7B-ZoQFjq5_1PYCDNun_GSRXVOmkr8QNaXWvZYMTUkrifuzbvpRNdQQxv4Mm9IOFEti1JguxNDRELT37pVwjiEkXh8VgIHJvIln8z5OQ.jpeg)

This way, mobile users are only one tap away from going back to the “Women” category.

### 3. Use a Consistent Format

Breadcrumbs should appear in a consistent format to create an easy browsing experience for users.

You can make breadcrumbs consistent by:

- Using the same separators between levels (e.g. “/”, “>”, or “→”)
- Making sure the font and link color align with your visual guidelines and look the same across pages
- Applying the same type of breadcrumbs (e.g. hierarchy- or attribute-based) throughout your site

### 4. Don’t Link to the Current Page

Breadcrumbs shouldn’t link to the current page because such links have no purpose. And they might confuse users since they don’t direct them elsewhere.

But you should **list** the current page in the breadcrumb trail to help users understand their location.

This is also good for SEO because you can mention a [primary keyword](https://www.semrush.com/blog/primary-keywords/) (main keyword) organically. Naturally incorporating terms you’re targeting in this way helps search engines understand that your page is relevant to certain queries.

### 5. Add and Verify Breadcrumb Schema

[Adding breadcrumb schema](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb) helps search engines understand your website structure and how pages relate to one another.

After you add breadcrumb [schema markup](https://www.semrush.com/blog/schema-markup/) to your website, run an audit to check that it’s properly formatted.

You can do this with Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool.

Once you set up your project and scan your website, you’ll see a dashboard with thematic reports. Click “**View details**” below “Markup.”

![Semrush dashboard showing 90% Markup score with an arrow pointing to the “View details” button below it.](https://static.semrush.com/blog/uploads/media/2c/86/2c86ff283088ccce5d661f7a7be705ee/764716fc62928c97a91d2d65063f79c4/AD_4nXeBs29Sti3qcOYxUmA-VZSvzX-4e-f5zJmljvW8vjiX-a2v_441D6r3qi0YASVWMolPlYu5SsmdK9VnMfHZnjAnUqmYY4Pxz_-X5Iq-10RJgbVfIRZElw2twn2r0Bw6Dhhy8ie2JA.png)

Under “Structured Data Items,” find “Breadcrumb.” And check whether you have any invalid items in the “Invalid” column.

![Structured data table showing “Breadcrumb” row with 6,961 valid items and zero invalid, highlighted.](https://static.semrush.com/blog/uploads/media/0b/06/0b066a7d2a150b7015577c9ab649d9da/511d360ddf66a6f05516b6342c095316/AD_4nXfBRE_SkIu-aflCSuK3QOyr-XokB4e0gqVcreJRrwqD9R9M2UTntAojZsbgR7BcTD_ytGLK5ywNErnVFiNNJljkIKkkzqU-4CvAMc50eBWTpQ3WVFB8aUV-C2ZkkYkYUJaJuqk1.png)

If you see any errors, click the linked number to see a list of errors and affected URLs. From here, you can click the drop-down arrows in the “Affected Fields” column to find the specific fields that need to be fixed.

## How to Implement Breadcrumbs in WordPress

WordPress users can implement breadcrumbs by installing a theme that supports them out of the box.

Or you can use a plugin like Yoast SEO.

To install it, go to “**Plugins**” > “**Add Plugin**.”

![WordPress admin menu with an arrow pointing from “Plugins” to the “Add Plugin” submenu option.](https://static.semrush.com/blog/uploads/media/39/7d/397d787990680adaa67e4df059f5cbc3/23878e77ac0cb9e677a50bf579c6ebf4/AD_4nXesE5YU-uHNKtWDbXtxtSG3f3VNFKPo1IkvKcv8Zcgv40Xom5pcU2EAT0q2fYxVj2DlXNM8pPxJJHxtDcGAhTa4AwbNOArsC_ALWKlA_u7gUN4Oiq1tTdF74cGjBSIFjpNjBN4FVA.png)

Search for “Yoast” and click “**Install Now.**”

![WordPress add plugin page with an arrow pointing to the “Install Now” button on the Yoast SEO plugin card.](https://static.semrush.com/blog/uploads/media/ff/8b/ff8b72bea7b49ccd9a5497cbafadc7b7/e7a10902dd2d66192b82889a4c9c4d4c/AD_4nXdAN4kz3ctOQBEuwsKlFwVGMqW4wyW2yT9pE1JfdyQGrfDEmKnFxZvW8RCNkoYWrn6FaE-Zjw5oA-vIOeSCWQE0n_ZaGJa8BFEcwl1DtW8guQTlw1-2aLHpFz14SKswv7FwNQzWJQ.png)

Once the plugin installs, click “**Activate**.”

![Yoast SEO plugin card in WordPress with an arrow pointing to the blue “Activate” button on the right.](https://static.semrush.com/blog/uploads/media/8c/a4/8ca419413f41281905dbe7a69b85ae5c/bfb720c0c25685c5e8c3a8cdae4e5f49/AD_4nXfa-lXU8dM71urNDPnVwfyfd3xqdLdRNOzEZv8F_pAdTtwPrKRtsMAWOdt0BshBqO0x8eDZprhDPmBqfD_vOleshJuYZwkY5JS0bCPqR1dkWcpHEYEmyDnr9UqoaEM0S_9KUuXlUg.png)

Next, you need to add a piece of code to your theme. If you’re uncomfortable making technical changes to your website, ask a developer for help.

To proceed, copy the code below and paste it into your theme where you want breadcrumbs to display.

`<?php
if ( function_exists('yoast_breadcrumb') ) {
yoast_breadcrumb( '</p><p id="breadcrumbs">','</p><p>' );
}
?>`

After that, go to “**Yoast SEO**” > “**Settings**” from the sidebar. Then, select “**Advanced**” > “**Breadcrumbs**.”

![Yoast SEO sidebar with an arrow pointing to the “Breadcrumbs” section under Advanced settings.](https://static.semrush.com/blog/uploads/media/a9/6c/a96cd3d968e162b22d75117bd3635873/531c08a4e476972f5872dfb598a191cc/AD_4nXdEPfbJJ-TIdcn5v4S9I08WkfP6rmhUfQJm5G2egLwoPZ5MMfzky7O73Au2RfY9qPPqhy0-IPNCDGXYQNj86cuf3_GyKHpxa7AI6g_PTk6gQ0GCDi-HT1QE5v08t5zVQU2Qf1j8.png)

Here, you can configure your breadcrumbs and customize how they appear on your website.

![Yoast SEO Breadcrumbs settings screen showing fields for separator, homepage text, and prefix options.](https://static.semrush.com/blog/uploads/media/68/6f/686fe730dffc0c01f113f677510ae1a3/d5a597385afec3464fa50395f16760e6/AD_4nXfhDSTYiNH45U1-CVHSkWhH_7F0p_U-T7Wz9Pk9BfS6DRFkHBnEQxOWaK77axmOwuqB_gGlmw4b8zb8v7B4Xgao612qPY-ZS3NPv_tKkg6L8CqIxjHmmdsan1RKkYJQuAG8Yha6qg.png)

When you’re ready to push the changes live, click the toggle next to “Enable breadcrumbs for your theme.”

![Settings panel with the “Enable breadcrumbs for your theme” toggle switch highlighted.](https://static.semrush.com/blog/uploads/media/e4/4c/e44c4280537b6c077692e6ff8a99a466/0b5f92ca53d177062811068954b30095/AD_4nXfiOGp6XtAJ3kmAZZrKxwVfjKp1LfA_6Z2egbdhxUhkriWXk30qlM6vDIvJ0ZK5lDmS2jmdaEIa4RXBHQ6I081gNbvjIB8jGc5c1RePy2rPKA9oOOg-4o7QSNGNS-jjlFhEBXjNfA.png)

## Implement Breadcrumbs for Better UX and SEO

Breadcrumbs remove navigational friction for visitors and keep them on your site longer. So your website appears more helpful to search engines and can rank higher.

But breadcrumbs are just a small aspect of SEO. You need to consider backlinks, topical authority, technical performance, and more.

Semrush offers AI-powered SEO and content marketing toolkits to help you optimize every part of your website. Explore them with a free account.
