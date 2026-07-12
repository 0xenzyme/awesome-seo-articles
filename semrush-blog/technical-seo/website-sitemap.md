---
title: "What Is a Sitemap? Website Sitemaps Explained"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "website-sitemap"
url: "https://www.semrush.com/blog/website-sitemap/"
canonical: "https://www.semrush.com/blog/website-sitemap/"
author: "Vlado Pavlik, Chris Shirlow, Boris Mustapic"
published: "2021-05-24T11:55:00+00:00"
updated: "2024-08-05T12:27:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T20:36:06+00:00"
status_code: 200
html_hash: "6f43c70c852755f7da5de439c82d9a92bd5708bc6828a5b9b53f9f189bd1e99e"
clean_word_count: 2472
clean_char_count: 18800
---
# What Is a Sitemap? Website Sitemaps Explained

## What Is a Sitemap?

A sitemap is a file that shows the structure of your website, including its pages and content. And the relationships between them.

One type is intended to help search engines crawl your site more efficiently. Another type is intended to help users better navigate your website.

## Why Do You Need a Website Sitemap?

The larger and more complex your website is, the more difficult it can be for both users and search engines to navigate. But sitemaps make it easier.

All this means sitemaps are important. Because they can lead to:

- **Better discoverability**: An XML sitemap (more on this in the next section) helps search engines discover important pages on your website. This is particularly helpful for large websites that have thousands of pages and may be impacted by a limited [crawl budget](https://www.semrush.com/blog/crawl-budget/).
- **Faster indexation**: For newer websites, submitting an XML sitemap can lead to more pages ranking sooner. And for websites that update existing content, Google can discover those changes sooner when they’re included in the sitemap.
- **Improved user experience**: HTML sitemaps (more on this in the next section) can make it easier for users to find exactly what content they’re looking for. Because they’re able to see all your most important pages in one place.

Different sitemaps offer different benefits, so let’s discuss those next.

## What Are the Different Types of Website Sitemaps?

There are two types of sitemaps:

- **XML sitemaps**: Sitemaps written in a specific format designed for search engine crawlers
- **HTML sitemaps**: Sitemaps that look like regular pages and help users navigate the website

![XML website sitemap vs html website sitemap](https://static.semrush.com/blog/uploads/media/fd/dc/fddc1901d6628810a127436ace2f456d/d426d74157367af62f0efb51371ea0fd/AD_4nXdKzAiQc9sMsCVdqc9YcvTmhQ6-dF9U7y3tyiP1eDwujsFY0Lc-_-H9-6XQs6dLhI8tTp04c1n5CBTo34-XBNXGkKl3YFpXycEJV5vrwG4zVcNtIu-WzCStf6P9I-FknF_9vDoiZmvJ9rckJu70Hso3f3Q7.png)

### XML Sitemaps

Extensible Markup Language (XML) sitemaps are the preferred format for search engines like Google.

They provide three main types of information to search engines:

- The list of all the URLs you want to have indexed
- The “lastmod” attribute that informs when the URLs were last updated
- The ["hreflang" attribute](https://www.semrush.com/blog/hreflang-attribute-101/) that reveals local variants of the URLs

These sitemaps look something like this:

![XML website sitemap example](https://static.semrush.com/blog/uploads/media/86/e8/86e875e5dd31a47ecb994dd284a07eb4/792d5f496426a7df34d4f34de2f54610/AD_4nXdip-vKwZ43OxB3MjjZ-r-ZYRXuskxeOR9OOJ3oX7v8u2IVp2ou52GXdFQxNGKK6kKh4a8MMVmF8lvvyQW7wlPVebeH2rGfwh7vOEeEaeVCN-9fNuTeAuu5nAN56ghfGBVbAI9Pq6ZQVvt4LnI5tWndo-wt.jpeg)

While XML sitemaps are especially suitable for large websites, websites with extensive archives, or new websites with few links, every website can benefit from having one.

Plus, it only takes a few minutes to create one.

***Further reading****:*

- [*XML Sitemap: What It Is & How to Generate One*](https://www.semrush.com/blog/xml-sitemap/)
- [*WordPress Sitemap: How to Create, Check, and Submit One*](https://www.semrush.com/blog/wordpress-sitemap/)

### HTML Sitemaps

[HTML sitemaps](https://www.semrush.com/blog/html-sitemap/) used to be a popular way to improve a website's navigation and provide links to all your important pages in one place.

Here's an example of an HTML sitemap from H&M Group:

![HTML sitemap example by H&M Group](https://static.semrush.com/blog/uploads/media/e1/6e/e16e5d2bc44a02601ed00966dfe6d874/44fa9a370b8dc4a5b83cee9dc14dd093/AD_4nXcYwsutFMnwLs1_5LLFzdFyMWD0fJ9_kjb1MjNiWlJr8aLocWhNOr71NkFJuLU2jd3WP8RGBt_L_DrnQUzzjBC9bganx2f1eZQfE9uKpc17EstTs0NpbfR9908oCadPRbuJHz4PlnwDWIOOmB8bZqtSj5E5.png)

As you can see, it’s a standard page with links to various pages organized in a hierarchical way.

Although HTML sitemaps aren’t that common anymore, some [voices in the SEO community](https://www.searchenginejournal.com/html-sitemap-importance/325405/) still say they’re a must. Because HTML sitemaps can improve your [internal linking](https://www.semrush.com/blog/internal-links/) and provide another layer of navigation for complex websites with many pages.

But **don’t** use an HTML sitemap as a replacement for good site navigation elements (such as menus, footer links, breadcrumbs, categories, etc.).

Google’s John Mueller spoke to this [on Mastodon](https://mastodon.social/@johnmu/109477617298107922):

> If you feel the need for an HTML sitemap, spend the time improving your site's architecture instead.

In other words, users shouldn’t need a sitemap to effectively navigate your website.

## How to Find a Sitemap

Here are some effective ways to find a sitemap on a website:

### Manual Check

The easiest way to find an XML sitemap is to look for it manually. Most commonly, a website’s XML sitemap will be located at this URL address: “https://domain.com/**sitemap.xml**.”

Quite often—especially if the website uses WordPress and the [Yoast SEO plugin](https://www.semrush.com/blog/yoast-seo/)—you'll be redirected to a sitemap index (/sitemap\_index.xml).

In that case, it’ll look like this:

![website sitemap index file](https://static.semrush.com/blog/uploads/media/f0/90/f090f08abc19f90a3d8c7eb10c74fe0c/910be5f7dc83af82e4719e63d8543dac/AD_4nXe-c3hpNN1vYxGHTfdOtoeyhdqccPcRXWEAc9I3pa-GcQxVinOPrnMMaNMkau7g59yF3heHaN-E3vLxkszUXWPxzHbDjM_fIFxIhBrdk6iwT7T_9zvf-8YfjU-Tx-4eeIa10oPjQiv6zffFChoGt8AeHtoP.png)

As you can see, a sitemap index is a simple file that lists all the sitemaps a website has. (Yes, there can be multiple sitemaps.)

To see the actual sitemap, just click the link to the specific sitemap in the index.

### Search Operators

Search operators are special commands you can add to search queries to return more specific results.

Here are some search operators you can use to find a website’s sitemap:

- “site:[domain.com] filetype:xml”
- “site:[domain.com] inurl:sitemap”
- “site:[domain.com] intitle:sitemap”

Simply enter the operator into the search bar and replace “domain.com” with the actual website's address.

![search operator in google looks like "site:semrush.com filetype:xml"](https://static.semrush.com/blog/uploads/media/83/59/83597800610399ddb1ed9f6ec7f1b818/051faac228814f503725864fc468e409/AD_4nXcH8TR9oGjHo5r84iBDF20mlTx4tmtsgKSJv-MIRDzTmbh1ajZBnpLH03shFf_UsI3Vz1WeIlnPGvf4Fq8740chbbWQzHD6PqKFQzi6t-cJj1N296yabUYNPixHy0WM7IUsPrEnLTt3hxYviHh_NLCZZPt7.png)

The search results should return the location of the website sitemap—if it exists and the search engine you’re using has indexed it.

![top search result is Semrush's sitemap as an xml](https://static.semrush.com/blog/uploads/media/5b/34/5b34d60a6047a9a8ac52687900f7e380/d01df6c847e4a618c386edd92977de32/AD_4nXfv0XU4ZMGpv78r0LIObU7X8LQOKHoDAoiWfn95xRK7lDNzCDoObp-WhjRjCSF3JArggOs3haRzCAkD5ZOi_M-BX8SgEBYHaypnjcuzhEdy2xMJyRsxhrZb1vZLjfYU5iYhaX623ty-g19_c0YhbBY-xjRu.png)

### Google Search Console

If you have access to your website's Google Search Console (GSC), there's a chance the sitemap has been submitted there.

Head to the “**Sitemaps**” report in the “Indexing” section of the left menu.

![Navigation to sitemaps in google search console](https://static.semrush.com/blog/uploads/media/ac/78/ac785499f500efeff39354579f1da28d/a12132976aa891c864dc254f23e916d6/AD_4nXfiJ33qqGuUiJpCeN9M50_azaAUkV9uxYyCqZETjf28Llgx2m_Khht3B_hPGpJSABRGp3xAgSrGq8amCIx06CLyHesYtt5fGeFHETKTfIPzQxvNNPMiDXbbhG1nMaEZHD2vKugxVBPNNToYQvCm0qHxApw.png)

Here, you'll see a section called “Submitted sitemaps.”

If someone has submitted an XML sitemap before, you'll find its URL in the list.

![Submitted sitemaps in google search console](https://static.semrush.com/blog/uploads/media/fd/84/fd846f2b04fd6e5c44d901226a5e45f1/c87df585a950629c50e956a604c3bee2/AD_4nXfGrxFH_gozuqerlErUMDqJ_gMKB6dlPVr8iqMHN6tdeEfwKsL-J_k1FepYjuTEDGSZJPuJIlaYHgiyc-WkOhE5xwa5drQgus0vtgF5BReMJl8p8mneuFmDGMHcM6ZnxmoGN08_MH7yVzAIX64OK8j63zjW.png)

### Robots.txt

A [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) file tells search engine crawlers which sections of the website they should crawl and which they should avoid.

It should go in the root folder of your site: “https://domain.com/**robots.txt**.”

If the robots.txt file follows best practices, it’ll link to the website sitemap. Just search for “sitemap” within the robots.txt file.

The section linking to a sitemap will look something like this:

![section linking to a sitemap in robots.txt](https://static.semrush.com/blog/uploads/media/5a/aa/5aaaa79f9b04e26fe272ddf7c34d27a7/199f94aa4cc3fe259166a8096b640313/AD_4nXfMJU4whNkpplq_6AXOKr6kdElZyiEYzGb8ffuooFCZVwdVJiHd1cws6Yr1EY6NqcSNK276J91fxW4OOQlW43_1Bv6fIvrMHu-bheBn45ikrRnajpnZYkJkHMRIQSLmuMhg611UNiqJzgBcO5BGqO3uECQ.png)

## How to Review Your Sitemap for Issues

Run a free [website audit](https://www.semrush.com/siteaudit/) to confirm your sitemap is valid.

For a full crawl that detects sitemap problems and other technical issues, use Semrush Site Audit. It works similar to the way Googlebot does.

To begin, add your homepage URL to the text bar. Then, click “**Start Audit**.”

![enter yourdomain.com into site audit](https://static.semrush.com/blog/uploads/media/3e/17/3e1799665d03cff78fa48a353ac4f107/c8821fe67cd1e817c6c68f400db68319/AD_4nXcKSURhrF6bqh90kxEE1z1UPB7SJwOUI4lhQv2r-wsSMc2noUh5wgjiAxJyNAZm36w9X5BxjlrOM4yWF6S4jSe2BmZls-7p-KWjW9MGkkG2AhhIzBfQkgOjE-XRtp0nBc53Qi8zNLLji8PbpSLfkbYaKotX.png)

Next, choose your settings for the audit.

Follow our [detailed setup guide](https://www.semrush.com/kb/539-configuring-site-audit) if you need help.

Next, click “**Start Site Audit**.”

![site audit setting pop up](https://static.semrush.com/blog/uploads/media/80/dc/80dc486f23f2513342e8f749252a654b/43501aef366ac7bbccc6fd62195b322b/AD_4nXcrnctH25G-a11jOUwcMl9xc-CrseDQPSOEXfZijgJ9wRz0wlGNnoH255wI21DTp-2hQR868kDGgycC83q92jQMTKs7hsrzlEyTf1NlXETlh-r1CwVS5P4O-zEaCuR-s1ZIlbFYOSpiN_o28yn3ZD3aBy2h.png)

Once the audit is complete, you’ll arrive at the tool's “Overview” report. Here’s what it looks like:

![site audit overview report shows site health, total errors, and thematic reports](https://static.semrush.com/blog/uploads/media/21/a9/21a9af6804f53bfe43d4e6546b25ed9f/61b5d9fe498758e7d01891aa9dd2a3d2/AD_4nXcWdDnSqqfW2uv2UbpXxKvjqrdzAaVJDXJBjXLW5tXsFiBcR6NHhN55FUjglJy9Hc0zKd45m4Yyagwnk4Q4VJgeoDKSOV6wyYjtqu_YGcMZ0Z4GlX4M21gXsjr30TJhiZEg4LSZBNySWTZACVbfDQvyM8S7.png)

Click the “**Issues**” tab. Then, search for “**sitemap**” in the text box.

![search for "sitemap" in site audit issues](https://static.semrush.com/blog/uploads/media/a7/3d/a73d91cbd7d0ba72c30f6b1b81146e22/b2aa14afdb48d5fe4c1c90d41ed2d512/AD_4nXfv83cJs5bT0XNVMmItUj2JO3-RsBVyxGWhg9Oxur2d-er5OXWCajO7qiVnKR7lCZBfxPsV7vK6v6-OVZ6hzW1RMrj7AQaQAiOa6wIYJE798eazVkPWUbhkb8TeS3h49_uvfxj7z7M49cWlNTJhFntgfRE.png)

You'll get a list of issues related to your sitemap.xml file.

Address “Errors” first, then move on to “Warnings” and “Notices.”

![website sitemap issues found in site audit include incorrect pages, format errors, not found, and orphaned pages](https://static.semrush.com/blog/uploads/media/9b/1b/9b1b0d589b337278c1505a9cf232f246/33b0a781d6314475d28c86c9ee83a312/AD_4nXd_FI6Nox73iMiKGVhFfiZJmXTzlpfdXN9aph55RUbqE3cWifESKkoVFotuI8crSEIt97W1SPRL2EHLG_oMmnBS3kKXy7tAJ9BVZUNKu8675YDpUgAW57SZZz62tkNtbLAR7o6afIgWKgJ0RicTfbqfelwS.png)

Some common sitemap-related issues include:

- **Sitemap has format errors**: There are format errors (like missing XML tags) in your sitemap file
- **Incorrect pages found in a sitemap**: Your sitemap contains pages that aren’t supposed to be in a sitemap (like pages with [redirects](https://www.semrush.com/blog/redirects/) or pages that aren’t [canonical](https://www.semrush.com/blog/canonical-url-guide/) versions)
- **Sitemap files are too large**: Your sitemap exceeds Google's size limit (more than 50MB or more than 50,000 URLs)
- **Sitemap not indicated in robots.txt**: Your robots.txt file doesn’t indicate the path to your sitemap. Including this path is a best practice because it directs search engines to your sitemap. And facilitates faster and more complete indexing.
- **Sitemap not found**: The sitemap URL provided returns a 404 error. This could be due to a typo in the sitemap URL, the sitemap not being uploaded, or it being placed in the wrong directory.
- **HTTP URLs in sitemap for HTTPS site**: Your sitemap contains HTTP URLs on an HTTPS site. All URLs should be HTTPS to prevent duplicate content issues and security warnings in browsers.
- [**Orphaned pages**](https://www.semrush.com/blog/orphan-pages/) **in sitemaps**: These are pages that are listed in the sitemap but don’t have any internal links pointing to them from other pages on the site. This makes it hard to find them and can limit those pages’ ability to rank well.

Click one of the links with the number of affected pages to see a full list of pages with that specific issue.

![number of incorrect pages found in sitemap.xml highlighted](https://static.semrush.com/blog/uploads/media/04/00/0400548c8455379ee2677fd4f0f7fb28/dc36099785d1cd7e8422b59df6aa56e4/AD_4nXe1yyWrD_LXDVOJa8mFTdy2X_JE9eOTXhePxsHhbg9oe7BlUIiVX50nzpnKHkNr1XnaWfLpsjdoBnvQrFHIdrlzyq0Ql4ICLVVwHXUdCQoxjEx78OEDrmiNqGVin5nkoiViMRVFrtr-7PhlMp-Fu84eSlYr.png)![list of sitemap urls and the link urls with issue type. for example non-canonical URL or redirect.](https://static.semrush.com/blog/uploads/media/d8/12/d812930291c207f3ce7e46d653ce5261/4cf6971d321203b2e2628f1ab65a1a31/AD_4nXd94y9cRW7nYJCYT0vO5VBwFxAdKCuyRdqI7EYWVZzHRcybTL7YGlcJa5LYEwSDNBra7AbisAsSOOaXazBo_Y2hwQSOlpLiCQglKEwQ5Cgj2U0u7Tee1inNTGnmhE6nqc3YD4ayN8rUsjU68FZ4-VcyJtA.png)

Next, click “**Why and how to fix it**” next to each type of issue.

This will open a window with an explanation of the problem. And tips on how to fix it.

![why and how to fix incorrect sitemap issues pop up](https://static.semrush.com/blog/uploads/media/5b/c4/5bc4a551bde520ce395a00df9cff7262/d9c12c4484cae32d1ce853c2de9384eb/AD_4nXcsk_rEdJ6lKBOnQ4VOtlMQMibBlqIunQXY8t2XwrRexr49yrjwnxowfZDV-1wbCmCQDddofee7BENfZLa5K-SfTZR1WJEybVD-oQVrd0Ht3aNU2DiCYSrN83lq-NxHpNZLE6dEwgqC0kcpM58ZQfDf1-AU.png)

Go through the list and implement the necessary changes.

Then, rerun the audit to confirm that all issues have been successfully resolved.

## How to Submit a Sitemap to Google

Submitting your XML sitemap to Google is an SEO best practice.

Why?

- It can speed up the process of Google discovering your sitemap
- It can help you detect issues with your sitemap

Submit your sitemap in [Google Search Console](https://www.semrush.com/blog/google-search-console/). (If you don't have an account yet, create one so you can [log in to GSC](https://search.google.com/search-console).)

To submit your sitemap, go to the "**Sitemaps**" report. You'll find it in the "Indexing" section of the left menu.

![navigate to Sitemaps in google search console](https://static.semrush.com/blog/uploads/media/41/6b/416b7ad74bf67e5d9005aa6eae93071d/38ed13b562b534959801a53821a3702c/AD_4nXd2U4b1tt7YloMGXbNCaCNrGXVsTefGEp0tb3IM_dmAvS7pJRH7UViFrUO24qOKy0bXChUTZ7N_jLYaL_e8cb5Cs2yHSmkyLmteEKa62WZciCBgHb_uTj1vgaC3WcgE1riZzQD3QMJg1TGSiKCZM_WAAXte.png)

There, enter your XML sitemap’s URL in the “Add a new sitemap” section. And click the “**Submit**” button.

![Submit a new sitemap](https://static.semrush.com/blog/uploads/media/41/51/415119444cdaef69aad7873a85da99ab/9afabcd8b9753ffe921a2d1aea58450d/AD_4nXf94D5pKZxtr0zWyO9Ju4wCJpDObSX0GCHJhEj3Ud_evyGm3u8RIHAs8hLfsn7eLNzrfPpqMhAQ6JI9jOF_zxg0EC8KqUiL0wZa1hg15Tx7kr-8fCdAzyI5nLSzDzUZc6of8pCP0cCKk8pqYHiaf5Sv2F8.png)

After you've submitted your sitemap, you'll get a message like this:

![sitemap submitted successfully message](https://static.semrush.com/blog/uploads/media/31/27/3127dc51be933706415396c08c786bec/45045c5abfdbc0b451010338d327f306/AD_4nXeRyNO2pDULNysKLPxwZVTfA2Xa7-Q9PCkcuoBF3CIXQXmirRD2wZ3xk0ChL_NoMuQye-qw_DFcHul9SmyQ1gOVHdC8vuyyKGh1HByRgy03HJUjeZMYOTwC4IlUnvu2KIfxK1SVg4dMkvIpk8Ksd_IyxAo.png)

For a more in-depth guide, read our post on [how to submit a sitemap to Google](https://www.semrush.com/blog/submit-sitemap-to-google/).

Monitor the status of your sitemap anytime you visit the report. If there's a green “Success” message, you're all good.

If there's an issue with your sitemap, you'll see a red “Couldn't fetch” or “Has errors” status. In this case, the report will provide a detailed explanation of what went wrong and how to fix it.

Check the full list of possible errors and how to fix them in Google’s [guide to the “Sitemaps” report](https://support.google.com/webmasters/answer/7451001).

## FAQs

Below are some common questions related to sitemaps. With answers and additional resources.

### Do I Need a Sitemap for a Small Website?

Google states that websites with 500 or fewer pages [may not need a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview#:~:text=A%20sitemap%20helps%20search%20engines,benefit%20from%20having%20a%20sitemap.). But only if all of the pages are properly linked and discoverable by search engine crawlers.

That said, there are no downsides to having an XML sitemap. And if your website regularly updates content for SEO purposes, a sitemap can speed up the process of Google finding those changes.

### What Shouldn’t Be Included in a Sitemap?

All of the pages listed in your sitemap should show Google that your site is high-quality and well-maintained.

That means you should leave out some pages. Such as:

- Pages with 3xx, 4xx, or 5xx status codes
- Orphaned pages
- Duplicate pages
- Pages that aren’t the canonical version
- Pages with a “noindex” robots tag
- Pages blocked in your robots.txt file

### How Big Is Too Big for a Sitemap?

A single sitemap should be limited to 50MB or 50,000 URLs.

Google encourages users to follow best practices outlined by [sitemaps.org](https://www.sitemaps.org/protocol.html).

If yours exceeds the size limits, you’ll need to [split up your sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps).

Then, create and submit a sitemap index file to Google. So it can identify all of your sitemaps.

### How Often Should You Generate a Sitemap?

The more often you update and publish new content, the more often you should generate a sitemap.

As a general rule, we recommend auditing your sitemap once per month. If you publish multiple pieces of content per day, you may need to update your sitemap on a weekly basis.

Just keep an eye out for errors. Which is easy with our [website audit](https://www.semrush.com/siteaudit/) tool.
