---
title: "How to Avoid Ruining SEO During a Website Redesign"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "website-redesign-seo"
url: "https://ahrefs.com/blog/website-redesign-seo/"
canonical: "https://ahrefs.com/blog/website-redesign-seo/"
author: "Mateusz Makosiewicz"
published: "2024-03-18T14:38:27+00:00"
updated: "2024-05-22T14:50:52+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T12:16:00+00:00"
status_code: 200
html_hash: "e0391ed2ee3712e251771bea4294a1f4703806cf4dfb8c86a9addd8645a2cffb"
clean_word_count: 1560
clean_char_count: 9496
---
# How to Avoid Ruining SEO During a Website Redesign

It’s too easy to break your SEO during a website redesign. Here’s a foretaste of what can go wrong:

- Loss of rankings and traffic.
- Loses of link equity.
- Broken pages.
- Sluggish page loading.
- Bad mobile experience.
- Broken internal links.
- Duplicate content.

For example, this site deleted about 15% of organic pages (yellow line) during the redesign, which resulted in an almost 50% organic traffic loss (orange line). Interestingly, even the growth of referring domains (blue line) afterward didn’t help it recover the traffic.

![Website redesign with bad consequences for SEO - example. ](https://ahrefs.com/blog/wp-content/uploads/2024/03/website-redesign-with-bad-consequences-for-seo-e.png)

Fortunately, it’s not that hard to avoid these and other common issues - just six simple rules to follow.

## 1. Keep a backup of the old site

Easily overlooked but could save the day. A backup ensures you can restore the original site if anything goes wrong.

Ask the site’s developer to be prepared for this fallback strategy. All they will need to do then is redirect the domain to the folder with the old site, and the changes will take effect almost instantly. Make sure they don’t overwrite any current databases, too.

It won’t hurt to make a backup yourself, too. See if your hosting provider has a backup tool or use a plugin like Updraft if you’re using WordPress or a similar CMS.

## 2. Test staging site for mobile friendliness and Core Web Vitals

Testing your site for [Core Web Vitals](https://ahrefs.com/blog/core-web-vitals/) (CWV) and mobile friendliness before it goes live is the best way to ensure that your new site will comply with [Google’s page experience guidelines](https://developers.google.com/search/docs/appearance/page-experience).

The thing is, a website redesign can seriously affect site speed, stability, responsiveness, and mobile experience. Some design flaws will be quite easy to spot, such as excessive use of animations or layout not scaling properly on mobile devices, but not others, like unoptimized code.

Ask your site developer to run mobile friendliness and CWV tests on template pages as soon as they are ready (no need to test every single page) and ask for the report. For example, they should be able to run Google Lighthouse on a [password-protected website](https://github.com/GoogleChrome/lighthouse/blob/main/docs/authenticated-pages.md).

Tip

You can run these tests yourself on password-protected sites with Ahrefs if you’re on the Advanced plan. When setting up a new crawl, open the **Crawl settings** tab.

To test both desktop and mobile versions, you will need to run two separate tests with the right user agent:

The authentication option is right below:

Finally, get a [free CWV API key](https://developers.google.com/speed/docs/insights/v5/get-started) and paste it here (you need to do this only once per project):

Once the crawl is complete, look for the highlighted issues in the **All issues** report.

## 3. Run a site audit pre and post-launch

An [SEO audit](https://ahrefs.com/blog/seo-audit/) uncovers SEO issues on your site. And if you do it pre-and post-launch, you will easily spot any potential new problems caused by the redesign, especially those that really matter, such as:

- Unwanted [noindex](https://ahrefs.com/seo/glossary/noindex-tag) pages.
- Sites accessible both as http and https.
- Broken pages.

So before the new site goes, click on **New crawl** in **Site Audit** and then again right after it goes live.

Then after the crawl, go to the **All issues** report and look at the Change column - new errors found between crawls will be colored red (fixed errors will be green) .

You might want to give some issues higher priority than others. See our take on the [most impactful technical SEO issues](https://ahrefs.com/blog/seo-issues/).

Tip

You can access the history of site audits by clicking on the project’s name in **Site Audit**.

## 4. Keep the old URL structure

By URL structure, I mean the way web addresses are organized and formatted. For example, these would be considered URL structure changes:

- *ahrefs.com/blog* to *ahrefs.com/blog/*
- *ahrefs.com/blog* to *ahrefs.com/resources/blog*
- *ahrefs.com/blog* to *blog.ahrefs.com*
- *ahrefs.com/site-audit* to *ahrefs.com/site-audit-tool*

Altering that structure in an uncontrolled process can lead to:

- **Broken redirects**: redirects leading to non-existing or inaccessible pages.
- **Broken backlinks**: external links pointing to deleted or moved pages on your site.
- **Broken internal links**: internal site links that don’t work, hindering site navigation and content discoverability.
- **Orphan pages**: pages not linked from your site, making them hard for users and search engines to find.

Naturally, you should keep the old URL structure unless you’re *absolutely sure* you know what you’re doing. In this case, you will need to put some [redirects](https://ahrefs.com/blog/redirects-for-seo/) in place. On top of that, make sure to submit a [sitemap via Google Search Console](https://ahrefs.com/blog/how-to-create-a-sitemap/#section5) to help Google reflect changes on your site faster.

Tip

Google also advises submitting a new sitemap if you’re adding many pages in one go. You may want to do that if that’s the case in your redesign project.

## 5. Keep important organic pages

Redesigns often include some kind of content pruning or simply arbitrary deleting of older content. But whatever you do, it’s crucial that you keep the pages that are already ranking high.

Traffic is one reason, but since these pages are already ranking, chances are they’ve got some backlinks you risk losing.

To make sure you’re not cutting out the good stuff, use two reports in [Ahrefs’ Site Explorer](https://ahrefs.com/site-explorer): **Top pages** and **Best by links**.

**Top pages** report is a list of all the pages on your site ranking in the top 100, appended with [SEO data](https://ahrefs.com/blog/seo-data/) and sorted by traffic by default. So, just one click on your left-hand side, and you’ll see a list of your best “traffic generators”.

The **Best by links** report follows the same logic, but the focus is on links (both external and internal) and it shows all crawled pages on your site (not only the ones ranking in top 100).

You can also plug in any page in **Ahrefs’ Site Explorer** and see whether it can be cut without any damage to the site’s organic performance.

Recommendation

If part of the redesign is an inventory cleanup, you can still get traffic to products you don’t offer anymore if you create an “archive” page and link to a place where visitors can find more similar products. E-commerce sites and hardware brands do that regularly.

This way, you can still rank for related terms, and the user experience is better than simply redirecting old products to new products.

Further reading

- [Follow Our Content Audit Process (Template Included)](https://ahrefs.com/blog/content-audit/)

## 6. Minimize modifications to pages with high rankings

Lastly, if you find yourself in a situation where the new design imposes significant changes to your top-ranking pages, take extra caution when altering these elements:

- **Keywords in text, title and H1s**: changing keywords can alter the page’s relevance for corresponding queries. For instance, if a product page ranks for “kick scooter for kids”, you might lose that if you start scratching the phrase out from the crucial parts of the content.
- **Depth of content**: expanding or reducing content should be done with the intent to serve user needs better, provide more value, or clarify existing information (i.e., [search intent](https://ahrefs.com/blog/search-intent/)). Keep in mind that Google rewards [helpful, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), and not necessarily creative, persuasive copywriting.
- **Internal links**: changing/cutting a few [internal links](https://ahrefs.com/blog/internal-links-for-seo/) shouldn’t do any harm, but you need to be tactical about it - ask yourself if any particular change could hurt the ranking. Keep in mind that internal links aid the flow of [link equity](https://ahrefs.com/seo/glossary/link-equity) and help Google understand the context of pages.
- **Distance of that page from the homepage**: keep high-value pages close to the homepage to signal their importance to search engines.
- **Schema markup**: any changes should aim to accurately describe the content and take advantage of eligible [schema](https://ahrefs.com/blog/schema-markup/) properties.
- **Page speed**: don’t overuse heavy graphics, animations, and video. Again, make sure to pre-test the staging site for CWV and run a site audit right after the launch.

## Final thoughts

While an overall site redesign might sound like a good moment to introduce some SEO, you need to think about the traffic and backlink equity the site has already earned. If you change too much in one go, you won’t know what worked and why, and maybe more importantly, what didn’t work and how to fix it.

Truth is, SEO is always about experimentation. You can have a well-educated guess, but you can never really know what will happen.

Want to share your SEO story here? Let me know on [X](https://twitter.com/m_makosiewicz) or [LinkedIn](https://www.linkedin.com/in/mateusz-makosiewicz-38154b67/).
