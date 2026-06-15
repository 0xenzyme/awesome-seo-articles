---
title: "Nofollow Links vs. Follow Links: All You Need to Know"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "nofollow-links"
url: "https://www.semrush.com/blog/nofollow-links/"
canonical: "https://www.semrush.com/blog/nofollow-links/"
author: "Vlado Pavlik, Zach Paruch, Tushar Pol, Christine Skopec"
published: "2023-06-07T10:15:00+00:00"
updated: "2024-12-03T15:41:00+00:00"
categories:
  - "Link Building"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "Link Building"
fetched_at: "2026-06-12T18:10:29+00:00"
status_code: 200
html_hash: "6c39982892696eccb60394c9c5fdb29740d68443c5f0a8d648f625307a8d3e6f"
clean_word_count: 1553
clean_char_count: 11217
---
# Nofollow Links vs. Follow Links: All You Need to Know

## What Are Nofollow Links?

Nofollow links are hyperlinks that include the `rel="nofollow"` attribute in their HTML code.

The `nofollow` attribute instructs Google not to crawl the linked page and not to pass link equity (ranking strength) to it.

An example of a nofollow link in HTML code is:

`<a href="https://example.com/" rel="nofollow">Click here</a>`

The presence of the `rel="nofollow"` attribute confirms that the link is a nofollow link.

## What Are Dofollow Links?

Dofollow links, also known as "follow" links, are the standard type of hyperlinks on the web. These links do not have any special attributes like [“nofollow,” “UGC,” or “sponsored”](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links) attached to them.

Because they lack these attributes, dofollow links pass link equity (ranking strength) to the linked page.

An example of a dofollow link in HTML code is:

`<a href="https://example.com/">Click here</a>`

The absence of a `rel` attribute confirms that the link is a dofollow link.

## How Do Nofollow and Dofollow Links Differ?\*\*

Nofollow and dofollow links differ in how they influence the search rankings of the linked page.

Dofollow links can boost the search ranking of the page they link to, but nofollow links likely cannot.

For example, linking to Apple's website like this:

`<a href="https://apple.com/">Apple</a>`

creates a dofollow link that can influence Apple's search engine rankings.

Alternatively, linking like this:

`<a href="https://apple.com/" rel="nofollow">Apple</a>`

includes the `rel="nofollow"` attribute, which generally will not pass ranking power to Apple's site.

Are nofollow links completely useless?

Not exactly.

## Why Are Nofollow Links Important?

Nofollow links are important for several reasons:

## Referral Traffic

Nofollow backlinks from popular websites can drive referral traffic to your site. Even though these links do not pass link equity, visitors can still click on them and reach your website.

For example, some sites like Forbes use the `nofollow` attribute for all external links. In an author's byline, the link might look like this:

