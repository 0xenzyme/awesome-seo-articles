---
title: "Meta Tags for SEO: A Simple Guide for Beginners"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "seo-meta-tags"
url: "https://ahrefs.com/blog/seo-meta-tags/"
canonical: "https://ahrefs.com/blog/seo-meta-tags/"
author: "Joshua Hardwick"
published: "2020-02-05T01:10:51+00:00"
updated: "2024-04-10T13:35:00+00:00"
categories:
  - "On-Page SEO"
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T12:06:15+00:00"
status_code: 200
html_hash: "40352b6950023fd7875d60c1c9dcd3f1f78b9b0397b501a49202bd42b070fb39"
clean_word_count: 3188
clean_char_count: 19662
---
# Meta Tags for SEO: A Simple Guide for Beginners

Meta tags are snippets of code that tell search engines important information about your web page, such as how they should display it in search results. They also tell web browsers how to display it to visitors.

Every web page has meta tags, but they’re only visible in the HTML code.

In this guide, you’ll learn how to use, and not to use, the six most important meta tags for SEO:

1. [Meta title](#meta-title)
2. [Meta description](#meta-description)
3. [Meta robots](#meta-robots)
4. [Meta refresh redirect](#meta-refresh-redirect)
5. [Meta charset](#meta-charset)
6. [Meta viewport](#meta-viewport)

## Meta title

This is the page title that Google and most [other search engines](https://ahrefs.com/blog/alternative-search-engines/) show in search results.

Sidenote.

Google doesn’t always show the title tag. It sometimes shows something different.

### Why it’s important for SEO

Google [explains](https://support.google.com/webmasters/answer/35624?visit_id=636880082951453933-4272044119&rd=1) it best:

> Titles are critical to giving users a quick insight into the content of a result and why it’s relevant to their query. It’s often the primary piece of information used to decide which result to click on, so it’s important to use high-quality titles on your web pages.

### Best practices

- Write a unique title tag for each page;
- Be brief, but descriptive;
- Avoid generic and vague titles;
- Use sentence case or title case;
- Create something click-worthy—not clickbait;
- Match search intent;
- Include your target keyword where it makes sense;
- Keep it under 60 characters.

**Recommended reading:***[How to Craft the Perfect SEO Title Tag (Our 4‐Step Process)](https://ahrefs.com/blog/title-tag-seo/)*

### How to add a title tag to your page

Paste the code below into the `<head>` section of your page:

```
<title>This is the title of the page.</title>
```

If you’re using WordPress, install an [SEO plugin](https://ahrefs.com/blog/best-seo-plugins-for-wordpress/) like Yoast. You should see a place to set the title tag on the page or post editor.

Other CMS’ like Squarespace and Wix have similar functionality built-in.

### How to find and fix common title tag mistakes

There are four common issues with title tags:

1. **Too long/short**. Google [says](https://support.google.com/webmasters/answer/35624?visit_id=636880082951453933-4272044119&rd=1) to “avoid unnecessarily long or verbose titles” while keeping them “descriptive and concise.”
2. **Doesn’t exist.** Google says that every page should have a title tag.
3. **Multiple title tags on one page.** Search engines may display an undesirable title tag if there is more than one on a page.
4. **Duplicate titles across multiple pages**. Google says that “it’s important to have distinct, descriptive titles for each page on your site.”

To check a page for the first two issues, plug the URL into a free tool like [SERPSim](https://serpsim.com/).

If it doesn’t pull a title back, then you need to add one.

If the pixel length count is red, then it needs shortening.

To check for duplicate and multiple title tags, crawl your site with [Ahrefs’ Site Audit](https://ahrefs.com/site-audit).

From there, check the **On page** report for “Multiple title tag” errors:

Fix these by removing one of the tags from the affected pages.

Next, go to the **Duplicate content** report and look for title tags with “Bad duplicate” errors:

Rewrite the title tags on affected pages to make them unique.

Note that this same report also shows pages with title tags that are too long, too short, missing, or empty.

## Meta description

The [meta description](https://ahrefs.com/blog/meta-description-study/) summarizes the page’s content. Search engines often use it for the snippet in search results.

Sidenote.

 Google doesn’t always show the meta description you set. Sometimes they show a different snippet.

### Why it’s important for SEO

Google [explains](https://support.google.com/webmasters/answer/35624?visit_id=636880082951453933-4272044119&rd=1) it best once again:

> A meta description tag should generally inform and interest users with a short, relevant summary of what a particular page is about. They are like a pitch that convinces the user that the page is exactly what they’re looking for.

Meta descriptions, however, are **not** a direct ranking factor. Google says:

> Even though we sometimes use the description meta tag for the snippets we show, we still don’t use the description meta tag in our ranking.

### Best practices

- Write a unique description for each page;
- Try to summarize content accurately;
- Avoid generic descriptions;
- Use sentence case;
- Create something click-worthy, not clickbait;
- Match search intent;
- Include your target keyword where it makes sense;
- Keep it under 160 characters

**Recommended reading:***[How to Efficiently Write the Perfect Meta Description](https://ahrefs.com/blog/meta-description/)*

### How to add a meta description to your page

Paste the code below into the `<head>` section of your page:

```
<meta name="description" content="Place the meta description text here.">
```

If you’re using WordPress, you can do this easily in Yoast.

Other CMS’ like Squarespace and Wix have similar functionality.

### How to find and fix common meta description mistakes

The four common issues with meta descriptions are the same as those with title tags:

1. **Too long/short.** Google [says](https://support.google.com/webmasters/answer/35624?visit_id=636880082951453933-4272044119&rd=1) “there’s no limit on how long a meta description can be, but the search result snippets are truncated as needed, typically to fit the device width.”
2. **Doesn’t exist.** Google says to “make sure that every page on your site has a meta description.”
3. **Multiple meta descriptions on one page**. More than one tag may confuse search engines.
4. **Duplicate meta descriptions across multiple pages.** Google says that you should “differentiate the descriptions for different pages.”

Check for the first two errors on a page-by-page basis with [SERPSim](https://serpsim.com/) or Yoast.

Crawl your website with [Ahrefs’ Site Audit](https://ahrefs.com/site-audit) and check the **On page** report to check for the first three errors across all pages.

Check the **Duplicate content** report for duplicate meta descriptions across pages.

Use the same fixes as with title tags.

## Meta robots

The meta robots tag tells search engines if and how they should crawl your web pages.

### Syntax

```
<meta name=”robots” content="index, follow">
```

### Why it’s important for SEO

Using the wrong attributes in the meta robots tag can have a catastrophic impact on your site’s presence in the search results. Your SEO efforts rely on you understanding this tag and using it effectively.

With that in mind, here are the values you can use in this tag:

- **index**: tells bots to index the page;
- **noindex**: tells bots not to index the page;
- **follow**: tells bots to crawl links on the page, and that you also vouch for them;
- **nofollow**: tells bots not to crawl links on the page, and that no endorsement is implied.

You can combine these in any of the following ways:

```
<meta name=”robots” content="noindex, nofollow">
<meta name=”robots” content="index, follow">
<meta name=”robots” content="noindex, follow">
<meta name=”robots” content="index, nofollow">
```

You can also use `<meta name=”robots” content="none">`, which is the same as noindex, nofollow. Not setting a meta robots tag is also equivalent to index, follow.

Sidenote.

Google sees “nofollow” tags as [hints, not directives](https://webmasters.googleblog.com/2019/09/evolving-nofollow-new-ways-to-identify.html). There are other attributes such as noarchive, noimageindex, nosnippet, etc. But as these are more advanced values, we’re not going to talk about them in this post.

### Best practices

- Use meta robots tags **only** when you want to restrict the way Google crawls a page;
- Don’t block pages with meta robots tags in [robots.txt](https://ahrefs.com/blog/robots-txt/);

**Recommended reading:** *[Robots Meta Tag & X‑Robots-Tag: Everything You Need to Know](https://ahrefs.com/blog/meta-robots/)*

### How to add a meta robots tag to your page

Paste the appropriate code above into the `<head>` section of your page.

In WordPress, use Yoast’s advanced settings to set meta robots tags:

Most CMS’ have similar options built-in.

### How to diagnose and fix common meta robots mistakes

There are three common mistakes with meta robots:

1. **Noindexed pages blocked by robots.txt.** This prevents Google from seeing the noindex robots tag, so they may still index the URL.
2. **Rogue meta noindex.** This prevents Google from indexing the page, so it’ll get no organic traffic.
3. **Rogue meta nofollow.** This prevents Google from crawling the links on the page, which might prevent the discovery and indexing of important content. It also prevents the flow of [PageRank](https://ahrefs.com/blog/google-pagerank/) to those pages—which may not be desirable.

You can check for the first two issues using the **Coverage** report in Google Search Console.

To find indexed pages that may be set to meta robots noindex, hit the “Valid with warnings” tab and look for “[Indexed, though blocked by robots.txt](https://ahrefs.com/blog/indexed-though-blocked-by-robots-txt/)” warnings:

Check the source code of these pages for a meta robots noindex tag. Remove either the robots.txt block or meta robots noindex tag depending on what you’re trying to do.

To find rogue meta robots noindex tags, hit the “Excluded” tab and look for pages “Excluded by ‘noindex’ tag”:

Remove the robots meta tag from any pages that should be indexed.

To find pages with rogue meta robots nofollow tags, crawl the site with [Ahrefs’ Site Audit](https://ahrefs.com/site-audit) and check the **Indexability** report for “Nofollow page” warnings.

Remove the tag unless you specifically want search engines not to crawl the links on the page.

Sidenote.

There are few issues not covered here, such as having pages with noindex tags in your [sitemap](https://ahrefs.com/blog/how-to-create-a-sitemap/). To learn more about those issues, check out the **Indexability** report in Ahrefs’ Site Audit.

## Meta viewport

A meta viewport tag sets the visible area of a web page. It is used to instruct the browser how to render the page on different screen sizes (i.e., desktop/tablet/mobile).

### Why it’s important for SEO

Google [says](https://support.google.com/webmasters/answer/79812?hl=en) that the “presence of this tag indicates to Google that the page is mobile-friendly.” This matters because Google ranks mobile-friendly web pages higher in mobile search results [as of 2015](https://webmasters.googleblog.com/2015/04/rolling-out-mobile-friendly-update.html).

Here’s what a page might look like on mobile with and without a meta viewport tag:

Many people likely hit the back button when the desktop version of a page loads on mobile. It’s annoying and makes things hard to read. This may send negative signals to Google and tell them there’s something undesirable about your page.

Sidenote.

The viewport tag isn’t all that’s needed to make a website mobile-friendly. Your website also needs to make use of responsive design.

### Best practices

- Use meta viewport tag on all web pages;
- Use the “standard” tag unless you know what you’re doing (see below)

### How to add a meta viewport tag to your page

Paste the code below into the `<head>` section of your webpage:

```
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Note that the content attribute doesn’t have to be set to *width=device-width, initial-scale=1.0*, but this is the most common implementation—and the correct one for most pages.

### How to diagnose and fix common meta viewport mistakes

Because most CMS’ and themes set the viewport automatically, tag-related issues are uncommon on most modern websites.

That said, you can check for issues using the [Mobile Usability](https://support.google.com/webmasters/answer/9063469?hl=en) report in [Google Search Console](https://search.google.com/search-console/about).

This shows pages with usability issues on mobile devices. If this issue is even partly down to the lack of a viewport meta tag, it will show the “Viewport not set” error.

Fix this issue by adding the appropriate meta viewport tag to any affected pages.

IMPORTANT

Adding a meta viewport tag won’t fix underlying mobile display issues caused by CSS styles not written for different widths. If adding a meta viewport tag doesn’t solve things, consult a developer.

Don’t use Google Search Console?

Meta viewport is almost always set at the site-level and is usually hardcoded into the theme.

Use [Google’s Mobile-Friendly Test tool](https://search.google.com/test/mobile-friendly) to check your homepage for a meta viewport tag.

If the tag isn’t on your homepage, it probably isn’t anywhere else on your site.

Note that this is far from a foolproof method, and you should always use Google Search Console if possible.

## Meta charset

The meta charset tag sets the character encoding for the web page. In other words, it tells the browser how the text on your web page should be displayed.

There are hundreds of different character sets, but the two most common on the web are:

- **UTF-8** - Character encoding for Unicode;
- **ISO-8859-1** - Character encoding for the Latin alphabet.

See a full list [here](http://www.iana.org/assignments/character-sets/character-sets.xhtml).

### Why it’s important for SEO

Using the wrong character encoding can cause some characters to display incorrectly in the browser.

Character formatting issues are bad for user experience and can cause your pages to look quite broken.

That can lead to SEO problems like:

- People not wanting to link to your page.
- High bounce rate, low time on page, and low [dwell time](https://ahrefs.com/seo/glossary/dwell-time).
- Search engines not understanding your content.

But let’s be real about this:

Unless your page is severely broken as a result of charset issues, which is unlikely, the impact is going to be quite minimal.

Still, it’s worth noting that Google [recommends](https://support.google.com/webmasters/answer/79812?hl=en) using Unicode/UTF-8 where possible.

### Best practices

- Use the meta charset tag on all webpages;
- Use UTF-8 where possible;
- Use the correct syntax for your HTML version (see below).

### How to add a meta charset tag to your web page

Paste the code below into the `<head>` section of your webpage:

```
<meta charset="UTF-8">
```

If you’re using HTML4 or below, use this code instead:

```
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
```

If you’re unsure which version of HTML you’re using, check your source code for `<!doctype html>`. If it’s there, you’re using HTML5.

### How to diagnose and fix common meta charset mistakes

Most websites use either UTF-8 or ISO-8859-1 character encoding.

The former is preferable to the latter.

For that reason, it’s worth checking for pages on your site that don’t use UTF-8 encoding. You can do this in [Ahrefs’ Site Audit](https://ahrefs.com/site-audit). Go to the Page Explorer, then use these settings:

If the search returns any results, check each of them manually for character encoding issues.

Switch to UTF-8 encoding if possible. That may solve the issue, but not always. However, if you don’t set meta charset at all, the browser will be forced to guess and may show garbage text to users.

## Meta refresh redirect

A meta refresh tag tells the web browser to redirect the user to a different URL after a set amount of time.

### Why it’s important for SEO

Meta refresh redirect tags are important for SEO in the sense that **you should not use them**, even though Google [understands](https://support.google.com/webmasters/answer/79812?hl=en) and respects them.

There are a few reasons for this:

- Not supported by all browsers;
- Can be confusing to the user (and raise security concerns);
- Pages need parsing before they see the destination URL, which can take some time.

Another potential issue arises when there’s no [canonical tag](https://ahrefs.com/blog/canonical-tags/) present on the page, as John Mueller explains in [this tweet](https://twitter.com/searchmartin/status/969481490802229249?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E969486943351394304&ref_url=https%3A%2F%2Fwww.seroundtable.com%2Fgoogle-meta-refresh-redirects-work-25335.html):

### Best practices

- Avoid meta refresh redirect tags unless absolutely necessary;
- Use a [301 redirect](https://ahrefs.com/blog/301-redirects/) instead.

### How to add a meta refresh redirect tag to your page (if you really need to)

Paste the code below into the `<head>` section of your page:

```
<meta http-equiv="refresh" content="5;url="https://example.com/">
```

The content attribute specifies the time delay in seconds. The URL attribute specifies the redirect URL.

### How to find and fix common meta refresh redirect mistakes

Meta refresh redirects are bad practice, so it’s best to remove them where possible.

To find them, crawl your site with [Ahrefs’ Site Audit](https://ahrefs.com/site-audit) and check the **Internal pages** report. Look for the “Meta refresh redirect” error.

Replace them with 301 or 302 redirects where possible.

If not, check for the presence of a [canonical tag](https://ahrefs.com/blog/canonical-tags/), and make sure it references the canonical version of the page.

## What about meta keywords?

Some articles say to fill in the meta keywords tag with a list of target keywords. This is pointless and potentially bad advice. Google hasn’t used meta keywords for rankings [since 2009](https://webmasters.googleblog.com/2009/09/google-does-not-use-keywords-meta-tag.html) because:

> […] keyword meta tags quickly became an area where someone could stuff often-irrelevant keywords without typical visitors ever seeing those keywords. Because the keywords meta tag was so often abused, many years ago Google began disregarding the keywords meta tag.

Bing went one step further in 2011 when they [announced](https://searchengineland.com/the-meta-keywords-tag-lives-at-bing-why-only-spammers-should-use-it-96874) they use the tag as a spam signal. So, if yours are stuffed with keywords, then that could work against you in Bing.

For this reason, it’s best to be on the safe side and remove meta keywords tags from your site.

To do this, crawl your site with [Ahrefs’ Site Audit](https://ahrefs.com/site-audit), then plug these settings into Page Explorer:

Remove the meta keywords tag from any matching pages.

Note that most of the time, removing these tags is easy, as many sites set a sitewide meta keywords tag in their CMS. Removing the tag from all pages can be done by removing that one piece of code.

**Recommended reading:** *[Meta Keywords: What Are They and Should You Use Them?](https://ahrefs.com/blog/meta-keywords/)*

## Final thoughts

Meta tags aren’t *that* complicated. Understanding the six tags above should be enough to prevent any significant SEO faux pas.

Looking to learn more about meta tags? [This should do it](https://www.metatags.org/all_metatags).

Looking to maximize your traffic from social media? Read [about Open Graph meta tags](https://ahrefs.com/blog/open-graph-meta-tags/).

Give me a shout [on Twitter](https://twitter.com/joshuachardwick?lang=en) if there’s anything I missed.
