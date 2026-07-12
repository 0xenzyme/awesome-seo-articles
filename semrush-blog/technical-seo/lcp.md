---
title: "Largest Contentful Paint (LCP): What It Is & How to Improve It"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "lcp"
url: "https://www.semrush.com/blog/lcp/"
canonical: "https://www.semrush.com/blog/lcp/"
author: "Boris Mustapic"
published: "2021-05-16T22:12:00+00:00"
updated: "2023-10-31T10:15:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T17:22:23+00:00"
status_code: 200
html_hash: "84b6ada57028292daf06e3918def9f9f0ab4a82b67949b0a908484ea2f0cf6d9"
clean_word_count: 2019
clean_char_count: 15414
---
# Largest Contentful Paint (LCP): What It Is & How to Improve It

## What Is Largest Contentful Paint?

Largest Contentful Paint (LCP) is a core web performance metric that measures how long it takes for the largest piece of visible content (often an image, video, or text block) to fully render on a user’s screen.

LCP is one of three Core Web Vitals that Google uses to assess website performance. The other two metrics are:

- [First Input Delay (FID)](https://www.semrush.com/blog/google-inp/): Measures how quickly the page responds when a user interacts with it.
- [Cumulative Layout Shift (CLS)](https://www.semrush.com/blog/cumulative-layout-shift/): Measures how much the page layout shifts unexpectedly while loading.

These three metrics are interconnected. For example, a large LCP value can delay user interactions, causing a high FID, because the browser may not respond until the largest element has loaded.

## Largest Contentful Paint vs. First Contentful Paint

LCP and First Contentful Paint (FCP) are two very different metrics.

**LCP** measures how long it takes the largest element to load.

**FCP** measures how long it takes the first visual element to appear, regardless of size.

LCP is more reliable for determining when a page is ready for interaction. FCP can mislead, since the first element to appear might be minor, like a small icon or an empty image tag, rather than the main content.

## Why Is LCP Important for Website Performance?

LCP is important for website performance because users expect fast-loading websites. Improving LCP can make the site feel faster and ready for interaction sooner.

A better LCP score can help you achieve:

- **Higher rankings:** LCP is a [Core Web Vital](https://www.semrush.com/blog/core-web-vitals/), so improving it can help achieve higher Google rankings
- **Lower bounce rates:** Faster loading times reduce the likelihood of users leaving prematurely
- **Increased conversion rates:** Faster websites often [improve conversion outcomes](https://www.portent.com/blog/analytics/research-site-speed-hurting-everyones-revenue.htm)

## What Is a Good LCP Score?

A good LCP score is 2.5 seconds or less, which meets Google’s Core Web Vitals standard.

An LCP score between 2.5 and 4 seconds signals that improvement is needed.

An LCP score of more than 4 seconds is considered poor and requires significant changes.

![An infographic on Google’s largest contentful pain guidelines](https://static.semrush.com/blog/uploads/media/3a/e6/3ae61d9c2654db2342c9249d299cac33/ce221f1e7b4cded2cf86aefe23c0f39d/AD_4nXf5nQYPsOOsGdMgmLNw8E1oGiEuLatbrXWE-V12ERAAiLMM6GDcNSxldIK_8czCcKzHFw3xlvB7DL9vqXq0dwxY7y28mW_aDGHtjvadCUU8cR1wQ-sevmLFNFWLyK2Puoj0bZcrag.jpeg)

## What Causes a Low LCP Score?

Four main factors can lower an LCP score:

![An infographic listing the four factors that cause the poor LCP](https://static.semrush.com/blog/uploads/media/47/82/478248b32a6cbd496ab9ba9ec90a9827/01e252b5f43bef08fee3964f46e7c58c/AD_4nXc3_0ubKmqFOeUaIt6IFAqfVVujJAW9kxF4PBGmnGU-zDz1H9RqOw11eG-OjEoR1lrCGY4uEeG2JTa4xPssKHiv_pxyyJ_g4oj5GhcqEQbX0HXW51n9vZxCjcR0lxoEMt7hr1SM.jpeg)

- **Slow server response times:** Delayed server responses slow down the largest content’s rendering
- **Render-blocking JavaScript and CSS:** Certain page elements, such as scripts and stylesheets, can delay page content from appearing
- **Slow resource load times:** Large, high-definition images [above the fold](https://www.semrush.com/blog/above-the-fold/) can slow down the display of main content
- **Client-side rendering:** Heavy client-side rendering, often involving large JavaScript files, can slow initial load times

## How to Measure Largest Contentful Paint

You can measure Largest Contentful Paint using the following tools:

### Semrush’s Site Audit Tool

Run our free [website SEO checker](https://www.semrush.com/siteaudit/) to flag LCP issues quickly.

To measure LCP across every page on your site, use Semrush Site Audit.

Enter your domain, then click “**Start Audit**.”

![Site Audit tool landing page](https://static.semrush.com/blog/uploads/media/a0/50/a05056738d85383487339e4a7c234f40/a99f1c0f74159ae48f1a954c9083c84e/AD_4nXf2-16HvL1zW8b4XT5xQCaRqre1U1KTni7oDnnvbacVEuKwPBb2Pbkibv_I-ie3SgO-vwrLYRstghXIYpriNqjO5WE3C1VAM9gD-kwSSOHIpBKElttLP1Rfo8C0IFQoXi-6OkdPhA.jpeg)

You can customize the audit settings by limiting the number of pages checked. The tool checks Core Web Vitals for 10 pages, and you can choose which ones.

You can also select a user agent, exclude specific URLs, and apply other filters.

!["Site Audit Settings" window](https://static.semrush.com/blog/uploads/media/ff/1a/ff1a978c57d996df10584cadf9236c5c/022af3bcecdd3cd021e6c8812db2d427/AD_4nXcS3du6f8iNGI5CnJ87cWGC_NfWMMJgF64i0fTR6YdXGwmNvirbaUkc_GGZrFRgIC_L27S8b6WTNllSO6MWDzqAXL8uwFABc5jpO3O8gu23LgVbeqV7ecHBqCJlhpF0V1EK08xWiQ.jpeg)

In “Crawler settings,” select whether to analyze the desktop or mobile version of your site. Choose between Google’s desktop or mobile crawler, or Semrush’s crawlers.

Differences in your site’s desktop and mobile designs may cause slight variations in the resulting data.

In most cases, keep the default settings and click “**Start Site Audit**.”

After crawling, open the generated report and click “**View details**” in the “Core Web Vitals” section.

![“Core Web Vitals” box highlighted in the Site Audit overview report](https://static.semrush.com/blog/uploads/media/6e/60/6e601382ac75a6bae17004712077d7d7/11d34e533ee810d05c547b18a5fc1543/AD_4nXcR-_D9NnCxASmlJacGiJStL9pSYOUdPHwIRtQFfaW5vo1BaPTQlS1ZDia1EQYLmniaHm1UB3-43etCqLuKgV6QWS_mjNBSmmiGG4uyrsqfmMhVK0DibiGOUgg71rIxfYhBhsSz.jpeg)

Scroll down to the “Metrics” section to find your LCP score and recommendations for improvement.

!["Largest Contentful Paint (LCP)" section highlighted under "Metrics" report](https://static.semrush.com/blog/uploads/media/4c/aa/4caa53c32b0b96899e54642ce9472717/311ee1d67a6f648d3fc238d21c5111f1/AD_4nXcfxbBbCGHnw7fklvdTujqqfcN9bxaeUtir5ZbZdj_v7lPJ9EGbVi-8SLMiP0mYUlPKhf2iH2V3SDIwEyjfNzxrA00KHd1Q-Um-YZhKwth8XzHUserPZB80-v59CiaJv-DtB03r.jpeg)

### Google PageSpeed Insights

Visit Google’s [PageSpeed Insights](https://pagespeed.web.dev/), enter the URL you want to test, and click “**Analyze**.”

![PageSpeed Insights landing page](https://static.semrush.com/blog/uploads/media/13/78/1378001878cff171d37895b791012ec4/e6374214464cf581c845209403b91186/AD_4nXdyry3u5T8c05AOX8l5eyFTM1C1_RliBixnHv5Xd05piWH9wqh1PcPQPuGAIhKEuEOngnM36U4amswiXCBcry6tEHwRdGQgfk5BoCq5DQyHsFfttX1E0HZE59nn2n5Y0fJCg6Pv.jpeg)

When the report appears, locate your LCP score in the “Core Web Vitals assessment” section.

!["Largest Contentful Paint (LCP)" metric highlighted under “Core Web Vitals assessment”](https://static.semrush.com/blog/uploads/media/f2/7c/f27c183f5ec06f35c45b3db6f8e0d14e/3e2710508f1ab129367920f814b08873/AD_4nXcs228pAM7zvdXWESFNwqorsgKuR-6jC1BhUSonGK3MeaAfX5L6s3T8E4zpD1JH3XDbn4wDmY3bQUi4QgndwyRLUhvDHp7SPoAku7dP_4WD7ywWEtR7hDMnLrNYxRCZq6XkqStc.png)

Toggle between mobile and desktop reports to see how LCP differs between the two versions of your site.

!["Mobile" and "Desktop" buttons highlighted in the PageSpeed Insights](https://static.semrush.com/blog/uploads/media/ff/7b/ff7b0a53ec09638dd69b2e0ec5228bc9/01cfaf719b9b9a3a818ac71046ffa252/AD_4nXdL-YjDpWmZwt_ClM-h5NbDi5SDlqSjSEgHEpMaGovxkzu5euWY81jpKJA-nzzF1QJrWyr1fsLO0NDTVhdUKR8cBn2uFJXqf3NaE-T8AGQ7ce0Y8HopWFN6QYypO1E8keEsDSo0vw.jpeg)

PageSpeed Insights will provide tailored recommendations depending on which report type you review.

### Google Lighthouse

Google [Lighthouse](https://www.semrush.com/blog/google-lighthouse/) is a free, open-source tool that can help improve site performance.

Install the Google Chrome [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk), then visit your webpage, click the extension’s icon, and select “**Generate report**.”

Lighthouse will analyze the page and display a detailed report. You can find the LCP score in the “Metrics” section.

!["Largest Contentful Paint" metric highlighted in the Google Lighthouse report](https://static.semrush.com/blog/uploads/media/9a/f7/9af7bd5ad7394f14558d9bc77f6dfc1d/600f35d19f94a79bf758a7340fdf185d/AD_4nXeRHTH5_AkodPi0U84ijj-3rofyTe9cNmIbzxCQEQoHuVwOM2xalX6WGTEbRr7xS7KaV9cjT_Bi92hOXEUQoAK3wrkbl13VWlJoSkjTcTjSZDAb_RzROGqqHbFZNIkNF2Jy2JyL.jpeg)

You can also access Lighthouse via Chrome Dev Tools by right-clicking on a page, selecting “**Inspect**,” clicking “**>>**” on the right, and choosing “**Lighthouse**.”

![“Lighthouse" selected from the "Inspect" drop-down menu](https://static.semrush.com/blog/uploads/media/95/3c/953cca798a1d6e5898f904dbf1b36cfa/982a24b03968dce50003474f370a0653/AD_4nXc27YjKA9e2Upcax1LYrB6XUmenCiabsd4NZYKmukqhZAIn0j3xcoWTFKwNdneU540MMQgOMyVkKml9RogT2MJBMIsmpCINvSfRx3xrWkHa41SbYsS4NRnlMAPzY0KKqwVFhkLYrQ.jpeg)

## How to Fix Largest Contentful Paint Issues: 12 Strategies

If a report from the previous step shows LCP issues, use the following techniques to fix them.

### 1. Identify the LCP Element

Identify the LCP element on the page you need to improve.

Use Google’s [PageSpeed Insights](https://pagespeed.web.dev/) to find this element.

Enter the page’s URL and click “**Analyze**.”

![PageSpeed Insights tool landing page](https://static.semrush.com/blog/uploads/media/9b/87/9b87236ba9b88b64239c598b9213b343/ac9b054f3d5f402e4fbd7a59895f6372/AD_4nXfUOEVPPxYxctXoZTjGhi2FpNvGwWiv2gmAKWT5ykZMz9a7YvBZmj7UrovN7FuqeRv5mi7jLbyzaCau573r1FD0NDQZxRGAkw4jn3ZoP0uUhBgl0zYv8KLVWZLlo-lyQLZf0i5C.jpeg)

After the tool generates the report, scroll to the “Diagnostics” section and click on“**Largest Contentful Paint element**.”

The tool will display the LCP element.

!["Largest Contentful Paint element" section under "Diagnostics" report](https://static.semrush.com/blog/uploads/media/3a/9f/3a9f1a5f4e474c7ade4ec90194a9bb0f/c1a397f0d22eb3a1ccdf1ff7cf3bc98b/AD_4nXdovzFXL7uQayQWs0FQifpxTcbCk0xh2ISLQdKeikx9WoIgXfNdauraH0gqK0c5S8X-4FXmRMoEy2bGzNGadklWTbes_MYuSH3sUiZDvPxfjEbtXxI1u25sQW3R9JasCGFVe9Sz.jpeg)

LCP elements vary by page. Sometimes, the LCP element is a heading or paragraph; sometimes it’s an image or a video poster image.

Knowing the LCP element allows you to choose the right optimization tactics.

### 2. Optimize Images

Large, high-definition images can load slowly and affect LCP.

Resize images and compress them using online image compression tools like https://kraken.io/ [Kraken](https://kraken.io/) or [Optimizilla](https://imagecompressor.com/).

Consider using a more performance-friendly format like WebP, which can be smaller than PNG or JPG images with little quality loss.

### 3. Optimize Fonts

Before any text can appear on a page, the selected fonts need to load.

The font you choose and delivery method can affect LCP if the LCP element is text.

If fonts are causing LCP issues, try these tips:

- Use [system fonts](https://fonts.google.com/knowledge/glossary/system_font_web_safe_font) that don’t require downloading
- Consider [self-hosting fonts](https://fonts.google.com/knowledge/using_type/self_hosting_web_fonts) to avoid external requests

- [Create subset fonts](https://fonts.google.com/knowledge/glossary/subsetting) to reduce file size and speed up loading
- Use [“font-display: optional”](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display) so the browser can show fallback fonts if custom fonts have not loaded yet

### 4. Minify JavaScript, CSS, and HTML Files

Minify JavaScript, CSS, and HTML files by removing unnecessary line breaks, spaces, and comments.

This reduces file sizes and speeds up loading.

Use an online code minification tool or a plugin like [Minifier](https://www.minifier.org/) if you use a content management system.

### 5. Remove Render-Blocking JavaScript and CSS Code

Resources like JavaScript and CSS code can block page rendering because the user’s browser needs to download the files before it can render the page.

Identify render-blocking resources using Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) Tool or similar methods.

Then, remove unnecessary code.

If a script or stylesheet isn’t needed for initial rendering, load it later.

### 6. Defer Non-Critical CSS

Separate your CSS into two categories: critical and non-critical.

Critical CSS styles the content visible as soon as the page loads (above-the-fold content).

Non-critical CSS styles content that appears below the fold.

Because below-the-fold content isn’t immediately visible, you can [delay its CSS](https://web.dev/defer-non-critical-css/). Load only the critical CSS first, then load non-critical CSS after the essential above-the-fold content appears.

### 7. Use Preloading for Critical Resources

Preloading tells the browser to prioritize and load specified resources early. These resources then remain available in the browser’s cache when needed.

By [preloading critical resources](https://web.dev/preload-critical-assets/)—such as CSS, fonts, and above-the-fold images—you can reduce delays and improve your LCP score.

### 8. Upgrade Your Web Hosting

Upgrading your web hosting can improve your server’s response time, which can enhance your LCP score.

Many websites use shared hosting, where multiple sites share one server.

Heavy traffic on neighboring sites can slow your site’s performance.

For optimal performance, switch to dedicated hosting from a reputable provider.

### 9. Enable Page Caching

Caching stores data in temporary storage (called a “cache”), speeding up subsequent page loads.

Page caching stores a static HTML copy of a page after its first load, reducing repeated database [queries](https://www.techtarget.com/searchdatamanagement/definition/query).

This approach works best on sites not relying on dynamic content. If your pages don’t change often, page caching may improve load times and LCP.

### 10. Use a Content Delivery Network

A Content Delivery Network (CDN) caches site content on multiple servers worldwide.

When users request your page, a server located near them delivers the content, reducing latency.

Popular CDN options include:

- Cloudflare
- Akamai
- KeyCDN

### 11. Limit Client-Side Rendering

Client-side rendering uses JavaScript in the browser to display content. Adding too much JavaScript can slow down rendering and impact your LCP score.

To improve performance, reduce the amount of JavaScript or compress and minify it.

Consider server-side rendering or a [hybrid approach](https://web.dev/rendering-on-the-web/#server-side-rendering) to handle content more efficiently.

### 12. Avoid Using Lazy Loading for Above-the-Fold Images

Lazy loading delays the loading of images until the user scrolls to them.

While this can [improve general page speed](https://www.semrush.com/blog/page-speed/), it may harm LCP if the LCP element is an above-the-fold image.

If the browser delays loading this critical element, LCP may worsen.

Only apply lazy loading to below-the-fold elements.

## Optimize LCP and Maximize Your Website’s Potential

Optimizing LCP aligns with Google’s page experience guidelines and improves user satisfaction. Better LCP can also support higher rankings in search results.

Check your site for LCP issues with our [free SEO audit](https://www.semrush.com/siteaudit/). Then, apply the techniques in this guide to enhance your LCP score further.
