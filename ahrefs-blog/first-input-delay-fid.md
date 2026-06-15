---
title: "Improving First Input Delay (FID): Tips For Faster Interactions"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "first-input-delay-fid"
url: "https://ahrefs.com/blog/first-input-delay-fid/"
canonical: "https://ahrefs.com/blog/first-input-delay-fid/"
author: "Patrick Stox"
published: "2023-06-15T05:04:57+00:00"
updated: "2025-01-22T23:30:07+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
fetched_at: "2026-06-12T11:31:27+00:00"
status_code: 200
html_hash: "ece54ae8935e8580c509efde512f2f0f74a1f07560e22f6198c49c1e5003a389"
clean_word_count: 1746
clean_char_count: 10148
---
# Improving First Input Delay (FID): Tips For Faster Interactions

First Input Delay (FID) is the time from when a user first interacts with your page to when the page responds. It measures responsiveness and used to be one of the three Core Web Vitals metrics Google uses to measure page experience. FID has been replaced by Interaction to Next Paint (INP) as of March 12th, 2024.

Example interactions include:

- Clicking on a link or button.
- Inputting text into a blank field.
- Selecting a drop-down menu.
- Clicking a checkbox.

Some events like scrolling or zooming are not counted.

Let’s look at how fast your FID should be and how to improve it.

## What’s a good FID value?

A good FID value is less than 100 ms and should be based on Chrome User Experience Report (CrUX) data. This is data from actual users of Chrome who are on your site and have opted in to sharing this information. You need 75% of interactions to respond in less than 100 ms.

Your page may be classified into one of the following buckets:

- Good: <=100 ms
- Needs improvement: >100 ms and <=300 ms
- Poor: >300 ms

