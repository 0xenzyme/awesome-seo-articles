---
title: "What Is Organic Traffic in Google Analytics 4? (+ Analysis Tips)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "organic-traffic-google-analytics"
url: "https://www.semrush.com/blog/organic-traffic-google-analytics/"
canonical: "https://www.semrush.com/blog/organic-traffic-google-analytics/"
author: "Aida Knezevic, Christine Skopec"
published: "2024-01-11T14:51:00+00:00"
updated: "2024-01-11T14:51:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2024_watch"
  - "time_sensitive_title"
schema_genre: "Analytics"
fetched_at: "2026-06-12T18:22:21+00:00"
status_code: 200
html_hash: "3f9e641acee2b03fdfa928a963a0b7aab8bc62ff923d006ef6488cb357aa96a0"
clean_word_count: 4051
clean_char_count: 34390
---
# What Is Organic Traffic in Google Analytics 4? (+ Analysis Tips)

## What Is Organic Traffic in Google Analytics 4?

Organic traffic refers to website visits that come from organic (unpaid) search results.

When someone looks up “how to make vegan pasta” using a search engine and clicks on the link to go to a website, this counts as organic traffic.

The main difference between direct and organic traffic in Google Analytics 4 (GA4) is the referral source.

“A session is processed as direct traffic when no information about the referral source is available, or when the referring source or search term has been configured to be ignored,” [according to Google](https://support.google.com/analytics/answer/11242841#zippy=%2Cin-this-article).

In other words, direct traffic doesn’t have a referral source. But organic traffic does.

GA4 tracks organic traffic from numerous search engines, including Google and Bing. Which you can see in the report below (check the “Session source” column):

![“Session source” column highlighted in GA4 report](https://static.semrush.com/blog/uploads/media/5d/bc/5dbcf998252dd29ace32e077d09ac38b/4ef42017173ac9dced98fc2551923155/n27ue3lOqr4sVa9kVimvb9naDg0uTLHxZs7mKqo7Xf5MmiGkmUv0NGRdsAp6y0gFwhaaQHvwKQvzNyuIOs0Ipkm75JtxPF214aeATJBtx3naAh3iFIlac9Zg5hi8RccNL3iNf7PK4UJBsfOx03wiOp8.png)

[Organic traffic](https://www.semrush.com/blog/organic-traffic/) is important because:

- It increases brand awareness
- It grows conversions like signing up for a newsletter or buying a product
- It allows you to reach a wide audience

Plus, organic traffic is free.

But this comes with a caveat.

You need to first implement [organic SEO](https://www.semrush.com/blog/organic-seo/) techniques—including keyword research, on-page optimization, and much more—to attract organic traffic. And these efforts require time and money if you want to execute them well.

But once you do rank at the top of the search results, you can expect a steady stream of traffic to your website for months or even years. So, your efforts will likely pay off.

### Organic Traffic in GA4 vs. Organic Traffic in Universal Analytics

Universal Analytics (UA) was the previous version of Google Analytics. And it was incredibly popular among marketers.

But on July 1, 2023, all UA properties stopped processing data. This marked the official shift from UA to GA4.

There are many differences between GA4 and UA. And they also apply to organic traffic and metrics you’ll use to analyze it.

Let’s start by comparing the differences between [key metrics in GA4 and UA](https://support.google.com/analytics/answer/11986666?sjid=18284260661175300681-EU#zippy=%2Cin-this-article).

|  |  |
| --- | --- |
| **Users** | UA had just “Total Users” and “New Users.” GA4 includes an “Active Users” metric, which refers to users who had an engaged session on your website—meaning your site was their primary focus. |
| **Pageviews** | UA had “Pageviews” and “Unique Pageviews” as metrics. GA4 only has “Views.” This metric refers to the number of webpages/screens users viewed, including repeat views. |
| **Sessions** | UA measured “Sessions” (a metric that starts when a user opens a page on your site and ends after 30 minutes of inactivity). And all sessions restarted at midnight. (A new session began if a user was using your website at midnight.)  GA4 also uses this metric but doesn’t restart them at midnight. It also doesn’t trigger a new session when it spots new campaign parameters. |
| **Conversions** | UA had “Goals” to track user actions and counted one conversion per session for each goal. So, if a user completed the same goal multiple times during a session, it would count as one conversion.  GA4 uses “Conversion events” to track conversions and will typically count multiple conversions within the same session. |
| **Bounce rate** | In UA, “Bounce rate” refers to the percentage of sessions when users saw only one page and didn’t trigger any other events. Like clicking on a link.  In GA4, this metric refers to sessions that don’t count as engaged sessions. An engaged session lasts more than 10 seconds, creates one or more conversions, or leads to two or more screen or page views. |

There are also significant differences between the user interfaces of UA and GA4.

Here’s what a basic organic traffic report looked like in UA:

![A basic organic traffic report in UA](https://static.semrush.com/blog/uploads/media/ee/92/ee9294cdc045e7e4e6d877b40a7016ba/121654633887c41cc6ce80c16b0365fd/Y4FEXmNr6QtSJfUR9lwq6NINmby5Ixpjgtobpbx1W2koACTpJR2ow1RHi-rGNKT7ZKM4ieDJl8juELBiS7w_kLHYpbHcTRkZdSDRKVj3dw9dSAXeluNZtHwF8Jtce8KjYaL4a5W271kRR9D0_HZeS78.png)

And here’s the corresponding report in GA4:

![A basic organic traffic report in GA4](https://static.semrush.com/blog/uploads/media/cf/3f/cf3fc25d94df1598eb78b49631f0e232/860827146046887f6563d1a1781e1fbe/tiJI94hWQeIyFV6SpCvoCbIx86zKzYvJtyOKlfvQWPmd1hxXOvDa5PaE849Mx4VX5E6uW1DPzxRVBSZNlN8aSxn5ciY0gNgsKpgb0QmD0vRE7yiUoWrXY-Ryh5vn5o7n6Mw31yaup4XjUUbmcLXRn94.png)

If you’re used to UA, it might take a bit of a learning curve to become comfortable with the reports in GA4.

Let’s start by going over where to find the correct traffic report in GA4. And how to isolate organic search traffic.

## How to Find Organic Traffic in Google Analytics 4

To find organic search traffic metrics in Google Analytics 4, go to the main dashboard and click on “**Reports**” in the left-hand menu.

![“Reports” selected in the GA4 left-hand menu](https://static.semrush.com/blog/uploads/media/f9/0b/f90b92781aa711965197cf6e34ac7aac/7dd783b315e87a59da60981953283528/Uk2jFQZ1gOUI9vDv7t4x-a3M_IBD6PUf6sarflEcUWcx9P8G6iyrOwJF7cNIn3F5bKhzSy-VcGqia0cyelMQDtzDfB5-KHbY2uO4kw0hDPMHnmrn9RixxnwKIQ32JMRWsWiIcOe5AT-CO9U5Vl3wMEU.png)

This will take you to a “Reports snapshot” dashboard.

Next, go to the “Life cycle” section, then click “**Acquisition**” > “**Traffic acquisition**.”

![“Traffic acquisition" selected from the GA4 menu](https://static.semrush.com/blog/uploads/media/7a/1f/7a1f533354011abd72e529ee3f651cc2/4b6079d6a7d8348879318a6ab9c13f34/mM33z6XRaGFJ1LCKQx9xyYchOYshxaBBFJg1q0pAVnObjA2ErsFusMdbo-KCDXIjtTSBzpGBluC7_EmSjOjMb-O6Ql6lAfvISwQCbypt_tV7zL8jKHFaReWLBvWJUBSnW_1vfGMCjUL0fMv8-7d0DYY.png)

The “Traffic acquisition” report contains all the data on your website traffic. Including traffic from organic search, direct, and organic social.

![Traffic acquisition report in GA4](https://static.semrush.com/blog/uploads/media/24/9e/249e943afe85f816379106805a7865aa/661da57f3b83cbfb9af02330e11dc4ef/Gkj1kjUUMK4LvNf2VBapYwV2zVSKBc4U5DHpTaiZa_u2sOMb0LyMXTThbBhVKZKOWDoOxk8VSUax719ZnlcC8V72Etp7ztYfBjZuDR0axBjIz9Wyh2qd1PWZl-ouNyVO7Fmw3EUO1CpOuMwAmTg2Gwo.png)

When you scroll down, you’ll see more traffic data broken down by channel.

![Traffic data broken down by channel](https://static.semrush.com/blog/uploads/media/f0/01/f001b6d596b139ef866736ef22a410cf/fa80194382d2933f283e47d3ab2a9c1f/mOFB0zscZTsdyVCtgtir6utQuMNB7lufDQa86ZGeoSp7lgCM4D3Pdpy7BPMhCLW4zd4Y7PgcP50lI5BC-AFH28xTV9auUVVji1Uwl7zjENBgERq5RjEpefeaWkpSpGcOM7WNVJ3tTVmzGuBIoSzfZ_o.png)

From here, we need to apply a filter to isolate organic search traffic. This is an important step because it allows you to apply additional filters later on that will consider **only** organic traffic data.

Click on “**Add filter +**,” which will pull up the “Build filter” menu.

![“Build filter” box opened in GA4](https://static.semrush.com/blog/uploads/media/94/7b/947bda3507195197ada701157e148c62/5a28d7b81030c5ccf3b62557cb27e2ec/n75zEN1A8Khcxzs32HZCD6uiRC5xtrhWxK99tPwohmJuEo4RJNycUUX3aB4ZCWzHKvDgxVKKTh3q_Wi8wJXpEdI03LHEo26gHmMKJH8p6tRSRTNuiwkRInTK_a5c1BVBFst3jJYUccN65eIZ0Jew3Y8.png)

Then, set the following conditions:

- Select “**Session default channel group**” under “Dimension”
- Select “**exactly matches**” under “Match Type”
- Select “**Organic Search**” under “Value”

Then, click “**Apply**” to filter the report.

![Applying the filter to isolate organic search traffic data](https://static.semrush.com/blog/uploads/media/59/c0/59c0ed23228a44dd05192ad690d7bc7d/f76a32f35fc1ac2968c8044d5b4b3f04/8U76zGot1dFSCK3FUl-06cknudKOTlSmMddnS5XOgs_d0APfB8692n3Hi3xD5ibvmX7pPgD4y7QDZk6AJgWJmHQGz-7TT_gBVqEkM4SG2AcTzNroieEVVaAfnyK2bCyXl5rxFZnI_sNdj58O6WQnGTk.png)

Now, you’ve successfully isolated your website’s organic search traffic data. And the report will look something like this:

![Traffic acquisition report showing organic search traffic data only](https://static.semrush.com/blog/uploads/media/0e/63/0e639c0afddcad493ce65e07a1b23de5/c0de8ccce5d1ac39ca8fc72504dedf92/hajTmOkel1o4hTyS8GfOoWVx9iBcWqOQNtLwMzqSwg6e_NI8vuCzR2JIRHbno8qhG7zoEam24qMDGxrvADO6GD_C2lmhvTgDuyy5WFgLD5bOO0XZltz63hf05q0l9nHdLKvN2ccpSQWRtASWQA-Zzk4.png)

This is a basic report that doesn’t give you any in-depth insights. So, you need to use additional features to analyze the data. We’ll cover this next.

## How to Analyze Organic Traffic Data in GA4 with Dimensions and Metrics

In GA4, dimensions refer to data attributes like geographical location or the landing page of a user session. You can use these dimensions to display more information about your organic traffic.

Before following along with the examples below, make sure to complete the steps in the previous section so you’re only analyzing organic traffic data.

### 1. Identify Your Top-Performing Pages

GA4 allows you to find which pages on your website are receiving the most traffic from organic search.

We can do this using the “Landing page” dimension. This will break down the report into rows showing which pages users first visit during their sessions.

Here’s how to find your top landing pages.

In the traffic acquisition report, scroll down to the table and click on the “**+**” next to “Session default channel group.”

![“+” button highlighted in the traffic acquisition report](https://static.semrush.com/blog/uploads/media/2f/13/2f13aaad4b2cdd6655a22f9a4d795b50/74e42044e9e726d891cb6b423f7f935f/sRM1_kqRohPrzz1Qdxqgre0NAA9rCePIdBehotp3Pc0sdGLNs8qPVFmE3BjCWzcwvdu--32rlGbsG8NP7302HIMEbCCubVqMdBvlQSAgdXOy3fqh4q2M4gi-xbJIU0LYya8ckrZGpqgRkaoUzEKRjuI.png)

Click on “**Page / screen**” > “**Landing page + query string**.”

![“Landing page + query string" button selected](https://static.semrush.com/blog/uploads/media/b4/0d/b40d43c776dfc38250fd521f527ea6a1/1e22b0507cf659bc23762ae08fb3688f/wimFVW9fV644gqMR909NQo5m6DIXFzIC9h8SP_IpNhJXAn_nT36hoeDErD-kLeBltUBTyG5uwXMGwpsHbG_9c70kfHpUltDPnW0t4ao_LFBvLSIB0VSLKFjOM1MdwC4MJSZQbMVXtIQ_R5J0_Hzmuiw.png)

You’ll now see a list of your most visited pages from organic search.

The report orders the pages according to the number of users. (Note the arrow next to “Users.”)

![Pages ordered according to the number of users in traffic acquisition report](https://static.semrush.com/blog/uploads/media/1e/eb/1eeb4144667bda89801f56108de8ff9b/2b504458af9b55b1a8639f50fe96f824/k2u81CvP-o7BePMNb29fr7Iwn0oZTE-k1CzuUkQR1fhGSKI7cUOP7hHx2owgeAKn6_0wXDWXsqpkFB5a8RiqUzX5fWmLZEj6-QnuKSi0ClLH5v-98YAzSJaid-INC5jSnHNsa8uuYTRruLriIgLSXy0.png)

You can order them based on other columns. Like by clicking “**Sessions**.”

![“Sessions" column highlighted in the traffic acquisition report](https://static.semrush.com/blog/uploads/media/70/bb/70bbd940875b82c1ab12a63297c86b32/3ee379fed3dab8cb453800c7490d1727/7aRURKlN5vLG2us1SrwtHlmItqdHo0pLG9ia530EypXATjste-_t4P4y231F2ixvi7K9EQmHCcqGbIOmvnj3ZsoP-D5lZ5TopVFPU713z_Xmz3QIef80vifF-KSgsBX2xb_LbaRq0X_ZIXmOFaibgWk.png)

You can also export this report (and any others you generate) by clicking the share button in the top-right corner.

![Share button highlighted in the top-right corner of the report](https://static.semrush.com/blog/uploads/media/ab/db/abdbe79d268a4618870a25f5b1cb8199/1d4806f6b7bb5dd606accd8ab88e142e/vcUT2GB1RXD8ej-_XAeHLnZUUoaFe6wYNDgkGxnyxYmMPtPp_QhH0dINm6Qi99s5QJ4VV8rAFlSUBjlqI7Vb8MJXgLsvkJpOwr7KObPEAck4_TqFN6xPHJB6fbd7-9TB1vhX_MzW_NnFer1xzXwZl7Q.png)

Click “**Download File.**”

!["Download File" option selected under "Share this report" window](https://static.semrush.com/blog/uploads/media/16/b8/16b8ad6345c07b4acadfb99478be2090/aceb59a4eca2682211ec42efeb6b84d7/B4M781mun-nFPNtzUgUs3Rsm0uyrr3XSc9Bl0CCxdBRYBr9-BjsVCnlF6Z8yeeO8cr9z6mmTaUxPwc0mfeoORVR-RFUjb017GPKvCTrEBEYD090fv469NmiXLJMBgi9HIgejEA8ZjcRPOPc15NAXc2s.png)

Then, choose your preferred file format.

![Select export format window](https://static.semrush.com/blog/uploads/media/4b/a6/4ba69cf713ff5e3ec08ac61991a61653/6d85afbf9a277b86a301699fcbe61111/xF6As3IiqwFXquRGSzasSL_-Uu5rExQg8LgpSQg-QzIRSDx5aW1PG3dfMe74mS4_NX-wkFIgBzZC6m29ev20JM6X032ET3_mhX85XbHbyNCE5wzTXClRvj-qMkPSFym9wMWj0tIKcNbEGmgpAhVW14E.png)

### 2. Measure Organic Traffic Changes Over Time

In GA4, you can compare organic traffic data from different periods.

This helps you understand how pages have performed in search over time. And you can see if some are experiencing a traffic increase or decrease.

Many marketers analyze this data to see whether a page is due for a refresh. And to report on the progress of their SEO efforts.

You can also use this feature to find out if a Google search algorithm update has impacted your website.

To analyze this data, click the date tab in the upper right corner.

![Date tab highlighted in the upper right corner](https://static.semrush.com/blog/uploads/media/c1/b3/c1b376ab2b83dc390afce77d2026045a/fc995d67f8822b7bbd7fa54a2d295ebd/7NnoWNPyrKFt39Z78hPTcRfSveXDkQR5dmj4BcjjOxAEx49YCUy7izeuwkFy9vrPIaVf7gHogMYe5LmyIrdIfnPTcFIBAQZ2s8rfLlnB-GBUI45KD1SzbWZJaT39xsXAoMbN6Crv2sf268jXjXwGrzE.png)

Turn on the “**Compare**” option and select the periods you want to compare. GA will automatically suggest a couple of options, but you can also customize the selection.

When you’ve chosen your dates, click “**Apply**.”

![Select the dates you want to compare in your report](https://static.semrush.com/blog/uploads/media/81/79/81791305ddb3e9584acc3b019cfbc2ff/b4af784ddbf21445e9fe7390c5076e14/SHXA-wD2G0m8SrT8cap80afqFDehngHEGEmggvrPcRWw_L8ldwUGHhuUbvEPpZa0jsi2CiZ_cEp1--qBz3OnTgp6kjMM4NpZh-ty7Ah3hl_jPHTdg8AIvD_N4Kvt-A9PGWoa-MIjx1dwbKDpYjn3iq4.png)

The new report includes data from both periods. Any increases or decreases are expressed in percentages.

![Traffic acquisition report comparing the data for two periods](https://static.semrush.com/blog/uploads/media/e4/a1/e4a15b94ac35aa4489bd1470e63ca041/fa7a11ecc236c68547333c721a34da47/1v64wIVHim4WRvIvX_fo6lMfz5dgS8X1dvuijw6825pCVkEAv8HPIbKZL1r6_xOAyPKeffSHQ8haN7S9PL1ilDeYiJWQADaAj51dWx5wRFMA37Yx4WFPo2h_iwc51p4Y6FRVoQ1v8xtR3dwdBK3QyVE.png)

But what if you’re only interested in data on a specific page or a subset of pages?

In that case, enter the URL slug into the search bar.

!["/Google+Redesign/" slug entered into the search bar](https://static.semrush.com/blog/uploads/media/fc/c9/fcc9747db4f7cbf62869284556569ba9/557d357910d42010e3e3eca8e1d56798/Jr2rE7Q_OE-ekaj9i2pHR9e_RgCyM62Y_zPozMSq-lRp2ZWPcN2Js9ZYok8pjbG0xfnQp3_g_5jbxBBawbqi3prQ4SCrNoBzSVQ4HM2hHbD9NVWXVP9S8dVuGs2DJa-FlnAE9hlEux8qxWMUObb_P5M.png)

The report will now display only the data for this group of pages. So you can easily pull data on the organic traffic performance of your blog, product pages, or any other part of your website.

### 3. Understand Your Visitors’ Locations

GA4 collects user location data, which allows you to see where your website visitors are coming from.

By analyzing this data, you’ll notice if your brand is getting more attention in some locations. Then, you can launch more paid ads targeting people in that area or create content that speaks to their interests.

Here’s how to filter your organic traffic data by location.

Click on the “**+**” next to “Session default channel group.”

![“+” button highlighted next to “Session default channel group"](https://static.semrush.com/blog/uploads/media/67/88/67882f4ad6bcc9e3e8de3b5bc4798c43/791ab77685668d73cb640e5bc829a75d/scUdsI11r4PZV-yeJcBK0owgag4ank_WkPmQIozKB-ffJEwHrNy63VcLx8ANgitEspZmWCix2zQPx4VvYiIaKPfd5_2EL1eAFRLlmSrIzSDy-iiDY55H06D7hM8ZDaTTXB5JwU2hU9ZSh09BT5VdHX8.png)

Click “**Geography**,” then select one of the three options. For this example, we’ll use “**Country**.”

![“Country" selected in the "Geography" window](https://static.semrush.com/blog/uploads/media/8c/10/8c107dcf6d3ce6fd50ba6fee473f7e70/2ea38120c419cf0f93b8b837ec7759e7/xU4fM6hq81xpdRAvxmtDo3t_BEqq28Lbu9alHUhnjsBAt1_FmRuYzMFiHNCOAy3Yi45ZLcclV5jRH_oVMu_3ZqONJzBNX9vtbA0Ug3XlAkGY0tnOKuVbcDltPKBpVAETSsUBobAxEtKDCPA95SyVAUo.png)

The report will display all the countries where users visited your website via organic search.

You can use metrics like “Engaged sessions” and “Average engagement time per session” to analyze how visitors in different locations respond to your website.

GA counts a session as engaged if it lasts more than 10 seconds, includes a conversion, or has a minimum of two page views. Average engagement time measures how long your website was the main focus of a visitor’s browser.

![“Engaged sessions” and “Average engagement time per session” columns highlighted in the report](https://static.semrush.com/blog/uploads/media/c1/ba/c1ba8b2dbe42cb6df6ce6f8af7d5f225/1e98d6a6b61e0238c2ea676736906c57/b7d9kxI8zgWdLSZwO67OjWDsr-OvkLFurbXQzT0si8dt9gK0dMG8Xz_jq02IShvGq7ciwKUY-GgeU9m9uJruuqGp78h5LqR8KCyFJljZyw6sMVw13GqiG8gOCR5-mi7CY-fQ3M2xPILuJwgcHQP5-D4.png)

We can take this analysis one step further.

Let’s say you want to see which landing pages get the most organic traffic in Canada.

Here’s how to find this data.

Scroll to the top of the report and click on the first filter we applied to isolate organic traffic: “**Session default channel group exactly matches ‘Organic Search’**.”

![“Session default channel group exactly matches ‘Organic Search’” filter selected](https://static.semrush.com/blog/uploads/media/3f/dc/3fdc0bb0a6ca85d75b1ccd4c66cd9dbb/1aee698919cf1d88d531e736bcfc689d/QaRRabqcgzKPu9gWDlHM3K9Q2ocyFSfXmwfH6I11hbmYYOEP3T8-SA7U73mrSvGf0XgQ_fpZtMyuwdgU_41s2z0DJlYOm7j8-TLn6aywt8Kz_TUI4RsMATIIWJfCeObBhDM1XUDJ_Vxv5Un3wBQUbiU.png)

We need to expand this filter and isolate organic traffic from Canada. To do so, click “**+****Add new condition**.”

![Add new condition under "Build filter" window](https://static.semrush.com/blog/uploads/media/87/20/87202876b232f46cfa710904fd5744ec/903e43c72ca2b891cbf9a1ca523ec57c/6XzWOQYk0AnHdbMksW7YBbwHKO5cZPpUNBoQUQEzZSJJehBmior4YkjQ5nvmqBDxIazDRVI3O3JGVD21ngw0BrshdDTHxOvvS-givqHmi8YEFkTjQs1xzJsgebW3LVhkzbhx2RaxoCbl-5r0zKUciZU.png)

Then, we select the following:

- Choose “**Country**” under “Dimension”
- Choose “**exactly matches**” under “Match Type”
- Choose “**Canada**” under “Value”

And click “**Apply**.”

![Adjust filter to include the organic traffic from Canada](https://static.semrush.com/blog/uploads/media/69/f5/69f5628c32e2461d970999a6f987edc7/d2435f2abcb31203deda3ea9c3af9de2/ekuaReQmKxdyEuuhAlk2XUl3EEdl5FyeHGANOzU5vX9ao-QJLKS3tfwtLAjCZWM01GSO5lLY1IbeoiAhwrVxIiT1MXx0qL3Lj7aKxV3Y9xCLIdulFQKV8aWIa9Zz7a0v6L73GLRwUI8dWNaXX20EiZQ.png)

Now, scroll to the bottom of the report and apply a dimension filter by clicking “**Page / screen**” > “**Landing page + query string**.” (You’ll need to remove the “Country” column from earlier by clicking the “**X**” next to it.)

![“Landing page + query string” selected from the "Page / screen" box](https://static.semrush.com/blog/uploads/media/7e/34/7e345b0ea625f804e3cd35236b75e4b0/1b8b9004f93a195229c383c0e0bd97a7/Ener6eBP-pHN2K6GeuU5uT7nzq7zj99wa4_NF3vMWYnb_hAt7PKNHG5ymA--ga6cVXfwFrZRTxqfv9fAhGindJ1wPM65Vtq9L2gpiv4fyGTLm3akGsUXb_r1r_oNMp1BoNdcxhAKK3CmSnrmjSd74AA.png)

The finished report displays only the top landing pages in Canada.

![Traffic acquisition report showing only top landing pages in Canada](https://static.semrush.com/blog/uploads/media/00/a4/00a44031e7e124038bace4cfb75bbe49/1ae5f51ce8a97851a5b11c17ecf7c783/AFBnV-3MQexuI7coNXfn6TmVgfFBuYEDI2MBh_-TBF-f2yv9eD7UwVYWDhWGjbyjYrF8eEEi1S_QQ3mUO_cFZkCov3cDxrtvH-CntoL9dHZQwyKyv-k-Mfw90euJc12ggxyF6ccBJDJ7WYS9Ds4Nk6Y.png)

### 4. Measure How Organic Traffic Impacts Conversions

As any marketer will tell you, measuring the impact of organic traffic on conversions is essential to proving the value of your marketing efforts.

For example, you might want to know which pages drive a particular type of conversion from organic traffic.

Scroll down to the table in the report and set the secondary dimension to “**Page / screen**” > “**Landing page + query string**.”

![Setting the secondary dimension to “Page / screen” > “Landing page + query string"](https://static.semrush.com/blog/uploads/media/65/c4/65c4a9d34c1cf9c818051809ad0b572a/b166846522c1b9bcbb19328b8c9bd07f/O_oQUA2z3daqIDR0etwgYeWyVvN8ZdiXyyO-x0iqsheBPWru5DMef1PPLBYnU2kxRSNg1fEc3VozFuHYafsPsbNKx0XGwlkRlIWFIXV0Fzo-ct96wN1LlXNOgROAZ4pXMmDNC9_pK-TMT8IDO1xRkZg.png)

Then, find the “Conversions” column by scrolling to the right.

![“Conversions” column highlighted in the traffic acquisition report](https://static.semrush.com/blog/uploads/media/53/4b/534bb3737388d00274d2e1eb4d94e40a/99788c22490fee5f8a379d0821bbd2fe/OTYWkLC68PyrlsJRpaewuWtYk1iBDHcPEAFQrXwMI-JsvlbcoAS6kSF9n2i9EpkAJ4_xmOvQfRCy1iAS_6DzIS-M9GhmH5fhsuHix1e1gqQt4cOmPtVwy0hhQKdDLikLSWE-GZA709SQpZNjTQnmU9M.png)

Under “Conversions,” click “**All events**.” Then, select the event you want to pull up the data for. Such as “**view\_item**.”

![“view_item" selected from the events list](https://static.semrush.com/blog/uploads/media/51/9c/519c5fe8b7156fe0fdad5cb07a220842/d777bd1600a76381a084212700c1a20b/MsAX34ITolwpxbN1eP6sT4WQvsrRyUAWe4TjgkO_-C-r5WSRYWghuLGZSwlmsao_rN2QBR5YyysQavLPrOjRn9ym3OMy9-iDGMf1D3uLAjnSnmv0yuRtLofFwMTsw66tSO5YCZrb2R-U7J50yWPoqTo.png)

The table will display how many “view\_item” conversion events were driven by organic visits to specific landing pages.

![A report showing how many “view_item” conversion events are driven by organic visits](https://static.semrush.com/blog/uploads/media/80/2a/802a174533ec7045ecc71f4e95a0a642/d3c45b007bed709f9d2f9ae1686fc722/UxS1Or4LO9k6kktAC3XW_kRUDfAUPyPmaV_-zSbRD9UU4iy0KR9c4jidtfSf0TaTGNQty_Qv8UxCwHmQnQJ7tol9bncS4y8rqjNe8By_tubNghWp8wGhSaXPZWS0V-6tQD2r6e1Q9h0-8p7F_h_tw_0.png)

### 5. Discover Keywords That Drive Organic Traffic

When you connect your GA4 account to Google Search Console (GSC), you can see which keywords send users to your website.

You can follow Google’s documentation on [integrating GSC with GA4](https://support.google.com/analytics/answer/10737381?hl=en&sjid=1516520254681804131-NC) to link your accounts.

Now, it’s time to add your GSC data to a GA4 report that you can easily access.

Open GA and click on “**Reports**.”

![“Reports" selected from the GA4 menu](https://static.semrush.com/blog/uploads/media/e8/cc/e8ccd1bcfadd363c4523b66a6c806376/03f64b4a184c09698cf0c7325a142213/XTMOjwSZjXDr0DSJ4v7Q3vYuDL2kzRxMks60RYkrSCqzfx9BMuCm_IsnbT8OcOC_giA8X82JAMocPmU7_njUtXLixZUGCkSt_iatRFRLIzPtnXe3rx7EnhfLA2vGdwIpB66DGFCgIIV8OXcP4k9Kp2c.png)

Then, go to “**Library**.”

![Navigating to "Library" in GA4 menu](https://static.semrush.com/blog/uploads/media/ff/f8/fff8e218b5a0baaebf0954019a65b951/eec7cd3db19a744182f807c5f65cc166/osYyKBUsyZ-telNnQnXINNZjLTvXvYdhLdlD-SAdyeTyDlo4xJzQnrIcxySBdHEryXU_2zhO-MbUaOy2qvUTVv1OQcaW-qWHVdiK6810aSK887sgvxQGgXUGL1StolxDF-WHxCkzllxj8hfBMD7AKr0.png)

Find “Search Console” in the “Collections” section.

![“Search Console” box selected from the “Collections” section](https://static.semrush.com/blog/uploads/media/c3/e3/c3e3044965c30246ff8dfb0a89f8eca4/73df5b9e2e3acc789170e39ee795d6de/meRDira-RR7jiGpC6c8epAKClHaS_TCkc37BGREjEHAKnJ1DAPrVSG4ShMKPL2_elcTvwkUR2nqiO8aulHlD8MM3fTvGx19Q1EFBbuKZBbLGz5tBQsDo6H-eFOHAGwFnEDQ1Wf97DWtAICuL_CSAOQM.png)

Click on the three-dot icon to open the menu. Then click “**Publish**.”

![“Publish" button selected from the drop-down menu](https://static.semrush.com/blog/uploads/media/ee/7c/ee7c3c59d829e0fdc17d714cf17e18f7/2451a6589ed1fb1a28f1af26233a8aff/95FahnS-AdmVM9F3_XQIaPqyCb9G-5rGWM1rEvdY_3kVT8zYg3Va9i3MqQYiMQgGZdebwcTpjMNboH_7sZdM5KxRMx-0Dy8GlpmAD6F2c2gaDlHZxb1JOVzZmFLXPCBnuoNJkq09Sy7eYVYiUvZLvzI.png)

The “Search Console” report should immediately appear in the left-hand menu.

![“Search Console” highlighted in the left-hand menu](https://static.semrush.com/blog/uploads/media/c5/a7/c5a77655bb1335b39ca7b734621fd1dd/30f1b2a673bec5d2e6b4c899808d785b/f9RJTenuwLauUWC7ybmN9ungCcnLheLvdrS2N0ptCyfUGKvY800Tamh1_oET6LMbyZoKbtqAMeq0xYYSn8IUwPAo_NdoGK1oXfha_26O8bwid6WnWIbBCO8EzZIFUnOJLWf0VLyN_BVARLA5rXgQWcc.png)

Finally, we can click on “**Search Console**” > “**Queries**” to see all the search queries that led users to your website.

![“Search Console” > “Queries” highlighted in the menu](https://static.semrush.com/blog/uploads/media/d0/68/d068507064eacb7e44bb778a852f24c7/4f6bc4742cd3288c62329ed8d54a0045/e9eZdfo_szXpWrcDLhuvL7bjUacpApoFT1yYvdedQ-DP9HBFa7a8dR9lNzFmjPI5SYt3a_b4MdLA7MX17sleQ0M95OZp_2Xq3xo99sD_q8BFfxHdvYeux8hCFqgsN1PBM6oxYsjzLZAx4k8H9vmTclw.png)

The report displays clicks from Google Search over time. And a chart containing the top queries.

![A report overview showing clicks from Google Search over time](https://static.semrush.com/blog/uploads/media/d7/f4/d7f4f7a3041a2e301cf1a60e758ed5c4/502f6a737958b767bb61092cf5779c8c/KohYLCklDENMytoNm4wu4v5Hm78luWq1VI7dR1tZ5MaCismrXY62qTQ6kC9bP2T0OhsZdv3-eFviZTHsyUns24fVaODwZZcZOgSEACm9VjHh2UPoWbyumQV6JM6axx22wK8UAodRjmROzNjFXsVpsLE.png)

Scroll down to discover the complete query list and metrics associated with each. Including clicks, impressions, and click-through rate.

![Organic Google Search query report overview](https://static.semrush.com/blog/uploads/media/9f/64/9f6415296f43ec26a863e4008e9972cf/113b21cb92714056020acbea0832e3b2/8mi_A2700JiWfcgSQAqxTx6Z6BNcYpWm9kVeyVA86AI3XC18IDU3h8QiAodY-bP15wFcPyCJjYU2j7f_cyeZLMOZIbfwJ-oTxpoMOHZ8lO7qGF9GGe-cclwcfHEWF0hV_Rd8qACy7SvEgA7t2MNkzgg.png)

These queries can help you better measure the success of your SEO efforts. And also serve as great starting points for additional keyword research.

## How to Improve Your SEO with Insights from Organic Traffic

Organic traffic data allows you to analyze your SEO performance and find ways to improve.

Here’s how:

### Create More High-Performing Content

Organic traffic data from GA4 helps you identify which types of content attract the most visitors or engaged sessions. And then create similar content to attract even more visitors.

This [SEO technique](https://www.semrush.com/blog/seo-techniques/) allows you to quickly come up with new content ideas.

For example, consider adding more guides to your content calendar if the top 10 pages on your blog are mostly in-depth guides.

Another way to find content ideas tailored to your audience is through competitor research—a popular [tip for improving SEO](https://www.semrush.com/blog/seo-tips/) that also uses organic traffic.

Although you can’t access a competitor’s GA account to see their traffic data, you can use a tool like [Organic Rankings](https://www.semrush.com/analytics/organic/) to find their top-performing pages.

Enter your competitor’s website URL into the search bar, select your location, and click “**Search**.”

!["nasa.gov" entered into the Organic Rankings search bar](https://static.semrush.com/blog/uploads/media/8c/2d/8c2d752edd63b01fdc5be593b111cdf8/c966916b6a11a6c53b1a28caafe2a794/Deb44Vl_9568fS3RqGNHaI5Dsn2QEghDTEaWVeAcQSWJ1l1_RYsOAjb8VBdv2D-aNadcEPaW2HxNmH5AVuEC_khrLC8oArZmnEO8GNAbinlCPfivFtDskX3dBgbhL-i29GgJqs2OV1CX-dr7_dO-Nns.png)

Click on the “**Pages**” tab.

!["Pages" tab selected in the Organic Rankings tool](https://static.semrush.com/blog/uploads/media/96/49/964985d11909410f9d066c90c6c5e82c/1da092b6eb819cdf70c72e255e144550/xLhs6F4xBTH5qe1w0vgCs4y4zwdmyfBGm2Yl3vj0C_Vd0ys4ub1h8p9uJTeezWeS66_qTnFN553hxCZBdY6Ry0RA6fCA9ux38vw1gyNGwiaysQvWu7fnlvT6VA9mzt6FX8mMrVXH7OXjHWtGjy0PeWs.png)

Now, you can see which competitor pages get the most organic traffic.

![Organic Pages report in the Organic Rankings tool](https://static.semrush.com/blog/uploads/media/e7/eb/e7eba60c9c0c2d67026bffe2a2061d78/2fa586de571e7ce8a234fd0d874251a9/QdEFxXXwV_ZM22O-Bqyb_DvBDPZx8FGKON-cD28E1D8a7N13DrrXh6_nBlz9f4SFe5WduzWOI_EXc1igSFi7ZRgBE60KkcCUICW4cHIfRxScTSkCE8HEU7ZF_yXIjE-dW09v9OpWbJmDQ3jBxg0thZo.png)

Analyze each page to understand what contributes to its performance. Maybe your competitor is using original research, images, or even videos to elevate its content.

If you choose to cover one of these topics, remember that it’s not enough just to mimic your competitor’s content. (Without plagiarizing, of course.) Offer original insights or a unique take.

This will help you create [quality content](https://www.semrush.com/blog/quality-content/) and increase organic traffic.

### Identify Pages That Need Updating

GA4 enables you to easily discover which pages have been losing organic traffic. When you combine this with keyword ranking data, you can pinpoint pages that could be due for a refresh.

It’s important to use keyword ranking data whenever you’re identifying pages to update. Because a page could see less traffic for different reasons.

For example, some keywords could have a higher search volume during certain times of the year. So, the decreased traffic could be caused by a lower search volume and not poor rankings.

Here’s how to find out whether a page has experienced any significant position changes.

Open the [Position Tracking](https://www.semrush.com/position-tracking/) tool and enter the name of your domain.

Then, click “**Set up tracking**.”

![Position Tracking tool search bar](https://static.semrush.com/blog/uploads/media/91/ec/91ec0283c51f4a2b46ef73a24d957393/65c7a6d1af313f03dd0b3c3501d12448/yhOPUuIVrQLvJ6x9veBTIYsgakuzouyxWHireQs8si9waQeADpl88YfYO8yKV2frnK_LmsYu3n604MMoJmjBnqZOpPT_oElsslY_rWJvW7muOwLtHrwOGYjpt17eSpHX416Qr88nZOBdjU3YGK9ZbyE.png)

Select the search engine, device type, and location that you want to gather data for. And click “**Continue To Keywords**” when you’re done.

!["Targeting" window in Position Tracking tool settings](https://static.semrush.com/blog/uploads/media/b5/d3/b5d3c0a1d2381b8bfee58204825310d2/5e9131ab2bd84eea729c3fda8d805a60/-oYTgTObtrSXVTMFWnDMs--Ydree8qtqr3v7pW193Sw3Ng7Nl2CvrNuAzNkhRWbxVhonFGqGZim3vmsnms7b3UdlSEsgxr29MvOK4DkropEGCssZ3-nwbGk36vIJPz4LThL1CmmxnC0AmGihcZg_NNk.png)

Then, enter the keywords that you want to track your rankings for. You can also import them from a CSV or text file, Google Analytics, or another campaign. Or you can use Semrush suggestions.

When you’ve entered your keywords, click “**Add keywords to campaign**.”

Then, select “**Start Tracking**.”

!["Keywords" window in Position Tracking tool settings](https://static.semrush.com/blog/uploads/media/46/eb/46eb1bf09c27d162dd4ced1fbfb74ade/67b793231c1bb8499ea05e065460f304/IL_3Skc526esKcC-lcKViAoCaFSOPLrKitvPNrXBxyGiXiaUjk8xXo9t2WwaUf0aDCURSruEUbH1Jqpr36C7scuZVdiC_UT9hhyA54LlQ_CvXi8ma3mEFhe44-thGnnifEY69p0TTsl6Qk0shXkDFh8.png)

When the project is generated, go to the “**Pages**” tab.

!["Pages" tab selected in the Position Tracking tool](https://static.semrush.com/blog/uploads/media/1f/1b/1f1bfea137b30334ee128b9f9072930f/21d29783c0c7286f61bd43d225b6c1a6/ZIojT39t89xj41EX1XPUvQ4SbyDO7jigwB1p3DcJ6AH307pHWXaMOv4tRphVNKwYJcor0bilVvFPAlwzfrfMtw4ZbRGwwNHdU0h6Kmo_Am1Hrdoap5uFehHACBiJBlpzqJBUEJGQTlzRd7KcawsxckA.png)

This tab contains all the URLs that rank for the keywords you entered when you set up the position tracking campaign.

In the “Average position” column, you’ll see how your rankings have changed. For example, the URL with the slug “ai-art-generator” has improved its rankings by 58 positions compared to the previous period.

![Pages report results highlighted for the slug “ai-art-generator”](https://static.semrush.com/blog/uploads/media/a5/ff/a5ffa3478f860c956375a27d4e1f7002/d1f16fcb7ca11bf99235d8e7028d062f/0osnfoaYl384bKrg3eKLfplIp-3i8ZS-6ilYE9BMz7qJCZPuO2eUYgGfKr4Mz2Zq1vgq8sUni9IeJjOSWocWZStzc5kV9_wt5j64dCZiqOEoA4o5vw4s2BXuk3UyvUBef-q4tSS8RCd2LjFornrMgUU.png)

If you notice that one of your pages has lost rankings, analyze the search engine results of the target keyword to see what kind of content Google prioritizes.

For example, you could discover that most top-ranking pages now include user reviews. You could update your page to include reviews and monitor your rankings to see if there are any improvements.

### Discover More Keywords to Increase Your Search Visibility

When you connect GSC and GA4, you can see the search queries that lead users to your website in one dashboard. And you can use these queries to find more [organic keywords](https://www.semrush.com/blog/organic-keywords/) to target.

Semrush’s [Keyword Magic Tool](https://www.semrush.com/analytics/keywordmagic/) is a great way to find new search terms.

Let’s say your website receives a lot of traffic from the keyword “thin hair.”

Enter this keyword and click “**Search**.”

!["thin hair" entered into the Keyword Magic Tool search bar](https://static.semrush.com/blog/uploads/media/bb/03/bb03c0356640ff8c3dcf8545e3eb1d3b/2e396a6ff8280f12f38730eca453a548/ONsPD4hblm7i_kQpaNR5tCXBA_-qYRJZDPQLXvwQzPdE7wE1KD0UIBDmzOKRWpoYJ5lhHw3QaUWjuOMVx0XP906__F3M1UcX0AT_rEOAXnyleIL_d_nuIlACk98LLoAdTMCGHAvv-t8dQtaxw10z4Ys.png)

From here, you can apply different filters to narrow down your search. They include search volume, Keyword Difficulty (a measure of how difficult it is to rank in the top 10 for a given keyword), and search intent (the reason behind a user’s query).

And you’re able to exclude (or include) certain keywords from your list.

![Filters table highlighted in the Keyword Magic Tool](https://static.semrush.com/blog/uploads/media/a9/47/a947f7b4b59dc41830e2d75867e61fb1/271b4ee7218ccc8a6a983ef4a3a4f5c6/Zm9IKV_jwnzOZ2KEYA67ca1KH3FkzEbMcvRRZBsYK5ifa6X8KVsgLHu4_M9pjP7OVtaoP_FEc4Xoj9Kcr-3FzAn-MrjUoeTEwvTQvYHruabXaoKWNO6SzAqEIk3T6tI7xPiniJECupRwq2qv7S_xSas.png)

## Take the Next Step in Your SEO Efforts

Measuring organic traffic in Google Analytics is an important step.

But actually **growing** organic traffic needs a multi-pronged approach. Because multiple factors play into your search performance.

Thankfully, monitoring these factors doesn’t have to be complex.

Semrush’s [Project Dashboard](https://www.semrush.com/seo/) provides the most important search visibility data in one place. So you can stay informed, find opportunities, and manage any issues that arise.
