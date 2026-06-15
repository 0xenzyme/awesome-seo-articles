---
title: "What Is Review Schema? & How to Implement It"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "review-schema"
url: "https://www.semrush.com/blog/review-schema/"
canonical: "https://www.semrush.com/blog/review-schema/"
author: "Zach Paruch, Sydney Go"
published: "2024-01-19T16:19:00+00:00"
updated: "2025-02-27T11:24:00+00:00"
categories:
  - "General SEO"
freshness_reasons: []
schema_genre: "General SEO"
fetched_at: "2026-06-12T18:56:20+00:00"
status_code: 200
html_hash: "7b8619d238c82ce76b7f0b53c97a1ffe2b3e447d8714fd2516a8954354c2fbe8"
clean_word_count: 2081
clean_char_count: 17533
---
# What Is Review Schema? & How to Implement It

## What Is Review Schema Markup?

Review schema is a type of structured data markup that helps search engines interpret and display review information—such as star ratings, reviewer details, and review summaries—in search results.

Below is an example of review schema:

`<script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Review",
        "author": {
            "@type": "Person",
            "name": "melissawho"
        },
        "itemReviewed": {
            "@type": "LocalBusiness",
            "name": "Tokyo Tower"
        },
        "reviewRating": {
            "@type": "Rating",
            "ratingValue": 4
        }
</script>`

And here is how Google can display your review data as a review snippet in search results:

