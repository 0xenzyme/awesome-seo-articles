---
title: "Pageviews in Google Analytics 4: The Complete Beginner's Guide"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "pageviews"
url: "https://www.semrush.com/blog/pageviews/"
canonical: "https://www.semrush.com/blog/pageviews/"
author: "Aida Knezevic"
published: "2021-03-30T06:34:00+00:00"
updated: "2024-12-12T18:49:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2024_watch"
  - "time_sensitive_title"
schema_genre: "Analytics"
fetched_at: "2026-06-12T18:28:03+00:00"
status_code: 200
html_hash: "f96e7e080a04c666806045c5420df99374c9f9e2642ca899a287038c7612ae3a"
clean_word_count: 2473
clean_char_count: 21032
---
# Pageviews in Google Analytics 4: The Complete Beginner's Guide

As a website owner, tracking pageviews in Google Analytics 4 (GA4) is likely a top priority.

You’ve spent time building your website and optimizing it to ensure a good user experience. Pageview data can help you measure the success of these efforts and identify areas that need improvement.

In this guide, you’ll learn where to find pageview data in GA4 and how to use it to improve your website’s performance.

## What Is a Pageview in Google Analytics 4?

A pageview in GA4 is an event that triggers whenever a user loads a page on your website.

Here’s an example of a pageview report in GA4:

