---
title: "How to Create a Custom 404 Page in WordPress (+ Examples)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "custom-404-page-wordpress"
url: "https://www.semrush.com/blog/custom-404-page-wordpress/"
canonical: "https://www.semrush.com/blog/custom-404-page-wordpress/"
author: "Dana Nicole, Chris Hanna, Boris Mustapic"
published: "2024-04-29T15:25:00+00:00"
updated: "2024-04-29T15:25:00+00:00"
categories:
  - "General Marketing"
freshness_reasons:
  - "date_2024_watch"
  - "time_sensitive_title"
schema_genre: "General Marketing"
fetched_at: "2026-06-12T14:55:55+00:00"
status_code: 200
html_hash: "7d279eeadeb096a962ba49dfd46f25362d64be6690d813ffc2eac69ac8b35e06"
clean_word_count: 2410
clean_char_count: 19426
---
# How to Create a Custom 404 Page in WordPress (+ Examples)

404 pages show when users try to access resources that don’t exist.

Like a misspelled URL.

Or a page that was deleted.

And you can create a custom 404 page in WordPress (even if you can’t code).

## Why You Need a Custom 404 Page in WordPress

Custom [404 pages](https://www.semrush.com/blog/what-does-error-404-not-found-mean/) can improve the user experience by helping users find what they need.

And you can tailor your 404 page to reflect your brand. Through elements like personalized copy and imagery.

Take this default 404 page:

![Server error page with message "not found." The requested URL /example.html was not found on this server.](https://static.semrush.com/blog/uploads/media/b5/bb/b5bbb835db302350f1f573baa13fa589/3fb676c9f93bb6ca4dc9493274f08162/Y9NeEzJE-ZDBZCAwhHyhbP_hrZIbq4zMiGp6egEznwp0qjUjduZ5BRKKOs4-HFUZdBheZjrwiBM16uVNXOig776tU-zTtjipuAVKWzkd5RFY8vfQWt030u5Glna4NfVidLk1H2-pWys44wOFvOkLoEg.png)

This page is unhelpful. And doesn’t point users in the right direction through elements like useful links. Or a site search box.

This might cause people to leave your site and go elsewhere. Which can drive up [bounce rates](https://www.semrush.com/blog/bounce-rate/).

The solution?

Create a custom 404 page that reflects your brand. And helps users move through your site with ease.

## How to Create a Custom 404 Page in WordPress

Here are three methods to make your own 404 page in WordPress:

### Option 1: Theme File Editor

Many WordPress themes come with a premade 404 page.

However, if you’re not comfortable working in PHP—a scripting language—consider another option to build your 404 page. Like a [page builder](#option-2:-page-builder).

But if you do want to go this route, you can edit your premade 404 page using your theme file editor. WordPress’s theme file editor is a text editor that lets you edit files for your site’s theme.

To do this, log into your site. Click “**Appearance**” and “**Theme File Editor**.”

![WordPress Appearance menu showing the Theme File Editor.](https://static.semrush.com/blog/uploads/media/b3/f9/b3f95610e294cf8d1096197fe0989bae/8ca6e8b0d94357691ca1a53284a4bcec/OyHjvglQA7sWaU3OQcdK5CzNuHt48fVAOMwDk6vgvKijaTu73npXoBWRs-0o-C99cIqpzRuLTyc2eL2zboAbcmRThKbVBBpLaHt_4kPW9xgH2lStUxE5TtUbGxtCR8nemXCr9SeYZ4PK3lv-9UTxSyI.jpeg)

Your theme file editor contains a drop-down where you can select which theme you’d like to edit.

It also contains your theme’s files and a text box with each file’s code.

![WordPress theme file editor screen for the GeneratePress theme](https://static.semrush.com/blog/uploads/media/8a/c4/8ac4fa22fca8d97b5fc7200fb0f091b2/cc8b1c757603dcf19c8883e82fe68f08/l8xvIT_bXI07jJx85IkRjH1DoIek1xMe4F3Fp4qfNrXn3YU161nASXQWg2LYoS2BlIZMSbDOH7CJBQXut4JRh3jW2dYa1E1QkhQrTVvmX6izJJ-W1bDHM8lmpBYQfd5oJ4noxesEiCKm4s9P3Ici8oM.jpeg)

Changes you make through your child theme remain even when you update your parent theme. So, create a child theme to keep any changes to your 404 page.

You can use plugins like the [Child Theme Configurator](https://en-ca.wordpress.org/plugins/child-theme-configurator/) to create a child theme in a few clicks. Or follow [WordPress’s instructions](https://developer.wordpress.org/themes/advanced-topics/child-themes/) to create a child theme without a plugin.

Once you have a child theme, use an FTP client or your web host’s file manager to add files to your child theme.

The following tutorial will show you how to add files with your site’s file manager.

To start, log in to your host and locate your file manager.

![Web host file manager interface.](https://static.semrush.com/blog/uploads/media/e3/2f/e32fc3dc5bbf2e7c477ef6f1c7091b40/101a3fc2513910c0541fe44493024031/zRbWqnoXifTrCjI9yBwlgzGZgFKv9iUgqTMEB9WaqSIiUuKiAd4Dp-HJ_J1uBAGQr32IIlgwAuw3smNGWD0pv29HSKgD-6tnSy2CsUFY1NQioT8iHjJ7uGjIQEGoSowTKw5-oAtTYjRxvYMx4aSRirc.jpeg)

Find your 404 page file. It will likely be under your root folder (often named “/” or “public\_html”). Then go to “**wp-content**” > “**themes**” > “**your theme**.”

Our example has two 404 page files:

- A file named 404.php for the overall format of the 404 page
- A file named content-404.php that includes the content of the 404 page (like text and images)

![Web host file manager screen showing 404.php and content-404.php files.](https://static.semrush.com/blog/uploads/media/db/1b/db1b0f7bdd86b1113607e81075c9a206/10cf1b0f8f561a93da325e58d8271480/LbKToImEigSGUXspmyrqNq_baYF6srgNfXggoIMgQDYLLmKEDuP-wFTBNC7MVHwqM4dhWemrcDr9wpB1NySRBgNc4GVF60_X5-Xj4tLN6vft04X-1-wiOutdfDpZigB4B8jEoTH3nawWLqFqmkHrakM.jpeg)

For our example, we’ll make a copy of the content-404.php file. To edit the text and imagery for this page.

Double click this to open your 404 page file.

Then copy the contents into a plain text editor. Like a notepad app on your computer.

Next, click your child theme’s folder and create a new file within it. Name this file the same name as your 404 page (in our case, “content-404.php”).

Then, paste the code from your plain text editor into your new file, and click save.

![Web host file manager showing a child theme](https://static.semrush.com/blog/uploads/media/3a/f8/3af85eec4618f1acea3e5179b289250e/f9d1e3e5b764181e55118d6f2d5c1675/HEtFHs5Yxh-ZPygfCdDSjkTHds_P_wZMho_S_Ir5cFCDgVd_DxTYwMZwmel2oe2tpKKi9Rvwf8wRWe9ATNwyOK5SR8Ayapa8O0kYdiia2f4NPAhYij3VZN1C8dJ1UUg6rLyhxHNArKalIftOTMb1KuA.jpeg)

Next, edit the contents of your 404 page.

For example, we could change the highlighted text (below) to something that’s more aligned with our [brand voice](https://www.semrush.com/blog/how-to-define-your-tone-of-voice/).

![Web host file manager editor for child theme content-404.php file.](https://static.semrush.com/blog/uploads/media/65/5f/655fcfe817e9c9b9cf52042a5a85a509/08b5650ef84324a645495a2643d50406/luBhUwn2XKzFDu65xG_QGDZ62IjEHLgmanImq30XPPpzKkPwU2sQeyD94FFtM7CZGxLIMFP34HoaLjhsUfqltPotuyxjgULQqvXGq0xpn4tsODIe5OK2jcFqrmfKGb0lynbWeoi97l5d8TDlDLbeEEE.jpeg)

After saving your changes, your custom 404 page should now display when someone tries to access a page that doesn’t exist.

### Option 2: Page Builder

Page builders like [Elementor](https://elementor.com/), [Beaver Builder](https://www.wpbeaverbuilder.com/), and [Divi Builder](https://www.elegantthemes.com/gallery/divi/) are no-code solutions for building a custom 404 page.

While page builders often have free options, you may need to upgrade to the paid version to build a custom 404 page.

Here’s how to make a custom 404 page with Elementor.

First, install and activate [Elementor Pro](https://elementor.com/pro/).

Click “**Templates**” and “**Theme Builder**.”

![WordPress side menu showing option for Theme Builder.](https://static.semrush.com/blog/uploads/media/5e/48/5e488fd351a7fd7e43c75e57c7ab549e/5790699a09566551be8784bcb9ca497b/yacnnN7z3JZTFI5uPxL0NmN2fiqqFJNWhpFSmNkf79S1U-uC1L5dzOU6iiRXVs3ziNMwiJpSys9GYFLCZApp2WErC6jNI_Q0iKZRZbxuYI-HdpvQbl7pXfUmc9gIAtxThFLig2NXe0bjOvcv4C0N2YA.png)

Then click the “**Add new**” button.

A window will pop up. Select “**Error 404**” from the drop-down, and give your template a name. Click “**Create Template**.”

![Elementor Pro template creation screen showing the option to create a custom 404 page.](https://static.semrush.com/blog/uploads/media/72/e5/72e56c1468774e11ae307a9d1b21bc68/2d7aaab25d7d3d570220b973025f96c3/Fc043-ja4xVKQ72rZ70sdTW3KPV1ZhiBKiMvU1bCBx1QimbOut4jJA8X3_Y5JZsOPyuW3z8gx4FBBoPpoG39-J1z2c9yVjMssHOrAuZqTfMhQWFE8iCTwXYH92XZ1EycUGPew5Z8upQ7SuF2pi9BvbM.jpeg)

You can select from premade templates. Or design one from scratch.

![Elementor template library for 404 pages.](https://static.semrush.com/blog/uploads/media/22/63/226337986f10a86345fd4a2a424aa8d4/9f2c305d01a8f294f70d6424ca1874a0/iMj1CEsdMz6i0n9oTe9XvhAl2fFz9fyugjo-D0CC78EIIDvQeEe0L53aMRa93tRISOB9iD0dB-ntsDLlgTYuQWvuwG82oVAibHbDlV8LnwvthoGjwVW_3Zm1mJWR2au2MTaTShmINRWpt-f0-anouDU.jpeg)

Add elements like text, imagery, and a site search box to your 404 page. So your users can easily navigate elsewhere.

Publish your page when you’re ready. Make sure the “Include” drop-down says “**404 Page**.” Then click “**Save & Close**.”

![Elementor template publish screen for 404 page.](https://static.semrush.com/blog/uploads/media/2e/89/2e89b5c1e73e118718acfa1a7b859857/1307046eaf3d6532b2fdcc21a1c79f32/J1D8X3TLSW-nrWq7a4zq6C7LrXHe6SP__r8qgMWyZ4rUMwKuW-30Gj0JXxfP5JpK0-OWemp2XuPUoQzy5s2xvtRehfAZIRRzEvOimdOosVSrzmsr7I0MEZKFNrdRxXhy3t6rYiymLLPSE7K573koeto.jpeg)

Your custom 404 page will now display when someone lands on a URL that doesn’t exist.

### Option 3: 404 Page Plugin

Plugins are another option to create a custom WordPress 404 page without code.

Some plugins to consider are [404page](https://wordpress.org/plugins/404page/) (also listed as “Smart Custom 404”) and [Colorlib 404 Customizer](https://wordpress.org/plugins/colorlib-404-customizer/).

We’ll use the 404page plugin for our example.

Install and activate the plugin. Then create your 404 error page by clicking “**Pages**” > “**Add New Page**.”

![WordPress Pages side menu with the option to Add New Page.](https://static.semrush.com/blog/uploads/media/b3/ae/b3ae176901cc937b1a789a0165874e67/9772f3b1e56e6ed7b0b0c110bc828813/nHRXRiqx6C4kuuUbNuiQ_20h50KGv4Xst0bELg52rGkEwZmg05GYbUJ0OSwRh6V7OhV7-7sy_YroquHpnCdH4XCnjhUXMQBrmP5sBGpftHpFQthaQYilzpnkChBlxRo4uN-om7EUF9hF_G36srio058.png)

Make your page using your page builder. We’ve made the error page below with Gutenberg, WordPress’s native page builder.

Update the [URL slug](https://www.semrush.com/blog/what-is-a-url-slug/)—the last part of the URL—to something like “404.”

![WordPress Gutenberg editor for a custom 404 page.](https://static.semrush.com/blog/uploads/media/2f/d2/2fd2ff9156ed3a940e006fe96bb1cf4f/92b0374b0aaa54602cd3c79258a6f93c/jI2fcM6WNTsFEz9KcTGNaBSWzAQUjvR0P6LkL9ESCFad-EH05-AkcJv8-kZons17KQMQmw7VjjsNsjajEfjzp-UH_wCOVSDDIOprpdIzvMuUmGywuc_s7nnvjghxHwh38BlDOSzGMT1zl7kZmPvz07c.jpeg)

Publish your page. Then click “**Appearance**” and “**404 Error Page**.”

![WordPress Appearance menu showing the 404 Error Page option from the 404 page plugin.](https://static.semrush.com/blog/uploads/media/ea/e1/eae1b80cf09de909140aaf8fbdd19426/d852e1006134b570f70a19c879f3c1a8/3Zii-1p73U6djYZO2OplXLaHFeuXRr4TZrfjX993tRbYAoOy4U-jFTg--WQmDfQcHZynoLJJ2yiblvOY_SC4fgPLzs2McfebcVNYYcxiao_1NvgWka4loDpsRNDrtb0MC5_aw1HPvZE473_DYqDyI-Y.jpeg)

Head into the “**General**” tab and select your 404 page from the drop-down. Click “**Save Changes**.”

![404 page WordPress plugin settings interface.](https://static.semrush.com/blog/uploads/media/10/25/102516cf0314be3d37947b592825bcf0/aa0353dce462e8e979fcf226620936d3/a830SptYU_E17nqtSPKInuFa1ZJAddOsxV-1dB97yU7fDzMtmEFBFY3xjkDY_QeSvksADXTW8W6wLT67evbaIrO1dB3fKfzEDbYvmzTqHBaG4Qzjt6RnwjlchwnASft2OP6Hsi_cprvshfp0tNJW61s.jpeg)

Your website will now load your custom 404 page when someone navigates to a page that doesn’t exist.

## Custom 404 Page Examples

Here are four custom 404 error page examples to inspire your own:

### Netflix

Netflix tailors their 404 page to popular shows with an image in the background. Which helps them promote their product while directing users to their homepage.

![Netflix 404 page.](https://static.semrush.com/blog/uploads/media/45/df/45df140dc0909a405ac90961966ab2cf/1a6e8ef496581de100d4c9d15c0a2f3d/lwO9xjQpevrpujzb18vvx_ItCeE2H-_fwXMBVGruf3TcoSOZpw63djMlRn-IemkviHquprkwT3_tDRZIIQ-dYUDNNxHkMTnYOzTLVzui3rpANY2FuDGmlViJHZuHS6dqwkcvDSGfKZdDqoQ8qBEf_u8.jpeg)

### Wendy’s

Wendy’s includes a simple game on their 404 page. Which adds a bit of fun to a page that is otherwise frustrating to land on.

Plus, this 404 page has links directly below the game. To help users find what they need.

![Wendy's 404 page.](https://static.semrush.com/blog/uploads/media/34/1d/341d2a7c299fa84e986ecaa2d4861d94/b12f61ab3f9e6e5d89806eae8668218d/POlk4FHOh_EFX_fQBXvZgJSTk6ExR9mZBBHpwTUDVPdPQ8C9z8OjNLcrW0X3TqVKD--U3-C_hrFEG0fJX6pi2EfwRHowIxReusDrkkmFSkGb8T1OMW4MDyj7YNlFPNKFezH154Q8QfOP-TtRmu8FFAc.jpeg)

### Ryanair

Ryanair leans on their travel-based brand for their 404 page with a relevant image background. They also include links to help users continue along their journey.

![Ryanair 404 page.](https://static.semrush.com/blog/uploads/media/4c/4e/4c4e82fd30fbb8f945b9f696e0a8b710/860836969132cee40ab4a85f210e8aa5/mypVWQlmZ7gSYW_RLOzfrHk3aXG0Y1g4ur-pEGV2Xr7-ZP5O-YEBvGbdG-NcuOBa6Y-j-W5-ejyNxzHXcvxH9eqecy3QNI2wCOHCfiZBfyzF68hio5qWxhSIlemLGxVRAr2ko79go57lJbc0qfatIyc.jpeg)

### Cadbury

Cadbury includes links to their homepage on their 404 page, along with a playful, relevant “Oh, Crumbs!” message. And encourages users to reach out to let them know if they continue to encounter issues.

![Cadbury 404 page.](https://static.semrush.com/blog/uploads/media/4a/65/4a6578e7f0663f752455375fec00a73c/822eeb1ac9b23dee7dea8a173a2e9c7e/XZ_-Qo2hzSnMhY5wQPjSj0S1oRZTIuouh_3Btfdwh1_quujF6C4YHqIWmbQ4o9yjXkHixbkw71E3MGZRzl-TWDQymA69dDGd33hRm1VvSo65yeEXqIVtpXHkLKLdYmAIHjnuX1B43Igp7Mr7cZ5pYcE.jpeg)

## Best Practices for 404 Pages

These tips will help you craft up a great 404 page for your site. Improving the user experience and potentially reducing bounce rates.

### Explain What Happened

A quick explanation helps users understand why they got an error. So they can troubleshoot on their own.

For example, Microsoft's 404 page explains that the URL may be misspelled or the page no longer exists:

![Microsoft 404 page.](https://static.semrush.com/blog/uploads/media/8c/a9/8ca9718d7d332c68f1e4b7917a7510e3/ff0ae6dfd335840d36672493df97b507/PJ_2XBKS_YgyOQw5VKhSVD1CMPIV7XsUloN8o0zYeJx2CbhQfWPmfDOgOukWzLwivu1Bdkq0-A-J-QGMN80vgAo8Zy_U_Zymyz7b0Ud_2dcEj94tcP8JJF15u9lxOYIYnZeqZrP6Ll_BVQxd-5NL9nU.jpeg)

### Stay on Brand

Your 404 page shouldn’t feel disjointed from your website. So, inject your brand and personality into your 404 page.

Tripadvisor uses clever language that reflects their brand on their 404 page:

![Tripadvisor 404 page.](https://static.semrush.com/blog/uploads/media/86/d3/86d3aff092b89d28c42ea6865b08f862/e769b7fcf0cc006d981a350763a1e982/yGIOPd14lHZhitMT4oVDh3mX6xUlcKtcLz6g8Fk6H6uidojZ6Hm0kt3FuOIdfoT05qyQnOtxoCMi1zlKrOZuI3n0jA9jZQ3ASxzGZr56opZ8GSL8L7DsBt1OqyhxgSp1ZHczWoKfvpntutWOmn9W524.jpeg)

### Help Users Find What They Need

Keep users flowing through your site by adding elements like a search bar to your custom 404 page. Or links to popular pages. Or links to your top products.

This way, users can carry on with their journey.

Amazon includes a search bar and a link to their homepage within their 404 page (along with an image of one of many possible dogs):

![Amazon 404 page.](https://static.semrush.com/blog/uploads/media/fb/e3/fbe3359fdbc73e1de7b3a2692c3f25f4/20192b899c9d17205afaa84530c4164a/6I8Uj5QJ6g5hhWSPtCO_-pYBh8jcGg9Cs8WzIbinGYwnQLDuHi_9TsVHy_n56Xa2PZPJiVupbUOZK_3g4ud5ETS4Pk-BBq36mW_VtCnamhNn9YlnphuYDqApoANrKlTeCQGVFWrIkO4SS5cqayeKQcQ.jpeg)

## How to Check Your Website for 404 Errors

Use Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) to check—and monitor—your site for unwanted 404 errors.

Open Site Audit, enter your domain, and click “**Start Audit**.”

![Site Audit interface with “yourdomain.com” entered.](https://static.semrush.com/blog/uploads/media/06/d6/06d697ecd8cb1dd252f70f07f426ed55/367b671cb73e5ab16aa26031ac1a3782/XpQ44neK-h52k-1GATVloTeYrtsz7k5WxAxdlun5GY8LNzk5aXS6MjGLXnhYcIjRVNiN2FtjvnCdFwy9a_Ic1RjS843Iya3fZwJ4fWXYamo6cvPpPp8Wr41WTP0vA60QsOS_Hk0Icsp0Ts1FBw2L4LI.jpeg)

Configure the site audit. (Our [configuration guide](https://www.semrush.com/kb/539-configuring-site-audit) can help if you get stuck.) Click “**Start Site Audit**” when you’re ready.

![Site Audit settings configuration screen.](https://static.semrush.com/blog/uploads/media/63/28/6328a42a5fd4c390acd82e8c3ac81de3/a2a8203e3c402f356b652097d48d865b/KBcwhEk04ZvOwEsSv6SnhzUGU3rvApcwUdowIfM5S5akIEms1fK73IAuF0g2X8HbjiSEjHjfczg5cDn0gt0zMceT7qmuZQXIF4xGZf3XNajF2oecipDBXmEadIwtGA5qPslCX95ZMK3GvvGnnW_7XDw.jpeg)

You’ll then get a report outlining your site’s health along with an overview of issues, warnings, and notices.

Inside the report click “**Issues**.”

![Site Audit overview tab showing Site Health and the number of errors, warnings, and notices.](https://static.semrush.com/blog/uploads/media/0f/d1/0fd1108dc79b8d61a829dc4972e39216/4daec04b1742b737906eafb5a4832b98/LhXeIBrUiN4zwN28HDvUarTtJRd11ODP-hq8bWm7IsGrVZu-xQ57qXhboPrWgmh1bz_ElGBjqkJgfGOF1lm9-dfNi3n36jNzXY-Xw0-ocSPj_cPhLYAHM4J9XYqygpTv8GF2O0IrDY53vGeHjlIU6lI.jpeg)

Under “Errors” look for “# pages returned 4XX status code.” Click the “**# pages**” part to view which pages on your site show a 4XX error.

![Site Audit issues tab showing 84 pages return 4XX status codes.](https://static.semrush.com/blog/uploads/media/0c/f5/0cf54884b92ea342cdc3241d7681ee28/e7b72874af8331c3c37a2d31661285be/gkvd-TeJSIOwilTWZCo6yg6-V1I35q91N7ah__ZouM51xCtxIlAugCixh02Di_6tTD4mqncRwwpJPsk71yOfBMO5sYgH7yF0lK3oX8PeQTNpDL4CAo_xSs1a_b9Juc0bh07IJEbsWIrJ01RSmGpxkiI.jpeg)

Look for pages with a 404 error. Click “**View broken links**” to see which pages link to the page with the 404 error.

![Site Audit results for pages that returned 4XX status code.](https://static.semrush.com/blog/uploads/media/08/f3/08f3a124f1ec8d52f6db42d9f5a68e0b/dae90641251ddd1946dde87e952df388/kfL1gH4nTyo-yGhWfSrzeI_K5gYEQQNWrzq6nWfDekrCWh4PxjJQgfGZ5yLYt5pMWcZ4bjaeEJvBzysW6TXwNPFEbt60L2MyrYQyJOM6KXhW89Odqb3SFyM109atgt8GLzMv0w0wYj8nEWkdjwqhU0w.jpeg)

Remove or change these [broken links](https://www.semrush.com/blog/broken-link/) to another relevant (and working) link. So that people don’t end up on a 404 page when they click them. And so search engines don’t encounter potential [crawl errors](https://www.semrush.com/blog/site-crawler-errors/).

![Site Audit results for broken links and 404 errors.](https://static.semrush.com/blog/uploads/media/35/cf/35cf726b80bedf01864c65fe4c808703/18ee6abeb9ff3d7c81a9d88c420f687e/SEGhDx7wRbwVFBMhI1d9sDUI3p0f-ZsVhvDHh4FetMJg2T409_6aWWYu9rVS6aS8uh4r93nZEbF4BHi710fEfjP0Ex82-Dh8H2mSd23soIMo0rjx__4L9swLD1JGXr49Qv19UEK1gq_Px51ug57vQPA.jpeg)

Then, decide how you’d like to approach the page with the 404 error. You have two options:

### Leave the Error

404 errors can be useful. As they indicate that certain pages no longer exist. And you might want to communicate this to users.

For example, say you deleted a product page because you no longer sell that product. You’d want to leave the 404 error so users know the product’s page no longer exists.

### Redirect Traffic to a New Page

[Redirects](https://www.semrush.com/blog/redirects/)—like a 301 permanent redirect—can automatically send users from one page to another when they access a link. You might do this if you replaced a page with a new one. And you want to direct users from the old page to the new page.

Imagine you changed your about page from example.com/about to example.com/about-us. You’d likely want to redirect traffic from /about to /about-us. Because the page still exists, but it has moved. And so you wouldn't want to keep the 404 page.

## Improve Your Website Experience with a Custom 404 Page

Create a custom 404 page to help users find what they need without any roadblocks.

Then, use Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool to monitor your 404 errors. And ensure that users don’t get stuck while browsing your site.

Try Site Audit for free today.
