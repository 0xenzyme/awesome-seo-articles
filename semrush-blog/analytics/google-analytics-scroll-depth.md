---
title: "How to Track Scroll Depth in Google Analytics 4"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-analytics-scroll-depth"
url: "https://www.semrush.com/blog/google-analytics-scroll-depth/"
canonical: "https://www.semrush.com/blog/google-analytics-scroll-depth/"
author: "Zack Duncan"
published: "2024-01-16T15:08:00+00:00"
updated: "2024-01-16T15:08:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2024_watch"
  - "time_sensitive_title"
schema_genre: "Analytics"
fetched_at: "2026-06-12T15:42:06+00:00"
status_code: 200
html_hash: "8c20c55a03c4e2e6fd13dbe05dca865be12ba1120172131fd4be3c1736336fc8"
clean_word_count: 4636
clean_char_count: 38206
---
# How to Track Scroll Depth in Google Analytics 4

## What Is Scroll Depth in Google Analytics 4?

Scroll depth in Google Analytics 4 is a measure of how far users scroll on your page before leaving.

Scroll depth is expressed as a percentage of up to 100%, where 100% represents a user who has scrolled all the way to the bottom of your page. Depending on your specific implementation, you may choose to track scroll depth at percentages like 10%, 25%, 50%, 75%, and 90%.

Here’s an example of a portion of the scroll tracking setup process within GA4.

