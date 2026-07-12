---
title: "How to Connect Google Search Console to Google Analytics 4"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "connect-google-search-console-analytics"
url: "https://www.semrush.com/blog/connect-google-search-console-analytics/"
canonical: "https://www.semrush.com/blog/connect-google-search-console-analytics/"
author: "Zack Duncan"
published: "2020-08-20T13:00:00+00:00"
updated: "2024-02-15T10:52:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2024_watch"
  - "time_sensitive_title"
schema_genre: "Analytics"
fetched_at: "2026-06-12T14:32:46+00:00"
status_code: 200
html_hash: "705c6cc19d000070093bc1e734580ca77454d0404b19af66455a0e92c9afa2be"
clean_word_count: 3063
clean_char_count: 23868
---
# How to Connect Google Search Console to Google Analytics 4

You can connect Google Search Console to Google Analytics 4 (GA4) to get organic search data in your GA4 property.

The integration expands the level of detail you can get from Google Analytics. Once the two platforms are connected, you’ll get performance and ranking data for specific search queries and landing pages. All in one place.

In this guide, you’ll learn how to connect the two platforms. And how to get the most out of the integrated reports.

## Why Should You Connect Search Console to Google Analytics?

Google Search Console (GSC) helps you measure [organic search performance](https://www.semrush.com/blog/organic-traffic/) in Google. So you can uncover SEO opportunities for your site.

You can connect GSC to Google Analytics to get that organic search performance data within your GA4 property. Where you can use it for common SEO tasks like:

- Sharing detailed reports with stakeholders
- Generating new content ideas
- Prioritizing pages that need a content update

### The Data You Get When You Connect Search Console to Google Analytics

The “Search results” report in GSC displays data for four key performance metrics:

1. **Total clicks**: The number of clicks coming to your site from Google organic search
2. **Total impressions**: The number of times your pages appeared in Google search results
3. **Average CTR**: The number of clicks divided by the number of impressions (multiplied by 100 to give a percentage)
4. **Average position**: The average ranking of where your search results appeared on Google (across all impressions)

![Performance on Search results metrics and graph in GSC](https://static.semrush.com/blog/uploads/media/6d/72/6d72088245822ee64e68ada5ed72a88f/218c3d4065fb5182d72c299688891507/r0n9mr6YoUsosc7KU-f-1SHzIWNu9fLjOTIgZJatwmbBj134-AXTF_e2F9QHKVng23uRL0amK_8WpR8HmEsvf7NRCzFhWjm2L4oPnuEWwKfxiaPkCD9aE2sy_rNf2j_GYrbNB3Uc_22k.png)

By default, the “Search results” report will show a graph of **total clicks** and **total impressions**. You can visualize different metrics by clicking into any of the four metrics.

For example, here’s what you’ll see when you turn off clicks and impressions and turn on **average position**:

![Performance on Search results graph in GSC, showing the average position data](https://static.semrush.com/blog/uploads/media/ca/28/ca28ce87fe4846f23a831482ff7623d5/a66f0ebf0e24aeb3d4d31d61691d44dd/GUFWF4UWmBS5KedAno7fFjMoD68j_Vq1g9mLqUST4xKFlr5VG-TWh3_r90WPFFcRktM8BEEw_twHXK6ZiBuBBRkgvkUncjrB7AWTw1HqQ6ECBZfuxVCyeBPiCyD_XoYlN9w-ToscxrQN.png)

These metrics provide an aggregated view of your performance. Search Console provides query-level information on the same four performance metrics.

Queries are the specific search terms visitors typed into Google before finding your site (i.e., keywords). Here is an example showing the top search queries.

!["Queries" section of the Performance on Search results report in GSC](https://static.semrush.com/blog/uploads/media/81/09/8109f06f108e3a6d751e068c92e2e058/1e87c1cc6361a1092e85f31084ed9686/l2YQYK7dy5CJL-4Q8iohFBU7zn_o9hXv7JxQbJRTmRwZvZodI2GXDPL3h3GQb2NNqoiE-5SeQxsA1vJnJhiH8udALKEu69NHZb8TBQeNqTrr6JHlcU1wpjUtQY5UOQaQq2e7KHyC6Lnx.png)

On its own, Google Analytics can’t display this granular, keyword-level data.

### Why Google Analytics Needs Search Console Data

Google Analytics is a free [web analytics](https://www.semrush.com/blog/web-analytics/) tool that can help you understand your website’s performance and the visitors who come to it.

Like where they live, how often they visit, how they arrive, and what they do on the site.

![A dashboard in Google Analytics showing website visitors' information](https://static.semrush.com/blog/uploads/media/6d/c7/6dc7e7e758d8c859cc6963cb8addbc4f/1c80aa052ed277f2093ec3c741d32859/AUmpm1uPCBui18wKkYhsxo25WElV8Bx8zK7DIzvjaEYQH3PxvN62JMnPMhABnSUZwgMtlbrafayxeqgoepuXSQSGnDEM_eIeVdGWM3Q-qFYUsLYZdVhJKy4Spul4Ccktb1m6sOpIIsIa.png)

But without connecting Google Search Console to Google Analytics, you won’t be able to see that all-important query-level data alongside your user behavior metrics.

So let’s find out how to combine the two platforms.

## How to Connect Google Search Console to Google Analytics

You’ll need editor-level access to your Google Analytics 4 property before you begin.

### 1. Verify Your Google Search Console Property

You need to be a verified owner of your Google Search Console property to link it to your GA4 property.

You can verify ownership in various ways depending on the specific way you set it up. These include verifying via HTML tags or by adding a TXT record via your DNS (domain name system) provider.

For a full guide on setting up GSC if you haven’t already, check out our [Google Search Console tutorial](https://www.semrush.com/blog/google-search-console/).

### 2. Go to Google Analytics and Access ‘Search Console Links’

Sign in to [Google Analytics](https://analytics.google.com/) using the same Google account you use for Google Search Console.

From the home screen, click on the gear icon in the bottom left to access the “**Admin**” section.

![Navigating to Google Analytics admin section](https://static.semrush.com/blog/uploads/media/1e/b1/1eb16fca4b076be834e4c96894af5340/a0606d495e3465339d52c211bb9ff9a5/C1dQHrpbqjdSqt9kI9ti9rjCp3PX1XyLJIH8Pr4dsC8914ccPeycL1b0RC9iqYFTPz21HCNqMYf03C8zzHxEuD357PrF_Fn2SP32niGnjFPUP0LLGwArU-yT752pAWYeUyl6W5aW25Lx.png)

Click “**Product links**” under your “Property settings.”

Scroll down and click “**Search Console links**.”

!["Search Console links" section in Google Analytics Admin](https://static.semrush.com/blog/uploads/media/f5/fa/f5fae000d50602a51cd222651873703a/8314b8ef1d88fa1af40458900a40a0da/yBPI5WwRmYG-fm3vwTQrqN0q-39A9PegYjHk320xstuXk4pbxOvlGBtB-ac4wv7AbILImP8_HzLIFFPsPQMyoxE51uHx7D9naHzJ-680Cv7l9RNlwSv0iHdrSRZ32aq2xwWDa736vTL9.png)

### 3. Choose Your Search Console Property to Link

On the “Search Console links” screen, click the “**Link**” button at right-hand side.

You’ll only be able to link a Search Console property to a single GA4 property.

!["Link" button highlighted in the "Search Console links" section](https://static.semrush.com/blog/uploads/media/60/7d/607d5ec5e234c9eeb28db8d9aec6b333/23f744af6b18ef3a46a81a4a7a6a85d0/wsjvbsiJBkDQSf-b3FpWED__PkV3AYhzNYPaYFcnKVSQ1vLUOqtePR2yieJjoDUvZBmRu2bXH4YiGV07oj0uLix5sZcdAbWcW4WCPqARLFAnEg73N2P-Pqr4XCXmYeVd8uw07ANBVHUN.png)

You’ll see a “Link setup” page like the one below.

Click “**Choose accounts**” to see a list of Search Console properties. You will see all properties in which your email address is a verified owner.

!["Link to Search Console properties I manage" option selected under "Link setup" page](https://static.semrush.com/blog/uploads/media/0d/71/0d71eb87225019ade88e01045c59a2bf/0609c64cd5be628defef9a2dc40b6332/W6huCyCH5_7Lrn6Um0r9q-XMP-CGze8Ip7Av-GhnJ1jNTCuaGXVqjVjmXxWVhCHa2oP3xV0O8atzrYHaJS2P5QsJD6JiPZrJZ6zaes7HJtexLr8VoGp-dhZd9hvuBdEon5QS2gSbOMuu.png)

Find your property and select it using the checkbox on the left of the “Property Name.” Then, click “**Confirm**.”

![Select the GSC property you want to connect to Google Analytics](https://static.semrush.com/blog/uploads/media/52/89/528908d333a8f023cb61ce7a51aaeb27/27173bfde046dd97302946f5cf5c97a7/vSq6OCmk9i1Md5WHItA9Q8HiVdKvNPiU-bLJ2_rfO725g5alATs8DwXB1AYJ5JTYXlCTCQfOvCBagIXeMpqvoxhWyat5SiXCXFt2tbwiRNSPyZWCDyZ385Y7SCiRCXuSO0kA7Kf0783r.png)

### 4. Pair Your Search Console Property with Your GA4 Web Stream

Next, you’ll pair your Search Console property with your Google Analytics web data stream.

A data stream is the place from which your Google Analytics data originates. Google Analytics 4 has three types of data streams:

1. **iOS app**
2. **Android app**
3. **Web**

You can only connect Google Search Console to a Google Analytics 4 web stream (i.e., for a website, not an app). Click “**Next**.”

!["Next" button highlighted under the "Link setup" page](https://static.semrush.com/blog/uploads/media/93/3c/933cc3b06e77105243fcd96381cdcde4/2861e53aa393d68ddc9a3e3f9559be1c/SwalMDfdwTtGztDU719DYHd36WSNQwlpycE64kzrQ4deC-88IrxMJp-M4mRcEWmxGVOOcBS6t3JGUoaH7k0VLc4vRQWRaENgeT62ph10rCdtpOmuiCMGPw-ql_3DB2sdOZ9EjXaK_l2j.png)

Then, click “**Select**” to choose your Google Analytics web stream.

!["Select Web Stream" step 2 highlighted under "Link setup" page](https://static.semrush.com/blog/uploads/media/1a/50/1a5017481ccc8a5930013c7630642437/efea8715d806d5571a1b4959d2a50018/aGgmzazbTNLd3Ue_8w5lPA1-YPX4-UGhplsnWwlGePXNOVLrPtczDaNr_FeXHeE5UNKgnLowZBHRdqIvEdIM2DwDWt5me-xoF7lqLq8fM1CvIhelf76ZAjxfQ0uv6j3Rl57tMV2Wzpxx.png)

You’ll see the relevant web data stream in your GA4 property. Click it.

Click “**Next**” again.

![Select the Web Stream and click "Next"](https://static.semrush.com/blog/uploads/media/16/5b/165bbbbc92b54d0351ec395932ac8f75/32fe4ed47a5c07a5d546c94f4c1b64e6/0SVsURuuaF2C6IAHuAVN14vjdTtT39i8NSmxApWSiRgkiwtUypE3pqLlEKNOHEsKWBon4uQQuRPJIYEplUXVrowTLM7LQ3BbmqUPUbtzw9blw_yhPfARKQ5qoiy-GtMoBkGM76P-hMz9.png)

### 5. Review and Submit Your Search Console Link

You’ll see a final review screen like the one below.

Click “**Submit**” to complete the Search Console integration.

!["Submit" button highlighted under the "Link setup" page](https://static.semrush.com/blog/uploads/media/a4/a1/a4a193df83e640c78f12152f52f69947/a7d47127a347681406a5bf827e639a8f/OT3TkL_1Ktv9qr1Gd8wL4SIaXpDyul0pmtAAx4__aVJ-lsOoqSAVX3oLcYKTEukHyZ-8asbEqSWK7EzfAsxJK-xzu-uOgwKqJgQuNPRjWuxSy0_WReg7wQAa5qzcQTC7ikUOBZsFWc-A.png)

### 6. Publish Your Reports

You need to publish your Search Console reports so you can find them within the “Reports” area in the left-hand navigation of GA4.

To do that, click “**Reports**.”

!["Reports" area in the left-hand navigation of GA4](https://static.semrush.com/blog/uploads/media/0a/a1/0aa1ff33324aa32f526fe9a2e4b2b294/a9f51e43452304e27a1232f9795fc0a6/MvOQo857b7U3MPIhUVvMBFxG4atUCi4db6lAxu9Q70E5JYPvzMJeuyEaCNyOlC32mPJiz95TjZi4F4uSzPWfzvPcSrTxHUf-Xx3byS-5To6EA9SvnsZsHKZc60u6Jm9kNh6Ux30zmWyO.png)

Then, click “**Library**” to access your available reports.

!["Library" selected from the GA4 sidebar](https://static.semrush.com/blog/uploads/media/ba/17/ba17b39b1a8a2c92ac55e1fdd6713700/84aacc0a84fc71f4d4959681d0c228c6/v0jLdN7TkE8VxtQxnsxJqgN3LlGfUDudpRUbIKNSmXca9RcDUqWn4b0F3eUhdeXoQgbcPaA32nifwEfMQpSI3iKGA6DhiQ2JOC9f5INBlCsy41tGkPJXPIOZjKODw7s9xusM58zxbO4h.png)

You’ll see “**Search Console**” within your “Collection.” It may show an “Unpublished” status. (If it shows as “Published,” Google has already done your work for you, and you don’t need to do anything else here.)

Click the vertical three-dot icon.

![“Search Console” widget highlighted in the “Collection" section under "Library" page](https://static.semrush.com/blog/uploads/media/fe/24/fe242f65899ce9a7868dd49d55b7768b/35c302801ebda71f0339b087f8f4c463/ollFG_rSeCv5QsprVY68rE0_Ece0LWUn6UdoC5zH50QlYhRjRPjgrP6O5Ee0ZzT4bqnc78N9bVQCXwwbz7wz6F237AoMYFkLC50HbeQdczhrbdmNSAKZ8DE6hDDYNsDI2DdsxPnkUH33.png)

Then, click “**Publish**.”

!["Publish" option selected in the "Search Console" drop-down menu](https://static.semrush.com/blog/uploads/media/c9/04/c9046da95c5188c4ac4b00a78990e0d7/92fb95f0e685c4e8641affc40ae5b653/LNS_eUVhaluAQ245vzj9-zmczL-Xpny_-Qqk7VlePl0v-91zAPuV7uvGWIhMdQrNfD2NQlB_kXaEYgG3BjNjj4-Tjlb0sAxL720lxueMOIobvhcSLR1HPsoaTKhoeHjj9QhGg1nadcEW.png)

Now that you’ve connected GSC and GA4, let’s see how you can use your new data.

## How to Use Search Console Reports in GA4

Your Search Console data appears in two different reports in GA4:

- Queries report
- Google organic search traffic report

You can now find both of these by clicking “**Reports**” within the primary left-hand navigation.

![“Reports” selected from the GA4 left-hand navigation](https://static.semrush.com/blog/uploads/media/03/e7/03e72c785a5bf5fcd60f800c8ac08715/9b15a87570b908353c1dfeb55cdf5693/eZVEkiMI2FmTYHuCFB416E44LA0BhzSjxTfw9uB2R31R4ITxWA6oFDp795RnAdIBfaInubZnu_QsOHOBTOSUYzVqsNae0H1GmINSwpp78VdCfF2TEyD60aPY0IH2PqOX-EpGPX8E8Ue5.png)

You’ll see your “**Search Console**” section below your “Life cycle” reports. Click on it to expand the individual reports.

![“Search Console” section highlighted below “Life cycle” reports in GA4](https://static.semrush.com/blog/uploads/media/da/e6/dae623b84572982fb29d9e8cb04811a1/f65e06e1500400bc75875541649cf3cf/NfKghNJnQECoykIeHJYL1nS1FePkRd_6b1U6wzL1lHfo-fMpCxRHB-HXH16mzAstZ_GpmrT_Z3rf0uTNP3M2N17WUDD33NLVRbpW5ZDKNU_L90Nk-39a4ItAOk3ISYIBuTxX8-d2Bq2S.png)

You’ll see both the “Queries” report with keyword-level data, and the “Google organic search traffic report,” which has landing page data.

Let’s start by looking at the Queries report.

### Search Console Queries Report

The Queries report tells you about the specific search terms your visitors typed into Google before finding your site.

It can help you understand more about the needs of your visitors. And track how your site is ranking on Google for the individual keywords they are looking for.

You can also identify pages where your rankings are dropping. These can be great places to [update your SEO](https://www.semrush.com/blog/on-page-seo/) efforts.

The report shows the same four metrics we reviewed earlier in this article, albeit with slightly different names:

1. **Organic Google Search clicks**
2. **Organic Google Search impressions**
3. **Organic Google Search click through rate**
4. **Organic Google Search average position**

By default, you’ll see your top 10 Google organic search queries ranked by the number of clicks each one received within the given time frame.

You can click the drop-down arrow to the right of “Rows per page” to display more queries.

![Organic Google Search query report shown in GA4](https://static.semrush.com/blog/uploads/media/57/b8/57b8279f03333a051dc0f6bdc1b651fb/cfe4e0a4cb193703b2f72c8ddc223e69/dLVRfMeMO1tKcU48TKgfVc3pmfzKzTTfE-ZQMCPE5MkcsAQLstLKLrP_NQ_Yz02J3J6CXSWmO2KvRp7SikmL1bKv4pQ6lrrFiFch1VrAbwtCEGRAJ6nFyZxDr5ToTm9mpqt8XBiucFSp.png)

On its own, the report provides a snapshot of your website’s Google organic search performance. You can use the date range selector to analyze your performance over time.

![The date range selector highlighted in the upper right corner of Queries: Organic Google Search query report](https://static.semrush.com/blog/uploads/media/97/75/977545c7952f986949b903155e7a532e/b6278b7f93bdf48b89932822c2d14448/Hh6vQiu1sIijm6Azw_z1Ioru7-HtOrzTW7KYZc0bXrjY03VXXF61lLkKwULRoGLJ8fhUyDXCs8-T-_x0-ycM6oJq3inwGPHrmTlphJJ_qsH9mzOkl0EmiZL2UQ89J-v3_WtyXsnvQxDr.png)

By default, you’ll see the past 28 days’ worth of data. You can get more detailed information by adding a comparison to your date range.

For example, you might want to compare your recent performance to the preceding 28-day performance.

Use the “**Compare**” toggle to add a date range comparison.

The default comparison is the immediately preceding period. In our case, the 28 days before the most recent 28-day period. You can do a year-over-year analysis or use a custom time frame.

We’ll use the default comparison. Click “**Apply**.”

![Setting the default comparison option under date range selector window](https://static.semrush.com/blog/uploads/media/f9/91/f991ac8304c0ccda8772fa9b55fb4bd2/37335f4e5757a6d59c49f88f6ab25068/G0yyUgnFpc6jB5zHDrE7EyFWaycouwbQtPRMpqUt5IZaSOG6fZd2qBYQWxKIcENst6jfq2twzS8zwF4T6AF7Ni1tTe2lB_E1EkIoo1TWzMK0Hwgn3yjp-iuv32L5MZ1t6HRvMU774Xmu.png)

You’ll see three rows for each of your search queries:

- Your primary time range
- Your comparison time range
- The percentage change over time

The third search query stands out in this example:

![Organic Google Search query report in GA4, showing the comparison for the selected date range](https://static.semrush.com/blog/uploads/media/14/b6/14b6ea2c56d852402f71a82e3096e3a7/f02d363b9bb05e19da98058db547f85a/U55qzQ_wakY2-gRcyOjRrCx56WhyN557SMnLlAnBgjoM0ABZ8TP6LN8w9obLFQKK-F6RgRVWK8KXCpsxEW6IwvIUHyYyVMtY9nQsDP39qAe4AHH4g5yylrVzZMIwdcZU40XGnlmHxagr.png)

You’ll notice that it’s one of the site’s top click performers despite its low click-through rate. It represents almost half of all the site’s Organic Google Search impressions (473,990 out of 958,562).

Clicks also increased by 9.55%, despite the rankings drop during that time (going from an average position of 6.19 to 6.35).

This indicates that search interest is increasing for this term, but the page is likely not well-optimized. Which we can tell from the low click-through rate and dropping rankings.

It could be worth reviewing this piece of content to see if you can further optimize it for that search query and increase your organic traffic. And you can use Semrush to help with that.

In this example, we’ll use the [Keyword Overview](https://www.semrush.com/analytics/keywordoverview/) tool to learn more about the “emoji kitchen” keyword.

Type your keyword into the blank field. Then, click “**Search**.”

!["emoji kitchen" keyword entered into the Keyword Overview tool](https://static.semrush.com/blog/uploads/media/01/a2/01a215125b8d063b4c1d11246bfcbe10/59d18a653a1056b53aecb81f09bb59b9/9I2PW3yqiYKUS_mMNrMSzLGSN29TWWpYcFyTu4AJsttEUIiYnWs98kSjeiQuU0Lnim3EyYD89SqIwTzgKOxZlpQtrsCouMhzH_hW_gGnPCZbxIGmfsvo9BDEDNk4PB15v-Tgosa8PezF.png)

You’ll then get helpful metrics about the keyword. In this case two pieces of information are especially interesting:

- Volume (the average number of monthly searches) is 135k in the U.S., but if you look at “Global Volume,” you see there are three other countries that have at least that much search interest
- Trend shows the estimated interest over the preceding 12 months (Interest in this spiked recently.)

![Keyword Overview tool results for "emoji kitchen" with "Volume," "Global Volume, and "Trend" metrics highlighted](https://static.semrush.com/blog/uploads/media/c3/30/c3301591810defe229c84b0b40b3428c/01a793bd58932e24e4c684f1598f1ac3/iEQ3s7Bg73jFXG1vYs8KMqwAerzsSqe4-fWVrdX3RG0eGuCajtb4vUszUx2u67EdxjC3P0s2wNtrZ9GjJaMHgsfom1EmjoSuu-rnHETJzAQC3yX1FJQ9SXdZLUaqsexDnObJdiWFwgei.png)

You don’t know what the future trend will look like. But if you optimize for the keyword now, you’ll be better positioned to drive a greater share of clicks if that trend continues.

And you may want to consider optimizing for search in Turkey, India, and Japan, where search volume is equal to or greater than that in the U.S. for this term.

The “Keyword Ideas” section of the report can provide ideas to further optimize your existing page.

One simple way to do that is to use the “Questions” data. These are search questions that include a variant of your keyword.

!["Questions" widget in Keyword Overview tool showing search questions that include a variant of "emoji kitchen" keyword](https://static.semrush.com/blog/uploads/media/ba/ec/baec478d1c3ee290db86f747720daeae/f8e14a01dd7b4dab2353f92e7117e51a/ZI_-ORZvewsRBIP6Bv2wl4rkuBIsm_LQ433ggr7lbANI5rYuxnc5k0EOzk8zSNOTEnX7dz9aZwa5VKz1aFnWNE5uOaaOCMUE5EBSMA4erSJfScQMXxs4vunnDfubvsTNluDE0JV2bajq.png)

You could use these terms to add an FAQ section at the bottom of your page to address these specific questions. This could help your page rank for those related keywords, while providing additional value to your readers.

### Google Organic Search Traffic Report

The Organic Search Traffic report tells you about your top landing pages in Google organic search.

It uses the same four metrics as the Queries report and combines them with more metrics from Google Analytics. These GA4 metrics tell you information like each page’s engagement rate, and the number of [GA4 events](https://www.semrush.com/blog/google-analytics-4-events/) tracked on each page.

![A report in GA4 showing "Landing page + query string"](https://static.semrush.com/blog/uploads/media/75/5d/755d248db514ae09540ad140409d3bf2/7ceedb7bb589d77c732eee30aec33b5b/7isEYXNl0WFjV46ju3wiIHye3b-qM0DAQo664Z_9S5qOXVW3Uu__2NEFofjbAcFUB5LNsCsNjyDQnyF7MBhQWBNUUXwm4O1lWWPX4p6k5gByk_ngJV9cTc92fF0V4gfg3ny5goTmK4F_.png)

The fifth landing page on the list looks like it’s the page where the “emoji kitchen” keyword is ranking. The “Engagement rate” for this page (42.47%) stands out because it’s much lower than the average across all pages (64.32%).

Engagement rate is the percentage of sessions where a visitor satisfied at least one of the following conditions:

- Viewed more than one page
- Actively engaged with the page for at least 10 seconds
- Completed a conversion (such as buying something or filling out a form)

The low engagement rate tells us that these kinds of valuable visits are happening less frequently on this page. This suggests you might want to update it to make it more helpful for your readers.

## Take Your Organic Search Data Further with Semrush

Get useful keyword insights alongside your Google Search Console and Google Analytics data all in one place with Semrush.

[Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) combines three important sources of information:

- Data from Google Search Console and Google Analytics for your top landing pages
- Conversion data from Google Analytics so you can see which of those pages drive the most conversions
- Keyword ideas powered by Semrush so you can find ways to drive more traffic and get more conversions

!["Organic Search Traffic" report in Organic Traffic Insights tool](https://static.semrush.com/blog/uploads/media/b0/1d/b01d7784da55a4b69fa5c0fa99bd6a9d/722179ca900a493b1227307b7078d7b5/QxH27NcjFMUifZB_7p2MO0UAUPRO80YPhF1sxXQP0Oyuay5QdFT11yaWY3DMXMRYmcEKOsxyWXqy1EdRRe7D4MpoBlvE6WMveoxFlLqZ9wxrYsSPbMc6qq2l9x6LZoUXCxmttSXOOXCt.png)

Look at the second landing page in the list. It accounts for over 35% of all your organic search conversions (41 out of 116) and 2.4% of all sessions for that page result in a conversion (41 out of 1,708). You also see that your sessions and your conversions are falling.

You want to use keyword data to find opportunities to improve your rankings and drive more traffic. To do that, click the hyperlinked number (129 in this case) to view Semrush keywords driving traffic to that page.

!["Landing Pages" section of the Organic Search Traffic report](https://static.semrush.com/blog/uploads/media/5d/4b/5d4b29d9862b662ed6a238d4bd567d15/a4416a52cbc5bb51e1507f50252fb95e/YfdFgSgz_fJ432KpLdStOjIEVH4zq-Mq6vzPLW5dAKca7K7Nd6SGX0IuBpMhWHRlbyyInr26NDLbcscBbcEYAKpdqxhmHTui_wfORnYbAC9tgYdOVyfzM85E3ONlGsUYr_BZRi97XFfG.png)

This will take you to a page showing keywords along with various metrics for each, including two that Google Search Console doesn’t show:

1. Volume (estimated number of monthly searches)
2. Keyword Difficulty (an estimate of how hard it would be to rank well for each keyword in organic search results)

You can use both of these metrics to find new keywords to target. You focus on the fifth keyword in the list, “ga4 active users.”

![“ga4 active users” keywords highlighted under Semrush keywords table](https://static.semrush.com/blog/uploads/media/77/5d/775d55cd275bbc0f200361fb6ab8d3ac/4a48d765651fd00558b56edc15ca9ee5/ZmsAfSJ9SWu5QTm2XQCTtAi011AuNQ_7LcP58E6rlHx-2l7nEcyprQoVOrcdO1yHcGn9bnfVhmDgwDJh6iCrC9yGDnWF2X6D6AK0VI03lOMJ-0FnCrYxP6xg7tBxDt3vAxVEErTUUjnl.png)

You see it has a Keyword Difficulty of 20%, which is lower than keywords for which you are already ranking in the first position on Google. Yet, your page is only ranking in the sixth position on Google for this term.

This could make it a prime candidate for a content update to improve your rankings for that keyword, boost your click-through rate, and get more conversions.

Want to benefit from this kind of data on your own website? Try [Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) for free today.

*This post was updated in 2024. Excerpts from the original article by Amit Panchal may remain.*
