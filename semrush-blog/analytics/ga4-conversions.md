---
title: "How to Set Up GA4 Conversion Tracking: A Step-by-Step Guide"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "ga4-conversions"
url: "https://www.semrush.com/blog/ga4-conversions/"
canonical: "https://www.semrush.com/blog/ga4-conversions/"
author: "Zack Duncan, Martha Vassallo, Boris Mustapic"
published: "2024-05-06T13:47:00+00:00"
updated: "2024-05-06T13:47:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2024_watch"
  - "time_sensitive_title"
schema_genre: "Analytics"
fetched_at: "2026-06-12T15:27:25+00:00"
status_code: 200
html_hash: "adaf5921d1363c218a5183667256b0128c251bc5ea4dfa9cacb8b6105a438639"
clean_word_count: 3822
clean_char_count: 30290
---
# How to Set Up GA4 Conversion Tracking: A Step-by-Step Guide

***Editor’s note****: On March 21, 2024,* [*Google announced*](https://blog.google/products/marketingplatform/analytics/evolving-google-analytics-for-more-insightful-measurement/) *“conversions” would be renamed as “key events.” GA4 will continue to use the term “conversions” in only one specific context: reports that measure your Google Ads campaign performance. The rollout is gradual, so you may still see the term “conversion” in your reports. We’ll update this article with the latest information once the transition is complete.*

Google Analytics 4 (GA4) tracks web interactions that are important for your business. They’re known as conversions (or “key events”) and relate to how you achieve business goals.

For example, a completed sale for an online store is a conversion. The same goes for a form submission on a B2B site or an online restaurant reservation.

In this guide, you’ll learn how to set up GA4 conversion tracking for your website. And how conversions (key events) can help you understand your business’s performance, so you can make your marketing efforts more effective.

## Why Conversion Tracking Is Important

Conversion tracking turns [Google Analytics 4](https://www.semrush.com/blog/google-analytics/) into a more powerful tool that helps you understand if your website is doing its job. And lets you uncover insights about your site and web visitors that can help you drive more business.

Let’s say you’re a marketing manager for a dental practice with locations in several cities. And you want to get new appointments from patients.

For you, conversions equate to appointment requests submitted through your website. In GA4, you set this as a key event called “**generate\_lead**.”

Here are three important things you’ll be able to learn about your business in GA4:

### 1. Which Traffic Sources Perform Best

Conversion tracking reveals which traffic sources are best helping you reach your goals. So you can focus your marketing efforts and budget accordingly.

As you can see below, your site produced 112 “generate\_lead” conversions in the last 30 days. And you can add a [Google Analytics dimension](https://www.semrush.com/blog/google-analytics-dimensions/) (an attribute that helps you gain an in-depth understanding of your data) to your conversion data to see its traffic sources.

In this case, you can see the originating traffic source using the “Session source / medium” dimension.

![Google Analytics report showing conversions](https://static.semrush.com/blog/uploads/media/bc/be/bcbe1839602a1226e5eefab24150e79a/2da8914837d73dc3eaa94926957d0ef1/5QMUhVxblQ94nqNn0rrSGgXcjapmIGsLtuvzXve1N6m7a7jEx5k1SpuKafo8Y31TRLP2H8Qx_MneraYE0YB-5CLHd7jiawmBZINCM8JKvYyKHC6lxZ5diN3w0WNZAMPNCJXwJTsh5hPYH3WTz8vIOs4.jpeg)

Based on the above data, you may decide to continue focusing on your organic (meaning unpaid) search efforts. After all, organic traffic from Google drives the majority of your conversions (key events).

You also conclude that your social media efforts aren’t working well. And decide to test a new approach on Facebook to see if it’s more effective.

### 2. How Profitable Your Google Ads Are

Google Ads data integrates with Google Analytics to show campaign performance. Which helps you manage your budget because you can see how much you’re paying for a new patient inquiry.

Let’s say you’re willing to spend up to $300 to acquire a new patient. You can see that your average “Cost per conversion” is $154.30—which is well within your budget.

![Google Ads campaigns report in GA4](https://static.semrush.com/blog/uploads/media/19/33/1933a41c70f8a9b9d496b416efa82ba2/68dde29f6ff8064f134182e2b8e8a413/yW4bKxHblC4d-IX6ah1q8uq8l2NkLP3IWg_7Q0kWON-ipxzILYbg_33zdiDpkGzG5vTNWeMorc0zqOiiy2JFuBDY7RxFAOQgma8iCrdWnQvQGLgT4_JwpO7pXZTNWYg25vGWZP-iQ1wEverhzoIEpXM.jpeg)

The above ad campaigns both generate a similar cost per conversion. Should that change in the future, you’ll have the information you need to reallocate the budget between campaigns.

You can keep an eye on this important metric each month. Ensuring that your campaigns continue to be profitable for your business.

### 3. What Characteristics You Should Know About Your Audience

You can use key event data in custom Google Analytics reports to learn more about the people who use your site. So you can better meet their preferences.

If you’re a dental practice marketing manager responsible for several markets, you’ll want to know where your digital marketing efforts perform best.

To obtain that information, create a report in GA4 that shows the city and traffic source for each of your converting visitors. Like this one:

![a report in GA4 that shows the city and traffic source for each of converting visitors](https://static.semrush.com/blog/uploads/media/38/ff/38ff657b8f3d31252a1541b57b04abf0/b21a8e8ed2ecf2a653122781b1bda981/_WRBzTQGEzzlSeommS7QS6bylPFdaz54EgFMQMLqpf36PBuiCbB6b3Rra8_6VhS3sYzlDWNSTfYxRlTDRB_SNlWaVw0x4Am3dXV0Fn-sa_Nrl_ro_bS2Fb2Z9nB5nsIvgkPUYcgPDDUL0YOB3QdSow8.jpeg)

Now, you can compare your campaigns for each market. To tease out what did and didn’t work.

Or maybe you want to redesign your website to make it faster and easier to use for your patients. It’s helpful to know that over 63% of your converted visitors used a mobile device.

![GA4 report showing devices converted visitors use, mobile, desktop and tablet](https://static.semrush.com/blog/uploads/media/37/c4/37c46fbd4ab35de84be3d15536a96d23/97139e45a97ee8a2a452cf9c52b5ef4e/Pn_1KE0R1LK2mSp3uGr6pKWbpARKBADRFTd99s2RfQK4-cmsgD401OJTytHyfV7Kxk0Nrd7J2BQZRtHCmEKFcOqqv1wjbJx14GkVQuwN-bueMFoXs9wTKjZHFG827RFtjxPd2fEYMd6G6LhBv4FZ9rQ.jpeg)

With that knowledge, you can focus more on the mobile experience during the web redesign process.

## How GA4 Conversion Tracking Works

Google Analytics 4 collects all web interactions as events—visitor interactions like views, file downloads, scrolls, clicks, and purchases. They’re the foundation of all tracking in GA4 and essential to conversion (key event) tracking.

Google Analytics will record some events by default without any work from you. You can read our [GA4 event tracking guide](https://www.semrush.com/blog/google-analytics-4-events/) to learn about those.

But some events like form submissions require you to set them up.

## How to Set Up and See Conversions in GA4

To start using key event information, you need to identify a valuable interaction and follow a few steps to track it.

Let’s go back to our dental practice example.

As with many other businesses, the website generates new customer inquiries through a contact form. So, your first step is to track that important interaction as an event.

### Set Up a GA4 Event

To create an event in GA4, log in to Google Analytics. Click “**Admin**” in the bottom-left corner of any screen.

From the “Admin” area, click “**Events**” under “Property settings” > “Data display” from the left-hand navigation bar or in the main view.

![Navigating to "Events" > "Data display" in Google Analytics admin menu](https://static.semrush.com/blog/uploads/media/7b/99/7b99a289afc6729dcf2bd16a4a43f138/7c0cb28a2fe909a53ebb468433e97f12/0eOSvf7rA_7pBuL3r81ozC5uofQvWcfTC0lUBSv4Pqu67w5MqtgUCPzzE_FcZYgmDSoaytiSOGaJVlkIJsUxUMafGnZh6j8GuB1BJZ-OvU0mHcqePhX4OSXhpUiyHJDFdjfmt79UfMJXCmPBVFXdI8o.jpeg)

Then, click “**Create event**” to set up a new custom event.

!["Create event" button in Google Analytics](https://static.semrush.com/blog/uploads/media/1e/d4/1ed44240ac16337bf9a0be9b7dcc5934/ec4eb2b9bc59dc9a8b12b5854d9dc4fc/kpSQdf7FQmEN_K2qMip5zz7rfaXQkvy5dPyhbv6_xUQaeLRSYj1dv9bWOG_rQXxmzQLqXbfzk70t01x0hnE8dhos4Iq8mjNBUQCIyNOLDZNMFem-OooiKpnYLqZrF9QxYRcsTeSNpoxBC5fXqtwnlE8.jpeg)

And click “**Create**” once more.

!["Create" button in Google Analytics](https://static.semrush.com/blog/uploads/media/70/cb/70cb5b3432204d2b2ab8bfb3e7ded23e/ff032bcd0ed6efa74888e28f1a7f0a9c/QHWZuo7a3VTH-UA4ZmGu6BHl-9kYvzOJ7FMhZssIhmgM-5qW5gLix0HX6BBVN-bC_0gTiEI6uyxkXqonqnL4QMIzeLBVvP2xTW3UyYGSTIJSVMKlTsFq31e7VaLQ41P6uuB2J3FaZW9sbExaGvFRta8.jpeg)

You’ll see an event configuration window where you can start by naming your event in the “Custom event name” field. This is the name you’ll see in your reports whenever the event takes place.

Choose something like “form\_submission,” “thank\_you\_page,” or “generate\_lead.” The latter matches [Google’s recommendation](https://support.google.com/analytics/answer/9267735?hl=en).

!["Custom event name" field highlighted in the events configuration page](https://static.semrush.com/blog/uploads/media/ac/5c/ac5c09a532367f81b518865176b32ea6/b22f87d13b4d9e2242dff7768496cede/6o9N0u5cbzdwSb_pnOLPeW4mJuyBVccvsQcpPowa77U5CEDsG6DURALCTcC-3nXgJ9eO29Nu7zi8HlKTTOFV7a9GlckKN_DzoysZ3BUmbG-MFkz55HTbMwXniHwEfCRGAuFZ5d3VJBirs33Q6ErChm8.jpeg)

Now, it’s time to set the matching conditions that will determine when your “generate\_lead” event fires.

Your contact form redirects to a thank you page when it’s submitted. So, you can look for views of that page to record your custom event.

You’ll need two conditions to achieve that.

First, set the following parameter so the event name equals “page\_view.” This limits your custom event only to interactions where a new page is loading.

Click the “**Add condition**” button.

![event named "generate_lead" with “Add condition” button highlighted on the configuration page](https://static.semrush.com/blog/uploads/media/80/2a/802a0e0a467ff7158e9868f839540ed2/dae9b9ed56e05c15c3e98eeab8f1171f/MYsTy5bqu4rNRsAmKhBDQnfsAEQVXy8mQjss0pT9-k1G-g6cnbgaIwvcjxY0UcmM4oadW78Iw5gzQQRY4Ata5E0AFVZN8CCPAajMdu1PIK1xW74uxkMp6GTY9OzpEFIuP-BM2OvH5vKXA5Ziypydn78.jpeg)

Then, set your next condition to limit your custom event to your thank you page.

Set the “Parameter” by typing “page\_location” or choosing it from the drop-down list. Set the “Operator” to “contains.”

Type the page path of your thank you page URL in the “Value” field. Your page path is the part of the URL that comes after the domain name.

Adjust the value depending on the specific URL of the thank you page on your site.

Finally, click “**Create**.”

!["Create" button on the events configuration page](https://static.semrush.com/blog/uploads/media/05/d1/05d11e105a2b38943267aa5beb755728/e2bb1cd43c7b69233a50b714c843c2aa/OWelLWMh5SQ-kHoK4Cn5UbQiFX6tZ_3kR2GM2k6mFGfDlB9U2fJPrHlQ7AD1QCtTLW0GVhVJmrijZicSCvoAuQGMZ5DaAhIuxZsGDlRnGDkM2G22SrHhkviEdsvavHL-JerrJ69pgoBdqZGBbkEO-h8.jpeg)

Once you do, you’ll see your new custom event in a summary list.

!["generate_lead" new custom event in a summary list](https://static.semrush.com/blog/uploads/media/99/b6/99b60cb7f48cf8c43679b9e308a74e1f/2a4ff4c0b7efedc1885413c107b091e4/uMPJJvK9P6geIkK-bH-jzhYBB56mjroXg_W7T59LXOq06YaqlN2iCAr9uib0WqlZ0AdMxnUeTk3dIqRH6PrcP7wXLSevyIDJKxkOnu6rsjUxnREe97Bj-9Y1aB0phmkSPUSoUBCK6-s3JkTMSC8tFsU.jpeg)

You’re now recording event data that you can find in your GA4 reports. But it won’t count as a conversion (key event) until you take an extra step.

### Mark an Event as a Key Event

Now that you’ve created your custom event, click “**Conversions**” under “Admin” > “Property settings” > “Data display” to set up GA4 conversion events. Then, click “**New conversion event**.”

![“New conversion event" button highlighted on conversion events page](https://static.semrush.com/blog/uploads/media/81/c1/81c1fa283ca674120127a8a6a10c1bcc/537eb42740463d720803a92cc0e9c9b0/S5OL0UmFporiPMRzQDnQKODX37j8j8n3b69hreaX41zg1QUm6A8bBI8ZCvkQcH8iNL69Zcp3i0zxMdgm3OPNsZjUfHTNNj--oocUTn0xvwNOes_-ZUuOW2pqH14PYjpDtfx6mF5CmXosggCMRu7_jjY.jpeg)

Type the name of your new event in the “New event name \*” field and click “**Save**.”

!["generate_lead" name entered under “New event name *” field and "Save" button highlighted](https://static.semrush.com/blog/uploads/media/3e/2b/3e2bbd4880fd314556331fe3cc5e3143/b7c3c1c543f00a02d720ef5ef24fc477/VViPcjq7p-r3zZZxd3g2FqYh_W08Caq8E9vpFI-Ur-8z0MN_ZkMwf_mvFdgUVN1MARcr_s1ooKrZdPBC0jfj33d5lrXJxOiuL1xuNLb7UpcGcZ1eZXTTP0sHhtTl47dHfI8z0QnlPn6NM72PzlpwBQI.jpeg)

Your new conversion event will appear in a list.

!["generate_lead" conversion event shown on the conversion events page](https://static.semrush.com/blog/uploads/media/2b/26/2b26c0444ec3c91d9fff33a13cb78328/e039a41bffb5587b2ea9447e06e3c369/quh6nMc3kl7MTW_67WitHkpx_ZVSbMIab1S3g9LENM9aOalT4PBtPDnNnlQPmtbJ-htKGSXepdJa51s7yanP7jQdaC7gKUYyypcpe3zAf9ygfJRJTcvpXMNXcam37ItjtCT4BgnHeF_mY-non_XbG84.jpeg)

Next, let’s review where to find your conversion data.

### View Your Conversion Reports in GA4

Google Analytics has a built-in report where you can see all your conversions (key events).

To get there, click “**Reports**” from the left-hand navigation bar. Select “**Engagement**” followed by “**Conversions**.”

![Navigating to “Reports” > "Engagement" > "Conversions" in the Google Analytics menu](https://static.semrush.com/blog/uploads/media/f6/91/f69138354357131f9de46474244aa96a/8b7dd20eb65a7fd9c0f83c59d0623af4/pdwwWyEbr636-imU1dJzrNjy0JdOtPCenw1VCbSeWj4Ft9FveeZUownDtS7bsnkfhbkxiabogfDEQjHJhCxQfvfVx_LrSd79FI9EO-S4EwIpK15UBXsK1-bg7cizE2XjxYpa9PYW_9vr1-Pv52O2EtU.jpeg)

You’ll see a report listing any conversion events you’ve created so far. And a chart showing how often they occur over time.

To get more information, add a secondary dimension by clicking the “**+**” sign next to the event name.

![a report listing conversion events and a chart showing how often they occur over time](https://static.semrush.com/blog/uploads/media/8b/03/8b0312b3bdce917fed68306a8345c63c/21a8f473a92f713a381fff1a1a2dfe1d/YMeMY7e4Hvh2kP2paO99hyNo7-7w11tHs0VajLDtpdr-ZbylrX2H3F2YQRw4QBsHjD1-exp6HlHYCWIxZ3RZA6pim71vTqgRTqsXt2RAi2ypwCGsVFfYfomvo9ShNWp1FGZXvy_1WhuTUU-_CpsG-vo.jpeg)

A dialog box will appear showing various dimensions for more granular analysis.

Click “**Traffic source**” to analyze where your conversions came from.

![“Traffic source” selected from the list](https://static.semrush.com/blog/uploads/media/fb/02/fb025ae68d26dc8b6925ecf294c4b013/fe2cc79b8fa3470c8857839fd93085b9/8MZ_QWE_-CGJhsBVx4Yh4W2DjeO9rzBadfAzaLdZR2tKcpMSGC7PJE6zItgFALe5rBX1Xz7WTntGcLKVTp_M0M7-KbCdYvhcHUEAksf4AqcN3h43C9iID_LuZf5HOkaisWrgkgLBy84XgUW14tSdOPA.jpeg)

Then, select “**Cross-channel**” followed by “**Session source / medium**.”

![“Traffic source” > “Cross-channel” > “Session source / medium"](https://static.semrush.com/blog/uploads/media/b1/93/b1934c9f534b4b259d7ef3ceaaf0021e/af4b24445b5cece374898a7450f15d0d/Mo6mT7BXmqoZlu0HG5-HrSo-o_9NEgDGBJHLACeSD7BM6zlCkKj2BRs8xJdTMc5zEryAkZJLTfRtDruhw4Gi84u5XGdYutrjw3gGLNE2vP-UQTG0_JIIelsB-hI-ic3tqGM9_9spuWrM-YsGPXHxnck.jpeg)

This is a way to identify your most important Google Analytics traffic sources—what’s working well. It also helps you uncover traffic sources where you might have opportunities to try new tactics.

![Google Analytics traffic sources highlighted in the report](https://static.semrush.com/blog/uploads/media/ef/f7/eff7387dd131f8249ff634276a69a557/df09a05274eb5e2cee48016af72c3bd1/gWKSCQGvtawps2HnXF3OE1PH7NeyFyNnqfgk87vp0ELYfq2uO9FUVZ43aqJsyqRazJAsI8V-PD-kd3FiZDTnu1KaaBbHJf6qUyIkqiRF_Y6bVZAm6iAoO-0ywYzOvXxDc9huVVtCmIm3u1BpQO3oigw.jpeg)

For example, the traffic data shows only a single conversion from Facebook. This might signal that it’s time to look deeper at your social media content strategy.

## Evaluating Additional Conversion-Related Information

Here are a few ways to get even more insights about your conversions:

### Conversion Rates

Your conversion rate tells you how efficiently users are converting. To help you understand whether there’s room for improvement.

There are two conversion rates in GA4:

- **Session conversion (key event) rate**: The number of sessions (visits) resulting in a conversion divided by the total number of sessions. And multiplied by 100 to get a percentage.
- **User conversion (key event) rate**: The number of users (unique visitors) with a conversion divided by the total number of users. Also multiplied by 100.

Going back to our dental practice scenario, let’s say your website receives 10,000 visits in one month and generates 105 conversions. Your session conversion rate is 1.05%.

But many of your visitors come to the site more than once over that period. The total number of users is 5,000. And so your user key event rate is 2.10%.

You might choose to analyze one or the other depending on what question you’re trying to answer. And the insights you’re looking to glean. For instance:

- How likely is a single visit to result in a conversion? Look into session conversion rate.
- What are the chances that a visitor will ultimately convert? User conversion rate can help here.

Let’s say you want to forecast conversions based on a traffic goal.

For example, your leadership team wants to increase website traffic by 20,000 visits in the year ahead. You can anticipate that this will have a business impact of 210 new appointment requests (20,000 x .0105 = 210).

Here’s how you can get conversion rate data in your GA4 reports.

First, click “**Traffic acquisition**” from the “Acquisition” drop-down of your GA4 reports section.

![Navigating to “Traffic acquisition” in Google Analytics menu](https://static.semrush.com/blog/uploads/media/c5/d1/c5d12a16695d6acf475a8b264aaefb79/a6426caf2f2d388b17dc01d8d8fd44d9/SHyO3RlmHP7vIvuQwju_icWDrv6tgUo7vlbweQ6p7sxfGP6Rn4E1p240Q_YHpVEW-pFtgcyr4HNyM-XfUDuewoTCxpkpWL3EDUuth4GvU8CX_Um60dg3JQn2GC9DC40_hqLzgf_onYoeE2CY-25ojKo.jpeg)

You’ll see two graphs at the top and a detailed data table below. Your conversion (key event) counts are visible in the second column from the right, alongside other important metrics like “Users” and “Sessions.”

Click the pencil icon in the top right to customize your report.

![Traffic acquisition report in GA4, with the pencil icon highlighted in the top right corner](https://static.semrush.com/blog/uploads/media/d7/94/d794bbe5f6226301299568d20350dee9/44e2f665ce0dbd495ea31a51a73c7263/UHoLeEpBf5Q3mLobJWdnIzifpmvn4lpOxe8hWmY3JdKvElmHHs-WjvvX7t6g3sBsW-fj32c3z5yW7dfT0N5XeboPZYT0s2PlBTBXKWA3g73po31TwcPYQuXivK6KyAUGszwO1Kttdw0Jgs27EuD7UrE.jpeg)

You’ll see a “Customize report” window to the right. Click “**Metrics**.”

!["Metrics" selected from the “Customize report” window on the right-hand side](https://static.semrush.com/blog/uploads/media/17/d2/17d26c898adb0438dcbaa56e25c3da8b/206cf5c15c9716a8f353b924567447b3/OxneLqnrPLo-jlOg8Mw0VeQWftUp6Z0F3fEbI-Lsyok8sE0RsoHUCFNSXj8eXrN1cQoOCSKmZRCLbwCqIHo0tSG712OrjnyH8h3OBNEmhgstWP4LNVLor-jMoYRKcRPWV3PyWLEpmAVFfMxuaKpyOcA.jpeg)

Now, click the “**Add metric**” field at the bottom of your metrics list. You can also delete any irrelevant metrics from your table by clicking “**x**.”

![“Add metric” field highlighted at the bottom of metrics list](https://static.semrush.com/blog/uploads/media/7c/6c/7c6cd47fb02b7b0e7bff2490e2a3a5b4/a13cc61c4453767195f7b53e05715ee5/ddYkD4ybY7Y9mXPAxsqKcsHiQxRcfYwRJ2IXyiuwCWl9sOdAJG7HY2xSxGWeOGkPCC86BVV2UCMf5wJOh8PaJytkZWFYQHOXbRBbb5IA1M8csUVvgqtsMytylQ8aYnXCqEqKCJI7NxbYic8XtBwSvBw.jpeg)

Begin typing “conversion” and select “**Session conversion rate**” when it appears. Your list of metrics will change to include your new addition. Click “**Apply**” to update your reporting view.

![“Session conversion rate” option selected from the metrics list](https://static.semrush.com/blog/uploads/media/3c/ec/3cec975540f63f2b3435f87aa6a764e8/49eda4c8350b1d51e41ee3f7c29001f6/OV2BwawzG2n-Fpg0QJAtcV2sdJF_j_Ibi9pAkT5Q9Txhg0E4pMeIuyyefzhGjf-A21eWDAP7qSNerem2-mQIFazQ0J9zxfPvtVWXg7kd6yDbkhafbZVEYPW0232kLywDK4XOdmMP-RFiJvxE-X-RRh0.jpeg)

You’ll now see a new column at the far right of your table: “Session conversion rate.” By default, this will show the conversion rate for all your conversion events.

Click the down arrow to the right of “All events” to choose which specific conversion event you want to analyze.

![“Session conversion rate" column, showing the conversion rate of conversion events](https://static.semrush.com/blog/uploads/media/ff/02/ff026a59610af82b87c172de34bea325/3bc5f810cd3840b94301b3a477653c35/fRb9ZLlASLvXkrNR6DHP1khQjJ0OvhgpkF8MaFgL75xPhJvzUeBzJrWls2gPCotin9_hPOUENMBC1jl20K6quzWEoAB4etSIKVngRYPjCD7giNB6nDqM_aNWZgop9M_YUj7C1yr1mr-ClU_1AY3eTSw.jpeg)

Choose your desired conversion from the dialog box and your report data will refresh.

In this case, we only have the single “generate\_lead” conversion (remember that “purchase” is a GA4 conversion by default). Click on it.

![“generate_lead” conversion selected from the dialog box](https://static.semrush.com/blog/uploads/media/01/a2/01a21724c0cd5806aedec90b23faadd5/42551a6839ebbe9bbb1b320e64bb9afa/EZhnThQLXGGRZWkGOx3GJ2OAPY8EWVSFTqw8mo3lvQjE2Zq2Tjl_ELDP1d7rJkXt3NgoYIGkh6CvPO8WOj3TOBGoytmOMIkNT0DQxkVkru4wj8UE7zsgRHmmDhsGtRPddUtqpvxkQShiarC1sXGAJGY.jpeg)

The column header will update automatically so you can see what you’re analyzing.

![“Session conversion rate generate_lead" column highlighted in the table](https://static.semrush.com/blog/uploads/media/b9/39/b9392da1646659788e01d97be4e129f6/f889a6ab324102e7e23f139c93a87e55/2d0sswlWchdvHppN6bZ3tyDq7Oc-dHTqA5cb8c-ecSinnelSz-hlxSdI5KfBryCnhyYzf-MuqYRkyG6_zW3WvCfsgZTiMyWbcq7ZWR_Z_fxN73Oi4B8RjLCiCvdSdX2QlUy_HVKP1qDonbSxbSzq2mI.jpeg)

To make your changes to the report permanent, click “**Save**” as shown below. Then, select “**Save changes to current report**.”

![“Save changes to current report" option selected from the drop-down menu](https://static.semrush.com/blog/uploads/media/31/96/31966870ccd6537ea2f3c179cae62cd6/69ddc46e8b8846e800e0938176bc7368/HKO2Wyz_ASXzmO9ROarx9zuWva1hWqonFI5T8AGVib4K4d_SjVF7ps3H3brabLVwAFQ5v-fsot0SkRTfPItpISQwblx8ilRKt3uxn7PdCqnmkAIEw29-EiP8qswa1fS1XPpxNFiCNu3HjxPG5fMdHy0.jpeg)

Click “**Save**” one last time.

![Save changes to current report pop-up window](https://static.semrush.com/blog/uploads/media/b5/fb/b5fba6b83fa21b7dd71c5de73a9337f4/22e85f170402635b0b0d191c41abdf4d/9SsGztIMbjhV9xM8cqtql3e76u5Rr_vr79Knpd9AIfzulU0Jo4gdbP6vUFy1VWLfthgihaG_D7IKFXw6QcewjgiWt7y9D1qDlBT5qVMiQmitjs8ngm79z7ECg9KTAfVGp9yTH6SlsCMjL-hPp97V8tU.jpeg)

As you continue to create new GA4 events and mark them as event conversions, you’ll be able to use your conversion rate data to analyze individual conversions.

### Attribution

Attribution is the process of assigning “credit” for conversions (key events) to various Google Analytics traffic sources.

Let’s say you had a visitor who purchased from your ecommerce site after three visits.

1. The first visit came through organic search
2. The second visit came from email marketing
3. The third visit was via organic social media

Google Analytics can give all the credit to social media for driving the last visit—called last-click attribution. Or use data-driven attribution, which gives GA4 the flexibility to acknowledge multiple channels.

The data-driven attribution model is the default and what Google recommends. [Google says](https://support.google.com/analytics/answer/10596866) this model is advertiser-specific and uses data unique to each website and advertiser to credit conversions properly.

You can compare the attribution models using GA4’s model comparison report.

Start by clicking “**Advertising**” from the left-hand navigation menu. Then, click “**Model comparison**” to see the two attribution models side by side.

![Model comparison report in GA4, with data for organic search and email highlighted](https://static.semrush.com/blog/uploads/media/d0/06/d006f313758f2cca492e4a04f16040dc/6ee7b1268d178b796d3d0fb4a0bcdbfe/P5-Te3In5M3XqAXYPhH966MpnMjpoFYCU5DyKND9139OTxgCpbtRlFk0l9sxPE2vqep99YPpFt0oYRVxe27ulU5Sw6_ud_tsfLLd9rjOBCBSNGPsvLnZXUjA_Ei3LstJuoTfZ3azZPXR5dmJe00KHmE.jpeg)

For this particular ecommerce business, you can see that the data-driven model assigns more credit to email and less to organic social than the last-click model.

### Conversion Paths

Conversion paths help you understand all the traffic sources factored into your conversions.

Let’s go back to our dental practice example and click the “**Conversion paths**” report. By default, this report will show data for all conversion events combined.

![Conversion paths report in GA4](https://static.semrush.com/blog/uploads/media/dc/f5/dcf5de75e53cd5f4cac74ee78de6e3a0/3788f5b6bc9387e71e928e16762d1404/HxlhVNERddKXxUh5xyPWxeQ4rLXg16Ptkn6GMh3GRtUdFEB2lPdEqU5dvsxadHLZAead107p_LHJ5QaBYxeNQ552D_3xu8RdGQMfB7pCeQ8SWsqt_hjyGVohQI6BoZuI3_en3HsonyzCFQaQOVbIJDk.jpeg)

If you want to limit your conversion path analysis to a single conversion (key event), click the “**conversion events**” drop-down at the top of the page. Use the toggles to choose a conversion and click “**Apply**.”

!["generate_lead" event selected from the “conversion events” drop-down menu](https://static.semrush.com/blog/uploads/media/15/e4/15e4b4ac93519ca38118c42dc3818394/a031318fb01fd8265eee0eb89923e26d/Ce9ynnb5TMqaXrwIyiwlmpvob-brUtvk65FusgJ0-J2L9Vl02DEZR-5AOA9T0os-j-qzy9rV3QYRnec5BI-feUxuChwPJsqUBS6fBwJS3EhO_TozHhana0HrmDqUuacQupC_N4ggY959Ln8XimHxL5A.jpeg)

You’ll see which paths are most common for that specific conversion. In this case, the most common conversion path is two separate visits via organic search.

To change how you group traffic sources, click the “Default channel group” drop-down arrow.

![the report shows the most common conversion path is two separate visits via organic search](https://static.semrush.com/blog/uploads/media/61/fe/61fe8181706a903b0a912cb3d434630f/b44dc3659aeb7452e172c870a128e8b1/v8kzB2NYfNmgjgh1rmtl7TBZ_htRlAsV_-aPSE9Zz5DkWKsiq5jbjhGWsn8fAX9EyflcM9cAATwLCLp7-myne0uuqbINCgKY5Zic0Zzcq5CRAHK9PdjJ69Ky4lC5gm7mlYDpanVz1ZW6togT-k-BbIA.jpeg)

You’ll see a dialog box with different traffic source options. Here’s what they mean:

- Source: The specific source sending the traffic (like Google, Bing, or DuckDuckGo)
- Medium: The type of traffic (like organic or [cost per click](https://www.semrush.com/blog/cost-per-click/))
- Campaign: Traffic coming from a specific marketing campaign
- Session channel group: Rule-based definitions of traffic groups (for example, the organic search channel)

Select “**Medium**” to group your conversion traffic based on the type of traffic that drove the visit.

![“Medium” option selected from the dialog box](https://static.semrush.com/blog/uploads/media/21/8f/218fcb53819c57606ef26b43c2c1679b/7ddef920309125b4ed426eecec66fbd5/SQMnuoMFmF_sJJJc0rURhUKtq0eKj2DfhDzq2OT1gOKmLdOXIJZo0x7ZHAhiIrjG2dSNptDE6wjLwlcE2CM-jJangOiT4RwpYwvjzluhAuy6OiLiaP_tzbc-aPTbv6DM1Z3cyVUdpE391i-_cBqAS1M.jpeg)

***Further reading****:* [*Google Analytics Traffic Sources: An In-Depth Guide*](https://www.semrush.com/blog/traffic-sources-ga4/)

## Limitations of GA4 Conversion Tracking

There are several limitations to GA4 conversions, which we outline below.

### Few Conversion Types

There isn’t a simple way to track session duration conversions or pages/screens per session conversions.

Since everything is an event in GA4, these types of conversions aren’t available as they are in some [Google Analytics alternatives](https://www.semrush.com/blog/google-analytics-alternatives/).

### Some Tracking Requires Google Tag Manager

You can’t track everything with only GA4. For some things, you need to use Google Tag Manager to assist with the setup process.

Examples include button click tracking, submitted forms that don’t redirect to a thank you page, and ecommerce tracking.

### Limited Attribution Options

You can only use last-click or data-driven attribution with GA4.

Other web analytics tools include additional options like these:

- First-click attribution gives 100% of the credit to the channel that brought the first visit, regardless of when the visitor converted
- Linear attribution splits the credit equally across any and all traffic sources involved in the visitor’s journey before conversion
- Time-decay attribution assigns most of the credit to the traffic source that brought the final visit, with decreasing credit assigned to preceding visits

In GA4, you don’t have the flexibility to view any other of these attribution models.

### No Assisted Conversions Report

There isn’t a dedicated assisted conversions report in GA4 that summarizes how many times each traffic channel participated in a conversion path.

Use the conversion paths report we outlined earlier to visualize the various traffic channels that contributed to your conversions.

## The Next Step After GA4 Conversion Analysis

When you have the conversion data to understand your website, you can see how to drive performance into the future.

Let’s say your dental practice aspires to get 50% more new patients in the next 12 months. And you recognize that driving more organic traffic is one of the most feasible ways to do that.

Our [keyword research](https://www.semrush.com/analytics/keywordmagic/) tool is a great way to start working on your traffic growth goals.

For example, you might search for “pain free dentistry” because patients have recently started asking about this.

Enter the keyword and click “**Search**” to see if they’ve been searching about it as well.

!["pain free dentistry" entered into the Keyword Magic Tool search bar](https://static.semrush.com/blog/uploads/media/ba/10/ba10ff073beea5d63cd9f8802de18741/8933712886dc8aed70ddae3a29cccee0/Q8wepo-ADCSnVS1KosD-g1z84G9aFDZpNZRoPHjrfJkN6NTl0d_ZDoeQPM2guxN3hoJ_soEw-cqdu3TPvX9ulK_LO-6Xyhl1Mm23X25JgGeP8OjB_Fm4G-Z9M5bEnkQUIlrgiptclBSUJyCi7ii7dHI.jpeg)

With a relatively high search volume (“Volume”) and low keyword difficulty (“KD %”), both “pain free dentistry” and “pain free dentistry near me” have great potential.

![“pain free dentistry” has 390 search volume and 29 keyword difficulty, while “pain free dentistry near me” has 170 search volume and 1 keyword difficulty](https://static.semrush.com/blog/uploads/media/79/4e/794ebbc004085abdc98200870a2a71ef/bc5d1fdb6532f7a00a6de09d125ec4ed/68vRqJYBO_KWT3W_StNzT19yo2nk-93lr2VqBX4Vl5OXX-nvxk-QQkKBko1xcNItOj-3zamgZMjXfcUo_JunapLKVPw8lS1iuIc_iYbPj0xH4-wLYQmupeuOee8-mfTHf3RdTqcn9jMHY53qy4EmlfM.jpeg)

You’ve already spotted a great opportunity that you could target with a new service page or detailed blog post.

And you could include a link to your appointment request form within that content to help drive readers toward converting.