![A pageview report in GA4](https://static.semrush.com/blog/uploads/media/ed/1a/ed1aa65aa17ba17afa471818f519eb25/285d99db1d76d1e81a97947755132afa/AD_4nXeGY4yLpySKDROqvgQJk8LRnm2T7BSsDdmhwrTKTZvhg9EjbGf0GALcgWgbNknnZDDvHXoHmEeHHmX1INct1o-B9WORZgMrtVYPKa6PuDvdIa3Co1HFxgLMolLqgxNOa9TeCRdN.png)

GA4 spells the event as “page\_view.” However, this guide also uses “pageview” without the underscore for better readability.

The pageview event triggers each time the user’s browser loads or reloads a page. GA4 counts each repeated view of the same page.

This event helps identify which pages get the most traffic. It also allows you to compare traffic volumes over time:

![A section of the pageview report in GA4, with dates and comparison metrics highlighted](https://static.semrush.com/blog/uploads/media/38/6f/386fc7a46d85b4429effad6339fbb70e/1742706e086601e1f662d7942483ca54/AD_4nXefgWJa_v2z9XY-v3vvHBkfbJTza25SFEd2N3n_TrTMg_Cw_ykwnR9quG52TiCRELLioWc7c0jHwRscRVq6pKJHetEqF9LIArLNtqBRPAOGTmKoLlMsF5DwnGTFETrkcr5Dq4ZsFg.png)

By comparing pageview data over different periods, you can analyze your SEO efforts, identify traffic trends, and make data-driven decisions.

Keep in mind that pageviews alone don’t provide a complete picture. Combine pageviews with other metrics like conversions and engagement time to get deeper insights.

For example, a page with many pageviews but low engagement or conversion rates may indicate problems with the content or user experience.

***Further reading:***[*Conversion Rate Optimization: 9 Tactics That Work*](https://www.semrush.com/blog/conversion-rate-optimization/)

### GA4 Pageview Event Parameters Explained

GA4 collects additional details about each pageview event, known as event parameters.

[Google states](https://support.google.com/analytics/answer/13675006?hl=en) that event parameters provide “valuable context and details about the interaction.”

GA4 collects the following page\_view event parameters:

- **page\_location**: The page URL
- **page\_referrer**: The previous page’s URL

These parameters provide more context about the visitor’s experience.

Other important GA4 metrics metrics include views, sessions, and users. Read on to learn more about them.

## GA4 Views vs. Sessions vs. Users

GA4 uses several metrics to measure user interactions:

- **Views:** The total number of pageviews and screenviews. This includes repeated views of the same page or screen.
- **Sessions:** A period during which a user engages with your website or app. It starts when a user opens a page and ends after 30 minutes of inactivity.
- **Users:** Individuals who visited your website or app. GA4 focuses on “Active users,” which are users who had an engaged session. An engaged session lasts at least 10 seconds or includes at least one conversion event or at least two pageviews or screenviews.

***Further reading:***[*12 Key Google Analytics Metrics to Track*](https://www.semrush.com/blog/metrics-in-google-analytics/)

## Universal Analytics Pageviews vs. GA4 Views

GA4 and Universal Analytics (UA) differ in many ways, but their core pageview metrics are similar.

In UA, “Pageviews” counted every time a user viewed a **page**, including repeats.

In GA4, “Views” includes **pageviews and screenviews** (for apps). It also counts repeated views.

UA separated app data from website data. GA4 combines both.

This means if you track both a website and an app in GA4, “Views” includes page and screen data.

### Are There Unique Pageviews in GA4?

No, GA4 doesn’t offer a “Unique Pageviews” metric like UA did.

Instead, the “Pages and screens” report in GA4 shows “Views,” “Users,” and “Views per user.”

![The pages and screens report in GA4, with metric column names highlighted](https://static.semrush.com/blog/uploads/media/d0/dd/d0dd684bea0fedfa099fb8b955ef95ad/36587102452c0b008a294c5ff87a5588/AD_4nXdNUBvnjIusAsqZ3D1c1_xS1k9JAOBM8fmhQtXqftiqh-MfNSgiAN6VHDZpJtCTfPv2ZTL14qgGB3_MOhGdG7rvcUqmTh25dRDIYWgGxRdI1APZWpx9r5WRtPR8YepUKgl8uIC-aw.png)

Some marketers use the “Users” metric as a substitute for unique pageviews. “Users” measures the number of unique active users who viewed a given page.

## How to See Pageviews in Google Analytics 4

You can find pageviews using several reports in GA4.

Two common methods are looking at the “Pages and screens” report and the “Events” report.

### 1. Pages and Screens Report

The “Pages and screens” report shows the pages users viewed. If you track an app, this report also shows the screens users viewed.

To access it, click “**Reports**” in the [GA4 dashboard](https://www.semrush.com/blog/google-analytics-dashboard/).

![Navigating to “Reports" in GA4 sidebar](https://static.semrush.com/blog/uploads/media/8e/0c/8e0caa462253ceee5b6dbcb95f53356c/bed9b31a04d11f2a08a9bd6e17e5989e/AD_4nXdo6JK5vipZMCCJaj4G5Nyamr81tGBz49Zu55XoWVzH1UhsRC7XwGznSOSqKCb81jxYEneupr-nSKL26AjgppZUw0C_jdNl-x0VKhmDqzh86_QlNqv34byTt9hFpPz4IraINrp67Q.png)

Then, click “**Life cycle**” > “**Engagement**” > “**Pages and screens**.”

![Navigating to “Pages and screens" in GA4 sidebar](https://static.semrush.com/blog/uploads/media/c5/3c/c53ca12e22d1596cd407e0a172affb7e/89325496ef771963c5d7f601365ca941/AD_4nXd3A95wa1kWRNBq6Rh00hnYC6d-T9ZNAL94N8MdF2iQ5x5ACzbUYmItv-jO8Jl_q3XRBBqmTABV16gFWDtCux1L_GF7o1BlqmFFGKCQsqbfwoP9uAmF68ELWofSSyLe8oI_cu99.png)

This will take you to the “Pages and screens” report.

![A graph section of the pages and screens report in GA4](https://static.semrush.com/blog/uploads/media/bf/c9/bfc97a4f278c7ef780bd4fa1ecd6dce4/a45f389a910ff8c000435014675db7c6/AD_4nXcBDi4sTJPbIyLvFQzItfNawn9rFYGn5xjPLDw7o4vuHJpESrbJ7-aogNRn6_-SJ95KSD467QyD6LELS1fxctdMwMjwu467_VqpVvx2noRJIqB2Jc14ZN-RqfewKQkwNC5KcQWUmw.png)

This report displays a graph and a table with metrics like “Views,” “Users,” and “Views per user.”

The “Views” metric includes both pageviews and screenviews.

![A table section of the pages and screens report in GA4](https://static.semrush.com/blog/uploads/media/dd/9d/dd9deb72e3d0656f819ab115fb9e14cf/d1c32af668f31d46e72e057ef098fcd2/AD_4nXeg0F9Ny_0alUf2hfvovPTkb8xbp7wvCnSfv-NHrTD1uYxopF_soDYnnsDlPNYc98_EbHzbg2Hmys5q51GtvWNe3F3BxYslZVLvWM3CpQb2mu05FUgOOCgwzVzCS-FQkW1f8x3X.png)

Use the search bar to filter the data by specific words or URL paths. Press enter to see only data related to that keyword or path.

![Searching the pages and screens report for "/Google+Redesign/"](https://static.semrush.com/blog/uploads/media/af/d9/afd9626573919b18af0c7722f11d0643/0e73db014858ed1f5812a155afaf9039/AD_4nXf0m3t3vOHtW3RFcr0C7Tirvq_ZLCtAxGcugNzNRyA4WglmJHZsxLFszkdkG1vZa5AnUBQArwCgVAbMLvfXKZAmltgj99S1B2G-D3HkpcIEr1UxhdOxNaE3jdJGnVZXilCWXmbqAQ.png)

### 2. Events Report

The “Events” report shows all events triggered by users, including page\_view events.

This is where you can find the total number of views across all of your site’s pages.

To access it, click “**Reports**” in the GA4 dashboard.

![Navigating to “Reports" in GA4 sidebar](https://static.semrush.com/blog/uploads/media/f2/c5/f2c52004367ffed89dd583eaeb0ff992/5e6c7df59f7ca6a25c75820727b48a8a/AD_4nXdQDMUfhcaTsBK837BJOPtT18Sx_9u8Ew2_2n8yjucvDyxxireLFhCbMfL_VNb4kJkCDXmtDl9JQVHBTdVWkYn2e2e5NniXCGuxUQbj2ZV_p47ovCwimZzMyBFLuW8QULGKZZiZTA.png)

Then, click “**Life cycle**” > “**Engagement**” > “**Events**.”

![Navigating to “Events" in GA4 sidebar](https://static.semrush.com/blog/uploads/media/ab/ba/abbade1d3344ae902643553886f5a27a/5611c8c37e28c16a5311a44162f3f004/AD_4nXfgSbnwuuiTJ7h2yB-ridOR2x1Rf8m8X_Nq9cVaNbEiGYYzEbA7dIVXK9z0lfSRK9aNsxPh1DXxMrwhWQgkQbydd64yikyRAYEH6pT-JRSulIkvjq39RbPAkUfyh9LGyKH-Kl6FkQ.png)

Scroll down to see a table with each event. Click on “**page\_view**” to see pageview-only data.

![A table section of the events report in GA4](https://static.semrush.com/blog/uploads/media/a0/21/a021e95d246fedb867064e5a2cca592b/691a18678d44ede2aec89281a768eeda/AD_4nXcLgScN1eio-8zKdxjOQSMvv4u-xmEIsInLQ8aMjSpkd7lGjbmUrzR-Fu3WCMkVP3Kb42XUUopDTGkOxY9vCqgUHyarPM95TEpirf5duNgcv-l6r9CSwDkis_BSUx-V1vPrFbFF7A.png)

This page\_view report shows how many views your website received over time. You can switch the graph to show “**Total users**” instead of “Views.”

!["Total users" widget showing 29K highlighted under page_view report in GA4](https://static.semrush.com/blog/uploads/media/ff/e4/ffe496994d4e291efd7a5887bdcf02bf/dfdf3c1072f683a44277e2bebf21c2c9/AD_4nXfxLOC2dOWIzmjQO9SZ3IpYcH-OgtSs3HP-9x0LZEjmGXEwpKFQIxBNASHUJEUZ0QEHhiObJ4uqu9H7oIeAP5Gbwfa4Lr19nmxEM24F0-k71a-i8CCb_KIkpmCrUSfiAYGSWXeT.png)

Scroll down to see additional data, such as the geographic distribution of your pageviews.

![A section of the report showing geographical distribution of pageviews](https://static.semrush.com/blog/uploads/media/7a/43/7a4327b9a9b72c9e27055091091340d6/b22ae2fbdb140ec193f448291d921773/AD_4nXfNf_P2j_be1XXr5B9B2ZOgSy0ltsDB2-MAq_VCu3B0JXo38u-pnGqQIDDA0cChLML6-30y2fuq7dwfHwZXoy8VP6_j3-Pa1RfkejXfPmeIzB4VrtCsB2aUBQFl7MsV8C1QwyIiYQ.png)

## How to Use GA4 Views Data to Audit and Grow Your Website Traffic

After finding your GA4 pageviews data, use it to audit your content and identify growth opportunities.

### Identify Your Most Popular Pages

Your most popular pages are pages with a high number of pageviews.

High pageview counts can indicate content that attracts many visitors. Use these insights to guide content creation and updates.

Also consider other metrics, like average engagement time or conversions, to [align your SEO and business goals](https://www.semrush.com/blog/seo-goals/).

!["Average engagement time," and "Conversions" columns highlighted in the page path and screens class report](https://static.semrush.com/blog/uploads/media/0e/e4/0ee495d899af9ba223ee8fd332c672d3/87c3557f4e09fdc89da118c6bc1be2f0/AD_4nXfOfXlzli8fEDB6pca3MD1TvEV_Q_UWFMOm_egHCEHocgek2KERUCnDQUz3NswuTRtDfokZga4XvgUAhjCzg52J2KuoLz2lG15LJ1KJFlRYCYyJ-o1IvTTuhKnaWmiogQAUfZPSfg.png)

A page with many pageviews but low conversions may indicate a user experience issue.

Because “Views” data includes traffic from all channels, it doesn’t provide a channel-specific analysis.

For [SEO strategy](https://www.semrush.com/blog/seo-strategy/) insights, focus on organic traffic.

Use Semrush’s [Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) to analyze your organic traffic.

Enter your domain and click “**Get Insights**.”

![Organic Traffic Insights search bar](https://static.semrush.com/blog/uploads/media/ca/ca/caca938c1554ce6d40ff4218dfa69482/fd6007240f39d77c02fab5558918cef5/AD_4nXeRg35jD1srJ35aY61858SC2DbtOhBL4ED8lphd0evr0BXoZBf9nyog0PwpC9eewTg5zzcmbNAz2ydwu7qC4YrlkH0_T7pbNM9Kt0fYn22_cr1Y6YlfTeKUq3K_xWiyilVfNYR7xw.png)

Connect your GA and Google Search Console accounts to Semrush for a unified dashboard of your organic traffic data and related keywords.

Do this by clicking “**Connect Google Account**” and following the setup instructions.

!["Connect Your Google account" step in Organic Traffic Insights settings](https://static.semrush.com/blog/uploads/media/72/c1/72c19566104b150c1515c81915e8f16a/04877445bf2fa377e5e7676c403c4001/AD_4nXd8vEv6N7kgiL2Dy1ovwLpz9Yk8pRCLk9F7TN2ac27tSBNsjB4Xi0hZP7-ba5w7T27dKGqP2MLXm_m_dwG3GR7kZZIJKuUZWZh2CIr9Hfze32u685nRsEmyjxRCeQxN8GoU_XfH-g.png)

After completing the setup process, look at the “Sessions” column. This section of the report will show you organic traffic data like “Engaged Sessions” and “Average Engagement time.”

!["Sessions" columns highlighted in the "Landing Pages" report in Organic Traffic Insights](https://static.semrush.com/blog/uploads/media/e4/ea/e4ea6e80fa1c78dfd4a002d1be7a2057/d0ecf97584760c2b73625a349b0a5efa/AD_4nXc5GwfVJhp5takrv2LGL6AGeu2g7eaqH0Qa12IMUEA9Vwhtoq0Bi2YxuTw6XaSa9Htnk6ZXTHm26QDCIw7ym7qmVJbf9T_dxgHqTe8cIWxMbkbtqFk53wMOVmiVBG0ABy_ZKKadeg.png)

You can also analyze keyword data in Semrush. Click on the number of keywords to see which queries drive traffic to a specific page.

Because Organic Traffic Insights brings all of your keyword data into one place, you can explore both Semrush and Google Search Console data from one dashboard.

!["Semrush" column highlighted in the "Landing Pages" table](https://static.semrush.com/blog/uploads/media/28/bf/28bfd058b2532265168e75b1c78aa1e0/eb0659d24de431879409ef1630222ce9/AD_4nXd9-udUVe4TmTiThzFpz0lZfEbquwbMGnlEHFxfMG44A0d5SWiWudsMPTbBJUPwjniAP70Sj4tjmmWK8rQ6eEfToWs6M_gUgwCs0m9bMVtTE_UgkrcqVMzXixu5QjWS0yWiHKQunQ.png)

You’ll see a list of the top keywords your page ranks for and its position in search. The dashboard also lists the traffic share for each keyword, indicating the proportion of that page's traffic that comes from specific keywords.

![A list of top keywords, with "Position," and "Traffic Share" columns highlighted](https://static.semrush.com/blog/uploads/media/7c/41/7c415e00a8aaf89bb5f02e7062b6e525/495694158e0702233acd2e87b9a0ae08/AD_4nXcfDV06Vo0MFlLP9MaXR06rzEpT3V8Omsth35VvUYuw95ue4td6Gi2C6gt-Xtb4o2aE-7fduLKer19ECDf12EjJzZL8qslpiC8B_nlI1nloDIA2UTFv0S-y_B4arv47w1WVKXX2fw.png)

Use these insights to optimize your pages for relevant keywords and track their performance over time.

### Find Pages That Are Losing Views

Track pageviews over time to identify pages that are declining in views or traffic. Decide whether to update these pages based on the findings.

Open the “**Pages and screens**” report in GA4. Set a date range and enable the “**Compare**” option to see data from two distinct periods.

![A date range showing "Jan 9 - Feb 5, 2024" in the top right corner](https://static.semrush.com/blog/uploads/media/aa/0a/aa0a4d55600318f62351698d6b552d18/6309130c9565f5b781fe216f3bbf3794/AD_4nXfH_EbBtj6_ZIEDtnHZwCVnE8ksG1VjP7dl2L9uLk9IyrmVTA96NtaPxNLtRgtibNLzs6U7lzt8HdcLOWrbE7YHZniujKIWxinZEermcqBn-5RFMoomFAhYJF47QtODwfZ5B7W0gg.png)

Compare the two data sets to observe changes in pageviews. Use the URL or keyword filters to focus on specific pages.

Adjust the date range as needed. When finished, click “**Apply**.”

![Customize the dates window](https://static.semrush.com/blog/uploads/media/95/11/95116d04a0602e5c29633105a7aece5b/2c4ae4bd5ed5c7363f904fae96c655da/AD_4nXfYpaRybW5pnN-54sPIstpyCCTxiqWpxiVBVn3T8jpDoDe4TpursYYmdRspxiNwgG4Y8Li0WIEEuK3u0jV0MO8d9rb5gek0UIwG7kZIv1IN2HSbsb_DSwCxBGg9nu9dmoVHewMocQ.png)

The dashboard now shows two data sets: dark blue for the most recent period and light blue for the preceding period.

![A graph in pages and screens report containing two data sets, displayed in dark and light blue](https://static.semrush.com/blog/uploads/media/83/08/8308d1ac7b17297bc2323bcb521baea4/ebd8caa9ed4de40a14e8cbf6510b9694/AD_4nXccP10LgJtMvroRR8sKlvLddVm0YJTbxLlfHQlcIGeVbMYIvpFX7V8PiF5Nt8J9IA_YEFDQnoOwpPosalCKLsjXzueHlfhp-FKi7NutDEJQDL4ufoNE5Jq4hIN0MYElbCjNTvVv.png)

Scroll down to the table. Check whether pageviews have increased or decreased compared to the previous period for each page path.

![A table in pages and screens report containing two data sets](https://static.semrush.com/blog/uploads/media/ce/53/ce53c30167bfdbbb901a8a4787da8fa7/c0c486795b1a340e435c3787261e3ed0/AD_4nXfUMthbXK8xoMcATmkYJMMk4crqI4HV5mm7X-R4gtIgS3NwM7TTaM9X-spqE00sIWTk6BlFWrPbQTvjP3qBI2YtIi4QRogDeMytXmMv852hIM1BA8WdRCAIMASd-3jP71HKG_8sTw.png)

Use the search bar to filter views data for a particular page or group of pages.

![Searching for "/Google+Redesign/Apparel" in the report](https://static.semrush.com/blog/uploads/media/ca/29/ca29463a0027739df78f389de88fe50a/3b154def0d610f1a6a66dc582265ed37/AD_4nXcHcETqeCzlmh_aJ4CrTBHVaJv8QTPREB4fNoguLBrTwzTKM-MMHcLR5rYbvj5d74IkNw4VyOfeiiIe_rzmAxRwPJ4ATRubDeu6Stty3aWPreQq3cy_HzEli-UPKmJwzXjMzzzASg.png)

If you prefer to view percentage changes only, click “**Show All Rows**,” then select “**Show % Change**.”

![“Show % Change" option selected under “Show All Rows” drop-down menu](https://static.semrush.com/blog/uploads/media/6e/ad/6eadf50794f6180de6fa731094e058c6/23811712c6259956ccc6e6abb29eb7d9/AD_4nXc0HiYTUQyZelQlOzMR0Hbr2ptYKwJxCvt1LaR09eF5INXSOVH8E0gtdGCgaP3MR1i2M5YJr0rdGprsz65-izuFWXh1fElX1Ykhrw1juwYffik92ffc2JxC5ARowCzdBduk4uHMpQ.png)

This view makes identifying pages that have lost significant traffic easier. For example, a page with a 77.69% decrease in views may need analysis and updates.

Analyze this page to understand the cause of the decline and determine whether updating it’s necessary.

![The second result's "Views" column highlighted, showing a drop of 77.69% in views](https://static.semrush.com/blog/uploads/media/b6/d0/b6d00ddae665168b2c2ec41476a51a67/6eb5bc922198fe3b923ac9c4ae3ab4f6/AD_4nXcjqyOPFFD1arolE82u6kbTDsUgWvbdxXvHWqjT7r4gWd7jEH2Pbtj8izuaG0ddMhHLTJUQZx1KFRUfJ6-QCXg4q9WroPFpZZtMc1IBjWFxnfsA6KdYA7RtAAZ1DIlu4czld1n4fw.png)

After identifying pages to improve, consider using Semrush’s [On Page SEO Checker](https://www.semrush.com/on-page-seo-checker/).

This tool analyzes webpages for SEO weaknesses that might limit search performance. The tool provides tailored recommendations to address these issues and improve traffic.

Enter your [domain name](https://www.semrush.com/blog/changing-domain-name-seo/) and click “**Get Ideas**.” If you’ve used the tool before, click “**+ Create Project**.”

![On Page SEO Checker search bar](https://static.semrush.com/blog/uploads/media/09/be/09be61086d73965ca44c74e99b7b980c/5258cbcfc00e8459208117d8809c9689/AD_4nXdcLsP5CPKj67qdpnC-ldkCPxI8ztgZ8d6qXiINLH1SMSiHlxdXIkdc00TZ89exPjkPfLDWNUUE3Ye1s2JEArveENWzznQdyuopRXzZqh7bUXrt7qR5-zlfpOYh-3XPf5wgZxKsIA.png)

Select your target location and click “**Continue**.”

!["Select target location" window in On Page SEO Checker settings](https://static.semrush.com/blog/uploads/media/73/f5/73f5e204d9ba1d083c626af8c4647e1a/6e76528a209ec9be39dc6a73d626efd6/AD_4nXfwGbuj33dexXe5t0NXXl7RCeLYGxhJsRz7ydOvb24pdHjF9BkGU-43JJWZxQQY7bwDuyHaCcvNBKonnYyCzTuPT8tNJxwMicU79FwCxoryeWny4EFNRR280tUbo3T8nUmt5v5tdg.png)

Add pages to optimize. Semrush can generate a list automatically, or you can import a CSV file or use Google Search Console (GSC) or [Organic Rankings](https://www.semrush.com/analytics/organic/) data.

When ready, click “**Collect ideas**.”

!["Add pages to optimize" window in On Page SEO Checker settings](https://static.semrush.com/blog/uploads/media/25/b9/25b99fa421a5e390eaf5be380f89346e/72ea28c0831aa5f932407cede31269fd/AD_4nXfC3IOYNQEdMLei-3Lchq9RpzE2puizcwQUzmNDUcB470Yhxpw7aYy9isTnV3dvNSi44tK62wd394xRdPUwMH665DvQuuXwqiOwhmq1fqxw01pRXkk7bMeudPUs5GKEnw3Xm_A9CA.png)

When the dashboard is ready, click “**Optimization Ideas**” to explore improvement suggestions.

!["Optimization Ideas" tab highlighted in the On Page SEO Checker](https://static.semrush.com/blog/uploads/media/58/0f/580f41e46239f7a0a1e9274ac99de152/2a2f7fc76010f895c76f7023e3ee94c1/AD_4nXfSVJw4BMtKjcCZtEZTzm0vbKlsomhoim4tJGk1e7n9h_7EZ-zwVwWPdMYk8JGfGZcW33svWKqZCGuQP-1FsIcwovz9NYphD0U2UPlz5VBismspRFeo1RHXU5sQaad_8iTc4GrJ.png)

Click the **blue buttons** in the “All Ideas” column to view optimization suggestions for each page.

!["7 ideas" button highlighted next to "www.nasa.gov" result under the "Optimization Ideas" tab](https://static.semrush.com/blog/uploads/media/73/4c/734c959af9013d0b46be697578845a0f/06dff15b412784e5ebb68b61593be906/AD_4nXemjAuj28thxAXAsGmryJLAGUiisTXif_RLRhKFr25rP5uaoOzBxNir32k8mqmKKj1Rzq-Xnc6amh69Js9sRFs2kJLGYZFpv1Tx5gNQmqciljYaKjGk-f2tJtNjhDakQpIlL1GrQg.png)

For example, suggestions may include improving readability and adding target keywords. Click “**See detailed analysis**” to learn more about each recommendation.

![A section of "Content" suggestions in On Page SEO Checker](https://static.semrush.com/blog/uploads/media/8d/e7/8de7e37ab91312843af70b5460364e75/e6b020b23148129889ef4412c33ac16d/AD_4nXd_kdL8whFKYPqvKhTG8SO_m4k5L7_RgULKxDt3xuRcIujPvrqHGac-3KHudLDYTry4cfmjguw0yIs_xAEzi3S0F4VoFTX6nq8cCDwKmVpHu3fvarrzVLtM1KrY36zcZIwKkgtH4A.png)

Implement these optimization ideas to improve search rankings and attract more visitors to your pages.

## Amplify Your Pageview Analysis with Semrush

Pageview data helps you analyze website performance.

Combine GA4 pageview data with Semrush’s [Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) and [On Page SEO Checker](https://www.semrush.com/on-page-seo-checker/) to gain deeper [SEO insights](https://www.semrush.com/blog/seo-insights/) and optimization ideas.

Sign up for [a free Semrush trial](https://www.semrush.com/signup/get-free-trial/) to access these tools.
