---
title: "10 SEO Issues That Really Matter & How to Fix Them"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "seo-issues"
url: "https://ahrefs.com/blog/seo-issues/"
canonical: "https://ahrefs.com/blog/seo-issues/"
author: "Mateusz Makosiewicz"
published: "2023-01-31T05:46:34+00:00"
updated: "2026-03-25T10:58:33+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
fetched_at: "2026-06-12T12:05:46+00:00"
status_code: 200
html_hash: "9e1c400ef3e1573cf52b20549f6b562d88df0e04e359b4338bf631339205098f"
clean_word_count: 3716
clean_char_count: 22364
---
# 10 SEO Issues That Really Matter & How to Fix Them

Last year, we dug deep into a [study of over a million domains](https://ahrefs.com/blog/site-audit-study/) to figure out the most common technical SEO problems.

Surprisingly, the ones you see the most aren’t necessarily the ones you should be losing sleep over. They may be worth fixing, but definitely not putting on the top of your list.

For instance, we found that meta descriptions were missing on 72.9% of studied sites. But these don’t impact rankings, and Google will generate one for you in that case, anyway. Conversely, a serious issue of a canonical page pointing to a broken page was found on only 2.6% of sites.

So if you want to fix issues that can seriously impact your rankings, here’s a better idea. You can use the [free Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) and [Google Search Console](https://search.google.com/search-console/about) to see if your site is affected by any of the nine issues we listed in this article.

Read on to learn why these issues matter and how to use the tools to find and fix them.

Update: In February 20226, Google updated its documentation clarifying that [Googlebot crawls only the first 2 MB of supported file types](https://developers.google.com/search/docs/crawling-indexing/googlebot), including HTML. Any content beyond that limit is ignored. It’s unlikely to affect most sites, but it’s a critical problem wherever it does occur—so I’ve added it to this list.

## 1. Indexability issues

Indexability is a webpage’s ability to be indexed by search engines. Depending on the issue, Google will index the wrong pages or won’t be able to display it in the SERPs (and you won’t get any traffic to these pages).

Here are some examples of these issues:

- **Canonical points to 4XX** — Only valid live URLs should be specified as canonicals. When the search engine crawler is not able to access the specified canonical page, this instruction will be ignored, and wrong (non-canonical) page version can be indexed.
- **Canonical points to redirect** — Similar or duplicate pages of a website must specify the canonical page to instruct search engines to show the most authoritative (canonical) version of the page in search results.

Three requirements must be met for a page to be indexable:

1. **The page must be crawlable.** If you haven’t blocked [Googlebot](https://ahrefs.com/blog/googlebot/) from entering the page [robots.txt](https://ahrefs.com/blog/robots-txt/) or you have a website with fewer than 1,000 pages, you probably don’t have an issue there.
2. **The page must not have a noindex tag** (more on that in a bit).
3. **The page must be** [**canonical**](https://ahrefs.com/blog/canonicalization/) (i.e., the main version).

### How to fix

Sign up for a free account of [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) and set up your project (you can do it in a [few clicks](https://help.ahrefs.com/en/articles/4455322-setting-up-your-first-project-in-ahrefs-webmaster-tools-awt)). Next:

1. Open [**Site Audit**](https://ahrefs.com/site-audit)**.**
2. Go to the **Indexability** report.
3. Click on issues related to canonicalization and “noindex” to see affected pages.

![Indexability issues in Ahrefs' Site Audit.](https://ahrefs.com/blog/wp-content/uploads/2024/01/word-image-171485-1.jpg)

For canonicalization issues in this report, you will need to replace bad URLs in the link rel=“canonical” tag with valid ones (i.e., returning an “HTTP 200 OK”).

As for pages marked by [“noindex” issues](https://help.ahrefs.com/en/articles/2429909-what-does-noindex-page-warning-in-site-audit-mean), these are the pages with the “noindex” meta tag placed inside their code. Chances are, most of the pages found in the report should stay as they are. But if you see any pages that shouldn’t be there, simply remove the tag. Do make sure those pages aren’t blocked by [robots.txt](https://ahrefs.com/blog/robots-txt/) first.

Click on the question mark on the right to see instructions on how to fix each issue. For more detailed instructions, click on the “Learn more” link.

## 2. Broken pages

Broken pages are pages on your site that return 4XX errors (can’t be found) and 5XX errors (server errors). These pages either won’t be indexed by Google or will be dropped from the index; either way, you’re potentially missing out on traffic and creating a bad experience for your visitors.

Furthermore, if broken pages have backlinks pointing to them, all of that [link equity](https://ahrefs.com/seo/glossary/link-equity) goes to waste.

Broken pages are also a waste of [crawl budget](https://ahrefs.com/blog/crawl-budget/)—something to watch out for on bigger websites.

### How to fix

In [AWT](https://ahrefs.com/webmaster-tools), you should:

1. Open [**Site Audit**](https://ahrefs.com/site-audit)**.**
2. Go to the **Internal pages** report.
3. See if there are any broken pages. If so, the **Broken** section will show a number higher than 0. Click on the number to show affected pages.

In the report showing pages with issues, it’s a good idea to add a column for the number of referring domains. This will help you make the decision on how to fix the issue.

Now, fixing broken pages (4XX error codes) is quite simple, but there is more than one possibility. Here’s a short graph explaining the process:

Dealing with server errors (the ones reporting a 5XX) can be a tougher one, as there are different possible reasons for a server to be unresponsive. Read [this short guide](https://help.ahrefs.com/en/articles/2453036-what-does-5xx-page-error-mean-in-site-audit) for troubleshooting.

With [AWT](https://ahrefs.com/webmaster-tools), you can also see 404s that were caused by incorrect links to your website. While this is not a technical issue per se, reclaiming those links may give you an additional SEO boost.

1. Go to [**Site Explorer**](https://ahrefs.com/site-explorer)
2. Enter your domain
3. Go to the **Best by links** report
4. Add a “**404 not found**” filter
5. Then sort the report by referring domains from high to low

## 3. Few or no internal links

An [internal link](https://ahrefs.com/blog/internal-links-for-seo/) is any hyperlink leading to the page or resource on the same website. They can affect rankings by:

- Helping search engines like Google to find and crawl pages
- Boosting pages with [PageRank](https://ahrefs.com/blog/google-pagerank/) (aka link juice or link equity) passed down from stronger pages.

In the worst case scenario, pages that you want to rank won’t have any internal links. These pages are called orphan pages. Web crawlers have limited ability to access those pages (only from sitemap or backlinks), and there is no link equity flowing to them from other pages on your site.

A more likely scenario is that some pages could rank higher or rank for additional keywords if they had more relevant links.

### How to fix

1. Go to [**Site Audit**](https://ahrefs.com/site-audit)**.**
2. Open the **Links** report.
3. Open the **Issues** tab.
4. Scroll to the **Indexable** category.

An orphan page needs to be either linked to from some other page on your website or deleted if a given page holds no value to you.

Sidenote.

Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) can find orphan pages as long as they have backlinks or are included in the sitemap. For a more thorough search for this issue, you will need to analyze server logs to find orphan pages with hits. Find out how in [this guide](https://ahrefs.com/blog/orphan-pages/#how-to-find-orphan-pages).

As for internal link opportunities, AWT identifies these automatically:

1. Go **Site Audit**.
2. Open the **Internal link opportunities** tool.

Focus on the columns labeled “source page,” “keyword context,” and “target page” in your documentation. These columns will guide you on which webpage to link from, which webpage to link to, and the specific location on the page where the link should be added.

For example, there are a few relevant internal links we can add to our list of SEO statistics:

## 4. Mobile experience issues

Having a mobile-friendly website is a must for SEO. Two reasons:

1. **Google uses** [**mobile-first indexing**](https://ahrefs.com/blog/mobile-first-indexing/) — it’s mostly using the content of mobile pages for indexing and ranking pages.
2. **Mobile experience is part of the** [**Page Experience signals**](https://developers.google.com/search/docs/appearance/page-experience) — while Google will allegedly always “promote” the page with the best content, page experience can be a tiebreaker for pages offering content of similar quality.

Here are some examples of these issues:

- **Viewport not set** — when a page does not have a `<meta name=“viewport”>`, `tag` or `width` or `initial-scale` parameters.
- **Tap targets too small or too close together** — when interactive elements are not large enough or their tappable areas overlap.
- **Document uses plugins** — when a page requires plugins, such as Java or Flash.

### How to fix

In Ahrefs Site Audit, look for these issues under the **Usability and performance** category.

Next, click on the question mark next to the issue name and use the instructions to solve the issues for affected pages (they will require some web development work).

For example, if the tool finds pages with a font too small for mobile devices, you will need to make sure that the [viewport tag is set properly](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag) and make the font at least 12 px.

## 5. HTTPS issues

Google uses HTTPS encryption as a [small ranking signal](https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html). This means you can experience lower rankings if you don’t have a TLS certificate to secure your website.

But even if you do, some pages and/or resources on your pages may still use the HTTP protocol.

### How to fix

Assuming you already have an SSL/TLS certificate for all subdomains (if not, do get one), open [AWT](https://ahrefs.com/webmaster-tools) and do these:

1. Open [**Site Audit**](https://ahrefs.com/site-audit)
2. Go to the **Internal pages** report
3. Look at the protocol distribution graph and click on **HTTP** to see affected pages
4. Inside the report showing pages, add a column for **Final redirect URL**
5. Make sure all HTTP pages are [permanently redirected](https://ahrefs.com/blog/redirects-for-seo/) (301 or 308 redirects) to their HTTPS counterparts

Finally, let’s check if any resources on the site still use HTTP:

1. Inside the **Internal pages** report, click on **Issues.**
2. Then click on **HTTPS/HTTP mixed content** to view affected resources.

The quickest way to fix this is to add this short code in your .htaccess file or server config.

```
<ifModule mod_headers.c>
Header always set Content-Security-Policy "upgrade-insecure-requests;"
</IfModule>
```

This configuration ensures that whenever a browser requests a page or resource from the server, it will automatically convert any HTTP requests to HTTPS for enhanced security.

Further reading

- [What Is HTTPS? Everything You Need to Know](https://ahrefs.com/blog/what-is-https/)

## 6. Performance and stability issues (Core Web Vitals)

Google’s Core Web Vitals (CWV) is a set of metrics designed to gauge a website’s user experience, mainly in terms of loading and responsiveness speed. They are part of [Google’s Page Experience signals](https://developers.google.com/search/docs/appearance/page-experience), impacting search engine rankings.

That said, from an SEO perspective the goal isn’t to be the fastest site or the “most usable” one but to score at least “good” in these three categories:

- **[Largest Contentful Paint (LCP)](https://ahrefs.com/blog/largest-contentful-paint-lcp/)**. This measures how long it takes for the biggest content element on the screen (like an image, video, or large text block) to fully load after you request a webpage. It’s a key indicator of how quickly a visitor can see content on the page.
- **Interaction to Next Paint (INP).** It evaluates the page’s responsiveness to user actions. It measures how long it takes for the page to react to clicks, taps, and key presses. The INP value reflects the longest response time for these interactions, excluding extreme cases. This metric replaces [First Input Delay (FID)](https://ahrefs.com/blog/first-input-delay-fid/) in March 2024.
- **[Cumulative Layout Shift (CLS)](https://ahrefs.com/blog/cumulative-layout-shift-cls/).** CLS totals up all the unexpected movements of page elements while the page is loading. A higher score indicates more shifting, which can be frustrating for users trying to read or interact with the page. This metric helps identify and minimize these shifts to improve the user experience.

### How to fix

Probably the fastest way to check for CWV for an entire site is to use the free Google Search Console.

1. Click on **Core Web Vitals** in the **Experience** section of the reports.
2. Click **Open report** in each section to see how your website scores.
3. For pages that aren’t considered good, you’ll see a special section at the bottom of the report. Use it to see pages that need your attention.

Optimizing for CWV may take some time and some web dev skills. This may include things like moving to a faster (or closer) server, compressing images, optimizing CSS, etc. We’re explaining how to do this [in the third part of this guide to CWV.](https://ahrefs.com/blog/core-web-vitals/#3-cwv-components)

## 7. Unoptimized website structure

Unoptimized website structure in the context of technical SEO is mainly about important organic pages too deep into the website structure.

Pages that are nested too deep (users need more than 6 clicks from the website to get to them) will receive less link equity from your homepage (likely the page with the most backlinks), which may affect their rankings. This is because link value diminishes with every link “hop.”

Website structure is important for other reasons too, such as the overall user experience, crawl efficiency, and helping Google understand the context of your pages. Here, we’ll only focus on the technical aspect, but you can read more about the topic in our full guide: [Website Structure: How to Build Your SEO Foundation](https://ahrefs.com/blog/website-structure/).

### How to fix

1. Open **Site Audit** and go to the Structure Explorer (in the menu on the left-hand side)**.**
2. Configure the **Segment** to only **valid HTML pages** and click **Apply.**

1. Switch to the **Depth** tab, and set the data type to **Data table.**
2. Use the graph to investigate pages with more than six clicks away from the homepage.

The way to fix the issue is to link to deeper nested pages from pages closer to the homepage. More important pages could find their place in site navigation, while less important ones can be just linked to the pages a few clicks closer.

It’s a good idea to weigh in user experience and the business role of your website when deciding what goes into sitewide navigation.

For example, we could probably give our [SEO glossary](https://ahrefs.com/seo/glossary) a slightly higher chance to get ahead of organic competitors by including it in the main site navigation. Yet we decided not to because it isn’t such an important page for users who are not particularly searching for this type of information.

Instead, moved the glossary only up a notch by including a link inside the beginner’s guide to SEO (which itself is just one click away from the homepage).

## 8. Lack of relevant schema markup

[Schema markup](https://ahrefs.com/blog/schema-markup/) is code that helps Google understand the information on a page, which can be used to show rich results (also known as rich snippets).

Schema markup is not a ranking factor, and it can’t make you rank higher in text results.

However, schema markup can make your pages eligible to rank in rich results. Google displays these for some search queries in spots that really stand out in the SERPs; some even show up on top of the standard text results.

This is especially important for pages with the following types of content:

- Recipes.
- Job ads.
- Videos.
- News articles.
- Information about events/landing pages for events.
- Details about movies.

### How to fix

There are various methods you can generate and validate schema for free. You can use a tool like Merkle or Schema or semi-automate the process with ChatGPT.

ChatGPT is worth highlighting here because it’s able to recognize the relevant type schema for any page. Simply plug and URL if your page is already live or upload the copy if not live yet and ask AI to generate schema. You can use the following prompt:

```
Generate a ready-to-use schema in JSON-LD format for the following: [your URL or content].
```

Next copy the code and run it through [Google’s Rich Results Test](https://search.google.com/test/rich-results) just to double-check everything is in order.

Finally, apply the code to the page. If you’re using a popular CMS like WordPress or Wix, look for a schema markup plugin/app. Otherwise, you may need to add the code to each eligible page [manually](https://codelabs.developers.google.com/codelabs/structured-data/index.html#3).

You can also use AWT to look for any schema issues across the entire site. You will find these issues under the **Others** section of the **All issues report**.

Tip

Optimizing pages with schema markup is an effective way to get more clicks from pages that already rank high—we’re explaining the details in this [guide to schema.](https://ahrefs.com/blog/schema-markup/)

## 9. Duplicate content

Duplicate content happens when exact or near-duplicate content appears on the web in more than one place.

In cases of duplicate content, [Google will choose one of the pages](https://youtu.be/wsrL6l2Fxvo?si=EyZn7dJ495FPhe0H&t=260) to show in the SERPs, but it won’t necessarily be the page you want to be indexed.

> If we find exactly the same information on multiple pages on the web, and someone searches specifically for that piece of information, then we’ll try to find the best matching page ( … ) So if you have the same content on multiple pages then we won’t show all of these pages.
>
>
>
> John Mueller, Search Advocate [Google](https://www.google.com)

Content duplication is not necessarily a case of intentional or unintentional creation of similar pages. There are other less obvious causes, such as [faceted navigation](https://ahrefs.com/blog/faceted-navigation/), [tracking parameters in URLs](https://ahrefs.com/blog/url-parameters/), or using [trailing and non-trailing slashes](https://ahrefs.com/blog/trailing-slash/).

### How to fix

First, check if your website is available under only one URL. If your site is accessible as:

- http://domain.com
- http://www.domain.com
- https://domain.com
- https://www.domain.com

… then Google will see all of those URLs as different websites.

The easiest way to check if users can browse only one version of your website: type in all four variations in the browser, one by one, hit enter, and see if they get redirected to the master version (ideally, the one with HTTPS).

You can also go straight into Site Audit’s **Duplicates** report. If you see 100% [bad duplicates](https://help.ahrefs.com/en/articles/2115215-what-are-good-and-bad-duplicates-in-site-audit), that is likely the reason.

In this case, choose one version that will serve as canonical (likely the one with HTTPS) and permanently redirect other versions to it.

Then run a **New crawl** in Site Audit to see if there are any other bad duplicates left.

There are a few ways you can handle bad duplicates, depending on the case. Learn how to solve them in our [guide](https://help.ahrefs.com/en/articles/2134268-how-to-resolve-bad-duplicates-found-on-ahrefs-site-audit).

Further reading

- [Duplicate Content: Why It Happens and How to Fix It](https://ahrefs.com/blog/duplicate-content/)

## 10. Oversized HTML pages

[Googlebot will only process the first 2 MB of a page’s raw (uncompressed) HTML](https://developers.google.com/search/docs/crawling-indexing/googlebot#size-limit). Everything after that is ignored. For most pages, 2 MB is plenty, but unoptimized pages with things like heavy embedded CSS/JS can blow past it without anyone noticing—the browser renders everything fine, but Googlebot quietly stops reading.

That means content, links, and structured data near the bottom of an oversized page may never get indexed.

### How to fix

You can check whether the issue happens on your site with the free Ahrefs Webmaster Tools. Open Site Audit, go to All issues, and look for the “Page size exceeds Googlebot’s 2 MB crawl limit”.

Get the uncompressed HTML under 2 MB by tackling the most common culprits:

- **Inline base64 images.** Replace them with normal external image files.
- **Embedded SVGs and large JSON blocks.** Move them to separate files or simplify them.
- **Inline CSS and JavaScript.** Move these to external `.css` and `.js` files.
- **Bloated markup.** CMS themes and page builders often inject redundant HTML. Inspect the source and clean up.

## Final thoughts

When you’re done fixing the more pressing issues, dig a little deeper to keep your site in perfect SEO health. Open [Site Audit](https://ahrefs.com/site-audit) and go to the **All issues** report to see other issues regarding on-page SEO, image optimization, redirects, localization, and more. In each case, you will find instructions on how to deal with the issue.

Some issues, e.g., indexability issues, can be fixed directly in Site Audit using the [Patches](https://help.ahrefs.com/en/articles/9775727-how-patches-work-in-site-audit) feature (part of the [Project Boost Max add-on](https://help.ahrefs.com/en/articles/10130957-what-are-project-boost-add-ons)). No need to constantly swap windows with your CMS or rely on a developer. Worth considering it if you’re working on a big site or managing multiple clients.

For example, here you can see fixing blog post titles right from Site Audit—you can even ask AI for suggestions.

Did I miss any important technical issues? Let me know [on X](https://twitter.com/m_makosiewicz) or [LinkedIn](https://www.linkedin.com/in/mateusz-makosiewicz-38154b67/).