![FID thresholds for good, needs improvement, and poor](https://ahrefs.com/blog/wp-content/uploads/2023/06/fid-1.png)

### FID data

95.3% of sites are in the good FID bucket as of April 2023. This is averaged across the site. As we mentioned, you need 75% of interactions to respond in less than 100 ms to show as good here.

The majority of pages on most sites pass the CWV check for FID. I don’t believe this is really the best method to measure responsiveness, and Google replaced FID with Interaction to Next Paint (INP) in March 2024. Instead of looking at only the first input, INP looks at the latency of all the interactions a user makes.

When we ran a [study on Core Web Vitals](https://ahrefs.com/blog/core-web-vitals-study/), we found that almost no one needs to worry about FID on desktop connections, and very few need to worry about it on mobile.

Few sites need to worry about FID, even on slower connections, as most of their pages are passing.

Our page-level data from the study told the same story. FID doesn’t seem to be a concern for most pages.

## How to measure FID

The only FID number that matters comes from the [Chrome User Experience Report (CrUX)](https://developer.chrome.com/docs/crux/), which is data from real users of Chrome who choose to share their data.

This is called field data and gives you the best idea of real-world FID performance across different network conditions, devices, caching, etc. It’s also what you’ll actually be measured on by Google for [Core Web Vitals](https://ahrefs.com/blog/core-web-vitals/).

For consistent, repeatable tests, there’s also lab data, which tests with the same conditions. FID isn’t available in lab tests because the testing tools don’t click anything. However, you can use Total Blocking Time (TBT) as an alternative metric. By improving the processes that are blocked, you will also be improving your FID.

### Measuring FID for a single URL

[Pagespeed Insights](https://ahrefs.com/blog/pagespeed-insights/) pulls page-level field data that you can’t otherwise query in the CrUX dataset. It also gives you origin data so you can compare page performance to the entire site and runs lab tests based on Google [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) to give you TBT.

### Measuring FID for many URLs or an entire site

You can get CrUX data in Google Search Console that is bucketed into the categories of good, needs improvement, and poor.

Clicking into one of the issues gives you a breakdown of page groups that are impacted. The groups are pages with similar values that likely use the same template. You make the changes once in the template, and that will be fixed across the pages in the group.

If you want both lab data and field data at scale, the only way to get that is through the PageSpeed Insights API. You can connect to it easily with Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) and get reports detailing your performance. This is free for verified sites with an [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) (AWT) account.

#### Check your CWVs including FID for Free with Site Audit

Note that the Core Web Vitals data shown will be determined by the user-agent you select for your crawl during the setup. If you crawl from mobile, you’ll get mobile CWV values from the API.

### Free tool: Check CWVs and Lighthouse metrics for desktop and mobile for up to 10 pages or websites

Here’s another free tool that you can use to check up to 10 pages or websites at once to see how you compare to your competitors.

**Setup:**

- Enter your Google PageSpeed Insights API key into the designated input field. (Learn how to generate an API key [here](https://developers.google.com/speed/docs/insights/v5/get-started).)
- Add the URLs you want to analyze (one per line).

**Run the Analysis:**

- Click on the **“Check CWV”** button to start fetching metrics. A progress indicator will show the status of the requests.

**View Results:**

- The results are displayed in neatly categorized scorecards:
  - **Desktop CWV for the Page**
  - **Desktop CWV for the Origin**
  - **Desktop Lighthouse**
  - **Mobile CWV for the Page**
  - **Mobile CWV for the Origin**
  - **Mobile Lighthouse**
- Each metric is color-coded to show performance:
  - **Green:** Good
  - **Yellow:** Needs Improvement
  - **Red:** Poor

#### Core Web Vitals Bulk Checker

This is an example output to show you how the speed scorecards look. You can use it as a standalone tool: [website speed test](https://ahrefs.com/blog/bulk-pagespeed-insights-website-speed-test/).

## What causes the delay?

JavaScript competing for the main thread. There’s just one main thread, and JavaScript competes to run tasks on it.

JavaScript has to take turns to run on the main thread. It’s like a one-burner stove where you have to cook one item at a time, but you have multiple dishes to cook.

While a task is running, a page can’t respond to user input. This is the delay that is felt. The longer the task, the longer the delay experienced by the user.

Source: [web.dev](https://web.dev/vitals/).

The breaks between tasks are the opportunities that the page has to switch to the user input task and respond to what they wanted to do. This is worse on slower devices, as JavaScript can take longer to process and cause longer delays.

## How to improve FID

In PageSpeed Insights, you’ll see a TBT tab that has issues related to the main thread being blocked. These are the issues you’ll want to solve in order to improve FID.

Most pages pass FID checks. However, if you need to work on FID, there are just a few items you can work on:

### 1. Reduce the amount of JavaScript

If you can reduce the amount of JavaScript running, do that first. Focus on the JavaScript early on in the page load. If there hasn’t been a lot of optimization done, the early part of the load process can be filled with a ton of JavaScript all trying to run on that single main thread.

### 2. Load JavaScript later if possible

Any JavaScript you don’t need immediately should be loaded later. There are two main ways to do that—defer and async attributes. These attributes can be added to your script tags.

Usually, a script being downloaded blocks the parser while downloading and executing. Async will let the parsing and downloading occur at the same time but still block parsing during the script execution. Defer will not block parsing during the download and only execute after the HTML has finished parsing.

Which should you use? For anything that you want earlier or that has dependencies, I’d lean toward async.

For instance, I tend to use async on analytics tags so that more users are recorded. You’ll want to defer anything that is not needed until later or doesn’t have dependencies. The attributes are pretty easy to add.

Check out these examples:

Normal:

`<script src="https://www.domain.com/file.js"></script>`

Async:

`<script src="https://www.domain.com/file.js" async></script>`

Defer:

`<script src="https://www.domain.com/file.js" defer></script>`

### 3. Break up long tasks

Another option is to break up the JavaScript so that it runs for less time. You take those long tasks that delay response to user input and break them into smaller tasks that block for less time. This is done with [code splitting](https://developer.mozilla.org/en-US/docs/Glossary/Code_splitting), which breaks the tasks into smaller chunks.

### 4. Use web workers

There’s also the option of moving some of the JavaScript to a [service worker](https://developers.google.com/web/fundamentals/primers/service-workers). I did mention that JavaScript competes for the one main thread in the browser, but this is a workaround that gives it another place to run.

There are some trade-offs as far as caching goes. And the service worker can’t access the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction), so it can’t do any updates or changes. If you’re going to move JavaScript to a service worker, you really need to have a developer who knows what they are doing.

### 5. Use prerendering or server-side rendering (SSR)

If you’re on a JavaScript framework, there’s a lot of JavaScript needed for the page to load. That JavaScript can take a while to process in the browser, and that can cause delays. If you use prerendering or SSR, you shift this burden from the browser to the server.

Further reading

- [Optimize First Input Delay](https://web.dev/optimize-fid/) [–](https://web.dev/optimize-lcp/) [web.dev](https://web.dev/optimize-fid/)
- [How to Improve Page Speed From Start to Finish](https://ahrefs.com/blog/core-web-vitals/) [–](https://web.dev/optimize-lcp/) [Ahrefs](https://ahrefs.com/blog/core-web-vitals/)

## Final thoughts

Even though FID was replaced by INP in March 2024, it’s still worth working on improving FID. Many of the same things you work on to improve TBT and FID should also improve INP.

If you have any questions, message me [on Twitter](https://twitter.com/patrickstox).