![A link with nofollow attribute in author's byline](https://static.semrush.com/blog/uploads/media/5f/98/5f98743fdb0ab54530d02871a3d784a3/c238eecb1a48eae66057f7023a931f58/AD_4nXcOGz5GFA99LGk6cAK7EenYCXakCmUMnEMZxftIizCbWr7bElvEWjqtsMQgQIOmJqGiIrqXpj7p1bUykXj9goU8SDGhNhNicP1LlQzfevLpsrj35A1NCqifmEP389CWUUvCtHG6eA.png)

Receiving a backlink from such high-traffic sites is beneficial because their large audience can click the link and visit your site.

## Exposure

Being mentioned on popular websites is great for brand awareness and can naturally lead to more dofollow backlinks from other sites.

For example, if a popular blogger links to your site but uses the nofollow attribute, it still raises awareness of your brand among their audience.

Multiple readers may then organically link to your site, and those links could be dofollow links that pass link equity.

## Backlink Profile Diversity

Search engines value a natural and diverse backlink profile that includes a mix of both nofollow and follow links.

A website with only follow links may appear unnatural or manipulative to search engines, potentially triggering red flags.

By maintaining a healthy balance of nofollow links, your site demonstrates a more organic growth pattern.

That's why nofollow links are also important for SEO.

## How to Check If a Link Is Nofollow

To determine whether a specific link has a nofollow attribute, check the page's source code.

Hover over the link, right-click it, and select "**Inspect**" (this option may have different names in different browsers).

![“Inspect" option selected for the chosen link on a site](https://static.semrush.com/blog/uploads/media/a0/11/a011a784a7579c877ae3f3ef463239ef/26cf1c6a6c0d02495fca21b6748e21cd/AD_4nXcZabvrqWaLzsnlW1HbBtMbCjP7Z9lO-yxF0KoX7HQIDVd0OHX5LOkMch_uMb3gKOkW1_CgnKkp-TSILqc_1kY6RqNGxzHow3C1V14y6tKiJamuw7csNMmGnySOe01MXiOWMMiSWw.png)

If you see the word "nofollow" within the rel attribute, the link is a nofollow link.

![A section of source code with rel=“nofollow noopener” attribute](https://static.semrush.com/blog/uploads/media/9a/9c/9a9c22ae10a623406ba481041df125b6/75df5b92d2ab126ff9d708236763d3d7/AD_4nXdUsjqK0_XtYQ4bIDvbO1PL1NPQ03TuO6eYMrHBa-CWAMA7KVmxytgnlF35O9xjEfiR79pErzNUfsX_ZYODYJCUq9QEVHByZmSwH5yi5eE57lergorN7BRCeAvs76T3vo-1c-lN.png)

To analyze the distribution of follow and nofollow backlinks to your site or a competitor's site, use tools like Semrush's [Backlinks](https://www.semrush.com/analytics/backlinks/).

These tools provide a detailed breakdown of the attributes of the links pointing to a domain. You can also apply filters to view specific backlinks with certain attributes.

For example, to see only active "sponsored" backlinks for a domain, select “Active” and “Sponsored” from the filters at the top.

!["Active," and "Sponsored" tabs selected under "Backlinks" report](https://static.semrush.com/blog/uploads/media/57/71/5771f8406bb65ba939a4dd0ee74757db/6c0a1290290996bf76d951d1603e8a27/AD_4nXefrDIjfJIKf4M4gkomTfDinVFUshq4sVAPSpt9qxE-qjJ-fAre9mNoUrsgdKX9u8rdf0WY1Ibl0z0j3TWne3MtAfmlULB4N5WE7_RjU12PmzHV1g-M0m6GYx6zydSjdgm4BDz6.png)

The rel="sponsored" attribute indicates links that have been purchased, such as by sponsoring an article on a blog that links back to you. Google treats these links the same as nofollow links, meaning they don’t transfer link equity.

Using these tools can be useful for inspecting the [paid digital PR](https://www.semrush.com/blog/guide-to-digital-pr/) activities of your competitors.

## When to Use Nofollow Links

Here are the most common use cases for nofollow links:

- **Linking to a Page You Don’t Want to Endorse**: If you prefer not to be associated with the linked page—for example, if you need to link to a gambling website but don’t want to imply endorsement—use rel="nofollow"
- **Including Sponsored or Paid Links**: If the link is sponsored or purchased in any way, use rel="sponsored." This applies to both links pointing to other sites from your site and links pointing to your site. Make sure others linking to you with a paid link are using this attribute correctly.
- **Using Affiliate Links**: For affiliate links pointing to or from your website, also use rel="sponsored"
- **Incorporating User-Generated Content**: For links created by users on your website, such as in comments or forum discussions, use rel="ugc". This helps prevent people from spamming your site with links in an attempt to improve their search rankings.

## When to Avoid Using Nofollow Links

In the past, the nofollow attribute was often misused to manipulate how link equity passes from your page. For example, some webmasters applied the nofollow attribute to all external links to pass more link equity to their own pages through internal links.

This technique, known as [PageRank sculpting](https://www.mattcutts.com/blog/pagerank-sculpting/), no longer works because Google changed how it handles nofollow links for PageRank. However, some people still misuse the nofollow attribute, and bad practices persist.

Here are two common examples of how not to use nofollow:

- **Nofollow for All External Links**: You shouldn’t apply the nofollow attribute to all external links pointing from your site. Doing so doesn’t help your website and [may even harm it](https://youtu.be/CslpJABCE2w?t=3302).
- **Nofollow for Internal Links**: You shouldn’t use the nofollow attribute for internal links. If you don’t want a certain page to be crawled or indexed, use other methods like [robots meta tags](https://www.semrush.com/blog/robots-meta/).

If you’re unsure whether you’re using nofollow correctly on your site, Semrush's [Site Audit](https://www.semrush.com/siteaudit/) tool can help.

To use the tool:

[**Create a free account**](https://www.semrush.com/signup/) (no credit card needed) and set up your first crawl. If you need guidance, follow this step-by-step [setup guide](https://www.semrush.com/kb/539-configuring-site-audit).

Once the audit is complete, navigate to the "Internal Linking" report by clicking **"View details."**

![“Internal Linking” widget highlighted in Site Audit's overview dashboard](https://static.semrush.com/blog/uploads/media/08/20/0820819396a89abc51f1856dad1462ea/d2459b5f7c28c936c2af79f051c46128/AD_4nXcQAmAbUA8y9WCfFREa9e-lVII-KVt91UXGEv9dCX-WUKrU_-rIurdY7O3CY_ErOa9FtkBOz6Y-H_JJK2Ko_nr5xZDE6FHcTmCPCnuXP7Wy2g3EeL_0oKEKgOSFFrNSW5xXdbpoqQ.png)

On the right side, you’ll see a list of possible issues related to internal linking.

In the "Warnings" section, look for "Nofollow attributes in outgoing internal links."

![“Nofollow attributes in outgoing internal links" result highlighted under "Warnings" section](https://static.semrush.com/blog/uploads/media/59/a4/59a46fce3485258b4d5932e882021cb0/a2d61d7163edbc72c0c8ab4a13264a05/AD_4nXfJkH3TKBVTPoY2dpytNqJzLCBzgwSkxccxUjAQUWxq9wk-4Kpv7R0xunt0uNOmarMwA1-3d-MH2R533nhLOI7ZsJeLhfGvSEwJk07oY899m4CE55G2tjMkHvbtBAexMVUpyy6WGA.png)

If the tool detects issues, click the link showing the number of issues. This will lead you to a list of pages where nofollow internal links were detected.

![A full list of pages where nofollow internal links were found](https://static.semrush.com/blog/uploads/media/03/59/0359d5dfa7927eb6bc586c58f93d3ec2/0e42c27884d26e6b51dfffe2c6b09c02/AD_4nXcfVGHBpZfiWCeu0at0oyt6AX9lBWCKJo_l2Y9oIMIOpFLCqAcIZyF5qWp6s8Sig3UbWDyTqhgc5vKUV2exkGMY_TKwZcteW2asFwkETVxnY05-JbEn0V2cHnfPe_KMm-sBnFKTUw.png)

Review the list and remove the nofollow attributes from internal links.

Next, review all your external links with the nofollow attribute:

Look for the "Nofollow attributes in outgoing external links" issue in the "Notices" section.

![“Nofollow attributes in outgoing external links” issue in the “Notices” section](https://static.semrush.com/blog/uploads/media/84/5c/845c5474247d33904c76ff259de0670a/3becbd0381feee3cf9f3cf890741301f/AD_4nXfJEHI9yVCsmN7zJ9Ogfsn8iE8i_Vw7uTyh8fEROt5BGRTUYS-R3BM7Y4v8Q4RRQtZQi1FgQbeODfTkyWwiX0dzrA3a9GDmgWJsRitjAKNpoB5m7gnrP_FYR-9gQ4bF7pb-jZgl4w.png)

Go through the links and reconsider your use of nofollow attributes. Ensure they are truly necessary.

By properly managing your use of nofollow links, you can avoid potential SEO issues and improve your site's link equity distribution.

## Next Steps

To deepen your understanding of how links impact SEO and how to obtain the best backlinks for your website, explore these resources:

- [**What Are Backlinks?**](https://www.semrush.com/blog/what-are-backlinks/)
- [**Link Building for SEO**](https://www.semrush.com/blog/link-building/)
- [**Backlink Management**](https://www.semrush.com/academy/courses/backlink-management-course-with-greg-gifford/) (free video course)
- [**Internal Linking**](https://www.semrush.com/blog/internal-links/)

If you want to start building links immediately, try our [**Link Building Tool**](https://www.semrush.com/link_building/). With a [free account](https://www.semrush.com/signup/), you can begin your first link-building campaign.
