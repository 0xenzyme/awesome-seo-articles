---
title: "What Are UGC Links? (Vs. Sponsored and Nofollow)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "ugc-links"
url: "https://www.semrush.com/blog/ugc-links/"
canonical: "https://www.semrush.com/blog/ugc-links/"
author: "Sydney Go, Simon Fogg"
published: "2024-09-05T09:38:00+00:00"
updated: "2024-09-05T09:38:00+00:00"
categories:
  - "Link Building"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "Link Building"
fetched_at: "2026-06-12T20:19:19+00:00"
status_code: 200
html_hash: "c5287bc231987ad4a756bbfb64a870d8b0615d56f90f60fd9b011b8d3bf3630e"
clean_word_count: 3507
clean_char_count: 28047
---
# What Are UGC Links? (Vs. Sponsored and Nofollow)

User-generated content links, or UGC links, are hyperlinks found in customer reviews, blog comments, and other types of content created by visitors or random users.

If your site allows visitors to post content, add the UGC attribute (rel=ugc) to the links they share. So Google knows you’re not responsible for the content of the linked pages.

Here’s how and when to use the UGC link attribute—and why it matters.

## What Is a UGC Link Attribute? (rel=“UGC”)

The [UGC link attribute (rel=“UGC”)](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links) is an HTML value that indicates a specific link is user-generated. Which means you didn’t create the link. And aren’t vouching for the page it points to.

Telling Google that a link is user-generated is important because Google sees links as a vote of confidence. And linking to poor-quality sites can hurt your search engine rankings.

In your website’s code, the UGC link attribute looks like this:

`<a href="http://www.yourwebsite.com/" rel="ugc">Link text</a>`

By comparison, a plain link has the following structure:

`<a href="https://yourwebsite.com">Link text</a>`

Other link attributes include “nofollow” (rel=”nofollow”) and sponsored (rel=”sponsored”).

Similar to the UGC link attribute, the other two link attributes also help Google understand more about the links in your content.

The “nofollow” link attribute tells Google you don’t want your site associated with or connected to the linked domain.

It looks like this:

`<a href="https://yourwebsite.com" rel="nofollow">Link text</a>`

The “sponsored” link attribute tells Google the link is part of an ad, sponsorship, or other arrangement the website owner was paid to place.

The “sponsored” tag looks like this:

`<a href="https://yourwebsite.com" rel="sponsored">Link text</a>`

## How Does the UGC Attribute Affect SEO?

The UGC attribute doesn’t have a huge impact on search rankings.

When a website links to another, it passes authority to the linked page, which can boost that page’s search engine rankings.

Unless the link contains the rel="ugc," rel="sponsored," or "rel="nofollow" attribute. Then, the link is unlikely to pass on an SEO benefit.

However, Google now [treats link attributes as hints](https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify). Which means Google may consider a UGC link within its search ranking systems.