![Scroll tracking setup process within GA4](https://static.semrush.com/blog/uploads/media/2c/ea/2ceafdc8bf1b303c2ea3f31a438e687b/7b7ca8fce4d5d9583cfb8b5f91d2336d/21KC5NtxZDw7xUloobWMulPwZHVq2r_f0mn9moqpxxbhaAReLOpGRCmOW3IHARjEN6w4su8_GQwVABNJIpKU5KIYm14lnMaVTCJ-BVWl-pCRMKBQl9otvwoygIbF390E_us04HT6i2tLH1neLpblFc0.png)

In this article, you’ll learn how to track scroll depth in Google Analytics. And how you can begin to use your scroll data to optimize your content.

### Why Is Scroll Depth Important?

Scroll depth provides actionable data about how your users are interacting with your content.

Let’s say you wanted to uncover which pages resonate most with your audience.

Without scroll tracking, you could review your [Google Analytics sessions](https://www.semrush.com/blog/sessions-in-google-analytics/) and [event data](https://www.semrush.com/blog/google-analytics-4-events/) to see your most popular pages.

But with scroll depth data, you can see how those pages hold your readers’ attention as they scroll through your content. That is data you can act upon to improve your website’s performance.

You have two options when it comes to generating scroll data in Google Analytics:

1. You can use the default that will trigger a scroll depth event when someone scrolls 90% of your page
2. Or you can create a custom event to measure scroll activity in more detail

Let’s review the default option first.

## How to Activate Scroll Depth Tracking in GA4

You can track Google Analytics 4 scroll depth automatically as long as you turn the proper enhanced measurement event on. When enabled, this will generate scroll event data every time a user makes it 90% of the way down the page.

Why 90%?

Webpages often have a footer that sits below the conclusion of an article that most readers will not fully scroll through. So you can generally consider a scroll depth of 90% to mean a user has read your full article.

Before getting started, you need to ensure that you have [set up Google Analytics](https://www.semrush.com/blog/how-to-set-up-google-analytics/) on your website.

From there, click on the gear icon in the bottom left of GA4 to go to the “**Admin**” section.

Then, click “**Data streams**” within the property settings (under “Data collection and modification”).

![“Data streams” selected from the GA4 "Admin" dashboard](https://static.semrush.com/blog/uploads/media/d7/db/d7dbfd477971853e51d9d1283fa0cf8e/81b812cfc80811037d10d0a55e1a9e2f/7kv3Nudf8LTNkjAN_JLvTsWw8jXZaROGnq_e8-mSo6EQKSNiSNjwb8bdVRj4R-G8LeuYREpfK19F7FlYl9Cp09Wdav7mDsgkfCY1Ij7VB968I4GicUNQNCKCxq2v41TyzGtNwFQNTIk3xhNCAcOqDf0.png)

Click into your website’s data stream.

!["North America & Cana" data stream selected](https://static.semrush.com/blog/uploads/media/be/a7/bea7d2750ca5220c86505a675090172e/6090be9b249a3046c6c429c55395e20b/6lD7VW--AFnhs_JwB01qJXXU8_NJVqO9FfV8vVaIr8aaDJ-8ejOZppQPS1GGWO6tldnlVeMJx_Mnaxz-G99RXHn9GIMSIIt2u32vlIwjxyRu4oi69gy8W-x8DpKTtbDN73fJEu-vkrCMvHedQd0pPTo.png)

Ensure the blue bar to enable “**Enhanced measurement**” is toggled on. (It should be on by default.)

![“Enhanced measurement” switch toggled on](https://static.semrush.com/blog/uploads/media/23/3a/233a99b0d311764b17121b466f98fbdb/cf255621d7d3c04129571cc0f724710c/QFGSDimGt-ljWo6_9lqE3xp65RxF3lT_q8AGBI9rqJuqESNLZN0UQvyramomMwgB4boEEiZqZg-EjQaiGHzXGcUT3VIFGfuXJl4GHPvp6t4BOcaPFCkWxrdCTIupaPKZI3PY3XOqRcjJicJT5JkoSx0.png)

Now, click the gear icon to access settings for individual enhanced measurement events.

![Gear icon highlighted next to "Measuring" bar](https://static.semrush.com/blog/uploads/media/13/42/1342731e3e42561e37e65ad699f85340/766bca97053eb106f123854aebf17ef1/44fXzr8BX7mkZvd177Mh_5KdiNekdkcK-G0CWV_5kt0LACRbVcR08Uv5JddluJl95qaEWr8XCgnTOSQaKE5TJs3QMJ7BMPYn_VslNd1KfHjM5TGC5nhwmoGyJrhK5iD4H-SX31N1-YUCTv9bbGtFkns.png)

You’ll see a list of enhanced measurement events you can turn on or off with a single click. Below, we can see “Scrolls” is not turned on. To activate it, simply click the toggle switch and then click “**Save**.”

![Activate “Scrolls” switch under "Enhanced measurement" section](https://static.semrush.com/blog/uploads/media/c5/71/c571d4556967d1dc1f5046679da3e2dc/5e6d8beb0f21ca115d26a6bdf42af290/7Y-HhJuQDbzvXlXj49Ep1h7uMDoW5EzrvMMg3hTI8-QDlOJ367uA63eFyeNWAGI2SxgKkhewizv_e7wxI0qsXI3mDcf6WS54RAzJsPVXlppGbD_ycAGGjyoJ2F3tYoUPMRzakmhavB-8xqdNQ2prULo.png)

With this, you’ll now be tracking scroll activity whenever your readers scroll 90% of the way to the bottom of a page.

But what do you do if you want to see scroll depth with more detail?

To do that, you’ll first want to turn off the toggle switch we just reviewed here. (This avoids potentially double tracking the same scroll events.) And you’ll need the help of Google Tag Manager.

## How to Set Up Scroll Depth in Google Analytics with Google Tag Manager

You can track scroll depth with greater specificity by combining Google Analytics with Google Tag Manager (GTM). If you don’t have this set up yet, check out our full [Google Tag Manager guide](https://www.semrush.com/blog/beginners-guide-to-google-tag-manager/).

You’ll be able to track scroll depth at any percentages you choose by using a **tag**, a **trigger**, and **variables** that will generate GA4 event data. In this guide, we’ll use 10%, 25%, 50%, 75%, and 90% to get the data we need.

Let’s first define these three important Google Tag Manager terms before you set them up.

### Tags, Triggers, and Variables in Google Tag Manager

Tags, triggers, and variables work together in GTM to create GA4 event data:

- A **tag** is what will create the scroll depth event data that will flow into Google Analytics
- A **trigger** tells the tag when to fire and create the scroll data
- A **variable** is a placeholder for a value that will change, such as the specific vertical scroll depth percentages that you want to track

Strategically combining tags, triggers, and variables is the essence of using Google Tag Manager to create [GA4 custom events](https://www.semrush.com/blog/custom-events-google-analytics-4/).

### How to Configure Your Scroll Depth Variables in GTM

To get started, head over to [tagmanager.google.com](https://tagmanager.google.com/), where you’ll begin by configuring the variables you need. Then, click on the “**Container Name**” that is associated with your website.

!["yoursite.com" selected under “Container Name” in Tag Manager](https://static.semrush.com/blog/uploads/media/f6/1d/f61d01decde69f50a63ce7233ae58408/593564f0fd70ed268be3128583a541cc/6ldbUkZHOhRmxZweqK1eB5xVoywXfEwuQr6DtyvpQ4mfpinEHKfVhUSOOE1VPRyVC7hQZAqzj727qtBiCXBB-Ab6U6cC1yz6o-gxOdupcgVkiMrgGwOcObunzGx1RneEuYe567AJg90jjqZh4xaKNqg.png)

You’ll see the “**Overview**” section of your Google Tag Manager container.

![“Overview” section of Google Tag Manager container](https://static.semrush.com/blog/uploads/media/24/e3/24e34b47b6478682b44d65f5d238e56b/34f216daf6e05ced461d3f1e8e19b392/0HPfMD_RPZhBPbZd57mbsfH_z-YZpTiIpoiGrq6Cdcg9naiEEl5U5PS2Shm5p3-QUclDG6kil05OG5W03vGWTn9vVMl8OIW-lVu4iciDLuXGZYaxzamcOdvYjFb_kUdMUmBfMcc2toioNcbGTb0WXi4.png)

Click “**Variables**” from the left-hand navigation.

![“Variables” selected from the left-hand navigation in GTM](https://static.semrush.com/blog/uploads/media/0c/02/0c0249366efcd5b46a5efde8cf6ff9e6/b460dc5c79fe496e162aa445e6e44de4/X7gJ5oVM_SJ413tIDeWASLVMNJU7FhX0l_8tlkJGsKYsvASvtVvUcbqHjYVn3M4usZP4ghncdPUoB6a3QxibcKumoBlO2gs5RY9nFbc6XlA2pROH84cI_-jZVO3mnoqTLZF0aqTwEgnPdw81FA-mtM4.png)

You’ll see the option to configure “Built-In Variables” that you can use in your tags and triggers. Click “**Configure**.” A list of variables will appear on the right-hand side of the screen.

!["Configure" button highlighted next to “Built-In Variables” section](https://static.semrush.com/blog/uploads/media/92/d8/92d88e359f7c1f5fe627c8a485a87f01/24493738a8c665a6be86cd7a915f9fa5/IcoD--IZn9xKRcw7bUUH-6s86jh6dyCkpo_MdMob8T9Pmtsl1kV_yboclSa-XvJ_KSsdhwENDjssKRdL3X1uXCZUHF_muHZSP6CfujXu-D2iPubOyCd6bYt_idt1ehtWLgkrrCCgoBqnEaNpQrrREnk.png)

Scroll down toward the bottom of the list to see three variables specific to scroll depth tracking, under the “Scrolling” header. Use the checkboxes to turn them on.

Like this:

!["Scroll Depth Threshold," "Scroll Depth Units," and "Scroll Direction" turned on under “Scrolling” section](https://static.semrush.com/blog/uploads/media/a8/fa/a8fae5398b8fb9da922be9d07530764b/13323d3c6858bd43bbe7091a5f9feb4e/A4YFHSa3f56D9I1eMtZFnUfCw4xvXoe77ynDgD1660JX1vFjKvuJWSizvc_z3_IKobpB6FyZHCVnNQm8AzmQQ0WgvQmDwLrEbM9gM7avHtA2z18hFFC41-N5bKuFzZW3YyNZgb03IA6fGzdxQuzy6DM.png)

You’ve now configured your scroll depth variables. You can close this list.

Let’s now create a scroll depth trigger that will specify which scroll depth thresholds to track.

### How to Create a Scroll Depth Trigger

Click “**Triggers**” from the left-hand navigation.

![“Triggers” selected from the left-hand navigation in GTM](https://static.semrush.com/blog/uploads/media/e8/0c/e80c6c33729342b390693443b909d362/6202a56c8d57d499006c5f3bf3fb14f5/j-BmAhsuXr7ljWZogx1ut77CMpE5GXY6vqxSp0ytUtUHihGnI5c0U_3fuefu-9UyEA06Dc8BNxQXoc7WLL3eFmGm7IXnjLdey_HUzg863qfeVmMytXyyPab7tPtsLnWCgQn_yX6D1prUg9TeiG3_TYU.png)

Now, click “**New**” to create a new trigger.

!["New" button highlighted under "Triggers" section in GTM](https://static.semrush.com/blog/uploads/media/f4/d7/f4d7bfb884585e406104d12291b84eb0/e18b24e87a7b09a09ff83469ab89f45a/TELQ8_cn9H5T3t58Vs-Ua0_tVrzUcGUD_ezZ18m6lhF7jkdkkKhSJvc3t-WElGGvgFRmsf_t52KYtmU4J1nT3QBZDbIfUVcZQEo3ZUVC9NnJsSFCW0c5y_SbbBvWWR9Q4uEA0GOJmUYrlpy6FX0muTc.png)

You’ll see an untitled trigger and a space where you can begin setting up your new trigger. Start by giving your trigger a recognizable name.

You can use something like “Scroll Depth Trigger.” Then, click the “**Trigger Configuration**” area to choose your trigger type.

![“Trigger Configuration” area in GTM](https://static.semrush.com/blog/uploads/media/00/cf/00cf4f716bd41f3e9f00e01257396b86/b0e60f6ff986b731dd596a434fd1eb03/aY_bEUm7DD628RvZ9zORU4suY8ul1T-6jXO2TvyOSXZrAAV26zZOksdYQHkihatmcFRBBbEM-yA0DwlkQikiLWCgPuz3eirOLa0c7PS2g7sGs0Ccx4UO6ooBAs4CWRIVPUIcuxO_EcxErK5T37XNmYo.png)

You’ll see a variety of trigger types to choose from. Select “**Scroll Depth**” from the list, under “User Engagement.”

![“Scroll Depth” option selected under “User Engagement” area](https://static.semrush.com/blog/uploads/media/ee/0d/ee0d3dd6c5c2d6aa44b300dfa6ccf11a/c25037e503a22fa2140a298bd456989d/k8uI93AXOCXKm58xXGkwzLbfP7m21Kg6DWtl5mI38-sLQDbq9bB3DsGJnxwXZIPuZQYxYO9ZOH89hzXIFbN49gFQamIWBxDQNlHlGFnOv3fh1C67ojQDWdTWi03_g4I6X4XjN8gXLCc5_o1xMtYcXyI.png)

You can now configure your scroll depth trigger with the specific thresholds you want to track. You probably want to track vertical scroll activity, so check the box next to “**Vertical Scroll Depths**.”

![An arrow pointing to “Vertical Scroll Depths" checkbox under "Trigger Configuration" window](https://static.semrush.com/blog/uploads/media/a7/50/a750dab72a30bd5ebfb2641ecd6503cc/c7193f8828c094d3abd1eaa645543537/erPC_aVTi-pkk6wXimqtDB43cG9rKHo-qaaLg4Xj4VpKz5SE5y6-ajAJMRScGfJ7JgPJ6XYFwX0mTMxoTWwRJBncYSyZCaO3fnMWBkckcWzfxWDwvxNEo1SR-ykpmYsF96aXbbQpBgINqTFtmrukUq0.png)

You can now enter the specific percentage or percentages to track. To track scroll depth at 10%, 25%, 50%, 75%, and 90% type 10, 25, 50, 75, 90 like below. Then click “**Save**.”

![Enter percentages under "Vertical Scroll Depth" box](https://static.semrush.com/blog/uploads/media/c0/f6/c0f6a6969f0f1e5652b28c600fd77acc/9823ac0b93b7a0575f2730113167e6f6/tmmOyw-07zGPoIn04ayeugdsz4Q3eXxP4x1Vs1ev9Isf8cxV52ZouakTM80m1x2M5fIQgOun0Ju10iNWmu4K2lU_vz9V0rcfPnyvOhLYgRAri1UzriK9pQvGQwe5DqYaTaTfmwEoQplqRwNpEll1DxI.png)

Your new trigger will help create scroll data once you pair it with a corresponding tag and you publish all your changes.

Let’s now create the tag that you’ll pair with your trigger.

### How to Create Your Scroll Depth Tag

Click on “**Tags**” from the left-hand navigation.

![“Tags” selected from the left-hand navigation in GTM](https://static.semrush.com/blog/uploads/media/27/6e/276e087f0b09f3db782b5bf6c5cd1546/04474c91161ed45b8a1fe2873c4d624b/6ho5JrTZflfbpuGadDePZDtGcD3zHbTJUIUMeR6nGvwmsT5QFrbn9UzkSj4K2dQPaXrnzUKTbJYZYbq3xetBe85we9hehNb5EXk3i4TmPhHNpP0tXwe-nP2IvzRkfC97sPWIOgQNVMSMzuPjkneRJV4.png)

You’ll see a list of any tags that already exist in your container. The image below shows a container that has a single tag that was used to set up Google Analytics 4.

Click “**New**” to create another tag.

!["New" button highlighted under "Tags" section in GTM](https://static.semrush.com/blog/uploads/media/68/0b/680b3cf525f69c9e5ad32994b0730e02/a496f9c004474aaf09cec1d3c16d3efd/pU0Ej121mi9v1ap23_99jfRMXVrD4--Oko6GDk53Mf2gps6-IjgHOvTW3596xG6AIafhhmawMOLGQIl7LT3M0Y7F1aTjxSFwkW0op0l496PjOq3FKik1_t-Z6g7csOAUcsRk4cwxw4ZuDRN51G3S5EE.png)

Give your tag a name as shown below. Then, click anywhere in the “**Tag Configuration**” area.

![“Tag Configuration” area in GTM](https://static.semrush.com/blog/uploads/media/7c/c5/7cc54c6aae5ff6862464555fcacb760b/3b431c09ac6624309d745cd92cf47f0d/KcjtDEC3DkdYt7rNamzc5flyq8_M-xIcLp73ZBumb6mEqWuhfB9R1QxVM4fbSaLWmQLSc68kqlB2ve3gYvKJaMc-2pdxtITMuVmxJoeJozu5ojM6eTiy0WG5-MlIdqKR4djCKVlkaz7Ow6oD_M_IQRM.png)

You’ll see a list with multiple tag types to choose from. Select “**Google Analytics**” from the top of the list to see a list of Google Analytics options.

![“Google Analytics” option selected under "Choose tag type" window](https://static.semrush.com/blog/uploads/media/01/0e/010e138efceab39eca62e38ecfdea5b6/9061a9a73871b3e2066a4457a7e23f17/rqS51Wmk6vmPXqMGqI64jIYQkoU-1IyaGMi_Uo2babkhswRLEIfNYEWlUbhioLpQ-PykN8sgq5jYKP30ktGltH9goEtJf3D6fbpBOe6nEJ6okNF8jDi1fkCntz0B2i5vAFejsmTcrP5J23u6M2qJ_Mg.png)

Choose “**Google Analytics: GA4 Event**” from the list.

![“Google Analytics: GA4 Event” selected from the list under "Google Analytics"](https://static.semrush.com/blog/uploads/media/75/08/7508dcf06b296c854e2a2458c5eabfb8/12da3d2cd4b78935237c1b806540e5d3/tm2b3EAFYtZ-PXzePynlzmQaBglcWOp-k5v68I9P3J6HVG_bX1_uQbnQrBF4brvh1-_uccInqOnqc1m1RHsYHIOv0P9PVgaiHV6hnmRSlnQ0OfTqIsrnL-RSi8eXVVavo8RwdxKwXwF4216aUpB6auA.png)

You’ll now set up your tag configuration. Your tag already has a name but it needs a Measurement ID and an Event Name.

!["Tag Configuration" window, with "Measurement ID," and "Event Name" fields highlighted](https://static.semrush.com/blog/uploads/media/02/1d/021d7454d4040c094ba28186ae99b088/b6bc9d16b106e5bf83146c9bb42ca498/Z52pYZ4Y3HL6vyDGQyqCDz5cgNxdINNFAJTpdwKUhRa1eVzxfmTu5SqsSSkUS3_KQsLuRuJe2eJmDOovbifnZ6dK1ugZFOP2H5gSHEzMfuWaDdOOZldOPX2yLaKqtNcZ-kYsJmmBnUdraDsBr1K6Jvk.png)

The Measurement ID is also known as your [Google Analytics tracking ID](https://www.semrush.com/blog/google-analytics-tracking-id/). You can find it in the Admin section of your Google Analytics property for that website.

So let’s temporarily head to [Google Analytics](https://analytics.google.com/) and click the gear icon in the bottom left to access the Admin section.

Then, click “**Data streams**.”

![“Data streams” selected from the GA4 "Admin" dashboard](https://static.semrush.com/blog/uploads/media/6e/7d/6e7df4e9cc23de48369311b3fdab507f/41af67bc35277a28dd16715500f8f6e6/Zy3O5GOuoIX4bCK3VxbJJKdV3qxZPsi-LxYM6WrqrEVAkjv_PBpnaZVNSJ-OJMSQjaYpqsQ25pSt9IhP9ZXB4LGUd6gCHMwmumixZJPluiB5eY4ggWDLcodJuCbI4NmRbyRnsQlUmcZ55br4MrlvzDE.png)

Choose the relevant data stream from the list.

If you have multiple streams because you’re tracking both website and app traffic, make sure you click on the web data stream.

![Web data stream selected under "Data streams" section](https://static.semrush.com/blog/uploads/media/4e/bc/4ebc6bf1d694e93625e63e2b059a3487/3d997e7ab0141e93ce74da1114a776f9/9RUcHj5B1dqdTlh5c1WP1vv5HBFtb_h2-2IuPq-LozJ5H6abN1xTfWSidY0FnOfzoprx8kr_nFqgP8WfKOo6vKA83liTvoV-5t1_LBilgSkVZ-llM3M4prKSYBuRGWkCEqeHCK8ZGdRZ6OWO92XvIZk.png)

Now, copy the **Measurement ID**.

![Measurement ID highlighted under "Web stream details" window](https://static.semrush.com/blog/uploads/media/e9/ba/e9ba2b351c84e376584fc87ee904bc5b/1848fc67a9134042bf1632fa88c84c19/iEYkebnnaoxSQfE9_42BZ_UMkKEuK4MlIgnsj_-yT2_-iuVAwI2LPFbjLr5WIzr42d8WWQlQlhQJaSVXhXcbqTb_jn8LwXQaNC-BKaF5Ypu7AnE8GVbDVtlaZVrw5d8ff7yPvwUwxHkPoqU_MSORzrg.png)

Now, head back to GTM. Paste in your Measurement ID as shown below. If you have used your Google Tag Manager container code to install GA4 on your site, you’ll see a green check mark and a message saying “Google tag found in this container.”

!["Google tag found in this container" message highlighted under "Tag Configuration" window](https://static.semrush.com/blog/uploads/media/c2/bf/c2bf46b35ed15ae240aa2cacc3d1720b/0a9082bd7570c377819e601c3de28d5d/60w0rM45cl_bRW7Y2ZVtcDoWOUEfEqUezPTp4nwwgS5SRWyUuWs5pbmIggcbHxaf9FoArZyQIzFHggAO4SoDQTfWIEuXcPBmbY6GdIPbdnbEphP1FiKB1BKoFqxS-dN5ji1JSC7DWecB_p2uh3dGocY.png)

Let’s now create the “Event Name.” The “Event Name” is what will show up in your Google Analytics reports when the tag fires. We will create multiple events that will fire at each of the vertical thresholds you set in your trigger. And we’ll use a variable to help.

Begin by typing “scroll\_to\_{{” in the Event Name field. The curly brackets tell GTM you’re going to insert a variable.

Select “**{{Scroll Depth Threshold}}**” when it’s visible on screen. (If it disappears or you don’t see it, just start typing “Scroll” after the curly brackets.)

![“{{Scroll Depth Threshold}}” options selected under "Event Name" box](https://static.semrush.com/blog/uploads/media/98/ee/98ee3f4a19a6198aad870c56ca013e46/df689bc8dbdd34606bde4d7f1fc76991/xsHE4bLZ2ryQRFJ6O1XiTlY_JkB8cBH5EuTzZFHFfWDSYNI81Sv_fRe6sRpoJeWdkXmzwlSneBpjnqhxsOlv03GJKN7GDLPX5x4uljG96-V9lapT9wr7uLgWExsD9C6SvWfYSx3eMxrG9nnWh9gWcBs.png)

If you’ve configured your trigger as outlined here, you’ll be creating the following new events using this single tag:

- scroll\_to\_10
- scroll\_to\_25
- scroll\_to\_50
- scroll\_to\_75
- scroll\_to\_90

Now, click in the “**Triggering**” area below your tag.

![“Triggering” area highlighted below "Tag Configuration" window](https://static.semrush.com/blog/uploads/media/a7/d4/a7d4d33bacf5b0567a4143693086ad7b/0418e2cf20e7c39793211ab1a4eef33c/Tq1Pe8c1z_QAy-mb2QQXLemvVzU6IVFMHPjPEOW4hAGEBbQLZv-a60WQuA7LPjnej4ETSStauHG5xACw7F-GsqP_rRMp_8kLmh5C8l6dni7JM_Q71QaGdOeFupToMERxNgTTpJizSoSvfA8UomkTU98.png)

You’ll see a list of all available triggers, including the scroll depth trigger you’ve already created. Choose it from the list.

!["Scroll Depth Trigger" selected under "Choose a trigger" window](https://static.semrush.com/blog/uploads/media/9b/88/9b88fdd82dcdf4e64bce20b7f7091034/c3b77563acb3eaa32d78caec9761c891/K1iZrUVb6xPhAudDkYxmaOYWNxAIsGxQEu0JGt2EFL-4qTfVa-HUVTGCSGVEXj-7VpMIFEnN_wypmutTu2KhutlwalKk0m2zP-udR-O7_rdsdEGUiohV2DOO--JxmDNErUI8rIA1CRIBPM465YF2As4.png)

You’ve now paired your GA4 event tag with your scroll depth trigger. Click “**Save**.”

![Save your GA4 event tag paired with scroll depth trigger](https://static.semrush.com/blog/uploads/media/b9/ab/b9abeec5b4e297cf909c4b7b9a0f5a28/3e5e48b04bc29ae62935a44d03c57515/18me97elS4kdWaY8PV9Fb60cwM6mdp8Ji9S6SwJ0UIKdJpCteunC8dSIDIdtMyANFVakx68JJcrS1K7p0HEQTeU9ATvWExRAJ_ZWNc_v2_d15Ay0AbD20lZQaFACTehJTlp7X6p2DF9ohAaeXQ96tLM.png)

All that remains is to publish the changes to your Google Tag Manager container.

To do that, click “**Submit**” in the top right of your screen.

![“Submit” button highlighted in the top right of screen in GTM](https://static.semrush.com/blog/uploads/media/b1/89/b189dfbeccdb19aaae765700743ac280/c90a135ec521be18eca6229dd5b12cb5/i7Gp11SWtYzh_JrXx_QLVDeSctNGCpXDePRgNG3dtVXuqUSF7c1dz5__tjnT7xwMBhqlENP6NCvLmsCDzz3K7gmbSp54MMHogYziPb7aZfOsuEJ-d90HtFMvAPL0JWv5IJzqf8louyaKsaxTY2JAp_I.png)

Then, click “**Publish**” to make everything live.

![Submit changes in GTM](https://static.semrush.com/blog/uploads/media/98/a4/98a44523e027885d39992dab40c902b6/9029223c9e14609201bdd6642ed5669e/qfMuUr7GuJFob1wKBR15m7XWiXJw9MiVOOGhRvR1GFUl2K4RKj4fhMB1PE3Ua9JMaF098AS6wY0WYAxqqvET1boe0Fr0Bpgshh_668eMYu6OcipTF_4737W2hky5zokihyKkHABXk6wN7ETSBDT2nx0.png)

Once you’ve published your container, your new tags and triggers will create advanced scroll depth data in your GA4 property. [Google says](https://support.google.com/analytics/answer/9333790?hl=en) it can take 24-48 hours for data to start showing in your reports.

The next section will show you how to find scroll depth in Google Analytics. So that you can start using the data to improve your content.

## Where to View Scroll Events in GA4

You can find Google Analytics scroll depth data in two places:

1. Standard reports
2. Custom explorations

You can use standard reports to get a high-level snapshot of your scroll performance.

Explorations, on the other hand, are best suited for more in-depth scroll reporting (using the tags and triggers we set up in the previous section). You can create one of these advanced reports by using the “Explore” tab in the left-hand navigation.

Let’s start with the standard reports. These rely on the default scroll depth setup within GA4.

### How to Find Scroll Depth Data in Standard Reports

You can see a snapshot of your scroll data in your “Events” report.

First, click “**Reports**” from your Google Analytics property.

![“Reports” selected from Google Analytics menu](https://static.semrush.com/blog/uploads/media/0d/c3/0dc3ce9d2b5ca692b91f657e908d9727/9262b40fda9c56377df65a600821676d/75GpTTVB_CjNJw1NWXk2FpqG94pO9873BoDiY8LLcl2WA9p3b45TVRAVmk5w-WyUxctUoNmVXzmmYhHTWoL6ahiSNFnySm0adOvF_utz6YO6JH_yrIiWDidXIRCLJDgxWz6I5aVUrSHu29_M6-NTS44.png)

In the “Life cycle” menu, click “**Engagement**.”

![“Engagement" selected under "Life cycle" menu](https://static.semrush.com/blog/uploads/media/b0/fc/b0fcd69889d37fbd5440bd05dcb329a8/3b8e3527acd75178683cfa354cb449df/o1pfz6LW908RqC8dAMIB_uc3YZaU48GRodHRZuB8Grw0Vh4epB6CUl7ZN0guBNY8YoZcagXugZj7LQqksjW6CmZNKf78lpkN9PlKR3R5sJowMZTvKxW7GkIhDLkIHbbpcBFLJ1Dl4RbIpxz60HMOnZo.png)

To see a full list of your GA4 events, click the “**Events**” report within the “Engagement” reporting area.

![“Events” selected from the “Engagement” reporting area](https://static.semrush.com/blog/uploads/media/88/7d/887d9d1349e4423bb7ffb84c77a74683/056bdcea30ef50fda9a3fa61f8c69353/7GMPhRd9bcG6i2md7SQGyLgPluw3mm1NT__fh-SyUFVbm2kR8w8FTqR1e4hTiuUdFcukrnJeE5_TiNcLZragftMETp1SPRUmJsV5Xq3f7Iul42zIT7uAYkKbAiiuUXBIKq4h8R12GB1FaFsLtZSYMko.png)

You’ll see a list of all events sorted in descending order based on event count. You can click into each event in the list to see additional details.

!["scroll" even selected under "Events" report in GA4](https://static.semrush.com/blog/uploads/media/58/1c/581c4214397ca04775afd122b30cc4cc/65da1524319c228975024c067f68b4f8/IFHCqP5tprGzTVRhaB5TZaALIK2q56PnWGw1m0obWg5yNosRHlO30DJesNr96fIokwae7jgwPVWRw8Db7EtJdNl1t_Mv_KYa9CgCtocoorJsm7JylX9w-aVwOFVT4FP1NWi13zk4GxGmQwYkeApOevo.png)

The example above shows the default scroll event that will fire at 90% scroll depth. You can compare the number of scroll events to the number of page\_view events to get a sense of how many readers are fully consuming your content.

But you can get more actionable data with custom scroll event data in Explorations.

### How to Find Scroll Depth Data in Explorations

To analyze detailed scroll depth thresholds at the page level, you can use GA4 Explorations.

First, click “**Explore**” from the left-hand navigation.

![“Explore” selected from Google Analytics menu](https://static.semrush.com/blog/uploads/media/ae/4b/ae4b391774173fb6bd23c2fa239deeab/33f515a4a11a8d02a7cf632692e6c97d/k6p13nzKLrxuJtFf-JULHgwDe5-Sg5B_2qRWZJ9ft7mKF-SclNlFZvS9hNgfComxfBNqMF56ntMa7esqUytzUjILICyehlh8NMK672UPiMFP8seQ9sucoaeUXLUPQsKEbMqdpdulq69DJHTclRXHJ2A.png)

Then, click in the “**Blank**” report template to create a custom Exploration from scratch.

![“Blank” report template selected under "Explorations" section](https://static.semrush.com/blog/uploads/media/7b/43/7b43c8a817c4666c367723af75d3c7a6/ecc962d9f963a45b28c6a09b6427eb21/yfRfEiYvMfQg9l1qOi0lBsx1shCMKHVSGtEruqsA13mXTfgkpQj-yeZpYP-Kk3oSuMhzgV6TvN0E1VKraEU6llZ-T8mojH1X57s97hxQwrGuZigRrMAz8GC11UfDMKcKbpdHX7eCHjmWlwdAaXr0j2c.png)

Now you can select your “Dimensions” for your custom report.

Click on the “**+**” sign to the right of “Dimensions.”

![“+” sign highlighted to the right of “Dimensions"](https://static.semrush.com/blog/uploads/media/eb/66/eb6605ae9e83572ffd3f954cd0d33ec2/ef10976a60422424aa51e4c814424e54/6jpS_SmsA1xcJyWd1Py7MyglVfSduG2Yv3ltMNDDxIQ-U5RQ7NV3CsKXx_dbPmrxHa8Gto3-H9wN9hi6VuOZTQRHkPsIkECEY1Pw_-EWuV300iT33cHgwBaqpPFxPWbJnvYg7GSjMDPlnF3WJXSrdiI.png)

You’ll see a list of over 300 dimensions arranged in groups. You want to analyze scroll depth at the page level, so click on the “**Page / screen**” drop-down to expand your options and find the dimension you need.

![“Page / screen” option selected under "Select dimensions" drop-down menu](https://static.semrush.com/blog/uploads/media/d9/fa/d9fa871d7843bf061975701f03d9d935/8cf1d6849b04764d021c497e200231f5/k0-A9NUGYJZ2qW6iNS-QTebP6rk7wI-UEG46A2RCd7RzEsmanmF3hBL3u-qAGCXSQ3awqC08_7zSYX-QrjVTWIkDIvk0Ywd4wDPGmcZOMFImrkKTXbyxqvvURsP_I2eh8qx-ZharcCWjNiKR3KMS8Qs.png)

Use the checkbox to the left of “**Page path and screen class**” to select this dimension. Then, click “**Event**” so you can select the other dimension you’ll need.

![“Page path and screen class” dimension selected and "Event" option highlighted](https://static.semrush.com/blog/uploads/media/83/1a/831ae53c82ead9506ac1b086480118ca/5dd6ed579963b1581f333e02883ee7fb/LHTgw7nMz-SqAC7fHqQfcZBaTe5GLSghRjSO4hhq7s1JwenIz5IZ_kjODZDxxMdCSJOTwHvFyeWNd8ce9c4XRGFCLBE_OCaDT7YYcjp7fBpklj4qRM9QuDVVt9tKGO3avbzIj86ujw6nYQRrN_8DzYA.png)

You can now select the “**Event name**” dimension using the checkbox. Like this.

Then, click “**Import**” to add both dimensions to your report.

![“Event name” dimension selected](https://static.semrush.com/blog/uploads/media/0d/f4/0df4b63b6ecaaee6201246879d5a575e/7d0e4b1042663e2fc0ae6a6d50396f57/rTWRQCrlDowWyZSMh2i61Q1g_OPqvVnzQrK_B7cW9zPNsh59Iv-ZrjUtjqXs6lZV-DXeZeLnQGYnXeZPR7l7RAmoBsPk0kQQDIsuAkFCilv1bMFsTQuGMgkOA_PtJ5JUtCQJqCteAXbhNIazOuqSlmI.png)

Now, click the “**+**” sign to the right of “Metrics.”

![“+” sign highlighted to the right of “Metrics"](https://static.semrush.com/blog/uploads/media/2b/21/2b21f11aeb47eb27136abc54c4dfb7ec/33c29f6b48fe68bb4ac7828c26d1566e/_Tb21XUrkdt8Mq6yZcked_BCXPCrfIIimwfGJRml7p06bK1UZDyoWo2Fjdh3NSJFNUB1epe0l7Ohk-jJ7_T66LFf9qxgO_bBKApm_7cLEH2CMKIYuRZbrfCp6wNjag33abbFJ8c8NsnHtQb3eX6DFCw.png)

You’ll see a list of metrics you can choose. Click into the “**Event**” group and then use the checkbox to select “**Event count**.”

Then, click “**Import**.”

![“Event count" selected under "Select metrics" drop-down menu](https://static.semrush.com/blog/uploads/media/61/49/6149b1c9b0b235f8565e2b955cf9df6f/9ca6730e50636b25accbfe2a9c39e8f4/HKCCyToWYfQ9oXHjuq67YSgu61y0aNRpFBm7OKDWkus49oq4ngTCz7vZAuvJ67Yv0t3OG18xJvX-USH6ahf7_G4pZZF3XCTJqHNvMLwewHu4ObGow16nprHmOKd1C2uLXi1tPs67hUZLpqiuhWs6eKQ.png)

You now have your dimensions and metrics ready for your report. Name your report using the “**Exploration Name**” field.

!["Scroll Depth Report" added under “Exploration Name” field](https://static.semrush.com/blog/uploads/media/7d/22/7d22e67f59ac65438ce28be6a1b92bd3/fb2f9a02914c0e1acda7cec02b8ff9bb/r0Iht8mZ-FEw7hvJ1TJWYBCWYrocYNk39ef3z04rPKMibPiq8W8ujy159TmXH5-WiElMcRiiTQTnvlU9VSO6FJlofyc7sOOiiE56Q91s2jWEEol8261Z__X_jtGK2vqFNqukWpQRtmxIxagcNy0Ba3E.png)

Now, it’s time to add a filter to look at scroll events. To do that, look within “Settings” and click on the “**+**” below “Filters.”

![Add a filter under “Settings” section in GA4](https://static.semrush.com/blog/uploads/media/27/da/27da08ad854cff70323ee39efa4a3882/7f5f1fa948661092feeeb897f9c5740c/8lWJdQuXss6ogKSWZt61LuMw7FWgKM12nbMnadtV7NLD4MjfY3u_OAUa8ZXZ4pILFBOYUmUPEvZ_Do6kz3EO57nsV_MTn-m0JhKDKuhWyeXodYaTKLEaZqZJgLc6sEf7ZRgck1yuSC1CJLdNl4l-Og4.png)

You’ll see the two dimensions you’ve imported. Choose “**Event name**.”

![“Event name" selected under "Dimensions" section](https://static.semrush.com/blog/uploads/media/5b/f8/5bf87571fae8e0ba3bbd12bca3a18831/1a06755b48fea5ef373e055da5d91ff4/Y7SG3pb6R38fvC_0YcBADiVirwVEtllBvyALFx_LjG86deihUh1Lx8naQ1JB6NwxK5gloJbrtbYqkFK6hE-3GTgtURDRmfde-P2meZ4rUyBKjWuAxANK_xXgO9zvqPx2ir9DnIiOaTdhRSAWW_wy8mM.png)

Now, you can set the conditions of your filter using two fields.

![Event name conditions fields](https://static.semrush.com/blog/uploads/media/21/c2/21c21a44a9d7889fb0df53c359fa1b90/84f8c036d26ae861a68165a40777862e/uWhx3NFWyWHWAfWV5kAiL2y8za_jZYtaPO7KLr5xt9jgkS3z3CpApXGCQ4HPagQ7DuYJ-oUvRISPYQ_5JAvfA1QXcOE2g9TpBGfsTIq2SHe3T_2x0ETp5etLf51hKxygoxli4pLGjsfiG5tGHrYwkNM.png)

Choose “**contains**” as your match type in the first field. Select or type “scroll” in the second field to include all of your scroll events. Click “**Apply**.”

![Conditions "contains" "scroll" fields selected under match types](https://static.semrush.com/blog/uploads/media/70/0e/700e6af2eeb375d16899de5127623efa/7f281b88084b43e6eff6cfcd0bd95e72/SWxuci2PeihA2NFrIo6xhnLHmbBRqHMvw-m-HuDtl18y68EQo1kUWvr-wuyaASqmenSgJGeQmWRpdJ2fxTki7GhMzYbSN9WFM4prTuM5_u4vpAOTQTvEEjLC__BDKp_i9oS0Yc0FU1Uk_bGCFOT6hFs.png)

The last step is to add your data to your report. To do that, double click on each of your two dimensions and your single metric from the “Variables” section.

!["Dimensions" and "Metrics" fields highlighted under "Variables" window](https://static.semrush.com/blog/uploads/media/e5/0d/e50d5b5ed6a0f517e4f10bd46ac246a7/a6c0d9abcc81e6af0d677380a7e06da3/vBcEIF_3WbEoSMSYsyT3X-UHfT5zVIjywfvY8ivY8ee3yzQLY5BHb5HUD3i8hv5g2ZEfTCGCuNNqzbk7-UpgQzqovorvXGWVxkH3etOLiOYcsAbVbCby75i4pBCXKSypR6dZCk-tRFClcN2HLEbqrbg.png)

Finally, change the “Nested Rows” drop-down from “No” to “Yes” to organize your data at the page level.

!["Yes" set under “Nested Rows” fields](https://static.semrush.com/blog/uploads/media/de/ff/deffe21f3b8d89bd1fba1d0371dd3b69/a5bc207cf0dbd82eaeecbc2df63b6f8c/WD2zwoyVIS5hyu_H6Ul-xJosLx7n2lGc6ltGXoe1p9Xjh3gj2EWVUZL2tn_m7seRWYdzpNlIAJWSh7OmvLxVeBX-gOOKJzV_ol3z5iXvvC35gzn5VLRcVjvGyhQxBxXXZPZCzoSoOIuLoiUKJabvkuo.png)

Let’s now look at three ways you can use your data.

## How to Optimize User Experience with Scroll Data

You can uncover page-specific insights to improve performance by comparing scroll data at different thresholds.

Let’s say you’re a marketing manager for a B2B website and you rely on your blog to help generate leads. You’re interested in the performance of the specific articles on your blog.

You track scroll depth at 10%, 25%, 50%, 75%, and 90% and you use that information to find places to improve.

Here are three ways you can do that using the report you’ve built in the previous section.

### Learn from Your Top Pages

You can identify structure and layout patterns in your top performing content that you can apply to other articles.

When you analyze your top four articles by total page views, you notice that the first and second have significantly more readers at the beginning of the article. You look at the **scroll\_to\_10** event counts to see they are more than twice as high as the third and fourth articles.

And yet the **scroll\_to\_75** event counts for the third and fourth articles are more than three times as high as the first and second.

Why are your top two articles getting more views in total, but fewer people are making it all the way through them?

![Page path and screen class report](https://static.semrush.com/blog/uploads/media/72/a8/72a82f3858d49ed971b74a9de888caad/eb184426b449285599a7b8d5803fe279/k2B4Fe6TydPLP_L-MZLPv10bpOJCQw-UfbaPIGpF7l9HjCsDNU6l-6_ZrpVrQJEhmxwfpGsxPQtDGNsRzCZJcZON-i-g9p0jXfaOQFzs4NnysD23u5CI5Dkh0Anp5SIG3GzmhT5HKYOZDgGHJFwf79M.png)

You review all four pages and see that your third and fourth best articles have significantly more images than the top two. They also feature shorter paragraphs and more white space.

In contrast, the first and second articles are visually dense without as much white space. You surmise that the layout and structure may be holding your readers back from getting all the way through.

You plan to revise the first and second articles and measure results. If you get the results you hope to see, you can continue to roll out the changes in other pieces of content.

You could also use our [keyword research tool](https://www.semrush.com/analytics/keywordmagic/) to see if there are any keyword opportunities to improve the ranking potential of the third and fourth best pages. You know your audience is finding them helpful. So, optimizing them for other relevant keywords could improve their overall performance.

### Understand Where You Need to Improve Introductions

You can also compare the number of **scroll\_to\_10** events with the number of **scroll\_to\_25** events to understand how well your introduction is grabbing attention and motivating your visitors to keep reading.

You compare your average ratio for all articles to the same ratio for new articles. You do this by dividing the number of scrolls to 25% by the number of scrolls to 10%, then multiplying that by 100.

You know that your overall ratio is just over 80%, and you’ve just published a new article that is performing slightly worse than normal. You get this number via the sum: (15/19) x 100 = 78.9%.

!["Even count" filed highlighted for the two scroll events in a table](https://static.semrush.com/blog/uploads/media/fd/84/fd84489745a6dcc2a3eeb0d034e6f0ad/008e7a8358e7cb3551f9d489f6eca5dc/4P8fkI77N8_yWqmSvGm_FdZ3tDSjcVjk0Ybr_hdsOg7sPzQ3NhUrCoynXkcCvYGeQjYxC8AJi79qp5LQ0b5H6oThcUObURgqd6xIVcWfuTv5jmojoGV0XLWYcgF6rjG95TUEft4QjG-0FSbstC3zpTA.png)

You want all your new articles to hit an 80% or higher ratio. So you ask your content team to revise the introduction to make it even more compelling.

If you find articles with very few people getting past 10%, you might have a real issue with content quality. Or you might have a title tag and meta description that don’t accurately reflect the content.

You know that if more readers get beyond the introduction, there will be more opportunities for them to see your call to action (CTA) and consider becoming leads for your business. So you prioritize updating the introductions, titles, and meta descriptions of articles with very few people making it past 10% scroll depth.

### Find Opportunities for Multiple CTAs

You can compare the number of **scroll\_to\_25** events with the number of **scroll\_to\_75** events to understand how engaged your readers are in the main body of your article.

This matters because you typically place a single CTA about halfway down the page. But you know some of your content maintains readers’ interest better than others. And you want to test two CTAs in those most engaging pieces to see if it boosts conversions.

To find those test subjects, you compare your average ratio for all articles to the same ratio for individual articles.

You know that your overall ratio of scroll\_to\_25 events compared to scroll\_to\_75 events is 40%.

Here is the article you’re analyzing. Instead of your normal 40%, this article has a 75% ratio (6 / 8 = 0.75. Multiply it by 100 to get 75%).

![Event count shown in a table for scroll_to_25 events and scroll_to_75 events](https://static.semrush.com/blog/uploads/media/1e/4d/1e4dc716bc9a21a7f6358ca71d335d1e/9b8e9f144a678c0b9d6a0df5da3510c5/MZ6dQfRfcgCMvUqt6iZ8xbf5y0GrDhl3k-oD8VV2sK9CztWN4wED-nONgEU7MYTqfItWkDd1wjgzHFBIlXRbdRjnIekiKAbF5jVjy1hE0wJYVV2t3qkbG6-hJbWWtVyJ0PGWX4-Mn_0mlC54NdmiSA8.png)

This would be an ideal candidate for testing an additional CTA, as your scroll depth data shows it’s a particularly engaging piece of content.

### More Ways to Act on Your Data

Taking action with your scroll data is one way you can improve your website’s performance.

And you can use scroll depth data alongside insights from tools like Semrush to take things further.

Semrush’s [Project Dashboard](https://www.semrush.com/seo/) can help you manage the health of your website so you can put your best digital foot forward. Fast-loading, error-free sites are better optimized for search engines and more likely to keep your audience scrolling and engaged.

![Semrush’s Project Dashboard](https://static.semrush.com/blog/uploads/media/39/e4/39e414995a66d4b2e735d52b5fa975df/31a9590fd1dfd675754b9c0c98666791/sWY6ivEL5JRgA5dv4vBipzhJLGwiRJEyQZBDoGZHVdMv3knA2XVmqLzmLo2MxuVexd6MGrQ3Fwfi_6HH6yieJV6KtrHiYHsnDnWC2C5wh_hwQJ5IDWJHS2R45rOyxNnWWISzINVtPteWT1zpG7jlqdc.png)

And you can integrate this with other digital platforms like Google Analytics. So you can learn more about how to improve your top content.

For example, [Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) shows your top landing pages from Google Analytics combined with keyword data from Semrush and Google Search Console.

![Organic Traffic Insights report](https://static.semrush.com/blog/uploads/media/fd/aa/fdaaaa7f5634de97f709597c85e1e6ae/02d88e9b22ff8aa2d2751bf7032f71fd/slTpVvRHrLKKhVs4BKFxBZm5sPlwxwxXWzbI_DRydWUDo2AGr96fhUSPAUNAlHUvKuh4oR7F0IQmUuESEphApbImnEWibsivvWiRAPU2_S9Ahtnq7BCVQ33uHP1Rfv4NNTrk58Cuxa_3kQLWcssO1f0.jpeg)

You can use it to prioritize your efforts to focus on ranking your most important pages. So you can improve your ranking potential while also making scroll data-informed content enhancements.

Are you ready to try out Semrush to get more data you can act on? [Start your free trial](https://www.semrush.com/signup/get-free-trial/) today.
