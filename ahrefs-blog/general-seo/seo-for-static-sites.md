---
title: "SEO for Static Sites: 8 Problems to Watch For"
source: "ahrefs-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "seo-for-static-sites"
url: "https://ahrefs.com/blog/seo-for-static-sites/"
canonical: "https://ahrefs.com/blog/seo-for-static-sites/"
author: "Despina Gavoyannis"
published: "2026-10-01T14:57:42+00:00"
updated: "2026-10-01T14:57:42+00:00"
categories:
  - "General SEO"
  - "Technical SEO"
freshness_reasons: []
fetched_at: "2026-10-12T10:03:02.274175+00:00"
status_code: 200
html_hash: "1da335656e231647e38609eb9c57c14fe57bc48a36a9d83b6586e01ad7637625"
clean_word_count: 3318
clean_char_count: 20518
---
# SEO for Static Sites: 8 Problems to Watch For

Vibe coding has made static websites easier than ever to build. You can spin up a site with Astro, Jekyll, Gatsby, Hugo, or another static framework without ever touching a traditional CMS.

But easier to build doesn’t necessarily mean easier to optimize.

WordPress and other CMSs quietly handle many SEO basics through plugins and built-in functionality, from canonicals and sitemaps to redirects, metadata, schema, and 404 handling.

With a static site, much of that work becomes your responsibility.

![Quotation marks](/assets/esbuild/quotation-marks-6PWBEG7B.svg)

Going static doesn't remove SEO work; it moves it, in my opinion. WordPress hides a load of defaults behind plugins, and static turns every one into a job you do yourself.

That doesn’t make static sites bad for SEO. It just means you need to know what your CMS used to do for you, and what you now need to build, configure, and monitor yourself.

## Common SEO issues on static sites

