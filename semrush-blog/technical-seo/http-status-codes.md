---
title: "HTTP Status Codes Explained: Full List & Impact on SEO"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "http-status-codes"
url: "https://www.semrush.com/blog/http-status-codes/"
canonical: "https://www.semrush.com/blog/http-status-codes/"
author: "Carlos Silva, Christine Skopec"
published: "2021-03-22T15:00:00+00:00"
updated: "2025-07-08T08:52:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T16:58:27+00:00"
status_code: 200
html_hash: "2fd35aec11e1da8ad28a3053134fa8e10cafc70a30c041d748e4e2dc11814d4b"
clean_word_count: 2219
clean_char_count: 14576
---
# HTTP Status Codes Explained: Full List & Impact on SEO

## What Are HTTP Status Codes?

HTTP status codes are three-digit numbers servers generate in response to a client (e.g., a browser) request. They indicate whether the request was completed successfully.

For example, a 404 error is a common HTTP status code you might have seen.

![A URL returns a 404 error page.](https://static.semrush.com/blog/uploads/media/81/c2/81c2c9105fe4a38571c5291d60299a69/82d45f4b44e16d95fc1551e16f38b6d9/AD_4nXcVEnCXbIk9M40jL80nMXv4Z-6IzP5icb4e-yjcmbjgz37gPymIwW6ympon2pdzCbhaANz3VqXJUoDUDDsB4qJRKuGODrLfcVNTJYG0kK5tDWpwnzNbJNRWLEy2MT6NJf3Qnts9sw.png)

If you’re a website owner, HTTP status codes give you important information for improving your website’s functionality and user experience. And they can impact your SEO.

## Categories of HTTP Status Codes

There are five categories of HTTP status codes:

- **1XX (informational codes)**: The server received the request and is processing it
- **2XX (success codes)**: The server successfully received and processed the request
- **3XX (redirection codes)**:The server received the request, but there’s a redirect to another destination ([301 or 302](https://www.semrush.com/blog/301-vs-302-redirect/) are common)
- **4XX (client error codes)**:The requested resource couldn’t be found or reached due to a client error
- **5XX (server error codes)**: The server ran into an error when processing the request

## A Complete List of HTTP Status Codes

|  |  |
| --- | --- |
| **Code** | **Meaning** |
| **1XX: Informational Responses** | |
| 100: Continue | The server has received the initial request and is ready for the client to send the rest if it hasn’t already |
| 101: Switching protocols | The server agrees to accept the client’s request to change to a different protocol |
| 102: Processing | The server has received the request but hasn’t completed it. This code has been deprecated. |
| 103: Early hints | The server sends hints about the expected final response while the response is still being processed |
| **2XX: Success Codes** | |
| 200: OK | The request was successful. The specific response depends on the request method (GET, PUT, etc.). |
| 201: Created | The request worked, so a new resource was created |
| 202: Accepted | The request was accepted but hasn’t been processed |
| 203: Non-authoritative information | The data returned is from a third party rather than from the original server |
| 204: No content | The request was successful, but there's no content |
| 205: Reset content | The request was successful, and the user agent (e.g., browser) should reset the document |
| 206: Partial content | The server is only sending part of the requested resource |
| 207: Multi status | Provides the statuses of multiple operations within a single response |
| 208: Already reported | Tells the client that a resource’s information has already been included earlier in the response and won’t be repeated |
| 226: IM used (HTTP delta encoding) | The server successfully handled the request and returned a version of the resource that includes only the changes—not the full resource |
| **3XX: Redirection Codes** | |
| 300: Multiple choices | Indicates there are multiple possible responses, and the user or client needs to choose one |
| 301: Moved permanently | The resource has permanently moved to a new web address. The server provides the new URL. |
| 302: Found | The resource has temporarily moved to a different web address. But it might move again. |
| 303: See other | The server is telling the client to get the resource from another location using a standard GET request |
| 304: Not modified | The response hasn’t changed, so the client can keep using the cached version |
| 305: Use proxy | Indicates the client should use a proxy to access the resource. This code has been deprecated. |
| 307: Temporary redirect | The resource has temporarily moved, and the client should use the same HTTP method (e.g., POST) as in the previous request |
| 308: Permanent redirect | The resource has permanently moved, and the client must use the same HTTP method as in the previous request |
| **4XX: Client Error Codes** | |
| 400: Bad request | The server can’t process the request because of a client error |
| 401: Unauthorized | The client doesn’t have the proper credentials to access the resource |
| 402: Payment required | Originally meant to indicate the requested resource requires payment, but it’s rarely used and doesn’t have a standard purpose |
| 403: Forbidden | The client isn’t authorized to access the resource, even though the server knows the client’s identity |
| 404: Not found | The server can’t find the resource. Often because a browser is requesting an incorrect URL or the content no longer exists. |
| 405: Method not allowed | The request method (e.g., GET) isn’t allowed for the specified resource |
| 406: Not acceptable | The server can’t provide a response in any format the client specified |
| 407: Proxy authentication required | A proxy server needs to authenticate the client before the request can be processed |
| 408: Request timeout | The server gave up waiting because the client didn’t complete the request fast enough |
| 409: Conflict | The request conflicts with what’s already on the server (e.g., two people editing the same content at the same time) |
| 410: Gone | The requested resource has been permanently deleted. And there’s no forwarding address. |
| 411: Length required | The server didn’t accept the request because it didn’t specify how much data is being sent |
| 412: Precondition failed | A condition set in the request wasn’t met, so the server didn’t process it |
| 413: Content too large | The amount of data the client is sending is too big for the server to handle |
| 414: URI too long | The requested web address is too long for the server to manage |
| 415: Unsupported media type | The server doesn’t support the format the request is using |
| 416: Range not satisfiable | The requested part of a resource isn’t within the server’s available range |
| 417: Expectation failed | The server couldn’t meet a requirement specified in the request |
| 421: Misdirected request | The request went to the wrong server—one that isn’t set up to handle it |
| 422: Unprocessable content | The server understands the request format but is unable to process it because of issues with the actual data (e.g., wrong values) |
| 423: Locked | The requested resource is locked and inaccessible |
| 424: Failed dependency | The request failed because a related request also failed |
| 425: Too early | The server didn’t process the request because it was too early and might be replayed |
| 426: Upgrade required | The server won’t process the request unless the client switches to a newer or different protocol (like HTTPS) |
| 428: Precondition required | The server requires the request to include certain conditions to ensure safe updates |
| 429: Too many requests | The user sent too many requests too quickly |
| 431: Request header fields too large | The request headers contain too much information for the server to process |
| 451: Unavailable for legal reasons | The requested resource is blocked due to legal reasons |
| **5XX: Server Error Codes** | |
| 500: Internal server error | The server encountered an error and couldn’t complete the request |
| 501: Not implemented | The server doesn’t support the request method |
| 502: Bad gateway | The gateway server received an invalid or no response from another server |
| 503: Service unavailable | The server is temporarily unavailable—usually because it’s down for maintenance or overloaded |
| 504: Gateway timeout | The gateway server didn’t get a response from another server in time |
| 505: HTTP version not supported | The server doesn’t support the HTTP version used in the request |
| 506: Variant also negotiates | A misconfiguration caused the server to get stuck in a loop when trying to choose between different versions of the resource |
| 507: Insufficient storage | The server doesn’t have enough space to save or process the request |
| 508: Loop detected | The server detects an endless loop while trying to process the request |
| 510: Not extended | The request is missing extensions the server requires for processing |
| 511: Network authentication required | The client needs to authenticate to gain network access |

## How to Check a Webpage’s HTTP Status Codes

You can easily check a page’s HTTP status codes using Google Chrome.

Go to the webpage you want to check.

Right-click anywhere on the page and select "**Inspect**” to open the Developer Tools. Or press “Ctrl + Shift + I” (Windows/Linux) or “Cmd + Option + I” (Mac).

![Inspect is highlighted in the right-click menu.](https://static.semrush.com/blog/uploads/media/aa/95/aa9516794d12beb900e226bb0fb0fc79/78f5eebd4d8269f38693b57673bc7e38/AD_4nXdrNGDyEzSOTjveTyCw_QxYjqy3Aad-8yqFRvpJs98mXQLIvNmlsl8EtPvQENQ-AyJ2rLhE4D0JomkOqjDUDMPUbobdVsFs5cDnTRs-20l4sIU7aSrzSCe3QChhDXLaV1AMU7hraQ.png)

Click on the "**Network**" tab in the Developer Tools panel.

Refresh the page (select “F5” or “Ctrl + R”).

Look at the list of network requests.

The “Status” column shows you a list of HTTP status codes for the page. The first one in the list is the page’s HTML document.

![The HTTP status code column is highlighted in the tool.](https://static.semrush.com/blog/uploads/media/2a/22/2a22a56d8b6c659776b8bf12a272d924/3eeb364f2e438db8ab62548f45bfb22c/AD_4nXcZbfMoZNBijFOVMj_GwvET-D_u-yodoNwDsX7qaXYXoDDrTh1o4lAvsCviVWBsMHxpAK8CDVNXjbewzGU2IeqWxXDHVl-pl2LP1gdAnSQFPpHho8frx2vE0DmY92Hkq04RNDe7.png)

It’s also a good idea to audit your site for HTTP status code errors. You can do this easily in Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool.

Simply run a crawl and click on “**Crawled Pages**.”

The “Status” column will show you the status code of each page so you can see if there are any errors that need fixing.

![The HTTP status code column is highlighted for the list of crawled pages.](https://static.semrush.com/blog/uploads/media/ff/21/ff2149146cfd67bb8902fde8055d560e/8581ed3ddd72f1210e56481eb2238b22/AD_4nXcS7lMhybffl42RA8Bzo-ylta5HGeujc6ElsQDnn-YIPzd7vqozZV5Ib3Cdu4t-gPmM3CCK2QhFqstF0J-ev5jpjVUQoknGxxb9M8bTs9nYc-uw13SnDimG-lI5D03LgFNL-IQt.png)

## The Implications of Common HTTP Status Codes for SEO

Here’s what some of the most common status codes mean for your SEO:

### 200 (OK)

A 200 response code is what you’ll want most of your webpages to return.

It indicates that a webpage works and is accessible to both people and search engines.

### 301 (Moved Permanently)

A [301 code](https://www.semrush.com/blog/301-redirects/) means you’ve permanently moved a page to a new URL. And signals to Google that the old URL in its index should be replaced with the new one.

Importantly, a 301 redirect also transfers link equity from the old page to the new one. Which preserves your visibility.

![Two webpages link to the same page. These links pass link equity to that page and its 301 redirected page.](https://static.semrush.com/blog/uploads/media/bc/26/bc26230ee334d04c563cb51df4084779/9434b30f663eec6b32691af1a5ac0d03/AD_4nXcMj88QqFzbw4c-FIIy3n8G6cIavzBTDSLBL_qy4ODOaN6B9xne_K1SPqMYarRPT8gIG65cBUXOKKYBEZAWmT02T2xunhfveHf21cdTkTZkPXU46saTVu9iMKOvjrMW1JXqmc-65Q.png)

### 302 (Found/Temporary Redirect)

A [302 redirect](https://www.semrush.com/blog/302-redirect/) is a temporary redirect. It can preserve links and rankings while a webpage is temporarily unavailable.

For example, if you’re doing website maintenance and want to send users to a temporary holding page. Or you’re carrying out A/B testing.

If a 302 redirect is in place for a long time, Google may start treating it as a 301 redirect. Meaning the old URL will be replaced by the new one in Google’s index.

### 404 (Not Found) and 410 (Gone)

Both 404 and 410 status codes tell search engines that a page no longer exists, which typically leads to it being removed from the index.

While both ultimately lead to deindexing, a 410 more clearly communicates that the page is gone for good. This can speed up its removalfrom search engine indexes.

### 5XX (Server Errors)

Search engines have trouble accessing pages with 5XX errors, which can lead to problems with crawling, indexing, and the user experience.

Over time, this can negatively impact visibility in search results. So it’s important to monitor and resolve 5XX errors promptly.

## The Impact of HTTP Status Codes on LLMs

It’s important to make sure your content’s accessible to tools built on large language models (LLMs), like Google’s AI Overviews, ChatGPT, Perplexity, and Claude. Because it’ll help you gain more visibility in those AI responses.

Status codes that signal errors—like 404s and 500s—can block LLMs from seeing your content. Because LLMs find and understand website content similar to traditional search engines.

Web developer and AI engineer [Vincent Schmalbach](https://www.linkedin.com/in/vschmalbach/) notes:

> “Sites with frequent HTTP status code errors may find their content underrepresented in both search results and AI-generated responses, since both systems require reliable access to index and utilize content effectively.”

Vincent adds the following when talking specifically about 4XX and 5XX status codes:

> “Both 404 and 410 responses mean no content is available, so those pages don't contribute to training data. Server errors like 500s cause crawlers to retry later, but persistent errors result in content being skipped entirely.”

[Toby Basalla](https://www.linkedin.com/in/toby-basalla/), Founder and Principal Data Consultant at data analytics consultancy Synthelize, warns that a website with unintentional redirect status codes can skew data used to train the actual models if it's scraped all at once. Because those mistakes are difficult to spot among so much data.

He reflects on a notable experience running a custom-trained LLM that relied on a scraped dataset:

> “In one case, a client had 180 landing pages misflagged as temporary redirects, and none of it made it into our scraped dataset. Which means, in effect, those pages did not exist to the model.”

## Check Your Website for HTTP Status Code Errors

You should check your website’s HTTP status codes regularly to stay on top of any errors.

Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool makes it easy to identify any of these problems. So you can swiftly address issues and boost your SEO performance.
