---
title: "Duplicate, Google Chose Different Canonical Than User. What It Is, Causes, & How to Fix"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "duplicate-google-chose-different-canonical-than-user"
url: "https://ahrefs.com/blog/duplicate-google-chose-different-canonical-than-user/"
canonical: "https://ahrefs.com/blog/duplicate-google-chose-different-canonical-than-user/"
author: "Patrick Stox"
published: "2024-06-25T12:44:50+00:00"
updated: "2025-01-17T23:50:10+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
fetched_at: "2026-06-12T11:27:51+00:00"
status_code: 200
html_hash: "a7fbb2711d30c8220cdcf15646cf7693af63a96e3b972ca723773f7f2c198fac"
clean_word_count: 1526
clean_char_count: 8995
---
# Duplicate, Google Chose Different Canonical Than User. What It Is, Causes, & How to Fix

The Google Search Console status “Duplicate, Google chose different canonical than user” means that Google chose a different URL to index than the one the user selected. This can happen when Google finds two or more pieces of content on a site that are very similar or identical.

The issue will show in the Page Indexing report in Google Search Console. This is how it looks.

![Duplicate, Google chose a different canonical than user error in the GSC Page indexing report](https://ahrefs.com/blog/wp-content/uploads/2024/06/duplicate-google-chose-a-different-canonical-than.png)

When I check on one of our pages with this issue, I see that the content hasn’t been translated yet for either language. It’s still in English, so I suspect that we have more of these pages that still have the issue. There’s a bit of a delay in our translation process that causes this issue.

Let’s look at what causes the issue and how to fix it.

## What causes “duplicate, Google chose different canonical than user”

There are a few things that might cause a page to be flagged with this issue.

### Duplicate or similar content

According to Google’s Gary Illyes, 60% of the web is [duplicate content](https://ahrefs.com/blog/duplicate-content/).

https://twitter.com/lilyraynyc/status/1509176261884747781

Google doesn’t want to store every version of every page. They store one main version of the page and then create records of the alternates.

The canonical link element, or [canonical tag](https://ahrefs.com/blog/canonical-tags/), is one of [~20 canonicalization signals](https://ahrefs.com/blog/canonicalization/) that Google uses. It’s a hint, and so other signals can tell Google that it’s a different page that should actually be the indexed version of the page shown to users.

All of the signals will consolidate to the indexed version of the page, and many of these other pages will be flagged as duplicates. If their specified canonical URL doesn’t match, then you’ll see them with the issue “duplicate, Google chose a different canonical than user.” This isn’t usually an issue and usually won’t impact rankings, but it may not be the page you prefer to be shown.

There may be several URLs for the same content, which leads to duplicate content issues. This may be caused by capitalization, [trailing slashes](https://ahrefs.com/blog/trailing-slash/), IDs, [URL parameters](https://ahrefs.com/blog/url-parameters/), etc. So all of these may exist:

```
domain.com/Abc
domain.com/abc
domain.com/123
domain.com/?id=123
```

Another time you may see this issue is if you have an ecommerce store that has many product variants without having much unique content. The product variants may have self-referencing canonical tags, but Google may only index one of the versions of the page.

If you only want one version indexed, you should set a self-referencing canonical and either canonical tags from other versions that reference the main version or redirect the other versions to the main version.

Check the **Duplicates** report in [Site Audit](https://ahrefs.com/site-audit). We break down which duplicate clusters have canonical tags set and which have issues.

This issue may also show for international websites. Sometimes companies use the same content or similar content for multiple countries that use the same language. For example, companies may use the same or similar content on pages targeting the US, UK, and AU. Google will usually index one of these, but thanks to the magic of [hreflang tags](https://ahrefs.com/blog/hreflang-tags/), they can still swap and show the alternate versions in search results.

There’s also the case that I showed earlier, where we published content in English on pages meant for another language. These were waiting for translation and should be resolved when they are translated.

Those alternate versions usually show as “duplicate, Google chose a different canonical than user” in GSC. Google will even report traffic just to the canonical version in GSC, even if they’re swapping and showing users the correct versions.

Hreflang tags work in pairs to form a cluster. We have a cluster visualization tool in Site Audit that shows and tells you what is broken, making it much easier to understand and explain than the typical spreadsheet.

And sometimes Google just gets it wrong. With [syndicated content](https://ahrefs.com/blog/content-syndication/), Google can occasionally choose the copied content as the canonical URL instead of the original.

This can also happen with content that is stolen. We had this happen to one of our pages a while back. Google chose the other site to index for our original content!

This may resolve itself over time, and in our case it took just a few days. If you own the content that’s being used on another website, you may be able to file a claim based on the Digital Millennium Copyright Act (DMCA). You can use [Google’s Copyright Removal tool](https://www.google.com/webmasters/tools/dmca-dashboard) to do what’s called a DMCA takedown, which requests the removal of any copyrighted material.

### Canonical tag mistakes

Similar to what happens with [redirects](https://ahrefs.com/blog/redirects-for-seo/), canonical tags can also have chains or loops. The extra pages may be classified as “duplicate, Google chose a different canonical than user.”

A canonical chain is a series of URLs whose canonical tags point to the next URL in the chain.

You also may run into canonical loops, where one of the chains points back to a page that was earlier in the sequence. This forms an infinite loop.

You can check for these issues in Site Audit. We show them under the issue “Non-canonical page specified as the canonical one,” which appeared on 1.36% of websites in our [study of 1 million domains](https://ahrefs.com/blog/site-audit-study/).

You might also see this issue if you accidentally made a mistake in your canonical tag, such as including an extra character. Pages may still resolve, but Google may choose your original URL as the canonical URL.

### Rendering issues

With JavaScript websites, particularly app shell models, the initial HTML response may show very little content and code. In fact, every page on the site may display the same code, which may be the exact same as the code on some other websites.

If you see a high number of duplicate pages in the same cluster in Site Audit, you may have this issue.

This can sometimes cause pages to be treated as duplicates and not immediately go to rendering. Even worse, the wrong page or even the wrong site may show in search results. This should resolve itself over time but can be problematic, especially with newer websites.

## How to fix “duplicate, Google chose different canonical than user”

How you fix the issue will depend on which issue applies to your page.

### If your content is duplicate, make it more unique

If you have content that’s the same or duplicate and you want each of the pages indexed, you’ll have to put in some work to make them more unique. This is common on websites with a lot of boilerplate content with very little unique content for their pages.

Most of the pages I see as an issue for our website come from a delay in our translation process. We sometimes publish pages for other languages before they are translated or fully translated, which leads them to be flagged as duplicates. As we translate the pages, the issues are cleared out. Translated pages are not considered duplicates.

### If you have canonicalization issues, fix them

For any canonical chains or loops, choose your preferred version of the page and make sure that it, as well as all other versions of the page, references your preferred version.

You may even want to use stronger canonicalization signals to consolidate the pages, such as a [301](https://ahrefs.com/blog/301-redirects/) or 308 redirect.

If you made any mistakes with your canonical tag (e.g., including an extra character) and Google has ignored it, you can fix the issue by fixing the canonical tag to point to the main version of the page.

### If you have rendering issues, use a pre-render or SSR

If your problem is coming from the returned HTML on your site all looking the same, you may want a pre-rendering or server-side rendering (SSR) solution. This will render the content of the page before users or bots receive it. That content on most sites would include some unique content and should clear up this issue. Talk to your devs if you need to set this up.

## Final thoughts

“Duplicate, Google chose different canonical than user” usually happens with duplicate pages, but not always. Usually, Google is trying to keep its index clean and not have a bunch of duplicates, or Google is trying to fix a mistake on the website.

Have questions? Message me on [X](https://twitter.com/patrickstox) or [LinkedIn](https://www.linkedin.com/in/patrickstox/).