Static sites can be fast and technically clean, but they also leave more room for small [SEO mistakes](https://ahrefs.com/blog/seo-mistakes/) to slip through, since no CMS or plugin handles things in the background.

That becomes even more important with [vibe-coded sites](https://ahrefs.com/blog/vibe-coding-for-marketers-a-beginners-guide/). AI can build the page, but it won’t necessarily know which SEO conventions you want it to follow across the entire site.

Here are some of the most common issues to watch for:

|  |  |  |
| --- | --- | --- |
| Trailing slash and canonical conflicts | Your website host (such as Netlify) and static site framework (such as Astro) may disagree about whether a page URL should end with a slash. | Duplicate URLs and split ranking signals |
| Sitemaps that ignore noindex | Your sitemap may include pages you don’t want Google to show in search. | Drafts, thank-you pages, and other unwanted URLs can get indexed |
| Missing or misconfigured robots.txt | Your website may launch without a robots.txt file unless you create one yourself. | Important crawling rules can be missing or accidentally misconfigured |
|  | Images added outside your site’s usual image tools may not be resized or compressed automatically. | Larger page weight, slower loads, and missing alt text |
| Meta and schema template failures | A mistake in a shared template can appear on every page that uses it. | Duplicate or overlong titles, incorrect metadata, and broken schema at scale |
| Incorrect HTTP status codes | Missing pages can return a “success” response (200 OK) unless your 404 is set up correctly. | Soft 404s and wasted crawling |
| Inconsistent internal linking | Different templates and components can link to the same page in different ways, for example, with and without a trailing slash. | Crawl confusion and diluted internal linking signals |
|  | A basic sitemap setup can become difficult to manage when different pages need different rules. | Bloated, incomplete, or malformed sitemap files |
| Poor loading performance and Core Web Vitals | A static site can still load more JavaScript or CSS than a page actually needs. | Slower page loads and weaker Core Web Vitals |

A website audit is one of the easiest ways to catch these problems.

Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) crawls your site and surfaces over 170 technical SEO issues that may otherwise go unnoticed, which is especially useful when there’s no CMS or SEO plugin checking them for you.

## 1. Trailing slash and canonical conflicts

Static sites can accidentally make the same page accessible at two URLs, such as /page and /page/.

This usually happens because your static framework and hosting platform have different defaults for [trailing slashes](https://ahrefs.com/blog/trailing-slash/).

Your framework might generate one version while your host serves or redirects to another.

The problem is that your [canonical tags](https://ahrefs.com/blog/canonical-tags/), [internal links](https://ahrefs.com/blog/internal-links-for-seo/), and [redirects](https://ahrefs.com/blog/redirects-for-seo/) can then disagree about which URL is the preferred version. At best, that creates unnecessary redirects. At worst, search engines may see duplicate URLs, and ranking signals can get split between them.

### How to fix trailing slashes on static sites

Choose one URL format, with or without a trailing slash, and use it consistently across your site.

Configure both your framework and hosting environment to follow the same convention, then check that your canonical tags and internal links point to the version that actually resolves.

You can also crawl the site with Ahrefs’ Site Audit to find canonical conflicts, [redirect chains](https://help.ahrefs.com/en/articles/79340-what-are-redirect-chains), and internal links pointing to non-canonical URLs.

## 2. Robots.txt, sitemap and noindex conflicts

On a static site, your [XML sitemap](https://ahrefs.com/blog/how-to-create-a-sitemap/) is usually generated by code. The problem is that the [sitemap generator](https://ahrefs.com/sitemap-generator) may not know which pages you’ve marked as noindex.

That means URLs such as drafts, thank-you pages, confirmation pages, or other pages you don’t want in search can still end up in the sitemap.

This happens because there’s no CMS plugin keeping everything in sync for you. A page might be excluded from your main navigation or marked noindex, but still appear in the sitemap or RSS feed unless you’ve explicitly built logic to exclude it.

The setup can also become fragile as the site grows. A basic flat sitemap is fairly easy to manage, but things get more complicated once you need to split sitemaps by page type, exclude certain sections, or apply different rules to different templates.

Static sites can have a similar problem with robots.txt.

Depending on your framework and deployment setup, one may not be created automatically, so it’s worth checking that the file exists and contains the crawl rules you actually want. Just remember that [robots.txt controls crawling, not indexing](https://ahrefs.com/blog/indexed-though-blocked-by-robots-txt/), so it shouldn’t be used as a substitute for noindex.

### How to fix sitemaps on status sites

Create one rule for pages you want to keep out of search. For example, mark them noindex: true, then tell your sitemap and RSS feed to ignore any page with that label. Also check that your robots.txt file exists, points search engines to the correct sitemap, and doesn’t accidentally block sections you want crawled.

Recheck the logic whenever you add a new page type or change how pages are generated.

You can also use Ahrefs’ Site Audit to compare the URLs in your sitemap against indexability signals and catch pages that shouldn’t be there.

For instance, this report can help you track indexable pages that aren’t in your sitemap (and should be) and noindex pages that shouldn’t be in the sitemap but are.

## 3. Image optimization gaps

Some static-site frameworks include tools for resizing, compressing, and serving images more efficiently. But this is not universal. For example, Jekyll copies image files as they are by default, without automatically resizing, compressing, or converting them. To get those [image optimizations](https://ahrefs.com/blog/image-seo/) with Jekyll, you’ll need a plugin, an image CDN, or a separate image-processing step before you publish.

Even when a framework does have built-in image tools, they generally work only when you add images through the framework’s image pipeline.

For example, Next.js provides an <Image> component through next/image that automatically handles things like responsive sizing, optimization, lazy loading, and serving modern image formats. If you use a regular HTML <img> tag instead, you have to handle those optimizations yourself.

If you drop a raw image directly into the site, it can bypass that process entirely.

You can end up publishing an image file that is much larger than it needs to be, which can slow down page loads (especially on mobile). Or you might publish an image without [alt text](https://ahrefs.com/seo/glossary/alt-text), making it less accessible to people using screen readers and giving search engines less context about what the image shows. Because the site can still build successfully, neither problem is guaranteed to be caught before you publish.

That’s what makes this easy to miss, especially on vibe-coded sites. The page can look completely fine in a preview while still loading unnecessarily large images or incomplete image markup.

### How to optimize images on your static site

Use your framework’s image component or optimization pipeline consistently rather than dropping raw files straight into pages. Before publishing, check for oversized images and missing or blank alt text.

You can also crawl the site with Ahrefs’ Site Audit and check for issues like large image files, missing alt text, and other image-related SEO problems.

There is also a dedicated Images report that you can use to dig deeper into specific image issues:

## 4. Template-driven metadata and schema errors

On static sites, titles, meta descriptions, canonical tags, and [schema](https://ahrefs.com/blog/schema-markup/) are often generated from shared templates. That makes them efficient to manage, but it also means one bad default can affect hundreds of pages at once.

For example, adding your brand name automatically to every title could push a whole set of page titles beyond the length you intended.

The same applies to schema. If the template uses the wrong type, misses required properties, or structures relationships incorrectly, that mistake gets reproduced everywhere the template is used.

You can define a pattern once, such as adding the site name to every page title, and apply it across an entire content type. The difference is that Yoast gives you an SEO-specific interface for managing those rules.

On a static site, you may be building the same logic directly into your templates.

For example, Next.js lets you define a title template once in a shared layout and apply it across multiple pages. That’s convenient, but it also means a bad default can spread just as quickly.

Vibe coding can make this easier to miss. An AI-generated template may produce metadata or basic schema that looks reasonable without necessarily matching the page type or structure you actually need.

### How to fix template mistakes for static sites

Define the metadata and schema requirements for each page type before building the template. Then test multiple pages that use it, not just one example, whenever you make a change.

Ahrefs’ Site Audit can also help surface issues with titles, meta descriptions, canonical tags, and structured data across the site.

## 5. Incorrect HTTP status codes

A page can look like a 404 to a user while still returning a 200 OK status to search engines.

The page visibly showed a “404 — Page not found” message, but Chrome DevTools showed the request returning a 200 status. Google would treat this as a [soft 404](https://ahrefs.com/blog/what-is-soft-404/) because the page says it doesn’t exist while the server reports a successful response.

This can happen when 404 handling hasn’t been configured properly at the framework or hosting level. On Deltener’s Nuxt setup, the issue came from a generated 200.html SPA fallback being served for unknown routes.

The tricky part is that you won’t necessarily spot the same problem on your site just by looking at your pages. Look for when the design says “Page not found” while the underlying HTTP response says everything is fine.

### How to fix HTTP status handling for static sites

Create a proper 404 page, then test a few URLs you know don’t exist and check the actual HTTP response code. They should return 404, not just display a 404-looking page.

Ahrefs’ Site Audit can also surface URLs returning unexpected status codes, including soft 404s and broken internal links, so you can catch cases that aren’t obvious from browsing the site manually.

## 6. Internal linking inconsistencies

Static sites can end up with inconsistent internal links, especially when different templates or AI-generated components build URLs slightly differently.

For example, some links might point to /about, while others point to /about/. You may also end up mixing relative URLs like ../about/ with absolute URLs like https://example.com/about/.

None of these formats is inherently wrong, but problems arise when they don’t match the URL convention you’ve chosen for the site.

These problems can happen even to experienced teams. When we migrated our blog to a new website framework, a misconfigured internal linking rule meant we were nofollowing all of our internal links—effectively telling Google to ignore them. Not ideal:

These issues can create unnecessary redirects, send crawlers through multiple URL versions, and make it harder to keep internal linking signals focused on each page's canonical version. This is especially easy to introduce on vibe-coded sites, where AI-generated components may use different URL formats unless you explicitly tell the system which convention to follow.

### How to fix internal link inconsistencies on static sites

Pick one URL format and use it consistently across templates, navigation, breadcrumbs, and in-content links.

- **www vs non-www**: e.g. www.example.com or example.com
- **Trailing slash vs no trailing slash**: e.g. /about/ or /about
- **Absolute vs relative URLs**: e.g. https://example.com/about/ or /about/
- **HTTP vs HTTPS**: all internal links should point to the HTTPS version
- **Uppercase vs lowercase**: usually lowercase, e.g. /about-us/ rather than /About-Us/
- **File extensions vs clean URLs**: e.g. /about/ rather than /about.html
- **Hyphens vs underscores**: e.g. /seo-guide/ rather than /seo\_guide/
- **Parameter handling**: decide when URLs with query strings like ?sort=price should be linked to, canonicalized, or avoided
- **Default/index pages**: avoid mixing URLs like /about/, /about/index.html, and /about

Where possible, define that format once in a shared link component or helper rather than manually typing URLs throughout the site.

Then crawl the site to check for internal links that point to redirects or non-canonical URL versions. Ahrefs’ Site Audit can flag pages linking to redirects:

While the [Site Structure](https://ahrefs.com/academy/how-to-use-ahrefs/site-explorer/site-structure) report can help you inspect how URLs are organized by folder and link depth.

## 7. Technical performance issues

Static sites have a reputation for being fast, but static generation alone doesn’t guarantee good performance.

- Ship too much JavaScript
- Load CSS that isn’t needed on every page
- Use heavy third-party scripts
- Poorly load fonts or images
- Bundle code inefficiently

These problems can slow rendering and interactivity even when the HTML itself is generated ahead of time.

Vibe-coded sites are especially worth checking.

AI can keep adding scripts, libraries, animations, and components without necessarily considering their cumulative performance cost. A page may look polished in preview while getting heavier with every iteration.

### How to fix technical performance on static sites

Check the technical decisions behind the build, including:

- [**JavaScript**](https://ahrefs.com/blog/javascript-seo/)**:** avoid loading or activating unnecessary interactive code on every page.
- **Code splitting:** break large bundles into smaller chunks that load when required.
- **CSS:** avoid loading sitewide styles that are only needed on a few pages, and consider critical CSS for above-the-fold content.
- **Rendering strategy:** use static generation, server-side rendering, or other rendering methods based on what each page actually needs.
- **Images and fonts:** compress assets, use responsive images, preload only critical resources, and avoid unnecessary font weights.
- **Third-party scripts:** remove or defer scripts that aren’t essential to the initial page load.
- **Caching and CDN delivery:** make sure static assets are cached and served efficiently.

Then test the finished site rather than assuming a static build is fast. Use [PageSpeed Insights](https://pagespeed.web.dev/) to check [Core Web Vitals](https://ahrefs.com/blog/core-web-vitals/) such as LCP, INP, and CLS, and crawl the site to find performance problems across multiple pages.

You can also check Ahrefs’ Site Audit for specific reports on JavaScript and CSS errors:

## 8. Migration-specific SEO pitfalls

Moving from a CMS to a static site can introduce SEO problems even when the new pages look identical.

That’s because a [website migration](https://ahrefs.com/blog/website-migration/) often removes more than the CMS interface. You can also lose redirects, sitemap rules, metadata logic, schema, internal linking behavior, and other SEO settings that were previously handled in the background.

One of the biggest risks is URL changes.

If an old URL disappears without a proper 301 redirect to its replacement, any links and ranking signals pointing to that page may be lost.

You can easily check this with the [Ahrefs SEO toolbar.](https://ahrefs.com/seo-toolbar) Here’s an example from our recent international blog migration, moving from one subfolder structure to another:

It’s also easy to miss things like legacy canonicals, outdated sitemap entries, or stale assets being served from a build or cache.

### How to keep SEO performance after a migration to a static site

Treat the move as a full SEO migration, not just a redesign. Before launch:

- Map every old URL to its new destination.
- Add 301 redirects wherever URLs change.
- Compare old and new canonicals, metadata, schema, and sitemap rules.
- Check that important internal links still point to the right pages.
- Test the live site after launch, not just the preview or staging build.
- Crawl the old and new versions so you can spot missing pages, redirect errors, and other unexpected changes.

A static migration can absolutely work well, but don’t assume the new framework will recreate everything your old CMS was quietly doing for you.

## Which static site frameworks are better for SEO?

There isn’t one static framework that’s inherently “best for SEO.”

[Astro](https://astro.build/), [Next.js](https://nextjs.org/), [Gatsby](https://www.gatsbyjs.com/), [Hugo](https://gohugo.io/), [Jekyll](https://jekyllrb.com/), and similar frameworks can all support strong SEO, but the amount of work required varies depending on what you need to build. Things like canonicals, Open Graph tags, schema, sitemap rules, and noindex handling still need to be configured rather than assumed.

Image handling is one area where frameworks differ more noticeably.

Some, like Astro, have stronger built-in image tooling, while others leave more of the optimization work to you. But for metadata, schema, canonicals, and sitemap logic, the bigger difference usually comes down to how well you configure the framework rather than which one you choose.

So instead of asking “Which framework is best for SEO?”, ask:

- Does it handle the URL structure you want cleanly?
- How are canonicals and metadata generated?
- Can you control noindex rules and sitemap exclusions?
- What image optimization is built in?
- How easy is it to add and validate structured data?
- How much manual work will redirects, 404s, and internal linking require?

The right choice depends on the site you’re building and how much technical control you actually need.

![Quotation marks](/assets/esbuild/quotation-marks-6PWBEG7B.svg)

Not all businesses need a CMS. Not all businesses can live without one.

That’s probably the more useful decision framework. A small site with a handful of pages and infrequent updates may be a great fit for a static setup. A large publishing operation with complex workflows may not be.

## Final thoughts

Static sites can give you more control, fewer dependencies, and less reliance on plugins. But that control comes with more responsibility.

A traditional CMS hides a lot of SEO plumbing behind plugins and defaults. With a static or vibe-coded site, you’re more likely to own that plumbing yourself, from canonicals and sitemaps to redirects, schema, performance, and status codes.

Vibe coding makes the build process faster, but it doesn’t remove the need to understand what good technical SEO looks like.
