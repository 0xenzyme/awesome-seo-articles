---
title: "JavaScript SEO: How to Optimize JS for Search Engines"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "javascript-seo"
url: "https://www.semrush.com/blog/javascript-seo/"
canonical: "https://www.semrush.com/blog/javascript-seo/"
author: "Carlos Silva"
published: "2021-01-05T15:01:00+00:00"
updated: "2023-03-14T08:00:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T17:09:24+00:00"
status_code: 200
html_hash: "6282b7c8a81737858914d5c8d38e29a457b28031b9307e35f276296a63f25da1"
clean_word_count: 1926
clean_char_count: 13946
---
# JavaScript SEO: How to Optimize JS for Search Engines

## What Is JavaScript SEO?

JavaScript SEO is a part of technical SEO that focuses on making websites built with JavaScript easier for search engines to crawl, render, and index.

Common tasks include the following:

- Optimizing content injected via JavaScript

- Correctly implementing lazy loading

- Following internal linking best practices

- Preventing, finding, and fixing JavaScript issues

And others.

**Note:** If you need to refresh your knowledge about basic JS, read our guide: [What Is JavaScript & What Do You Use It For?](https://www.semrush.com/blog/javascript/)

## How Does Google Crawl and Index JavaScript?

Google processes JS in three phases:

1. Crawling
2. Rendering
3. Indexing

![how google processes JS](https://static.semrush.com/blog/uploads/media/95/c9/95c957f269663b35863b43b7c67c68d6/Mx7lqS8oDRFuIw-VxxwPmCLxBPtAoPfE5oq-6_m2gEB8Iq9y8nU3It4URJpou3xyxF_HKqn_NpCN52mKBwe2GmX9oKzwZNuxRiiuDGsHxmbd7nesYWnwUhFx-TlT5L_TqkliE91Uk_QktxCmYISH1iY.png)

Image Source: [Google](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)

Google’s web crawler (known as Googlebot) queues pages for crawling and rendering.

It crawls every URL in the queue.

Googlebot makes a request. Then the server sends the HTML document.

Next, Googlebot decides which resources it needs to render the page’s content.

This means it crawls the HTML. Not JS or CSS files because rendering JavaScript requires immense resources.

Think about all the computing power Googlebot needs to download, read, and run JS for trillions of pages on nearly [2 billion websites](https://www.statista.com/chart/19058/number-of-websites-online/).

So, Google defers rendering JavaScript. It queues anything unexecuted to process later as resources become available.

Once resources allow, a headless Chromium (Chrome browser without a user interface) renders the page and executes the JavaScript.

Googlebot processes the rendered HTML again for links. And queues the URLs it finds for crawling.

In the final step, Google uses the rendered HTML to index the page.

## Server-Side Rendering vs. Client-Side Rendering vs. Dynamic Rendering

Google JavaScript indexing issues are largely based on how your site renders this code: server-side, client-side, or dynamic rendering.

### Server-Side Rendering

Server-side rendering (SSR) is when JavaScript is rendered on the server. A rendered HTML page is then served to the client (browser, Googlebot, etc.).

For example, when you visit a website, your browser makes a request to the server that holds the website’s content.

Once the request is processed, your browser returns the rendered HTML and shows it on your screen.

SSR tends to help pages with SEO performance because:

- It can reduce the time it takes for a page’s main content to load
- It can reduce layout shifts that harm the user experience

However, SSR can increase the amount of time it takes for your page to allow user inputs.

Which is why some websites that deal heavily in JS opt to use SSR for some pages and not others.

Under hybrid models like that, SSR is usually reserved for pages that matter for SEO purposes. And client-side rendering (CSR) is usually reserved for pages that require a lot of user interaction and inputs.

But implementing SSR is often complex and challenging for developers.

Still, there are tools to help implement SSR:

- Gatsby and Next.JS for the React framework
- Angular Universal for the Angular framework
- Nuxt.js for the Vue.js framework

Read [this guide](https://web.dev/rendering-on-the-web/#server-rendering) to learn more about setting up server-side rendering.

### Client-Side Rendering

CSR is the opposite of SSR. In this case, JavaScript is rendered on the client side (browser or Googlebot, in this case) using the Document Object Model ([DOM](https://www.w3.org/TR/WD-DOM/introduction.html)).

Rather than receiving the content from the HTML document as in server-side rendering, you get a bare-bones HTML with a JavaScript file that renders the rest of the site using the browser.

Most websites that use CSR have complex user interfaces or many interactions.

Check out [this guide](https://web.dev/rendering-on-the-web/#client-side-rendering-csr) to learn more about how to set up client-side rendering.

### Dynamic Rendering

Dynamic Rendering is an alternative to server-side rendering.

![how dynamic rendering works infographic](https://static.semrush.com/blog/uploads/media/ec/66/ec661d623627150d560437ca617566a4/Q1DnanbUqPHiocCbykQFwGWF0qVewb5xPgahCfX-nDVDeVdtZW0CZ9Wzqq6D7QbRkrOzNSQdBEieGCjScSEogjaKiBBBF_0qHxX8CSSGezfUX9INGRNZfPpr63rpl4fPULN6IEJ0a9ud8B3wZAKLQcY.png)

It detects bots that may have problems with JS-generated content and delivers a server-rendered version without JavaScript.

All while showing users the client-side rendered version.

Dynamic rendering is a workaround and not a solution Google recommends. It creates additional, unnecessary complexities and resources for Google.

You might consider using dynamic rendering if you have a large site with content that changes rapidly and needs quick indexing.

Or if your site relies on social media and chat apps that need access to a page’s content.

Or if the crawlers important to your site cannot support some of the features of your JS.

But really, dynamic rendering is rarely a long-term solution. You can learn more about setting up dynamic rendering and some alternative approaches from [Google’s guidelines](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering#implement).

**Note:** Google generally does not consider dynamic rendering to be “[cloaking](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering#cloaking)” (the act of presenting different content to search engines and users). While dynamic rendering isn’t ideal for other reasons, it’s unlikely to violate the [cloaking rules](https://developers.google.com/search/docs/essentials/spam-policies#cloaking) outlined in Google’s spam policies.

## How to Make Your Website’s JavaScript Content SEO-Friendly

You can follow several steps to ensure search engines properly crawl, render, and index your JS content.

### Use Google Search Console to Find Errors

Googlebot is based on Chrome’s latest version. But it doesn’t behave the same way as a browser.

Which means launching your site doesn’t guarantee Google can render its content.

The URL Inspection Tool in [Google Search Console](https://search.google.com/search-console/) (GSC) can check whether Google can render your pages.

Enter the URL of the page you want to test at the very top. And hit enter.

![Enter the URL site](https://static.semrush.com/blog/uploads/media/74/97/74971a4bf5f0601e11283876f0217489/7_LQM3qazu94ZYU6vZXF6GCwf-YZO8pcyX6t1F0QaQRie_Z2B7QTbmaVraBxOPBXYwxZk_R4SvkLs8Wg3WJ6d6qsDljP2KtftH-H8xcSrQTeNmLids6FeJIwXy7pPx96tl4qaLVZeh_Jx0UaB52jfUM.jpeg)

Then, click on the “**Test Live URL**” button on the far right.

![Test live URL button](https://static.semrush.com/blog/uploads/media/8c/6b/8c6b8f23c1d4ebde3bcc831c7cd44dfe/1bNG0jre3vleNBC7kmWOgqehrucyPgbwSdEvQXIFAVd2664DHJ0XQkKyiSOVZJ2HViE4a9s6hQ7toK_B6wDmzDRoKwd-ODmpyLRt2mzUj07EHAupwN8O8-nbqKIEfQSXVoCT5AgArt16tii6rifNiq8.jpeg)

After a minute or two, the tool will show a “**Live Test**” tab. Now, click “**View Tested Page**,” and you’ll see the page’s code and a screenshot.

![Tested page view](https://static.semrush.com/blog/uploads/media/e6/82/e6826c76b84eae0fdefbb8ab77be605e/kIaaqe4dLJrV-aJhIYESFVtVl4WnIB_vo9k8ekev1HFZ7A64sAsGDFxoTF6q3fDpuEnsDcKcnUXAWwl-dPehYItjY7L8Ao8Q6dMtqLhynN73u8ndmi-Xutsaf88fGlsL3AZZSu4tB7JAk1yCgCwzvHY.jpeg)

Check for any discrepancies or missing content by clicking on the “**More Info**” tab.

![More info tab](https://static.semrush.com/blog/uploads/media/bc/bb/bcbb7790dfaa77c1e6100f91ed3bd39a/zFIHWokvOtT8QkqbNKBBDAiYqFEiL6YnK8uvKbcgSMVHEIKo9dLnA5mGNtDE3gYbYvSjzYH3_NIyJM3W5VbAGYFiDU4i-zM_wx1IeP29TWb01HSaUteolwxo6SulslQiHvNcBccBI6nyndb9pJNHqaA.jpeg)

A common reason Google can’t render JS pages is because your site’s [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) file blocks the rendering. Often accidentally.

Add the following code to the robot.txt file to ensure no crucial resources are blocked from being crawled:

`User-Agent: Googlebot
Allow: .js
Allow: .css`

**Note:** Google doesn’t index .js or .css files in the search results. They’re used to render a webpage.

There’s no reason to block these crucial resources. Doing so can prevent your content from being rendered and, in turn, from being indexed.

### Ensure Google Is Indexing JavaScript Content

Once you confirm your pages are rendering properly, ensure they’re being indexed.

You can check this in GSC or on the search engine itself.

To check on Google, use the “site:” command. For example, replace yourdomain.com below with the URL of the page you want to test:

`site:yourdomain.com/page-URL/`

If the page is indexed, you’ll see it show up as a result. Like so:

![indexed pages show in SERP](https://static.semrush.com/blog/uploads/media/48/d6/48d6d54f6c7d84601348bc3b02f5e51c/I0JsSnaA1La9EmVYHiJ62bO1qDYU7jYtiy197COo6sfvKQXGHVwaQJLdWQMT32Rh8ImBCVh6EH04hjm1f3kNGdxV_7e4R9VwrPHg_ygiHTKId8kNl2GoTBaPeoAZoCWh5O-q-LpRiGgfyHwUyYq-xLc.jpeg)

If you don’t, the page isn’t in Google’s index.

If the page is indexed, check whether a section of JavaScript-generated content is indexed.

Again, use the “site:” command and include a snippet of JS content on the page.

For example:

`site:yourdomain.com/page-URL/ "snippet of JS content"`

You’re checking whether this specific section of JS content has been indexed. If it is, you’ll see it within the snippet.

Like this:

![indexed JS content shown in SERP](https://static.semrush.com/blog/uploads/media/96/4e/964e01aa75af3a2eb84fec1b5819a094/2pnbDC_wVQSnryrG_jzcT7CKO2n6MDdBqib4sYpsMZi2vxKQjxyGO01orE8qYZswCxrR-eMpyUnHnnef9dMCxTwYGUCK2tEHBovMu7W2hdQiZ7CZ8zS4-ThQE8rcbqLiXweLJZ-68f5yl1GLTVW21VU.jpeg)

You can also use GSC to see whether JavaScript content is indexed. Again, using the URL Inspection Tool.

This time, rather than testing the live URL, click the “**View Crawled Page**” button. And check the page’s HTML source code.

![View crawled page button](https://static.semrush.com/blog/uploads/media/cd/96/cd96675bb545e3edcd04644f1a71a3f1/xgBPCOmiR4AMuFNUCECobM8wCUu28MRMbpMKKMtTKo6CvKItA8vqSwdE6HCSdnGhonimunfEvZrZMfB9VXJvpgdfUgDKQju-r2VtbELaIQsf02zHieG0AS-qJNK9EJqLGDwUclpJLpASY5YJGrfkkHs.jpeg)

Scan the HTML code for snippets of JavaScript content.

If you don’t see your JS content, it could be for several reasons:

- The content cannot be rendered

- The URL cannot be discovered because JS is generating internal links pointing to it in the event of a click

- The page times out while Google is indexing the content

### Run a Site Audit

Regularly running audits on your site is a [technical SEO](https://www.semrush.com/blog/technical-seo/) best practice.

Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool can crawl JS as Google would. Even if it’s rendered client-side.

To start, enter your domain, and click “**Create project**.”

![Site Audit tool](https://static.semrush.com/blog/uploads/media/7c/0f/7c0fa75c5994bf361c83df1a17bd498b/OB0xrwnexyr46ec1ojzCHeakx9MLzyTskU9GoI-wc9hJVeW-IQUShm2RTp7Ck0j46XhBXjc0g8DMi6WYnY70K2WW4iGgpLaTckg4cikcBWOQJV-Uzgt_d978lW6GFKRZca4IwKAT2iFuGWHJIy0VPXc.jpeg)

Then, choose “**Enabled**” for JS-rendering in the crawler settings.

![Enable JS-rendering in Site Audit](https://static.semrush.com/blog/uploads/media/aa/00/aa0025996df82843ac900d937b167306/TDKcJMnmFIBlF_3aiS1GNPEkf-zLVb4zZnBMxaMQssCisnGCHcGzMg-7mjx5t24EnxJbHW29Er1d77hMMxMoxVdKpdeQsClCjJk0ylDk68gNnXOmI6EVSTfCGs1vE48R_cjnolmRO3hWwD4P7DcoBqc.jpeg)

After the crawl, you’ll find any issues under the “**Issues**” tab.

![Issues tab overview](https://static.semrush.com/blog/uploads/media/b6/90/b69052a579986a0269d1a31d34aedaeb/mRYWCR2qeGbiA1L02sR7ZVuzeMPTJCoPAny7kfVXlNIfSbcSpyM6IJVkqGM9Jjv2Tb9zBYZNRg4fJ9FEsxz5JF5suksw3VHJI8YjJaVHpgmvk7Qz20RFGYUG5RDNHsVRmlKEFj3j-dYW5unsHynN_ds.jpeg)

## Common JavaScript SEO Issues & How to Avoid Them

Here are some of the most common issues, as well as some JavaScript SEO best practices:

- Blocking .js files in your robots.txt file can prevent Googlebot from crawling these resources. Which means it can’t render and index them. Allow these files to be crawled to avoid this problem.

- Google doesn’t wait long for JavaScript content to render. Your content may not be indexed because of a timeout error.

- Search engines don’t click buttons. Use internal links to help Googlebot discover your site’s pages.

- When lazy loading a page using JavaScript, don’t delay loading content that should be indexed. Primarily focus on images versus text content when setting up lazy loading.

- Google often ignores hashes, so make sure static URLs are generated for your site’s webpages. Ensure your URLs look like this: (yourdomain.com/web-page). And not like this (yourdomain.com/#/web-page) or this (yourdomain.com#web-page).

## Take It a Step Further

If you use what you’ve learned about JavaScript SEO, you’ll be well on your way to creating efficient websites that rank well and users love.

Ready to dive deeper?

We recommend reading the following to learn more about JS and technical SEO:

- [JavaScript commands cheat sheet](https://www.semrush.com/blog/javascript-cheat-sheet/)

- [How to redirect a URL with JavaScript](https://www.semrush.com/blog/javascript-redirect/)

- [How to use JS to change meta tags](https://www.semrush.com/blog/meta-tag/)

- [How to get Google to index your website](https://www.semrush.com/blog/google-index/)

- [Crawlability, indexability, and SEO](https://www.semrush.com/blog/what-are-crawlability-and-indexability-of-a-website/)
