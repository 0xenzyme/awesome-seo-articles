---
title: "Google Analytics 4 Users: What They Are & How to Track Them"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-analytics-user"
url: "https://www.semrush.com/blog/google-analytics-user/"
canonical: "https://www.semrush.com/blog/google-analytics-user/"
author: "Sydney Go, Chris Hanna, Bartłomiej Barcik"
published: "2024-03-12T11:46:00+00:00"
updated: "2024-03-12T11:46:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2024_watch"
  - "time_sensitive_title"
schema_genre: "Analytics"
fetched_at: "2026-06-12T15:43:28+00:00"
status_code: 200
html_hash: "8d5ae4adc3a8b41794f8e6fd0b56f11f88fec14ab3eb2df1483ed5bf0cad8177"
clean_word_count: 2405
clean_char_count: 18382
---
# Google Analytics 4 Users: What They Are & How to Track Them

Google Analytics 4 (GA4) is the newest version of Google’s analytics platform. It helps you measure things like your website’s traffic, user behavior, and conversions.

Users in Google Analytics are one of the main metrics the platform focuses on. Let’s look at how users are defined, user tracking features, and how you can use this data to improve your website’s performance.

## What Is a User in Google Analytics 4?

A user in Google Analytics 4 is an individual who initiates a [session](https://www.semrush.com/blog/sessions-in-google-analytics/) on your website. The analytics platform tracks the user’s behavior as they engage with your pages.

![Users metric in Google Analytics 4](https://static.semrush.com/blog/uploads/media/9c/0f/9c0f6abaa1adbab0c7aa8003e7016ab6/d39b7ef3a84aa2829118acc054cc7901/Gr9q1rS3pKMBGnIPwNo4To7F5pbJ4v7LimeRImfFyvSFhmnn09OhiTmiRS39YlR_5PBGf_cu3aflv_IiiikQJNsRlm6eU1wa9Nbi52MdHpkAQ0ApHQSQgWyC6Wpz_TqNdL5dkJ9kMcSq0i45DB7DMTo.png)

### How GA4 Identifies Users

GA4 uses several methods to identify and differentiate users:

- **User ID**: A unique identifier you can manually assign to users who are logged in to their account on your website. It tracks user journeys across devices, and it’s the most accurate method of identification since you’re collecting the data directly from the user.
- **Google signals**: Session data from sites that Google associates with users who have logged in to their Google accounts and have opted into ad personalization. It’s useful for analyzing audiences, conversions, and running [retargeting campaigns](https://www.semrush.com/blog/retargeting/) in Google Ads.
- **Device ID**: Identifies user sessions across devices. On websites, it comes from first-party cookies (cookies stored by the website), derived from the “\_ga” cookie (the main Google Analytics cookie that distinguishes one visitor from another). This method tracks only the device and not the user.
- **Modeling**: [Behavioral modeling](https://support.google.com/analytics/answer/11161109?hl=en) helps fill the gaps in your data. When users decline analytics identifiers (like cookies), behavioral data isn’t available. GA4 models the behavior of these users based on data from similar users who accept cookies on your site.

### How User Data Changed Between Universal Analytics and GA4

Universal Analytics (UA) had two user types: total and new. UA relied on cookies for tracking users.

There are now four user types in GA4: total, active, new, and returning. GA4 offers multiple identification methods, as outlined in the previous section.

Understanding GA4’s user types provides helpful insights you can use to optimize your site’s performance.

## GA4 User Types Explained

Before we go into the details on each of the user types mentioned above, it’s worth noting that you can typically find data for each of them quite easily on the **Home** tab of your GA4 dashboard.

Click the arrow next to any of the metric headers at the top of the overview card.

![Users metrics on the Home tab of GA4 dashboard](https://static.semrush.com/blog/uploads/media/5b/08/5b08e81e7a0cf179fc0b2e91c32815da/a4609476e2a78a3620128d28a9a63814/kmTT3FB9AO03kVS1OcjBdEaNmjKEjoXOagIWbzMcZNAJ_lUtS8hY_xGg0hcE90S2yeUBYTLm7bzYU5h-r1djhau1Ha1oKCRVmdX9-5uqreu_eXGtaXLBWp4wKM2ZoHeyErW1I_oY1zcGqAvJtauHjZY.png)

In the menu that appears, click “**User**” to reveal a list of user-related metrics. In this menu, you can choose any of the four types to replace the current header with that one and display the relevant data in the overview card.

!["Returning users", and "Total users" selected from "User" drop-down menu in GA4](https://static.semrush.com/blog/uploads/media/d9/1b/d91b239df25d9d57283c2aed166d423a/3a32547af38ae1628550fee7e3494048/ytop2ssR9D3kdqvsKgeVFKEJXrLiC9nSPwZYMPzuKk1bp90y6D1MW-iuupil4KK7o6DHFC3cvseWUDYv2_gEuVXGWr8G0plr99_1TowIZb__E3mgSPpkWkNn059ODVq9qQrlgXrU9RIi0qKX04R5lyk.png)

Let’s look at what each user type tells you about the people visiting your website.

### New Users

The new users metric tells you the number of people who have previously never visited your site, within your specified time range.

Google relies on a unique identifier called a user ID to distinguish between users. When a user visits your site for the first time, they trigger the “first\_visit” event. Google recognizes these visitors as new users.

### Returning Users

Returning users data represents the number of users who have visited your site at least once in the past. The GA4 cookie that identifies unique users will last for [two years](https://support.google.com/analytics/answer/11397207?hl=en). At that point, a returning user will then become a new user.

When users return to your site, they likely find value in what you have to offer. Returning users is a key [Google Analytics metric](https://www.semrush.com/blog/metrics-in-google-analytics/) to understand user retention and customer loyalty.

### Total Users

Total users represents the total number of people who visited your site during a specified date range.

This Google Analytics user type includes both new and returning users, providing a comprehensive overview of your audience.

### Active Users

Finally, active users data (also referred to as just “Users” in GA4) represents the number of people who engaged with your site during a specified date range. This number includes new users.

An active user is any single user who either:

- Had an engaged session. This means they stayed on your page for 10 or more seconds, recorded two or more pageviews, or completed at least one conversion event.
- Triggered the first\_visit event (meaning they’re a new user) or the engagement\_time\_msec parameter (this records user engagement time)

## How to Analyze User Data in GA4

Analyzing Google Analytics user data helps uncover what your visitors engage with, and what keeps them coming back.

Uncover patterns, spot opportunities for improvement, and [optimize your content](https://www.semrush.com/blog/content-optimization-guide/) to turn more visitors into customers. Here are a few ways to do this:

### Analyzing User Events

Analyzing user events allows you to understand if users are taking the actions you want them to take.

Learn how your users interact with your content by clicking “**Reports**” in the left-hand navigation. Then click “**Engagement**” > “**Events**” in the drop-down menu.

![Navigating to “Engagement” > “Events” in GA4 dashboard](https://static.semrush.com/blog/uploads/media/e8/7b/e87b305e9dfd0be02129ad481983fdb4/d1c410d6b500e2027392bd9d4ede433e/FnH-SFRx0LPJhV6FFe1ucqJQ4QgyTBN-EdvewWBYRCAhh84ZX-Oj5BmE01Kcs4oUztP3bECIGdf9DIoXERnbEcQEDFr9NkwmdWL6bUdm54RarjNiMyOUfdrR-ChvDx6NfQjlcH_MPNsWkHjvPrba220.png)

Below the line chart is a table that includes a column for “Total users.” This is where you’ll see a list of all events that occurred during the specified time period and for how many users.

!["Total users" metric highlighted in the Events report in GA4](https://static.semrush.com/blog/uploads/media/61/e6/61e6dc9d2096f265c249446022f4dea0/b6b06428f8d60a44da9772e6df9cca1c/yTuTrA4TeFG2cAFG4yv0ITZ7z088fFsxdLN3wDi4ujbHLtRApEu9JkaQDK5QPlzL_tRdRWd9B0a8ymsNzgd2gD2katBXAfPgZbo_QCi7LxdGyqtuICk-L27KjZcXstNTPJkAudwr2QwRKwhTNShhp3U.png)

Here, learn how your users interact with your site, such as downloading a file, scrolling down the page, playing a video, or submitting a form.

A low number of event counts can help you determine whether to make site changes to encourage certain desired actions.

For example, a low number of “form\_submit” events could mean your sign-up forms aren’t working properly, or your pages aren’t optimized to encourage users to complete them.

### Analyzing User Acquisition Channels

User acquisition data helps you understand how well your search engine optimization (SEO), social media, and other [content marketing strategies](https://www.semrush.com/blog/content-marketing-strategy-guide/) are working.

Identify where new users come from by clicking “**Reports**” in the left-hand navigation. Then click “**Acquisition**” > “**User acquisition**” in the drop-down menu.

![Navigating to “Acquisition” > “User acquisition” in GA4 dashboard](https://static.semrush.com/blog/uploads/media/66/c2/66c2d60c0ce4c5bb57d2f86c0595f651/c8ef7ff91f7369fea1075eb9fcda365c/18wfZ_F8VWCoLwe1HgwdYULTdEjrBK5Y8a8zv418Xd_x3vTz_olLMdibBo09Fm6ViBi9k9hRTdPrJrWKykFD382n3AcKQJ34R_tjqbJfTxKkdrZ97YEby3IdpjhV_NSiQLtjOUeEDeJlkIhHqnJ0YA0.png)

Below the chart, you’ll see a table that includes a column with new user data. This is where you’ll see a list of channels that new users are coming from (such as direct, organic search, and referral), along with corresponding engagement metrics.

!["New users" metric highlighted in the User acquisition report in GA4](https://static.semrush.com/blog/uploads/media/39/7c/397c493f29e38b01eeafa7f0c7e9d661/1c5d4a41bf37a18afeb6d1a66e9dfdc5/lFuxIuUGVMMAnURdijJItbTej_YVTQv84U2YfBWGCiyjyJL1d3jhboBfj7eJJ3NeJBfd7MAQtjcem_CbEn30F5HsdvkG6TYn3ZQr6rYrTyl6IvXVE2L4Ezimki6BB_w42C-0LIFS8tJTYIQYUUeF_vk.png)

For example, if you’re running a social media marketing campaign, you’ll ideally see users arriving at your site through “Organic Social” (or “Paid Social” if you’re running a [paid social](https://www.semrush.com/blog/paid-social/) campaign).

### Analyzing User Engagement Metrics with the Pages and Screens Report

The “Pages and screens” report is great for understanding key user engagement metrics. It can help you determine which pages get the most attention and generate the most conversions. And which ones you might want to update first.

To find this data, click “**Reports**” in the left-hand navigation. Then, click “**Engagement**” > “**Pages and screens**” in the drop-down menu.

![Navigating to “Engagement” > “Pages and screens” in GA4 dashboard](https://static.semrush.com/blog/uploads/media/24/e8/24e8524c4551026afafb9520c1568f5c/25b6ced3ab7013bff921c39f7da444bb/Wg7_2nWs826iz5v62hwydUUAynXpVFXtQsr_kelZ-BM5RueooDslcIdsb6S3w4OGfq6x5ZbV0px1TSgSPbsRiL3f0CW4LwMNZMmdsAWRK0SbePf1P6Ku78Fz_VXZkShsApxucGmOtReOM1L7LwM4WDU.png)

Below the line chart, you’ll see a table of your pages sorted in descending order of most pageviews. You can sort by users instead by clicking the arrow next to the “Users” header at the top.

Notable engagement metrics for these pages include:

- **Views per user**: Average number of pages viewed per user
- **Average engagement time**: Average amount of time the page was in focus in the user’s browser
- **Conversions**: Number of times users triggered a conversion event

![Views per user, average engagement time, and conversions metrics highlighted in the Pages and screens report in GA4](https://static.semrush.com/blog/uploads/media/27/b7/27b73b39d20891b31ca89859351220d7/eea9c6f3df5e2c7c5e525e3718c06e1a/O275aYIN7ql1oo7dGQKq3It2MHP4z0LQYprNm7JpLMKjfnPfAnYzz6ZI6H1Xc1qicHG911EhmGi5Dj0_kmGPQmccfDwO_Y3QSVo-gV59FinSw6DTF60XLsFzsVksRNKbYQFoQgxb7tx17zOXQUWd9uQ.png)

The average for some of these metrics is shown below the header (for others the number shown is the total, like under the “Event count” header). Look for pages with below-average key metrics like average engagement time. These are pages you may consider updating first.

### How to Analyze User Retention Metrics

Analyzing your returning users can help you understand how well you’re building loyalty with your visitors and customers.

Find data on your returning users by clicking “**Reports**” in the left-hand navigation. Then click “**Retention**.”

![Navigating to “Retention” under Reports in GA4 dashboard](https://static.semrush.com/blog/uploads/media/58/89/5889c2347cc9c7713e5c8343950f6de2/6d4ffb71ad9cf924476f435ab9b1df5b/_2rOagoanG0EXlpPSAZUp6Ed6h1rKz-Hv3RYSpsVfAHIRHBi2aHDXym-1qQXTY0CXamWzzEreO7u6nDWTxPmBs9BPe8v7VMw4uE4bp7lySNGNIWTf1iEW7FoBYXfxkbU2lGaaTniiI1ThhnPf7jhHeo.png)

A line chart shows new users as the default display. Click “**Returning users**” to change the chart to show returning users.

![“Returning users” metrics above the retention line chart in GA4](https://static.semrush.com/blog/uploads/media/03/cd/03cd884413711beefeef129a2387b033/0e2b10ec190bf8f4c99f92c6f2dd4f9f/q98O-Q3dOLAQbvw8thU5_z41i0K5SbYYZx_p_UE8dxtqknFf0wue71WiXo0bBhmC1EPv_VwDm3MEI3clD0-wgTWCB1tJKB9MdFEzTtRaEiUebn6jDtthETHfBVjsqIafqOe4gazUoiZtKW--4E6_HNk.png)

The data in this report is somewhat limited compared with the other user metrics.

However, comparing your new users to your returning users can provide insights on how engaging your content is. Ideally, your returning user graph is an upward trend over time as you build customer loyalty.

### Analyzing GA4 User Demographics

You can also use Google Analytics 4 to understand user demographics. This enables you to learn where your users are located and what languages they speak. If you enable Google Signals, you can also learn about their age, gender, and interests (but beware this could result in [data thresholding](https://support.google.com/analytics/answer/9383630?hl=en)).

To find data about your user demographics, click “**Reports**” > “**User**” > “**User attributes**” > “**Overview**.”

![Navigating to “User attributes” > “Overview” in GA4 dashboard](https://static.semrush.com/blog/uploads/media/d6/93/d693216681bfb8419ee1a9b8d65eb4f1/0c98eb94d08bf046fb881ec851c78d7e/gRtN-z5FhuAs9DSz5uo95WzpHKjh_kZfFzJOb6y6k1TA0Y3i7W9hB5n3_IV43VXHoPk5eDqAxR3_kMl_L1dXxstJSttEr_KxRgtddIubYyaLoYXkppXfpvUt-N7nZ6v-FvBcXS808oRPZpiabzGpPJs.png)

This shows an overview of your user demographics, with cards for country, users in the past 30 minutes and their corresponding location, and users by town or city. If you have Google Signals enabled, you may also see data about the gender, interests, and age of your users.

![User attributes overview dashboard in GA4](https://static.semrush.com/blog/uploads/media/7e/0c/7e0c35b4ee272febe90cc4b27be35d39/2cb421b71a7c2b28af3c972b74ce795b/rqaiIr8_PspPzEwna_JHeg5PMqLb6QqdWCljW2Sa8Ky7AINCpgQgKeRs4OghUdQkDk20UC5n-ehyY3tgTi7yTbQs_LGzE6hklpaXN6CvFy953Zjdlr6J9YrWSJR6ES4NJQuJn0T6g1wyRzZoSTQa9UM.png)

For more details about the engagement metrics associated with users in different locations, click “**Demographic details**” in the left-hand menu.

![Navigating to “Demographic details” in GA4 dashboard](https://static.semrush.com/blog/uploads/media/2e/5d/2e5d995278808ecd27911702e461f906/790fbcf77397320a25761995dc321305/htWatnCzV5QBBYUtgxI8vtADIpUFj8X4iv7CdXNBs-8an4oHtMZ72Ku1N-VoFswSiY_CL_teJOa-Ofk2GYRH974pxHS-c0FEppWL-saWo2dXMdxNl6I4RAN-5ek1GN6xf7lXebSKdNiEjIqaNAqNEZ8.png)

This page shows you engagement data with rows for each country your users come from. You can swap this for other user demographic metrics using the drop-down menu at the top left of the table area.

![Demographic details by country dashboard in GA4](https://static.semrush.com/blog/uploads/media/08/93/0893e9daae80bbcb0155eb7016540507/6bcc758c333f5ca48cd63e7eebe1abf1/GmDN24yOeP7SUzWwvg7_3GOCLE_zWzhJJO96vVgerSplBBUWVXjIFvsKdplK5BFlB20VtiwTQMkcjCuMswbay51nblYlU4GNjtIO34923yUHs5AhdrFDY89_9_zXiNBoNcDkCUHDoxaxTf3XU80pS5U.png)

This data can help you understand how well optimized your content is for different segments of your audience. If you notice you’re getting a lot of users from a country that uses a [different search engine](https://www.semrush.com/blog/alternative-search-engines/) for example, you may want to look into optimizing for that search engine.

## Learn More About Your Users with Semrush

If you don’t want to enable Google Signals, or you just want access to other useful user data, Semrush allows you to easily find out key insights about your users Google analytics won’t provide.

Use the [Traffic Analytics](https://www.semrush.com/analytics/traffic/) tool to learn about your audience’s sex, age, socioeconomics, and more. Navigate to the tool and enter your domain in the search bar, then click “**Analyze**.”

You’ll notice this tool is typically used for analyzing competitors. But like many other Semrush tools, it’s fairly versatile, and you can still use it to analyze your own website, too.

!["chewy.com" entered into the Traffic Analytics tool](https://static.semrush.com/blog/uploads/media/32/b8/32b8aa87213b8a06d44cd6449ff67bb7/6e928dcf0855dcc3ec2969fd3154f3e6/IRqgHnRqA1azaahCrG8vp3lQk_fAM_yC_XBp-PcmUbYE0E8m0omsIaZ51vVcP5ksT4LFmID74yCsdBG0GJ1RYRgLtmfmRROeH4gsVgl5C8TGbMMNKOBOAaxyWRkDHpcAn82ctCe9RWj-S0LsIBPUvYw.png)

Click the “**Audience Overview**” tab at the top.

!["Audience Overview" tab highlighted in Traffic Analytics tool](https://static.semrush.com/blog/uploads/media/45/6c/456cc9b238d48726570f3705c9479060/533642bc1d8a8c62e41a451f40d254b9/ndRgDW7lQi3CAd9_WpNYDtVDlDXM01XxbtD57c6l9UE0Y9DhNirrntlnMyZyzpPO9HJeVG1KqqvqWqXlyxZ0YaGH6t18rju8jiweft8n8qS6Pr7D0KAgneBcqoWogW_tCUx3dECRDhaVJ2IgmzNAKV0.png)

You’ll see data about your audience’s demographics, socioeconomics, behavior, and more. This data can help you better understand your audience and inform your content strategy going forward.

If you click “**View full report**” in one of the cards, you’ll be taken to the [One2Target](https://www.semrush.com/analytics/one2target/) dashboard with a more detailed breakdown.

![Audience Overview dashboard in Traffic Analytics tool](https://static.semrush.com/blog/uploads/media/62/67/626768e1dc15e6ba57307ee340108a68/7fcc0deb6562d19bec5da71c8a72c6e1/gMnYwcrDO-cG2Myy8zzpX0EiykXmUpDv1YHFMzTgQeBJoK7i2VMI1Bd3pdP3nRc-vER5Xx0EU6lQautMs6k7p0jMN9Fxq9qCXpNc9InGgltLA9Kz6aMo3w5zZ7he3OBiRhbV9qpT90eEDZWWM6hjKyk.png)

For example, in the “**Behavior**” tab, you can see which social media platforms your users visit most often.

!["Behavior" dashboard in One2Target tool, showing audience's interests, devices, and social media usage](https://static.semrush.com/blog/uploads/media/45/6a/456a84d9bd09e0c1915398c87339f0d2/79e55f7da1af9da037d30af0664d661a/vUm--2auLAok9_bJmPQnO2oajpyuuwXZL5LIQYG05O5EbDGH6QOE48BguhDOituXePVM_5HCkXybFwGktozY1S02uCPdojl8ARtDKP1Ato_Tw0gy1jflZDdGV5AasG-iYXqp4No1_g49N2wcwI_M0ks.png)

This can help you understand where you may want to focus your social media marketing efforts to better engage with your audience.

Access [Traffic Analytics](https://www.semrush.com/analytics/traffic/) alongside 55+ other helpful digital marketing tools with a Semrush subscription.
