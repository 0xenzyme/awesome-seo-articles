---
title: "What Is Google Tag Manager & How Does It Work?"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-tag-manager"
url: "https://www.semrush.com/blog/google-tag-manager/"
canonical: "https://www.semrush.com/blog/google-tag-manager/"
author: "Zach Paruch"
published: "2024-01-04T11:33:00+00:00"
updated: "2024-01-04T11:33:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "Analytics"
fetched_at: "2026-06-12T16:01:33+00:00"
status_code: 200
html_hash: "e6ee552d0c1b12bce4f806eab545834ad9171916020630dce58b370589209d93"
clean_word_count: 3207
clean_char_count: 25239
---
# What Is Google Tag Manager & How Does It Work?

## What Is Google Tag Manager?

Google Tag Manager (GTM) is a free tool that enables you to install, store, and manage marketing tags without modifying website code.

[Marketing tags](https://www.semrush.com/blog/google-tag-manager/#what-are-tags) are small snippets of code that track user actions and collect data.

The most common example of a marketing tag is the [Google tag](https://developers.google.com/tag-platform/gtagjs).

The Google tag is used to install Google Analytics and other Google products and services.

Other common examples include Google Analytics events, Google Ads conversion scripts, Meta Pixel, and remarketing tags.

![install the google tag manually](https://static.semrush.com/blog/uploads/media/bf/2b/bf2b236d94486cefa1fe08cc460c62d6/K73qYRNjrxOOfHJD_s1hJ_HFTJ1T8dE2Y9mXjmKUKd8OYztbS469Is-loKR-mppODf3iDz57jaqjqK8lqUgi3nJKj_jGsiVrUSY1HcCjVpoOO75lp6CT_3aE_vQS4SjhPWCeaKpHIdfzX4CtxsSV8i0.png)

Tags like these are placed in your website code for Google Analytics and other platforms to function and collect data.

But with every code change, you risk losing or breaking tags (or other website elements).

GTM mitigates these issues by allowing you to install, manage, and deploy marketing tags from within its software instead of in your website code.

And the software injects code snippets and marketing tags into your website code only when necessary.

So you won’t accidentally break your website by testing something.

## What Is Google Tag Manager Used For?

Google Tag Manager is used for managing and deploying marketing tags on a website without having to modify the code.

This allows you to integrate easily with other marketing tools and platforms such as:

- Google Analytics
- Google Ads
- Facebook
- Hotjar
- CRM Platforms

And it allows you to track almost any kind of event or user behavior you can think of.

Here are some examples of commonly tracked events:

- Link clicks
- Button clicks
- Form submissions
- Conversions
- Shopping cart abandonment
- Adding items to cart
- Removing items from cart
- File downloads
- Scroll behavior
- Video views
- Call to action (CTA) performance
- Table of contents (TOC) clicks
- Custom events

Due to its ease of use and built-in security features, GTM is also used to reduce dependency on developers and plugins.

## Benefits of Google Tag Manager

While Tag Manager requires some technical knowledge, it saves marketers tons of time and resources.

And it’s free.

Here are some benefits:

- **Reduced reliance on developers:** Quickly and simply add and manage marketing tags without developer assistance
- **Testing and debugging:** Preview, test, and debug changes before pushing them to a live site. This feature helps prevent errors and reduces the need for testing on a live or staging site.
- **User permission control:** Only authorized people can make or approve changes to your marketing setup
- **Versions:** GTM creates and logs a new version of the code whenever you publish changes. This allows you to view past and present changes and revert to previous versions if necessary.
- **Workspaces:** GTM enables multiple workspaces for team members to work simultaneously without overwriting each other’s progress
- **Easy configuration of many popular tools:** Easily add tools and tracking tags to your website code using code snippets or existing templates (e.g., for Google Analytics, Pinterest, Google Ads, etc.) from the [Community Template Gallery](https://tagmanager.google.com/gallery/)
- **Tag storage and management:** Google Tag Manager consolidates marketing tags and tracking codes in one place and injects them into website code as needed. Which allows you to add, remove, and update tools and tracking codes with fewer errors.

![the benefits of using gtm](https://static.semrush.com/blog/uploads/media/86/40/8640101c70e50306f8406d4d71ef8a6c/image.png)

## Should You Use Google Tag Manager?

Yes, you should probably use Google Tag Manager.

Even if you are not super technical or have limited resources available.

GTM is great for adding, managing, and editing website tracking and analytics codes.

And it saves time and resources by allowing you to do these things without changing your site’s source code.

This eases the burden on development resources.

And reduces the likelihood of site-breaking errors.

However, GTM is a complex tool that comes with a steep learning curve.

And setting it up correctly is critical.

But once it’s set up and you’ve learned to use Tag Manager properly, you’ll kick yourself for not doing it sooner.

## How Does Google Tag Manager Work?

Google Tag Manager works by using a single [JavaScript](https://www.semrush.com/blog/javascript/) code snippet that you add to your site as a container for all the tags you want to manage.

It has listeners that detect user interactions, such as page views.

When a user loads a page, the GTM listeners detect the action.

Then they check if the action matches any triggers that have been set up in GTM.

If the interaction matches a trigger, the associated tag is fired.

The tag could be a code snippet for Google Analytics or other marketing platform.

Or it could be a specific event you want to track (e.g., views of a certain page).

When the tag is fired, the code is injected into the website.

Then the tag processes the relevant data and sends it to the respective third-party service (e.g., Google Analytics or Facebook Pixel).

In other words, GTM only injects and executes a tag when a user triggers one.

This reduces the overall amount of code on a website and minimizes the risk of implementation errors.

Tags can only function along with other GTM components called triggers and variables.

They help to determine when to execute the code snippets.

### Tags

Tags are snippets of code that analytics, marketing, and support platforms use to integrate with sites and apps.

They are like observers you put on your website.

They keep track of what users do, like click links or view pages.

And they send this information to tools like [Google Analytics](https://www.semrush.com/blog/google-analytics/) or [ImpactHero](https://www.semrush.com/impacthero/).

Tags ultimately help you understand user behavior.

![GA4 configuration page](https://static.semrush.com/blog/uploads/media/ac/76/ac764cc2a26f8448ef04fab06d01dfe7/96c08f45e0826f4c15c94a8468f5f476/JU2p16zkzuma0fkOpgWimntYUIOYWM1nhlnTbjt8GOQ4k_9U_CNBs3p3zTBNYwNiCoZQPTzX8YTPiQ0IJ4wtn9mppFgOD1qBa1BY5It7boOvZ9xgHOUCGglpj7YDgtbSBpLRYgkcXFtr6HRHf0IaHAs.jpeg)

#### Examples of Tags

The following are examples of commonly used tags. These are tools and platforms often installed with GTM:

- Google Analytics
- [Google Ads](https://www.semrush.com/blog/google-advertising/)
- Crazy Egg
- Hotjar
- ImpactHero
- Pinterest Tag
- LinkedIn Insight
- Twitter Universal Web Tag
- Facebook/Meta Pixel
- [SplitSignal](https://www.semrush.com/splitsignal/)
- Appcues
- HubSpot
- Intercom
- Mixpanel
- Salesforce
- Custom events and tracking

### Triggers

Triggers are instructions and criteria for when tags should fire.

Page views, form submissions, and link clicks are common examples of triggers.

When a user views a page or clicks a link, the associated tag will fire.

Every tag must have at least one trigger so GTM knows under which circumstances to fire the tag.

Analytics platforms like Google Analytics typically use page views as a trigger.

This is because you want analytics data from every page a user visits.

Alternatively, you might only want a conversion tracking tag to fire when a user places an item in their cart.

Or perhaps when they complete the checkout process.

When each tag’s specified event occurs, its trigger tells the tag to fire.

Otherwise, the tag will not fire.

And GTM won’t execute the code snippet.

You can also add variables to triggers to further specify when you want tags to fire.

For example, you may only want your support chat to fire on pages in the checkout funnel.

In this case, you could add a variable telling the tag to only fire on page views of pages with “/checkout/” in the URL.

You can assign multiple triggers to a single tag.

![assign triggers to tags in ga4](https://static.semrush.com/blog/uploads/media/0f/f9/0ff962114cf11c59d66fbdaed99078ab/8df3284738e04823a26082685575c073/BVloercJltPMtlHnJU2EjKdd4hwFI6-WMuTkFrKLFkj7dYiHedR5yLLfij8NwK8RyRg7EeFx2hAh85bLF2iq9ps9VRA7KYKJ3hwA4GaaSDWwP87S64LPWOepEtZI990jDraOdAJVMrciiMYepcYYTlI.png)

#### Examples of Triggers

Here are some of the most commonly used triggers:

- Page views
- Link clicks
- Button clicks
- Form submissions
- File downloads
- Scroll depth
- Time spent on page
- Custom event

### Variables

Variables are additional pieces of information GTM may need to fire a tag or trigger.

They help define precisely what the tag or trigger is supposed to do.

For example, “[Constant](https://www.simoahava.com/analytics/variable-guide-google-tag-manager/#:~:text=The%20Constant%20variable%20returns%20the,type%20in%20the%20Value%20field.&text=The%20obvious%20use%20case%20is,create%20a%20new%20GA%20tag.)” and “Google Analytics Settings” are common types of variables.

They are both typically used to define Google Analytics account IDs (i.e., “Tracking ID” in Universal Analytics and “Measurement ID” or “Google Tag” in GA4).

Every time you create a Google Analytics tag, you need to enter your tracking or measurement ID.

This can get tedious, as most of us don’t memorize these IDs.

Instead, you can create a variable that simply stores your ID.

Then, whenever you create a new tag that requires this information, you simply attach the variable you created.

Another common variable is “Page URL.”

If you wanted to track page views of your checkout page, you’d have to assign the “Page Views” trigger.

But to specify the checkout page, you’d have to assign the Page URL variable and add the URL for your checkout page.

![variables overview in gtm](https://static.semrush.com/blog/uploads/media/8d/6e/8d6e46573feb6383826bdca7e25d39a8/mFJNCyBSKyMI2ONWBlDelhuqGabGMvOYBrmiovDdbgpyupsAiJINja2wvjB2B_NVSPVc1IIsHivVH8qWeuhq2YB6zSA6CL8XiuU3FmWTUnNk1WoaUrOQyb8HKr2oakLDZuiukqg5QZvuBrnaeG-Vpjc.png)

#### Examples of Variables

The following are some of the most common variables:

- Constant
- Google Analytics Settings
- Click URL
- Click ID
- Click Class
- Page URL
- Page Path
- Form ID
- Scroll depth threshold

## Google Tag Manager vs. Google Analytics

Though often conflated, Google Tag Manager and Google Analytics are different tools you can use together to collect and report on web analytics and user behavior.

Google Tag Manager is a tag management system that stores and manages marketing tags and third-party code snippets.

There are no analytics or reports in Tag Manager.

![Google Tag Manager home](https://static.semrush.com/blog/uploads/media/97/f6/97f6b7fce7eea2c15ef01a2285c88700/2aG_BfgOMu5ACxfZgqSlJoeYPMF4CWHDF81D0BrQ7NgY-a_KtC4N3uoVT_Km7CGdljSVEQgn-bGZYcPzjrz6UHiI2sZUq31HUPBp9oVqBmDRuEO76lP1qGc94GeyDcQFcduk-MMCQGNNvOEkdTN7Sa8.png)

Google Analytics, on the other hand, is software used for analytics, conversion tracking, and reporting.

![Google Analytics home](https://static.semrush.com/blog/uploads/media/34/f8/34f84aa1a7cd7b0f53b838287a36f6ce/CujHwrBUrwKTPKzJuLC9s0O6X7daUIpFIngQNlRX7XJkvbpOvXrKqgOylp8mWR4mbZmiofooA5DS2dase3PfPyFSaOWN_9YX9qWwDQtYC1CKoE5o_8SyhWgH1f2MohzxTqgkWcaGz_OTvF6kUZdekN8.png)

You can use GTM to install and deploy Google Analytics on a website. ([Google recommends doing this](https://developers.google.com/tag-platform/devguides/prerequisites#gtm_gtag_fb:~:text=If%20your%20site,integrations%20as%20well.).)

### Do You Need to Change Anything for Google Analytics 4?

Yes. If you are using GTM to install Google Analytics 4 (GA4), you’ll need to install the Google Tag.

Aside from that, using Google Tag Manager with GA4 is very similar to using it with Universal Analytics (UA).

One of the main differences is that Google now provides a separate tag for GA4 events.

Previously, you’d implement UA and track events using the same tag.

Another difference is that GA4 can automatically track and collect many more events than UA on its own.

Which means less need for manual event tracking in GTM.

However, you can still use GTM to track anything GA4 doesn’t provide.

Tag Manager and GA4 work seamlessly together.

Read Google’s guide on [moving from UA to GA4](https://support.google.com/analytics/answer/10759417?hl=en&ref_topic=10737980) for additional information.

## How to Set Up Google Tag Manager

To set up Google Tag Manager, log in to your Google account and go to [Tag Manager](https://tagmanager.google.com/).

Click “Create Account” to create an account for your business or organization.

![create account button highlighted](https://static.semrush.com/blog/uploads/media/21/33/21335332a20f49f80bfefe887d667d3e/ON_EHOMyu_-J1RbJDqqetoe31f_sliFUZ0-AFBr3_xLGgMx6ejdLX2QNIEI8CI-4G2wi7tTkY9ZJDmdCYFfqUuCNTSBbWB-VInONRNYA0x_EDqpCljNC08KsZbQB5faz_ya51g4sdDsZGJTeFCec8ng.png)

Enter an “Account Name” and select your country.

Google recommends that each business create only one account—whether you have one website or multiple.

Your company name can serve as your account name.

![account setup](https://static.semrush.com/blog/uploads/media/1a/74/1a74466a0e587c75a464a6c17db36149/-ejNT5G0JRQZDOiqVLgeXf_ivduM7uXC_0tjQj3QolkSd4QwnBLEeavYhkmc5U8t2zTTPxyDIKRMnymTGssUXV0Xln1YVsPVgGlRlT00WE0th7sRlgzrUOXmxuFe2QOaBhWGrrJvUZXOSkFle2iLdlo.png)

Next, enter a “Container name.”

![Container name box highlighted](https://static.semrush.com/blog/uploads/media/af/6b/af6b50d497c662a5f9b09d39f0682ea2/Tm6d6COvhb7_bsj6Mz7Je_OeHJmkm7thhAU_8lbE7pyzvcwffiOQNCj_lkTFDYEr7q1QjzYa2iaHP7omWim1ZK4K4k151p9RG8JSf3r2a-90_NIcIVwNLsk3Ihu8P41dT9eEZtjOzOhECLhHyuR0mJA.png)

Your container is the piece of code you will add to your website to make Google Tag Manager work.

You will typically use one container per website.

So your container name can be your website name or URL.

Then, select your “Target platform.” For websites, choose “**Web**.”

![select target platform](https://static.semrush.com/blog/uploads/media/cf/86/cf86dbe4b4d01f45a197c7d637a8177b/zzC0fohN4eirFNOoO1vFhfsYxarefgrr7IFDy_Voy49uqfgB2-aJHI6VnHchO1P7MwFv_cVtYNcryVeBYUgE-LTa6Cu1MbR7NqkwCjiof5THsTJf3z-2uOGWfC8U9-NUjr8N38YH9u6iul1eUKikIao.png)

Click “**Create**” to make your Tag Manager account and your first container.

Next, you’ll see two pop-ups.

The first is the Google terms of service.

Agree to the terms by checking the box at the bottom of the page.

And click “**Yes**” to accept at the top right corner of your screen.

![agree to google terms](https://static.semrush.com/blog/uploads/media/78/15/78152636f95601821846936fe9645233/uTYlZGYgj79gzTqrGDGIKN7C_QHr47yCnlhZR_fNHqCGk_MXe5pTGAbbYm0IBy-vpyvAcuaW3kI9-2ldv-BeiU8z0wwai2pyvVoBqyJRPG1Lij1y_hSeUU-co0_2Kg7ZuU5cTtd1l11NXZNxs-9sSX4.png)

The second pop-up displays the code snippets you need to add to your site to install GTM.

![code snippet to install gtm](https://static.semrush.com/blog/uploads/media/13/ff/13ff655c50b1ae65fd5801aec2735b51/iPVCFs1ZepcZWkguBmyK5ny_7NtjIEsSiJeWUo6ilQ-L9Hgj43KTeFIjt0x2oQ5aErbopi0DvfFy61V_vSUqAxWC3tjR30bxOlfPlFNwunJYXQkTSeeraL9N8f8rPJ14oqKaIZiLuWMjiqyO-sFWxL8.png)

The first code snippet uses JavaScript to extract information.

Place that snippet as high in the <head> section of your website pages as possible.

![how to add code snippet to your website](https://static.semrush.com/blog/uploads/media/a0/ea/a0ea4bfb7befed5779bb80b384ea0e2e/1HOfopb6BDZZsD7lwlDsuf8iiLunrvNHtmdde5QlceK78ia-9VsIxjt1F0n3UPqS5DuHosoPhIADjKy_fHFsHfcJ6srGfxoog3YXoMqHOV0lHEeScSe_FtO9yxwaOuAg_IzsRwtAvOE1A19W4O0xBrY.png)

The second snippet is an HTML iframe.

Place that code immediately after the opening <body> tag on your webpages.

Like this:

![how to add code snippet to your website](https://static.semrush.com/blog/uploads/media/06/35/06356c5b16d5fc6f926389e23771d942/Ptql3c0vAbv_rUJ9bj_YJa4-r7y_-R20K9mm26oZR7y129YmJtmRcRL93HtTn1vw5vVkrqkcx0HZD3_876rIkZ1eNG40OjJWTBVj3vqYCf2DXzd9AM7JSrRjGFgz3hiNvv-UECXt68A7e1CK3mj3-wI.png)

(The HTML iframe element ensures that GTM still works when users disable JavaScript in their browsers.)

Once you’ve set up your account and properly installed the two code snippets, you’re ready to start using Google Tag Manager.

## How to Use Google Tag Manager

To demonstrate how to use Google Tag Manager, we’ll walk you through how to connect a Google Analytics 4 property to your site.

Begin by logging in to your [Google Tag Manager account](https://tagmanager.google.com/?hl=en).

Click “**New Tag**” or “**Add a new tag**” to create a new tag.

![create a new tag in gtm](https://static.semrush.com/blog/uploads/media/a1/e3/a1e358dd1c98000d7aaeefed6e09b41b/BXAf19v9fDqs-TC18HnWSQjUfMk3Kbts4bafjqJrF-NwD-_k75GKTjXFAY-CYLiKy3olOqNI9Mj1mXOW4ZHgvHOggdlmIcrEBh3mPRpyOKGJKarClZDsUFo2dR8TiVwrd2bexn0_r5wMe3OuMZEP82k.png)

Add a name for your tag. We suggest something like “GA4 Configuration.”

![choose a tag name](https://static.semrush.com/blog/uploads/media/a9/00/a9008722ab3f1bbf595b030a4d853461/husmXTzhmK8Oc5k4FaXcJ1BIMrbnMnWxOqYMSlexNcsI8Crap1pad9WC8NqTqlFip1VEDbNUWImpoHHFHOYHgDGqmzzDmVhN1L79zgIevdK49zIQQ9TPlLw4hNMyfRTwrUHj6ZKzKDchwTs8Vgwhdv4.png)

Next, click on “**Tag Configuration**.”

![Tag Configuration highlighted](https://static.semrush.com/blog/uploads/media/b3/0d/b30d19c1fede31a17fb6a1e41e128075/oOsTVKKVg9EwKdFJ8Fgeptv409AmZ0gY7uRX56ISjfk0tGdYh6NZK3JcHW5DMe2q5v-ic-xSxbSrc65nuPSBe9lfLVdOD8EPq89wsG4nlYoNHdhTZfD0I-dNxb38zNUTx7FJSk_qF7PEyFEkCrqWUNw.png)

Click “**Google Analytics**.”

![select Google Analytics: GA4 Configuration](https://static.semrush.com/blog/uploads/media/79/1e/791ee72618562806c41241d9c083258e/d1c0f84a1ac61af3aa12d04a9d6f6b9a/aRcpHuLR4eVa5lgGCjOzgTos64T5wP1AuMZAbT1vrVBZqBkA3H6qbRICU4vR0STowvGyjGntMrIYk-2EEHGMtQQYGGpj-rGHyL3scWNqJjtfft3cOIXdQpAEJz-dG6zpSnfZ1f7STjaabcOa0vxEfrg.jpeg)

And select “**Google Tag**” from the list.

![“Google Tag” selected from the list](https://static.semrush.com/blog/uploads/media/61/13/6113a63a975b595a905cb77094a479a1/91a2f399db03b3cf4a1b1b6f5efe614c/xshhpTk_QQqihX2hZE7PWqxKexrtxC_H3ByMKMisJy-qSO8-dD5JJVaVkFJb8PDP5OKsAiPeJvOWyh9iyg73A3YPWV-Dn1JDq9OgVBrG-cewNihql2wjg62Ngay2f7VFau2UVo5IUbAnublYtTdPXOs.jpeg)

Enter the [Google tag ID](https://support.google.com/analytics/answer/9539598#find-G-ID) for your GA4 property.

Alternatively, you can create a variable to store your Google tag ID for future use.

![Google tag ID box under ga4 configuration](https://static.semrush.com/blog/uploads/media/d2/61/d261e605bce46f0454c7c01d07a33b4c/a3f1981ad5cf31a579f2a977ae8ff6b5/n73tcTX00hDjhjRTxEe2qyGD3qt2SS7xC3K2TUN_OVFFaKQJxibKQ4cag3YWJKFzj-x6HVZ4iMG2zb29MTRgD65cmsnoPVBILlAgzjQ1D2tEbjwMbesZJTKDji2RT-F-IWA8ca055q1jDhBg3Mgr1Yc.jpeg)

Click the “**Triggering**” box.

![Triggering box under ga4 configuration](https://static.semrush.com/blog/uploads/media/01/68/016891f9cb7ed152c7bd51d9cbc6727c/3e944e76136b743e7ac72dd743b9c45c/Opkow8BuiSxqojLc0_VSn7kcTn4FwxCFuqrVP_gx3MBAjIIYWv1SUMdtfrTSgieTHJTFhFI0y17mewaUx8aXVtj76G63fYXB83hBw-V0bOr8hh004wPaDvqXpYokQVy4C4lfTU2OsABPkmWvM-vRbYI.jpeg)

And select “**All Pages**” from the list that pops up.

![all pages](https://static.semrush.com/blog/uploads/media/63/b3/63b331a16ff929a218585fd4aa67f2ed/X62BFRnZUlO3kVUELCRF75V9Z3FgFgJ1Z3sOTgN3lYn7rzCMslUU5xGqs6ovCGswBnbms0kxQWPGp2i4mHyGp5efTTnEqhsEcqRxk4KtDkiKYKU2RKLB4NO4I-vYp2KVru9FX7fhU5EbtlWK1PjusGc.png)

Then click “**Save**.”

![save button highlighted](https://static.semrush.com/blog/uploads/media/06/3d/063d651f285e40a1580618be7fe29f35/fd5b9e7e95470705126ef401a4fd7df6/W3NghhJF08_E61lRSu_7H5dM_CZTASWImCBZjeyd6lLQsIPP_LkgfY4wZ3WpHLpcm3IirGxsMa_yx0z1YPDlpfYYStoSA2_-jRAUeC8SaHy8G_fOjjXB60OCESgkGjC0YSI94LVVLjhvbhWmIfPEspk.jpeg)

Go back to your workspace overview page and click “**Preview**” to test your new changes.

![test new changes by clicking preview](https://static.semrush.com/blog/uploads/media/38/ae/38aecbca9a29aa47a15e74099fb1b0e9/WP84Vq7-QA4wzbrcFLopTPilY92kCZihssdkcKzMylg8pEFvMFOkf3LLY0jXymF4iiWX8W3hAeXLbYyGye9E4SJhRLznDnIyfVoOXaLRYR_anb9M5-HSMUkzVSliYlcQi_1ovXnJoZJLGdVX43eFN9k.png)

Enter your website’s URL in the next screen.

Then click “**Connect**” to open your site in a new window and begin testing and debugging.

![connect button](https://static.semrush.com/blog/uploads/media/fe/68/fe684398acf5ef8c09c466be802f3d59/---fHS_g8D_Ld0f71hcaV4-0py8RJpEMb-hdZtlnyCluR0daCLVItxvHRPl7V49hwCCODn87prtgwuwPIbngMPeFuSM7gtMB8crpJGv2WmnoGYsWk_102wjpyUQANi8CpFJfCcPu85FB7uEQSEdbDSk.png)

Once you’re connected, your site should open in a new pop-up.

With the Tag Assistant in the lower right corner of your window.

![tag assistant connected](https://static.semrush.com/blog/uploads/media/7a/80/7a804c7a0594404d3d586d20d8e50a0a/y7VtzAfVn8tNSTUeNZEDMq8jZfU1_GICSqypyZaF3wCxa1hUnlNuesVgGmY7Pndp1z1fXpE4c3iWTbnDaU9X_7aX94A-l6KtOVNIy__hZZ2MNpogrHmQckq4u72vIlkMFvGRaMi6VPQBKxWLZAKI_MA.png)

Keep that window open and return to the preview page.

The preview page should say, “Connected!”

![Connected! page](https://static.semrush.com/blog/uploads/media/2e/dc/2edc0071ebfc84c35f206af14314504c/d04063dd9b8f529d60ab7d2e6dbd4c08/9stif8NKLn0HGMrEaCRHE0kyK8LnI2fay_FHVd2ip3I-5fPbcddKwoIZLuZB8VpB4fYB9_6XcuJ-nqibjOd9gnWsYfaJpBnIq1E98PdLlcOnlDwFxtbI350xul8kjNnKsxy6yi8-QH9ACdlPfd0Koqg.png)

After you hit “**Continue**,” start debugging your tags in the preview window.

![Google tags preview window](https://static.semrush.com/blog/uploads/media/92/46/92466605d6f3b70ae17587b435dfa6ea/d80c23dc7bbcc7f661a173dd44a15539/_FbEluVVsoWG09A-dj5Zuo5hGVMB8bGsibSjtfoOc2HT25ZDtYUWlVstLxmE9EwGkzI2WE4262iG2JcZT4CRhQig86QSi04xV80_LZfvLgfGbZGTJ2hWeB_xyVfgdDrEEW7-gh6MbZCRe2P3QdiMg0A.png)

You should see your newly created GA4 Configuration tag firing on each page as you navigate your website.

This means your tag implementation was successful.

When you’re done debugging, close the newly opened windows and go back to your page overview.

Then click “**Submit**” to submit your changes.

![submit changes button](https://static.semrush.com/blog/uploads/media/d3/87/d3878e41b130556be5c1476e33c5d6a5/Syo0HoDM6g7gR7hLvUWsvfAL2V_Q-m4ecmT2N4YbkwlPIgKLUsn7bo9v_BmAurVRAVrd_cBRozTbu9DbDoQ5WZL31T8Rxo0V8VNglYyzqPis4YE7KY7NMAQldbxQJrcnSfOMAbdZlb2ZgOd6VElvQo0.png)

Be sure to give your changes a descriptive “Version Name” and “Version Description.”

![Version name and description boxes](https://static.semrush.com/blog/uploads/media/31/e0/31e08a5a180e3044d4c44945b9b188a6/SwvoRhI12IVwqbXRF7sVxBdPPYu3-tIZpeUp0QLO-_JkR8uKazFHriL2joFx_Rwm4SYrYHB2UlgzpoJ9K7Xh6vC7JMUUQtaWsfJrpVd1_FooLgpmraMOw7ARylHBtt0the4PLDhQGcquLRYQNh5ZUcc.png)

Lastly, click “**Publish**” to push your changes to your live website and enable GA4.

This will [publish a new version of your container](https://support.google.com/tagmanager/answer/6107163?hl=en) to your website.

You should now see hits registering in the “Realtime” report of your GA4 property as you and other users navigate the website.

![Realtime overview](https://static.semrush.com/blog/uploads/media/43/76/437627aac85501ad40d849110b5a645c/5v0trcnJOLarylvDWKIRHQI18TrxFGLqRhReveBUN4PGs5Ecsd7_DNe4lHwTgU8Bpi2wqt2pjL3KwFWxuAn-Y8zbR7k39cEpmoMe7S9pqJk3MIFACw61h41-MUl5vP_Z38v6NdUONn5b-sJWaiRiyPs.png)

## Best GTM Extensions

Browser extensions help you get more out of Tag Manager.

The following extensions provide additional information on the tags that are firing (or not firing).

And any issues that arise with your implementations.

They also provide important details regarding your variables, triggers, and code snippets.

The following extensions are some of the best for facilitating your GTM efforts:

- [Tag Assistant](https://chrome.google.com/webstore/detail/tag-assistant-by-google/kejbdjndbnbjgmefkgdddjlbokphdefk)
- [GTM/GA Debugger](https://chrome.google.com/webstore/detail/gtmga-debug/ilnpmccnfdjdjjikgkefkcegefikecdc)
- [Dataslayer](https://chrome.google.com/webstore/detail/dataslayer/ikbablmmjldhamhcldjjigniffkkjgpo)
- [DataLayer Inspector+](https://chrome.google.com/webstore/detail/adswerve-datalayer-inspec/kmcbdogdandhihllalknlcjfpdjcleom)
- [Da Vinci Tools](https://chrome.google.com/webstore/detail/da-vinci-tools/pekljbkpgnpphbkgjbfgiiclemodfpen?hl=en)

## Track Even More Data

Google Tag Manager allows you to track almost any user behavior or interaction you can think of.

And GA4 comes with a lot of valuable user data right out of the box.

But simple page metrics and events can only tell you what happened.

[ImpactHero](https://www.semrush.com/impacthero/) goes beyond that and tells you **why** something happened.

And what you need to do to improve it.

![ImpactHero overview dashboard](https://static.semrush.com/blog/uploads/media/26/5c/265ccb57ebd3c4ed394b3fc6d88013b3/2bdc7ce4477a87829acf84b1c56e6d07/0kMu2RSIGODdxP1Cgwd2x_QNmNh5kALr_i5Ji6gLe_FmLKbETZtqAgfPdsyZnEtDhk4U92J9ZUP7lmuSSknoNvordxvlL9EYQ6OCfpad7SYrtToIBi2gYt5HE-AZg014d3UPtvdeQTWkepYmkIfFVW8.jpeg)

From customer journey mapping to content performance analysis, ImpactHero provides the marketing data you really need to be successful.
