---
title: "Google Analytics 4 Dimensions: What You Need to Know"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "google-analytics-dimensions"
url: "https://www.semrush.com/blog/google-analytics-dimensions/"
canonical: "https://www.semrush.com/blog/google-analytics-dimensions/"
author: "Suman Chatterjee"
published: "2021-09-10T12:13:00+00:00"
updated: "2023-11-02T16:37:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2023_aging"
  - "time_sensitive_title"
schema_genre: "Analytics"
fetched_at: "2026-06-12T15:41:05+00:00"
status_code: 200
html_hash: "f69e5bfa4eada64352f94533547e2d4a7e741e21306c35298b26631f93b2d975"
clean_word_count: 3024
clean_char_count: 22143
---
# Google Analytics 4 Dimensions: What You Need to Know

## What Is a Dimension in Google Analytics 4?

In Google Analytics 4 (GA4), dimensions are data attributes or characteristics that provide additional information about your website’s users and how they interact with your website.

Dimensions provide context that makes your data meaningful. Like in the image below:

![Users by country report in Google Analytics 4](https://static.semrush.com/blog/uploads/media/a0/d2/a0d2eef03404f7bfb848bb8cc9564610/b13a8b624f00eab2f2a5b984e315fcdb/iFmXjwpOrCa2umAX02DkfioNwnYCj8exx7RidP-5L7NEaN0_H12M9pY5MwNRePPKCEVoP_Eb6_rHTzoOrhxs17i-d8-tQHolbfh2sk7NFS4BccD4tL7mfxgXcsrMPXpTwG7KwhPPK4XrnrkUrDhhq7E.png)

For example, the “Country” dimension indicates where a website visitor is located. Which means you can see how many visitors came from different countries.

Or it could be the “Device Category” dimension. Which reveals which kinds of devices your visitors use to access your site.

Examples of dimensions are:

- **Device category****:** The type of device user activity originated from (e.g., desktop)
- **Source / medium****:** The referring website/platform (e.g., Facebook) and the broader channel category that refers the visit (e.g., “email”)
- **Browser****:** The browser used to access content (e.g., Chrome)
- **Country****:** Geographical location of the user (e.g., United States)
- **Language****:** The language the user’s browser or device uses (e.g., English)
- **Campaign / Campaign ID****:** The name of a marketing campaign that led to a conversion (e.g., “Spring2023\_Sale”)
- **Page location****:** The URL of a webpage the user visited (e.g., “https://www.yourwebsite.com/blog/how-to-train-a-puppy”)
- **Custom dimensions****:** The dimensions you create yourself to track specific information about your users

### Google Analytics Dimensions vs. Google Analytics Metrics

Note that dimensions are not the same as metrics. Dimensions are qualitative aspects of your data.

Metrics are the quantitative aspects of data—measurements. In other words, metrics are concrete numbers.

Here are a few common metrics you will see inside GA4:

- **Sessions****:** The visits when your website or app is the user’s primary focus
- **Average session duration****:** The mean time (in seconds) of users’ sessions
- **Views per session****:** The average number of pages viewed in a session
- **Bounce rate****:** The portion of sessions that weren’t engaged
- **Transaction****s:** The number of completed purchases
- **Total revenue****:** The revenue generated from purchases, subscriptions, and ads

You’ll find metrics like these under “**Reports**” > “**Life cycle**” > “**Acquisition**” > “**User Acquisition**” inside Google Analytics 4.

![User Acquisition report in Google Analytics 4](https://static.semrush.com/blog/uploads/media/b1/3f/b13f198adaed45c57b1d0f80b154b639/63e0dc1901eb5004c70c51764f4b57a0/image.png)

***Further reading****:** [What Is a Metric in Google Analytics? [Explained]](https://www.semrush.com/blog/metrics-in-google-analytics/)*

## Why Are Google Analytics Dimensions Important?

Dimensions help you understand your data better. And help you gain insights you wouldn’t otherwise be able to.

Here’s an example of how dimensions work:

Say you have two views on your website. One is from a 30-year-old woman from Mississippi who got to your site from X (formerly Twitter) using her desktop computer. The other is a 50-year-old man from Yishun, Singapore, who landed on your site from a Google search engine results page (SERP) using his mobile phone.

If dimensions didn’t exist, all you would know is that your site got two views.

But dimensions help you see much more:

**Visit #1**

- **Session source****:** X (formerly Twitter)
- **Age****:** 25-34
- **Country****:** United States
- **Device category****:** Desktop

**Visit #2**

- **Session source****:** Google
- **Age****:** 45-54
- **Country****:** Singapore
- **Device category****:** Mobile

## What Are the Types of Dimensions in Google Analytics 4?

Google Analytics dimensions can be divided into two subcategories: predefined and custom.

Predefined dimensions are built into Google Analytics reports and are ready to use.

These are the main groups that all have specific, predefined dimensions within them:

- **Attribution:** Includes all dimensions that provide information about how users arrived at your site
  - **Google Ads****:** Covers dimensions related to Google Ads
  - **Search Ads 360****:** Focuses on dimensions associated with Search Ads 360
- **Demographics****:** Contains dimensions describing users’ age, gender, and interests

!["Demographics details" section in Google Analytics 4](https://static.semrush.com/blog/uploads/media/29/91/29912520fa7f68cd7a5b41ff98698dec/11354be5be94b63e3fbf5248e81e817b/HM7sufeNv9QfvYkPoy5AScrMZrLZEbLFuRKKATfbPUL0Mvl3e-oLjuZNPauVFKltvdNl6V8pjgIEKDQrg9Drh_-CW8EoXXr88SIMa4jhjarW-OyyqvlcZ-P3cDZw5n7s1JY5bIPeIsFK79dkK2DwZ2Q.png)

- **Ecommerce****:** Encompasses dimensions concerning transactions, products, promotions, and ecommerce-related attributes
- **Event****:** Provides details about specific events and their conversion values and statuses
- **Gaming****:** Relates to dimensions associated with in-game events and achievements
- **General****:** Includes general metrics that may not fit into other categories, like file information and search terms
- **Geography****:** Includes dimensions pertaining to user’s geographical location
- **Link****:** Encompasses dimensions related to links and outbound activities
- **Page / screen****:** Covers dimensions regarding content on your website
- **Platform / device****:** Offers details about users’ devices, browsers, and operating systems

!["Tech details: Browser" report in Google Analytics 4](https://static.semrush.com/blog/uploads/media/da/0b/da0b3bcc036a2224d7a10e43abaccf2d/9bcdd47ddca382ed0f6890efc2a2b87c/Qep2LxSv4-PAF0F93kETbFkSsbQ0uiXlsAuCYsR2EVT3svxqCEtPCG4eNAsRSwFUDxv7dqwK3J6-HJ4UJcVaCR1yScFlVIKrIovjmuzYQ6oh8OLnYwzPD2mxVv_etTLfA4uNI_YbBqGSSHNEJ4IrZwQ.png)

- **Publisher****:** Comprises dimensions associated with ad formats and sources
- **Time****:** Contains dimensions related to specific times and dates of events
- **Traffic source****:** Pertains to the origin of the user’s journey
  - **User-scoped****:** Focuses on the user’s first interaction sources and campaigns
  - **Session-scoped****:** Contains dimensions related to session sources and campaigns

!["Session campaign" dimension highlighted in the Traffic acquisition report in Google Analytics 4](https://static.semrush.com/blog/uploads/media/04/2a/042a48623932800c2d38e2d337ea3821/d90cf5200475943afa7ab22c5e44a55e/image.png)

- ​​​​**User****:** Involves dimensions describing specific user statuses and traits
- **User lifetime****:** Focuses on the user’s historical interactions and purchases
- **Video****:** Covers dimensions associated with video content and providers

***Further reading:** [Check the full list of dimensions here.](https://support.google.com/analytics/answer/9143382)*

Custom dimensions (which we’ll discuss more later) are different from predefined dimensions in that they aren’t automatically collected by Google Analytics.

## How Do You View Dimensions in Google Analytics 4?

Dimensions appear all throughout Google Analytics.

When you go to the “**Reports**” tab inside GA4, you’ll see reports categorized into broader collections like “Life cycle,” “User,” etc.

Within individual reports, the dimension appears at the top of the table on the left side. The dimension values are listed underneath.

![Dimensions and dimension values highlighted in the “Reports” tab inside GA4](https://static.semrush.com/blog/uploads/media/1f/27/1f27342b9d77b409fc1c289e5b09c7fb/fa965bef020c397d66dbbc7fc6b1d135/image.png)

The column names on the right side are metrics. And can be recognized by their numerical values. As you can see, metrics quantify the dimension values.

For example, let’s say the top row in your “Traffic acquisition” report shows you got 10,000 sessions from organic traffic. That same report also shows you how long users from organic search stayed on your site (average engagement time per session) and how many conversions they drove (conversions).

***Further reading****:** [What Are Google Analytics Sessions & How Are They Measured?](https://www.semrush.com/blog/sessions-in-google-analytics/)*

## What Is a Primary Dimension in Google Analytics 4?

Primary dimensions are the default dimensions that a Google Analytics report is sorted by. And appear on the left-hand side at the top of tables.

Like this:

!["Page path and screen class" dimension highlighted in Google Analytics 4 report](https://static.semrush.com/blog/uploads/media/60/77/6077555a19a4d1666f6f3a88e46990a5/85e74a83529df15f68ee0aaa296fc200/eexgUI--wWbQxkoH7bi5uJfyrG2V-JL7hDMoS3ey0INbEJ-Bh9aeYX30YU-aQjv2ytCrjw5hdf_J-I34YPTLBCVBHCuKRTgQ0GJIhfkZPwks5c-dpFLdPDXSG-0Ye5Cn8Rb0XKw5aFAs5oBiKLkfPH8.png)

You can also change the dimension for some reports by clicking the drop-down menu over the dimension name. And choosing another one.

![Changing dimensions in GA4](https://static.semrush.com/blog/uploads/media/5d/cf/5dcf3d011ed12249710f7e0b40f79bb2/e918c99f67cddd3aaf70b1fc7f78e713/image.png)

This allows you to change how the data is displayed. So you can learn more about what interests you.

## What Is a Secondary Dimension in Google Analytics 4?

While the primary dimension provides you with the starting point, a secondary dimension allows you to explore data based on what you find most valuable. And adds additional context and depth to the data storytelling.

To add a secondary dimension inside GA4’s reports, click on the ‘**+**’ sign beside the primary dimension dropdown.

![Adding secondary dimension in GA4](https://static.semrush.com/blog/uploads/media/5b/74/5b74eb11e8d4653cf29121f4b31360e8/8e741c8f0ddf4c992e9d747c7c8b0844/image.jpeg)

Imagine this:

You select the “Session source / medium” primary dimension to see where your traffic is coming from in the “Traffic acquisition” report. And notice that much of it is coming from Google Ads.

Then, you add the “Session campaign” secondary dimension to find out which specific campaign drove the most traffic.

This gives you a clearer picture.

## What Are Custom Dimensions in Google Analytics 4?

Custom dimensions are dimensions you configure yourself to collect specific data (attributes) on user interactions.

Not every business is alike—so they all have different needs.

Custom dimensions fulfill those needs by allowing each business to create dimensions that provide useful information specific to them. And they allow you to create customized reports that provide even more information.

But you don’t have to use custom dimensions. In certain cases, they might not add much value beyond what’s already provided by Google Analytics.

### Understanding Custom Dimensions

It’s important to understand the relationship between all the elements that go into dimensions before creating custom dimensions.

A user represents a unique IP address visiting your website. And there are different properties that describe them (like where they live and what they do for work.

An event is a user interaction on the site. It can be a scroll, a click, a view, etc.

Every event contains parameters—bits of information that provide more context about the user or event. For example, a click event will contain parameters that provide information about the URL that was clicked, the link’s location, etc.

When you group user properties or event parameters, they become dimensions.

## How to Add Custom Dimensions in Google Analytics 4

Before using the custom dimensions inside Google Analytics 4, you need to create them first.

Also, keep in mind that the reporting on custom dimensions is not retroactive inside GA4. Meaning you need to set them up before you can begin analyzing the data.

So, how do you add custom dimensions in Google Analytics?

It depends a bit on which type of dimension you’re creating (event-scoped, user-scoped, or item-scoped). But we’ll go over how to create an event-scoped custom dimension.

The first step is to create a custom event and parameter in GA4.

The event fires when a specific condition is met (e.g., someone filled out an information request form). And this event contains custom parameters (e.g., the form was located on a landing page).

You can add custom events and parameters through Google Tag Manager or directly in Google Analytics via “**Admin**” > “**Events**.”

While the latter is convenient, it’s also limited. So, it’s usually best to use Google Tag Manager.

Get started by logging into your Google Tag Manager account. Then, you’ll need to enable the appropriate variable and configure your event.

You can learn more about this in our [guide to Google Tag Manager](https://www.semrush.com/blog/google-tag-manager/)—just make sure you select “**Google** **Analytics: GA4 Event**” as your tag type.

Once you’ve published your changes to start tracking the event, you can head to your [Google Analytics](https://analytics.google.com/) account.

Inside GA4, go to “**Admin**” > “**Custom** **definitions**.”

!["Custom definitions" selected from the GA4 Admin menu](https://static.semrush.com/blog/uploads/media/7b/51/7b51ccd6571916009f82f10915b1078a/4c11cd906b9b9632ea63dd644f43cdb6/eT-EjvTbktuj0EkdLYLvLCXq8EkhqXe21kiR5paErhnRY7bDN6KtGWIL9KJtrhGhIbKrmiyRlBeluFME46X7bD2dUXjWq6PhxS1bHUHEJe1tHFHKoXE_fPrgyojVz1hKN0bgxmopf85a4vCevqsU60g.png)

You’ll be redirected to a page where you can find all the custom dimensions registered with your property.

Then, click the “**Create custom dimension**” button in the top right.

![“Create custom dimension” button highlighted in the top right](https://static.semrush.com/blog/uploads/media/65/5d/655d356721dd4f38490fde9341eda530/7bb97b156ef2eeb3a5780d14f53de0a0/OPSJejRfeWltY1HkdxwPHsJzqp49Je3YO5duL3lcs0yoGuSt91NSUctU87XZ3r7oP1lVfBiLMF62GcMMdRzL8kjogp16Y-me9GiHw0falC4op1ctvQWd5W0ud47mdCs7KuIgswHIgAecGCPcm_RD2JM.png)

The next step is to fill out the following fields:

- **Dimension name:** You can enter any name you want—something that resembles the parameter’s name (e.g., “custom\_plugin\_text”) or a descriptive one (e.g., “Custom plugin text”).
- **Scope:** For an event-scoped dimension, select “Event.”
- **Description:** If you want to add a description, you can. But it’s not required.
- **Event paramete**r**:** Choose the parameter you want to collect the data on. If you used Google Tag Manager to set up your event, this parameter name should be the same as that one.

!["New custom dimension" window in GA4](https://static.semrush.com/blog/uploads/media/25/9c/259c218ff7b8bf8ae55ddc63976d075e/ca4cf13696be06ae34fe37a94c057bfe/GrWygPyUDIsQJ-iCkBmSNsAjbtmOse_97izPu6YJt2jM_Bx04lzxfFfzNopJ7TSccdJ0ipgEJ2g9C8okJFcYxEh7694jvI0mNBhCIITQYuzJc-T_k6Cevw2aJzHPmWC9DSQ39e5eh1bP4d3TFTH3IgQ.png)

When you’re done, click the “**Save**” button.

The custom dimension should appear inside the GA4 after 24-48 hours.

## Best Practices for Effective Custom Dimension Implementation

Here are a few best practices for choosing the right custom dimension parameters:

### Ensure They’re Relevant to Business Goals

Determine what data matters most to your business. To ensure you’re creating dimensions that are actually valuable.

For example, creating a “Membership level” custom dimension might be a good idea if you run a subscription-based business.

And you might create one called “Content format” if you have a portal with articles, videos, podcasts, and other types of content.

Your business goals decide what data you’ll collect, determining your custom dimensions.

### Apply Meaningful Property Values

Make the values distinct and descriptive so they’re clear to everyone.

If the custom dimension was “Membership level,” the values might be “bronze,” “silver,” “gold,” and “platinum.”

Do you need to add the “free” value? Not if you don't have a free membership tier.

### Avoid Dimensions with Too Many Unique Values

For some dimensions, there is a chance of a high number of unique values.

This is known as high cardinality and applies in the case of user IDs, session IDs, order IDs, timestamps, etc.

Unless you have a website that demands otherwise, avoid custom dimensions with high cardinality. It might mess with your reports and aggregate data under an “other” row.

### Use Consistent Naming Conventions

You don’t want to name one custom dimension “my\_plugin\_url” and another “My Plugin Title.”

Look how the default dimensions follow a consistent naming pattern.

![Default dimensions in GA4](https://static.semrush.com/blog/uploads/media/5a/12/5a12a2786ed709d2c356a19e06c9017b/15cae0935bfcf3e7ae9861aa29fc7080/image.png)

While it won’t pose any real issue, it might become baffling and time-consuming for new users in your GA4 account.

### Prevent Data Duplication at All Costs

Say the collected data already comes with a standard parameter that works for you.

If you create a duplicate one, it negatively affects the storage space and complicates data analysis.

Thus, check for an available one before making a new one.

## Different Use Cases for Custom Dimensions

How do custom dimensions play out in real life?

Let’s explore a few interesting use cases.

### Tracking Differences Among User Types

A custom dimension focused on different categories of users can be helpful for seeing differences in how those groups interact with a site.

Let’s say your site is used by students, teachers, and administrators.

You can create a custom dimension based on user attributes to differentiate between them. And then use it to dig into specifics about those groups.

### Seeing Which Content Format Performs Best

Custom dimensions can help you determine which content format works best for your audience: how-to articles, infographics, news updates, and op-ed pieces.

You can add a “Content format” custom dimension for this. Once registered, you can check for the custom dimension separately, and decide where to double down in the future.

### Discover Your Top-Selling Seasonal Products

If you run an ecommerce site, custom dimensions can help you verify which products perform best during which seasons.

With a custom dimension like “Season,” every purchase transaction gets recorded with additional context. So, you can filter the data for the custom dimension and find the winning products.

## How to Analyze Data with Custom Dimensions

You can access the custom dimension data in both existing reports and ones you create yourself.

For example, you can go to “**Reports**” > “**Life** **cycle**” > “**Engagement**” > “**Events**.”

![Events report in GA4](https://static.semrush.com/blog/uploads/media/e0/f5/e0f5211acef7a8cc455d902ba3f480cc/3a377bc1af45e0cae3b863c965f9b64d/9VZpi4x28EW6ropuQTPXBoetJ_wBcpAPSU_NXZI63n2IZOUsQwjNCSQKYwj60V6FRYOti9pxVavkfvIjeFWAn2SKW2GEdxKJI9pGAXGEbsE-40i3jx2U2EHuFgmt0VkNPDOGGRjjSboHkRmgqF-pJxM.png)

Click on the “**+**” icon in the table to add a custom dimension as a secondary dimension. In the drop-down menu, click the arrow next to “Custom” to see all the custom dimensions you can add to the report.

!["Custom" dimensions drop-down menu](https://static.semrush.com/blog/uploads/media/00/38/0038190244c3b9a3f323e50236f7a61c/3452f0d785d7f0d58124521b7f25230b/XEonAwdxq1LuO0naUab9HGYH1A5U1kczkQp4JApL6M2oFUb01YIg-Fatx4r44-U0IiaNMxF3KWsyXfZHML7vl1JdZdf126HQpn5_w8cXB8o23glGxnctp93UBczeFU16Jl4i_BVk70qZ5lELIZqABfk.png)!["Custom" dimensions drop-down menu](https://static.semrush.com/blog/uploads/media/d7/dc/d7dcc6ae71f18c49a5f1e25bec651382/5aa8deb6e28284e0b1f7b182a92efdda/image.png)

You can also filter the overall report by a custom dimension.

For example, if you want to see only the events where the “ad\_frequency” custom dimension is set to “2,” you click the “Add filter” button beside the name of the report.

Fill out the fields to align with your specifications. And click “**Apply**.”

![“Add filter +” button highlighted in the Events report in GA4](https://static.semrush.com/blog/uploads/media/c7/c9/c7c91083e25c3439737d5e86a032777b/b1ffdac44604322e5216f385f6860701/yr_KufgdmUWJg6nvC7Tdr6o8K7q8E25rTGa6WmYOtzPTAVsYgSnIXvHO3O9rhhHpznFy_y7vuNXev5bAYymrdGvWSVXwCxJE4bl6NiaSdTnpGb-GSQ39URiITGTvqiMCDvI7QKH2fbbvsjk3r8SPFJM.png)

Last but not least, you can also create custom reports that use your custom dimensions via “**Explore**” > “**Free** **form**.”

The Explorations feature of Google Analytics 4 allows you to create custom reports based on advanced data segmentation. Which is useful when there are multiple custom dimensions to deal with.

Check out [Google’s documentation on explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) to learn more.

## Empower Decisions with GA4 Dimensions

Google Analytics dimensions are foundational for data-driven analysis and decision-making.

And with the right dimensions, your data becomes a reliable source of intelligence to bank on.

But you still need additional tools to gain a holistic understanding of your website’s performance.

[Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) can help. Because it compiles all your data from Google Analytics, Google Search Console and Semrush in one place.

Just follow the [Organic Traffic Insights configuration instructions](https://www.semrush.com/kb/587-configuring-organic-traffic-insights-tool) to set up your project and connect your accounts. And click “**Go to Organic Traffic Insights**” in the setup wizard.

![Organic Traffic Insights tool](https://static.semrush.com/blog/uploads/media/1e/8d/1e8d411007c68d19d0f4cd98eb42bd27/6a258cc21e1423de546f16a5bc2224fc/image.png)

You’ll then be able to see a comprehensive report with data on your keyword rankings, traffic, conversions, and much more.

![Organic Traffic Insights report](https://static.semrush.com/blog/uploads/media/9e/9e/9e9e0858a38b625a339e3db5790a029d/0f90ea4e4102319f6cc9106733b7bfbc/image.png)
