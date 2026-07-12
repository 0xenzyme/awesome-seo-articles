---
title: "What is technical SEO? Basics and best practices"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "technical-seo"
url: "https://www.semrush.com/blog/technical-seo/"
canonical: "https://www.semrush.com/blog/technical-seo/"
author: "Tushar Pol, Faizan Ali, Cecilia Meis"
published: "2023-02-01T15:56:00+00:00"
updated: "2026-04-23T09:22:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "time_sensitive_title"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T20:02:54+00:00"
status_code: 200
html_hash: "d27d0a7213c6d841dec52283f5e20fc5a5ac6f0ac1c1c6b7ad16b5c1272b2f85"
clean_word_count: 5284
clean_char_count: 35521
---
# What is technical SEO? Basics and best practices

## What is technical SEO?

Technical SEO is the work of optimizing a website's infrastructure so search engines and AI systems can crawl, render, index, and cite its content. It's the foundation that determines whether your pages are eligible to appear in traditional search results and AI-generated answers.

As search has expanded beyond traditional results into experiences like ChatGPT, Google AI Overviews, and CoPilot, getting the technical fundamentals right has become more consequential. Content quality alone doesn’t matter if search systems can’t reach or interpret your pages in the first place.

This guide walks through how crawling and indexing work, covers the best practices that most affect both traditional and AI search visibility, and shows you how to audit and maintain them on an ongoing basis.

## Why is technical SEO important?

Technical SEO is important because it determines whether search engines and AI systems can access, understand, and index your content.

Without a solid technical foundation, your best content won’t appear in search results or get cited in AI-generated answers, no matter how valuable it is.

That means lost traffic, missed business opportunities, and fewer chances to be references when users turn to AI for answers.

Technical SEO lays the foundation for everything else. It ensures search engines can crawl your site, render its content correctly, understand how pages relate to each other, and index the right versions.

That foundation now supports both traditional search results and AI-driven search features.

AI search systems like ChatGPT, Claude, and Gemini still rely on strong technical SEO fundamentals. If your pages aren’t crawlable or indexable, they’re far less likely to be surfaced or cited in AI-generated answers.

And when your site structure, rendering, and metadata are clear, it becomes easier for search systems to extract and interpret your content accurately.

## Understanding crawling and how to optimize for it

Crawling is an essential component of how search engines work. It’s also the first step toward both traditional search visibility and inclusion in AI-powered search experiences.

