---
title: "Google Lighthouse: What It Is & How to Use It"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-lighthouse"
url: "https://www.semrush.com/blog/google-lighthouse/"
canonical: "https://www.semrush.com/blog/google-lighthouse/"
author: "Tushar Pol"
published: "2021-09-13T19:32:00+00:00"
updated: "2023-03-24T16:09:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T15:50:59+00:00"
status_code: 200
html_hash: "e96cc725e17788e741fbc44aa42c198f52187ab5a1bf59905af2d462088a77d3"
clean_word_count: 2254
clean_char_count: 18602
---
# Google Lighthouse: What It Is & How to Use It

## What Is Google Lighthouse?

Google Lighthouse is a free Google tool that helps you improve the quality of webpages on your website.

The tool audits your pages for performance, accessibility, SEO, and more. And offers suggestions so you can improve these aspects.

It is open-source software—anyone can use it on any webpage.

Whether you’re a web developer, SEO, or website owner, Google Lighthouse can help you enhance your website’s overall experience and performance.

In this post, we’ll cover how Google Lighthouse works and how you can use it to audit your webpages.

Let’s dive in.

## How Does Google Lighthouse Work?

Google Lighthouse works by performing audits for five main website optimization categories.

### 1. Performance

In this audit, Lighthouse measures how quickly a website loads and how quickly users can access it.

