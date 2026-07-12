---
title: "Google Analytics for Beginners: Getting Started with GA4"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "google-analytics"
url: "https://www.semrush.com/blog/google-analytics/"
canonical: "https://www.semrush.com/blog/google-analytics/"
author: "Zack Duncan"
published: "2023-08-11T15:16:00+00:00"
updated: "2023-08-11T15:16:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2023_aging"
  - "time_sensitive_title"
schema_genre: "Analytics"
fetched_at: "2026-06-12T15:43:49+00:00"
status_code: 200
html_hash: "e548eabfa1b959d0a7f594e0189b2e9ead61a616a86a42ba9d6d1545bdc21e6e"
clean_word_count: 4815
clean_char_count: 34986
---
# Google Analytics for Beginners: Getting Started with GA4

## What Is Google Analytics?

Google Analytics is a free website analytics tool that helps marketers better understand their site’s overall performance.

Unlike [Google Search Console](https://www.semrush.com/blog/google-search-console/), which provides detailed data about how users discover websites through Google organic (meaning unpaid) search, Google Analytics deals with all traffic sources. Including organic search, paid search, social media, and more.

And beyond telling you how your users arriveon your site, it has data that tells you what they do after they arrive. That includes which pages they view and what actions they take.

Google Analytics can also seem complicated and confusing at first. But it doesn't have to be.

In this guide, we’ll teach you the basics of Google Analytics and help you install it on your site.

Let’s start with a brief history.

### Universal Analytics

Universal Analytics (UA) is no longer the current version of Google Analytics. But it is the version that made Google Analytics famous.

It became widespread across the digital marketing world after the beta version was released in 2012.

How widespread? The various versions of Google Analytics have a greater than 70% share of the web analytics software market, according to [Statista](https://www.statista.com/statistics/1258557/web-analytics-market-share-technology-worldwide/).

Here’s what the dashboard looked like:

![what the dashboard in Universal Analytics looked like](https://static.semrush.com/blog/uploads/media/e6/fb/e6fb68c7e61768455a3f47407f71b4fc/NA0PdO0luFjKi4fJXH0nvQyx1MAUzRX5PDevTQUQXc-tlCahDvIbsBkJGOnAM-KyOpaK7wN2ZkPgNiw9247Brh7wc_OYiMJzn58G0OTO_DE-wnwKV9P3D-_IgXfjwdCjvQFIdLoZgTrzAQWzICtv0sA.jpeg)

But you won’t see it these days.

That’s because Universal Analytics was set to stop processing new data in standard accounts on July 1, 2023. So marketers started adjusting to the new Google Analytics 4.

### Google Analytics 4

Google Analytics 4 (commonly called GA4) is the new standard for the Google Analytics platform.

The platform was originally released as a beta version in 2019. And called the “App + Web” property.

The dashboard in GA4 looks like this:

![a dashboard in GA4 (Google Analytics 4)](https://static.semrush.com/blog/uploads/media/70/41/70414f3d0190430c4fe88a114e1a3f45/7jgezQtrnh5JlILVWmwmF8GI_CkQKJHh25ZMEkvIzz6CsPAObOBx5UKKTXFywseqT2e8OAynGZWRgZkW7Y3fMkgHXgSTn5KBAwsam0otR5B0j7xlS_7CZo0YcFkC4vZnm0jFSnNSOFeJNipKM7w3aO4.jpeg)

It doesn’t look all that different, does it?

But there are some fundamental differences between GA4 and UA. Especially for those who were accustomed to the prior version.

### Differences Between GA4 and UA

Knowing these two differences between GA4 and UA will help you understand today’s Google Analytics better.

#### Difference 1: Event-Based Data

Google Analytics measures user interactions on a website. Each of those user interactions is called a “hit” and it becomes part of the data you can see in your Google Analytics reports.

GA4 collects all web interaction data as “events.” In other words, all hits in GA4 are collected as events.

Universal Analytics collected data through multiple hit types. You can see this in the table below, with the various UA hit types on the left and how they translate to GA4’s event-based data on the right.

![a table showing how "hit type on Universal Analytics property" column translates to "measurement in Google Analytics 4 property"](https://static.semrush.com/blog/uploads/media/5d/90/5d90ea35982e1a6184f5ac6f0235d49f/MPbDx_5aVDqs8odY6_iSwfep3E_qbtPQe_fzQezDNKQWoBM7_LmrpU_s0DoWwBiQpRljF4jDVQXrB_DEAoagLAzZCNVR5Y9MZNTohi4gPgEzfiuk9TEYmx3MpItGAOvAG6UZiMzFNoOVWAa67Tmk2nA.jpeg)

The event-based data model in GA4 means some metrics and reports are now different in Google Analytics. We’ll see this in greater detail when we review Google Analytics basics later in this guide.

***Note**: Differences like this have been so disorienting for some marketers that they’re exploring [Google Analytics alternatives](https://www.semrush.com/blog/google-analytics-alternatives/). But Google Analytics is still an incredibly useful and powerful tool for those who learn how to use it.*

#### Difference 2: A New Account Structure and New Data Streams

Google Analytics 4 has a different account structure than UA and introduces the concept of a “data stream.”

Universal Analytics had an account, a property, and a view.

The account level was typically linked with an organization. The property level was linked with a specific digital property, like a website or an app. And the View level was where data was actually viewed.

GA4 has an account and a property level. But it doesn’t have any views.

The account level works the same as it did in UA. The property level is different.

Remember when we said that GA4 was initially released as something called the “App + Web” property?

That’s because Google Analytics can now combine data from a website and an app into a single, unified picture. Both the website and the app can have their own unique data streams that flow into a complete picture of user behavior within the GA4 property.

We’ll see how to set up a data stream when we get to the [installation walkthrough below](#how-to-set-up-google-analytics).

But first, let’s answer a critical question. What does Google Analytics actually do?

## What Is Google Analytics Used For?

Google Analytics helps answer important questions about how your website (or app) is performing. So you can find ways to improve.

***Note**: We’re focusing exclusively on GA4 for the rest of this article. Because UA is no longer supported.*

Here are some of the questions the platform can answer:

- **Who was on your website?** You can see what users’ interests are, which languages they speak, which cities they’re from, and which countries they’re from.

![an example of a map showing users by country ID in GA4](https://static.semrush.com/blog/uploads/media/6c/29/6c2954e5447cb78a332fd489aa420a5e/Nsgk2aNEAEOBAZFWupanS2p_mGtkJyoTr7ODx5154fQp21Qju1dUKOUVcvnpuI-28uc-FtYlR6yi7dMqsBz_ePMpeIJGHGC3NBoNFz3-HXIGe8hD71CXm9iBQBExp5KLZ5MUHSnTxYoce5h8XS_v9xA.jpeg)

**What happened on your website?** You can see how many pages were viewed, how many links were clicked, how many videos were played, and much more. Google Analytics will show you how often these interactions occur.

![a table in Google Analytics showing "event count," "total users" and "event count per user" metrics](https://static.semrush.com/blog/uploads/media/b8/46/b846c75cd331d7d94dd09072959f1d10/Za01Q1LUKtyBCCdSY7IbjueZF87tWStaTAjKJvOYzkibYK0SyanyhDAipcTimv3-qNxRZQI2t6rWsF7KZyuq3ryoQToHm3mMrHLK8oEDQulMRtxb-0okZv28v8ZPV8FS0Wm9Pc4L3XIMJ7xla5V0VcM.jpeg)

- **When did different events happen?** You can shift your date range to analyze relevant time frames. You can also compare performance across time frames to see year-over-year or month-over-month trends.

![search for data in Google Analytics for the last 12 months](https://static.semrush.com/blog/uploads/media/e0/ee/e0ee9f2ecb89c96e653c6466b686958e/U206f2-pfosLgodf5aHAxPiu7s0Nxq5Zi_xr5_he4PcyanaXf9Mzb-IFxB5PXm7WHAv-KGg9yMLROYw3abYGe1W3dX8MUaAvhOrnBDHGpTCrKXcEmrlvr7Exc3XCWt3YxEAq7iptZ8Ff7C56ESwrerU.jpeg)

- **Where did your visitors come from?** You can see which sources contribute the most (and least) traffic to your site. Let’s look at the “Acquisition overview” report below. Look to the table on the far right and you can see that the vast majority of traffic comes from organic search (unpaid traffic from search engines). Organic social and email contribute a small percentage of traffic.

![in “Acquisition overview” report you can see which sources contribute the most traffic to your site](https://static.semrush.com/blog/uploads/media/8d/ee/8deeb30bcf32536ffa5c64d6f62ed7a3/698cjyhPDMmO9clEhlVTfGlklH3gPujYszvyKBvhvUNZ_0rUfd9RD_ivS9jWMxs6G9G6jMywcavdFxlRaT4DAYQaAeLE2ykbO1CgEbezv8AHSiEQbvwiR2LdhcUfVY9K_kaORKlJKzW3CCrAGPVnyQI.jpeg)

***Pro tip**: An organization with a traffic profile like this might choose to prioritize their [keyword research](https://www.semrush.com/blog/how-to-use-semrush-keyword-research/) to continue strengthening their organic search performance.*

As you answer these questions, you’ll learn what works and what doesn’t. And you can use this to improve your results over time.

## How Does Google Analytics Work?

Google Analytics works by collecting data from your website (or app) and then creating reports so you can analyze that data.

A small tracking code needs to be installed on the site to enable data collection.

Here’s an example of the Google Analytics tracking code.

![an example of the Google Analytics tracking code](https://static.semrush.com/blog/uploads/media/49/26/4926e198bdb0ec4441a3a41ab1aa187b/ew7GWcP8IbtcKNtERMtRLeDfCAdSqyS_TuhEIeCgOFti476YacffIFW9maA-y4vXn5TKF1hP4gBdW5CFd1EhXm7Kwjhy_54xhTay-v-W4q1FZu_mIKjPP_82lcPCB6UrTbcefUCttse3_h2ZqRyUwLg.jpeg)

When a user arrives on a site with this tracking code installed, Google Analytics will place a cookie (a small file that collects information about the user) in that user’s web browser. This visitor activity is what you ultimately see in Google Analytics reports.

How does this data get there?

Let’s break it down into four steps moving from left to right. Like in the diagram below.

![a digram illustrating how Google Analytics generates data](https://static.semrush.com/blog/uploads/media/14/d5/14d591a5ddc8e192c2e2b52a708bbd18/pH2aFMVpyshPTrV1uOdC4jjuFfWhUeJns4dVPnaNt3boBijF1RxxSpALusDwPo-a2PLifd9F9KztrBofFbrnEbMN3Y78ywS78Voghh9L8uc9KJG7amDVt7BKJKzOcp3IYF1SieyJuin8rbwi42QTpgE.jpeg)

- **Step 1**: A user lands on a website with Google Analytics installed. The Google Analytics code sends a cookie to their web browser

- **Step 2**: As the user interacts with the site, their actions are now being tracked by Google Analytics

- **Step 3**: The user's interactions then get processed by the Google Analytics servers

- **Step 4**: After processing, the data is available for review and analysis in Google Analytics

Now, let’s set up Google Analytics on your site.

## How to Set up Google Analytics

Installing Google Analytics is a two-part process.

The first part is creating a Google Analytics 4 property. Which generates your unique tracking code.

The second part is installing that tracking code on your website.

We’ll start this Google Analytics how-to by walking through setting up your account.

### Create a Google Analytics Account

First, [sign in to Google Analytics](https://analytics.google.com/analytics/web/) with your Google account.

If you’ve never used Google Analytics before, you’ll see a screen like this.

!["Welcome to Google Analytics" page](https://static.semrush.com/blog/uploads/media/f8/50/f85006270bce9e5ef06f155a75caccf0/Hy7ArGrH08gzhEJrqtW_zchuq_QnBq_Br24Rg2HfziurfWKaNkYF18HgB-38kX8OMrGbXovC2CIF9Ew6vrxfHRrVhNqlM5unmiXuDWjfOj7XJJKXQ-pmbStPkhPM0GZWsWHu0M2sMG7EWRl9ll6v_qQ.jpeg)

Click “**Start** **measuring**” and proceed to Step 1 below.

If you have used Google Analytics before (with the email address you’ve used to log in), you won’t see this same welcome screen. If that is your situation, click on the gear icon in the bottom left of your screen to access the admin area.

![Admin area in Google Analytics](https://static.semrush.com/blog/uploads/media/fa/20/fa20b00970e97b8310c4c5b242c566be/iaf5xtS1oX0CTkl6hXpZi9QlrWnUm-dgVQ2O0YZr5Hxw_ci3nlXXztXNqE4vogUjjhJoL8rniw9wEUCfojG1oYPuNPBxFraSQDY9ZFzUC-pHugSY8L7RJ2EUTJInkThbBRhR66biTBNZRBkAhyZj0_k.jpeg)

Then click “**Create** **Account**” and proceed to Step 1 below.

#### 1. Set up Your Account

First, give your account a name.

![add your account in Google Analytics a name](https://static.semrush.com/blog/uploads/media/b2/9a/b29ab3b8995747099c4375c6bec6a941/bSepTgMrsAkruyvCAsrM4inlRi_e7QVtognqPm4NM0l7vEFcoHMYOxlrpYPBNyxt5xYtqhVFiqG8pF1kKD6Uww-T2JsOU3H83D-NCFl9KM1zcHrH6drGxeKf6c02HGFm2jMbefaL9tp___AArKBzbVQ.jpeg)

You can choose whatever name you want. But it’s a good idea to use your business’s name. So it’s easy to recognize.

You can also choose what information you want to share with Google at this step. Such as “Technical support” (who might be able to help with a technical problem in the future) and “Account specialists” (who might contact you for sales purposes in the future).

Then, click “**Next**”.

#### 2. Create Your GA4 Property

Now, give your property a name.

***Note**: Remember that the property level is where the data lives in Google Analytics. If you have multiple websites, you can have multiple properties that exist in a single account.*

Once again, you can choose whatever name you want. It’s not a bad idea to use your website’s domain name.

You’ll also select your reporting time zone and your currency.

!["Create a property" page in Google Analytics](https://static.semrush.com/blog/uploads/media/47/1f/471f779ecb66474efa814562873dca68/mhlon9kSD1mOADLnsi4VRKleGLUP9Q9vvyXXZIuLvJau2J7YyERyv8M-jjwFzGKuZ7viFx8lOHo1ggjPzFS8x7qrECbsfFuCoYnH_S4Sk9h7JL0Z4sFH1sWWOB1EjDSU8wUJue5Nkpt2SccntGQGVN0.jpeg)

After making your selections, click “**Next**.”

#### 3. Provide Your Business Information

Now, choose the industry category that seems like the closest fit using the drop-down. If nothing matches, you can choose “**Other** **Business** **Activity**.”

And select your business size.

Then, click “**Next**.”

!["Describe your business" page in Google Analytics](https://static.semrush.com/blog/uploads/media/a0/91/a0919a88b86b9fca98b359841192b42f/K5LjRWIegqNr5_mO12et4OurnyI74_ilNmXtYacv9Exc3Yu-oPYZTI-jS0ah6kc25k1BdKTuF3vpJAb_92yt722BSBaLDpc2bpzcCRFtVpS5fock2-FTKaOEv9kBTyRdWmPM0-nHQyoL2hPCKn4thaw.jpeg)

#### 4. Select Your Business Objective and Accept Terms of Service

The selection you make here determines what reports will be pre-loaded in your Google Analytics property.

If you’re not sure, it’s fine to choose “**Get baseline reports**.” You can always add additional reports in the future.

!["Choose your business objectives" page in Google Analytics](https://static.semrush.com/blog/uploads/media/35/14/351445403edecd7a1afa2e8a74e8233b/9GSXPQXQ60Mh9Lc-E2znC9DYtOriBOPQHdr9ozgGapvua8aadnqlZY1FCyzNjHjxPYTHWbSbB9XLNbjOa2qerqWexDHvqASN6rbNXO5a9IK2vOFFREZkhX_OoQLOhOExSmstEXQd-ecbLHLeZfzF6M8.jpeg)

Then, click “**Create**.”

You’ll now need to accept the Google Analytics terms of service to move forward.

After reviewing, accept the data processing terms and click “**I Accept**.”

!["Google Analytics Terms of Service Agreement" page](https://static.semrush.com/blog/uploads/media/a6/1d/a61d653d3b542f2cd05ef407fbc274be/hbdEaT8YCupqvdMRvRA4mrnfnsHHFyt__nhOoIx5934x5YqHD1X58fBNAhnKAZm2-kiUa-y64wqOyG3GNWTWh97hje0e0Mu_v7r8mnbEARdsodeEPMMLSvvpOjtFOOd5EBfubCChd2lu6y9R-cDXxHI.jpeg)

#### 5. Set up Your Data Stream

You’re now ready to start collecting data and you can set up your **data stream**. The data stream is what sends data into your Google Analytics property.

Choose the type of platform you’re working on.

![choose the type of platform you are working on at "Start collecting data" page](https://static.semrush.com/blog/uploads/media/d1/00/d100a5b65170a55ceee7eefc46ce6f64/pqq81Pwtg_yAZNncsyVxe6fg2RNa-HbUKdW7dlnrOOC27uww5x6LXKZoYy42YJ5f_GgpY1wuk49S8WRjaJo9hC-BaO3eC8qr56G7Pozj8J50CnJna_jRueAkN7y2mh8CW9jDH0sMftFwFbAqKIDPIRA.jpeg)

Choose “**Web**” if you’re working on a website. You can now set up your web data stream and you’ll see a section that looks like this:

!["Set up your web stream" page](https://static.semrush.com/blog/uploads/media/b6/e5/b6e51de28d1309a34c3ee0c9ec4a1e35/Qh99wnDOUtngaG9ZYmAQeKXEvCdnGuEwhjVIUVwuHXbCKtO9oJa0AQFQP2xug88gTgFIwA2DCoBkJKa2Nd5Q9C3eY25gq6gfbCCKwSQ0Vg_G2s4lLyji65AYFJUUEgYe5IRPAIL--b9QSfScO0wWc7Y.jpeg)

There are three things to do here:

1. Enter your website URL
2. Give your data stream a name. You can choose any name you’d like. If your domain name is www.widgetcorp.com, you might choose Widget Corp Website as your stream name.
3. Ensure the blue toggle bar is turned on for “Enhanced measurement”—this allows you to track certain interactions like file downloads, external link clicks, and embedded video plays without doing custom work

Now, it’s time to install your tracking code so your data stream will start flowing data into GA4.

### Install Google Analytics

You’re now ready to install Google Analytics on your website.

After your stream is configured in GA4, you’ll see a screen with a “MEASUREMENT ID” field that’s unique to your property. And a “View tag instructions” button.

![“MEASUREMENT ID” field and “View tag instructions” button highlighted](https://static.semrush.com/blog/uploads/media/92/61/926111305d1c30e4a50aab40c18f2c6a/QETYNht1U24La-yrCDP6I2QlrEfF-7T0F2--0tARvnDjqGIfES1H1hPqTtYuLZKGp1QqBBZ_sKFJzY39OQppQh1LC4a0YCIS5YjV-WU0ytoAJWXU9jnnq-1kt0PXnSsMacF5clR8qHrwSdOu2cS4PT0.jpeg)

Once you click the button, you’ll be given three installation options:

1. You can install the code manually on your website
2. You can install the code with a plugin or integration, if applicable
3. You can use Google Tag Manager to install the code

***Pro tip**: If you already have Google Tag Manager running on your site, the third option is likely the easiest. You can use the installation instructions in this [Google Tag Manager](https://www.semrush.com/blog/google-tag-manager/) guide.*

We’re going to go with the manual option.

#### How to Install GA4 Manually

To start the installation, click the “**View tag instructions**” button from your data stream.

Now, click the linked header text to “**Install** **manually**.” This is the tracking code that will run GA4.

Click the “copy” icon to copy it to your clipboard.

![where to copy tracking code in the “Install manually” section](https://static.semrush.com/blog/uploads/media/9e/6d/9e6dd3607c3f0d8b371d2f4c543db302/CtQsDFQRY7Hp0BB7FBMuVvwgsOFxk_CbMOsplxZMGvFGFnMcNsmJPpA9MIQcA2eMdIX-jj99zFXMFZJPrmh61pa7tcpyo5nK5b_UGweL8DjmBSP2OKvnmoCGvGIhGLpSSpZ-7D2I7VBo2TK_i2AmSTc.jpeg)

Now, go to your website and paste the code high in the <head> section of the page.

Pasting the code high in the <head> section will help the tag fire properly and ensure you get the most accurate data.

***Note**: If you’re not comfortable modifying your website code, ask a developer for help. Also, some WordPress plugins will allow you to modify your header without directly editing website template files.*

Congratulations—Google Analytics 4 is now running on your website!

## Google Analytics Basics

Data is flowing into your Google Analytics property.

But what data, exactly?

Google Analytics data shows information about visitors and their interactions that take place on your website.

Here’s an overview of the main data categories:

- Users
- Views
- Sessions
- Events
- Conversions

Let’s see how it all works.

### Users

A user is an individual who visits your website.

Google Analytics uses cookies to help track the number of these unique individuals who visit your site. You can see this in the data table below.

![a data table in Google Analytics with "users" column highlighted](https://static.semrush.com/blog/uploads/media/3d/15/3d150093266577766285b0b85cc5b909/xH2Rswbqz44nHKlXg0TiIU67BrVN_3-Hd15iyqsVooxdKRpWYVeGtahuPwrjMCSftVK_JMK6O7ntZ4NR2wapi-DLmLl_1WcEzhlPuAixZu1hfv0nIWIaKtWAvs_N4cQSwYC0tao0N7sdpaB5wUWInsM.jpeg)

But when you use Google Analytics, you are doing more than simply counting users. You can analyze the behavior of those users. Such as what specific pages they view.

### Views

Google Analytics records a view each time a user views a page on your site.

If a user views a page, leaves, and then comes back to that same page in a few minutes, that counts as two views.

Here, you can see a data table containing a list of top pages by views.

![a data table in Google Analytics with "visits" column highlighted](https://static.semrush.com/blog/uploads/media/01/b8/01b84010370363f77df0c2fc2016d3b1/-X4Fp-wpkxWw9BTvTbqpSZ_jC0el_5D6CWrDQvEw3e9u9MuN6_sDZJIteWS8rnoZx1bsCIro3hoJ6EK7NRGXyscOLo5Kx98nF-UdCyoTKLf4kHhTrSlCT4v0Q2WTE6QN_GdJFPl7iOulvdbUbVjTtDM.jpeg)

***Pro tip**: You can easily see this same report in your own GA4 property. Simply click “**Reports**” in the left-hand navigation, and then select “**Pages and screens**” within the “Engagement” reporting area.*

### Sessions

A session is another name for a user’s visit to (not just a view of) your website. A user can have one or more sessions on your site.

During a session, a user can perform a number of actions. Like viewing a page, downloading a file, playing a video, clicking a link, or completing a form.

Google Analytics associates each of these interactions with a unique session identifier. So you can understand which interactions took place during a session.

Google Analytics ends a session after the visitor leaves the site or after 30 minutes of inactivity.

The partial data table below shows a Google Analytics property that had 27,053 sessions during the specified time period.

![a data table in Google Analytics with "sessions" column highlighted](https://static.semrush.com/blog/uploads/media/46/6f/466fe376277cc3881a3acd042ed44a5e/6NpcH27pBQ5ZruISjWRMXGvU_mqkzPsPXjo4rhzrdbJgJ_xoE3w-wvTY7KHGkdlQMqhqylrr8dBRRLvPdmLrSG50Wz287Cg8Q3dF2jFu3xAfXOD0GqPUoKXNVoOn1YDtBned4uFwYavblDg_uYyxBWc.jpeg)

***Note**: The number of sessions should never be lower than the number of users. That’s because you can’t have a visit (a “session”) without a visitor (a “user”).*

### Events

During a session, a user may interact with your site in a number of ways. They might download a file, play a video, scroll down the page, click a link, or complete a form. These interactions are known as events.

Google Analytics can record events like scrolls, session starts, clicks, and more. Like in this image:

![a data table in Google Analytics with "event name" column highlighted](https://static.semrush.com/blog/uploads/media/12/04/120411fc5a6b1b2246ce2676bb9b9796/nDQaOxc9IN3OfgpJtSVSSZo81RYbCQN4ioMr50k3Co5LSeRZ0EHz3pQe-gk3OFe_U_XZMzRX1QxEnofZsqoXAKi4lOpYN5sOyqXdIvKzFcAw_pdr_inMuy0l9UfLhFCKIrY337WxAesaT78VnDjVPZ0.jpeg)

When it comes to events, there are four basics to understand:

1. All website interactions are tracked as events. But there are different kinds of events, and they’re treated differently.
2. Google Analytics will track some events by default. Some of those cannot be turned off. They are called “automatically collected events.”
3. As long as you kept the toggle for “Enhanced measurement” turned on during the setup phase, you are also tracking enhanced measurement events by default. You can turn some of these off at any time if they aren’t a fit for your measurement needs. Here’s a link to [Google’s resource](https://support.google.com/analytics/answer/9216061?hl=en) if you want to learn more right now.
4. You can also track some events through your own setup work. Google will provide a recommended name for you to use for some of these events. Google calls these “recommended events.” Any other events you create are called “custom events.” [Recommended events](https://www.semrush.com/blog/recommended-events-google-analytics-4/) and [custom events](https://www.semrush.com/blog/custom-events-google-analytics-4/) are similar in that you need to do all the work to create them.

***Note**: Some custom events can be created within the Google Analytics interface, while other custom events require the help of Google Tag Manager. This is a key benefit of using Google Tag Manager with Google Analytics.*

### Conversions

Conversions are the most important actions that users take on your website.

If you run an ecommerce website, your most important conversion is likely a purchase. If you run a lead generation website, your most important conversion might be a contact form submission.

But you first need to identify which specific events should be counted as conversions you want to track. In GA4, the simplest way to create conversions is from events that already exist.

That means you’ll want to do this in the future after your GA4 property has recorded specific events. You can even create that event data yourself by performing the desired action on your site.

Let’s imagine you want to track the file download event (called file\_download) as a conversion. This event will be tracked by default through enhanced measurement.

Here’s what to do.

Click “**Admin**” in the bottom left of the Google Analytics interface.

![“Admin” button in the bottom left of the Google Analytics interface](https://static.semrush.com/blog/uploads/media/a8/3c/a83c431f16ec7101a041f641af29775d/Mied1xB0zIjtEhdzwDeKVMnxg82xMKt4Lg7kXuAW6MnCTA6aYjKsUQRVrpK_TCXQk3LJ-eT54Unn83byxTmUh4ymLTBFVD3nKCx3wR-LTx_kuNafWpD7vjmRZmg2yHDYW3DuqVvi_ZkiWg8HAQSQKK8.jpeg)

Within the property settings in the middle of the screen, click on “**Events**”.

!["Events" button highlighted in the property settings](https://static.semrush.com/blog/uploads/media/8a/3e/8a3e3a5e71891f486e37c0265dc38aa1/6PsPhfYYWXoXL8U60JZAqnfZc15JNHF3o73goGjzM3Aba8FqtyP0ytDQlJitznnH9fEwetznp7UO2j93pBqL8H_Hx5YY_hL-kkWsCe4Lb6xfsBYgW3f6w5Njs0tPQlzIyR-i-ByQTMuMBuhS_sXKVXs.jpeg)

Now, you’ll see a list of all events that have been tracked in Google Analytics.

Find the file\_download event. Use the toggle on the right side of the screen to “Mark as conversion.”

![marking the file_download event as conversion](https://static.semrush.com/blog/uploads/media/f2/a4/f2a4b6cbb26400ec9242e598edb52f29/LTKLzWu2OuB6Ol6NLvnVB_duRjbKqrk1ufdYcl2xvpcP8SCb1uV5TNf1i00PoY-Lk-yH_cG_NLUm6OV35jx4JcAViCJJcFW-UdbNDGKyyTAXcm1iilARHfgUbGce34GcaxSlbM8BSBwRRfnhHIfpxNQ.jpeg)

You’ve now created a conversion.

***Note**: You can still get value from Google Analytics if you don’t set up conversions. Although it does help when it comes to evaluating your site content and traffic channels.*

## How to Use Google Analytics

Now that you understand the basics, you’re ready to start using Google Analytics.

Let’s go over how you can use the platform to analyze metrics for important pages and how to refine your marketing strategy based on the results.

### Analyze Important Pages with Google Analytics

GA4 makes it easy to see information about your best- and worst-performing content.

Let’s use the “Pages and screens” report to do this.

Click on “**Reports**” in the left-hand navigation.

![“Reports” button highlighted in the left-hand navigation](https://static.semrush.com/blog/uploads/media/3e/81/3e81e80727922a1e4c8ecc9d684b91f4/NaldhIItM1LtIn6JDlw8k7U4jfFA470f-5gRa5hd0yHTlyodW8L6cfwEZSv6vBC0dk9UCeCgR8uAU8fZjK5t3WFe2ftMVMaG8CvN3LFSMaHSItM9X8P4B3b8yKzZnJuBZp4DnvthoTfs9a4hTfQcemU.jpeg)

Now, expand the “**Engagement**” reporting area and click on “**Pages** **and** **screens**.”

![where to find “Pages and screens" button shown in the menu](https://static.semrush.com/blog/uploads/media/64/00/64008db84e0663a54822551b42275dcf/RkuIeAGWc-kVXKw3jIJ6e_z3y9KFlVk_jy0xtw8LzB5MrodAfyyZCLIZ3B6PqeblXTxgZEYXK8D3KFhExsOlaD89U6xUL2HDkDtVn7B7xbAHTv2u_e5A3iBh0ojIHUhOb5xsEhQCbJxe2mo9LDwNAfQ.jpeg)

You’ll see a list of your most-viewed pages with the data sorted in descending order based on total views in the “Views” column.

![a data table with the most-viewed pages and their metrics in Google Analytics](https://static.semrush.com/blog/uploads/media/7f/18/7f189450b5cc512e28b41a56815a3a27/RJk_f3-T3T38UPfp1TGbAsdPAkDk0CA7bWLpAK2FxSRYXk1Gef40YC9BtId23J1l4cv7eQlV0Jo7nB8_wqeDIq-fBENX-fmcUKVjq0e9OOcsPw60Ff3x02dQaUudAGpPvs0YHpTB1XN0W5C2ii3_w0w.jpeg)

You can also analyze these engagement metrics to understand performance:

- **Views per user**: The average number of times each user views the page
- **Average engagement time**: The average length of time the page was in focus in the web browser
- **Conversions**: The number of conversions coming from each page

***Pro tip**: Clicking on the arrow immediately to the left of a column headers in a report will sort the data based on that specific [Google Analytics metric](https://www.semrush.com/blog/metrics-in-google-analytics/).*

Now let’s see how you can use Google Analytics to analyze your traffic and improve overall performance.

### Refine Your Marketing Strategy Based on Performance

GA4 will show you which marketing channels are driving the best performance so you can focus on what is most important and work to fix what is not working.

For this, let’s use the “Traffic acquisition.”

We’ll stay within the “**Reports**” area.

![“Reports” button highlighted on the left side menu](https://static.semrush.com/blog/uploads/media/3e/81/3e81e80727922a1e4c8ecc9d684b91f4/NaldhIItM1LtIn6JDlw8k7U4jfFA470f-5gRa5hd0yHTlyodW8L6cfwEZSv6vBC0dk9UCeCgR8uAU8fZjK5t3WFe2ftMVMaG8CvN3LFSMaHSItM9X8P4B3b8yKzZnJuBZp4DnvthoTfs9a4hTfQcemU.jpeg)

Expand the “**Acquisition**” reporting area and click on “**Traffic** **acquisition**.”

![where to find “Traffic acquisition” button shown in the menu](https://static.semrush.com/blog/uploads/media/58/a0/58a0cc09f44be8e1d394222cb1ab13f7/SNiSiHJglaKqogr-soiDG0Ri0WbNP0oDyVBHrM-5lclifStJ8KQfsTH8mQahQu17Nc9MJMsq2BvYvOf1U2czQrvhcoU2EqiRFIlbSsFsI2JKoao09-6yDJrSPqaOJGNk8AZTKOYb-6i1c10Yshxe10k.jpeg)

You’ll see a breakdown of how your website acquires traffic. Based on channels like organic search, direct (users who came directly to your site), referral (users who came to your site from another site), etc.

![a data table in Google Analytics showing a breakdown of how your website acquires traffic](https://static.semrush.com/blog/uploads/media/98/6b/986b2c694a1b704ca767dc731a9334e1/nWxEiLwBHuED17I4q4LBxn4b2zkszRnaP5qaaI602r3QtRkLhmPSkE3jvQ-CFuToVk2VGqeLDCfN2tpHUV4LmLJcRXQl2N7H9wkUnE-fq43wAITJfs_KwA3w5aqBMcr5Ftda7ZHCGZn2lzxS_WagWyw.jpeg)

You can analyze these acquisition metrics to understand channel performance and learn how you might refine your marketing strategy.

Here’s one way that could work.

You can see that organic search is your most important traffic channel. It drives the majority of traffic and is responsible for the most conversions. Organic social, on the other hand, drives very little traffic and hasn’t had a single conversion.

Let’s say you decide that organic social could be an opportunity for growth. A great place to start would be to look at which organic search landing pages are driving the most traffic and conversions. Perhaps you could create a social campaign focused on the content on these top pages and create a series of engaging posts that would help drive traffic to those pages.

Here’s another idea:

You can see that paid search has a relatively high number of conversions but a lower engagement rate than organic search. You might hypothesize that the CTAs in your paid search ad copy are working well.

How could you leverage them in new ways?

You could use them as inspiration for in-page banners in your organic content to drive more conversions from pages that your readers are already engaging with.

## Google Analytics Tutorials

You’ve already learned a lot about Google Analytics. And there are additional tutorials that will further accelerate your learning.

You can start with these [Google tutorials](https://developers.google.com/analytics/learn).

You’ll be able to choose your own path based on your specific needs. The “Analytics for beginners and small businesses” path has helpful resources for those who are just beginning.

Click “**Get** **started**” under that section.

![Google tutorials page with “Analytics for beginners and small businesses” tutorial highlighted](https://static.semrush.com/blog/uploads/media/db/3c/db3ca0c3602452e2ee6d1fcfef888844/f5_Rc62cvlWFugmFFnhtBOve-aH1LqZdouKezjs4JZej9s7WiB-Ps4aKvR7YE9uK6bVNjdBe4REIKle19ydSvavZomYp13LjSCfsc-TNl7fUCGEh0AIiZgVsq0HgVNQdXyDkuOdzV89WCtQ9W7Q2OTs.jpeg)

From here, you’ll be able to choose a specific training.

If you’ve been following along, you’ve already set up a property.

Reviewing part two, “Find your way around Analytics,” is a good bet.

![“Find your way around Analytics” tutorial highlighted](https://static.semrush.com/blog/uploads/media/fa/84/fa84632f5cf29e9dbc1e56f69bf12039/dBHAbUWawDZKWgKc7tMqOIvhbVcz1TFL6qccxlUE2nMICL6ZcITIW83KqC45d74U7qyK6NNAtb5FF0mA8yUGTkOKz8TwtVhiWrIrvR_0U1934kB-B1WuWmmEl9ub4yjHh0iZhIqzOM3xNXdEt8YfdN8.jpeg)

Here, you’ll learn how to customize your reports. Which is a helpful next step.

You can even test your knowledge with the certification track in Google’s [Skillshop](https://skillshop.exceedlms.com/student/catalog/list?category_ids=6431-google-analytics-4). Just search for “Google Analytics certification” within Skillshop to find it.

But the certification is optional. And many Google Analytics beginners get more long-term value from the platform by using it regularly to analyze user behavior and traffic performance.

You can amplify your analytical insights by comparing your performance with your competitors.

## Analyze Competitor Performance with Traffic Analytics

As you begin to understand your website performance, you’ll likely want to know how your top competitors are performing.

But your competitors aren’t offering to share their Google Analytics data with you, are they?

**[Traffic Analytics](https://www.semrush.com/analytics/traffic/)** solves that challenge by modeling competitor data based on the actual user behavior of over 200 million real but anonymized internet users. You get a clear picture of your top competitors’ web traffic so you can see how your own site performance compares.

Here’s how to use it.

Go to the Traffic Analytics tool and enter the domain name. The tool will suggest additional relevant competitors after you type the first two.

![search for your competitors in Traffic Analytics tool](https://static.semrush.com/blog/uploads/media/a4/95/a495b2d83f0feb9ef5a63105a7eaacef/tBw-JSd2-AiV9zVNYEZ6vJY1xL77cfMat4JTgAllooYEiZ32l_et-x12AbylnDovXPBZXOSylJxXEMmNAkr3njt2hmK5B3l2Gz1D8GjHs_79ntBBfBWR5A4uIeXNqnWUFbP4ycusKd__sPi9IYQekY8.jpeg)

Click “**Analyze**.”

You’ll see data on visits (equivalent to sessions in Google Analytics), unique visitors (users), and pages / visit. You can also see who is trending up and who is trending down.

![Traffic Analytics provides information on your competitors’ visits, unique visitors (users), and pages / visit](https://static.semrush.com/blog/uploads/media/2d/6d/2d6d1f7e4e9f98fdb39b0d0e2147f001/FGOvYQslMt6So11HrQTt5inTFkgYll-YjHjO1MSV-e1iLhGM2IPwDc-LWAgtb-UXdAO4CBuUXBNLfi0_QA00bd_cLAFws2YIxz0bBwHikWYLgzQ9ioQhSGl3LLPQpMAtw-LcWK4GHg0TauNw1Q3-v9I.jpeg)

And that’s just the Overview section of the report.

You can dive deeper into audience statistics and top pages to see what’s working for them. With it, you can learn from their top performers and refine your own strategy.

Ready to try out Semrush supercharge your analytics insights? [Start your free trial](https://www.semrush.com/signup/get-free-trial/) today.
