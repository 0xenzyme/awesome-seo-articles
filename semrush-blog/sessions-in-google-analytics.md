---
title: "What Are Google Analytics Sessions & How Are They Measured?"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "sessions-in-google-analytics"
url: "https://www.semrush.com/blog/sessions-in-google-analytics/"
canonical: "https://www.semrush.com/blog/sessions-in-google-analytics/"
author: "Zach Paruch"
published: "2021-09-27T19:39:00+00:00"
updated: "2023-03-15T09:10:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2023_aging"
  - "time_sensitive_title"
schema_genre: "Analytics"
fetched_at: "2026-06-12T19:43:27+00:00"
status_code: 200
html_hash: "d03c202fe5a49024e59e5fe822f4127423869f11ef80002bb4bd095d10b4156f"
clean_word_count: 1841
clean_char_count: 13691
---
# What Are Google Analytics Sessions & How Are They Measured?

## What Are Sessions in Google Analytics?

Google Analytics sessions track a user's actions on your website during a single visit. A session begins when they arrive and ends when they leave or are inactive for 30 minutes. Actions they take while they are on the website are recorded as part of the session.

Think of sessions as containers for all the actions and activities users perform while on your site.

![sessions infographic](https://static.semrush.com/blog/uploads/media/51/ad/51adeefb09cd1d30acdfc89a1a369aa2/td-eCj8dNPoLGIiQrMjFHtSRurMYVlIoHZ2I1OFF4h9tZoMGpQkHsGfJoTE5QLU-1MtdXg7cjUaDgQD6lVwl4MZ_YF9mcfGhFGzV6vrhA82OSp4QVrwpnrPjUnT8Xc4ZEDMs1FDCZHJnqUU0-2v4BsM.png)

GA sessions can be as long as several hours or more.

A session can contain multiple hits (e.g., page views, button clicks, events, and transactions).

Or it can include only a single page view.

And a single user can record multiple sessions a day.

Sessions tell you how much time users spend on your site. As well as what they do on your website during that time.

### Google Analytics Users vs. Sessions

In Google Analytics, a user is an individual who visits your website and starts a session.

The users metric records how many individuals visit your site. The sessions metric records **how many times** those individuals visited your site.

A single user can record multiple sessions, but a session can’t have multiple users.

As a result, GA will typically show more sessions than users. Like this:

![users and sessions in GA](https://static.semrush.com/blog/uploads/media/f3/8a/f38aafa8a5603984d6d763d57f7b8c98/qV23Coc6YiyZaf5feCzdlA8TeqjYiijsuvzp7fESXUI6BjB_uTL05ANHJgBwnNQJkkljBI16Ywq_PV77AuqLn0nM2FmiSLH9i1Wo9z1L_d-KU1HphGZ1OzLDFyTDBfULUC1r9VdvwL12CHj2YYYVC7o.png)

### Google Analytics Sessions vs. Page Views

A [page view](https://www.semrush.com/blog/pageviews/) (or “view” in GA 4) is a single instance of a page on your website being loaded (or reloaded) by a user.

Typically, a user starts a session with a page view.

The user can trigger multiple page views during their session as they browse your site.

A single user can record multiple sessions, and they can log multiple page views during each session. That’s why Google Analytics often shows more page views than sessions. And more sessions than users.

## How Does Google Analytics Track Sessions?

Google Analytics uses cookies to distinguish individual users and track user sessions.

When a user visits your site, Google Analytics starts a session, sets a cookie on the user’s device, and assigns it a session ID.

As the user interacts with your website, GA tracks the various hits (e.g., page views, clicks, transactions, etc.) and records them as part of the session data.

When the user leaves your site, or when the session ends, GA records the final session data.

## When Will Google Analytics End a Session?

By default, Google Analytics will end a session when a user is inactive for 30 minutes.

If the user comes back after 30 minutes of inactivity, a new session will begin.

Conversely, if the user comes back before the 30 minutes is up, the original session will resume.

In Google Analytics 4, there is **no limit to how long a session can last**.

### How to Change Session Timeout Settings

You can adjust how long users must be inactive for their sessions to expire in both Universal Analytics and Google Analytics 4.

But before you decide on a new session timeout duration, consider the following:

- If your site logs a user out after a defined period of inactivity, consider setting the session timeout to match that length of time.
- If your site contains a lot of content, users may spend a long time engaging with the content. Consider increasing the session timeout duration.
- If your website has a small amount of content, consider shortening the session timeout duration.

If you decide to change the timeout settings, keep in mind that the modification will only affect future data.

#### Universal Analytics

To change session timeout settings in Universal Analytics:

Select the gear icon labeled “**Admin**” at the bottom left of your Google Analytics dashboard.

In the “Property” column, select “**Tracking Info**” and then “**Session Settings**.”

![navigate to session settings](https://static.semrush.com/blog/uploads/media/62/1e/621ecbdf61c9769f6ce0a9a116b9b1ae/iFy8X-O5vgwK9H6rtt62XeXHn07NQXbqydaC0yeLC92Y8NSLq0cXm5enYlDX-vvXiY77mWInCB5xAuozfvhjwpVp4SYh9vIKtQ4jqaZrq2O5Y5lrANTYxcJkmDj1MDDkjvbR1ZlxhdXStxXORb-xMlg.jpeg)

Under “Timeout Handling,” use the drop-down menus to set your desired “Session timeout.”

Click “**Apply**.”

![timeout handling settings](https://static.semrush.com/blog/uploads/media/c8/1c/c81ce66bcaf86fe171b6eda3f42e64f9/R6pJm1SCQX83OLYw8gHy3vkx_ghnWCepvRHdhlcFOU9NsGIuDCBg5qqvM9Tg-6ltS_MWcjncPF8-Vnnh1IarhvrXlLx3cjJW4F3vJCMqLAgdyszPTxQiD-heR4LFRP-k0q2NXVyDP1kVojG_jH-tZH0.png)

In Universal Analytics, sessions can be as short as one minute or as long as four hours.

#### Google Analytics 4

To change session timeout settings in Google Analytics 4:

Select the gear icon labeled “**Admin**” at the bottom left of your dashboard.

In the “Property” column, select “**Data** **Streams**.”

![navigate to data streams](https://static.semrush.com/blog/uploads/media/74/9b/749b603cc20d741c95144ea477a32738/UQuY9grTymdcr2JctHnA8rOMWkq5Yu2--tDbiTxFNHAYoG6i-6-rlRpgu0fH8HzzS-4trOc1lZxmt_fVriVO_Uq3mklxCc6jLlqbDAAVmFDR3agB08OoZX60ExIDbpc2GemTSXUHmHgY63H3sz_7nbk.jpeg)

Select a web data stream. (You should see your website URL here.)

![select a web data stream](https://static.semrush.com/blog/uploads/media/ab/0c/ab0c0078a56c24721aa289b07b5d327a/PTo26rE0y_Ot30Gg3b4_GQGofX8bS2_zY1qk30PUdeaKFMAiHD7jyf_CL4GA0k8VctfjmDUn6Ow9JsWTneJWivI1eHhPcZ5Rzq_6CetRLeOZy5Dhf9HuohM7_9G9UFaUPROkGeetVCY5H_7Zrfim2XI.png)

On the next screen, scroll to the bottom and click “**Configure tag settings**.”

![configure tag settings option](https://static.semrush.com/blog/uploads/media/23/d9/23d92c3524dd96c2c798ac7707a6e11b/phefrfb7spdnuqfttYcL8CaL7udPnnb9aWNfp1QKuQdXWPKJ2uUshZWCYLHHOPAsVHTtP3RBE5JMsX38qun8WFAVistP9Hb1Z9ylXeZ9paWh5QTuCV2V344Mg-jI0zr1XWdW8uouixNMujnrw2i1f98.jpeg)

On the next screen, under “Settings,” click “**Show all**” to reveal more options.

![see detailed settings](https://static.semrush.com/blog/uploads/media/52/9d/529d4be04680926922c570a6d636e9c7/DfPzRa2L9splrsB7o1tNaft_d7Vob2T7nKe2hE1o2IBfDfp11rBL9QOL-dmGiYnWCkSHJ2NIq3k5Oif5LqE-qNhTKW_2KvjnWSHSTIN1xqVfU3Z6u-vEFS8SVooX6N4-1h3tlIxb-eT6NKJBUyIk-Wc.jpeg)

Click “**Adjust session timeout**.”

![adjust session timeout option highlighted](https://static.semrush.com/blog/uploads/media/37/a3/37a3fd295296768dd73305851d2282f7/CaMjOakCPvhW_7qa9p3ULKIeWqYbQEiEyu8MNJMhWCLWIJae1gRZnvySedr3Z-q_Fq7he3gu2Z24Ta7fTgrDWUGZDs9FUxf5GXByfodIwB6T4Irwc-UmV6onrltFhcjydEWalKOEUNwIF6GHvYn1gCM.jpeg)

Use the drop-downs to set your desired session timeout duration. Click “**Save**.”

![save button highlighted](https://static.semrush.com/blog/uploads/media/da/53/da53c810dc4feaf43721d4ce1acc4af2/iSqzJ_spHaic8Xf0mVabPmqnyPwF6kQWaV1GkTcPJlQ6zD1d7BzV-71NhLoHkU5BRedOXBAdaqgvGodm6jNsx3fDMzIBnLCZ6jUXsSSd_wPGEMuqREIgOYpO28NgRe9DhvtBBiaXvYVt7DUMR8xVMog.png)

In GA 4, sessions can be as short as five minutes, or as long as seven hours and 55 minutes.

### Differences Between Universal Analytics and Google Analytics 4

The number of sessions you see in Universal Analytics and Google Analytics 4 may differ due to the way the respective platforms end sessions.

While both analytics platforms will end a session after 30 minutes of inactivity (by default), Universal Analytics will also automatically end a session at midnight (according to your time zone settings) and start a new one.

Google Analytics 4 won’t start a new session at midnight.

However, if a session goes past midnight, it will be counted once for each day, despite being a single session.

Additionally, in Universal Analytics, if a user picks up new campaign parameters, it will automatically start a new session.

This means that if a user changes their campaign source (e.g., arrives at the site using a different Google search term, an email link, a referral link, a pay-per-click link, etc.), Universal Analytics will create a new session for the user.

GA 4 doesn’t create a new session when the campaign source changes.

Lastly, Google Analytics 4 estimates the number of sessions based on the number of session IDs assigned.

Universal Analytics, on the other hand, uses sampling to infer session numbers for larger sets of data.

This means there may be data discrepancies between the two sets of session data.

#### Engaged Sessions

Google Analytics 4 also provides a new metric referred to as “engaged sessions.”

Engaged sessions are sessions that last 10 seconds or longer, include one or more conversion events, or include two or more page views.

The metric is automatically populated, and you can adjust the 10-second threshold up to a minute.

## How to Find Sessions in Google Analytics

You can find session data for your website in both Universal Analytics and Google Analytics 4.

### Universal Analytics

To see how many sessions your site got over a given period in Universal Analytics:

In the sidebar menu of the dashboard, select the “**Audience**” tab.

Then click “**Overview**.”

In the “Overview” report, Universal Analytics displays the total number of sessions for a given period.

![sessions in overview report](https://static.semrush.com/blog/uploads/media/ac/34/ac34d7da7b6b906a3794809cb8669f67/_D3YSf_mssw9rAAh4MyNgqE1slA2b_WGCeyza24u7ZR9L39ruSbKVXq27Ak8OXm1YkQC-6R_Hq1El_MJPxDokLR8vkKvSf3rgBqIHByJZt9Zoe6bqXdNRltbqaoUSfGPDbZ-9TzJ-XZLDW5nWkUsAeA.png)

By default, Universal Analytics will provide data for the last seven days.

So you’ll need to adjust the time frame using the “Date Range” feature at the top-right of the page to see more data.

![adjust the time frame](https://static.semrush.com/blog/uploads/media/73/87/7387dfe91f32e1d1628b7fc63d806752/ilkfVWY4Mo52vyeJst6ASALbtGaas6ir-fC5_kBZdWWdQIxNqa_sYYV5K3W_7TQ5g3cbOZ2aOG9rfM0Lr_log1ccn4vG_W3wn5OTVlCMKY0KdFU-X2Er-boa_h3HRf42mWynOW_TE_Z_lGKDQ2xyApQ.png)

You can view data from the first day you set up the tool on your website to the current date.

You can also compare the number of sessions year-over-year or within specific periods.

### Google Analytics 4

To see how many sessions your site got over a given period in Google Analytics 4:

In the sidebar menu of the dashboard, select the “**Reports**” tab.

Then select the “**Acquisition**” tab, and click “**Traffic acquisition**.”

The “Traffic acquisition” dashboard provides session data for the last 28 days by default.

Use the date range selector in the upper-right corner to see data for your desired time period.

## How to Use Google Analytics Sessions with Semrush

The [Organic Traffic Insights](https://www.semrush.com/kb/588-organic-traffic-insights-manual#2) tool gathers search data for your domain’s top landing pages into one easy-access dashboard.

Once you [connect the tool to Google Analytics](https://www.semrush.com/kb/939-organic-traffic-insights-google-connection), it will display metrics for the top landing pages on your domain.

These metrics include total users, new users, sessions, pages per session, average session duration, bounce rate, and even goal completions.

Organic Traffic Insights can also provide data on the “not provided” keywords that GA can't report on.

Combining data from these powerful sources means access to accurate data that can help you improve your organic search rankings and user experience.

To use the tool, find [Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) under “Keyword Research” in the sidebar menu:

![Organic Traffic Insights](https://static.semrush.com/blog/uploads/media/a1/e2/a1e2c46a2c9407ca4b698576f531c318/MbEszW9PnLCtMqP7_7DTT21_UPhU9sFd7f9v0XAK9NTy3xRSI3uaB3tUANTlBsfUXoOh_SvHJmT6Ykl7RcR3R_6oNwmJIAJHL_6xr4RC5ttAziY2pP1wB6LgoeYK-TWpfu9a7KKQe3GHA22YPKqpqYc.jpeg)

You’ll need to have a project created to use the tool.

If you don’t have a project, set one up by selecting the “**Add new project**” button at the top right of the screen.

![add new project button](https://static.semrush.com/blog/uploads/media/cf/fa/cffa25b78076ec6f946a720fd6d64492/d0hSbkfff2w2SrKao5Bz2vuTOvejAVCi-vHg4q6E2K6CKoqMj7gHzxRoHdJkCMi_x7QSs0SQ2mDxi-s-iqPD8DmWA7GPhO8X4KTV-hNxKXyXrSTKlVT1SQwDVFyOS0byO7Z9SRvlzmj5PCNDG4Sj24Q.jpeg)

[Create a new project](https://www.semrush.com/kb/243-managing-a-project) for your website.

Open the Organic Traffic Insights tool and select “**Set up**.”

The tool will prompt you to connect your Google Analytics account.

(You can also connect your Google Search Console account for even more valuable insights.)

![connect your Google account](https://static.semrush.com/blog/uploads/media/38/5e/385ecbdc3e50a83589bef1c8007c1bca/yevmmFB2tySd24sw1jqcW-ZoYQGb-f7WAND8mw4bZYS_NEanDvLskwiM0j2qWFfgY4CMvZ3EWuaURB_KfOax35e6aaPyrd_j035QzOvYdVe5P-6GFU7pQj4eO2L29-yPjkxSeqFVOt2BDoR5Cup5VRk.jpeg)

Once you’ve set it up, the tool can provide metrics for each of your landing pages.

![landing pages metrics](https://static.semrush.com/blog/uploads/media/87/03/8703c050a8a6b705f32205133c3588f5/EI29p-5BTv-x7Ivj267Ric5YJ8feQ7qf7Y2EkGb3MZUUaUIl-eup7h3i2OIySS4TXC39GytDhp70oZpx514ywzKeygRsY-cVpuMmuN7Yjid0CA-EyUe305YdbGeM3bPWU7nF96aqJM7d3rN0ntKOXis.jpeg)

Organic Traffic Insights helps you better understand what is happening on your website. And improve your SEO strategies based on traffic statistics and invaluable keyword data.