It reports your performance for five speed metrics, each measuring some aspect of [page speed](https://www.semrush.com/blog/page-speed/):

![page speed metrics](https://static.semrush.com/blog/uploads/media/22/c4/22c4214a51ac0ce90d76997294b4cc9d/-M8ygRPfxdtshzFfuvqvH32IPfxO0eSCw_GHsueDjCyrItxHORkpyZWdFYnLYUgwro1fq8iRPk0ekjpTE5bosuGTBg5IKBGafpGX5y5P2JMmUDzgMerAr6cjsrAJMi0lL4n0SxWmWJxyvDmDQCrDgMk.jpeg)

- **First Contentful Paint (FCP):** Measures the time at which the first text or image becomes visible to users
- **Largest Contentful Paint (LCP):** Calculates the time a page takes to load its largest element for users
- **Total Blocking Time (TBT):** Measures the amount of time that a page is blocked from reacting to user input, like a mouse click
- **Cumulative Layout Shift (CLS):** Measures the layout shifts that occur as users access a page
- **Speed Index (SI):** Shows how quickly the content of a page is loaded

Lighthouse assigns an overall performance score to a page based on how your page performed for all these metrics. The score can be anything from 0 to 100.

![performance metric](https://static.semrush.com/blog/uploads/media/22/80/2280eed6683f698e1e91a7136323dd4d/2IHp5FJNQxW7BaG7GW5AaSe9_AAjLvzNA8hIbR3Sup7IOOdk-bLFBvTrztuLCmB9wby5XSiBVfh1QUFrduYlm4YdOUTA4RFGHLsPNqY_XzomxIPuVjxqN8xgSu2Q1GAfdzmDhk7Xts5v2PLwoZBKOuQ.png)

If your score is between 90 and 100, it indicates that your page is well optimized for user experience.

Anything below 90 means a significant number of resources on your page are slowing things down, affecting the overall page experience.

Lighthouse also offers suggestions. Which you can implement to improve your performance.

![Lighthouse opportunities and diagnostics sections](https://static.semrush.com/blog/uploads/media/59/8c/598c99d66b0ec6da67c52b568012cbb0/hGfoc6R2b5cRSfzrhRpE2aGytyxkUtMOdCr7Mj5ej09t1iJcvZBBcpB8DVdIW0AGreL6GO-ssIsQurHSBQODoZ0QA7gWWdYSKKpmJVLJmintyuZdTO9xYj6fF-hUzhsXqaAzbnGGMv7WNfBYb7ggE-0.png)

### 2. Accessibility

Lighthouse’s accessibility test analyzes how well people who use assistive technologies can use your website.

Specifically, it looks at elements like buttons and links to see whether they’re described well.

It also analyzes images to see whether [alt text](https://www.semrush.com/blog/alt-text/) is specified. So when users with limited or no vision use screen readers, they understand what the image is all about.

Similar to a performance audit report, the accessibility report gives you a score out of 100. The higher the score, the better.

![accessibility report](https://static.semrush.com/blog/uploads/media/4f/b8/4fb8a960cb7c11a2c5feec50df2699da/QzpBvcGc2j7TLHu3XFwa-cuXdTnT0mNjGQHE5U9DAwdhJZ0dbaSNsg8IEWqTWwWrJdufKbFbGgy-SkDHEo99syTJZJHPNcMyKoc-j9lCNejVn6ijn_xecn09ceeRMkKkKKbApekZeP6eY9-dUG6-KPM.png)

The tool also highlights opportunities to improve your overall accessibility.

![opportunities to improve overall accessibility](https://static.semrush.com/blog/uploads/media/04/f8/04f845989998016f6b5f81bcc551fd24/4g1WCXkaoJVA8GPa7Yyra0rj3J3t3WkrvDYxA-datIe4x-LTJDuMh7mRRpiikbtZx06mhLaPoVTweNyDtDBSDwLWvsSHXvf1MhfIgrD-TtyFJ9ML0TitfLyrbwGaBNgDNreERr-GOVuKKP60t-shluY.png)

### 3. Best Practices

The best practices audit in Lighthouse checks whether your page is built on the modern standards of web development.

Lighthouse examines whether:

- Resources load from secure servers with HTTPS.
- All images appear with the correct aspect ratio and in appropriate resolution
- All JavaScript libraries are safe and free from any vulnerabilities.
- Page has the HTML doctype
- Content Security Policy (CSP) is effective against cross-site scripting (XSS) attacks
- Page is free from all browser errors
- Page is free from deprecated frameworks and APIs
- Page has valid source maps
- Page is free from issues appearing in Chrome DevTools panel, such as network request failures, insufficient security measures, and other browser issues
- Page’s character encoding is set with the meta charset tag
- Page allows users to paste password in password field
- Page creates a good user experience by blocking geolocation and notification permission requests on page load

All these factors decide your score out of 100.

![Lighthouse score out of 100](https://static.semrush.com/blog/uploads/media/d1/0f/d10f8dc0f1c6df570b47ee2ef0779d7e/0x0fHFJs6HwIA_m7WXpN3x1s3axRaRa8Y6o3WAXFAlfoWH6LUtQhoGsAgTR-zS1tl4uXykXtmAe1anrVrTx3mpk8vEEbYbMxWtXrFL4aDeoKlJGQkjw4dtYnHdLHztrjHlkgmL4AaUPBiO4qOhJTBUw.png)

The Lighthouse report on best practices also highlights specific elements that require your attention. Which can improve your score.

![best practices to improve score](https://static.semrush.com/blog/uploads/media/0e/01/0e01fe736199c1a7c8e9551800e86a43/tTI2Dm86--tdM7OpYljd_rtVxLBcBLKysWEx-Gsfw7ySnHVy5XnK9hwMZqQdDo5FzaNS2iml7npf_xhiPdGY2UkoNEPCVBVldNP9imSE115LwsguBPuyHOT1tJJlLg89Y5jrqmsb1EtwXoqyFwYWmnA.png)

### 4. SEO

Lighthouse runs a test to analyze your webpage for some [technical aspects of SEO](https://www.semrush.com/blog/technical-seo/).

Specifically, it checks whether:

- Your webpage is mobile-friendly
- Page has a valid structured data
- Internal links are crawlable
- Page has a valid hreflang attribute
- Title and meta description tags are set
- Page is indexable
- Robots.txt is valid
- Page is returning HTTP 200 (OK) status response code
- Page has a valid “rel=canonical” tag set
- Page content is independent of plugins
- Links on a page are introduced with descriptive text
- Images on a page have image alt texts specified
- Page has a viewport meta tag with width or initial-scale set

And then assigns a score out of 100.

![SEO score](https://static.semrush.com/blog/uploads/media/d8/4c/d84c45f726bf3400fc609ce6885b240e/4JgQIaHSsRlSqQeaAjmOz4xRj9tDoE2HthRpMWmR-SE9a2sUbRbo4TxCK5HGYDc9x6dGaf_RYAKGsPqXoTdhe0S1HcFRlDOdAUK21Uqcwmowtx8ty-9HO5BK7-ZWZbwnJRQLh7YeUqVlN8GVSJDgM50.png)

It also highlights any SEO issues it detected when running an audit.

![SEO issues](https://static.semrush.com/blog/uploads/media/66/64/666468f61a1ac25385cb56df24394158/pPWUs6EUw9dtW-3yJpsdS4joI0XIYT4oIt1fs6qXZPUDGwe9qoF9loF7yElVh9Qeo9MPVG4kdIn0ZsL5KXzB85B6gfdtyUN2eGK8plpbEl01lMId4VjBxCvTmT9nnyD-pVUYwpBzBWkkYCU5skRh9PI.png)

But the tool doesn’t give you a full picture of your SEO.

If you want your website to rank better in Google, you need to ensure it is optimized for all aspects of SEO. Make sure no issues are affecting your rankings.

That's where tools from Semrush can come in handy.

Start with our [free SEO checker](https://www.semrush.com/siteaudit/) for an entry-level read. For deeper coverage, Semrush Site Audit checks your website for over 140 aspects of SEO. Like duplicate content, redirects, internal links, URL structure, and more.

To use the tool, [set up a project](https://www.semrush.com/kb/539-configuring-site-audit) and run your audit.

Once the audit is complete, you’ll get a high-level overview of your website’s SEO health.

![Site Audit dashboard](https://static.semrush.com/blog/uploads/media/f3/3f/f33fa5c9698d4ed6809dabea65ac35c7/NbAG8Rs0TNs-wwTKBms3nQZ_nbd8dta6lI9eKuV9H8eXROeMJnp88fS9XR_iCzmUifOXKsVAXZQHCsjyS4rxUUG2yIzs3NLaPFdz1-nszGbeZZOKLva2H-6J4I6aBUMN9V9zAGxljVkzrlP5nxft5xY.jpeg)

You can also see specific issues that are affecting your performance. Just go to the “**Issues**” tab.

![Issues tab](https://static.semrush.com/blog/uploads/media/f3/8c/f38c7779607d12211580e80173b5b1d4/jE__ATVjk_mmmoD1YAREBN_wjAh2b55kIL9n8aJgjGki6BF_MOOG4wcOBlBqk-0phk7-BfoRHIVlZwPqKP84IbgOzQleBSJ0_cYvPLzaI13ErseenjJtmb8TnxvAYhP35Ip1IjNxjKEprcb2mo4wkwE.jpeg)

For each issue detected, the tool offers advice on how to fix it.

![why and how to fix it example](https://static.semrush.com/blog/uploads/media/89/d7/89d7af0ce29ffb2806dbe351d304e3df/-SAXRC6X07wXXP0s8IKOgEEmTCXNYr221EcDYcEldoif0SICG-NRrDWRBcp808qkAl2DeVv80EgjYrfdrxvbMRzzjE8WmAcOhE9RPMCp5-KYsgpRFMbTft_a5Nx8xyh5IHulAROW2NFAP2B6CCmosnc.jpeg)

Solve each issue the tool detects for your site. So your website’s SEO stays in a healthy state.

### 5. Progressive Web App (PWA)

The PWA audit in Lighthouse validates whether your web application uses modern web capabilities to provide an optimal user experience.

It checks whether your web app is:

- **Fast and reliable** on mobile networks and offers offline functionality
- **Installable** on multiple device types and has features like offline functionality and push notifications
- **PWA-optimized** by redirecting HTTP traffic to HTTPS, configuring a custom splash screen, sizing webpage content to fit on mobile screens, and implementing all the [other best practices listed by Lighthouse](https://developer.chrome.com/en/docs/lighthouse/pwa/)

The test runs your web app against these factors and assigns one of the PWA badges.

![PWA badges](https://static.semrush.com/blog/uploads/media/84/b1/84b101dce24252c21594097c9974a19d/zgG74hsFa8htNN0s3kO_pYdttODRyz_1asZ3ov1q9ILRVLklndvLpP6c5ZIVXIa4M9xg9-MP-crZD2Y2gHZNqUZPltVO1IO--wBc3Vap7RLbGxQj9jRyNIKmzVHCNBs8x_VIZR5RLAsHUCc7GDd_mbg.png)

(Image source: Github)

This means that, unlike the first four reports, you’re assigned **a** **badge** (not a score of 100) when you run a PWA audit in Lighthouse.

Like this:

![PWA audit in Lighthouse](https://static.semrush.com/blog/uploads/media/9e/41/9e4150cfe557670e1c1e0721644c1d82/cH5bW2ydhXqZhyaNtibCKU3UXSWtwxi_C9nPhM2LSVoU7EPfHFnrjbHcW0q0XRLQxhZECC3TqmoryIu9DzsuJwAmZDFSiU653hTNvXcTRJC3IwASYyPeGLlUBfx0nkB7wwGftIGiFDfOuW30npk1JxQ.png)

The audit report will also provide suggestions for improving your overall PWA performance. Including specific issues that need to be addressed.

![suggestions for improving overall PWA performance](https://static.semrush.com/blog/uploads/media/8d/1a/8d1a9b5c9525098e6e22405c9b5065f7/H_Fy3KltZJ95agelpi7YKl3Mtiku4SImKc3QL8yS3C0aM_tbsIWrxXxmilLoT0gGofgA4Epcw592UUFvsmEldn7ga42j0dNkGR9n8-sZWg9ScIUD1jkKz2KvNGdCVH8lMQdE_cJjBUpEzj73un-9P4M.png)

## How to Use Google Lighthouse

Now that you know what Google Lighthouse is and how it works, let’s look at the different ways you can use it to audit your pages.

### Using Lighthouse with Chrome DevTools

In your Chrome browser, you can run a Google Lighthouse audit with Chrome DevTools.

Open the webpage you want to audit.

Then right-click anywhere on the page and select “**Inspect**.”

![navigation to inspect tool](https://static.semrush.com/blog/uploads/media/9b/53/9b537c6bf0b05e7c529db5c657530c87/_IXO1d-9o4fpfwW2eSmD_kbDZrCkkMVBuD1CUOu1XjAQg1D-Eo4qlQbjUtZ7f8OwGhzgOE8qoelyhFtWV12WhwkyKgQ4OWbzQ6DpFeLlNVOfGyAzOk8_85SRwVSlnKQlEsvJaE5h1mc28CH4kRGPu18.jpeg)

The Inspect feature will open a DevTools panel on the right side of the webpage.

![DevTools panel](https://static.semrush.com/blog/uploads/media/5c/c9/5cc9491b5412b1fc1ef06d23ab2328e7/5vS7_ZU1d-9vfMJv9l61GLG0Ch6GVaZizs0MR8SWa_t8FmL5Sw--BddIyEGd_k1wvy007E1G8rTXZg1qfxJCHakeeyne_wCdLLn3WllMzHcw-JW3XFF2wavFaO1NRubuloh6l52-Wr0qbk_hXIeAx7s.jpeg)

Select “**Lighthouse**” from the panel’s toolbar. (If you can’t find the Lighthouse option, click on the two arrows at the end of the toolbar. You’ll see it there.)

![lighthouse in panel’s toolbar highlighted](https://static.semrush.com/blog/uploads/media/17/c8/17c87518da6c545d4f0bccc24557548d/I9UNvYy7Y2RT2UJwr1n8YMMjtHikXZ5iL1iYaSnVuSjbkNxZQTX_VGr9mNjLMpoIlwo-AeL2JrbQvvpy6cJi1XnFD3KlSi3PykwUmaIliarhhUAtNub87oDJ0Ht2WajLHbaZ_4vQEfgn4F9xYNPSavA.jpeg)

From here, you can select one, more, or all categories, depending on which aspects of your website you want to analyze. And click “**Analyze page load**.”

![Analyze page load button highlighted](https://static.semrush.com/blog/uploads/media/b5/b7/b5b770d7f78b81f74312817b6fee1bbc/Nbsba98ai3v_pREjQTiGBUUruENlBMAp-z5AO99Tppuqc2Ny8AHiLwrwZXqKsCIj-Hj-9J8WfCBF5THbcc4V2svylmYguih9wBSyLqMRyWxT1inVFIwJWuS5alrGgKlyoG2EywzfFLJ0gXVgbdOpf_M.png)

Then the tool will generate a report for you. You’ll find your audit scores for each category at the top.

![report with audit scores](https://static.semrush.com/blog/uploads/media/c3/1e/c31e65bbc6a067fcbf8ff975b8dc0bc4/nc-_GWY_R5u7jLL4eDWhBLNNguDSB5V5srzuSvM3f73-xuvfTfuVbOJzq24bBHhuzjtgT9bGiqgwhYbUBf5na2f7UCchvofGwWgJdmTUuCpjXUoNLuVHjMZBw5eOd6pILiW0g_eUu34ymMQ5LOpA7vE.png)

You can click on a specific category to learn more. In this example, we clicked “**Performance**” audit.

![Performance audit more details](https://static.semrush.com/blog/uploads/media/86/ab/86ab4f89df138a3fab75320f8eb0a8f1/O86qvrrucUPig9hCcknCCncOUaxNLo5Zr3-PGPfGtcHftgs16IklSm3IM_5sTfnWy2qXhhx0jg2X9ccydzzUyjBh41nO7SxC3yc1OzvvWhIg5SiiUzaYE-Qt7TS53HGzqUjiKzn7847M92u-lR2ApWE.png)

**Note:** You’ll notice Lighthouse measuring your performance for six speed metrics (instead of five) when you run a performance audit with DevTools.

That extra metric is **Time to Interactive** (TTI). Which calculates the time it takes for a page to become fully interactive for users.

This metric is [one of their retired metrics](https://developer.chrome.com/en/docs/lighthouse/performance/). It’s unclear why it is still being accounted for when you run Lighthouse audits in DevTools.

### Using Lighthouse with Chrome Extension

Lighthouse has a Chrome extension that can perform audits for you.

On your Chrome browser, install the [Lighthouse Chrome extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk/).

Visit the webpage you want to test.

Then open the Chrome extension menu and select “**Lighthouse**.”

![Lighthouse in Chrome extension menu](https://static.semrush.com/blog/uploads/media/28/04/2804135f59093355f70a75a3407e193e/Xq8psRg4hftIpK6iIf0G5VrQ0AGcunqGsiWi5g1AkN9E0uqP8v5ndBQHiy_pHbGEq1KZntEDbZ-CYP42Uy9ifhMqcmYh2uuy0IYZ7ArQePd3jkxGEJ6HxecQj14qy5ywIveh3uXaHT0WqzFSpHjQUdA.png)

Then click on the cog icon.

![cog icon highlighted](https://static.semrush.com/blog/uploads/media/64/2f/642fafb541d51ea6cecc083b10d5a061/TZcPHAuNVELA2xyujhbtFzUjyFbCv5vKaNnpfsoNYPXfJkEaR22RhhghEnLrhU9BlahmqJMXW26svYE5g_2yK48sgFUoDH6nHF127IQaHZ7ChXbg_p4YY5ua7-uU_Wd5c_k1gl1BdFrVLuR0q6UosFs.png)

You will see settings where you can select or deselect specific categories based on the reports you want to generate.

![categories settings](https://static.semrush.com/blog/uploads/media/2d/a0/2da0179eaf895e1b565d376885c5fca8/7irwvoOe3PZ7TST943LZfFhPNUFhpa7fNpi8f8IS0jdhbSph_hQpiwwIoE7nW98v5vLAfc-Tg0rSsgKSnPeY4bSvlmu3En7zrOAEhNU2QjReKE9yA3lO4GLg-BmMmsIrAxHPIxhZautYjh0FvLQlCpU.png)

Then start the audit by clicking the “**Generate report**” button.

![Generate report button highlighted](https://static.semrush.com/blog/uploads/media/9b/15/9b15ff685ae4a754d0325cfdee4e9fb6/PYDquHGOdU7MhD2VsE7r9TB0ZI1ADYPUm5-RFv3UVZOXZm8rxLPkRBgUiZbTTEDPM5_tG-AACdqsNxwoF0PDARqltXaiHkdGV2d459P68fytvapaTWqgdMSp7zllz65gkD5V594gkikHByeekPjLU4k.png)

Lighthouse will generate a report for you in a new tab.

![Lighthouse report](https://static.semrush.com/blog/uploads/media/84/19/8419926379a870037df7f430b1caff4f/2EQwMzyfRddofWaETwNv4Q_RLEvPNBE78H9_plvEBD4U1TKtSK9t5k7izPRyNziK6qPZ00Sztzf2JsmkjN73o5_V6MKdduQNrsgcr2MznLRPwwjHNoJud4PfGCJp5qUaAA4dyz1tu1u-d7j1qNwjMoE.png)

### Using Lighthouse in PageSpeed Insights

Lighthouse is also available through Google’s [PageSpeed Insights](https://pagespeed.web.dev/) tool.

Open the tool. Enter your page URL, and click “**Analyze**.”

![PageSpeed Insights tool](https://static.semrush.com/blog/uploads/media/51/6e/516e8a14fd246ff3a98a4ae7154cf240/TR3bTHlUpSvzyM9IZqYwnVJYdhqOE2HBuFPoCCLBY6cVZfea_8voGqQXPzHbmYbfMIKwv8EGVFRFw6AsaG0-javLeF35Wqm1Fnel-o4TP-xNtcjZAG-ehBaXx8T6dgBGJvwZLJCllXQ36us_ynMQiCo.png)

The tool will generate reports for all categories, except PWA. [PageSpeed insights](https://www.semrush.com/blog/google-pagespeed-insights/) doesn’t perform PWA audits.

![PageSpeed insights generated report](https://static.semrush.com/blog/uploads/media/03/d7/03d77a705eb1a765c1fa7232f86a0af5/-ykigbXJgxnE98Eqp1Worp3ey5BZcPcPbFh6w6_YkrM1e6bJpjRP33s-96lAiWb1GfEcTgxCw6g6BhuicLev81sKPy0xO0tfmJfzBLK4dsjxEF679jwHvzablSH-sbdeVdM0jc-E_DkY2hntIZioA2Q.png)

### Using Google Lighthouse via Node Module

You can also use a Node JavaScript module to run Lighthouse audits.

Install the [current Node](https://nodejs.org/en/download/current/) on your system.

Then run the following command line to install Lighthouse:

`npm install -g lighthouse`

Once Lighthouse is installed, use the command line below to generate reports.

`lighthouse <url>`

(You need to replace the “url” with the web address of the page you want to test.)

## FAQs

### How Is Lighthouse Different from PageSpeed Insights?

Lighthouse is different from PageSpeed Insights in that Lighthouse only uses lab data to measure the performance of your pages. While PageSpeed insights uses **both** lab and field data.

Lab data reflects how hypothetical users **may experience** your site. In contrast, field data reflects how real users **experienced** your website.

### Why Are My Scores Different Each Time I Test?

The scores you see in Lighthouse can vary each time you run the test.

Network conditions, browser extensions that modify network requests, and ads displayed on the specific page affect your score each time you conduct the test.

### Do Lighthouse Reports Include Core Web Vitals Metrics?

Yes. The performance audit in Lighthouse analyzes your website for the following [Core Web Vitals](https://www.semrush.com/blog/core-web-vitals/) metrics:

- [Largest Contentful Paint (LCP)](https://www.semrush.com/blog/lcp/)
- [Total Blocking Time (TBT)](https://www.semrush.com/blog/google-inp/) (which acts as a proxy for the original First Input Delay (FID) metric)
- [Cumulative Layout Shift (CLS)](https://www.semrush.com/blog/cumulative-layout-shift/)