Google has also said that it analyzes these attributes to detect patterns of [unnatural or spammy links](https://www.semrush.com/blog/unnatural-links/).

For example, some webmasters leave spam comments on forums and blogs—along with a link back to their sites. Their goal is to manipulate search engines and generate more traffic.

Link in this example below:

!["Comments" tab of the Wordpress CMS showing multiple user comments that include spammy links](https://static.semrush.com/blog/uploads/media/fa/77/fa772cec4df018276e60e0636a64e28b/4ae49126519298d0b41dd63c861c4229/AD_4nXc9kLJHxsf2DcUwwY5nS97tesVnd0FdzwP0p8peXFDMZh1EfY2f_n_MoMRQYEg_OnXRzrRhq6u8SoEvn2ylQBMKaX7lzG7wfjRY_bcdIwT-b_hA-b4T2xzOY-tQcgeevEcDpTk2BTeq_3o3ZhNKz8Tx-kds.jpeg)

In some cases, UGC links can indirectly impact SEO. For instance, relevant UGC links from authoritative sources (e.g., a CNET product review) to your site may increase traffic and engagement.

And linking to spammy websites may harm your SEO efforts. So, if your website allows user-generated links in comments, articles, or customer reviews, be sure to add the UGC link attribute.

(Many website comment platforms will automatically add a UGC attribute to links within user-submitted comments. Or will provide an option to do so.)

***Further reading****:* [*Types of Backlinks: Which Ones Help Your Website?*](https://www.semrush.com/blog/types-of-backlinks/)

## How to Find the UGC Links Pointing to a Website

Quickly find UGC links with Semrush's [Backlinks](https://www.semrush.com/analytics/backlinks/) tool. This information may come in handy when you're researching your competitors or a domain you want to buy.

A domain with lots of UGC links from irrelevant or questionable sites may engage in spammy activities. So you might think twice before purchasing it.

To find UGC links, enter a domain name (yours or your competitors’) into [Backlinks](https://www.semrush.com/analytics/backlinks/). And click "**Analyze**."

![Backlinks tool with "www.financialsamurai.com" in the text field and the "Analyze" button highlighted](https://static.semrush.com/blog/uploads/media/41/ce/41ce444e6db39655057325992e272f89/42cfd44f9318534778114a254089793e/AD_4nXctbTecyXFzJfxZ_8se6iqaZ7pDsHyI9WP_1_ILmySQI66c5xvCgTj_oafQM6Z7PloOfELkyaAR9Zoi4wyud54lUwjvyDIezgPeYS-gbcqqtx4ooyvZ1W2NYlHOboUQbt4n1v1ZSWyLqGmxcldhMPrRXILF.jpeg)

Semrush will scan that domain and the links pointing to it, otherwise known as [backlinks or inbound links](https://www.semrush.com/blog/what-are-backlinks/).

And then generate an overview that includes the website’s link profile, organic traffic, top pages, and other data.

!["Overview" tab of the Backlinks tool showing various data related to the backlink profile](https://static.semrush.com/blog/uploads/media/9a/e2/9ae2ca44fbdf344f132a501ae0f13903/0730494b558d57917ddd2ea6c53655ec/AD_4nXdoHU7qYbrIVKfI56Mdm5R2M4ymr34IcT47ga8qeQ7WQauwtQMuowhofeKRgq3MaljC-i5swJ-3mor7r9Gx5l6RSEnQzjO6DChZigFTfLXwvCCA5P1ADVmIyXVUwVVa-wM-eWbeHmLE9APLaSRXhVLd4Ao.jpeg)

Next, click the "**Backlinks**" tab.

!["Overview" tab of the Backlinks tool with the "Backlinks" tab highlighted](https://static.semrush.com/blog/uploads/media/b8/78/b878eecf8a565056018df830874464f8/7e5298999aa33b9b6d3bbce2f948623e/AD_4nXcWnmhfy6mFG7LqoClzFssHnOd10CVGrJ6rHxtl3z0ccRjMZO5PxhU9uMfcyxw11Ui0-drcMCeP8Kb9kBrwylQTl_srmWvymynwBkImHi9HC6AflzU8DuQKkuiD7rY_ERh6vYvkbjUcPBUhnKt86PRXDNE.jpeg)

The tool will take you to a new page displaying all the links pointing to that domain. From here, you can sort and filter them by status ("Active," "New," or "Lost"), attribute, placement, and other criteria.

!["Backlinks" tab of the Backlinks tool with the "Active", "New" and "Lost" filters highlighted](https://static.semrush.com/blog/uploads/media/85/a2/85a2a9eda951ad3bc0a48b7af099727e/23c6bcf3ab59e5b16bdfe47c00bdf5f7/AD_4nXfnd6aw88c9l3Mtx9ho1RCH5CTPxK3AG6fcxCYoy048s3-Y8o5moym1P1xBnKfcrnJqHiBkN1ucJaK_ah94MKYNnCHYJGudDNyDOTcL1Q5zeSmKL6JOGhJcPy20HmmIFG_Eeb_i8rT_8iMjYVanKuLSOeQ.jpeg)

Go to the graph labeled "Link Attributes," and then click on the bar or number beside "UGC."

![Backlinks tool "Backlink Types" and "Link Attributes" sections with "UGC" bar and number highlighted](https://static.semrush.com/blog/uploads/media/1f/cb/1fcb6658c25a42adc14723c66d38e736/58d2f1197f5243700e4fa289ac9545ce/AD_4nXc99Hsdx6k-8uAMnPvjsVUWktsFK8xfmX2RsYm-JbN9XXZuUar3gjAUEyrmp0mR1VZ7IZn7wWsNUMpDmYo9q6HnNjx1C2HC7LRTIGCxpk23PLTbbq6xzFAf-uxxmjBdps22F25fLdq_XXBdhgT3wjOB8hcm.jpeg)

Semrush will display all the UGC links pointing to that website.

!["Backlinks" section of the Backlinks tool with the "UGC" filter and "Source page" column highlighted](https://static.semrush.com/blog/uploads/media/0c/e7/0ce7722bc56ee03140bfde7ec056b0aa/69856b8eacbf38478983edcc1afda965/AD_4nXfHMgszghb9LXE2CFYhcbVmxGM5GjlqvWcYbd6QljM3IbOBaehOFo5y3HLYm64qwQRMG-S0oGpDdrBcynXubrkTlTdy3k6CPpgzmk5E6BCSDx_tQbiw6iS-nkTbfR-O_HCkd7DuAx_WfQzcbwF7epcVPV8.jpeg)

This data can provide insight into your competitors. For instance, you can see if there's a way to get UGC links from the websites linking to them.

## How to Use Link Attributes

All three link attributes—UGC, sponsored, and nofollow—serve a different purpose. Each communicates to Google what kind of link appears on your page.

And give Google some “[hints](https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify)” about how to treat that link.

Sometimes, you don’t need to use a link attribute. If you want to pass authority to another page on your site, for example, you can skip the link attribute.

Here's how to use these link attributes to help Google understand your content better.

### Automatically Add the UGC Link Attribute to Comments and Reviews

If your site runs on [WordPress](https://wordpress.org/), you can use plugins to automatically add the rel="ugc” attribute to comments and reviews left by visitors. Here are some plugins that work well:

- [All in One SEO (AIOSEO)](https://wordpress.org/plugins/all-in-one-seo-pack/)
- [UGC Comments](https://wordpress.org/plugins/ugc-comments/)
- [WP External Links](https://wordpress.com/plugins/wp-external-links)

Say your website allows visitors to create and publish content such as reviews.

Use AIOSEO to add the UGC attribute to the links they include in their posts. Like this:

!["Insert/edit link" window of the ALL in One SEO tool with the "Add rel='UGC' to link" box checked](https://static.semrush.com/blog/uploads/media/fd/15/fd15be019431020eb45278195c1e99f1/9c2edbc27b809c833b5db8dcb87a117d/AD_4nXcUd6xwlBgOyuDWeIDRLlyoDmjt96p3r1bGAGeJGt0uTpjB5bDlIczDDw6lbZnuDlRByZ2ZDm53yl7oO7ae1xnilpjeuC7w8Z4_HJsa8qraJWzzUahzOCgQf8rf4ouQepzU0aUhwg-az5FlBzGLuGRsu48D.png)

Also, install the UGC Comments plugin to automatically add rel="ugc” to the comments left by visitors:

![UGC Comments plugin with "Add 'ugc' attribute" box checked for the "Comments Links" section](https://static.semrush.com/blog/uploads/media/4d/1b/4d1b58c9f4968ad3fbdebfc879adacce/9cb921493b0e5fa0062c5cab704d8f6d/AD_4nXc0-3HQRr5n-3r19xEF1hqBaLqRQq3nvHTmUJ8hALF4jknNd79nB04lCs9KzHnyc-IdYHc3tELReZ_tAj51UpmhIc7EBetf7zxUVJPAB9vW50TS4k2jkJz4o959pzuhXNlc2b2ZF5qvpcZtclF-g1bPirs.png)

Now open any page (on your site) that has comments from users.

![User comment that includes a link on a website](https://static.semrush.com/blog/uploads/media/c0/d0/c0d063a469876f6805afb66759935c48/6d80ec265318d670a6e19f6e41925526/AD_4nXcj3SXrRo7wIm5d2qiYE-Zff742Yu4GrZj8CnZnZs9o_Emx7AxDKvTv1Vem7euVu0PrFAwlzfKGFTzBq2EeUy6XkhX9djlNG5hLvN8mahNNZX1H6Yw38bHDG420jWjaeGld16qBNrHnllGW07Opl8BF3Fwb.jpeg)

Right-click on the page and select “**View page source**.”

![Google Chrome's "View page source" button highlighted next to the previous user comment](https://static.semrush.com/blog/uploads/media/68/23/6823e8a8761df085b281273044ccbddf/a6b608ef89fd68c64579fea842c52bd2/AD_4nXdhvBkCCUiHDLh0qBJdoK-eGJ2Gqf6p5JFHJ4mg2Mpwlws8MaVUaSYHui76MPUqbg5mJ3TG-GbwglMWq-fAeS4xDmAu-Wwc3NEvRGS1bKsZfmCajV0RXzIYqpHaFPP0p1HjDdveJNFyEFl9-FaycTa--D9e.jpeg)

If there are any links in those comments, they’ll have the UGC attribute.

![Page source of the website showing the user comment HTML code with "rel='ugc'" attribute highlighted](https://static.semrush.com/blog/uploads/media/e6/2b/e62b1add5312a67e875e864c2675818a/031f428988c74665945e597535621d6a/AD_4nXdCh5GuyGd86iUd0XPL-9hYXbRwoBFf3Y9FcnQwILYG6N3M_x-ErDaTDlCmik1Gxjz5RIntb7EYhnU0QaE0CvLBk0WMbcxR_l554FVdYvRfSJq-CaoptcSFhYb3CCd0EC8NU64y8gLevZ3k-vKLoXbwMOAY.jpeg)

### Add Sponsored Links to Paid External Links (rel="sponsored")

Add the "sponsored" tag to any links pointing to sites that paid you to link to them.

Let's say a company paid you to link to their newest product in your next blog post. Use rel=“sponsored” every time you link to that product to tell search engines that they paid you to mention them.

The link would look like this:

`<a href="http://www.yourwebsite.com/" rel="sponsored">Link text</a>`

Do the same when linking to other websites in sponsored reviews, advertisements, or affiliate blog posts.

Semrush's [Backlinks](https://www.semrush.com/analytics/backlinks/) allows you to check a website's sponsored links.

**Doing so will give you a better idea of your competitor's messaging and offers. And their partnerships with influencers, brands, or other third-party products.**

Simply add a domain name, and then go to the "**Backlinks**" tab.

!["Backlinks" tab of the Backlinks tool with "myprotein.com" website used as an example](https://static.semrush.com/blog/uploads/media/2d/cc/2dcc54afe561cc4cd021e4c594be8586/52989622a3b46fa9161f1200c17f869f/AD_4nXeROh70WCT-SpAzdQn79CMexxQdFS8xrNrJmbSGcOhGodvMwL7WiUdg2cZTjQoOU5vjVkDKX-xS6suKwh3Mog9Tj8aAtfGKCkuc2j3-ll459ldlgAuAGBT8XixT31Kv5aPWonNnyaUuElzPO13sxc0h0L7D.jpeg)

Next, click "**Sponsored**" from the filtering menu to see the sponsored links pointing to that domain.

!["Backlinks" section of the Backlinks tool with the "Sponsored" filter highlighted](https://static.semrush.com/blog/uploads/media/0c/f7/0cf76b9bff4c627a7eaa33cb06fbbf25/daea6f9d78dd111c94cedb365d03d806/AD_4nXfEhwOth4bfWoQW6tFZ0oNdQ4l-rOdxj_akGulVJHyBnSbTtUqrnAAuLlrdsulDo2jcn-Jnli_915u8XZ_9r1tDe9SgfVlnROVJdL_6EfaZtKrFq9Cn6G3IF04vg7FdmiuLo2eTFU3_Gwk8zkXjEgCRkTQ.jpeg)

Click the "**Active**" tab to exclude any lost links from the results.

!["Backlinks" section of the Backlinks tool with "Active" and "Sponsored" filters highlighted](https://static.semrush.com/blog/uploads/media/14/01/14018c2ec523cf8c1b38977ba2e6d22d/494149f92994c07a8d5c3e273714cd17/AD_4nXe3awTAjJbX9szPYHIEn-2iuD-AGZrdOnp_wifk2p7J9jOMKNmNZxar35wC9mQw-robVBMOz5BdYUMq4OTqnzBGbaA2nTGoKkA9tRiGUj-Jtm0oTJnKX4LSbPTMfG-x0JNy7ynsuxBB8sSbvjdGNPfXUpTg.jpeg)

For example, MyProtein has around 2,300 sponsored links. Including two from a product roundup featured in The Telegraph.

!["The Telegraph" sponsored link with two "Myprotein" product links highlighted in Backlinks tool](https://static.semrush.com/blog/uploads/media/7d/05/7d05a33643742127bae21830ea417596/fdebc88dce3f99f4ed8671062bcab214/AD_4nXd8Y9cPM-J0QsXFmsMoyHsJcMFTZF9m0o9oFvBuFbKQm7ZmFTk2FJbJbth1pd00DEaFMMcDfl5DbkTbK0FHVLTvAeAHm_c1RdUF4snc8_6tqZEJeeVciuAwIYDS2qyqtKm8glC_JKbZNEu6YSMtFreeFOEp.jpeg)

If you’re in the protein drink space, you might want to contact The Telegraph to place a sponsored link, too.

Likewise, you can use Backlinks to check the sponsored links pointing to your domain.

**This way, you can see if your partners hold to their part of the deal and link to your brand or products as agreed.**

***Further reading****:* [*Sponsored Content: The Ultimate Guide with Inspiring Examples*](https://www.semrush.com/blog/sponsored-content-guide/)

### Add the Nofollow Attribute to Content You Don’t Vouch For (rel="nofollow")

Add rel="nofollow" to any links you don't want Google to associate with your website. These may include:

- UGC links
- Sponsored links
- Low-quality links
- Unapproved links

Here's an example of a nofollow link:

`<a href="https://yourwebsite.com/" rel="nofollow">Link text</a>`

The nofollow attribute is catch-all. And you can add it to any links you don’t vouch for. Including UGC links.

Again, you can use [Backlinks](https://www.semrush.com/analytics/backlinks/) to find the nofollow links for your website or other sites.

This time, click the "**Nofollow**" and "**Active**" tabs.

!["Backlinks" section of the Backlinks tool with "Active" and "Nofollow" filters highlighted](https://static.semrush.com/blog/uploads/media/f8/9a/f89ac1213bf97415d2b50194f49081f3/bcc17cf58fcf0e348abe081b8efed23e/AD_4nXc5mbiy5cmL2cuVszaDCegCdbNYA7W11BrhJPrbe2W8IZaern2BNBlw7BCYgzNB1bExvILIKfdZEqxw2WXULnSrkptpJRDftNV9tIErnU4nFFF-mlUxiJsmiGMcvEf_2059uEVxRENWM9ut5wy_vvbCWbwF.jpeg)

For instance, MyProtein has a nofollow link from Muscle & Fitness.

!["Muscle & Fitness" nofollow link with the "Myprotein" link highlighted in Backlinks tool](https://static.semrush.com/blog/uploads/media/ed/31/ed316c46f21c5da5dfeac07c3384b452/950a370a298eb3211cc06950f0b35940/AD_4nXe32EhFf_LEv9WmSS-9yRlTBXhKeexWA3ROPY-Wd0fwaOaLBqFArSB6SnOIZm5o6JyGbzsxB_Jh9KHDaDNZzRP-_BZpiPSvLvcLfPy3_fmmSvkK5AL5jFLVAUf_w2ccWU7eqGqUK0Bhz9A_5h9fKW6lBNBN.jpeg)

Muscle & Fitness has an article about the best and worst whey protein powders. And mentions MyProtein's Impact Whey as one of its top picks.

The nofollow link comes in the form of a clickable product image that takes you to the brand's product page.

![HTML code of the "Myprotein" image in the article, shown using the inspect tool with the nofollow attribute highlighted](https://static.semrush.com/blog/uploads/media/b6/3e/b63e1be3cb7516409b7c074520a33a16/548bb78ef2b731c865e1c8c77ca4f31f/AD_4nXcf2s1kx-KGj0mZH6uxlRWhhTYeBBTMFRb3Y4A4Ch7WxaUua_puiTyWYUYt4y3IV4zCSQsXSxmw3Mjm6R7-0EjtmdHyjpUj0EnCFaFIGWeC8G3UFu30-sWab3_TPirydqTf_Uf0bYBZx80pMtrGyaBEgnBj.jpeg)

Nofollow links are unlikely to directly impact your search engine rankings. But they can increase website traffic. As more people discover your content, you may see higher engagement and revenue.

With that in mind, use Semrush's Backlinks to see who's linking to your competitors. Some websites may agree to link to your pages, even if they'll add the nofollow tag.

### Don’t Use an Attribute for Content You Vouch For

Dofollow links (often simply called “follow” links) are hyperlinks without any attributes. By using them, you tell Google that you trust the linked page.

Here's an example of a follow link pointing from another website to yours:

`<a href="https://yourwebsite.com/">Link text</a>`

These types of links pass on authority, or “link juice,” to the pages they point to. Therefore, they can boost your website’s search engine results.

Let's imagine you quote some industry experts in one of your posts. Since you trust their information, it's OK to add follow links to their pages.

Similarly, you can include follow links to peer-reviewed journals, unbiased reviews, government agencies, or other trustworthy sources.

Find follow links with Semrush’s [Backlinks](https://www.semrush.com/analytics/backlinks/). Knowing how many links you (or your competitors) have can be useful for PR campaigns, competitor research, or brand monitoring.

First, enter the domain name you want to analyze. After that, click the "**Backlinks**" tab.

!["Backlinks" tab of the Backlinks tool with "paulaschoice.com" website used as an example](https://static.semrush.com/blog/uploads/media/1d/fe/1dfe0fd0c5f8006c4faa696445466c55/75b88d21e4c49b0f50d6608154d798e3/AD_4nXe5GtGBsSxzuGxzkvUHqudYaq3t7XWSkmOnI1aHRyOEpVD5XcDg4XnNVipHUb5NBm-JFUjd5POS892gm8QECIUMpNTdJOqkFIBEEwAgrQ9--bg3CkFU7mFbBbCVTBhS32aBDLyM9yw-7stVe-KZZjCUuExR.jpeg)

Next, scroll down to the “**Backlinks**” section and select "**Follow**" from the filtering menu. Click the "**Active**" tab, too.

!["Backlinks" section of the Backlinks tool with "Active" and "Follow" filters highlighted](https://static.semrush.com/blog/uploads/media/c0/63/c0632c87d07acaf79677712655deb0b9/0cdd2fcdf71a942b08772ef91987be51/AD_4nXfuC5H6CIBongPz9_qxj4943_LR9rp0kK8LR7Wg9sn6porR5ZBblCvWPAYmOxxg7FBaelNXBPg8mP9da970KOR8fyCBkkbCfqmuVCd18CujzCZt_tWxBn8vtwGrmbXtuTv_Cpcxr2CYcAI2I7d-zpO1Nt4.jpeg)

Then, check the follow links pointing to that domain.

For instance, skincare brand Paula's Choice has about 1.8 million follow links from USA Today, The New York Times, Healthline, and other sources.

Click on the arrow symbol next to a link to open the source of the backlink.

![Several dofollow links shown as an example with the arrow symbol highlighted in Backlinks tool](https://static.semrush.com/blog/uploads/media/1f/8e/1f8e29471239742154282445691d612b/014e8ac364eb401a6892bbcf2544a18f/AD_4nXer4Q5b_YUKfIFG9mkaGRTfZ8x8T1R7AiJUQKTpnnPKVCEP0ZKJaRjw02sSyKXwPGWvIiyF5cPx4-D84IKtRjeviAUpM1QgJEdlr5NkZKgR9co5pGBrCYGdGGVy_iXChtvzVFf9j1aa6GuiYn8uFxZPIJuZ.jpeg)

Clicking the arrow symbol in the image above will open a [Northwestern Medicine article](https://www.nm.org/healthbeat/healthy-tips/do-you-really-need-a-skin-care-routine) about skincare. With a link to a blog post by Paula’s Choice.

![Northwestern Medicine article with the dofollow link to "Paula's Choice" highlighted](https://static.semrush.com/blog/uploads/media/11/ff/11ffa6b93db5a0d9bd11b7ca687c8058/1cfce22d88324dc0fe3fb1b4e95a4e3b/AD_4nXcIK8Mpw6-cb89dWLBD0xLzMGDvbrGpv3GqJ5lK8w0FXYV62fH6KWJxEaVxN0RovpgcZtg89uPe6WnfFdHMpXQaBKsrbwGdLxyFq3JvIkNtZOewkzCykfl2CqOWTDULSzAF8vk3rvMTkifc-50Q1AiRcc4.jpeg)

Having a mix of follow and nofollow links to your site creates a natural backlink profile. As opposed to a spammy one.

### Use Multiple Attributes to Further Explain Links on Your Site

As [Google](https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify) points out, it's fine to use multiple rel values in some situations.

For example, some search engines don't support the rel="ugc" and rel="sponsored" tags. In such cases, you can combine either of these attributes with the nofollow attribute. Like this:

`<a href="https://yourwebsite.com/" rel="nofollow sponsored">Link text</a>`

## How to Check for Issues with Your Outbound Links

Use Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool to detect link issues that can affect your SEO strategy. Addressing these problems may improve your chances of ranking in search results. And prevent penalties.

To get started, open the Site Audit tool.

Enter your domain name in the designated field, and click “**Start Audit**.”

![Site Audit tool with "yourdomain.com" in the text field and the "Start Audit" button highlighted](https://static.semrush.com/blog/uploads/media/d5/6f/d56f0df9b65ba617afce5486d5105ebb/0275e5271a336c5aa0116c7a1c3c774f/AD_4nXc328fw2DakiEkD18S5qJnEdHWkP6S3XaK1U_0SXJEku93zDSwZkOigAfQcbsSbAwtgCKd_ZGwZ9wGxOu53-kkA0FlngJSOZSyGI9X1mNbZJ2D_yw4J403qs_tOJevq7aGGttqLO5whWb_aCOoXfP-rBvKK.jpeg)

Once you have configured the tool, it will audit your site and generate a report:

!["Overview" tab of the Site Audit tool showing all the widgets](https://static.semrush.com/blog/uploads/media/f6/39/f63966e74151e36598c8bb0933165910/6a194ae961519cc1a9d28a9823ae4451/AD_4nXfoAFP9PdtZAyubJs9i7yPCQZxNm4bFdZ5faLScRbMfgE3cLCkSlbrneIaglemRgIL4yr4fHc0arA1F_W0HlVabRU9bXIz--EkAIvrh-OMywNxtLcQZAp2ZwtTUsA-FnAcPGt6lOHHvRIn1Pruzu0LVAD3O.jpeg)

Click “**Issues**” next to the “Overview” tab to check for problems with your external links. These fall into three categories:

- **Errors**: High-severity issues you should address immediately
- **Warnings**: Medium-severity issues that require your attention
- **Notices**: Potential problems to be aware of

!["Issues" tab of the Site Audit tool with "Errors", "Warnings" and "Notices" filters highlighted](https://static.semrush.com/blog/uploads/media/30/15/30151946a1505f099a435a165dabc315/6299985bfb2b7348e0ef24831c02e82a/AD_4nXfJswV3TW-PKaFmk-uc8pDs2RFEXv08qKLOqeVaA4W349BnxXd6PMSs-gW1oES1xVoKKeCFkWHJY9QUhzl0oke06B2IyFW8zsfibNPY68rWGBt5l5cJlu7_jd4RWssGfOyq58ZM_8R1Xm2wrRtycJdtKq-q.jpeg)

Next, enter “external links” in the search box. Site Audit will display potential issues related to your outbound links. Like [broken external links](https://www.semrush.com/blog/broken-link/) (i.e., hyperlinks that point to a non-existent webpage or resource).

This issue will appear under "Warnings."

!["Issues" tab of the Site Audit tool with "external links" in the search bar and "1 external link is broken" highlighted](https://static.semrush.com/blog/uploads/media/d1/0e/d10e56ae35d9ee3b9f81d4d97d822307/2a26793854e5cb13dc78d8b8dda3fa4c/AD_4nXdaI0FAnULEsPtGHS1cTf2IEtGkwSdEMpzFSZ4mmY1oBn3LaJV1IGBVnDx2Q0dbEz9YKj6M9v4djfcXx6ixlQuLrKs-IS2U0VP_HW02ZNOQz7E9_6KW6tZ18IpOctazindzK4xBz4m8qY09VnQ6ZOKO2Kk.jpeg)

To find specific links, click on the error to see your list of broken links. And where they appear on your website or blog.

!["1 external link is broken" page of the Site Audit tool with the "Link URL" column highlighted](https://static.semrush.com/blog/uploads/media/a1/22/a12215ff75c638d0980e4ebcdced27dd/7eaebed2b89ac1333475f13ab91316c8/AD_4nXcruAeE-lx0zO3XlolqbiSjwrAGzOBMXlZItp--vGW6KIna0zJuc-rVSEfzZEd6bFp77fXhTett8WHgA1c8PsroG39L3hcqS3qESzdJsVHMhpEruUoI-5nY0n4ZQQYbNLiQpr2cb_uGg6gW7g4fOKZ7_3XU.jpeg)

Then, click “**Why and how to fix it**” to learn more about the error. And how you can resolve it.

!["1 external link is broken" page of the Site Audit tool with the "Why and how to fix it" button highlighted](https://static.semrush.com/blog/uploads/media/cd/e9/cde9c2a48bbf001005c014178e9051d6/03f70ee4490a53ff6056ee627d6dcb81/AD_4nXeIM2SfGuwshLCjhHP0wBeCFxrdfZURuLLE6Dm8sgUXytfqJib14PnIc7PJXl7PywKIH9Z_qTFagLgjo1bhWBcXAdTqH_PEaoDNsjVDEk9_6UtTj-D0Y4n-3to0ghVBJl92HwtfRXh9t8c-qQEHqL2W0qAf.jpeg)

Remove or redirect broken links, as they can affect your site’s user experience.

Semrush’s Site Audit can also detect external links with the nofollow attribute. This potential issue will appear under "Notices."

!["Issues" tab of the Site Audit tool with "7 outgoing external links contain nofollow attributes" notice highlighted](https://static.semrush.com/blog/uploads/media/4c/16/4c169b9a36af69eef33e427904aac5e9/1170e37bdf2be4e70365b9d43da10a78/AD_4nXfWXO2jtIpYK0SU12eLj0K1GpHhKIdXn0ZGWTemSxI-Tb9N_4dMTKEu2VKV9vQzvPzldhtEp7Eav_FK4Rdf2jkl0p6-nE55-l4mzoixAZAHPpt4vvWKAzQ9-Zr9jNKxWlGEcWXI_Q15uNBXPhABYQv2SS0X.jpeg)

Click on “**# outgoing external links**” to view the links in question.

![Site Audit tool "7 outgoing external links contain nofollow attributes" page with the "Link URL" column highlighted](https://static.semrush.com/blog/uploads/media/cf/6a/cf6a59ff47bfafeb4da99391fa1c2d0e/7e519a542d9fe08699ec31d7d1edede1/AD_4nXewR428VI1bhWKyI9mT0ipxssUqkEK2dvjAfdN57ERsyyaOlwxJUr1BmUm2UXQthl9P5Nas6zbcw-2yN0Zl0RrhiwI4EqfCp0FV95Q2kumtrMJ79DJHEEiysWQk9mS4rdrlMKLvC8vTJPPQTZjWE35RNyBz.jpeg)

In the above example, some of the links under "Link URL" look spammy. Don't click on them. Instead, click the arrow sign next to them to open the webpages where those links appear.

!["Page URL" and "Link URL" columns with the arrow sign in the first column highlighted in Site Audit tool](https://static.semrush.com/blog/uploads/media/0e/db/0edbb5369bc2e215620bee6ce7e628f8/c308ca19b7e1594225bedc584d05820c/AD_4nXcR-KFtjTLWFMtVC7BIKFI37RdKSvL2tO2jzLrq3pxYvqvaGyb7d5Smg--cKB5t0DteWfcH_OFkwNIFjBrdh1oXBHD4jJL-kb3TBv-cFm0P4d2N8Gh3FKGtSJ0eLBmSzPDrqnumJTr7KwnlLsNUmf17FAta.jpeg)

For instance, "http://a2z.linksind.net/?S\*32d19" is a UGC link in an article comment.

![User comment on a website with the username highlighted containing a spammy link](https://static.semrush.com/blog/uploads/media/7d/6b/7d6b203d7ed9024421ad5eecd93f95f4/7f373405fb2f044b2c3f867a00c3548c/AD_4nXcL5MWkglboZXjQIUXDTNQdZuaX2TqJQXXRBIGewosKRRd5pfK_UtusMID1tUuWK2wVHCNKe271X-cIXbcP6zH5376GH05IAtHhss6jeBT0Xcg9EOUEcUxdPU1BU_AbknAvbrFWRPB_9ChwacrIJ8iw75M6.jpeg)

You can either delete the comment (since it provides no value) or add the UGC tag to it. Alternatively, use the nofollow and UGC tags together.

If a link doesn’t look spammy, simply remove the nofollow tag. Or use a different rel attribute, depending on the link type.

![Several outgoing external links, one highlighted and annotated with the text "Non-spammy link"](https://static.semrush.com/blog/uploads/media/0c/6f/0c6fb8c0821b6f128439df90d44f2d8d/4411e9208161ab8183cc7f5dd7a72586/AD_4nXdRfDuyhy_uwxHQTD_q0zBBV25zuQWO33x05t_chqUk_kAN71-bsZGA0YvAQ-mW9BSOtxrUDQNT_977OKlm6Oi8234NhweL145RaSl2P3Rt6lda9EsrNylbs9HvVfJd9xQxLZcr4ANdn0euGjLo4E27G485.jpeg)

***Further reading****:* [*11 Common Internal Linking Mistakes & How to Fix Them*](https://www.semrush.com/blog/internal-linking-mistakes/)

## Elevate Your Backlink Strategy with Semrush

UGC links and other link attributes may have little impact on your site’s rankings. But they are definitely useful.

By using the rel="ugc" attribute, you can help Google combat comment spam and understand the nature of a link.

Go one step further and use Semrush's [Backlinks](https://www.semrush.com/analytics/backlinks/) to develop a UGC SEO strategy.

With our tool, you can find UGC links pointing to your competitors' sites. Let's say one of them has several UGC links from a particular forum.

Join that forum to introduce your brand and engage in meaningful conversations. This can increase the number of UGC links to your site, which may result in higher traffic.

Backlinks can also help you identify your competitors’ nofollow and sponsored links. Leverage this data to boost your backlink profile and get more eyes on your content.
