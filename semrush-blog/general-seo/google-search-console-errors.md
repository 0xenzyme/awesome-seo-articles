---
title: "Google Search Console Errors: Identifying and Fixing Them"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-search-console-errors"
url: "https://www.semrush.com/blog/google-search-console-errors/"
canonical: "https://www.semrush.com/blog/google-search-console-errors/"
author: "Rachel Baker, Karla Margeson"
published: "2024-03-20T10:51:00+00:00"
updated: "2024-03-20T10:51:00+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "General SEO"
fetched_at: "2026-06-12T15:57:07+00:00"
status_code: 200
html_hash: "7c9f3ae9d9e32450415612f0e9aa651cc380d007e57b93f4b64ecd93a0dca6f1"
clean_word_count: 4365
clean_char_count: 32282
---
# Google Search Console Errors: Identifying and Fixing Them

Google Search Console is a web service that lets you monitor and manage your website's presence in Google Search results.

It also helps you identify potentially impactful website errors. Here’s what you need to know about these errors and how to fix them.

## Understanding Google Search Console Errors

If Googlebot comes across issues when it crawls your site, those issues may be flagged for you as errors in Google Search Console.

These issues are important to review.

Why?

For one, they can negatively impact your site's visibility in search engine results pages ([SERPs](https://www.semrush.com/blog/serp/)).

For example, unresolved errors can prevent Google from properly indexing your website. Unindexed pages won’t show up in search results.

Unresolved website errors can also negatively impact user experience. This is bad for visitors. And it’s a key ranking factor for Google, so poor performance in this area can cause Google to rank you lower in search results, too.

Let’s take a look at how to fix Google Search Console errors.

## Types of Google Search Console Errors and How to Fix Them

### Status Code Errors

Status code errors in Google Search Console relate to the HTTP status codes returned when Googlebot attempts to crawl your webpages.

HTTP status codes are relayed every time a site loads. When a user types in a URL or a bot visits the site, a request is sent to that site’s server. The server responds with an HTTP status code that tells the browser—or bot—more about that page.

The HTTP status codes are three-digit numbers. For example, “200,” “301,” or “404.”

