---
title: "What Is A Trailing Slash & When Does It Matter"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "trailing-slash"
url: "https://ahrefs.com/blog/trailing-slash/"
canonical: "https://ahrefs.com/blog/trailing-slash/"
author: "Patrick Stox"
published: "2021-01-14T16:00:00+00:00"
updated: "2023-10-05T08:10:24+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T12:13:42+00:00"
status_code: 200
html_hash: "1ae21effa10b65d38655f3bd2cda8b063bf7cb474df5dc23ee76e42259d044ec"
clean_word_count: 1112
clean_char_count: 6486
---
# What Is A Trailing Slash & When Does It Matter

A trailing slash is a forward slash (“/”) placed at the end of a URL such as domain.com/ or domain.com/page/. The trailing slash is generally used to distinguish a directory which has the trailing slash from a file that does not have the trailing slash. However, these are guidelines and not requirements.

In the past, a folder would have a trailing slash and a file would be without the trailing slash. A folder would indicate there were more files and you’d typically have an index file (index.html, index.php, etc.) where the content of the page would load from. So the content would come from say domain.com/page/index.html but domain.com/page/ would be shown to users. With individual files, you’d have the file name and no trailing slash on the end.

These days, URLs in most systems aren’t pointing to files. The URL is a record stored in a database. Serverless systems don’t even host files on your server.

Different URL structures may be treated differently. Whether you choose to use a trailing slash or not is more of a personal preference than anything. Let’s look at some common scenarios.

## Trailing slashes after the domain name don’t matter

`domain.com` = `domain.com/`

These URLs are treated exactly the same and it doesn’t matter which version you use.

## Trailing slashes matter for other URLs

`domain.com/page` ≠ `domain.com/page/`

For every case besides the trailing slash directly after the root domain, a trailing slash will be treated as a separate URL.

## Files shouldn’t end in a slash

In most cases, if you add a trailing slash to a file such as .html, .php, .js, .css, .pdf, .jpg, etc., it won’t load the file. This is because most systems will assume that the file is a folder and since there’s nothing after this path, usually a 404 page will be returned.

Now let’s look at the impact on SEO.

## Trailing slashes and SEO

You may want to make different decisions depending on how your systems work. Here are a few common scenarios you may encounter.

### The same content is shown on trailing slash and non-trailing slash URLs

As I mentioned before, if your content can be seen on both the trailing slash version and non-trailing slash version of pages, the pages can be treated as separate URLs. The usual concern here is that the content on the different versions will cause [duplicate content](https://ahrefs.com/blog/duplicate-content/). In most cases, this shouldn’t be an issue because a [canonical tag](https://ahrefs.com/blog/canonical-tags/) is likely going to specify a preferred version. Even without that, Google will usually pick a preferred version for you where they will consolidate the signals. You can force the URLs to your preferred version if you want.

Whether you decide to use a trailing slash or not, you want to make sure that all the different [canonicalization signals](https://ahrefs.com/blog/canonicalization/) like [redirects](https://ahrefs.com/blog/301-redirects/), [sitemaps](https://ahrefs.com/blog/how-to-create-a-sitemap/), [internal links](https://ahrefs.com/blog/internal-links-for-seo/), canonical tags, etc. point to the version you want indexed.

### Different content is showing on the trailing slash and non-trailing slash URLs

In some cases where you have two systems sharing the same folder structure or with certain A/B testing software, you may end up with a situation where the version of a URL with and without the trailing slash shows completely different content. In these cases, you ideally want to pick one version to index and show to users and then redirect the other version to it.

### Hreflang

You may run into issues with more complex setups involving [hreflang](https://ahrefs.com/blog/hreflang-tags/). Hreflang links should point to the indexed version of the pages. If a canonical tag points to a version of the page with a trailing slash and Google indexes a page this way, but the hreflang tags point to a version of the page without a trailing slash, then these hreflang tags may not be respected.

## Adding or removing trailing slashes

This process will change depending on your system. It’s best to check relevant documentation before making any changes.

### .htaccess

**Remove slash:**

```
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)/$ /$1 [L,R=301]
```

Sidenote.

!-d looks for a directory and if one exists, it won’t remove the slash. If you don’t include this, you may end up breaking these main directory pages.

**Add slash:**

```
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*[^/])$ /$1/ [L,R=301]
```

Sidenote.

!-f looks for a file and if the file exists it doesn’t add the trailing slash. This keeps images, PDFs, JS, CSS, etc. from breaking.

### WordPress

If you go to Settings > Permalinks, you can change whether you use a trailing slash if you use a custom structure.

`/%postname%/` would add the trailing slash to URLs

`/%postname%` would remove the trailing slash from URLs

### JavaScript Frameworks

Because of their routers, these systems may be a bit different than you’re used to. You can either customize the way the URLs work in the router, or—if you don’t want to spend much time on it—most of these systems have pre-built modules to add or remove trailing slashes.

## Trailing slash impact on reporting

Reporting should be considered when determining whether to use a trailing slash or not. For instance, in Google Search Console, you can set up either a domain or URL prefix property. If you don’t include the trailing slash when setting up a URL prefix property (e.g. domain/folder), Google adds one anyway. As a result, all visits to domain.com/folder (without the trailing slash) won’t be reported because domain.com/folder/ (with trailing slash) is a level higher.

Google Analytics (GA) has the same issue when trying to do a content drilldown by folder if your main pages don’t have the slash. If slash and no slash versions of your URLs both work, then both may be reported in GA.

You can [add a filter](https://support.google.com/analytics/answer/1034823) as shown below to force trailing slashes on the URLs in your analytics reports if you want to consolidate the data.

Here’s the regex: `^(/[a-z0–9/_-]*[^/])$`

## Final thoughts

There’s always a risk with changes, so unless your setup is causing issues I wouldn’t try to force a change to your URLs. Technology has changed and the old URL conventions for slashes don’t apply on most modern websites.
