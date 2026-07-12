---
title: "Google Analytics 4 Events Guide: Event Tracking Explained"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "google-analytics-4-events"
url: "https://www.semrush.com/blog/google-analytics-4-events/"
canonical: "https://www.semrush.com/blog/google-analytics-4-events/"
author: "Zack Duncan"
published: "2023-10-31T15:02:00+00:00"
updated: "2023-10-31T15:02:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2023_aging"
  - "time_sensitive_title"
schema_genre: "Analytics"
fetched_at: "2026-06-12T15:40:03+00:00"
status_code: 200
html_hash: "58ab2452e50a343234ac4222d0dcbc85ff643bb6f1c8b01fff647c00691f29fe"
clean_word_count: 3415
clean_char_count: 27563
---
# Google Analytics 4 Events Guide: Event Tracking Explained

## What Is an Event in Google Analytics 4?

Google Analytics 4 (GA4) events are user interactions or system occurrences on a website or app.

Events are the foundation of all GA4 tracking.

Any time a web interaction takes place—whether it’s a page view, click, scroll, or purchase—GA4 records that data as an event.

This is quite a change from the prior version. In Universal Analytics (UA), events were one of many types of data you could track. **In Google Analytics 4, all user interaction data points are tracked as events**.

Here’s how it works:

The technical name for one of those tracked web interactions is a “hit.” As you can see below, Universal Analytics had multiple hit types. But in GA4, all hits (interactions) are events.