![How search engines work: content is published, spiders crawl site, Google indexes the page, page shows up in the results.](https://static.semrush.com/blog/uploads/media/01/71/01713554d7d43edc21f78b8d11f2a795/96a8f905aa07ce053a96f0ace4b95db5/image.png)

Crawling happens when search engines follow links on pages they already know about to find pages they haven’t seen before.

For example, every time we publish new blog posts, we add them to our main blog page.

![Semrush's main blog page showing all their most recently published articles.](https://static.semrush.com/blog/uploads/media/69/bb/69bb66e2c706b7ba5c868353ea9aeb59/cc2583d4fac71016dd23076ab9f79b1b/image.jpeg)

The next time a search engine like Google crawls our blog page, it can discover new pages through those internal links.

There are a few ways to ensure your pages are accessible to search engines:

### Create an SEO-friendly site architecture

[Site architecture](https://www.semrush.com/blog/website-structure/) (also called site structure) is the way pages are linked together within your site.

An effective site structure organizes pages in a way that helps crawlers find your website content quickly and easily. Clear relationships between pages also make it easier for search systems to understand how topics connect across your site.

So, ensure all the pages are just a few clicks away from your homepage when structuring your site.

Like this:

![SEO-friendly site architecture with a clear hierarchy: homepage, category pages, and individual pages.](https://static.semrush.com/blog/uploads/media/cf/11/cf11d34bf64af340d9321793c88d375a/1bd73901f184a90bb7b81f20602b8445/image.png)

This type of hierarchy helps search engines find and prioritize your pages more efficiently and ensures important content is just a few clicks from the homepage, reducing the number of orphan pages.

Orphan pages are pages with no internal links pointing to them, making it difficult (or sometimes impossible) for crawlers and users to find them.

If you’re a Semrush user, you can easily find whether your site has any orphan pages.

[Set up a project](https://www.semrush.com/kb/539-configuring-site-audit) in the [Site Audit](https://www.semrush.com/siteaudit/) tool and crawl your website.

Once the crawl is complete, navigate to the “**Issues**” tab and search for “orphan.”

![The "Issues" tab on Site Audit with "orphan" entered showing a list of related issues.](https://static.semrush.com/blog/uploads/media/50/5e/505e82eb8bd4db913ece8f1764df1885/2e1f39284201bd6ed9fd90262181a690/image.jpeg)

The tool shows whether your site has any orphan pages. Click the blue link to see which ones they are.

To fix the issue, add [internal links](https://www.semrush.com/blog/internal-links/) on non-orphan pages that point to the orphan pages.

### Submit your sitemap to Google

Using an [XML sitemap](https://www.semrush.com/blog/xml-sitemap/) can help Google find your webpages.

An XML sitemap is a file containing a list of important pages on your site. It lets search engines know which pages you have and where to find them.

This is especially important if your site contains a lot of pages. Or if they’re not linked together well.

Here’s what Semrush’s XML sitemap looks like:

![Semrush’s XML sitemap showing a list of pages and where to find them.](https://static.semrush.com/blog/uploads/media/a0/63/a06314ac96a473c9c72219f45be3a1fa/62763a1343f98938e4eb60ca724a94de/image.jpeg)

Your sitemap is usually located at one of these two URLs:

- yoursite.com/sitemap.xml
- yoursite.com/sitemap\_index.xml

Once you locate your sitemap, submit it to Google via Google Search Console (GSC).

Go to GSC and click “**Indexing**” > “**Sitemaps**” from the sidebar.

![Navigating to "Sitemaps" in the Google Search Console sidebar.](https://static.semrush.com/blog/uploads/media/66/5d/665d645bc1aea0c71f842f4da00738a4/195332f4b3d232707ff22e6e24162b6d/image.jpeg)

Then, paste your sitemap URL in the blank field and click “**Submit**.”

![Adding a new sitemap to GSC.](https://static.semrush.com/blog/uploads/media/30/84/3084fc4b60f84dea5a12b5bcbb632b52/237e33f01730db995bb7c456b29a9f7f/image.jpeg)

After Google is done processing your sitemap, you should see a confirmation message like this:

![Sitemap submitted successfully confirmation message on GSC.](https://static.semrush.com/blog/uploads/media/4a/35/4a35877383e8dab14dc0f55503beb368/550cf37570e72e49f2fb2fe1a8056605/image.jpeg)

### Allow the right AI crawlers

Your [robots.txt file](https://www.semrush.com/blog/beginners-guide-robots-txt/) controls whether search engines and AI crawlers (like OAI-SearchBot) can access your content.

Start by checking your robots.txt file for accidental blocking of important pages or resources. Your robots.txt file is usually located at **yoursite.com/robots.txt**.

![A robots.txt file showing which crawlers are allowed and disallowed.](https://static.semrush.com/blog/uploads/media/10/32/1032b112d9f67ba531bd3d8d9a229e91/e37f23096eeabf7303a2a5b80e1b0e1c/image.jpeg)

If your goal includes [visibility in ChatGPT search experiences](https://www.semrush.com/blog/chatgpt-seo/), make sure **OAI-SearchBot** isn’t blocked.

![A robots.txt file with OAI-SearchBot allowed.](https://static.semrush.com/blog/uploads/media/71/99/71991e0702bce9eced043ffaf887aa30/c05eeb1c9f7399b01896e1c090f54555/image.jpeg)

If you want a page excluded from search results, use the [noindex](https://www.semrush.com/blog/noindex/) tag. Blocking crawling alone doesn’t prevent URLs from appearing in results if other pages link to them.

### JavaScript rendering and crawlability

If your site relies heavily on JavaScript (for example, single-page applications), crawling alone isn’t enough — content often needs to be rendered before it’s visible to search engines.

Unlike Google, many AI crawlers (such as GPTBot, OAI-SearchBot, and ClaudeBot) don’t execute JavaScript. They rely on the initial HTML response, so any content that only appears after rendering may not be seen.

Google typically [processes JavaScript in phases](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics): crawling, rendering, and indexing.

![How Google processes JavaScript in phases: crawling, rendering, and indexing.](https://static.semrush.com/blog/uploads/media/7a/18/7a1893d7bf17c78882b6bf4bdc873e05/6bcc0a0ffe6f6f7699a57a0327aac66b/image.jpeg)

If key content or internal links only appear *after* rendering, make sure they load reliably and aren’t delayed or hidden behind user interactions.

Also avoid blocking JavaScript files or other resources needed for rendering in robots.txt, since that can prevent Google from seeing important on-page content. This is especially important for modern frameworks and single-page application sites where navigation and content loading happen client-side.

You can use [Site Audit](https://www.semrush.com/siteaudit/) to flag JavaScript-related issues, such as blocked resources or pages where important content may not be rendered correctly.

![The "Issues" tab on Site Audit with "javascript" entered showing a list of related issues.](https://static.semrush.com/blog/uploads/media/2a/5b/2a5bce59ab84b4da443ef8fdae43a8c6/5669316cd0891a86530603fa543f1402/image.jpeg)

Check out our [full guide to JavaScript rendering](https://www.semrush.com/blog/js-rendering/) for more info.

## Understanding indexing and how to optimize for it

Indexing is the process of analyzing and storing the content from crawled pages in a search engine's database — a massive index containing billions of webpages. Your pages must be indexed before they can appear in search results.

Your webpages must be indexed by search engines to appear in search results.

The simplest way to check whether your pages are indexed is to perform a “site:” operator search.

For example, if you want to check the index status of semrush.com, you’ll type “site:www.semrush.com” into Google’s search box.

This tells you (roughly) how many pages from the site Google has indexed.

![Google shows about 3,99,000 results for “site:www.semrush.com” search.](https://static.semrush.com/blog/uploads/media/c4/b2/c4b236825cda001c3c5e8f19d4758b93/34cbb8c8f530785220d48c34ab68360c/image.jpeg)

You can also check whether individual pages are indexed by searching the page URL with the “site:” operator.

Like this:

![SERP for “site:www.semrush.com/blog/what-is-seo/” with the top result highlighted.](https://static.semrush.com/blog/uploads/media/e2/c7/e2c7fad74d9f11ff9e85c13c658fee39/01e11027702abfd71843783b557f4fd1/image.jpeg)

There are a few things you should do to ensure Google doesn’t have trouble indexing your webpages:

### Use the noindex tag carefully

The “noindex” tag is an HTML snippet that keeps your pages out of Google’s index.

It’s placed within the <head> section of your webpage and looks like this:

`<meta name="robots" content="noindex">`

Use the noindex tag only when you want to exclude certain pages from indexing. Common candidates include:

- Thank you pages
- PPC landing pages
- Internal search result pages
- Admin and login pages
- Staging or test URLs
- Filter and sort variations of the same product listing

To learn more about using noindex tags and how to avoid common implementation mistakes, read our guide to [robots meta tags](https://www.semrush.com/blog/robots-meta/).

### Implement canonical tags where needed

When Google finds similar content on multiple pages on your site, it sometimes doesn’t know which of the pages to index and show in search results.

That’s when [“canonical” tags](https://www.semrush.com/blog/canonical-url-guide/) come in handy.

The canonical tag (rel="canonical") identifies a link as the original version, which tells Google which page it should index and rank.

The tag is nested within the <head> of a duplicate page (but it’s a good idea to use it on the main page as well) and looks like this:

`<link rel="canonical" href="https://example.com/original-page/" />`

## Additional technical SEO best practices

Creating an SEO-friendly site structure, submitting your sitemap to Google, and using noindex and canonical tags appropriately should get your pages crawled and indexed.

But if you want your website to be fully optimized for technical SEO, consider these additional best practices.

### 1. Use HTTPS

Hypertext transfer protocol secure (HTTPS) is a secure version of hypertext transfer protocol (HTTP).

It helps protect sensitive user information like passwords and credit card details from being compromised.

And it’s been a ranking signal [since 2014](https://developers.google.com/search/blog/2014/08/https-as-ranking-signal).

It also builds user trust and aligns with modern browser standards, which flag non-HTTPS sites as “Not secure.”

HTTPS is also a baseline signal for AI systems that surface and cite web content, as most major platforms prioritize secure sources when selecting what to reference.

You can check whether your site uses HTTPS by simply visiting it.

Just look for the “lock” icon to confirm.

![A browser address bar showing the lock icon next to a secure HTTPS website URL with the message "Connection is secure".](https://static.semrush.com/blog/uploads/media/70/7a/707a0eea770aa9e7571516aa511e8117/a54b2c5b2db1fac245c1ac256074a56e/image.jpeg)

If you see the “Not secure” warning, you’re not using HTTPS.

![A browser address bar displaying a “Not secure” warning next to a website URL.](https://static.semrush.com/blog/uploads/media/84/68/84689c567715672e07fe5e33c4ea5ea4/0ede8f5c8e5a3b3b2bbfe88561bee114/image.jpeg)

In this case, you need to install a secure sockets layer (SSL) or transport layer security (TLS) certificate.

An SSL/TLS certificate authenticates the identity of the website. And establishes a secure connection when users are accessing it.

You can get an SSL/TLS certificate for free from [Let’s Encrypt](https://letsencrypt.org/).

### 2. Find & fix duplicate content issues

[Duplicate content](https://www.semrush.com/blog/duplicate-content/) occurs when you have the same or nearly the same content on multiple pages on your site.

For example, Buffer had these two different URLs for pages that are nearly identical:

- https://buffer.com/resources/social-media-manager-checklist/
- https://buffer.com/library/social-media-manager-checklist/

[Google doesn’t penalize](https://developers.google.com/search/blog/2008/09/demystifying-duplicate-content-penalty) sites for having duplicate content.

But duplicate content can cause issues like:

- Undesirable URLs ranking in search results
- Backlink dilution
- Wasted [crawl budget](https://developers.google.com/search/blog/2017/01/what-crawl-budget-means-for-googlebot)

With Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool, you can find out whether your site has duplicate content issues.

Start by running a full crawl of your site and then going to the “**Issues**” tab.

![Semrush Site Audit dashboard with the “Issues” tab highlighted after completing a site crawl.](https://static.semrush.com/blog/uploads/media/aa/7e/aa7ea9ffe1a0a5fa1ca0644c83d62b4e/2105f23d556224373c4c40699e57fc68/image.jpeg)

Then, search for “duplicate content.”

The tool will show the error if you have duplicate content. And offer advice on how to address it when you click “**How to fix**.”

![Site Audit tool showing a duplicate content issue with the “Why and how to fix it” panel open.](https://static.semrush.com/blog/uploads/media/32/53/3253cd670af9ba768e5142d56366b5d1/891e9aacb36a1454501750ee9d110e5e/image.jpeg)

### 3. Make sure only one version of your website is accessible to users and crawlers

Users and crawlers should only be able to access one of these two versions of your site:

- https://yourwebsite.com
- https://www.yourwebsite.com

Having both versions accessible creates duplicate content issues and splits your backlink profile, so choose one version and redirect the other.

### 4. Improve your page speed

Page speed is a ranking factor both on [mobile](https://developers.google.com/search/blog/2018/01/using-page-speed-in-mobile-search) and [desktop](https://developers.google.com/search/blog/2010/04/using-site-speed-in-web-search-ranking) devices.

So, make sure your site loads as fast as possible.

You can use Google’s [PageSpeed Insights](https://pagespeed.web.dev/) tool to check your website’s current speed.

It gives you a performance score from 0 to 100. The higher the number, the better.

![Google PageSpeed Insights showing a mobile performance report with a performance score and diagnostic metrics.](https://static.semrush.com/blog/uploads/media/a0/c3/a0c3871dd3891e21a59f3bdcd5d2c97c/6e6d402e8b892f4711ac5d4e032d608d/image.jpeg)

Here are a few ideas for improving your website speed:

- **Compress your images**: Images are usually the biggest files on a webpage. Compressing them with image optimization tools like [ShortPixel](https://shortpixel.com/) will reduce their file sizes so they take as little time to load as possible.
- **Use a content distribution network (CDN)**: A CDN stores copies of your webpages on servers around the globe. It then connects visitors to the nearest server, so there’s less distance for the requested files to travel.
- **Minify HTML, CSS, and JavaScript files**: Minification removes unnecessary characters and whitespace from code to reduce file sizes. Which improves page load time.

### 5. Ensure your website is mobile-friendly

Google uses [mobile-first indexing](https://developers.google.com/search/blog/2016/11/mobile-first-indexing). This means that it looks at mobile versions of webpages to index and rank content.

As a result, your mobile pages need to contain the same core content, links, and structured data as your desktop version (known as "mobile parity"). If something is missing from the mobile version, it effectively doesn't exist for indexing or ranking. Google evaluates the mobile experience, not the desktop one.

To check this for your site, use the same [PageSpeed Insights](https://pagespeed.web.dev/) tool.

Once you run a webpage through it, navigate to the “SEO” section of the report. And then the “**Passed Audits**” section.

Here, you’ll see whether mobile-friendly elements or features are present on your site:

- [Meta viewport tags](https://www.semrush.com/blog/viewport-meta-tag/) — code that tells browsers how to control sizing on a page’s visible area
- Legible font sizes
- Adequate spacing around buttons and clickable elements

![PageSpeed Insights report showing the “Passed Audits” section with mobile-friendly checks such as viewport configuration and readable font sizes.](https://static.semrush.com/blog/uploads/media/b9/d2/b9d2c67ba360f6bbdbfc967267ca8c1b/d0caf95d73c40904a2605f8017671075/image.jpeg)

If you take care of these things, your website is optimized for mobile devices.

### 6. Use breadcrumb navigation

[Breadcrumb navigation](https://www.semrush.com/blog/breadcrumbs-for-websites/) (or “breadcrumbs”) is a trail of text links that show users where they are on the website and how they reached that point.

Here’s an example:

![A webpage showing breadcrumb navigation at the top of the page with links such as “Home / Men / Clothing / Jeans”.](https://static.semrush.com/blog/uploads/media/cd/ad/cdadc0019e20e2676bb676cff9f97575/9f339eb10ab1910514df68a25822965c/image.jpeg)

These links make site navigation easier.

How?

Users can easily navigate to higher-level pages without the need to repeatedly use the back button or go through complex menu structures.

So, you should definitely implement breadcrumbs. Especially if your site is very large. Like an ecommerce site.

They also benefit SEO.

These additional links distribute link equity ([PageRank](https://www.semrush.com/blog/pagerank/)) throughout your website. Which helps your site rank higher.

If your website is on WordPress or Shopify, implementing breadcrumb navigation is particularly easy.

Some themes include breadcrumbs out of the box. If yours doesn’t, most SEO plugins will add them automatically, or you can implement them manually with breadcrumb schema.

### 7. Use pagination

Pagination is a navigation technique that’s used to divide a long list of content into multiple pages.

For example, we’ve used pagination on our blog.

![The Semrush blog page showing pagination links at the bottom (e.g., 1, 2, 3) used to navigate through multiple pages of blog posts.](https://static.semrush.com/blog/uploads/media/84/07/8407b1396923d42ebf97e49b79d50660/70828089b17abf9283c005994ac938f8/image.jpeg)

This approach is favored over infinite scrolling, where content loads dynamically as users scroll. Because search engines may not access all dynamically loaded content, some pages may not be crawled or appear in search results.

Implemented correctly, pagination will reference links to the next series of pages. Which Google can follow to discover your content.

***Learn more****:* [*Pagination: What Is It & How to Implement It Properly*](https://www.semrush.com/blog/pagination-you-are-doing-it-wrong-part-1/)

### 8. Review your robots.txt file

A robots.txt file tells Google which parts of the site it should access and which ones it shouldn’t.

Here’s what Semrush’s robots.txt file looks like:

![A robots.txt file showing allow and disallow directives for different site directories.](https://static.semrush.com/blog/uploads/media/7f/0c/7f0c42096d760c62168c9d42cf5df5bf/b89df78789cf35dfee685259850b5814/image.jpeg)

Your robots.txt file is available at your homepage URL with “/robots.txt” at the end.

Here’s an example: yoursite.com/robots.txt

Check it to ensure you’re not accidentally blocking access to important pages that Google should crawl via the disallow directive.

For example, you wouldn’t want to block your blog posts and regular website pages. Because then they’ll be hidden from Google.

Refer back to the “Allow the Right AI Crawlers” section to learn how to check if you’re blocking them.

***Further reading****:* [*Robots.txt: What It Is & How It Matters for SEO*](https://www.semrush.com/blog/beginners-guide-robots-txt/)

### 9. Implement structured data

Structured data (also called schema markup) is code that helps Google better understand a page’s content.

And by adding the right structured data, your pages can win rich snippets.

Rich snippets are more appealing search results with additional information appearing under the title and description.

Here’s an example:

![Google SERP with a recipe rich snippet with star ratings, number of reviews, and cooking time highlighted.](https://static.semrush.com/blog/uploads/media/a0/85/a08508a9a6afc6ef1f0aeb88e0ec6f5b/577357df7d2fb3efbb7deb21a116db49/image.jpeg)

The benefit of rich snippets is that they make your pages stand out from others. Which can improve your click-through rate (CTR).

Structured data also helps search engines understand what a page is about and the key elements on it — such as products, organizations, recipes, events, and reviews.

This clearer understanding improves how search systems interpret your content. And it can make your information easier to reuse in search features and AI-powered answers.

On the flip side, if the markup doesn’t match what users see, search engines may ignore it or flag it as misleading.

So, when implementing structured data, make sure it accurately reflects the visible content on the page — meaning the details in your markup (such as product names, prices, or ratings) should match what users can actually see.

![The visible on-page content like product name, price, and ratings matching the details in the markup.](https://static.semrush.com/blog/uploads/media/42/82/42828a62499506e32a8ed1f586f9e959/6fbc5d792763384fc43965906eb9d503/image.jpeg)

Google supports [dozens of structured data markups](https://developers.google.com/search/docs/appearance/structured-data/search-gallery), so choose one that best fits the nature of the pages you want to add structured data to.

For example, if you run an ecommerce store, adding product structured data to your product pages makes sense.

Here’s what the sample code might look like for a page selling the iPhone 15 Pro:

`<script type="application/ld+json">
{
"@context": "https://schema.org/",
"@type": "Product",
"name": "iPhone 15 Pro",
"image": "iphone15.jpg",
"brand": {
"@type": "Brand",
"name": "Apple"
},
"offers": {
"@type": "Offer",
"url": "",
"priceCurrency": "USD",
"price": "1099",
"availability": "https://schema.org/InStock",
"itemCondition": "https://schema.org/NewCondition"
},
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": "4.8"
}
</script>`

There are plenty of free structured data generator tools like [this one](https://technicalseo.com/tools/schema-markup-generator/). So you don’t have to write the code by hand.

And if you’re using WordPress, you can use the [Yoast SEO plugin to implement structured data](https://yoast.com/help/implementing-schema-with-yoast-seo/).

### 10. Find & fix broken pages

Having broken pages on your website negatively affects user experience.

Here’s an example of what one looks like:

![A browser window displaying a website 404 error page, on](https://static.semrush.com/blog/uploads/media/e2/f3/e2f386b8e18a2afacb54e9f2b4784f9c/b90489c6cdd0a639ca97981a7940e491/image.jpeg)

And if those pages have backlinks, they go wasted because they point to dead resources.

To find broken pages on your site, crawl your site using Semrush [Site Audit](https://www.semrush.com/siteaudit/).

Then, go to the “**Issues**” tab. And search for “4xx.”

![The "Issues" tab on Site Audit with "4xx" entered showing a list of related issues.](https://static.semrush.com/blog/uploads/media/5d/2d/5d2dee83c81ad858126f97d0f5f64e5d/d48c92e890e39f11ffb21d699ff32f29/image.jpeg)

It’ll show you if you have broken pages on your site. Click on the **“#****pages**” link to get a list of pages that are dead.

![A list of URLs with 4xx status codes displayed inside the Site Audit tool.](https://static.semrush.com/blog/uploads/media/79/b8/79b8fc3aff799fc5f8f9bc4bec2c739f/0860863c2907377e8b01e003e9b7d263/image.jpeg)

To fix broken pages, you have two options:

- Reinstate pages that were accidentally deleted
- Redirect old pages you no longer want to other relevant pages on your site

After fixing your broken pages, you need to remove or update any internal links that point to your old pages.

To do that, go back to the “**Issues**” tab. And search for “internal links.” The tool will show you if you have broken internal links.

![The "Issues" tab on Site Audit with "internal links" entered showing a list of related issues and "90 internal links are broken" clicked.](https://static.semrush.com/blog/uploads/media/92/f7/92f714210c070cf29b9118bdf9d50529/92cbb289e41881e3bc71ad7187ac393d/image.jpeg)

If you do, click on the “**# internal links**” button to see a full list of broken pages with links pointing to them. And click on a specific URL to learn more.

![A report inside Site Audit showing incoming internal links pointing to a broken page.](https://static.semrush.com/blog/uploads/media/9b/80/9b80ec0079fd6cc072c702ffa2e99829/86663d434b985d998bed0910504c4cdf/image.jpeg)

On the next page, click the “**# URLs**” button, found under “Incoming Internal Links,” to get a list of pages pointing to that broken page.

![A list of pages pointing to a broken page on Site Audit.](https://static.semrush.com/blog/uploads/media/c8/e3/c8e39e090eb3e96b4d4f102ad11be57e/0e5cf04e176e210aae10c8ce24f012c7/image.jpeg)

Update internal links pointing to broken pages with links to their updated locations.

### 11. Optimize for Core Web Vitals

Core Web Vitals are metrics [Google uses to measure user experience](https://developers.google.com/search/blog/2020/11/timing-for-page-experience).

These metrics include:

- **Largest Contentful Paint (LCP)**: Calculates the time a webpage takes to load its largest element for a user
- **Interaction to Next Paint (INP)**: Measures how quickly a page responds to user interactions
- **Cumulative Layout Shift (CLS)**: Measures the unexpected shifts in layouts of various elements on a webpage

To ensure your website is optimized for the Core Web Vitals, you need to aim for the following scores:

- **LCP**: 2.5 seconds or less
- **INP**: 200 milliseconds or less
- **CLS**: 0.1 or less

You can check your website’s performance for the Core Web Vitals metrics in Google Search Console.

To do this, visit the “**Core Web Vitals**” report.

![The “Core Web Vitals” report on Google Search Console.](https://static.semrush.com/blog/uploads/media/ae/d2/aed26c70b63111b033c9cc1d384398a5/5391d5897a2cf6a9c842a7206e7c43d7/image.jpeg)

Run our free [SEO checker](https://www.semrush.com/siteaudit/) for a fast Core Web Vitals check.

For deeper site-wide coverage, use Semrush Site Audit. Navigate to "Core Web Vitals" and click "**View details**."

![Site Audit Overview report with “Core Web Vitals” highlighted.](https://static.semrush.com/blog/uploads/media/99/1c/991c1a925d4ca7e654fa6240ddad9b8c/1c151d4ee9a464b02c35d7f0275dceff/image.jpeg)

This will open a report with a detailed record of your site's Core Web Vitals performance and recommendations for fixing any issues.

![Core Web Vitals performance report from the Semrush Site Audit tool showing metrics and recommendations.](https://static.semrush.com/blog/uploads/media/78/48/784874ce33903263fcb5ef6b26306c23/54790587e0477e94bc4308ab2c8cc187/image.jpeg)

***Further reading****:* [*Core Web Vitals: A Guide to Improving Page Speed*](https://www.semrush.com/blog/core-web-vitals/)

### 12. Use hreflang for content in multiple languages

If your site has content in multiple languages, you need to use [hreflang tags](https://www.semrush.com/blog/hreflang-attribute-101/).

Hreflang is an HTML attribute used for specifying a webpage's language and geographical targeting. And it helps Google serve the correct versions of your pages to different users.

For example, we have multiple versions of our homepage in different languages. This is our homepage in English:

![The Semrush homepage in English.](https://static.semrush.com/blog/uploads/media/ea/bb/eabbce4f1137b734f27822fbc6b69310/1a0141cf5ddab231e9abef1af99f2c59/image.jpeg)

And here’s our homepage in Spanish:

![The Semrush homepage in Spanish.](https://static.semrush.com/blog/uploads/media/b0/11/b011ef2ceaaf798f85d57f71eae751f1/22cd3288fa4c4417a2f4b13685246e4e/image.jpeg)

Each of our different versions uses hreflang tags to tell Google who the intended audience is.

This tag is reasonably simple to implement.

Just add the appropriate hreflang tags in the <head> section of all versions of the page.

For example, if you have your homepage in English, Spanish, and Portuguese, you’ll add these hreflang tags to all of those pages:

`<link rel="alternate" hreflang="x-default" href="https://yourwebsite.com" />
<link rel="alternate" hreflang="es" href="https://yourwebsite.com/es/" />
<link rel="alternate" hreflang="pt" href="https://yourwebsite.com/pt/" />
<link rel="alternate" hreflang="en" href="https://yourwebsite.com" />`

### 13. Stay on top of technical SEO issues

Technical optimization isn't a one-off thing. New problems will likely pop up over time as your website grows in complexity.

That’s why regularly monitoring your technical SEO health and fixing issues as they arise is important.

You can do this using Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool. It monitors over 140 technical SEO issues.

For example, if we audit Petco’s website, we find three issues related to redirect chains and loops.

![3 redirect chains and loops error shown in Site Audit tool](https://static.semrush.com/blog/uploads/media/2b/37/2b374a994328eb3104e1140569a2869b/bcbdb5ee38cf28b9c70e9142a18c4a97/image.jpeg)

Redirect chains and loops are bad for SEO because they contribute to a negative user experience.

And you’re unlikely to spot them by chance. So, this issue would have likely gone unnoticed without a crawl-based audit.

Regularly running these technical SEO audits gives you action items to improve your search performance.

Monitoring tools can also help track visibility in newer search experiences. For example, Bing Webmaster Tools' [AI Performance](https://bing.com/webmasters/aiperformance) report shows how often your content is cited across Microsoft Copilot, Bing's AI-generated summaries, and select partner integrations.

![Bing Webmaster Tools’ AI Performance report showing metrics like total citations and average cited pages.](https://static.semrush.com/blog/uploads/media/46/3f/463f603741dcae0a097606b9abf1a3f6/7dc5b6e8cd7a65f02f0e9758a48822af/image.jpeg)

### 14. Reduce ambiguity across formats

Keep your text, images, videos, and structured data consistent across the page. Use the same names, labels, and descriptions for key topics or entities throughout.

Search systems analyze multiple types of content on a page, not just text. They may evaluate images, videos, captions, structured data, and surrounding content to understand what a page is about.

When these elements all clearly refer to the same topic or entity, it’s easier for search engines and AI systems to interpret and reuse your content.

For example, take a look at Apple's Refurbished iPhone page.

![Consistent naming across on-page content and structured data all referencing the same product or entity.](https://static.semrush.com/blog/uploads/media/c8/ea/c8ea710ee3cfefb5001fad028b88e546/a172b7ea3e6f62f9a757a389404a20fc/image.jpeg)

The same entity appears consistently across multiple surfaces:

- The H1 and supporting body copy both lead with "Refurbished iPhone"
- The page title and meta description repeat the same entity ("Refurbished iPhone Deals - Apple")
- Open Graph tags (og:title, og:description, og:url) all reference "refurbished iPhone"
- The URL path itself includes /refurbished/iphone

When visible content, page metadata, and URL structure all point to the same entity, search engines and AI systems get a clearer signal about what the page is about. If those surfaces drift apart — captions referring to one product, metadata to another, body copy to a third — the page becomes harder to interpret and easier for AI systems to skip over.

To reduce ambiguity and help search engines better understand your content:

- Use consistent names for products, topics, or entities across text, images, and metadata
- Write descriptive alt text and captions that reflect the page topic
- Ensure filenames and surrounding text match the content of images or videos
- Align structured data with the visible page content

## Putting it all together

Technical SEO covers a lot of ground, but you don't need to fix everything at once. Start with the fundamentals — crawlability, indexability, HTTPS, and mobile experience — then work through the practices that affect your site most. Pages with strong technical foundations stay eligible to be surfaced and cited in both traditional search results and AI-generated answers.

The most reliable way to find out where your site stands today is to run a full audit, then revisit your priorities each quarter as your site grows and search behavior continues to shift.
