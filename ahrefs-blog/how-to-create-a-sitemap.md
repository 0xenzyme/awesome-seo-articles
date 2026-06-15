---
title: "How to Create an XML Sitemap (and Submit It to Google)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "how-to-create-a-sitemap"
url: "https://ahrefs.com/blog/how-to-create-a-sitemap/"
canonical: "https://ahrefs.com/blog/how-to-create-a-sitemap/"
author: "Joshua Hardwick"
published: "2019-09-19T14:28:47+00:00"
updated: "2024-06-16T21:10:59+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T11:37:44+00:00"
status_code: 200
html_hash: "e869e49ad2ea14312873c66f078a5de47a1a6c6a37396e12ef8a016172f6a100"
clean_word_count: 2806
clean_char_count: 16804
---
# How to Create an XML Sitemap (and Submit It to Google)

Just as it’s difficult to find a new destination without a map, it’s sometimes hard for Google to find all the pages on your website without a sitemap.

Luckily, it’s quick and easy to create and submit an XML sitemap to Google.

Below, we walk through how to do this step by step.

But first, let’s cover a few basics.

*(Already know the basics? [Click to jump straight to creating a sitemap](#section4).)*

New to SEO? Check out our

[SEO basics guide](https://ahrefs.com/blog/seo-basics/)

## What is a sitemap?

A sitemap is an XML file listing all the important content on your website. Any page or file that you want to show up in search engines should be in your sitemap.

Fun fact

Sitemaps can’t list more than 50,000 URLs, and they can’t be more than 50mb in size. If your sitemap exceeds one or more of those figures, then you’ll need to create more than one.

## What does an XML sitemap look like?

XML sitemaps are made for search engines, not humans. They can look a bit daunting if you’ve never seen one before.

```
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
	<url>
		<loc>https://ahrefs.com/</loc>
		<lastmod>2019-08-21T16:12:20+03:00</lastmod>
	</url>
	<url>
		<loc>https://ahrefs.com.com/blog/</loc>
		<lastmod>2019-07-31T07:56:12+03:00</lastmod>
	</url>
</urlset>
```

Let’s break this down.

### XML declaration

```
<?xml version="1.0" encoding="UTF-8"?>
```

This tells search engines that they’re reading an XML file. It also states the version of XML and character encoding used. For sitemaps, the version **should** be 1.0, and the encoding **must** be UTF-8.

### URL set

```
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
```

This is a container for all the URLs in the sitemap. It also tells crawlers which protocol standard is used. Most sitemaps specify the Sitemap 0.90 standard, which is supported by Google, Yahoo!, and Microsoft amongst others.

### URL

```
<url>
<loc>https://ahrefs.com/</loc>
<lastmod>2019-08-21T16:12:20+03:00</lastmod>
</url>
```

This is the parent tag for each URL. You must specify the location of the URL in a nested `<loc>` tag. Crucially, these must be absolute, not relative, canonical URLs.

Although this is the only required tag here, there are a few optional properties:

- `<lastmod>`: Specifies the date when the file was last modified. This must be in the [W3C Datetime](https://www.w3.org/TR/NOTE-datetime) format. For example, if you updated a post on September 25th, 2019, the attribute would read 2019-09-25. You can also include the time, but this is optional.
- `<priority>`**:** Specifies the priority of the URL relative to all other URLs on the site. Values range between 0.0 and 1.0. Higher is more important.
- `<changefreq>`**:** Specifies how frequently the page is likely to change. Its job is to give search engines some idea as to how often they might want to recrawl the URL. Valid values here are *always*, *hourly*, *daily*, *weekly*, *monthly*, *yearly*, and *never*.

None of these optional tags are *that* important for SEO.

For `<lastmod>`, Google’s Gary Ilyes [states](http://stackoverflow.com/questions/31349345/how-to-properly-format-last-modified-lastmod-time-for-xml-sitemaps?stw=2) that they ignore it in most cases as “webmasters are doing a horrible job keeping it accurate.” Since most sitemap generators set this to the current date for all pages, and not the date when the file was last modified, it’s easy to see why.

For  `<priority>`, Google [says](https://www.seroundtable.com/google-sitemap-priority-field-a-bag-of-noise-23645.html) they ignore this tag because it’s just a “bag of noise.”

For  `<changefreq>`, John Mueller [says](https://www.seroundtable.com/google-priority-change-frequency-xml-sitemap-20273.html) “Priority and change frequency doesn’t really play that much of a role with Sitemaps anymore.”

## Why do I need a sitemap?

Google discovers new content by crawling the web. When they crawl a page, they pay attention to both internal and external links on the page. If a discovered URL is not in their search index, they can parse its contents and index it where appropriate.

But Google can’t find all content this way. If a web page isn’t linked to from other known pages, they won’t find it.

This is where sitemaps come in.

Sitemaps tell Google (and other search engines) where to find the most important pages on your website so they can crawl and index them.

This is important because search engines can’t rank your content without first indexing it.

## How to create a sitemap

Some CMS’ generate a sitemap for you. These are automatically updated when you add or remove pages and posts from your site. If your CMS doesn’t do this, then there’s usually a plugin available which does.

### Creating a sitemap in WordPress

Even though WordPress [powers 34.5% of websites](https://w3techs.com/technologies/history_overview/content_management/all), it doesn’t generate a sitemap for you. To create one, you need to use [a plugin](https://ahrefs.com/blog/best-seo-plugins-for-wordpress/) like Yoast SEO.

To install Yoast SEO, login to your WordPress dashboard.

Go to *Plugins > Add New*.

Search for “Yoast SEO.”

Hit “Install now” on the first result, then “Activate.”

Go to *SEO > General > Features*. Make sure the “XML sitemaps” toggle is on.

You should now see your sitemap (or sitemap index) at either yourdomain.com/sitemap.xml or yourdomain.com/sitemap\_index.xml.

Sidenote.

 If your WordPress installation lies in a [subfolder or subdomain](https://ahrefs.com/blog/subdomain-vs-subfolder/), then your sitemap is located under that path. For example, the sitemap for our blog is accessible at ahrefs.com/blog/sitemap\_index.xml.

TIP

If you want to specifically include or exclude certain types of content (tags pages, category pages, etc.) from your sitemap, head to the “Search Appearance” settings.

You can also exclude individual posts or pages from the “Advanced” meta box on the editor.

**IMPORTANT.** Only exclude pages from your sitemap that you don’t want to show up in search results.

Learn more in [our guide to WordPress SEO](https://ahrefs.com/blog/wordpress-seo/).

### Creating a sitemap in Wix

Wix creates a sitemap for you automatically. You can find this at *yourwixsite.com/sitemap.xml*.

Unfortunately, you don’t get much control over the pages that do and don’t get included in your sitemap. If you want to exclude a page, head to the “SEO (Google)” settings tab for the page and turn the “Show this page in search results” switch off.

Note that this also adds a noindex meta tag to the page which excludes it from showing up in search results.

Sidenote.

 If you [canonicalize](https://ahrefs.com/blog/canonicalization/) a URL in Wix, it won’t remove it from your sitemap. While this probably won’t affect most users, be aware that including canonicalized pages in your sitemap isn’t best practice, and can send mixed signals to Google.

### Creating a sitemap in Squarespace

Squarespace also creates a sitemap for you automatically. You can usually find it *yoursquarespacesite.com/sitemap.xml*.

There’s no way to manually edit your sitemap in Squarespace, although you can exclude (noindex) pages from search engines in the “SEO” tab.

This will also exclude the page from your sitemap.

### Creating a sitemap in Shopify

Shopify automatically generates a sitemap for you. Find it at *yourstore.com/sitemap.xml*.

Unfortunately, there’s no easy way to noindex a page in Shopify. You have to edit the code in the .liquid files directly.

### Creating a sitemap without a CMS

If you think there are fewer than ~300 pages on your site, install the free version of [Screaming Frog](https://www.screamingfrog.co.uk/seo-spider/).

Once installed, go to *Mode > Spider*.

Paste your homepage URL in the box labeled “Enter URL to spider.”

Hit “Start.”

Sidenote.

 Make sure to use the [canonical](https://ahrefs.com/blog/canonical-tags/) (main) version of your homepage. If you don’t do this, Screaming Frog will only crawl one URL.

Once the crawl is complete, look at the bottom-right corner.

It will say something like this:

If the number is 499 or below, go to *Sitemaps > XML sitemap*.

Because Google doesn’t pay much attention to `<lastmod>`, `<changefreq>`, and `<priority>`, we recommend excluding them from the sitemap file.

Hit “Next” and save the sitemap to your computer. Done.

If the number shows “500 of 500,” then there’s no point exporting a sitemap. Why? Because it means you’ve hit the crawl limit before it crawled all the pages on your site. As a result, hundreds of pages could be missing from the exported sitemap—which makes it rather useless.

One way to solve this is to search for a free sitemap creator. There are lots of them.

Unfortunately, most aren’t reliable.

We tested some of the most popular generators and found that quite a few include non-canonical URLs, noindexed pages, and redirects. This is bad SEO practice.

| Generator | Includes canonicalized URLs? | Includes noindexed URLs? | Includes redirects? |
| --- | --- | --- | --- |
| xml-sitemaps.com | Yes ❌ | No ✅ | No ✅ |
| web-site-map.com | Yes ❌ | No ✅ | No ✅ |
| xmlsitemapgenerator.org | Yes ❌ | No ✅ | No ✅ |
| smallseotools.com/xml-sitemap-generator | Yes ❌ | Yes ❌ | Yes ❌ |
| freesitemapgenerator.com | Yes ❌ | Yes ❌ | Yes ❌ |
| duplichecker.com/xml-sitemap-generator.php | Yes ❌ | Yes ❌ | Yes ❌ |
| xsitemap.com | Yes ❌ | Yes ❌ | Yes ❌ |

So what’s the solution?

If Screaming Frog failed to crawl your entire site, crawl your site with [Ahrefs Site Audit](https://ahrefs.com/site-audit).

Sidenote.

 Verify your site for faster crawling. [Here’s how](https://help.ahrefs.com/en/articles/1431155-how-do-i-finish-crawling-my-website-faster-in-site-audit).

Once the crawl is complete, go to the Page Explorer and add these filters.

Hit *Export* > *Current table view*.

Open the CSV file, then copy and paste all the URLs from the URL column into [this tool](https://timestampgenerator.com/tools/xml-sitemap-from-list).

Hit “Add to queue,” then “Export queue as sitemap.xml.”

This file is your completed sitemap.

## How to submit a sitemap to Google

To start, you need to know where your sitemap is.

If you’re using a plugin, chances are the URL is *domain.com/sitemap.xml*.

If you’re doing this manually, name your sitemap something like sitemap.xml then upload to the root folder of your website. You should then be able to access the sitemap at domain.com/sitemap.xml.

Sidenote.

 You can choose any name for your sitemap, but it’s good practice to stick with sitemap.xml. If you have multiple sitemaps, you can go for a simple naming scheme like sitemap\_1.xml, sitemap\_2.xml.

Go to *Google Search Console > Sitemaps > paste in sitemap location > hit “Submit”*

That’s it. Done.

TIP

It’s also good practice to add your sitemap URL(s) to your [robots.txt file](https://ahrefs.com/blog/robots-txt/).

You can find this file in the root directory of your web server. To add your sitemap, open the file and paste this line:

```
Sitemap: https://www.yourdomain.com/sitemap.xml
```

You need to replace the example URL with the location of your sitemap.

If you have multiple sitemaps, just add multiple lines.

```
Sitemap: https://www.asos.com/sitemap_1.xml
Sitemap: https://www.asos.com/sitemap_2.xml
```

## Fixing common website errors that affect your sitemap

Google Search Console tells you about most technical errors related to your sitemap.

For example, here’s a warning that one of our submitted URLs is blocked by robots.txt:

You can learn more about these issues and how to solve them [here](https://support.google.com/webmasters/answer/7440203?hl=en).

That said, there are some issues that Google doesn’t tell you about.

Below are a couple of the more common ones, and how to find and fix them.

### Useless, low-quality pages in your sitemap

Every page in your sitemap should now be indexable and canonical.

Unfortunately, that doesn’t mean all those pages are of high quality. If you have a lot of content, some low-quality pages likely made it into your sitemap.

For example, take a look at these two pages on an ecommerce site:

Neither of them is valuable for searchers, yet they’re still in that website’s sitemap, and Google has both pages indexed.

To find these pages, go to *Site Audit > Duplicate Content*

Look for clusters of duplicate and near-duplicate pages without canonicals. These are the orange squares. Click one to see all the pages in the group.

Check out the pages and see if they have any value.

Having low-quality pages on your site is bad for three reasons:

- **They waste [crawl budget](https://ahrefs.com/blog/crawl-budget/)**. Making Google waste time and resources crawling useless, low-quality pages isn’t ideal. They could be spending that time crawling more important content instead.*(For the record, Google [states](https://webmasters.googleblog.com/2017/01/what-crawl-budget-means-for-googlebot.html) that crawl budget is “not something most publishers have to worry about.”)*
- **They “steal” link authority from more important pages.** There’s a clear [correlation](https://ahrefs.com/blog/search-traffic-study/) between the authority of pages and their rankings. [Internal links](https://ahrefs.com/blog/internal-links-for-seo/) to low-quality pages serve only to dilute authority that could flow to more important pages. *(Interestingly, when [we deleted almost ⅓ of posts from the Ahrefs blog](https://ahrefs.com/blog/content-audit/), we saw an increase in traffic—not a decrease.)*
- **They result in poor user experience.** There’s no value to visitors landing on these pages. It’s annoying for visitors to click on them, and they may end up bouncing if they feel your site is low-quality and neglected.

All in all, the best course of action is to remove low-quality from your website and, subsequently, your sitemap. If you’re doing this, you should also remember to remove any internal links to those pages. Fail to do that, and you’ll swap one problem (low-quality pages) for another ([broken links](https://ahrefs.com/blog/fix-broken-links/)).

Beyond duplicates and near-duplicates, you can also look for pages with thin content.

Just check the “On page” report in Site Audit for pages with a “Low word count” warning.

### Pages excluded from your sitemap by accident

If you used any of the recommended methods above to create your sitemap, pages with noindex or canonical tags (non-self-referencing) won’t be included.

That’s a good thing. You shouldn’t include canonicalized URLs or noindexed pages in your sitemap.

That said, if you have rogue noindex tags on your site, pages can get excluded by accident.

To check for errors, head to the “Indexability” report in Site Audit and click the “Noindex page” warning. This shows all noindexed pages.

Most of these will likely be intentionally noindexed, but it’s worth skimming the list to double-check. Usually, rogue noindex tags are easy to spot as they’ll exist across an entire subsection of your site.

If you see any pages that shouldn’t be noindexed, remove the rogue noindex tag from the page and add it to your sitemap. If you’re using a CMS or plugin, then this should happen automatically.

PRO TIP

It’s also worth checking for rogue canonicals and redirects. To do that, go to the Data Explorer and add these filters:

Checking for rogue canonicals.

Checking for rogue redirects.

Remove any rogue canonicals and redirects then add the affected pages to your sitemap.

## FAQs

Here are a few answers to some frequently asked questions about sitemaps. Let us know if you have a question not answered in this section, and we’ll add it.

### Do you need a sitemap for AMP pages?

Nope.

### How do I create a sitemap for an ecommerce website?

You create a sitemap for an ecommerce website in the same way as you would for any site. That said, it’s worth checking for duplicate and near-duplicate pages on ecommerce sites as these often slip through the net at grand scale thanks to the joys of faceted navigation.

## Final thoughts

Creating a sitemap isn’t rocket science, especially if you’re using a plugin that does the heavy lifting for you. It’s not hard to create one from scratch either—just crawl your site and format the resulting lists of URLs.

That said, it’s crucial to remember that Google doesn’t have to index the pages in your sitemap. And sitemaps have nothing to do with rankings.

If you’re looking to rank higher in Google, read [this](https://ahrefs.com/blog/how-to-rank-higher-on-google/).

Got questions? Give me a shout in the comments or [on Twitter](https://twitter.com/joshuachardwick?lang=en).