![The HTTP status code 404 error founds in GSC](https://static.semrush.com/blog/uploads/media/eb/17/eb176b21d5f2a46df340fa2a7748979b/931fca94be41458daedc7c8a490afab9/2T4IQpAhHmGW6qcNGy1tqilAdXhQl4o2IymSMcBW7Hq5wJwaFKlcxlRMvKcf06wYLE8rijUZTokwJbx8WZkNKx6n-mCk2oLaeIoTONcjHSG9m0WbKWxKXAmr9DHNKlldWdd_jiS3FOD-_irxdEGJ76A.jpeg)

Different status codes convey different information about the success or failure of a request.

For example, the status code “200” signals that everything is good and the page can be accessed as expected.

However, some status codes indicate there were problems accessing the webpage. These show up as errors in Google Search Console. Because they can negatively impact the ability of crawlers and users to access your site.

To see if you have any status code errors, open [Google Search Console](https://search.google.com/search-console/about) and click on “**Pages**” in the left-hand menu.

!["Pages" selected from the Google Search Console menu](https://static.semrush.com/blog/uploads/media/c9/80/c980ea21a38267d34b788d9c9a484d74/0ecb89d7294e77fd28dc34e6bbfab839/Tbzq6hl5dl0YNhXiFHqmdurzXRWug4vmtQOJN69W71_xXHChik_QTGU_ppoQx4420rSQnuP72vJYvElWZcKt5_TbZeDXZFGqu400wMQSk3u0gKKsdmn4eX9wMvJrn6LzLqkZg6NZ27WuR8PPErGKac8.jpeg)

You’ll see a breakdown of the pages on your website according to whether they are “indexed” or “not indexed.”

It’s possible some pages haven’t been indexed due to a status code error.

To see if that’s the case, scroll down to the bottom of the report. You’ll see a table with the title “Why pages aren’t indexed.”

!["Why pages aren't indexed" page in Google Search Console](https://static.semrush.com/blog/uploads/media/bb/09/bb09565db49b2c27e140e3b4246d58a0/b7b2d1b9799cdc5eab97355036e44a2a/pO9h8-SDfghOph9cYc3A9-24YNgS-oSDwAq_Jv9_Ot9hO16qJqblTf2DxQa1snzUuz0vH5NVna-QL3GoBVIALFfuw6KHSMoLe27QhhKerxtvQuqT4iho-d7C1Y5zktw4p1byigTtTcEzibHV9Vv6E18.jpeg)

If there are any status errors, you’ll see one of the following under “Reason”:

- Server Error (5xx)
- Not found (404)
- Unauthorized request (401)
- Soft 404
- Redirect error (3xx)

Let’s review what the different status code errors mean and how to fix them.

#### Server Errors (5xx)

A three-number status code beginning with “5” reflects a server error. This indicates a problem with the server hosting your website.

Here’s what a server error looks like in Google Search Console:

!["Server error (5xx)" in Google Search Console](https://static.semrush.com/blog/uploads/media/3e/17/3e17ac2c729b6bf53db083d36793b02c/ed1aaa74d26cbec905458b8df0c2ac54/Bkfa2HK-hxlJ2Tb_N6hkZsVTg78qdnWzl-fMh9LfgBAM6Aj0_41_U7MgwDi6r3N-uHTyqE8zV8kyz__uyZXUtFawl7j7Xvt5frdGt6uMLI9hKOtMSoAnZ_qJHg4_caJhg23by_retoMGjEP40iPQVXY.jpeg)

Common causes of a 5xx status include:

- **Programming errors**: Bugs or coding errors in the server-side scripts (e.g., PHP, Python, Ruby) that power your website
- **Server configuration issues**: Misconfigurations in the server settings or the web server software (e.g., Apache, Nginx)
- **Resource exhaustion**: If the server runs out of resources (such as memory or processing power), it may struggle to handle requests, leading to internal server errors
- **Database issues**: Problems with the database that your website relies on, such as connection issues or database server errors, can trigger a 5xx error

#### How to Fix a Server Error (5xx) in Google Search Console

- **Review recent changes.** If the error started occurring after recent updates or changes to your website, consider rolling back those changes to see if the issue resolves.
- **Contact your hosting provider.** If you're not sure how to resolve the server error or if it's related to the server infrastructure, contact your hosting provider for assistance. They may be able to identify and fix the problem.
- **Test server resources.** Ensure that your server has sufficient resources (CPU, memory, disk space) to handle the traffic and requests to your website. Consider upgrading your hosting plan if necessary.

Once you've identified and resolved the underlying cause of the 5xx server error, use Google Search Console to request a recrawl of the affected pages.

You do this by entering the affected URL into the search box at the top of Google Search Console:

![The search box at the top of Google Search Console](https://static.semrush.com/blog/uploads/media/12/42/1242130258d8ef57243daed6b390cced/d278649cfa33fb89c823bd23a9a44275/GzaZvXIBr-mFxzJ2MyHUkMicU7PNIDYnNtvc6tHpm2FQ7FhTkO1RP0ICebHpEzG_G-yZKfK6_g85aX8VeqlnZYma3TVgQaKSppLbB3FwifZUMdl-TNBIc5HU10Q8sCsYugRHLeJTvb4_oqjiDpoZdQo.png)

Then click “**REQUEST INDEXING**”:

!["REQUEST INDEXING" button in Google Search Console](https://static.semrush.com/blog/uploads/media/65/50/6550fe147450caeb8dbec445eac9e2ab/dc568e4091f17cd3e4ebd36184bf85df/NeU9KHVAV6DI2U1-HM6C20SR8RVzxtkDi2P886fAybl4BCWE8XjcDNk5r7ZrIGQI-YbLDzxxUZ_NsCJUr14reaxyLk8TnVKpHRL1nrzblr5L2BkcR8Oq82oPq50Or_ZkpO4ACpWNZdToFrXVQOnbuxA.jpeg)

This asks Googlebot to revisit the pages and update its index with the corrected information.

#### Not Found (404) Errors

The "404 Not Found" error is a standard HTTP response code that’s returned when a server can’t find the content associated with the requested URL.

In the context of Google Search Console, it means Googlebot tried to crawl a page on your site, but the server returned a 404 error because it couldn’t find the page’s content.

Here are some common reasons why a 404 error might occur:

- **Page deletion or removal**: If you intentionally deleted a page or removed it from your website and Googlebot attempts to crawl that page, the server will return a 404 error
- **URL changes without proper redirects**: If you've changed the URL structure of your website without implementing proper redirects (e.g. 301 redirects), the old URLs may result in 404 errors
- **Typo or mistyped URL**: It's possible that there was a typo or a mistake in the URL provided to Googlebot. Ensure the URLs in your sitemap and internal links are correct and lead to existing pages.

#### How to Find 404 Errors in Google Search Console

Open Google Search Console and click on the “**Pages**” report.

!["Pages" selected in Google Search Console menu](https://static.semrush.com/blog/uploads/media/11/05/1105d9ed3ed06cfcb43d2b3157ca86fa/6b081d97644fd246a4a058af4c6f453a/yAopiK0KN-EPkqJJjSyS4_W4bmAjmavxV-wHqaE8VhOlBRgQI_sCwCmx_2-ajRnIYE9KSwEPeehr5hNWattf8VMJupjpNYNGeQpt_equJheH7vYvn5reSMiJYruIr0qrneP0TYBhvi-xHp3CQrrDZTU.jpeg)

Scroll down to see “Why pages aren’t indexed.” Here, you’ll be able to see if any pages have a 404 error.

!["Not found (404)" error found in Google Search Console](https://static.semrush.com/blog/uploads/media/ba/14/ba14052d7c4e569ce08ab0252f4f1393/8aec674fd88b577cfb948b9f0cdc0fe8/Ha0YOfXp6lg6PZ_SSouWaSKfSfzMG60WOTZ42CBrRxwolnXFUQWljQfP5Euh7wvrkkOsnfBVDzuRRaqObDynCxYBzYRXv9j3LN7bUb1ibS0qn_z7inJkbRgVR8ygNbRju32GJ-bx8yd6HFc7qQo6anY.jpeg)

#### How to Fix a 404 Error in Google Search Console

- **Implement 301 redirects.** If you've deliberately and permanently moved a page to a new location, use[301 redirects](https://www.semrush.com/blog/301-redirects/) to point the old URL to the new one.
- **Update internal links.** If there are links within your website to deleted pages, update those links to point to valid URLs. You can find these links using [Site Audit](https://www.semrush.com/siteaudit///) from Semrush.
- **Check external links.** If external websites are linking to non-existent pages on your site, consider reaching out to those sites and requesting that they update their links.
- **Submit a sitemap.** Ensure that your website's sitemap is up to date and accurately reflects the current structure of your site. Then [submit the sitemap](https://www.semrush.com/blog/submit-sitemap-to-google/) to Google Search Console.

#### Unauthorized Request Errors (401)

An error with the HTTP status code "401" in Google Search Console indicates that a request was "unauthorized."

!["Blocked due to unauthorized request (401)" error in Google Search Console](https://static.semrush.com/blog/uploads/media/3d/68/3d68e1cbf0ac41515883caf3afe960f4/003e8a8f4df846b539dd792e1436a671/DqeYNqXGWSbTZAoJOdhe8d1hgYMrHGMa5a3-0F80MzXe9gAhxn3AeaOFhI_Vdx3pH70PlooWQkozFpC784nN9by9TTypcEDAt99qqqohFNvkiBz6uV-0JHekmyoR95Tq-s_PBkrKl3CPRnHrTf8bEYs.png)

Image Source: [Onely](https://www.onely.com/blog/how-to-fix-blocked-due-to-unauthorized-request-401/)

401 errors appear when:

- The page contains password-protected content, meaning Googlebot and other crawlers can’t access the page
- There are IP-blocking or access restrictions preventing Googlebot’s IP addresses from accessing the page
- Crawler-specific configuration issues have accidentally been set up

#### How to Fix a 401 Unauthorized Error in Google Search Console

- **Check authentication settings.** If the page requires authentication (for example, you need to log in to view the content), review the authentication settings to make sure they’re correctly configured.
- **Test access.** Manually test access to the affected pages by attempting to access them through a web browser or using tools like the Fetch as Google feature in Google Search Console. This can help identify any issues with access.
- **Review access restrictions.** Check for any IP-blocking or access restrictions on your server or website. Ensure that Googlebot's IP addresses are not blocked and the necessary permissions are in place for crawling.
- **Verify user agent access.** Confirm that your website's configuration allows access to common search engine user agents, including Googlebot. If there are rules limiting access to certain user agents, ensure that they are appropriately configured.

After addressing the unauthorized access issue, use Google Search Console to request a recrawl of the affected pages.

#### Soft 404 Errors

Soft 404 errors in Google Search Console occur when a page looks like a normal page (returns a 200 status code) but the content or certain signals on the page indicate that it should be treated as if it doesn't exist.

!["Soft 404" error in Google Search Console](https://static.semrush.com/blog/uploads/media/1a/bf/1abf9fe72d2f9911784fb8a11603c6ac/74dcedebe8a8252ff20a173d11b82fa7/YBA5ySpwDar503fq3mhQ2r0ZHEsdKF2autmVkjf8XC_hyNFbZ4kC-8hk0Bvk38_NcczaCvyx7_W2GVpbfLcQBp0jbfp-pHo8lW5K0nvU-WqDFz0jdPsCIXCWOrPye9U-kMUg2tD4hPgitacbssBCNfU.jpeg)

This can be confusing for search engines like Google. And it can impact how your pages are indexed and displayed in search results. Google Search Console flags them as errors.

Common scenarios leading to soft 404 errors include:

- **Empty pages**: Pages that are empty or contain very little content might trigger soft 404 errors. While the server returns a "200 OK" status code, the lack of content suggests the page isn’t providing meaningful information to users.
- **Redirected pages**: If a page is redirected to another URL, but the content on the destination URL is thin or not relevant, Google might interpret it as a soft 404
- **Custom error pages**: If your website has a custom error page showing the user an error message—even though it has a “200” OK” status code—this may trigger soft 404 errors

#### How to Fix a Soft 404 Error in Google Search Console

- **Review page content.** Examine the content of the pages flagged as soft 404 errors. Ensure that they provide meaningful information to users. If the content is insufficient, consider improving it or redirecting users to a more relevant page.
- **Verify redirects.** If a page is being redirected, make sure the destination URL contains relevant content. Avoid redirecting users to pages that don't relate to the content of the original page.
- **Check custom error pages.** If your website uses custom error pages, ensure that they provide helpful information and are not mistaken for empty or irrelevant content.

### Redirect Errors

Redirects send users and search engine crawlers from one URL to another.

For example, if a page no longer exists, you can place a redirect to automatically take visitors to a related page that **does** exist.

Redirect errors occur when a redirect fails for some reason. These errors can negatively impact how search engines like Google crawl, index, and rank your website.

!["Page with redirect" error in Google Search Console](https://static.semrush.com/blog/uploads/media/fc/2c/fc2c544b17567e44c85cbf9d0d23e875/e6e167ff07af06111a3933a69d0292f2/YOplMHcyG16fDG2RFfzqvpwQW97-0qjDZOocUT-sU3n0dcDD8Av1S8vIy2PKC2yLSmu-5G9cEPzzUZ-kTb0r-GTeKBmyCt-wPmq8nYuu9mF68lxKuCt8mKZhYzcuFM8FjA3um2hK4aoQW2bUYhDeXY8.jpeg)

Common redirect errors include:

- **Redirect chains**: This is when one URL redirects to another, and then that second URL redirects to a third, forming a sequence of redirects. Redirect chains can slow down the loading of pages and negatively impact user experience and search engine crawling efficiency.
- **Redirect loops**: These happen when the final destination URL redirects back to a previous URL in the chain. This can cause an infinite loop of redirects, preventing the page from loading and leading to crawl errors.
- **Incorrect redirects**: If a page is redirected to an incorrect or irrelevant URL, it can lead to a redirect error. Redirects should be set up accurately and lead users and search engines to a relevant destination URL.

### How to Fix a Redirect Error in Google Search Console

Identify any redirect errors in Google Search Console by visiting the “**Pages**” report. Scroll down to see “Why pages aren’t indexed.”

- **Analyze redirect chains.** If redirect chains are identified, review and simplify them. Ideally, a redirect should lead directly to the final destination without unnecessary intermediary steps.
- **Fix redirect loops.** If redirect loops are detected, identify the source of the loop and correct the redirect configurations to break the loop. Ensure that the final destination URL is correct.
- **Check redirect targets.** Verify that the URLs to which pages are redirected are accurate and relevant. Incorrect redirects can confuse users and search engines.
- **Update internal links.** If you've changed URLs and implemented redirects, update internal links on your site to point directly to the new URLs, reducing the need for redirects.
- **Use proper redirect status codes.** When implementing redirects, use appropriate HTTP status codes. For example, a 301 redirect indicates a permanent move, while a 302 redirect signals a temporary move.

## Crawl and Indexation Issues

Crawl and indexation issues happen when Google’s crawlers can’t reach a page they should be able to. Or when something’s stopping them from adding a page to their index.

You can check for these issues in the “**Pages**” report.

Open the report and scroll down to the table “Why pages aren’t indexed.”

You might encounter the following issues.

### Blocked by Robots.txt

If a page is blocked by robots.txt, this might be an issue. But only if you don’t want that page to be blocked. Some pages are blocked intentionally.

!["Blocked by robots.txt" error in Google Search Console](https://static.semrush.com/blog/uploads/media/7e/02/7e02fb69f0bdada79425ac0cf41acf31/b7be562ff49a592fd6b971e583f3a0e6/oDhj-FnHU9dzPUceDrLgAEB6wx3nVClHla5JKOekEUZL07eHZbWIlMhiXF6bU9j1tIsoOiuEVunPdWTEN6ENRT9qa1NxmAOo3Gm5fqK5fkh5G-urfCIp_FNPucjgeRTCkAafFUxt-rrl1jTWnEOiTOQ.jpeg)

Robots.txt is a file that sits on your website and contains instructions for search engine crawlers. It’s usually the first page they visit on your website.

You can include instructions in the robots.txt file to tell search bots not to crawl certain pages. For example, admin pages that aren’t accessible without a login.

You do this using a “disallow” directive.

![A “disallow” directive in robots.txt file](https://static.semrush.com/blog/uploads/media/83/f0/83f09ddd0342a2b428bc0e6ccb6a5099/3abf5d67d73651079e0006aec639cde0/7Wls3tr7AFOzEf66kJQ3IyTwWTpsAFsI_jApB6Tcs_wJOtKi9j4zwsJH1anlOXLE1YiFxnMWsSmonnS-Ob2sXPUfk9EX2y9WiGoW2dhS30k88daISiAIiY7nPiOOY-179aIs7onRTg9Wr82BaXvasr8.png)

However, it’s possible a page can be blocked by robots.txt by mistake.

In Google Search Console, if you see a page that says “blocked by robots.txt,” but you want Google to crawl that page, you can edit the robots.txt file. Then, use Google Search Console to request a recrawl of the affected pages.

### How to Fix Pages Blocked by Robots.txt

Get a free [SEO audit](https://www.semrush.com/siteaudit/) for a quick read on your site. To review and fix any issues with your robots.txt file across your full site, use Semrush Site Audit.

Open the tool and click “**+ Create project**.”

!["+ Create project" button in Site Audit tool](https://static.semrush.com/blog/uploads/media/f6/9d/f69db4e86eaf67d4e94a6fa77a670e07/020fff1a4799671f4c948a46111dd5ea/GGCko0HRFOxcwiiH51Q7cy-1N1SJISWDc8nxOFr5WsqZVwtEQG3zmAWiaV9ZCyQj86ScSgEOTxVXSMO9mLACdqn_PNlIqZFWNRHq4dIG1SX7FKltujThLnvaVde5z4GhCq82M67fwdzuPIwP68RgWWU.jpeg)

Enter your website domain. If you like, you can also give the project a name.

Click the “**Create project**” button.

!["Create project! window in Site Audit tool](https://static.semrush.com/blog/uploads/media/2d/39/2d397c3601bbc1499b4d35f7abdd5e79/c104cc8541d21444f59563e436eecec1/Sv8m2Y1PC5LX_aYHMArTiWs8CpkIoDdLLevJ4pk_JIfDFJe0rYKJWVJYiSAcL_NlH6T1jkl_7_zm73c5mpfmXwtjbJDCu2ueq6k0SBGJLLFPxkl5WrTPsKdRlbmOZr1jhZZBnmHGB0Stz4GfFlANhxw.png)

Configure any additional settings you’d like for the site audit. Then click “**Start Site Audit**.”

!["Site Audit Settings" window](https://static.semrush.com/blog/uploads/media/fd/32/fd32eb9e2e90316a5f295ac560d6c551/78d471701ea45fabbe4e6281ac826536/xEV7bn8LQeXenN-31XXJhmMS88Ifde_SWBzwpSoQjsWh7F-z6UHFI8zZZ7hWe7rJOfeXA3E1T_vC89Lknwn8UiD1eehblIlSeXHIhxN4it1wElnVmw2ePWiFe_N0zOaOFnWMJmkiDzRao1wnWW9FNzo.jpeg)

Once the audit is complete, go to the "**Issues**" tab and search for "robots.txt."

![Results for "robots.txt" under the "Issues" tab in Site Audit tool](https://static.semrush.com/blog/uploads/media/01/1a/011a9bbced87292e3c18b373bdfa5f48/c1edc528fc0f39cb7f7103b30ee2b484/Nq7AlSmul22ZzbJM7OtUYmtDYrW4rvIS5NRVYOszLRrcn0efcHIf5Xsy5nv6QBF15u2_kcEEk5NUTXLUuqW2MgcyqYEPO00bULZZ4UH2B0-fJKw_yER4UPP7aJLpP7kdmbOgcl76WZc9t1ToxsHFyNk.jpeg)

Click on any issues related to your robots.txt file, such as "Robots.txt file has format errors."

!["Robots.txt file has format errors" issue in Site Audit tool](https://static.semrush.com/blog/uploads/media/7f/5a/7f5aee27ad845c05cb0a53fa3fecf027/0f0bcf3f0055b5fb8a31386eeab9cd3d/xcK6MDXRb1jFTW7IPHpBCX1XEgd_jAmK-utiaa4uf7GeC09utYBtiWGzZM5IIa0QK7Zfe5kwTb07R5u0yVv1PSifj9ZeIivgeylRGGERbXFEjc3Y0ik2dJZ35QHFqNSxXSUJ7kC4hjT69eRoL2EDnnA.jpeg)

A list of invalid lines in the file will be displayed.

Click on "**Why and how to fix it**" to get specific instructions on how to resolve the error.

!["Why and how to fix it" window for robots.txt file in Site Audit tool](https://static.semrush.com/blog/uploads/media/68/45/6845f3adf45966a3348fd1f5704ecaeb/49f1e9a7c1c86f2fd1f517d566f9ab5c/QKrD60R-uS-zvzsSdi5xYQMjIzFaCfvmxNfF_xQpiVuX1rq6_Co-svLdgeot8_o6thlJqqG6YZD7q8xhlt3kGBTBUa7NkJJOZHpyLynlAv5Lk3YXXJSK0qzy8cttB4fDaj9Z2hOWTlyH5bXVnrb_jJg.jpeg)

## User Experience and Usability Issues

Website issues that cause poor user experiences are troubling for two reasons.

First, you don’t want visitors to your site to have poor experiences. It causes distrust in your brand. And it lowers the chances that person will interact with your content again.

Poor user experiences are also bad because positive user experiences are an important ranking factor for Google Search. Pages with poor user experiences will not do as well in the search results.

### Core Web Vitals Issues

Core Web Vitals are a set of user-centered metrics that measure the loading performance, interactivity, and visual stability of a page.

Essentially, Core Web Vitals measure how fast and pleasant a website is to use.

The three main metrics are:

- **Largest Contentful Paint (LCP)**: The time it takes for the largest content element (such as an image or a block of text) to become visible on the user’s screen
- **Interaction to Next Paint (INP)**: How well the webpage responds to user interactions
- **Cumulative Layout Shift (CLS)**: How many times the page shifts around as it loads

Google Search Console flags when you have Core Web Vitals performance issues.

![Core Web Vitals performance issues in GSC](https://static.semrush.com/blog/uploads/media/8d/f3/8df31420cb46dd238d11dd2bfbff0659/c5e0e6dd4d28ea6e9229a6928df4363a/XdXkvfiiJzZhDROgZeE7o-nIcjyYnSm3Z6pbj3KYqOLmH5aZYwjfgOzX1luhJAY3fczxHNFXxqEm5HPWVjOf2-mBPPQMbbh2aus7ZcKOlZNBvOK1LbRDCRuZr1a_CJI7_1yHb-AkaPPv5Z6V4Z14Vb0.jpeg)

You can identify these issues using the [website audit](https://www.semrush.com/siteaudit//) tool. And get tips on how to fix them.

### How to Fix Core Web Vitals Issues

Open [Site Audit](https://www.semrush.com/siteaudit//). Either choose an existing project or click “**+ Create project**.”

!["+ Create project" button in Site Audit tool](https://static.semrush.com/blog/uploads/media/e5/f3/e5f3d11b9dc279c673cb8e476b0298ae/2bfdcf8350e7138db0398e5bbb442747/aIHTghuxnOwhoOtCi-TmNtTxZQCUHUChDAQGP8mn1J0GOdclErMlS0loOD8VDTe2I1FPK-tusyhNHnAgHRsc0u-TpK2KslpE9G_hfGdrdjmCZU3X82NSSR59qLHuR9hDvBxPQxscgGXlkd5KBf5lYAY.jpeg)

Configure the settings and click “**Start Site Audit**.”

!["Site Audit Settings" window](https://static.semrush.com/blog/uploads/media/d7/3d/d73db57b3551ca0dcb96402c91c4fdb0/f2f75b7601783b5c94c3d087a64c8cdc/5hzMW3dll0GdTA1bLHwTUhn4kXD0RIP-HsGA5BmkU3H519Z3f0G2UhCYVu3WvKfjH2iH_WTdPZMYPaByFzBsA2SAuj0J54BJPKcVmj39BwcgQaDrzDQQgT9kXhw5sLJyzTGo3I_uO53W2azkgR9DIvk.jpeg)

In a few minutes, you’ll see your results.

In the “Overview” report, you’ll see a widget on the right called “Core Web Vitals.” Click “**View details**.”

!["Core Web Vitals" widget highlighted in Site Audit's overview dashboard](https://static.semrush.com/blog/uploads/media/f2/47/f247f24cdfa018c3f8b5eb9560e2d581/8cf1484c6170480790733e6eb4d2a1ed/qlwZ4OV2rgqTzHFwli4blQDoknhjD6TJkypM8mq6e808wEOoH3TqpH3VUGSpcvNZG6-PsfF1R9YfQfnoy2c4SkV8Dr1DVfJGfSmS6En3UBTNHL1-WCcx-NNOr3DtV_sJD-LwSvWMXWGu_TKpmHFRtr4.png)

You’ll see your performance against Core Web Vitals metrics for 10 pages on your site.

![Core Web Vitals performance report in Site Audit tool](https://static.semrush.com/blog/uploads/media/1e/f2/1ef2e7ff40e2b8cf57599ab425082e72/b0e702dac8ed58724173b63fe97d2b70/DUYWFZ5QSTvWS4AkRfQIwyfl-DCn-6reVxctOqNvk2IFb-R5f25HSh8Ia9S3zxDnuSU4YwNSqfJbzB9EaaqTNZRrcoi3GosgNNYfKY6SlfnwlQKHsVEYeNEGjYX2-1AKK4V6D2nJpCI4jmIf7SQ4u9Q.jpeg)

Scroll down to “Metrics” and you can see the performance broken down into the three Core Web Vitals.

Underneath each one, there’s a list titled “Top improvements” with suggestions to improve your performance in that area.

### HTTPS Errors in Google Search Console

Google favors sites with an SSL certificate. This is a security certificate that encrypts data sent between a website and a browser.

Once you have an SSL certificate, all pages on your website should begin with “https://.”

Any pages starting instead with “http://” could indicate security issues to search engines. So it’s best to fix them when they appear.

Open Google Search Console and click “HTTPS” in the left-hand menu.

![“HTTPS” highlighted in the GSC menu](https://static.semrush.com/blog/uploads/media/22/c2/22c2046887284e196b1b805cd2d296e7/272e4dc8b07a8845cb8348722b2ac012/0e97pf_-KFrDgXhhf1W_fFWtKZa_ml7GAkEV14vIidfZUfgKJXhrVdNGIukE-RTPI6Gzgb_QhCDkwHmS_DMTadyIlE1d1WlJ4A1oHTD2KJ99cg-bDkw3XiGjzfRxTJ5kkBxFaLn7cwlkhYNo18-nzlQ.jpeg)

The table will show if you have any non-HTTPS URLs on your site.

![Non-HTTPS URLs showing 0 in GSC](https://static.semrush.com/blog/uploads/media/d6/57/d657ac1750c49bdfdc2b4d4ef160c08c/27a0eb15945572e71a6d5ddee457ccac/eNBIL031Xlch7vUTytISLE5MSNHhgzCleeies2WmaHY0WLo_8nQg5ttxo0oWrFtKzYImGGuRIQ03Thp5yqjmG-LrPshMtt3hwPViALA-UBIk7kgTufIR1ggInRFpyMlvCRE_TZ21FGWWgg_Xfot8eyc.jpeg)

### How to Fix HTTPS Errors in Google Search Console

If you have HTTPS errors, scroll down on that HTTPS page in Google Search Console. You’ll see a table called “Why pages are not being served over HTTPS.”

Click on the issue row to see which URLs are affected.

!["HTTPS not evaluated" error in Google Search Console](https://static.semrush.com/blog/uploads/media/2e/27/2e27842c047b53b1ea5869df42afc60f/b5c181ab603a109a857ae00a16079e5c/E4e4-2r5cA9nvorzpkXyCDeipY-w_uScEZq9o6tBRCGgRjk2-CPkGEUydboNOp4r3cy5TKFqE6xNuxXxHsOsMSsrT1Fyc3a97Fi28GvNSx4ZssOqZO66vgS5NXsT3RwpaCdh8tFwvg1F5IuZEBetsGY.png)

Once you see the list of URLs, you can remove any links to these pages from your website and ask Google Search Console to recrawl your site.

## Manual Actions in Google Search Console

Manual actions in Google Search Console refer to penalties imposed on a website by human reviewers who work at Google. When these reviewers identify violations of Google's guidelines, they may take manual actions to penalize the site.

Manual actions are different to algorithmic penalties, which are automatically applied by Google's algorithms.

Common reasons for manual actions include:

- **Unnatural linking**: If a site is involved in link schemes, has purchased links, or participates in link exchanges that violate Google's guidelines, it may receive a manual action
- **Thin or duplicate content**: Websites with low-quality or duplicate content may face manual actions for violating content quality guidelines
- **Cloaking or sneaky redirects**: If a site shows different content to users and search engines or uses deceptive redirects, it may receive a manual action
- **Spammy structured markup**: Incorrect use of structured data markup (schema.org) to manipulate search results can lead to manual actions
- **User-generated spam**: Websites that allow users to generate content (comments, forums) may face manual actions if they fail to moderate and control spam effectively
- **Hacked content**: If a site is compromised and contains harmful or irrelevant content, Google may take manual action to protect users

If a manual action is imposed, you’ll be notified through Google Search Console.

![Manual actions in Google Search Console](https://static.semrush.com/blog/uploads/media/c0/ea/c0eafc8d2cc7bdc7c5c5c5d294c634e5/093471a7976bb3de7d5ec81c18107a1a/yOOt1lbklttvSw2KEJsCEC_SA_dkqnZYSwLIYoZbTHpJtN3q-s2uO0pBWF5VKZ5f9vnUQ3TU6V7SrFEAfExbFwXR1ofrHQaievvbMfCELoEl9cRdXA67BkyvWG8-P_9KsonwokTZdO4J0yvjOMLhBik.png)

**Image Source**: [Google](https://support.google.com/webmasters/thread/7879895/regarding-manual-actions-in-search-console?hl=en)

The notification will give you details about the issue. As well as guidance on how to fix it and steps for requesting a review after corrections are made.

Once you’ve fixed the issue, enter the issue in Google Search Console and click “**Request review**.”

If you’ve properly fixed the issue, the team at Google will mark it as resolved and penalties may be lifted.

### Security Issues in Google Search Console

When security issues are identified, they can negatively impact your site's search visibility. Plus, Google may label your site as potentially harmful to users.

The Security Issues Report in Google Search Console provides information about potential security threats or issues detected on your website.

Common security issues reported in Google Search Console include:

- **Malware infections**: Google may detect malware on your site, indicating that it’s been compromised. And there’s malicious software that could harm visitors.
- **Hacked content**: If your website has been hacked, attackers may inject unwanted content or links. Google will alert you if hacked content is detected.
- **Social engineering**: Google identifies instances where your site may be involved in social engineering attacks, such as phishing or deceptive practices

### Steps to Address Security Issues:

Use Google Search Console to view and fix any security issues.

Open Google Search Console. Navigate to the Security & Manual Actions section on the left-hand side of the screen. Click on “**Security issues**.”

!["Security issues" in Google Search Console](https://static.semrush.com/blog/uploads/media/95/9d/959d2f5774eee1427e0833bce43db4d4/2343556e216f4e69caf2a2e27a38af56/5Z_KYvwvbFAtp50R68Z9fgx7LRTY7RVugR6cmGEnUrGKS0gxjtk7vESi7da2XWJZ37vkaxRuSAa0LvKvPFzxYDt-dTOwzW9SFIMLUzynB6d_S77LJWugRJwxgdm88DITvjabdup9zdKKSpL9IzazED8.png)

If there are any flagged issues, you’ll see them here.

Google will provide information about the type of security issues detected. As well as recommendations or actions to resolve the problems.

If malware or hacked content is detected, clean and secure your website. Remove any malicious code, update passwords, and implement additional security measures.

After resolving the security issues, submit your site for a review through Google Search Console. Google will assess whether the issues have been adequately addressed.

## Preventing Google Search Console Errors

Follow these best practices to stop Google Search Console errors from happening.

- **Run regular site audits.** Conduct regular audits of your website to identify and address technical issues promptly.
- **Keep your XML sitemap up to date.** Ensure your website has an XML sitemap that includes all relevant pages. Submit the sitemap to search engines via Google Search Console to facilitate crawling and indexing.
- **Optimize your robots.txt file.** Use a well-constructed robots.txt file to control which parts of your site should be crawled by search engines. Regularly review and update this file.
- **Make sure you have a valid SSL certificate.** Ensure your website has a valid SSL certificate, providing a secure connection (HTTPS). Google favors secure sites, and it positively impacts rankings.
- **Optimize images.** Optimize images for faster loading. Use descriptive file names and include alt text for accessibility and SEO.
- **Use a strong URL structure.** Keep URLs simple, descriptive, and user-friendly. Avoid using complex URL parameters when possible.

Semrush tools help you stay on top of your website’s technical SEO performance. With them, you can catch issues before they escalate.

Use the [website SEO checker](https://www.semrush.com/siteaudit//) to learn about any current issues with your site. And how to fix them.

Plus, you’ll receive automatic emails the moment a potential new issue arises. So you’re always on top of your SEO performance.