![A comparison of hit types in Google Universal Analytics and GA4](https://static.semrush.com/blog/uploads/media/07/91/0791e537567dd2f8ed60d8be4edde15e/0dc41f084e63722161a06dc6af784018/6YfUJBMrXSL-rFgWyjRJWJOyW604hpjuyXkE-mr5dDsiqvrvDZAHQIOFhK_GvpiD8eDOcdFdYd2ocNp3lVwx69wHjyTw2Db8ka57fksU7S0PSXvl9RpenBth_pnfPhYPLFAqizgv0BEDPAW5KHzsyD8.jpeg)

Now, let’s look at two crucial differences between GA4 event tracking and UA.

## Google Analytics 4 Event Tracking vs. Universal Analytics: What Changed?

There are two major changes you need to know when comparing Google Analytics 4 events to Universal Analytics.

### GA4 Has Different Types of Events

Universal Analytics did not have different types of events.

As you’ll learn in this guide, GA4 event types include automatically collected events, enhanced measurement events, [recommended events](https://www.semrush.com/blog/recommended-events-google-analytics-4/), and custom events.

Although they all produce event data, they work differently in terms of creating event tracking.

### GA4 Allows Custom Event Creation With and Without Google Tag Manager

Universal Analytics required you to use [Google Tag Manager](https://www.semrush.com/blog/google-tag-manager/) to create all events.

In Google Analytics 4, some events are collected automatically. And some require you to set up Google Tag Manager. For others, however, you only need the GA4 platform. We’ll review the specifics later in the guide.

All events, regardless of type, have important supporting details called “event parameters.”

## What Are Event Parameters in GA4?

Event parameters provide additional information about how users interact with your website.

For instance, you can include parameters that describe the products you sell, such as their name, category, and price.

You need parameters to fully understand your event data.

Let’s look at a basic example to see how Google Analytics 4 events and event parameters work together: the page\_view event.

The page\_view event records data every time any page loads, but it needs a specific event parameter to collect all the information we need.

Here’s how it works:

- **page\_view event:** The event counts [page views](https://www.semrush.com/blog/pageviews/) whenever a page loads
- **page\_location event parameter****:** The parameter sends additional information about the event to show which pages are being viewed

Here’s another event parameter example:

- **click event****:** The event will count every time an external link gets clicked. With the event alone, you will only know the total number of times that all external links were clicked.
- **link\_url event parameter****:** Once again, the parameter sends additional information about the event. The link\_url will tell you what specific URLs those external link clicks point to.

In UA, you needed at least two event parameters per event. And you could have a maximum of four parameters per event.

However, in GA4, you can have anywhere from zero to 25 event parameters with every event. Those parameters can be different for each event.

## Types of Events in Google Analytics 4

There are four different types of events in Google Analytics 4. Below, we cover each one, including what they do and how they collect information.

### Automatically Collected Events

Some Google Analytics 4 events are collected automatically, and you can’t turn them off.

Here are some examples of automatically collected events:

- session\_start event
- first\_visit event
- user\_engagement event

Let’s review what these GA4 automatic events do.

#### Session Start Event

Two important things happen along with every session\_start event.

![An infographic showing what happens in a GA4 session start event](https://static.semrush.com/blog/uploads/media/93/23/9323383e23583d272cd8e4f2618234a6/693c07e489bb666d46a843a45816542d/zaHPbagkRl1Ws9UVJE7htetrf2YCIlkD_j_9lp7i0FMpR7snivvvsQ6k8dZd2g04Ia8VuAmkTPwtt7LPmaPTDjmg_TMDkEmvujbTijmQsUNksFn-yl-CtYaLEVCFYn5Lbwo9hWFRXyKaenWBa68QBtI.png)

- **Google Analytics generates a session ID for the session:** The ga\_session\_id event parameter now applies to all other events during the session. It allows GA4 to group these events for proper [session](https://www.semrush.com/blog/sessions-in-google-analytics/) reporting.
- **Google Analytics generates a session number for the session:** The ga\_session\_number event parameter counts how many sessions that particular user has had on your site

!["Session Count" table in GA4](https://static.semrush.com/blog/uploads/media/5a/92/5a924a23fea2a0412e39fa47e6b1b70a/4a8be057c8cc3017b03ff12d5c49db4e/7NE1AhDkJTj0krNgx6ngSvT7HBWwiYqGh-ZGuqEQyw78kl-l_jsKWzmyC1eaIEDiplNV-RHWcOqtB-H-nnCHhCtqHpPDjV2yKnhsApI5IbdC1qo0Gg_O4SKbE6RDEO7PzyTldcGmdtdi-VQ1LZZ-rXM.png)

#### First Visit Event

The first visit event identifies new users on your site or app. If Google Analytics doesn’t recognize a user through the cookie in their browser, the first\_visit event will fire.

The user\_engagement event fires when a session first qualifies as “engaged.” There are three ways for a session to count as engaged:

#### User Engagement Event

- Lasts 10 seconds or more
- Involves multiple page views
- Has one or more conversion events

If any of those three conditions are true, the session will count as engaged. You can see both sessions and engaged sessions in the GA4 “Traffic acquisition” report below.

![GA4 “Traffic acquisition” report with "Sessions" and "Engaged sessions" columns highlighted](https://static.semrush.com/blog/uploads/media/6d/ab/6dabb7c00600715a274233fc6a217767/b544034a16d29fc0f42a0e6c4943a8c4/CnROSGsNQ-lbeopoUuvMMJLUNiflxzdpYAQvz8Y0ldyA4l5M7eOd6pezCPgMxx7kWaPsg14zkQA7_5goYsEP6knsG6JcOczaf0wNuGKZX4U9WtiTwhE0dDsnCQ2GnjC2vvEu0JUSeYPqILG0IM-Sfsk.png)

### Enhanced Measurement Events

GA4 collects enhanced measurement events by default. You can, however, turn them off.

Enhanced measurement events represent one of the biggest areas of improvement for GA4. These Google Analytics 4 events will be collected by default.

You can track interactions like file downloads, outbound link clicks, embedded video plays, scrolls, and more by ensuring a simple toggle switch is on. While these built-in GA4 events should be on by default, it’s always good to double-check.

Here’s how:

Go to the “Admin” section by clicking on the **gear icon** in the bottom left of the GA4 interface.

Now, click “**Data Streams**” within the property settings.

![“Data Streams” selected under the "Admin" section in GA4](https://static.semrush.com/blog/uploads/media/01/b3/01b341e28b83531bd2ddc5abb33d4004/127690bc407c5f27efbff104016a49d5/GeW5cR7rLJD9dcpiJjDKv3PAbae3uIWYMdDFj0U2Qond4npN4OHakziwFccnZ3pSEIEeipUc3iSfIuiYcTiSiUcmDbzZ580Vd-CH6KAgWAEQKyjuVVRj70-Q-6ae8Ej7rUlzTW2aDUwyDw1sugVyStY.png)

Then, click into your data stream.

!["Root and Branch Website App+Web" data stream selected](https://static.semrush.com/blog/uploads/media/0d/b9/0db9f897fb0868c24c68ffb53f8f03b7/215646637865a67c40efb43fdff8b536/EQ4ilYzP6aOG3Lk7sIJqNLJ8m3IeTsdRsmDV57F2Czxs0kqnedwk37s6EG0byCDRCJndlSna4SxyteWllSPQiYdt5qm8zSbpa0ra73Gf_81eIeM8zElumiRQn-Y55VQLqbhRh-rMrU5TqQvwwsj73yk.jpeg)

Ensure the blue bar to enable “**Enhanced** **measurement**” is toggled on. It should be on by default, but move it to the right if not. Now, click the **gear** **icon** to adjust individual events.

![The blue bar next to “Enhanced measurement” highlighted](https://static.semrush.com/blog/uploads/media/6c/69/6c69c04f8fe665f0def6b0b93a3de565/90eea8bfdcf30a3005d2d9ce4be99fbf/PKbXlFMPS5eFQLEbSBtptZo_i8KGIHQwdrF_PL-qrgGYPKb4lIsGpgAamKw5OZiooy9tZ0qnCTueBzoyLFd2WdFfMG_ml1lU0RoIsAd_PP75Eh8z5baHSR-_oHODtUx-2sP7pMuMYNA0vGDHGb6_WfY.png)

You’ll see a list of seven enhanced measurement events you can turn on or off with a single click. If you want to turn an event on or off, simply move the toggle switch and click “**Save**.”

![“Enhanced measurement” events table with toggle switch highlighted on the side](https://static.semrush.com/blog/uploads/media/50/d4/50d4239a8db95691e8b22aeaaf8f4039/e576df03fffe8d42433da4a1f7922370/DzN4dp6zOXe1mWhl8W3oC6BsFsEr8g8cxx8pFxBFKGYRDbVP7L4yGV5yIc5ununpyqxz9V2EZtE0YwfWJ82R04QPbw8Ct9EkpedRUqS59wQwhuX-XkonWxKh2E-uu0maC8ie6JjDh7MpZz3hrr-z8yI.png)

Each of these enhanced measurement events will generate event data within your Google Analytics property.

Let’s review the full Google Analytics 4 events list so you have all the tracking info you need:

- **Page views****:** This generates the **page\_view** event that fires every time a new page loads on screen
- **Scrolls****:** This generates the **scroll** event that fires when a user scrolls 90% of the way down a page
- **Outbound clicks****:** This generates the **click** event that fires on all outbound link clicks leading away from the domain
- **Site search****:** The **view\_search\_results** event fires whenever a user is presented with a page containing search results after using the search function on your site
- **Form interactions****:** The **form\_start** event fires when a visitor first interacts with a form on your site. The form\_submit event fires when the visitor submits the form.
- **Video engagement****:** This event tracks video starts, progress, and completions of all embedded YouTube videos on the site. The event names it generates are **video\_start**, **video\_progress**, and **video\_complete**.
- **File downloads****:** When activated, the **file\_download** event fires whenever a file gets downloaded on your site.

### Recommended Events

Unlike automatically collected events and enhanced measurement events, recommended events require you to do the setup work.

For these events, Google recommends a name and specific event parameters to use, and you do the rest.

Ecommerce events like add\_to\_cart, begin\_checkout, and purchase are all recommended events.

Here’s an example for the add\_to\_cart event from [Google’s documentation](https://developers.google.com/analytics/devguides/collection/ga4/reference/events). Google recommends the specific event name (add\_to\_cart) and what event parameters to use, but you’ll need to handle implementation.

![Parameters explained in Google’s documentation for "add_to_cart" event](https://static.semrush.com/blog/uploads/media/f6/ee/f6ee6cb1ca29bf4c7de14862c80843c0/7a32ebd147105d3f8c2210a66311724c/AULlwGxfsV_XJadDMRb97VWlxu7hIzYbi30Ai1S1CRJjT3ZtvsWYqiB1Pxq6sXD76wmCZuxnDJRO8lEwzo0KsuR9v421SQ319gBz-SGfMLtTzPIXHqyAQfBR90S9AlUB5YBiStZNod66sXYq6_EZTyw.jpeg)

### Custom Events

Custom events also require custom setup work. Unlike recommended events, Google does not provide recommended names for custom events.

The technical name for the second group is “custom events.” These events will be relevant for some sites but not others. The event list below shows four specific custom events unique to this website.

![Examples of custom events highlighted in GA4](https://static.semrush.com/blog/uploads/media/2b/a0/2ba0f2f956e1059348d4b7f6aa877fb5/5ae283297ec8b171eaa6a7d98759c988/tMR2Gz4E-q6Ymk8fnhnQjZBcLiAuH6ISAxUDOAPHnaEQvWI3xP1HGKsWTvi6Px8AszX1Uvc0Q6lSMevS3pieXh6Krg03q4b12mVnoUvirYamtXgg4vCQXKOb_om7xbGeE3o4zl4c4FSqMpuMak7qy8A.jpeg)

- **The** **cookie\_consent\_visible event** fires when a cookie consent banner pops up
- **The cookie\_consent\_accept event** fires when the banner gets accepted and is not closed or ignored
- **The 10min\_70scroll event** fires when a visitor spends 10 minutes on a single page and scrolls at least 70% of the way down the page
- **The youtube\_any\_click event** fires on external links that go to the associated YouTube channel

Remember that while these interactions are essential for this particular website example, they may not be necessary for other sites—that’s why they are “custom.”

Both “recommended events” and “custom events” are custom because you need to do the implementation work.

To implement, you will often need to use Google Tag Manager to create a GA4 event tag. But you can create some custom Google Analytics 4 events through the interface.

Now, let’s see how to create a custom event to track form submissions that redirect to a “thank you” page without ever leaving GA4.

#### How to Create a Custom Event

You can create new custom events within the admin section of your GA4 property.

Here’s how:

Click the gear icon in the bottom left of the GA4 interface to access the admin panel. Then, click “**Events**” within the property settings.

![“Events” selected from the GA4 property settings](https://static.semrush.com/blog/uploads/media/1c/4f/1c4f021535d4b5be266435a35fae4c89/6b670e3fc1817e480c8b0bf742dfb78e/sEpzyE--yt35YpLS7yBoyXZUp4V1HkPfomsnNpb35nmJaRVu9kHhCBpmUM4r2zxpR1UHyhTYisrj3BLR9Lh4K2RLCp7J6__OaCRnmeoCh9Cr5jWVeZHH5qjBYAUPmDsbLhhuhaGC5tdoIaVRZy_bPK4.png)

Next, click “**Create event**.”

![“Create event” button highlighted in GA4](https://static.semrush.com/blog/uploads/media/b1/19/b1192264fb43d7c0bedacf50d06ad326/5419a16a20531fc2ae2aa1da2039a206/GKn83s4hnaXVArNHlWaaRTv3Y5hSUE-D_zreYclY0GQi2dbHY4-Fo76FERdf08vAsCJIvgERlWp5RIxSvsGNi88mcGlLSmFlKGl0ohyxnmCXluYoF6myNoq4SxgI5YCHQ7cRa9G684XcBhGpaFKrTco.png)

Click “**Create**.”

![“Create” button highlighted in the top right corner of GA4](https://static.semrush.com/blog/uploads/media/f9/b2/f9b2f7e716e040961de03ed40e466592/929f251e6ae579eae6bca158249dcc80/BD5UtLpOYfS6zo6xV1XE19j8ycVL8DRbx9QB1eBb2iGBg0952TJy0cqaXDpp9KPQlbksVi6AtM1fOHZHmyOMN5YT4R-OgZP0-x-KJZE4jcxdROoUf75d5zfIn31OKfkNBvgfoR7Mk8QHULF3LOvcNO8.png)

Now, you can configure your new custom event. First, select your custom event name. This is the name that will show up in your GA4 reports when your event fires.

Google has a specific [event name recommendation](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtag#generate_lead) for form submissions like this. You should use ‘generate\_lead’ here.

Now, set the conditions for your event. You’ll need two conditions to track “Thank You Page” visits. The first condition limits your event to only fire when the event\_name equals page\_view.

The second condition is when the page location contains the URL of your thank you page. You can see the page\_location event parameter contains “/thank-you.” If your thank you page ends with “/confirmation” or “/success,” you should update accordingly.

Click the check box to “Copy parameters from the source event” to keep the same event parameters from a standard page\_view event and pass them to your new custom event.

!["Configuration" page in GA4 settings](https://static.semrush.com/blog/uploads/media/f0/e8/f0e8de051879d6d26b8e5fdfc7cb4545/f33ed37daab4e7c45b0547c17508d242/xUofh0BAzvQP_vwqdCBiWNO34b5_y1D7WKKYAathRGzPxC5qh00o3XCvQTzOiQCmvMirXX5FNPX-_C3-AuIkV8gwHfjVQbNiNWxoUQMwfeNUtP-dDIA-ARbh1aZJpVcQrER5e8MpstogXZu5ei4OPC0.jpeg)

Click “**Save**.”

Your new event will now collect data as the event conditions are met.

## Tracking Events in Google Analytics 4

There are two places to look in GA4 to access your event data.

The first is the "Events" report within your standard reports. The second is the advanced explorations area, where you can quickly build a custom events report.

Here’s how to do both, starting with standard reports.

### See GA4 Event Data in Standard Reports

To see a full list of your GA4 events, click the "**Events**" report within the "Engagement" reporting area.

![](https://static.semrush.com/blog/uploads/media/29/f3/29f33edad699a987393625cbbbc76d28/f9d6660fa5184435461de9cd156c46cf/IrRDWmTVrBC8-7F_Wtj8TtHrXLbXwStHyZKYLg2B2mFmR507sFSdlVZDPr6Uc5VvI42iz501_EeiikxYNOBms_9wglaPFXkSh4LFjQNGDOy8axhvODFWVhzotnKSaMKjCQI7jEx3839ogN3Qtt1NWPs.png)

You’ll see a list of all events sorted in descending order based on event count. You can click into each event in the list to see additional details.

For example, let’s try this for the add\_to\_cart event:

!["add_to_cart" event highlighted in the GA4's](https://static.semrush.com/blog/uploads/media/95/c7/95c77c485aeeb57b14a603d67bfe4fe0/45e9c97ee20499f174f3a70b002c1053/fPQXNoXTzUcu99vBsBI5UMbeKHBAtC-fRJWRD1kLnx9YPxR_3KKmUy4PZ1phyQHL23l6cLwbCvHRVFGMH2f36nzSLXFyoafMYFfL_Jrbns8V9lPzy457Aa347FAe1ZBCX4ishG-fKdcJmkS5dWAs4EM.png)

If you click on the add\_to\_cart event, you’ll see a graph of that specific event, including the event count, total users, and event count per user.

![A graph of "add_to_cart" event, including the event count, total users, and event count per user](https://static.semrush.com/blog/uploads/media/5b/a5/5ba5f0db4cda6f9a4c5642b07f2bc644/45323c255be5a05f8c0bc88b41324a2d/oH0H4CNY6N-aF6qitRLEmkb0DOFE4Hpz2gxq1-hN6Z4zGf8A-R9jcY4PT2GBto7NilA52iWRrGHAXkqhR6rp9h3wnssxTEkKdNQAPKb2sR0AaCCUR0HrFY6KMNtZq3H2EWFiiWVmYp0B8_sRHVUm9Ps.png)

You can also see event parameter information for that specific event. Below, we can see the page\_title event parameter, which shows where the add\_to\_cart events occurred.

!["page_title" event parameter data](https://static.semrush.com/blog/uploads/media/23/88/23885638a37fd1c91221a994b959fe23/0d704e38f9d1aff907e80f6e4317dfa6/UWoQPZ2njMg17XDSjbcwbXYS4hDBm56lbHXPYMRhYY8iKJtf70c33aKxYeDq8YCK09Itiui-_FyXjf9xIKghXWI4bdHBoesgwSOhZZtM_rQMxQDFVtLwRaZgGkBUQ6PiQGO77GDCkZ00zOqBzEeKWEk.png)

For a more profound analysis, create a custom report with explorations. Explorations are more advanced reporting techniques that help you understand customer behavior on a deeper level.

### How to Create a Custom GA4 Events Exploration

Explorations work well when you need an in-depth report about a specific event. Let’s walk through how to create a report showing which of your external URLs drive the most clicks.

Go to "**Explore**" in the left-hand navigation.

![](https://static.semrush.com/blog/uploads/media/00/e2/00e2536a31e9485ce38c79ce7431195a/13820857abb824351e5787601c2a1fe2/iEBm991dXV1xzD-sdgerzWHqHizzefQNvVWLqt9MYVbr7PKFHDKVCpY2sSPDChIy2NfmrrNNNTXT3uSBk9mWWBQ3wHn6O_QH8B4Gt0ObJ5C8gem_Bsy4tENO3FYc6BtsQxdY5sykF3GbWyq-9UtOh7w.png)

Click to create a "**Blank**" exploration.

![](https://static.semrush.com/blog/uploads/media/7c/5c/7c5c21b345a4567b9c82da6512475a0b/f0b5ae041d919f39bf22495e9f34205f/Xr9TIt44R_J8a7Aw0RYOhjj_Q_nKdERVLPP0ehxe-sX7r3_DbTJAAVMKk3pWFF_MZbJ6J9zK0Q2TzhBINifsED80PaH_QGICaSdGwR1SR3Nnkn2Pba94s6d7GTJoIVzfES1E_50Kqn0efVVMFzWc3I4.png)

Click into "**Dimensions**" within the "Variables" of your exploration.

![](https://static.semrush.com/blog/uploads/media/57/0d/570df104425e0a90d6a05f4018541046/aa2a8aca98a9654b26129fc2cf3a0c52/sV8UGkX9o0HqgImBA47i55I6B3CcM2FonNbVJJ0lgm_chtSj5Ih5bri4jvc7NhdnqSxy8YTyNh9tgy1vTg6fcoe4DBmm4JhIQ2GJ5L5qc23amJ24EaBGF8oIFuWby6C7ujYHiEJIC0KM5DgBL8XWRaQ.png)

You’ll now search for the two dimensions you need for the link click report. First, search for "**Event** **name**" and toggle it on.

Then, click "**Import**" to add it to your custom event report.

![](https://static.semrush.com/blog/uploads/media/e4/4d/e44db91092e267e8109735ac2460718a/af5a870eb51b61738563335a6ce0fa98/NEzujHvTGz6-UZ5xsqrwbCMBHmaMgXydIQMutN5O2_HvRdIXlfn4lhLEMBb89zhwd3h9jFwxYzuXo0_Okst-zh4Y7gdvvVktJGZ1Eja6KWIx51OTsLSxukfsH78sdJDKsz_ycrBmOYyPk8ADi33-tBc.png)

Now, search for "Link URL" and select it with the check box.

Then, click "**Import**."

![](https://static.semrush.com/blog/uploads/media/d5/5e/d55e4cc97ff841a826a3370c37781d66/eddc8cd633416f2bcfcfd82e1c588953/2VUGdrJoZILiC_tNUt8SpEWc9IcxRtJOWTIyfzQAXPNFSnyUDesiKRwMDlHRgecJEQS5ok-2tRSksCnCBPUm7rpkaYY4g_-yieTgwmxxhbMsYddZgcvErbFCR2OSZTvb84eoMUAjlPrgtqNfG3VcK3A.png)

Now, click into "**Metrics**" within the "Variables" of your exploration.

![](https://static.semrush.com/blog/uploads/media/1e/e1/1ee116c21aa22df7f1b1a618865d9c62/b94f4e29885c7524846ff31ea7c13549/IWw7aPDE5u-FJZ8UiOonaeKeIAfqFbKN4zmhFJC_maYUCKxne7Zh6M4TDI1cGhpeNgHamrmW-0LoAomgHySaITu3qHs08fSRBPpjPwpABVZFs59TeCZkCMf4zb87Ecax9152jzqrV9ssa1qhUNtFaAY.png)

Search for "Event count" and select it.

Click "**Import**."

![](https://static.semrush.com/blog/uploads/media/a3/d4/a3d4477416c369d41f3be5f3cf11a276/9c19c1ac63236c916d0fde07b20368f2/bi9pwlBXiCTm9-4RP5UHG7hXPjrROje1tvhqIwVl8aBsbSdT2SINUUoRd31aC5XK4KCrTe9P_YUEmXlBnNsHjLE70BAa_2rVFkCEwcR_nUTdTJGtQCkWUpdQAOd9eoEP6n8v941Y1zZMGA_du-WNMZA.png)

You now have all your dimensions and metrics available to use. Double-click on all of them to add them to your report.

!["Dimensions" and "Metrics" list in GA4](https://static.semrush.com/blog/uploads/media/cf/4a/cf4a0852c90e7c68e511044ec3e0c000/131ff2ea915f2efb2194837b0281a41d/IYyjmtDJBpaXQesG-am9NJRS7Vtgz1OzZ1uESMqjU4XG2y896BzovTJsxv6FqF9ZCamITTCJ7PRsXJtjIey0E2zDlzRo2HTXW_Wna-fu_KWq7rOTMqAmGPsyM6ZVQdPDYGhWNuubSD6pGsk7BePn3jI.png)

Now, you’ll want to filter your report to only include the desired event.

Scroll down to "**Filters**" and click into the filtering area.

![](https://static.semrush.com/blog/uploads/media/c5/55/c55526e2e0b4b3f767b4c6b4618c7aec/f11cecfa48be30cceac8d569c4a51602/YoBF0e2WZP-uXM7VFhe9h2VazihN6nTwrWry6X_0L5PzNc8vy0mInsLfi55PGiaaZzR-zGYduyjt8V00xeRqznJfKa_xCiud2gKCE0Oz-ru0SyrL2aZ6EWnBjKZNQ54_7YSpmFwYwpycQkriXzb9Nyc.png)

You’ll be able to apply filters based on the dimensions and metrics you selected. Click "**Event name**."

![](https://static.semrush.com/blog/uploads/media/0e/2e/0e2e2e8c66235a68e023a3a009182fde/2531dacb5491d7b83eae5ea240275469/dtUQNKylLaxuZTPHUG7eR7Iu0NSoqUEkofkicTf0z1auOWQF42EamH-3UWDAFWR6kxrxNrzAsmp4X-EC0Z1Q4cakywwwJ7drLj5QvgbXLJa8WNuCt8SVgpIzUbK44wfgAApjtLHLCEKBz25HBMknBo8.png)

Now, set the conditions for your filter. To limit your custom report to external link clicks, set the condition so the event name exactly matches the ‘**click**’ event.

Click "**Apply**."

![Filter set so the event name exactly matches the ‘click’ event](https://static.semrush.com/blog/uploads/media/4e/8a/4e8aab7e272fdd75539235f44c41735e/abf7e2904f9639202bc3496b2aa23d77/u_y2zDLhzr8H7F5z_IHcfYIJqFbURWK23eieEDaaHDgoXvMK9Ttbjy9dRptuO_DHuZEAX5RdZz3u6Cb-RZI0NMvkoRUInu8zQONScrfpRVR9wNER4f3y9czfgnInjVcA9DLw11PHS3DFekqU0I__riU.png)

You now have a report showing which external URLs get clicked most often.

!["Event name" report in GA4 shows which external URLs get clicked most often](https://static.semrush.com/blog/uploads/media/f7/8f/f78f44e8374006e0d67d2fa77f359eab/9bf1a191d23b3731a8817df2b04c8984/5lX2iT2_4JS-HSMX_02XT42jawSH8n5t7iCTN8CWSsrnkz_tB6GB_cWCRlFkkJWqymv71n15ZeZ2jRtR8Z6JYF_wR-Fl8WJcj06EGN-utjb_jABmLtfQWdVhP7dtHnu0ol3SJ10UKGw_7ZVvZUk91UI.png)

## Using GA4 Events to Improve Your Marketing Strategy

To get even more from Google Analytics 4 events, use the data to enhance your marketing strategy.

Here’s how:

### Use GA4 Events to Refine Your Marketing Campaigns

Here’s a simple way to use Google Analytics events to enhance your marketing campaigns:

Use the custom report you built above to see what pages on your site drive the most clicks to [external links](https://www.semrush.com/blog/external-links/).

Why?

This data will show you what links are already the most popular with your readers. You can then use this information to prioritize which links to add on additional pages based on your specific site goals.

Another way would be to use your most productive landing pages to help drive your [email marketing](https://www.semrush.com/blog/email-marketing/) strategy.

Let’s imagine you run the email marketing program for a global company, and you send country-specific versions for your three most important locations: the United States, India, and Canada.

You can use event data within the landing page report to improve your content targeting and performance.

Here’s how:

Go to "**Landing** **page**" within the "Engagement" section of your "Life Cycle" reports.

![](https://static.semrush.com/blog/uploads/media/8a/0d/8a0d18130acc0790261b58fd71f2f9cf/ed6ea46260ee08162b73398e98b185f5/hy_jCnL-GZAnNgieQmPcCua5M9kdE4rpuL0eXu7-kkprvWqVurh4rvcQDQRwjFLd5-8KPeJLXh6YSmlTVwpln25HVmbbiFw9SsW7VII5sBqlMhAYvk9AmOYOzeDjMjhKCQoq2GEv9ZlbvFGf7Wwh4RM.png)

You’ll see a report of your top landing pages sorted in descending order by sessions. Instead of sorting by sessions, click the arrow to the left of "**Conversions**" to sort.

Now, click the blue "**+**" sign to the right of "Landing page" to add a secondary dimension.

![](https://static.semrush.com/blog/uploads/media/bc/5e/bc5e9465d5bf24a535e5e5105f55fbd4/223e93c750a30d63c2d0cf58a935f2b0/h35ICNAJhYIgQ03in4TxY4BkiNMKcPusBhKvPOjJr9CUSRKwT90EWGpdLZdygbQxNQVqQ44YO-u3PanFbvUH9YCCbUCEmTTD4Hvxlufh5tufnkL6j_YUmz4s32G9MQabr7Hqs8yjqOQsg4mC1DgpR-8.png)

You want to see how many add\_to\_cart events are occurring by page and by country. Search for "**Country**" and click it.

![](https://static.semrush.com/blog/uploads/media/0d/3a/0d3a963f69fdb844a568650222433ac1/333feb23ae302ac3fdb5da566f3f3be9/xUj0aqHnupRBohI-GfmVvo5JOw6wIDckn6if30-z1teXz__6bDppciUt7WywEpmnyc683tXSmjCPq5F6KSCIF1p0eVbvEcOh4LY_tQIfkV_ZAzUE0LsGenutHmylZg5AZfzWnd6GJ2mdex-P9LR-RL0.png)

Your landing page report now shows top converting landing pages based on the country of your audience.

!["Landing page" report with "Country" column highlighted](https://static.semrush.com/blog/uploads/media/80/d1/80d1ebec0801a0ceabe37d03ad49685a/471ca3fc2d382d81a1c6f0c29daa5704/SQ3QaPuF8b3fvxk-Rq8fIHWAa7SXfb5qP1jiW9dpxEmorro9NxtS_3ECzxh2ZW7MXh7vg8NztNtz_kDdBi28ztAfOIpsC6nx8mxqg5up7cCrpxwf3HWs1Yyxx7xZFNZQHfLzL1iD0QnqFTvbSnEEsM0.png)

You could use this information to prioritize different landing pages for your three country-specific emails.

### Combine GA4 Data with Semrush Insights

Power your marketing strategy to greater heights by combining GA4 data with Semrush tools.

[Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) combines data from your Google Analytics account with Semrush and Google Search Console into a unified dashboard. It helps you better understand what is happening on your site and improve your SEO strategies.

You can quickly see your top landing pages and get a snapshot of your organic traffic performance based on traffic and keyword ranks.

!["Organic Search Traffic" report with "Keywords" and "Conversions" columns highlighted](https://static.semrush.com/blog/uploads/media/1d/4f/1d4ff99dde8d6aaab82545a16968e85f/b7ce49edb0457fe7f0c5a5dc33167a84/AmNtXSb7GqrhLe3QxHFIB_Xad78qhghbcVOD6Ai-phj5wNJMhM4U5fWOb7wD_V96KZYgGqVnBEQs6q7KmNioUdfG3pSkEYxirc1X9B0wF5KgzQYjj7kGzk9g5yi2H7g0pwK3NLbIqEmul_PIK2ErPmI.png)

If your goal is to drive as many conversions as possible from inbound marketing, this tool will help you focus your SEO efforts where they can have the biggest impact and use Google Analytics 4 events to the fullest.

Ready to try out Semrush to improve your website’s performance? [Start your free trial](https://www.semrush.com/signup/get-free-trial/) today.
