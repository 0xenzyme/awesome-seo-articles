---
title: "JavaScript Redirect: How to Redirect to a New URL"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "javascript-redirect"
url: "https://www.semrush.com/blog/javascript-redirect/"
canonical: "https://www.semrush.com/blog/javascript-redirect/"
author: "Sean Collins"
published: "2021-10-14T17:25:00+00:00"
updated: "2023-08-07T12:41:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T17:09:03+00:00"
status_code: 200
html_hash: "baaf7e766380080ef68b1df49d08604daafbfb9eef6c748072c8273192e72ee3"
clean_word_count: 2736
clean_char_count: 18339
---
# JavaScript Redirect: How to Redirect to a New URL

A JavaScript redirect uses the programming language JavaScript (JS) to send users from one URL to another.

You can use a JS redirect to redirect users to a confirmation page after they submit a form or to provide fallback redirection if a page gets deleted, for example.

But they are not generally not recommended for SEO because search engines can have difficulty crawling and indexing sites that rely on them.

In this article, we’ll discuss creating a redirect with JS and suggest alternatives.

## How to Redirect with JavaScript

There are three main ways to redirect to another URL with [JavaScript](https://www.semrush.com/blog/javascript/):

1. **window.location.href**
2. **location.assign()**
3. **location.replace()**

### Set a New window.location.href Property

You can use the **window.location.href** property in JavaScript to get or set the URL of the current webpage.

The use of "window.location.href" for redirection simulates the action of clicking on a hyperlink. It adds a new entry to the browser’s session history. This allows users to use the “back” button to return to the previous page.

To redirect a user to a different URL, you can assign a new URL to this property.

The syntax is:

`window.location.href = ‘https://exampleURL.com/’;`

When tied to a user interaction-triggered change, such as a button click, this would redirect the user to “https://exampleURL.com/”

How?

You need to add the code inside of **<script>** tags inside of the **<head>** of your webpage and add an “**event** **handler**” to a button.

Here’s how you could do that:

`<html>
<head>
<script>
function myFunction() {
window.location.href = "https://exampleURL.com/";
}
</script>
</head>
<body>
<h2>Redirect to a Webpage</h2>
<p>The location.href method redirects the user to a new webpage:</p>
<button onclick="myFunction()">Redirect</button>
</body>
</html>`

When the user clicks the “**Redirect**” button, it triggers the **onclick** event handler, which calls the **myFunction()** function. The execution of **myFunction()** changes the value of "location.href" to "[https://exampleURL.com/](https://exampleurl.com/)", which instructs the browser to navigate to that URL.

Let's run through two other use cases for JavaScript redirects.

The example below demonstrates using **setTimeout()** for a JavaScript redirect.

It’s a built-in JavaScript function that lets you run another function after a certain amount of time (10 seconds in the example below).

`<html>
 <head>
<script type="text/JavaScript">
 function Redirect() {
window.location = "https://exampleURL.com/";
 }
 document.write("You will be redirected to the main page in 10 seconds.");
 setTimeout(function() {
Redirect();
 }, 10000);
</script>
 </head>
</html>`

Another use case could include redirecting a user based on the browser they’re using.

`<html>
<head>
<title>Your Page Title</title>
<script type="text/javascript">
window.onload = function() {
var userAgent = navigator.userAgent.toLowerCase();
if (userAgent.includes('chrome')) {
window.location.href = "http://www.location.com/chrome";
} else if (userAgent.includes('safari')) {
window.location.href = "http://www.location.com/safari";
} else {
window.location.href = "http://www.location.com/other";
}
</script>
</head>
<body>
<!-- Your body content goes here -->
</body>
</html>`

***Top tip:** Avoid creating JavaScript redirects in the header without tying them to user actions to prevent potential redirect loops (more on this later). To prevent users from using the “back” button, use "window.location.replace."*

### Redirect Using the location.assign() Method

You can use "**window.location.assign**" as an alternative to "**window.location.href**" for redirects.

The syntax is:

`window.location.assign(‘https://www.exampleURL.com/’);`

Here’s what it looks like inside of a script tag:

`<script type="text/JavaScript">
 function Redirect() {
window.location.assign("https://exampleURL.com/");
 }
</script>`

From a user’s perspective, a redirect using "window.location.assign()" looks the same as using "window.location.href".

This is because:

- They both create a new entry in the browsing session history (similar to clicking on a link)
- They both enable users to go back and view the previous page

Similarly to "window.location.href," it directs the browser to load the specified URL and add this new page to the session history—allowing users to use the browser’s “back” button to return to the previous page.

However, "window.location.assign()" calls a function to display the page located at the specified URL. Depending on your browser, this can be slower than simply setting a new href property using "window.location.href".

But in general, both "window.location.assign()" and changing the location.href property should work just fine. The choice between them is mostly a matter of personal preference and coding style.

### Redirect Using the location.replace() Method

Like "window.location.assign()", "**window.location.replace()**" calls a function to display a new document at the specified URL.

The syntax is:

`window.location.replace('https://www.exampleURL.com/');`

Here’s what it looks like inside of a script tag:

`<script type="text/JavaScript">
 function Redirect() {
window.location.replace("https://exampleURL.com/");
 }
</script>`

Unlike setting a new location property or using "window.location.assign()" the replace method does not create a new entry in your session history.

Instead, it replaces the current entry. Meaning users cannot click the “back” button and return to the previous, pre-redirect page.

Why would you want to do this?

Examples of where you may use the "window.location.replace()" method include:

- **Login redirects:** After successful login, users are directed to the main site content, and the login page is intentionally omitted from the browser history to prevent accidental return through the “back” button

- **User authentication:** To redirect unauthenticated users to a login page, blocking “back” button access to the previous page

- **Form submission success:** Post-form submission, "window.location.replace()" can navigate users to a success page, preventing form resubmission

- **Geolocation:** Based on the geolocation of a user, you can redirect them to a version of your site that’s more suitable for their location, like a site that’s translated to their language

To recap:

Use "window.location.replace()" when you **don’t** want the user to be able to go back to the original page using the “back” button.

Use "window.location.assign()" or "window.location.href" when you want the user to be able to go back to the original page using the “back” button.

But while you can redirect users to a new page using JavaScript methods like "window.location.assign()" or "window.location.href", server-side redirects, such as [HTTP redirects,](https://www.semrush.com/blog/redirects/) are typically recommended instead.

***Note:** If you’re just starting out or want to practice JavaScript, you can visit a website like W3Schools, which offers an interactive [W3Schools Tryit Editor](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_redirect_webpage) for JavaScript, HTML, CSS, and more:*

![W3Schools Tryit Editor](https://static.semrush.com/blog/uploads/media/95/88/9588295957c628fbff33dbf936e58e1a/Ci16wO6KJrtDcfn64KzLuClwhCu96I0dkqGTbWfa6lhDWOX7TFmuYshbPK2c8RaGFGjOzbD4yX2RNgWzQkMCQ2WYeT4XG1-JDbAXvDzuqiEw8Abob6esMR558GbmNykkuwo1oDLHhXMR0NEqi-PkOdA.png)

## How Google Understands and Processes JavaScript Redirects

Google processes JavaScript redirects the same way it [executes and renders JavaScript](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) when crawling and indexing websites.

Here’s what that looks like, [according to Google](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics):

![an image showing how Google processes JavaScript redirects](https://static.semrush.com/blog/uploads/media/a0/56/a056cb5d5789577b831096e394d226e1/vjpYL7fudY3d4zGCLJ_hHxp7loQW24lh159Xnp3FH0RdZzCWdxJ9zV3iclnlXPS-F5GwO9SL1nMNe8yg2xM7ADO85jToxEnZa-wU3dczUk7YQcH2ASWpOOC8pZF_LFHN8REJzDka_89v9UIV3MD6khk.png)

Google’s web crawler, Googlebot, initially indexes a webpage’s HTML content. It places any detected JavaScript, including redirects, into a “Render Queue” for later processing.

This two-step process helps Google quickly add important content to its [search index](https://www.semrush.com/blog/google-index/). JavaScript is dealt with later because Google needs more resources to process it.

***Learn more:** [JavaScript SEO: How to Optimize JS for Search Engines](https://www.semrush.com/blog/javascript-seo/)*

But, despite being capable of handling JavaScript redirects, **Google advises you to [avoid using them](https://developers.google.com/search/docs/crawling-indexing/301-redirects#jslocation)** if possible due to their high resource consumption and processing time.

![Google advises you to avoid using JavaScript redirects](https://static.semrush.com/blog/uploads/media/90/9d/909d36afdbdc451a08625ac090fca21f/rw28ozQiklGEaCkBFpzxL_GKb_STaFhx_JPyeBVdh9evgpF0XM8H9ii5_AO32VF_GIRJHtJah1SxBNO6fbLag-NrQc9YCCW_V1WeQxzbuCnDP7F_r8ybNu31mme61nzf2hRe0aNdf-oA-_IxbqprFH8.png)

This was also echoed by [John Mueller in a June 2022 SEO Office Hours](https://youtu.be/-qhUhnBRe3Y?t=684) video (11:25).

![Youtube video thumbnail](https://i.ytimg.com/vi/-qhUhnBRe3Y/hq720.jpg)

So JavaScript-triggered user actions, like a redirect after a button or link click, may go unnoticed. Hence [Google’s preference for server-side redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects#jslocation), such as HTTP redirects—which offer greater efficiency, reliability, and [search engine optimization](https://www.semrush.com/blog/what-is-seo/) (SEO) benefits.

HTTP redirects have several advantages over JavaScript redirects, including:

- **Consistent navigation history:** HTTP redirects don’t interfere with the user’s navigation history. Unlike the “location.replace()” method, users can still use the back button to return to previous pages.

- **SEO friendliness:** HTTP redirects provide explicit instructions for search engines when pages move, which helps maintain a site’s [SEO ranking](https://www.semrush.com/blog/seo-ranking/). For example, unlike a JS redirect, a [301 redirect](https://www.semrush.com/blog/301-redirects/) tells search engines that content has permanently moved to a new URL.

- **Performance:** HTTP redirects occur at the server level before the content is sent to the browser, which can make them faster than JavaScript redirects and improve your [page speed](https://www.semrush.com/blog/page-speed/)

- **Reliability:** Users may choose to disable JavaScript for security and privacy reasons. HTTP redirects will work even if a user has JavaScript disabled, making them more reliable.

***Learn more:** [The Ultimate Guide to Redirects: URL Redirections Explained](https://www.semrush.com/blog/redirects/)*

## How to Identify JavaScript and HTTP Redirect Issues

When working with JavaScript and HTTP redirects, the most common issues you might encounter include:

- Redirect chains and loops
- Linking to pages with redirects

### Redirect Chains and Loops

You might create a redirect chain or loop without realizing it when dealing with redirects.

What is a redirect chain?

A redirect chain is when you need to “hop” through several URLs before reaching the final one.

For example, consider that you initially have a page with URL A. You then decide to redirect URL A to a new URL B. At some later point, you choose to redirect URL B to URL C.

In this case, you've created a redirect chain from URL A to URL B to URL C.

![and image showing "What is a redirect chain?"](https://static.semrush.com/blog/uploads/media/5d/e1/5de18f1da1ae2a5bb4830dbfa80f38c3/redirect-chain.jpg)

Google can comfortably handle up to [10 redirect “hops.”](https://developers.google.com/search/docs/crawling-indexing/http-network-errors)

But too many redirect chains can cause issues with [website crawling](https://www.semrush.com/blog/website-crawler/), possibly increasing the time it takes a [page to load](https://www.semrush.com/blog/page-speed/). This could also negatively impact your SEO ranking and annoy your users.

To resolve this problem, redirect URL A to URL C (bypassing URL B).

Here’s what the redirect chain should look like:

![an example of what the redirect chain should look like](https://static.semrush.com/blog/uploads/media/0c/97/0c973e5ae107fdb13e632d3efef7c1c5/correct-redirect-example.jpg)

What is a **redirect loop?**

A redirect loop happens when a URL redirects to a different URL, and then that second URL redirects back to the first one, creating a never-ending cycle of redirects.

For example:

![and image titled "What is a redirect loop?"](https://static.semrush.com/blog/uploads/media/2b/cb/2bcbb11a9f973cda00506b44d63970f9/redirect-loop.jpg)

This type of redirection is broken and fails to properly direct visitors or search engines to the intended URL.

To fix redirect loops, identify the “correct” page and ensure the other page redirects to it. Then, get rid of any extra redirects that are causing the loop.

Semrush’s [Site Audit tool](https://www.semrush.com/siteaudit/) can help you detect both HTTP and JavaScript redirect chains.

How?

First, [create a project](https://www.semrush.com/kb/539-configuring-site-audit) or click on an existing one you want to look at.

![a created "petco.com" project in Semrush's Site Audit tool](https://static.semrush.com/blog/uploads/media/67/66/67669aeccfb27c1d2c7943f3c02d353d/Site-Audit-Petco.jpg)

Select the “**Issues**” tab and search for “redirect chain” by entering it into the search bar.

![search for “redirect chain” in Site Audit tool](https://static.semrush.com/blog/uploads/media/63/66/6366f713b8b75e86f03efb8e6c069407/Site-Audit-issues-tab.jpg)

Click on “**# redirect chains and loops**.”

This will give you a report with all your site’s redirect chain or loop errors.

!["3 redirect chains and loops” shown for "petco.com" project in Site Audit](https://static.semrush.com/blog/uploads/media/e8/58/e858da793742ebe1fb87cc7e73b16992/redirect-chains-and-loops.jpg)

The report includes details such as the page URL with the redirect link, the type of redirect, and the “length” of the chain or loop.

![List of redirect chains and loops in Site Audit](https://static.semrush.com/blog/uploads/media/7b/14/7b145ffe20370ff45fddf05fe596753c/Site-Audit-redirect-chains-loops.jpg)

You can then sign into your content management system (CMS) and fix each issue.

### Linking to Pages with Redirects

Suppose you redirect an old page to a new one. Some pages on your site might still link to the old page.

If that’s the case, users will be directed to your old link, and from there, they will be redirected to the new URL.

Users might not even notice this happening. However, this additional redirect can add up to a “redirect chain” if you fail to address the issue the first time.

Here’s how this problem appears:

![an example of linking to a page with redirect](https://static.semrush.com/blog/uploads/media/41/0f/410fb7a6bbdf1d6577f397af4515ec58/incorrect-internal-link-redirect.jpg)

Updating the old internal links to link directly to your new page’s URL is best.

This is how it should look:

![an example of linking to a page with new URL](https://static.semrush.com/blog/uploads/media/2f/7b/2f7b3be891c161a7e203942433933bf6/internal-link-redirect.jpg)

But how can you find links pointing to redirects?

You can do this by going to the “**Crawled Pages**” tab of the Site Audit tool:

!["Crawled Pages" tab of the Site Audit tool](https://static.semrush.com/blog/uploads/media/a6/db/a6db94a2e57ff1bb62652ea44f305180/Crawled-Pages-tab.jpg)

Next, enter your old URL (the one that’s being redirected) into the “Filter by Page URL” field.

![entering the new URL into the "Filter by Page URL" field](https://static.semrush.com/blog/uploads/media/e9/13/e9139759e57c05bbe0137b70f2cf5480/Crawled-pages-report.jpg)

Press “**Enter**” to see a report for the URL you just entered.

![Crawled Pages report for one URL](https://static.semrush.com/blog/uploads/media/30/75/30755de6871329b686ec30da82ab30d0/crawled-page.jpg)

Under the “Incoming Internal Links” section, you’ll find a list of internal links that direct to your old URL.

!["Incoming Internal Links" section in Site Audit](https://static.semrush.com/blog/uploads/media/f2/a4/f2a4df4ccb7526348505ca1bd31e150a/incoming-internal-links.jpg)

To avoid unnecessary redirects, all you need to do is replace the old link with the new link.

How?

You’ll have to do this by going to each page and manually changing the link.

## JavaScript Redirect FAQs

### What Is a JavaScript Redirect?

A JavaScript redirect is a method that uses JavaScript to direct a browser from the current webpage to a different URL. It’s typically used for conditional navigation or user interaction-triggered changes, though it requires the user's browser to enable JavaScript.

### Are Redirects with JavaScript Good or Bad For SEO?

JavaScript redirects can be used without necessarily harming SEO but are generally less favored than server-side redirects. This is due to their dependence on JavaScript being enabled on the user’s browser and their potential to be overlooked by search engines during the crawling and indexing process.

### What’s the Best Alternative to a JavaScript Redirect?

The best alternative is to use server-side redirect methods, such as 301 redirects, that don’t rely on JavaScript and provide explicit instructions that search engines better understand.

Want to learn more about JavaScript and redirects?

Check out these resources:

- [The Ultimate Guide to Redirects: URL Redirections Explained](https://www.semrush.com/blog/redirects/)
- [301 Redirect: What It Is & How It Impacts SEO](https://www.semrush.com/blog/301-redirects/)
- [JavaScript SEO: How to Optimize JS for Search Engines](https://www.semrush.com/blog/javascript-seo/)
- [Semrush Site Audit Can Now Render JavaScript](https://www.semrush.com/blog/js-rendering/)
