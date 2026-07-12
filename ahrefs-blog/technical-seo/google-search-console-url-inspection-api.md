---
title: "Google’s New Search Console URL Inspection API: What It Is & How to Use It"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-search-console-url-inspection-api"
url: "https://ahrefs.com/blog/google-search-console-url-inspection-api/"
canonical: "https://ahrefs.com/blog/google-search-console-url-inspection-api/"
author: "Chris Haines"
published: "2022-03-28T06:00:49+00:00"
updated: "2023-02-21T22:42:31+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T11:34:24+00:00"
status_code: 200
html_hash: "e9c2758c16e554e298cade8b7c01bb34ce36dbcf72f0839375db7ff91e08654f"
clean_word_count: 1917
clean_char_count: 11517
---
# Google’s New Search Console URL Inspection API: What It Is & How to Use It

Diagnosing technical issues on your website can be one of the most time-consuming but important aspects of running a website.

To make things worse, Google only allows you to inspect one URL at a time to diagnose potential issues on your website (this is done within Google Search Console).

Luckily, there is now a faster way to test your website: enter the Google Search Console URL Inspection API…

## What is the Google Search Console URL Inspection API?

The [Google Search Console URL Inspection API](https://developers.google.com/search/blog/2022/01/url-inspection-api) is a way to bulk-check the data that Google Search Console has on URLs. Its purpose is to help developers and SEOs more efficiently debug and optimize their pages using Google’s own data.

Here’s an example of me using the API to check whether a few URLs are indexed and submitted in my sitemap:

## What type of data can you get from the Google Search Console URL Inspection API?

The Google Search Console URL Inspection API allows you to pull a wide range of data. Below is a list of some of the most discussed features:

### lastCrawlTime

With this field, you can understand exactly when [Googlebot](https://ahrefs.com/blog/googlebot/) last crawled your website. This is extremely useful for SEOs and developers to measure the frequency of Google’s crawling of their sites. Previously, you could only get access to this type of data through log file analysis or spot-checking individual URLs with Google Search Console.

### robotsTxtState

With this field, you can understand whether you have any [robots.txt](https://ahrefs.com/blog/robots-txt/) rules that will block Googlebot. This is something you can check manually, but being able to test it at scale with Google’s own data is a fantastic step forward.

### googleCanonical and userCanonical

In some situations, Google has been known to select a different [canonical](https://ahrefs.com/blog/canonical-tags/) from the one that has been specified in the code. In this situation, having the ability to compare both (side by side and at scale) using the API is useful for enabling you to make the appropriate changes.

### crawledAs

This field allows you to understand which user agent is used for a crawl of your site: Mobile/Desktop. The response codes are below for reference:

- **DESKTOP** – Desktop user agent
- **MOBILE** – Mobile user agent

### pageFetchState

Understanding the pageFetchState can help you diagnose server errors, not found 4xxs, soft 404s, redirection errors, pages blocked by robots.txt, and invalid URLs. A list of responses is below for reference.

| Field | What it means |
| --- | --- |
| PAGE\_FETCH\_STATE\_UNSPECIFIED | Unknown fetch state |
| SUCCESSFUL | Successful fetch |
| SOFT\_404 | Soft 404 |
| BLOCKED\_ROBOTS\_TXT | Blocked by robots.txt |
| NOT\_FOUND | Not found (404) |
| ACCESS\_DENIED | Blocked due to unauthorized request (401) |
| SERVER\_ERROR | Server error (5xx) |
| REDIRECT\_ERROR | Redirection error |
| ACCESS\_FORBIDDEN | Blocked due to access forbidden (403) |
| BLOCKED\_4XX | Blocked due to other 4xx issue (not 403, 404) |
| INTERNAL\_CRAWL\_ERROR | Internal error |
| INVALID\_URL | Invalid URL |

### indexingState

The indexing state tells you the current status of indexation for the URLs. Apart from the more obvious Pass and Fail responses, there are other responses:

- **NEUTRAL** is equivalent to the “Excluded” message in Search Console.
- **PARTIAL** is equivalent to the “Valid with warnings” message in Search Console.
- **VERDICT\_UNSPECIFIED** means that Google is unable to come to a conclusion about the URL(s) in question.

TIP

Having indexing issues? Read our “[10 ways to get indexed on Google](https://ahrefs.com/blog/google-index/)” post.

### coverageState

This gives you detail on whether a URL has been submitted in your sitemap and indexed.

### referringUrls

This allows you to see where each page is linked from, according to Google.

### Sitemap

This enables you to understand which URLs are included in the sitemap(s).

### Other uses for the API

You can also use the API to inspect your AMP site—if you have one.

## How to use the Google Search Console URL Inspection API step by step

Using the Google Search Console URL Inspection API involves making a request to Google. The request [parameters](https://ahrefs.com/blog/url-parameters/) you need to define are the URL that you want to inspect and also the URL of the property in Google Search Console.

The request body contains data with the following structure:

If you are curious to learn more about how to use the API, [Google has extensive documentation about this](https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect).

Below is an example of the type of response you can get from the API:

If you’re not comfortable with code or just want to give it a go straight away, you can use [valentin.app’s free Google Bulk Inspect URLs tool](https://valentin.app/inspect.html). The tool provides a quick way to query the API without any coding skills!

Here’s how to use it. You can:

1. Go to <https://valentin.app/inspect.html>, authorize access to your Google account, and select the Search Console property you want to test. Then paste your URLs into the box below. (The data will be processed in your browser and not uploaded to a server or shared with anyone.)
2. Click the “Inspect URLs” button. The data will start to pull from the API.
3. Export the data as a CSV or Excel file by clicking the button.
4. Analyze the data and check for any potential issues.

## How can you use the Google Search Console URL Inspection API in practice?

In theory, the Google Search Console URL Inspection API seems like a great way to understand more about your website. However, you can pull so much data that it’s difficult to know where to start. So let’s look at a few examples of use cases.

### 1. Site migration – diagnosing any technical issues

[Site migrations](https://ahrefs.com/blog/website-migration/) can cause all kinds of issues. For example, developers can accidentally block Google from crawling your site or certain pages via robots.txt.

Luckily, the Google Search Console URL Inspection API makes auditing for these issues a doddle.

For example, you can check whether you’re blocking Googlebot from crawling URLs in bulk by calling robotsTxtState.

Here is an example of me using the Google Search Console URL Inspection API (via valentin.app) to call robotsTxtState to see the current status of my URLs.

As you can see, these pages are not blocked by robots.txt, and there are no issues here.

TIP

Site migrations can sometimes lead to unforeseen technical SEO issues. After the migration, we recommend using a tool, such as Ahrefs’ [Site Audit](https://ahrefs.com/site-audit), to check your website for over 100 pre-defined SEO issues.

### 2. Understand if Google has respected your declared canonicals

If you make a change to the[canonical tags](https://ahrefs.com/blog/canonical-tags/) across your site, you will want to know whether or not Google is respecting them.

You may be wondering why Google ignores the canonical that you declared. Google can do this for a number of reasons, for example:

- Your declared canonical is not https. (Google prefers https for canonicals.)
- Google has chosen a page that it believes is a better canonical page than your declared canonical.
- Your declared canonical is a noindex page.

Below is an example of me using the Google Search Console URL Inspection API to see whether Google has respected my declared canonicals:

As we can see from the above screenshot, there are no issues with these particular pages and Google is respecting the canonicals.

TIP

To quickly see if the googleCanonical matches the userCanonical, export the data from the Google Bulk Inspect URLs tool to CSV and use an **IF** formula in Excel. For example, assuming your googleCanonical data is in Column A and your userCanonical is in Column B, you can use the formula **=IF(A2=B2, “Self referencing”,”Non Self Referencing”)** to check for non-matching canonicals.

### 3. Understand when Google recrawls after you make changes to your site

When you update many pages on your website, you will want to know the impact of your efforts. This can only happen after Google has recrawled your site.

With the Google Search Console URL Inspection API, you can see the precise time Google crawled your pages by using lastCrawlTime.

If you can’t get access to the log files for your website, then this is a great alternative to understand how Google crawls your site.

Here’s an example of me checking this:

As you can see in the screenshot above, lastCrawlTime shows the date and time my website was crawled. In this example, the most recent crawl by Google is the homepage.

Understanding when Google recrawls your website following any changes will allow you to link whether or not the changes you made have any positive or negative impact following Google’s crawl.

## FAQs

### How to get around the Google Search Console URL Inspection API limits?

Although the Google Search Console URL Inspection API is limited to 2,000 queries per day, this query limit is determined [by Google Property](https://support.google.com/webmasters/answer/34592?hl=en#types).

This means you can have multiple properties within one website if they are verified separately in Google Search Console, effectively allowing you to bypass the limit of 2,000 queries per day.

Google Search Console allows you to have 1,000 properties in your Google Search Console account, so this should be more than enough for most users.

### Can I use the Google Search Console URL Inspection API on any website?

Another potential limiting factor is you can only run the Google Search Console URL Inspection API on a property that you own in Google Search Console. If you don’t have access to the property, then you cannot audit it using the Google Search Console URL Inspection API.

So this means auditing a site that you don’t have access to can be problematic.

### How accurate is the data?

Accuracy of the data itself has been an issue for Google over the last few years. This API gives you access to that data. So arguably, the Google Search Console URL Inspection API is only as good as the data within it.

As we have previously shown in our [study of Google Keyword Planner’s accuracy](https://www.youtube.com/watch?v=HDFQlxIfgHY), data from Google is often not as accurate as people assume it to be.

## Final thoughts

The Google Search Console URL Inspection API is a great way for site owners to get bulk data directly from Google on a larger scale than what was previously possible from Google Search Console.

[Daniel Waisberg](https://twitter.com/danielwaisberg) and the team behind the Google Search Console URL Inspection API have definitely done a great job of getting this released into the wild.

But one of the criticisms of the Google Search Console URL Inspection API from the SEO community is that the query rate limit is too low for larger sites. (It is capped at 2,000 queries per day, per property.)

For larger sites, this is not enough. Also, despite the possible workarounds, this number still seems to be on the low side.

What’s your experience of using the Google Search Console URL Inspection API? Got more questions? Ping me [on Twitter](https://twitter.com/chris_at_b449). 🙂
