---
title: "What Is a 404 Error? How It Affects SEO & How to Fix It"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "404-error"
url: "https://www.semrush.com/blog/404-error/"
canonical: "https://www.semrush.com/blog/404-error/"
author: "Tan Siew Ann"
published: "2022-10-31T13:27:00+00:00"
updated: "2024-12-03T15:47:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T13:18:35+00:00"
status_code: 200
html_hash: "ab9cd55aabe6dcb1606068820cab9621aa15a8c7af9985e905c1d82004a69443"
clean_word_count: 3306
clean_char_count: 24501
---
# What Is a 404 Error? How It Affects SEO & How to Fix It

## What Is Error 404?

An HTTP error 404 happens when a web server can’t locate a resource, such as a webpage, at a specific URL.

This can occur if:

- **The user entered an incorrect page URL**, possibly due to a typo
- **The website owner deleted the resource**, so it’s no longer available on the server
- **The website owner changed the URL** linking to the resource
- **The website owner misconfigured the website**, preventing the server from finding the resource

Website owners tend to dread 404 errors.

Why?

Because 404 errors make it so users can’t access the page's content, even if they try.

However, 404 errors aren’t always negative. They can assist search engines in properly indexing and ranking your pages.

This article provides a detailed explanation of error 404 and its impacts. You’ll learn how to identify 404 errors on your website and methods to fix them if necessary.

## What Does a 404 Error Look Like?

A 404 error can appear in various forms.

Sometimes, the error page is very simple:

![Upflex's 404 error page that reads "Whoops" 404"](https://static.semrush.com/blog/uploads/media/59/0e/590e9580dfc734727b8941bc0d73a35b/14affa7790fb78874af1b67209b86800/AD_4nXcH_a9LwEie2HcNU4AV48JRiPH7JVQF1d7JW6cta89gRk2dXH6-DKotckkuIS0W5RTHYnjFtYELPHbb0CVTYocPQKo75qo_XTbs6Z8wA9QEsQGpvePekf63xTwwrUtokhH83E1CTA.png)

Other times, they are more intricate or even playful:

![ebay's 404 error page that reads "We looked everywhere. Looks like this page is missing. If you still need help, visit our help pages" with an image of a child with a jacket over it's head](https://static.semrush.com/blog/uploads/media/cd/05/cd057fae21ba634d3509a540d45d35b7/227975c6e9d5b6aea973d126a72059f3/AD_4nXcXHvD-kTo2eyKAGDXHf6xgWGP9uVP0DLIjQiR6BLMQsCuk24KObPSnxE_jkV4sw-xv2viUHv-XN-2-wo3TevZXpBdYbx5tllXJERdMdG_KgohkuUDC9-pucgQSVfXQS6VWMqWwCQ.png)

Here’s another example of a playful 404 error page:

![Amazon's 404 error page that reads "Sorry we couldn't find that page. Try searching or go to Amazon's home page." with an image of a dog](https://static.semrush.com/blog/uploads/media/e4/d2/e4d2091d44751187fb82c5225f0c416b/d3507ca2878481a6819b8e5fa1b51e78/AD_4nXcrHaMjEYIEylwTpK6TQm_AZ-5gEv2WUzKU6SmaFlDsGqDdqZZp6mghQD0eu5gK27Wb1dlC6wZTjTlotN3QBu74QA-PdnLzZomYYixyZI6CNaEBm51YQcZsyI5M7IEf7SVl506WYQ.png)

Common messages you might see on 404 error pages include:

- “The page you’re trying to access doesn’t exist”
- “This page has been moved or deleted”
- “The requested page URL can’t be found”

However, all 404 error pages share one thing: the [HTTP status code](https://www.semrush.com/blog/http-status-codes/) 404.

Every time you visit a website, HTTP status codes are exchanged.

When you type a URL or click a link, your browser sends a request to the site's server. The server responds with an HTTP status code that provides information about the page.

HTTP status codes are always three digits and fall into five categories:

![HTTP status codes categories](https://static.semrush.com/blog/uploads/media/c5/b9/c5b997b1fb18e08586296b9baee30f4e/edb00993f8eee39c02f9a3fe05844766/AD_4nXct-HmeHRDEtoTXYzpW00gYVSDmRV2cZ4RRxVCoeXyw9xD6nhPMdkuqEF0sKQohwqTalg7jQyp-1CqepOWoIVAH8GamQ96U3LN0Wq3sYvJgYTzM3ouXLCwFM0H0ddLtH8Fl5VbpKg.png)

The "404" status code indicates that the resource at that URL is "not found."

When a browser tries to load content from a URL where the content doesn't exist, it receives the "404" HTTP status code from the server.

You can check any URL's HTTP status code using an HTTP status checker tool like [httpstatus.io](https://httpstatus.io/).

To use the tool, open it and paste a URL into the text field. Then click "**Check status**."

![Paste an URL into the httpstatus.io tool](https://static.semrush.com/blog/uploads/media/99/cb/99cbdcd474f786c5b2791b2dba5afad5/b9f8161c4071ab1accb0d67c67543887/AD_4nXfxVD5z4Tsu_KHVk74GG3ZgRYy8GTJDy38275LhWI9VpI9p5yW_wm825U3GUTYprbtsVxX3lZOwY-uLPn6omJL2t7nnaibctPz3Z8YAl9d2Za6tGfXz3Uy9Ds9ojimLtJv7ada89Q.png)

The tool will display the URL's status code.

![httpstatus.io showing "404" status code for the pasted URL](https://static.semrush.com/blog/uploads/media/e8/1e/e81e8dd4150ca7216faa64bda9ed131e/8e0449b9ffbb3937cea92da041d722ea/AD_4nXcQ4Oku3uepzAnRGj97FIKpHqaHJdlJgF13j876GnMF3AikiymrZmPW7XAYX-SQqob4XXSgwUiAr5Yw_bYwdJgvSTWnpev6mjhNTfvOGib7UZsv9923V4XLWGrDWKSkoqjuFRk0kg.png)

## ‘Hard’ vs. ‘Soft’ 404 Errors

A hard 404 error occurs when a page is completely unavailable, and the server correctly responds with a 404 HTTP status code.

This response informs both users and search engines that the page doesn’t exist, ensuring that search engines don’t waste resources attempting to crawl or index it.

When search engines encounter hard 404 errors, they usually remove these pages from their indexes.

In contrast, a soft 404 error happens when a page appears to load successfully and returns a 200 status code, but its content signals to search engines that it’s essentially unavailable.

This often occurs when an error message or placeholder page is displayed without the correct 404 status code.

For example, a page labeled "Page not found" with little or no content may confuse search engines into treating it as a low-value page rather than removing it from the index.

Both hard and soft 404 errors can negatively impact SEO.

## Impacts of 404 Errors

404 errors on your pages can lead to several consequences, especially if these pages [shouldn’t have 404 errors](https://www.semrush.com/blog/what-does-error-404-not-found-mean/#do-your-website%E2%80%99s-404-errors-need-fixing).

### 1. Poor User Experience

404 errors can harm your visitors' user experience by preventing them from accessing the pages they want to see.

Let’s say you’re reading a TIME Magazine article on the best diet advice. You decide to click on the linked text: "Read about environmentally friendly food."

![“Read about environmentally friendly food" link highlighted in the TIME Magazine article from above](https://static.semrush.com/blog/uploads/media/52/34/5234f0fbfea06bc64e1c9add700504da/2c7a3ea1aeeda5b9b06ff393e04ac7af/AD_4nXftZ6dUYHpFf_8VZto6gEB4WdHFPY0vs6-V9N0HDkkndRNVnYnytqx0nZgNkutu5TNfHEh2TUEcWkgnIJXer0orSECjfam-LJsbQRI5Jr2U_5ZycA0zUHRwPFuzu9NzNTWvq_dxoA.png)

But the link directs you to a 404 error page:

!["Sorry, you've reached a page that doesn't exist." message on TIME Magazine](https://static.semrush.com/blog/uploads/media/99/b1/99b1ddf97ec0bb150953240f53208d01/08cb22f83c1b81bbc33ca968880e86ca/AD_4nXetwQhQKqnII9q9o8vuUvCSUUc0ekPsJmoD06OcE06OpKDYATNVF6p1F3tkPuRMLjNC-UR1ydUsgTr7IoisQRFpQ9NmXbS7MOpOHYTmz_85MIe2s5mI3J-vdiZJAZKGhW1v-53ulg.png)

This error stops you from learning more about environmentally friendly food.

You have two options:

- **Spend extra time searching for information on environmentally friendly food elsewhere**, which is inconvenient compared to the expected experience when clicking the link.
- **Choose not to learn about environmentally friendly food** at this time, which is disappointing since the article sparked your interest.

In either case, it results in a negative user experience.

Your perception of the brand and your motivation to revisit the site likely did not improve because of this experience.

### 2. Search Engines Being Unable to Rank Your Page

For a page to rank on [search engine results pages](https://www.semrush.com/blog/serp/) (SERPs), search engines must first [index](https://www.semrush.com/blog/what-are-crawlability-and-indexability-of-a-website/) it by adding it to their search database.

![A graphic showing how search engines work](https://static.semrush.com/blog/uploads/media/8c/6c/8c6c675be913e26958a108b169b44950/eb2c0b12ea3806e3b8f27e58cb1a836a/AD_4nXckxQdVbci9OKcpTmb0IsVMf7VmcCmoVTz6pvRYlltIsWD4pQI7ckxUaSEujLwh5POqoVayMkj_SkIpOT0VCwVTWYWjMEuLxv7jVmgXlWJ5cBAZx8XtaGllLAW4YZjzzUUynfdu.png)

If a search engine encounters a 404 error while crawling a page, it recognizes that the page doesn’t exist.

As a result, the search engine won’t index or rank that page.

This means users can’t discover that page through search engine searches.

### 3. Reduced SERP Presence

Pages on your website with 404 errors can limit your site's overall visibility on SERPs.

Since search engines don’t rank pages with 404 errors, a website with such pages will have fewer pages eligible to appear on SERPs.

Additionally, any backlinks to pages with 404 errors become ineffective, providing less benefit to your website's authority. This makes your site appear less authoritative to search engines, potentially lowering its SERP rankings.

This reduced SERP presence may lead to decreased organic traffic to your website.

## How to Identify 404 Errors on Your Website

You could find 404 errors on your website by manually clicking each link to see if it leads to a "page not found" error message.

However, this method is tedious and time-consuming. Manually differentiating between "hard" and "soft" 404 errors can also be difficult.

Instead, try these methods for scanning your website for 404 errors at scale:

### 1. Use Semrush Site Audit Tool

Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool can detect over 140 technical website issues, including 404 errors. It also suggests solutions for fixing these issues.

Launch the tool, enter your domain, and click "**Start Audit**." Then, follow the prompts to set up your new project.

![Site Audit tool search bar](https://static.semrush.com/blog/uploads/media/0b/6a/0b6a202499097b059c94abcde1515f47/6740eef4f0ac8c05627d696d1abcd1ca/AD_4nXfkbcwW5Feko4GtsxwD4mrcMclnfevU3y_R2o1KQ68zyOZbf228fImesT0oKiq1jD5ta7hfkzllec92hBh8zuRhdHQuLjyM2sLoXv5s_s17L6ctfCyKDaX8I7DYu7fY4HQ4iM1zOA.png)

Site Audit will begin checking your website for issues and generate an "**Overview**" report.

Click the report's "**Issues**" tab.

![Site Audit overview dashboard with the "Issues" tab highlighted in the upper part of the tool](https://static.semrush.com/blog/uploads/media/9c/fb/9cfbaaf1c2ae93cdbc43cf404827f11e/365db48ff195d38be880a0bf0f8f5289/AD_4nXfd4cw0o9SrsXp97zpRfc8iMakt85O__NXlyZu9xHgNxW_YDsaOPH1oiQYsrmVW92oQeP_6B6ks4C-y82yja_MCeivSQuqH0OtxNASx44cHzve1pxibzMc1oQ9giVu6hKZr-qqyaw.png)

If Site Audit finds 404 errors on your website, you’ll see them under the "Errors" section. Look for a row that says "**# pages** returned 4XX status code."

![“57 pages returned 4XX status code" error highlighted under the "Errors" list in Site Audit tool](https://static.semrush.com/blog/uploads/media/e7/47/e747bd0d41620d919faa521532593620/64e8546c6b1a29fc0de62f3721842c99/AD_4nXdJI5XXNAto67SMwi6TTzFGXdv8ZTy5W5etDdhodCvIJEEKoiK3xdRXw3eYca7bsZF9RpbXKpjYDD59edpNTvVqJLRDkTiv2b3VopYty4mKOvn7TL5FGWTo-XBaw-KMW_mF4ad0NA.png)

Click this hyperlinked text to view a list of page URLs that returned a 4XX status code, such as a 404, 410, or 403 error.

![A list of page URLs that have returned a 4XX status code errors](https://static.semrush.com/blog/uploads/media/07/17/07171e95f3d2362ac6c61753a87ac93a/1f66b144d4f39d40a1f6a4de1c306dc4/AD_4nXe8OoZwENOICWPW7-RQrH1hrYQSOBWy9ebQByYber_NjxDGCHzuTBRzOvHXSz5AsJ7UF82OiNiGNZGt1cYbSVtbbnGonPd5ZJZdafOvHRnUPzr4N7q6z77O0T5ac-QDNCEHcWYSjA.png)

To sort the page URLs by their HTTP status codes in ascending order, click the arrows next to the "HTTP Code" heading twice.

![“HTTP Code” column highlighted in the list](https://static.semrush.com/blog/uploads/media/c5/ef/c5ef6529deb22d76ddd0cc9fc9ebee40/dfe0fd0e1cafc23f1a1b1a30963a13d6/AD_4nXcSjZ9UGhtIRf_IH596h19WO3tmkC04F6NBd-qYMSEKgqIGLqhwDZ7ZnsFibsLoCLp4shHe1BswM52lMok49C4g0Nle08juXsxWGUbIg0zeHUW6KorpIjWBvBR8yef_laY4SBTk.png)

This groups all page URLs leading to 404 errors together for easy reference.

![A list of all page URLs leading to 404 errors](https://static.semrush.com/blog/uploads/media/1b/a7/1ba73839e5f87bcb7bc777b7918ebadf/eefdaaf72c26da2c9846fe5a16089da4/AD_4nXeX3I3vlyeVOYCCnUTA23Vt5cPCCCb9fwky-305xqppXrTVjA9zeQnqjYkiBWafl9-mLBgamjQNO3YbWrp-B6fiIh0u3ThaxC5RyTabayBKzdN8x4quz-H2-smOTZno7wc2DWkipg.png)

Next to any page URL leading to a 404 error, click “**(View broken links)**”:

![“(View broken links)” highlighted next to a page URL leading to a 404 error from the list](https://static.semrush.com/blog/uploads/media/a0/10/a010e5cde289062419efdfc45e316fae/82c7c851cc6e6eb735f8a01bc2266656/AD_4nXfRLhV1oypvpY3vqxojs8kir3KoK0ThHqeVjxTK5TEMeRL6LNmtsmtBm4rdwxNI4vxFh5YwdjVoalJmZAN5yQrFnc-11-F-8QrzmuajRoYiID0JzOCabPpT9u3966-uUMarVavdcQ.png)

This shows you a list of pages that have included the broken URL in their content.

![A list of pages that have included a broken URL in their content](https://static.semrush.com/blog/uploads/media/c2/8b/c28b3e4ce92feea50ae482258427821a/0efbc80452137eeb86220d812bfdf64c/AD_4nXe34ZWTyNVZdXrkTTGL3RLLtIi0VGAZ4pCX88IynpSwnavL3rHYrtDN9e_xaf5awGlS93g1tE4KBjiOEa02Et-MVei8ByRGJKMKZIoDKaPlp9Z1z6wbWQWFr7sRFliVRKZfD89xcA.png)

From here, you can [fix these URLs](https://www.semrush.com/blog/what-does-error-404-not-found-mean/#how-to-fix-your-website%E2%80%99s-404-errors) to prevent users from encountering 404 errors.

To set up regular, automatic auditing, click the gear icon at the top of the report. Then select "**Schedule: Weekly, Every Friday**" under "Site Audit settings" to have Site Audit regularly scan your website for 404 errors.

!["Schedule: Weekly, Every Friday" selected under "Site Audit settings" drop-down menu](https://static.semrush.com/blog/uploads/media/93/e2/93e20c43cf0bd68b0e0b061301bc4302/b54774d097b9db7377e6cea4fa54ab41/AD_4nXfs4Rq59e2SV6I3Jynn4X4C9mtwDnHEVDBeH0k2-F6BGk2YBCY6Ea9CfPEuPnquewPqwhilVK6y3Lp_NS4-Uu9I_HafB0QrLQRTab_mnZmSD0etOc2U_W4a25EV6r7O4eOZ2I5C.png)

### 2. Use the Dead Link Checker Tool

[Dead Link Checker](https://www.deadlinkchecker.com/) scans your website for dead or [broken links](https://www.semrush.com/blog/broken-link/)—links that fail to bring the user to the intended destination, possibly due to a 404 error.

The free version can check up to 2,000 links at once.

To use it:

- Open Dead Link Checker in your browser
- Enter your website domain into the text box
- Ensure the "Whole Website" setting is enabled
- Click "**Check**”

![Add your website domain to the Dead Link Checker tool](https://static.semrush.com/blog/uploads/media/fe/4c/fe4c0eaf9410b7290d466892cf04242c/774fc3b6403e49c359df4b47203a8678/AD_4nXdbxwzkHPzuytnUu3_8-tPArlfqb0dBwQoO50eEf0Ppy7pPRlZU2G6BLet5ifZMkBNUHYZUirt4XmyXpiyA8-5U5AiXu3C_KlIbEOLDxo6VwbyeJZzEDcStw2Zcso8gj5-2QtY7.png)

Fill out the provided security code:

![Security code pop-up in Dead Link Checker tool](https://static.semrush.com/blog/uploads/media/08/b3/08b363e55152e6d33374fedd8c2b993f/f8c904d7e3b990914cc6e3e3fab101a6/AD_4nXex7PrUgEleHYSVtq_oFk5gk4SnX3LKuV2uyvfsBRc41KcNBPFhVto-XLOH_Vkr645TC-D0aNZ6V9uQtHbp9ADcykF8YCCd5EA2rC2lV0YcZyNujREGyr4zc8EXAoj5D78-ZSDejQ.png)

Press "**Enter**" or "**Return**" on your keyboard to start the scan.

For each broken URL found, the tool displays:

- **The URL's status** (e.g., "404 Not Found" for URLs with 404 errors)
- **The URL that returned an error**
- **The URL's source link text** ([anchor text](https://www.semrush.com/blog/anchor-text/)). Clicking the source link text opens the page containing the broken URL in a new browser tab, allowing you to locate and fix the broken URL.

![A list of broken URLs the Dead Link Checker tool found](https://static.semrush.com/blog/uploads/media/ba/1c/ba1c27951aa3ca06929849ac89f677f8/c76cab16af3e9619266b567c212fb336/AD_4nXcLK8sqkugtgA7A7GnqT9Osc3ecsBQsJKiatVLFt2wnPyVI5wy1vYC0zq46okxH9vfx1-9LEkOcrqWzU_AhbE8sssGnM4yv_kpegOtCynCBWqIh4EYT9tM2cyoz4F1t9at-TZbxOw.png)

### 3. Check Google Search Console

[Google Search Console](https://search.google.com/search-console/about) (GSC) provides reports on your website's performance on Google's search results, including a page indexing report that displays URLs with "hard" and "soft" 404 errors.

If you haven't set up GSC for your website, you can follow the instructions in [this GSC guide](https://www.semrush.com/blog/google-search-console/).

To access GSC's page indexing report:

- Open GSC
- Select your website property from the drop-down menu at the top left
- Click "**Pages**" under the "Indexing" tab in the left sidebar

![Property selection drop-down highlighted and "Pages" selected under "Indexing" tab in GSC sidebar](https://static.semrush.com/blog/uploads/media/5c/ff/5cff14287628f94b7f6029e91753004d/cc2d463a7eacb6f6c83991b25482cdca/AD_4nXc0q2o5UYSFmM28PTCvdpYgHM57hLSMkBAe2D2so2gRTNRb3L12mdkD1fG7jWxyG3lmdbZJUH-JH77rgtI_1RaTt5eoJpjlY91H4XWwNmTPvw_Hr6z3zsn8Wpyz3RsXfUZvzebxIg.png)

The "Page indexing" report will load. Scroll to the "Why pages aren't indexed" section.

If Google has detected 404 errors, you’ll see a "Not found (404)" row.

![“Why pages aren’t indexed” section of the "Page Indexing" report](https://static.semrush.com/blog/uploads/media/31/f5/31f5b017c24a3d5f259326d313ffd278/4cfc72205316697c37e33d4ecc4c573f/AD_4nXcOGRWSovs4oWPTV9M07vX4Ys1iQKiD6EtYHdG9tjOM8EiSQoBQYsmWzH_IVen2qGLb5AFpfuoMtom1uYmGmQVtLnD_7QQ-u9_pZt781Tm8PGXOM89LpNeJdRlp0Ma8C73uDq5IyA.png)

If Google has detected "soft" 404 errors, there will be a "Soft 404" row.

Click either row to view the corresponding report.

Scroll down to see examples of URLs that return "hard" or "soft" 404 errors.

![A list of that return “hard” or “soft” 404 errors in GSC](https://static.semrush.com/blog/uploads/media/d9/f4/d9f4ad9ef7825d195c821379123b532a/33cc3673398eaa85475b2c567081531d/AD_4nXcCbsqSjkd9oftALvTC963b5afXBIYd59OBMP2fowJwIM9DPdBFL6iisxSdD8tWJGdZqqn0CfflJ1N2854eFVMvEuS7LExoeyfMIIKJNg3lmk43UUzoPvSxsAqTIUNlyaku21f3Lg.png)

The list of URLs in GSC's page indexing reports isn’t exhaustive because:

- The report is based on Google’s last [crawl](https://www.semrush.com/blog/website-crawler/) of your website; new errors may have appeared since then
- The report can display only up to 1,000 URLs at once

## Do Your Website’s 404 Errors Need Fixing?

Not all 404 errors need fixing.

If you delete pages from your website and don’t want users to access them, their URLs should return 404 errors. This tells search engines not to index or rank their content.

If you want to display and drive traffic to pages that currently return 404 errors, then you need to fix them.

## How to Fix Your Website’s 404 Errors

Even if Google detects a "404 not found" error on a page, it will continue to crawl the page—though less frequently over time and possibly stopping altogether.

There are five methods to fix unwanted 404 errors on your pages before Google's next crawl.

The diagram below shows which method might be most appropriate for any particular 404 error situation:

![How to fix 404 errors on your website guide](https://static.semrush.com/blog/uploads/media/1c/e7/1ce760308a5f335dc4a7fa0aca152337/6520fb95a2656be1c62887f71940d35e/AD_4nXf-5rvohpAKmJPct1TpkzKfTjophuRR_auIedmqcbZGw8Clz_iOQyrcVvO6NY2IhCeqrntj-mNMRA9fVrx5ke47ErrqsP7ERhVOwBAczFXzkZtEs_Tw6AdUHHl_Xc2ffJVtHlZnxg.png)

### 1. Correct the Link Causing the 404 Error

If a link on your website leads to a 404 error due to a typo, edit the link so it directs users to the correct page.

For example, if the incorrect link is “https://example.com/blog/hello-**wold**” but it should be “https://example.com/blog/hello-**world**,” fix the 404 error by correcting the link to “https://example.com/blog/hello-**world**.”

### 2. Redirect the 404 Error-Causing URL

Set up a redirect that automatically takes users to the correct page to prevent users from landing on a page where content doesn’t exist.

This solution is ideal if you’ve moved a page's content from its original URL to a different one. A redirect sends users to the new page location without requiring updates to all instances of the link on your website.

Let’s say you originally published a guide to owning a cat at “https://example.com/owning-a-cat.”

Later, you write guides for other types of pets and decide to organize all guides under the [subdirectory](https://www.semrush.com/blog/subdomain-vs-subdirectory/) “https://example.com/guides/.”

You change the URL for your cat guide to “https://example.com/guides/owning-a-cat” and set up a redirect from “https://example.com/owning-a-cat” to “https://example.com/guides/owning-a-cat.”

Now, users who visit “https://example.com/owning-a-cat” won’t see a 404 error. Instead, they’ll automatically reach your guide at “https://example.com/guides/owning-a-cat” without any extra effort.

![A redirect from “https://example.com/owning-a-cat” to “https://example.com/guides/owning-a-cat" page](https://static.semrush.com/blog/uploads/media/78/96/7896a9708e9cfdb65efc93a24241f27a/5a50f48aa072e18583c2a75252f7948a/AD_4nXfSpJfaaZPJKGj1Fh3_2dOrJHMzYKWlI_CPSRMWGRUcgZANMP2cLzQzr3P5TQoYL7C0zMg-cbsCxuq-cs_PzdK0UiNkvjPCIpxtKYInXXG-aiRW7gM9x3EW8eAKlVIo2y9j1Du0.png)

There are various types of redirects. If you intend to permanently redirect users from one URL to another, set up a [301 redirect](https://www.semrush.com/blog/301-redirects/).

***Further reading:***[*Redirects: What They Are & How to Use Them*](https://www.semrush.com/blog/redirects/#how-to-implement-redirects)

### 3. Add Content to the Page with a 404 Error

If you want users to access a URL that currently leads to a 404 error, add content to the page.

Once the page has content, the 404 error will disappear because the server can now locate resources at that URL.

You can populate the page by restoring backup content or creating new content.

### 4. Remove the 404 Error-Causing URL from Your Website (and Redirect It)

If you no longer need a URL that causes a 404 error, remove it from your website. This prevents users from clicking the URL and encountering a 404 error.

If you used Semrush [Site Audit](https://www.semrush.com/siteaudit/) to [identify 404 errors](https://www.semrush.com/blog/what-does-error-404-not-found-mean/#1--use-semrush-site-audit), clicking "(View broken links)" next to a broken URL will reveal the pages that include return 404 errors.

![A list of 404 errors in Site Audit tool](https://static.semrush.com/blog/uploads/media/0a/cf/0acf867272fe6514dbf02c5ca42d31ea/6c008ef51ab1756ca85e1a6ed8d93bef/AD_4nXcAHlO_6TsqD6BdfO6vlu966ZozcrFptO5yaF2onlp1ppVnFZhZtzDiYvlk8iOYavh8AHEOA31XFwqwf7msxWa2vIb97BE8f975S3BQPjPLknjNzmZ0Qx_YjnmcT-i_NpF-ppTh0A.png)

Edit these pages to remove links to URLs that cause 404 errors.

Afterward, [set up an appropriate redirect](https://www.semrush.com/blog/what-does-error-404-not-found-mean/#2--redirect-the-404-error-causing-url) for each URL you removed. This ensures that users who attempt to visit the URL from bookmarks or external links are redirected appropriately.

### 5. Restore a Clean .htaccess File

The [.htaccess file](https://www.semrush.com/blog/htaccess-file/) contains rules that configure websites hosted on Apache web servers.

If this file is corrupted or its rules are formatted incorrectly, your website may not load properly, causing 404 errors when users try to visit specific pages.

To fix this issue, replace the corrupted .htaccess file with a clean version.

You can generate a clean .htaccess file using a tool like [.htaccess Generator](https://www.htaccessredirect.net/). Then, edit your existing .htaccess file to replace its contents with the new clean version.

The exact steps depend on your hosting platform. Here are guides for editing an .htaccess file on various popular hosting platforms:

- [Bluehost](https://www.bluehost.com/help/article/htaccess-tutorial#edit-htaccess)
- [HostGator](https://www.hostgator.com/help/article/how-to-edit-your-htaccess-file)
- [Hostwinds](https://www.hostwinds.com/tutorials/creating-editing-htaccess-file)
- [InMotion Hosting](https://www.inmotionhosting.com/support/edu/wordpress/reset-the-htaccess-file-to-troubleshoot-wordpress-php-errors/)

Your hosting platform's customer support team can assist if you need help editing your .htaccess file.

## Check Your Website for Error 404s Regularly

Having pages with error 404 on your website isn’t necessarily bad. However, you should be aware of which pages have 404 errors.

By knowing this, you can fix unwanted 404 errors that harm user experience or inadvertently reduce organic traffic to your site.

Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool effortlessly detects 404 errors on websites of all sizes. Sign up for a free Semrush trial to put the tool to work on your website today.
