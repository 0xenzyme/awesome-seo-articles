---
title: "HTTP Status Codes & Their SEO Impact"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "http-status-codes"
url: "https://ahrefs.com/blog/http-status-codes/"
canonical: "https://ahrefs.com/blog/http-status-codes/"
author: "Patrick Stox"
published: "2022-01-18T23:33:09+00:00"
updated: "2025-06-03T23:52:29+00:00"
categories:
  - "General SEO"
freshness_reasons: []
fetched_at: "2026-06-12T11:40:45+00:00"
status_code: 200
html_hash: "9c7e4ba9abdd7534e956398181d10f7cb49ac57975607d0561905b0d7e79b87b"
clean_word_count: 2516
clean_char_count: 15481
---
# HTTP Status Codes & Their SEO Impact

HTTP status codes are three-digit numbers included in the server response to let a browser know if its request has been successfully completed. Along with the three-digit number, they usually include a description of the status. Specifications and their functionality are defined by the World Wide Web Consortium (W3C).

The status codes are how your client and a server communicate with each other. You can view any page’s HTTP status codes for free using Ahrefs’ [SEO Toolbar](https://ahrefs.com/seo-toolbar) by clicking the toolbar icon.

You can also click and expand this to see the full header response, which helps with troubleshooting many technical issues.

There are five official ranges for the codes:

- [1xx – Informational](#1-1xxs-informational)
- [2xx – Request successful](#2-2xxs-request-successful)
- [3xx – Redirects](#3-3xxs-redirects)
- [4xx – Client errors](#4-4xxs-client-errors)
- [5xx – Server errors](#5-5xxs-server-errors)

You may see some higher codes. These are all unofficial:

- [6xx+ – Unofficial](#6-6xx-unofficial)

Keep reading to learn what the status codes mean and how Google handles them.

## 1xxs – Provide some kind of additional information

1xx status codes indicate the server has received the request and the processing will continue.

**100 Continue** – Everything is OK right now. Keep going.

**101 Switching Protocols** – There is a message, such as an upgrade request, that’s changing things to a different protocol.

**102 Processing** – Things are happening but are not done yet.

**103 Early Hints** – Lets you preload resources, which can help improve [Largest Contentful Paint](https://ahrefs.com/blog/largest-contentful-paint-lcp/) for [Core Web Vitals](https://ahrefs.com/blog/core-web-vitals/).

## 2xxs – Show that a request is successful

2xx status codes mean that a client request has been received, understood, and accepted.

**200 OK** – All good. Everything is successful.

**201 Created** – Similar to 200, but the measure of success is that a new resource has been created.

**202 Accepted** – A request has been accepted for processing, but it hasn’t been completed yet. It may not have even started yet.

**203 Non-Authoritative Information** – Something has changed after it was sent from the server to you.

**204 No Content** – The request has been sent, but there’s no content in the body.

**205 Reset Content** – Resets the document to the original state, e.g., clearing a form.

**206 Partial Content** – Only some of the content has been sent.

**207 Multi-Status** – There are more response codes that could be 2xx, 3xx, 4xx, or 5xx.

**208 Already Reported** – The client tells the server the same resource was mentioned earlier.

**218 This is fine** – Unofficial use by Apache.

**226 IM Used** – This allows the server to send changes (diffs) of resources to clients.

### How Google handles 2xx

Most 2xxs will allow pages to be indexed. However, 204s will be treated as [soft 404s](https://ahrefs.com/blog/what-is-soft-404/) and won’t be indexed.

Soft 404s may also be URLs where the server says it is successful (200), but the content of the page says it doesn’t exist. The code should have been a 404, but the server says everything is fine when it isn’t. This can also happen on pages with little or no content.

You can find these soft 404 errors in the Coverage report in Google Search Console.

## 3xxs – Related to redirects mostly but with few exceptions

3xx status codes indicate the client still needs to do something before the request can be successful.

**300 Multiple Choices** – There’s more than one possible response, and you may have to choose one of them.

**301 Moved Permanently** – The old resource now redirects to the new resource.

**302 Found** – The old resource now redirects to the new resource temporarily.

**302 Moved Temporarily** – The old resource now redirects to the new resource temporarily.

**303 See Other** – This is another redirect that indicates the resource may be found somewhere else.

**304 Not Modified** – Says the page hasn’t been modified. Typically used for caching.

**305 Use Proxy** – The requested resource is only available if you use a proxy.

**306 Switch Proxy** – Your next requests should use the proxy specified. This code is no longer used.

**307 Temporary Redirect** – Has the same functionality as a 302 redirect, except you can’t switch between POST and GET.

**307 HSTS Policy** – Forces the client to use HTTPS when making requests instead of HTTP.

**308 Permanent Redirect** – Has the same functionality as a 301 redirect, except you can’t switch between POST and GET.

### How Google handles 3xx

301s and 302s are [canonicalization signals](https://ahrefs.com/blog/canonicalization/). They pass [PageRank](https://ahrefs.com/blog/google-pagerank/) and help determine which URL is shown in Google’s index. A 301 consolidates forward to the new URL, and a 302 consolidates backward to the old URL. If a 302 is left in place long enough or if the URL it’s redirected to already exists, a 302 may be treated as a 301 and consolidated forward instead.

302s may also be used for redirecting users to language or country/language-specific homepages, but the same logic shouldn’t be used for deeper pages.

303s have an undefined treatment from Google. They may be treated as 301 or 302, depending on how they function.

A 307 has two different cases. In cases where it’s a temporary redirect, it will be treated the same as a 302 and attempt to consolidate backward. When web servers require clients to only use HTTPS connections (HSTS policy), Google won’t see the 307 because it’s cached in the browser. The initial hit (without cache) will have a server response code that’s likely a 301 or a 302. But your browser will show you a 307 for subsequent requests.

308s are treated the same as 301s and consolidate forward.

Google will follow up to 10 hops in a redirect chain. It typically follows five hops in one session and resumes where it left off in the next session. After this, signals may not consolidate to the redirected pages.

You can find these redirect chains in Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) or our free [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) (AWT).

## 4xxs – Errors on the client’s side

4xx status codes mean the client has an error. The error is usually explained in the response.

**400 Bad Request** – Something with the client request is wrong. It’s possibly malformed, invalid, or too large. And now the server can’t understand the request.

**401 Unauthorized** – The client hasn’t identified or verified itself when needed.

**402 Payment Required** – This doesn’t have an official use, and it’s reserved for the future for some kind of digital payment system. Some merchants use this for their own reasons, e.g., Shopify uses this when a store hasn’t paid its fees, and Stripe uses this for potentially fraudulent payments.

**403 Forbidden** – The client is known but doesn’t have access rights.

**404 Not Found** – The requested resource isn’t found.

**405 Method Not Allowed** – The request method used isn’t supported, e.g., a form needs to use POST but uses GET instead.

**406 Not Acceptable** – The accept header requested by the client can’t be fulfilled by the server.

**407 Proxy Authentication Required** – The authentication needs to be done via proxy.

**408 Request Timeout** – The server has timed out or decided to close the connection.

**409 Conflict** – The request conflicts with the state of the server.

**410 Gone** – Similar to a 404 where the request isn’t found, but this also says it won’t be available again.

**411 Length Required** – The request doesn’t contain a content-length field when it is required.

**412 Precondition Failed** – The client puts a condition on the request that the server doesn’t meet.

**413 Payload Too Large** – The request is larger than what the server allows.

**414 URI Too Long** – The URI requested is longer than the server allows.

**415 Unsupported Media Type** – The format requested isn’t supported by the server.

**416 Range Not Satisfiable** – The client asks for a portion of the file that can’t be supplied by the server, e.g., it asks for a part of the file beyond where the file actually ends.

**417 Expectation Failed** – The expectation indicated in the “Expect” request header can’t be met by the server.

**418 I’m a Teapot** – Happens when you try to brew coffee in a teapot. This started as an April Fool’s joke in 1998 but is actually standardized. With everything being smart devices these days, this could potentially be used.

**419 Page Expired** – Unofficial use by Laravel Framework.

**420 Method Failure** – Unofficial use by Spring Framework.

**420 Enhance Your Calm** – Unofficial use by Twitter.

**421 Misdirected Request** – The server that a request was sent to can’t respond to it.

**422 Unprocessable Entity** – There are semantic errors in the request.

**423 Locked** – The requested resource is locked.

**424 Failed Dependency** – This failure happens because it needs another request that also failed.

**425 Too Early** – The server is unwilling to process the request at this time because the request is likely to come again later.

**426 Upgrade Required** – The server refuses the request until the client uses a newer protocol. What needs to be upgraded is indicated in the “Upgrade” header.

**428 Precondition Required** – The server requires the request to be conditional.

**429 Too Many Requests** – This is a form of rate-limiting to protect the server because the client sent too many requests to the server too fast.

**430 Request Header Fields Too Large** – Unofficial use by Shopify.

**431 Request Header Fields Too Large** – The server won’t process the request because the header fields are too large.

**440 Login Time-out** – Unofficial use by IIS.

**444 No Response** – Unofficial use by nginx.

**449 Retry With** – Unofficial use by IIS.

**450 Blocked by Windows Parental Controls** – Unofficial use by Microsoft.

**451 Unavailable For Legal Reasons** – This is blocked for some kind of legal reason. You’ll see it sometimes with country-level blocks, e.g., blocked news or videos, due to privacy or licensing. You may see it for DMCA takedowns. The code itself is a reference to the novel Fahrenheit 451.

**451 Redirect** – Unofficial use by IIS.

**460** – Unofficial use by AWS Elastic Load Balancer.

**463** – Unofficial use by AWS Elastic Load Balancer.

**494 Request header too large** – Unofficial use by nginx.

**495 SSL Certificate Error** – Unofficial use by nginx.

**496 SSL Certificate Required** – Unofficial use by nginx.

**497 HTTP Request Sent to HTTPS Port** – Unofficial use by nginx.

**498 Invalid Token** – Unofficial use by Esri.

**499 Client Closed Request** – Unofficial use by nginx.

**499 Token Required** – Unofficial use by Esri.

### How Google handles 4xx

4xxs will cause pages to drop from the index.

404s and 410s have a similar treatment. Both drop pages from the index, but 410s are slightly faster. In practical applications, they’re roughly the same.

421s are used by Google to opt out of crawling with HTTP/2.

429s are a little special because they are generally treated as server errors and will cause Google to slow down crawling. But eventually, Google will drop these pages from the index as well.

You can find 4xx errors in [Site Audit](https://ahrefs.com/site-audit) or our free [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools).

Another thing you may want to check is if any of these 404 pages have links to them. If the links point to a 404 page, they don’t count for your website. More than likely, you just need to 301 redirect each of these pages to a relevant page.

Here’s how to find those opportunities:

1. Paste your domain into [Site Explorer](https://ahrefs.com/site-explorer) (also accessible for free in [AWT](https://ahrefs.com/webmaster-tools))
2. Go to the **Best by links** report
3. Add a “404 not found” HTTP response filter

I usually sort this by “Referring domains.”

## 5xxs – Errors on the server’s side

5xx status codes mean the server has an error, and it knows it can’t carry out the request. The response will contain a reason for the error.

**500 Internal Server Error** – The server encounters some kind of issue and doesn’t have a better or more specific error code.

**501 Not Implemented** – The request method isn’t supported by the server.

**502 Bad Gateway** – The server was in the middle of a request and used for routing. But it has received a bad response from the server it was routing to.

**503 Service Unavailable** – The server is overloaded or down for maintenance and can’t handle the request right now. It will probably be back up soon.

**504 Gateway Timeout** – The server was in the middle of a request and used for routing. But it has not received a timely response from the server it was routing to.

**505 HTTP Version Not Supported** – This is exactly what it says: The HTTP protocol version in the request isn’t supported by the server.

**506 Variant Also Negotiates** – Allows the client to get the best variant of a resource when the server has multiple variants.

**507 Insufficient Storage** – The server can’t store what it needs to store to complete the request.

**508 Loop Detected** – The server found an infinite loop when trying to process the request.

**509 Bandwidth Limit Exceeded** – Unofficial use by Apache and cPanel.

**510 Not Extended** – More extensions to the request are required before the server will fulfill it.

**511 Network Authentication Required** – The client needs authentication before the server allows network access.

**520 Web Server Returned an Unknown Error** – Unofficial use by Cloudflare.

**521 Web Server is Down** – Unofficial use by Cloudflare.

**522 Connection Timed Out** – Unofficial use by Cloudflare.

**523 Origin is Unreachable** – Unofficial use by Cloudflare.

**524 A Timeout Occurred** – Unofficial use by Cloudflare.

**525 SSL Handshake Failed** – Unofficial use by Cloudflare.

**526 Invalid SSL Certificate** – Unofficial use by Cloudflare.

**527 Railgun Error** – Unofficial use by Cloudflare.

**529 Site is overloaded** – Unofficial use by Qualys.

**530** – Unofficial use by Cloudflare.

**530 Site is frozen** – Unofficial use by Pantheon.

**561 Unauthorized** – Unofficial use by AWS Elastic Load Balancer.

**598 (Informal convention) Network read timeout error** – Unofficial use by some HTTP proxies.

### How Google handles 5xx

5xx errors will slow down crawling. Eventually, the pages will be dropped from Google’s index. You can find these in [Site Audit](https://ahrefs.com/site-audit) or [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools), but they may be different from the 5xxs that Google sees. Since these are server errors, they may not always be present.

## 6xx+ - Unofficial

The standards only specify 1xx-5xx codes, but you may encounter some unofficial status codes. A lot of times these will be used by different platforms or they may allow users to use certain ranges for any custom codes. Because these are all custom, it would be impossible to list what they do. The numbers can go above 1,000.

**999** – This is common enough to mention. It’s usually a generic error code used when a request is unable to be processed or it is denied.
