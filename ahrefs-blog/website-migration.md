---
title: "A Website Migration Takes More Than A Checklist To Be Successful"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "website-migration"
url: "https://ahrefs.com/blog/website-migration/"
canonical: "https://ahrefs.com/blog/website-migration/"
author: "Patrick Stox"
published: "2021-08-11T13:54:52+00:00"
updated: "2025-01-17T21:38:35+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
fetched_at: "2026-06-12T12:15:51+00:00"
status_code: 200
html_hash: "2a4e138f298aec78cb3f490c9d3e423f18da5343cdb213d71bb0c95253213e09"
clean_word_count: 1998
clean_char_count: 11819
---
# A Website Migration Takes More Than A Checklist To Be Successful

A website migration is any significant change to a website’s domain, URLs, hosting, platform, or design.

There are many different kinds of migrations, but the basic steps for planning and troubleshooting are similar. Migrations can be highly complex as they often involve many people and moving parts. Don’t panic if everything doesn’t go as planned; you can fix almost anything that goes wrong.

In this guide, we’ll cover:

- [Preparing for a website migration](#preparing)
- [Performing a website migration](#performing)
- [Testing and ongoing monitoring](#testing-and-monitoring)

## Preparing for a website migration

You need to know what is changing and who needs to be involved for it to happen. In other words, you need a plan and a place to track all the moving parts. You’ll need to know all of the people involved, their role, deadlines, and have a process in place to track everything. An [SEO project manager](https://ahrefs.com/blog/seo-project-management/) and project management system helps with this. Trying to do it all in email and Slack can get out of control fast.

You also want to have a rollback plan, just in case something goes horribly wrong. You should always have a way to get back to the original state, even if you only plan to use it in extreme situations.

You’ll want to know the impact of a move, so make sure you have access to GSC and Analytics on the old and new sites (make a combined view if needed to see both). Some changes may take a few weeks or even months where you may see flux, but others may not see any changes at all. For instance, if you’re migrating a mid-size site to a new domain, I’d expect a few weeks of flux. But if you’re combining into an existing site, you may not see any traffic disruptions at all.

You also want to do a bit of prep work. I suggest a few steps:

- **Crawl your website.** You’ll use this as a baseline to check for changes later on. You can use [Site Audit](https://ahrefs.com/site-audit) for this.
- **Create a set of test pages** such as those from the **Top Pages** report in [Site Explorer](https://ahrefs.com/site-explorer). You’ll use these later to check for errors. You may want to go ahead and crawl these in a separate Site Audit project so you can easily compare them later.
- **Restrict access to your staging or dev site (if you have one)** to prevent it from being indexed.
- **Make a backup of your site**, just in case you need to go back to it.

## Performing a website migration

Precisely what’s involved in a website migration depends on whether the URLs will remain the same or not. Below we’ll discuss both scenarios.

### When URLs are the same…

This is typically a more straightforward move—at least SEO-wise—since fewer things are changing. It still may be a complex move, but many of the tasks involved with these moves are typically more the work of infrastructure/DevOps or developers and not SEOs.

These migrations may include:

- **Hosting:** CDN, server
- **Platform**: CMS, language, JS framework
- **Design**: template, [internal links](https://ahrefs.com/blog/internal-links-for-seo/), tags

If you are using a staging or dev site, it’s best to get access to check for issues before you launch it live.

#### What to look for

For this, you’re essentially looking for any changes, including things like:

- **Canonical tags.** These should be the same.
- **Title tags.** Make sure these are the same or similar to what you have. New systems may have automated tag generation or some defaults that may be different than what you had.
- **Meta descriptions**
- **Heading tags**
- **Hreflang**
- **Schema**
- **Meta robots.** You want to make sure your pages aren’t noindexed.
- **Content.** This is especially important for JavaScript systems. New systems may not have all of the content loaded into the DOM by default, so search engines may not see some of the content in some cases.
- **Internal links.** Things like breadcrumbs, related posts, footer links, or even the main navigation may have changed.
- **Speed differences**

Use the comparison function of [Site Audit](https://ahrefs.com/site-audit) to see changes since your last crawl:

There are a couple more issues that may create more significant problems.

- If you accidentally leave a block in place, search engines can’t crawl your pages.
- Sometimes older redirects aren’t copied over from .htaccess files or server config files, and you’ll lose some of the links that were pointing to your site. This one is tricky because it’s harder to notice and often happens when changing hosts. Keep an eye on your **Best by links** report in [Site Explorer](https://ahrefs.com/site-explorer) and filter for 404s to see pages with links that are now broken.

### When URLs are different…

These migrations will usually be more complex. The exception is moving from HTTP to [HTTPS](https://ahrefs.com/blog/what-is-https/)—which is pretty easy these days.

These migrations may include:

- **Domain**: changing domain, merging into another site, splitting a site
- **Protocol**: HTTP > HTTPS
- **Path:** [subdomain/subfolder](https://ahrefs.com/blog/subdomain-vs-subfolder/), changing [site architecture](https://ahrefs.com/blog/website-structure/)

#### Specific to HTTP > HTTPS

- **Use a Content Security Policy of** **[upgrade-insecure-requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Upgrade-Insecure-Requests)** to fix all mixed content issues. It’s quick to implement and works for all resources besides things like internal links, which you still need to update yourself.
- **Install a security certificate**
- **301 redirect HTTP > HTTPS**
- **Add an** **[HSTS header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)**

I wouldn’t worry about things like a redirect chain on the root path or updating links to the site. Fixing the chain and updating links won’t provide any benefits since signals consolidate because of the redirects.

#### Specific to domain changes

- **Lower** **[TTL](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)****temporarily (a few hours for the value)**. This will refresh DNS caches faster and when you make the switch your changes will be seen by more users sooner.
- **Use the** **[change of address tool](https://support.google.com/webmasters/answer/9370220?hl=en)****in GSC**.
- **Check the old domain for any manual actions** that might be in place in GSC

Here’s a quick tip for Site Audit users: if you change the scope of your crawl in the project settings to a different domain, your new crawl will be on the new domain and you’ll be able to compare it to the crawl on the old domain.

#### All

- **Update internal links** and links in various tags like canonicals, hreflang, etc. You may be able to use a find and replace plugin to do this quickly for internal links.
- **Setup GSC**. This can include things like transferring your disavow file, setting geo-targeting, [URL parameter](https://ahrefs.com/blog/url-parameters/) settings, and uploading sitemaps. You’ll want to keep a sitemap with old URLs for a short period of time. This will help monitor indexing of URLs in GSC.
- **Remove any crawling blocks for pages on the old and new site**. Everything needs to be crawled for signals to consolidate properly.
- **Make sure pages you want indexed aren’t marked noindex**. You can use Site Audit for this.
- **Redirect pages**. You want to make sure old pages are redirected with a [301 redirect](https://ahrefs.com/blog/301-redirects/) to the new versions of your pages. It’s a good idea to redirect things like images and PDFs as well, but don’t worry about things like JS, CSS, or Font files. Focus on redirecting things that get indexed by search engines and don’t worry about other file types.

You want to catch changes as early as possible so if you have a dev or staging site, you should crawl this to make sure everything’s okay before pushing changes to a live site. Remember that if an old site was using HTTPS and the certificate expires, bots are passed but users will receive an error message and won’t be redirected. There are multi-domain certificates that cover multiple sites that can help prevent this issue.

If you see a drop, it’s likely related to redirects, something not being able to be crawled, something noindexed, changes to the content or removing content, changes to internal links, or something that changed related to technical SEO.

Sidenote.

 If you’re thinking about updating links to your site, you may want to update links from pages you control, but I wouldn’t bother doing outreach to update links on other sites that point to you. They should consolidate properly with the 301 redirects. It’s not worth the effort to get them changed.

## Testing and ongoing monitoring

There are various ways to watch the progress of the migration and make sure everything is progressing as it should.

### With Ahrefs

There are several various ways to look for changes. As I mentioned earlier, you can change the scope of your crawl in [Site Audit](https://ahrefs.com/site-audit) and get a comparison that shows you what changed. You’ll want to look out for changes to things like:

- **Canonicals**
- **Hreflang**. This will break for a while if you change domains since it will take some time for pages to be re-crawled and connections made.
- **Schema**
- **Meta robots**

The easiest way to check for any major drops is to create a Portfolio with the old domain and the new path or pages on the site. Then you can use the Site Explorer Overview report to look for any major traffic drops and use the compare mode in any of the other reports, like Organic Keywords, to zero in on where traffic may have been lost.

![Portfolio view of two websites that merged](https://ahrefs.com/blog/wp-content/uploads/2024/03/portfolio-view-of-two-websites-that-merged.png)

Depending on the setup, you may be able to just add the old domain as a competitor in the overview report to see how the migration went.

![Add merged website as a competitor to check for any traffic drops](https://ahrefs.com/blog/wp-content/uploads/2024/03/add-merged-website-as-a-competitor-to-check-for-an.png)

You’ll want to check the old URLs to make sure redirects were done, and all the content was migrated successfully.

To get a list of your most linked URLs, you can use the Best by links report in Site Explorer.

![Best by Links report in Ahrefs' Site Explorer](https://ahrefs.com/blog/wp-content/uploads/2024/03/best-by-links-report-in-ahrefs-site-explorer.png)

You can upload that list as a custom list in Site Audit in the URL sources tab. Alternatively, you could just select Backlinks as the source in this tab. I would remove any other crawl sources for this use case.

![Adding most linked URLs as a custom URL list in Site Audit](https://ahrefs.com/blog/wp-content/uploads/2024/03/adding-most-linked-urls-as-a-custom-url-list-in-si.png)

We’ll then crawl all the URLs with links. In Page Explorer, you can customize the table to include things like Redirect URL, Redirect status code, Final redirect URL, and Final redirect status code to get an easy view of all the redirects that are happening.

![Redirects in Site Audit's Page Explorer](https://ahrefs.com/blog/wp-content/uploads/2024/03/redirects-in-site-audits-page-explorer.jpg)

Make sure your redirects are 301 or 308 rather than 302 or 307 [status codes](https://ahrefs.com/blog/http-status-codes/) if you are doing a permanent move and want URLs indexed on the new website instead of the old one.

You should monitor the renewal of the old domains as well. You wouldn’t want a competitor registering them or for the site to be repurposed into something more nefarious.
