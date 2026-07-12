---
title: "What is a Soft 404 and what causes them?"
source: "ahrefs-blog"
content_type: "blog_article"
freshness_risk: "unknown"
slug: "what-is-soft-404"
url: "https://ahrefs.com/blog/what-is-soft-404/"
canonical: "https://ahrefs.com/blog/what-is-soft-404/"
author: ""
published: ""
updated: "2025-06-03T23:50:43+00:00"
categories:
  - "Uncategorized"
freshness_reasons: []
fetched_at: "2026-07-12T19:58:08.149057+00:00"
status_code: 200
html_hash: "ba148e03bba3a78499cba9f9b196cbaca28b0442211b96c2a0837bb04aacecb6"
clean_word_count: 454
clean_char_count: 2838
---
# What is a Soft 404 and what causes them?

A **soft 404 error** is a specific type of issue that occurs when a web page *appears* to be missing or broken to users, but the server incorrectly reports that the page is functioning properly. Instead of returning a standard “404 Not Found” status code, it returns a “200 OK” status code. 

**Here’s a breakdown:**

- **Standard 404 Error:** When a page is truly missing, the server sends a 404 status code, indicating that the page doesn’t exist and should not be indexed by search engines.
- **Soft 404 Error:** The page appears to be “not found” or “out of stock” to users, but the server returns a 200 OK status code. This signals to search engines that the page is valid and can be crawled and potentially indexed.

**Why are soft 404 errors problematic?**

- **Confuse Search Engines:** Soft 404s send mixed signals to search engines, leading to potential indexing issues and wasted crawl budget. Google might spend time crawling and processing these low-value pages instead of discovering valuable content on your site.
- **Poor User Experience:** Users who land on soft 404 pages may find the content irrelevant or non-existent, leading to frustration and increased bounce rates. This can negatively impact your site’s SEO and potentially deter users from returning.
- **Wasted Resources:** Search engines waste time crawling and indexing these unproductive pages, which can affect your site’s overall crawl efficiency and indexing process.

**Common causes of soft 404 errors include:**

- **Thin or low-quality content:** Pages with very little or irrelevant content can be flagged as soft 404s.
- **Incorrect redirects:** Redirecting deleted pages to irrelevant content or the homepage can confuse search engines.
- **Server misconfigurations:** Your server might be incorrectly configured to return a 200 OK status for missing pages.
- **Empty search results pages or category pages:** If your website’s search or category pages return “no results found” but still give a 200 status code, they can be interpreted as soft 404s.

**How to find and fix soft 404 errors:**

- **Google Search Console:** Use the Coverage report to identify pages flagged as “Submitted URL seems to be a Soft 404”.
- **Improve content:** If a page is flagged due to thin content, add more valuable and relevant information to it.
- **Set up proper redirects:** Use 301 redirects for permanently moved pages, directing users to the correct URL.
- **Configure server response codes:** Ensure your server returns a proper 404 or 410 status code for missing pages.
- **De-index unwanted pages:** If a page isn’t intended for indexing, use the ‘noindex’ directive to prevent search engines from crawling and indexing it.
- **Regularly audit your website:** Use tools like Screaming Frog or Ahrefs to identify soft 404 errors and address them promptly.