![Google search results for 'tokyo tower review' with review snippet highlighted for Tripadvisor result.](https://static.semrush.com/blog/uploads/media/66/73/66738109f457c306c41fc7b87f7ae073/39668a3cdf5d48da10f3aa28f14b0d06/AD_4nXdX2h7W7EQttV6JpXglT_xA6rMLztHu6jYGbX4iICWSwlsVccnk7YmQgf5H81LRgXyohe4B7AZk4UGPqt2Y-mMsV3ug-Ob_tcFnYy2dZ4VmNkGV8bmyeFacnCaTYE4UyqI0a8WbZA.png)

You can add review schema to product pages, recipe pages, movies pages, and more.

## Why Review Schema Is Important

Review schema helps search engines understand review data on your page, so they can display that data as rich snippets in search results.

Like this:

![Google search results with aggregated ratings highlighted in rich snippet.](https://static.semrush.com/blog/uploads/media/5e/56/5e5620a66fb827b6af0e507334fa63b4/0eaa29c235552d6623c0e6e21766a7f7/AD_4nXe_n5qH7cS7Z_8UhssVkKOrshjCyX4EGHgTzUNXf-3YpLV1SphxLPfm6Wvw5HlXWExiCMGLZL2U16NnAv5p56o_UC0FMMlQlBw6mlgwC9p7snOKDeJr1FSpXL3ejcTNjZOIQyNiLQ.png)

A review snippet can in search results can:

- **Increase click-through rates**: Searchers may be more likely to click on your page (e.g., a product page or a recipe) if they can see a star ranking right on the results page
- **Help your listing stand out**: The results page contains many blue links that look alike. A review snippet—which contains a yellow star rating—can differentiate it from similar listings
- **Provide social proof**: A higher rating can encourage more visitors to click

## Types of Review Schema

There are two main types of review schema: **simple reviews**, which are individual opinions, and **aggregate ratings**, which summarize the collective opinions of multiple users.

Let’s explore each type of [schema markup](https://www.semrush.com/blog/schema-markup/) in more detail:

### Simple Review Schema

Simple review schema tells search engines that the page contains one review from a single source.

This schema provides details such as the reviewer’s name, review text, rating, and the item reviewed.

For example, this review snippet is generated from a simple review schema. And it shows that Joseph Tomastik gave the movie “Everything Everywhere All at Once” a 4.5-star rating.

![Simple review rich snippet highlighted for search result.](https://static.semrush.com/blog/uploads/media/a4/c4/a4c41eecf5c49117f92eb2b8e6f4d884/0779460346d057f8c6ab3ca216ece24b/AD_4nXd9d-BGxuFBGbvFtYelKjqawVUSsmjhNNw8dJPEfX8u-7wzUuPSa2vW4STeOc7527rHyI1sv8R7Sb9S-qzxUI-ePaZm_NF8d2qpTgJLgwz9zJsYkcHy5Q3Qy8hGs1hmqAwl-3J2Vw.png)

Simple review schema markup must include the following information (called properties):

|  |  |
| --- | --- |
| **Property** | **Definition** |
| author | The review’s author (Person or [Organization](https://www.semrush.com/blog/schema-markup-for-company-corporations/)) |
| itemReviewed | The item’s type, such as Book, Course, or Product |
| itemReviewed.name | The name of the reviewed item |
| reviewRating | A property that stores the review’s rating |
| reviewRating.ratingValue | The rating (number, fraction, or percentage) |

Optional but recommended properties include:

- **datePublished**: The review’s publication date, using the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format
- **reviewRating.bestRating**: The highest rating, which is five by default
- **reviewRating.worstRating**: The lowest rating, which is zero by default

### Aggregate Ratings Schema

Aggregate ratings schema summarizes multiple user reviews into an average rating about the reviewed item.

For example, this review snippet—generated from aggregate ratings schema—shows the average rating for the movie “Everything Everywhere All at Once” based on multiple user reviews:

![Aggregate ratings rich snippet highlighted for search result.](https://static.semrush.com/blog/uploads/media/47/03/47036e88114fc484cdb5e9e359aa3520/44fd6e42e48ee2b4ae2bc393d1ac8de4/AD_4nXf-GmhnC7EbnKmihy33Ed_pPFvyhDAotsONxIxW7jpnqspDRl9gBQqeRAG-tCK6S2VnayOg7UnlLjYo9bNPCkuFyW2W1EvZc2pz053f6xEcn645QYBlDmFYhRTW1xmVwi3hCV-A6A.png)

Aggregate review schema markup must contain these properties:

|  |  |
| --- | --- |
| **Property** | **Definition** |
| itemReviewed | The item type, such as Book, Course, or Product |
| itemReviewed.name | The name of the reviewed item |
| ratingCount | The total number of ratings. Providing this property is mandatory if “reviewCount” is omitted. |
| reviewCount | The total number of reviewers. Providing this property is mandatory if “ratingCount” is omitted. |
| ratingValue | The average rating (number, fraction, or percentage) |

Optional but recommended properties include:

- **reviewRating.bestRating**: The highest rating, which is five by default
- **reviewRating.worstRating**: The lowest rating, which is zero by default

## How to Implement, Test, & Monitor Review Schema

### 1. Generate Your Review Schema

Use a tool like the [Schema Builder for Structured Data](https://chromewebstore.google.com/detail/schema-builder-for-struct/klohjdodjjeocpbpadmkcndjoadijgjg) Chrome browser extension to create your schema markup.

To start, open the page where you want to create review schema. Then, open the browser extension.

Click “**Review**” under “All Supported Schemas (36).”

![Schema Builder sidebar with arrow pointing to Review option under All Support Schemas](https://static.semrush.com/blog/uploads/media/28/dd/28dd14be03022a6b9bda5b537d8ee97f/2377dd41a8f1cf9fdc8c6d3f9db94f1f/AD_4nXcEb-CUxK93GVVgKNwGKxnxLV3arRBLKm3d8XbK5fgDbq8SQ__qZLmkUcXOT40gqKQfVB_KoxjNs4tEp-Eg4FmZf-dIM66cYfqudkGGlhR_X9jn4dD4dkSj3asoEMCqzVvkCAWGog.png)

Use the tool to mark important data on your page.

For example, select the “**Author**” property.

Then click on the arrow button to select the block on your page with the review author’s name.

![Arrow button under Author property and Author name on web page highlighted and annotated.](https://static.semrush.com/blog/uploads/media/91/c3/91c30342fc6cf287d992337d6b99ac3b/64d96d33321a77413203a568b32f9e3a/AD_4nXd_BIb0zEZcdk0eyN0bdgOLeNAb3p8Iy1hFnbLSQNWT4m5pN0V4dqBWwmgotr6-j9abWDIlc3MranxijcxC-1ZoNxXdGOG8Aqml_7-6rqerqOr1xXgMnUzglDFIqds4CmlNknMmqw.jpeg)

After you’re done marking up your page, click “**View Markup**.” And copy the generated code.

### 2. Nest Simple Reviews and Aggregate Ratings

If the reviewed item is also relevant (for example, a product you sell), you can **nest your review schema** inside the main schema.

In this case, nesting means placing your review schema markup within another structured data item’s schema markup.

To do that, generate schema for the main page using the Schema Builder for Structured Data Chrome browser extension.

Then, nest the generated review schema within the main page’s schema markup.

Like this:

`<script type="application/ld+json">
    {
      "@context": "https://schema.org/",
      "@type": "Product",
            "image": "https://www.example.com/waffle-iron.jpg",
            "name": "Waffle Iron",
            "review": {
            "@type": "Review",
            "reviewRating": {
                  "@type": "Rating",
                  "ratingValue": 4,
                  "bestRating": 5,
                  "worstRating": 0
                  },
            "author": {
                  "@type": "Person",
                  "name": "Waffle Expert"
                  },
            }
 </script>`

This markup indicates the item’s type as a product and uses the “review” property to add the review’s details inside the product schema markup.

### 3. Add the Review Schema to Your Website

Copy your generated review schema and add it to the <head> section of the relevant pages.

If you prefer not to add schema manually **use a plugin**. For example, you can use the [Schema Pro](https://wpschema.com/) plugin if you have a WordPress website.

### 4. Test Your Review Schema

**Schema.org’s** [**Schema Markup validator**](https://validator.schema.org/) checks your schema markup for errors.

To test your review schema, launch the tool and switch to the “**Code snippet**” tab. Input your review schema.

Then, click “**Run test**.”

![Schema.org code snippet validator popup with Code Snippet tab highlighted, code snippet pasted in field, and arrow to Run test button.](https://static.semrush.com/blog/uploads/media/47/84/4784f0cdcb3a5de2fcd4cf1b0999e864/7f39648435cc9868e87a88fd8234126f/AD_4nXcmaL83JTDvFvgDyjY8KFRK8hYc_ETZ72mlnE0PpvmmSwuvrkQdBo4VKpYNGbfBCRk4_9JNozscZGk7kQjwMxSW7yz6ODYhrojh2NfXI2OKaXRwAwRMSbmiRkleilgu5puUFqhl.png)

The tool will display any structured data errors.

![Schema.org test results with structured data errors highlighted.](https://static.semrush.com/blog/uploads/media/23/f0/23f0d2a05b65fbd96bacf70b7eefb0e6/3ab3744f7681a21ae665662c32840ef6/AD_4nXd3u8mcVX7ztFX8foILcyZM2KSk2xzb2qSgEb_spTiygUiaChyXISAMxYDJX1zrXpmXh5tLxjnanGje7H18J1rwCrprV2OdUdS8NiNfczt4BxE1pczx-UkEwwE6Otk0qdJG12JV.png)

**Google’s** [**Rich Results Test**](https://search.google.com/test/rich-results) **tool** helps you test whether Google’s crawlers can detect and understand your schema markup.

It also shows you what the markup can look like on search results pages.

Open the tool and click “**Code**.”

Paste your review schema. Choose a device type. Then, click “**Test code**.”

![Rich Results Test page with Code tab selected, code snippet pasted, and arrow pointing to Test Code button](https://static.semrush.com/blog/uploads/media/6c/a0/6ca028db18ff3ee4a5389fb18cbac3f8/99804e0f6abb2d620a1ebdf6f517ec13/AD_4nXdZ7xaHaWIozoGx5q1itKpz9itEzJhwlpHAMyv1oINR6kuSVJS5BIf_BJIPFd8FRorzuK7qRHNwGHGTfNeMM6i4zr8WiUXfn7EcCWt6lQ3lF4B_aL2EEbMjAPPRvz8V5e-KXvCe0w.png)

The tool then highlights the valid and invalid structured data items.

![Rich Results Test results with Missing field error highlighted](https://static.semrush.com/blog/uploads/media/3e/6e/3e6ecb698246873c2e9ba510e17b093a/170e60385cd88de9e6db8afcd694f725/AD_4nXdD2yFAeHhrsMsM9sIHuF4WsvGE6c92qhYMfTDcu4DFvQ3AfHZ9bUtGhJY3VNyArlfbmKA9GKGDr8ajXg3lpyo9QCOTDcgWEYJ14pR2a6LboeudXe2au7qZQDe6uB_pypUQpUQ0VA.png)

Click “**Preview results**” to preview your schema markup on Google SERPs:

![Rich Results Test Results Preview for example seafood restaurant](https://static.semrush.com/blog/uploads/media/1c/68/1c68082968a8a2f6307675f7816a4417/af52bf00ae24821bc376671ee53bdb66/AD_4nXcpTo_TPOjM4Nuq3kjyzb1-c93FJQ6ANECT_HqO-yWzH1yHl3MMztxMtKDyJLCHq_qasZsDx45ga_2HOrX79vBkRg3zVUlvG_5PXx6HjDwrxSmChtEPNZx_J0sJMDNd3uR6NlX5.png)

### 5. Measure the Impact of Review Schema

Measure the impact of your review schema by tracking how many of your pages appear in search results as review snippets, and how those review snippets perform.

Semrush’s [Organic Rankings](https://www.semrush.com/analytics/organic/) tool makes this easy.

Open the tool and search for your domain.

Then, scroll down to “SERP Features.” Click “**Reviews**” under “Linking to domain.”

![Semrush Organic Rankings tool Overview report SERP features section with Reviews option highlighted](https://static.semrush.com/blog/uploads/media/2e/4e/2e4ec3df3540e40c3c0b57cf34eea6d5/f632ffd27300c2e31ac51a17c055bc95/AD_4nXe9Q_v2PmxToNfT44aXN_FsImZ9Q3TMNDsJWDeU24NV7bbQbcRMA8WlTXpSCDzl4YwD-281EvdSMd-O9nIPmrBAP61r5K8tHx2TyONcUT6ddd7JiD2Mzw4DfnfVbMaKhYbfR_8f1w.png)

This will take you to a dashboard with keywords your site displays review snippets for.

![Positions tab open, table showing Organic Search Positions table filtered for SERP features with Keyword and Position columns highlighted](https://static.semrush.com/blog/uploads/media/f1/a8/f1a852fef16187b0e1a53c5fe350923e/7e5be34ee37eb32345f7e7acf154beb1/AD_4nXeWpaHKm3lNs9fA2eAO_R8ScqDubnDbp5gmi6tt4L1Rlo_MLeS1nTNKgM9_dK-7IKevs3nvqoBDCKAELSe0cDNZOCnSZodlU7fnCFA7TpWvJKcorQb5xjbFEL36Y1MkyEukzu7tpA.png)

Track the number of keywords. If it isn’t growing as you add review schema to more pages, check whether you’ve:

- Implemented your review schema correctly
- Adopted [SEO best practices](https://www.semrush.com/blog/seo-best-practices/) to help your pages rank higher

Then, use [Google Search Console](https://www.semrush.com/blog/google-search-console/) (GSC) to track the performance of your pages with review schema and other rich results.

[Connect your site to GSC](https://www.semrush.com/blog/connect-google-search-console-analytics/) if you haven’t already. And click “**Review snippets**” under the “Enhancements” drop-down menu.

![Google Search Console dashboard with Review snippets option highlighted](https://static.semrush.com/blog/uploads/media/7c/60/7c6081f073cfc46a7deaf1a6fde11478/db84ee21b233901acb68984388a2d7a1/AD_4nXfaKxnsL-1KvZjIWHzTgvCDXlZdEK-nTzi4mtBhUDRamzz7xVZNcCkGmhb1NRdhJopzmS_un9ydjT0jJAwcdtCGTF_nSCoMR8gPDdpMlVx0s-KF4sN1MT7iPKBEK7A1ivYF9BzF_Q.png)

The “Review snippets” report will show the number of valid and invalid review structured data items Google has detected on your site. And the number of review snippet impressions generated.

![Review snippets report showing graph of valid and invalid review snippets.](https://static.semrush.com/blog/uploads/media/3f/20/3f209f4908d06902f08171a3ac5fb425/4d0c473ca2ebebc8941a4b66a30cc489/AD_4nXdmfKW-hhTSGAH2zkHMeXCEprhArb-P9pRQVIQmq1Uppk6BkknTgt1QCEZFq4uvYhtFRX1doub604TZmE7xbTdrCuBB52hel0Ur6qO4mMGYr2zM1QPxnpQQhdzG5Ri-L6zH6K694w.png)

For a more detailed look at the performance of pages with review schema, click “**Search results**” under “Performance.”

![Google Search Console dashboard with Search results menu option highlighted](https://static.semrush.com/blog/uploads/media/0f/83/0f833b73a1d3285a67d70ffb763c0de5/857ed23560d5c4a903d1b3d6d1c6fc61/AD_4nXfWl5r9hQp5CEEUsPGF-krNYeWNM8ltitV6jPp4QdVsQJEt5-RHwC7ydtCHf1wc4DKBaXy5S7kEs0o-zs9z05gO88hf08EjgvGMUJwTyJ0s3DpmZmXAg99D_BUGLl46NYpkKkHQHQ.png)

Add a search appearance filter by clicking the “**+ Add filter**” button at the top, followed by “**Search appearance**.”

![Performance on Search results page with Add filter button clicked and arrow pointing to Search appearance filter option](https://static.semrush.com/blog/uploads/media/1a/90/1a9057f3f6c5e5fd4941e260637fcd94/22cc1af2ecf9a1875b7544c973b39cfd/AD_4nXfgIG7LbQ8-nPwrzK0NM8NsB0hZe36URSGvYNPwPKO2gM7JkV5UHc0tsKc9H4HrzeIk21CESxoDwHVBzc3BNiDA4gVZvb3_eb62uMv5FxAKyOYGJx7xGO1po8tA5iwAh4uT_6R-Gw.png)

A box will appear where you can select the rich snippets to filter results for. If you have pages showing review snippets, click the “**Review snippet**” option that appears here, and then click “**Apply**.”

![Search appearance filter popup with Review snippet radio button selected and highlighted and arrow pointing to Apply button](https://static.semrush.com/blog/uploads/media/a6/3e/a63ecac7c02e2ff48e9e31a4ff7c7aac/646575375f50d6f4366df59e4f32cc1a/AD_4nXe05K2uv_XBkylknJFoPeff08DaiOGXwzEj4Z2wl_POnqnMEVxUD8S8ytdiSj_-SvxiCwkv0kO5-1BUwSIkUuL0UJHDdUKkpvlXaNWVp63lrpD5PHQ1h24Xp1cNB1SzmGOl49OidA.png)

You’ll see a chart of clicks and impressions for all queries—also known as keywords—that led to users seeing your review snippets on the SERPs.

![Filtered chart of clicks and impressions for all keywords showing review snippets on SERPs](https://static.semrush.com/blog/uploads/media/b3/d8/b3d85a18ced96803cd1de6a8ed599dc9/2ff2561664d30caea6d112d1e6d7be7f/AD_4nXfUc9jDdzzy5vDnsiT5xWoc1v-VJf-gAsGgYbEp7jn0sGJZqHzSNHIB7loXMILQDqhCAlBWuwdJYcmaz0pSxcngT0MEzTcvPfQK-4NOTVOdxdMSqhSLKu3F4JKHasgQDtDVuARDRA.png)

Then, navigate to the “**Pages**” report to see the pages with review snippets, plus each page’s clicks and impressions.

## Review Schema Best Practices

- Make reviews and ratings clear on the page for users
- Ensure reviews are about single item, not a category of items
- Provide aggregate ratings when displaying multiple reviews
- Use the correct item type in the “itemReviewed” property (if the review schema isn’t nested) or the item’s main schema markup (if the review schema is nested)
- Do not aggregate reviews and ratings from other sites

## Monitor Your Schema Markup Implementation at Scale

Schema requirements can change, so monitor your implementation regularly.

Tools like Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) can check your entire site for schema errors.

After running the tool, you’ll get a report that shows valid and invalid structured data items.

![Semrush Site Audit tool Markup report dashboard.](https://static.semrush.com/blog/uploads/media/85/7e/857e1d8a72a7dabc89e731f1805179ce/8ed09d611a0873bdf2a0cc0659fa07da/AD_4nXfVnwsXC4SK_69h-aAp0MFD4k5ErhmYO_y66gl6zXRIPMOr2XAZEm7cJY0akSNDZMhKjyMRfst6evS8uRjtgGpzZW0_RzQ4tTVLvQ38sHVrOD6_pxSUF_Ukp-V_0f-NPfFsd6np.png)

Schedule regular [technical SEO audits](https://www.semrush.com/blog/technical-seo-audit/) to detect new issues quickly.
