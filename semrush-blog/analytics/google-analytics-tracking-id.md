---
title: "Google Analytics Tracking ID: What It Is & How to Find It"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-analytics-tracking-id"
url: "https://www.semrush.com/blog/google-analytics-tracking-id/"
canonical: "https://www.semrush.com/blog/google-analytics-tracking-id/"
author: "Rachel Handley, Zach Paruch, Christine Skopec"
published: "2021-09-08T16:59:00+00:00"
updated: "2024-03-25T09:51:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2024_watch"
  - "time_sensitive_title"
schema_genre: "Analytics"
fetched_at: "2026-06-12T15:43:08+00:00"
status_code: 200
html_hash: "a6f41da028f906bfe3179fa709bd691045c9200bf0dd9a2208edffa48d55ea16"
clean_word_count: 2291
clean_char_count: 19922
---
# Google Analytics Tracking ID: What It Is & How to Find It

## What Is a Google Analytics Tracking ID?

A Google Analytics tracking ID is a unique identifier that’s automatically assigned to each website or app in Google Analytics, a popular platform for tracking user behavior.

The tracking ID is used during GA installation. To ensure that user interaction data from your website or app is transferred to the correct data container.

### Google Analytics 4

In [Google Analytics 4 (GA4)](https://www.semrush.com/blog/google-analytics/), a tracking ID for a website is called the **measurement ID**.

It typically has the structure “G-XXXXXXX.” Where “XXXXXXX” is a unique alphanumeric code.

The measurement ID is frequently referred to as the **Google tag ID.**

And it’s also used in the **Google tag**—the unique tracking code that can be used to manually install GA4 on a website or app.

Here’s where you’ll find the ID in the GA4 tracking code:

`<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'G-PSW1MY7HB4');
</script>`

### Universal Analytics

In Universal Analytics (UA), the predecessor to GA4, each property had what was called a **tracking ID**.

The ID had the structure “UA-XXXXX-Y.” Where “XXXXX” was a series of numbers that represented your account ID and “Y” was the property number within the account.

## How to Find Your Google Analytics Measurement ID

Let’s learn where to find the Google Analytics Tracking ID in GA4.

First, [sign in to Google Analytics](https://analytics.google.com/). And open or create your property.

Then, type “Measurement ID” into the search bar at the top and refer to the correct result.

![“measurement ID” in the GA search bar and the relevant result highlighted](https://static.semrush.com/blog/uploads/media/3f/b0/3fb0096b9ef0ac2f8588cd97aa490f16/ee2e49cd983248d81703102bda7d9b5c/i4psGN-nIWwprva3nVp6-eLhJnrbNtmwJQv9iURhkcCe1ccctRh2ObKZcBZvITLZU9e9yFqPNOwGZ7OrHBK9xKYozULdB7hT2Y9TdcSqlPtoTJbpO6szjwF6goVUVKg-g3Jfo6MS09MQwaizl8GGfpk.png)

Alternatively, go to “**Admin**” > “**Property settings**” > “**Data collection and modification**” > “**Data streams**” and choose a data stream.

![Navigating to “Admin” > “Property settings” > “Data collection and modification” > “Data streams”](https://static.semrush.com/blog/uploads/media/6b/e5/6be57c8908b475fb868638515d5bcfa9/f4a61a3fdabb0c2dac54cac61c17f2b9/RCfz086sLe400AKIeZ7HX3Gv-18KOJxVPUWBfygTPgbqHmMEREEyDxfJzzOxGlZ9DEvH1CSyTNXnNmfpjsFrs7egot8QCBrh8pNuFp6tUU9_Rwuly7KfjCeGrXK6d-FYaXdkyb-7xMsIV2QQdYp4DLM.png)

Then, refer to the “Measurement ID” section.

Note that you can copy the ID by clicking the icon alongside it.

![“Measurement ID” section under "Web stream" details](https://static.semrush.com/blog/uploads/media/c6/4a/c64a7ab5a88f16b1beed3a0b07bc4bb0/1e552314c28df7a34aed0e2102e39866/t7WDC-nNhE1jJ0WIOvFsXYDp0tskU0pwLkzE-V8SdlIcd3-fXhfEkrmo9JzRSDDBDAZRugPXioWkMhAomVygnNzInlrdHG8OBKX7qpOxBXMTcb4LUt1GVJd5JPs4dRaanaY2iBnpRp-sQ0zl3xz_xoY.png)

## How to Install GA4 on Your Website

There are three different ways to install GA4 on your website:

- **Option 1**: Install via your website builder or content management system (CMS). If your platform or plugin offers support for GA4, this tends to be the simplest method.
- **Option 2**: Configure GA4 in Google Tag Manager (GTM). This tool lets you manage all your Google tags in one place. And it gives you advanced functionality and greater control.
- **Option 3**: Manually add the GA4 tracking code to your website

Let’s explore each method in detail.

### Option 1: Install via Your Website Builder or CMS

Many website builders and CMS platforms (including Magento, Shopify, Wix, and WordPress) offer native support for GA4. And some offer plugins that allow you to integrate the tool.

Generally, all you need to do is enter your measurement ID into a Google Analytics field.

For example, here’s what the field looks like in WordPress:

![GA4 ID field in WordPress](https://static.semrush.com/blog/uploads/media/e1/1b/e11be537e65cc8bb7484cf6384f32e8a/1b8411e04b0f45dd08c6aca86d1c18b0/RTVbzunjChabJiyPF0uDOoVLehE_t0iUNE9iaC--elLql4w8Y-O-GvaRopwlJGp9xq7Ibu8PotgKLjF3KQoAvkf27kuu48kkZ4N45FYdKioljQ04VJn5v-5F-HUgFPEbOj7vkRZI9fuM7dG8VexFqMA.png)

To find detailed instructions for your platform, sign into GA4 and open or create your property.

Then, go to “**Admin**” > “**Property settings**” > “**Data collection and modification**” > “**Data streams**.”

And click a data stream.

![Navigating to “Admin” > “Property settings” > “Data collection and modification” > “Data streams”](https://static.semrush.com/blog/uploads/media/6b/e5/6be57c8908b475fb868638515d5bcfa9/f4a61a3fdabb0c2dac54cac61c17f2b9/RCfz086sLe400AKIeZ7HX3Gv-18KOJxVPUWBfygTPgbqHmMEREEyDxfJzzOxGlZ9DEvH1CSyTNXnNmfpjsFrs7egot8QCBrh8pNuFp6tUU9_Rwuly7KfjCeGrXK6d-FYaXdkyb-7xMsIV2QQdYp4DLM.png)

Scroll down to the “Google tag” section and click “**Configure tag settings**.”

![“Configure tag settings” option highlighted under "Google tag" section](https://static.semrush.com/blog/uploads/media/96/cb/96cb59cd6244938fe8e9d60ed0f272d7/5e683005926628800fe14b2ea0183fbe/7VPc5AwS3kW8cd-UNmVL84LpGhSXCIeZsaFlwWUEPcY9mxvtP-Ggy_dWfm-TauOzJ4slT2TCoU272jcdU6WefwWvj8GG3GWS78DoWfz5pDNcZPw9jeI1W-laG0skqUUizEdF3YRGUqyAFR5maPvnhhg.png)

Next, click “**Installation instructions**.”

![“Installation instructions" button](https://static.semrush.com/blog/uploads/media/fb/a1/fba11084f8739d68a3393e0ddba9c309/0fdd41bebb108e5478d09e167d51a2de/D3LWIVSmbZRCLJWhMunzhprlUq1TJTo6AHR9cgGd36JF9GIbCKMLHAVcaimg3Ug57AviqEclIM-sXp1B8F9ruMttvxozgd4Odk6VN6v8jL3u-Bg9YWky32UeKmpojtFTcnYVIvTJ9N3pBQOBkiJhcaw.png)

Click “**Select your platform**.” Then, if available, select your platform from the list.

![Select your platform section](https://static.semrush.com/blog/uploads/media/82/91/82918a40756ca592221a784fcaaad378/c727d743a81895d1320e3a4019e62fd3/b8LJMVh9iZyLkALxVGFmGmIx8BUfhYIuYHssE-apYnarqSdkBHSBOrtOVWGHeizW6XFM1RV05AYrxKZEEE4y-gWBRdOGo74RxE_KMNtjTJiTOIfIXl6ZvCKCMNgYJx2M6YJw97jbWZ8npI94tVFb5xM.png)

Google will provide your Google tag ID and all the instructions you need.

![Snapshot of instructions page for Shopify](https://static.semrush.com/blog/uploads/media/ef/09/ef096dd7cbdd64596d1bde5626965a5e/2182307dbb6528cb277d823417dc185b/e_22kVLPkfPbSWvIy_Evb6zWkLPwAS4hNHzqxARZzmZPv20NNXXAnOPhMAviuUyOiaKkVB4AbZCy-BtjJQQDLKKJCeGXAluA6Mq_FHHttxefrmANmOpGSUfWT1Jfx5tLfGHUY1qacZtv3J5ui4kXdUk.png)

### Option 2: Configure GA4 in Google Tag Manager

[Google Tag Manager (GTM)](https://www.semrush.com/blog/google-tag-manager/) is a free tool that helps you manage various kinds of Google tags. Including the one used for GA4 installation.

In addition to setting up your GA4 property and web data stream, you’ll need to:

1. [Create an account in Tag Manager](https://tagmanager.google.com/)
2. Create a “container” (a space to house all the tags, etc.) for your website
3. [Install the container on your website](https://support.google.com/tagmanager/answer/6103696)

When you’re ready to configure GA4, open the relevant container in GTM.

And click “**Add a new tag**.”

![“Add a new tag" button in Tag Manager](https://static.semrush.com/blog/uploads/media/91/e7/91e76085ea7d52fe5056bbf99da45f89/df650595a8efd66acf905d8d2b4b55f9/kZDGcd2vJ7wq6NnKUNtqBV4u5LSVM0D8uIbg4H78PuG6LNdnkt1sDNDZ6fyex-WEyTsIzDyyo_ZF-Gn8MNWydAyzf7xfkylMwitu-O3ViGK_xR2IEcgQ2XUz_tTQ4D3pAEeLxezMTFY7gaaP8qiWsfw.png)

Then, click “**Tag Configuration**” > “**Google Analytics**” > “**Google Tag**.”

![“Tag Configuration” > “Google Analytics” > “Google Tag" buttons highlighted](https://static.semrush.com/blog/uploads/media/e6/cf/e6cf5fa5c82718ec8070d3d0ff94347d/3e7607b69dcc044b8125f17c7a089de8/kRCJKWsR83sqxPhZKICGbh3a4kA6o_mZ3InSZFEclQd4mlec1sJ2CN13HsyxxQYQOIq2ehKieDCdxjMJKh-NaeA8qBvjC-mR8ROmnvkK2zkOGwMSIF5kEwaR_6aHFpxYfv0ESX85TXYN0CEsXPjVq0I.png)

Enter the measurement ID for your GA property in the “Tag ID” field.

![An image showing measurement ID for GA property in the “Tag ID” field](https://static.semrush.com/blog/uploads/media/d1/f0/d1f0bcd7195d062b90511eff2b6acd9e/7bb369940c0f267216a694b9e099538c/sqz2YLlWc_TM3jN8O-6-s2Kw6HugfXdmSsRaBoz6VyLC5fUvXe2hoX_hNmANmX4D5sTS6mKvi8uFlqy8_tyWtDtqwY9-p5RZwl5jdam4jj4L8YhzRyO2XPhkikLxb6WprXiUUJ9PFsncNyK9M8xAUa8.png)

Then, follow the instructions in [our GTM guide](https://www.semrush.com/blog/google-tag-manager/#how-to-use-google-tag-manager) to configure the remaining settings to your needs.

### Option 3: Manually Add the GA4 Tracking Code to Your Site

To manually install GA4, you need the Google tag for your data stream.

To find it, [sign into Google Analytics](https://analytics.google.com/). And open or create your property.

Then, go to “**Admin**” > “**Property settings**” > “**Data collection and modification**” > “**Data streams**.”

And click a web data stream.

![Navigating to “Admin” > “Property settings” > “Data collection and modification” > “Data streams”](https://static.semrush.com/blog/uploads/media/6b/e5/6be57c8908b475fb868638515d5bcfa9/f4a61a3fdabb0c2dac54cac61c17f2b9/RCfz086sLe400AKIeZ7HX3Gv-18KOJxVPUWBfygTPgbqHmMEREEyDxfJzzOxGlZ9DEvH1CSyTNXnNmfpjsFrs7egot8QCBrh8pNuFp6tUU9_Rwuly7KfjCeGrXK6d-FYaXdkyb-7xMsIV2QQdYp4DLM.png)

Scroll down to the “Google tag” section and click “**Configure tag settings**.”

![“Configure tag settings” option highlighted under "Google tag" section](https://static.semrush.com/blog/uploads/media/96/cb/96cb59cd6244938fe8e9d60ed0f272d7/5e683005926628800fe14b2ea0183fbe/7VPc5AwS3kW8cd-UNmVL84LpGhSXCIeZsaFlwWUEPcY9mxvtP-Ggy_dWfm-TauOzJ4slT2TCoU272jcdU6WefwWvj8GG3GWS78DoWfz5pDNcZPw9jeI1W-laG0skqUUizEdF3YRGUqyAFR5maPvnhhg.png)

Then, click “**Installation instructions**.”

![“Installation instructions" button](https://static.semrush.com/blog/uploads/media/fb/a1/fba11084f8739d68a3393e0ddba9c309/0fdd41bebb108e5478d09e167d51a2de/D3LWIVSmbZRCLJWhMunzhprlUq1TJTo6AHR9cgGd36JF9GIbCKMLHAVcaimg3Ug57AviqEclIM-sXp1B8F9ruMttvxozgd4Odk6VN6v8jL3u-Bg9YWky32UeKmpojtFTcnYVIvTJ9N3pBQOBkiJhcaw.png)

You’ll find the Google Analytics code in the “**Install manually**” tab.

Click the icon in the upper right to copy it.

![Google Analytics code in the “Install manually” tab](https://static.semrush.com/blog/uploads/media/cc/eb/ccebc1e4548c24f45491f011b8e60d02/cf081e77d4896e2feb5b1b41f69da306/LJGvHLyt_VTBiLcq1PSOVByKFHL8Xyuzq0_48LlMBVUEFzELGwnMAb60OuL_ljYDsWa4CUgmzeBfX7JAIu7bOOkE1xYHiEIWR5ryOKZGb5PeAslwWQdkXW0Te8veL0oUnXcnbCq60TxJ7PFnkd7_Smw.png)

Next, you need to add the GA tracking code to your website. It should go immediately after the <head> tag in every webpage or webpage template.

Like this:

`<!DOCTYPE html>
<html>
<head>
  <!-- Insert GA4 tag here -->
 <!-- Other <head> elements like CSS links, meta tags, etc., go here -->
</head>
<body>
  <!-- Website content here -->
</body>
</html>`

When you’ve installed the Google tag, return to the GA4 page you were on last.

Then, enter your domain in the “Test your website (optional)” field and click the “**Test**” button to check if everything’s working correctly.

![“Test your website (optional)” field](https://static.semrush.com/blog/uploads/media/5a/de/5ade658b22fec3081fc26a3b15646f29/d3138a092c87f87df11d7c280f4022c6/qa8miJLTJ9i1gOOOAuArptYEWKOGYwG1C19xRIZ7mTM0C0mbGaC8ekopnqqc5PfL30nSj0r9Alw-QZYRPP8BIVlB10MyLQVo_QJQLQvjw7jAf2gKG_P-WxirpCOIe0f6RR5d8q-ydg4zdFsiigjJphA.png)

## Take the Next Step: Integrate GA4 with Semrush

By connecting your GA4 property to Semrush, you can get additional insight into your website’s performance. And make better decisions for your business.

Let’s see what you can do with GA4 data in five popular tools.

### On Page SEO Checker

The [On Page SEO Checker](https://www.semrush.com/on-page-seo-checker/) provides tailored recommendations to help your webpages appear higher for relevant search engine queries.

To connect to GA4, click the “**Connect**” button next to “User Experience Ideas.”

![“Connect” button next to “User Experience Ideas" highlighted in On Page SEO Checker](https://static.semrush.com/blog/uploads/media/0d/25/0d2565480c72ac6cb807e116e0b17531/b08f44caca31f22258eaa7bcc209c0e1/olNitCmjRQ1idZppWyKtMoJY8wU0gAaRsvpJyvLzVPsatm7Xul-ZwGBYOszliFb709a2OmDo9tE0aoMDvTLdYUBoCgyBZPB099wGBV_M90JKbG-ThpdBPCdIM1JQ6-IHjnVcE5E_0IkfdWQp1SPrH1k.png)

Then, follow the prompts.

The tool will then determine whether each page has a high [bounce rate](https://www.semrush.com/blog/bounce-rate/) (i.e., lots of visitors leave without engaging) or a low time on page (i.e., lots of visitors leave soon after arriving).

These issues can suggest that your page is unsatisfactory and needs to be improved.

![User Experience suggestions in On Page SEO Checker](https://static.semrush.com/blog/uploads/media/2d/3b/2d3b24c78a208db9e64ff52fc9f637b8/7dfb8363237d8f614b245fb6b4cfa88e/G5jM_-cv0qtLJlRa-5a601Z2CoVRpDf-JICZ2bBxZfjnZt6wrrDuyXaDq2aaFNnvhC-szucriQvRRdfbqM1JRJbPRpfbUDyfUopw5qkHG_Gck12SIr6nMzk3yGtEmVm-Cpm2oVqtDTfckjDYyR3muWY.png)

The tool may also provide ideas relating to [keyword strategy](https://www.semrush.com/blog/keyword-strategy/), [backlinks](https://www.semrush.com/blog/what-are-backlinks/) (links to your site from other sites), [content optimization](https://www.semrush.com/blog/content-optimization-guide/), etc. So you can easily determine where to focus your [on-page SEO](https://www.semrush.com/blog/on-page-seo/) efforts.

![Ideas overview and top pages to optimize list in On Page SEO Checker](https://static.semrush.com/blog/uploads/media/32/ea/32ea56e610ae8ac6d939e3c276db866e/b716ab1fd893d7b2ea5f96604d466610/PqQkSHdt9pPVRbMbZ17xL12lBOFsIyLgEZ0Cei4bvAebXel7nhp4rEGkAlG52g8hgy7ljIUCPBIswiBiELcMCA0iWI4Ijh2SEl-YRZe2vJokZxqY8yoZ6stCsTCG01ZQiT6syqpTiYa7XxL2VoNw42w.jpeg)

### Backlink Audit

The [Backlink Audit](https://www.semrush.com/backlink_audit/) tool makes it easy to review and monitor your site’s backlinks.

To link your GA4 account, click the “**Integrations**” button in the top right corner.

Then, select “**Connect**” under “Google Analytics” and provide the details requested.

![Connect Google Analytics to Backlink Audit tool](https://static.semrush.com/blog/uploads/media/c6/db/c6db8e73f60c5231a8a0b433c2483c66/7a61da7e344c1009cc739674643d4f8e/LNw0QIlQGSpP0tas2F5I3MKirCnSCyjTD75dt1H7FDBA0zAeqiH74nFLTGozNfKiAmlqvysZNPT0jxdB9gwrjQtKRtY2z-t0vV7oaCbqbb5kgv5eS6zLMI-7mD3dvXy7CU5LhQRLUsYkikpmPuXvLB0.png)

Once you’re connected, you can see how much referral traffic each backlink drives:

![A table showing how much referral traffic each backlink drives in Backlink Audit tool](https://static.semrush.com/blog/uploads/media/22/75/2275d5b5644c3ea63a69a1acecbd3eb9/e3be994995e17b3607cc43b0e06b697f/gNGNGRdzwmax-7tgOu54dZn-OcI5bl1S2E5PgXPD1AmKgjkvR_PfahN_iuExa1w1zj5mjEqEh1_ssBDv1izrJWTuaV2Uj8jbVSyN4W7AiFT-uYckt30ECP2qXG2tmvafSVNCJjmzyQaqH5Nw4ycTL-4.png)

This data can help you evaluate the value and quality of each backlink.

### Organic Traffic Insights

The [Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) tool helps you discover “(not provided)” keywords in Google Analytics.

If you haven’t noticed before, GA4 marks most search terms as “(not provided)” when you try to find them in your reports.

Like this:

![Search terms marked as "(not provided)" in GA4](https://static.semrush.com/blog/uploads/media/c2/be/c2be9b7622efb16541a82338427edc44/042d1d839e0610bfcdcf5b52cd33f2b5/6QA54huhCmjW87cO1wKPDmHEmuCY20WNEDAZEOyL9b5NmhefcneXLdZO5A0nxAlPC2qUY0PmO9_TVuKkyKeJRA_WnVpRye9CumNFFupliGUCX725Soa8D0hLhtxE82PK8f6fHHNoQrHtVQE9iTTMgUA.png)

This means you can’t work out which search terms led users to your site.

But Organic Traffic Insights uncovers these keywords by combining data from Semrush, GA4, and [Google Search Console](https://www.semrush.com/blog/google-search-console/).

![Organic Traffic Insights report showing Semrush and GA4 data](https://static.semrush.com/blog/uploads/media/63/cb/63cb43fb5405f92800e6f2d475622234/31470f95a0cb510a0ae1814fcd621d88/CoPO8_Rvrz8aAokVfpoLKy7lhup8qrl178fQ5GnusqcfbfBZ38Lsei6kssCj6JLy89LS31rM5JvUr_DJDFYulb6eY3xfdo-KCUOqb52W2p79vOoqBAl8UXmEEaK1PI6ZFZBr7uyyyuFdrPGjqsf7-30.png)

The tool also displays useful metrics from all three platforms in one simple interface.

### Site Audit

The [Site Audit](https://www.semrush.com/siteaudit/) tool checks your website for issues that could harm its performance in Google Search.

Connect your Google Analytics account by clicking the gear icon in the top right corner and selecting “**Google Analytics: not connected**.” Then, follow the remaining prompts.

![“Google Analytics: not connected" button in Site Audit tool](https://static.semrush.com/blog/uploads/media/d0/cb/d0cb7e93c67c7ff5002a57892a3a0879/323c95b13df88e0a3d51dd29e9a1d0dd/cvEeIN0gYka2kK2xAj5cfdL6A_QCvIp4A0YQVaEs7fmLEgJ_LrmPuMCiRFdGRZadJtXm8UqkAYBk6dKsrWjCLLM0aiQ2KM1HUvUNawA_TWBBZdu8EEW_91eX1xAu7fKqXmMba7oIYyfsxzZcn4Ofb2A.png)

Once you’re connected, the tool will display pageviews (now called “views" in GA4) data. So you can prioritize issues based on each page’s popularity.

!["Unique pageviews" column highlighted in "Crawled Pages" report in Site Audit tool](https://static.semrush.com/blog/uploads/media/7e/08/7e08bf9e131d8c352d30fd6bc287bb89/58ecb7e818904f6476e4f7091aec0a79/gyUazjHco83q0znJ9bpC3I9Ywnllc3bpJs9NPne0Aho1pl74GKENAQ4hfGa5aU5JqIbIWjtZse0zkPi2jZtalkxu9Q1QBg8Gs17gneHcLcb6Cv0BM8wjwLs4qCRtsynd5y6ypMRqTV7154acwa8I67w.png)

The GA integration also allows you to check more thoroughly for [orphan pages](https://www.semrush.com/blog/orphan-pages/)—pages on your site that aren’t linked to from anywhere else on your site.

![Searching for orphan pages in Site Audit tool's "Issues" report](https://static.semrush.com/blog/uploads/media/74/f5/74f5876427a04cb637c9fec72b9f9fbd/e146c64d638ea540f5a4fec5ef1ac492/u-VPBnkGwOdTMYO6e_p9oj_5y3Q60PpQ7bRK6rrU5IqchSlK4ZlLwf-tnmxkBTxQ3IoKzBFov9-CgweFA2AL4c941Ox_hES2WSf3YltWDo-eb2-XCyYW2QU30oVsugn6eaEjwzqXdx2ClQvscOIbYAs.png)

Adding [internal links](https://www.semrush.com/blog/internal-links/) to these URLs is good for both the user experience and [SEO](https://www.semrush.com/blog/what-is-seo/).

### Position Tracking

The [Position Tracking](https://www.semrush.com/position-tracking/) tool makes it easy to track your [Google keyword rankings](https://www.semrush.com/blog/google-keyword-ranking/) (i.e., how high up in the results your website appears for relevant search queries).

You can import keywords you’re already ranking for from Google Analytics.

![Import keywords from Google Analytics to Position Tracking tool](https://static.semrush.com/blog/uploads/media/7e/f0/7ef0e4abe96902cda99633444e8ab5f1/320fd82b34e40f0fdb3e8920578f1802/r16sL75e34kLM79dqA3mah6Yll2yFWfY2WnHGXSa_1yjjT44WL1G62_nT8APVjFkr4ZAd19eOEbuynKOivyuTCfyv1xSf0OlZwM_IGb40kn6HsNsK8Bj9tB9JWQorcbrwWDP6PPRx54u6nb6pUtZaO4.png)

For each tracked keyword, you can see your ranking positions on the selected dates.

And gather lots of other useful data.

![Rankings overview table in Position Tracking tool shows keywords' ranking positions on selected dates](https://static.semrush.com/blog/uploads/media/0e/8d/0e8de7de452d818b5515582e2d51c0f0/a44fb63e4cde84a98eb18cc62d5b85a2/LzqMClXjJndV88uGMXwojy-0vUbS7qH5S6wCaQwLKdIpBUqrJaKxtgWSPa4BtnbqB4A_RuhtfdtiR6I6-fLJtnZBAQjmRRzd7rC5aHcxYsiku7op6f5zW92BNYVhNQcwW-XdeA96TYFDkIU8cOM5Rqc.png)

Use this information to keep an eye out for trends in your rankings. So you can take steps to improve your pages if needed.

## Start Collecting and Analyzing Data

With the right marketing data at your fingertips, you can make better decisions for your business.

Get started by setting up GA4 and claiming your [free Semrush trial](https://www.semrush.com/signup/get-free-trial/).
