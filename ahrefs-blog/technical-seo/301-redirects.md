---
title: "301 Redirects Explained: How They Impact SEO"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "301-redirects"
url: "https://ahrefs.com/blog/301-redirects/"
canonical: "https://ahrefs.com/blog/301-redirects/"
author: "Joshua Hardwick"
published: "2019-04-16T14:50:44+00:00"
updated: "2025-06-23T15:51:54+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
fetched_at: "2026-06-12T11:09:14+00:00"
status_code: 200
html_hash: "0dd434275b882533196da4439d4b565c25143de7be7788db08938ce32e79417b"
clean_word_count: 5669
clean_char_count: 33500
---
# 301 Redirects Explained: How They Impact SEO

Looking to learn everything there is to know about 301 redirects, including how to use them to boost your organic traffic? You’re in the right place.

301 redirects are pretty simple. They’re used to redirect one webpage to another.

But understanding how they relate to SEO is more complicated.

In this guide, you’ll learn:

- [What 301 redirects are](#what-is-a-301-redirect)
- [How to implement them](#how-to-do-a-301-redirect)
- [How they affect SEO](#do-301-redirects-affect-seo)
- [How to fix SEO issues caused by 301 redirects](#how-to-fix-301-redirect-issues)
- [How to use 301 redirects to (potentially) boost organic traffic](#how-to-use-301-redirects-to-boost-traffic)

Let’s start at the top.

New to technical SEO? Check out our

[Beginner’s guide to technical SEO](https://ahrefs.com/blog/technical-seo/)

## What is a 301 redirect?

A 301 redirect indicates the permanent moving of a web page from one location to another.

The 301 part refers to the [HTTP status code](https://ahrefs.com/blog/http-status-codes/) of the redirected page.

**Example:** *blog.ahrefs.com* redirects to ahrefs.com/blog

In simple terms, a 301 redirect tells the browser: “This page has moved permanently. This is the new location and we don’t intend on moving it back.” To which the browser responds: “Sure thing! I’ll send the user there right now!”

That’s why if you try to visit *blog.ahrefs.com*, it won’t happen.

You’ll end up at *ahrefs.com/blog* instead.

## How to do a 301 redirect

There are many ways to do 301 redirects, but the most common method is to edit your site’s .htaccess file.

You’ll find this in your site’s root folder:

Don’t see the file? That means one of **two** things:

1. **You don’t have a .htaccess file.** Create one using Notepad (Windows) or TextEdit (Mac). Just create a new document and save it as .htaccess. Make sure to remove the standard .txt file extension.
2. **Your site isn’t running on an Apache web server.** This is somewhat technical, but there are different types of web servers. Apache, Windows/IIS, and Nginx are the most common. Only Apache servers use .htaccess. To check that your website runs on Apache, ask your web host.

Here are some snippets of code for adding common types of 301 redirect via .htaccess:

**IMPORTANT.** These instructions are for Apache web servers only. Read [this](https://bjornjohansen.no/nginx-redirect) if your site runs on Nginx, or [this](https://www.bowlerhat.co.uk/301-redirects-for-seo-from-windows-server-iis) if your site runs on Windows/IIS.

### Redirect an old page to a new page

```
 Redirect 301 /old-page.html /new-page.html
```

Using WordPress? Remove the need to edit the .htaccess file with the free [Redirection plugin](https://wordpress.org/plugins/redirection/).

It makes adding 301 redirects as simple as this:

### Redirect an old domain to a new domain

```
 RewriteEngine on
RewriteCond %{HTTP_HOST} ^oldsite.com [NC,OR]
RewriteCond %{HTTP_HOST} ^www.oldsite.com [NC]
RewriteRule ^(.*)$ https://newsite.com/$1 [L,R=301,NC]
```

Sidenote.

There are quite a few ways to do this. I am by no means an expert when it comes to Apache servers and htaccess files. This is the code that has always worked for me. Make sure to test this before implementing on your site.

**IMPORTANT!** If `RewriteEngine on` is already in your .htaccess file, do not repeat it. Just copy the rest of the code. It’s also possible to do this in Cpanel, which may be preferable.

### Redirect entire domain from non-www to www (and vice-versa)

Here’s the non-www to www version:

```
 RewriteEngine on
RewriteCond %{HTTP_HOST} ^example.com [NC]
RewriteRule ^(.*)$ http://www.example.com/$1 [L,R=301,NC]
```

Here’s the www to non-www version:

```
 RewriteEngine on
RewriteCond %{HTTP_HOST} ^www.example.com [NC]
RewriteRule ^(.*)$ http://example.com/$1 [L,R=301,NC]
```

**IMPORTANT!** The placement and order of code in your htaccess file matters too. You may experience unwanted effects if multiple instructions are placed in the “wrong” order (e.g., redirect chains, etc.). If you’re planning to implement a lot of 301 redirects in your htaccess file, this is something worth looking into.

### Redirect entire domain from HTTP to HTTPS

```
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

**IMPORTANT!** You must have an SSL certificate installed on your website for this to work. Otherwise, you’ll get the cautionary “Not secure” message.

### Redirect entire domain from non-www to www *and* HTTP to HTTPS

```
RewriteEngine On
RewriteCond %{HTTP_HOST} !^www\. [NC]
RewriteRule ^ https://www.%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
RewriteCond %{HTTP:X-Forwarded-Proto} !https
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

## Do 301 redirects affect SEO?

Most SEO professionals focus on the relationship between 301 redirects and PageRank.

Not familiar with [PageRank](https://ahrefs.com/blog/google-pagerank/)? It’s the formula Google created to judge the “value of a page” based on the quantity and quality of its links. Of course, PageRank is far from the only “ranking factor,” but it’s generally believed that, on the whole, higher PageRank equates to higher rankings.

Is there evidence for that? Yes, Google (re)[confirmed](https://twitter.com/methode/status/829755916895535104) PageRank as a ranking signal last year:

> DYK that after 18 years we’re still using PageRank (and 100s of other signals) in ranking?
>
> Wanna know how it works?<https://t.co/CfOlxGauGF> [pic.twitter.com/3YJeNbXLml](https://t.co/3YJeNbXLml)
>
> — Gary “鯨理” Illyes (@methode) [February 9, 2017](https://twitter.com/methode/status/829755916895535104?ref_src=twsrc%5Etfw)

There’s also a clear positive correlation between [Ahrefs’ URL Rating](/blog/ahrefs-seo-metrics/#section9)—which works in a similar way to PageRank—and the amount of organic traffic a page gets:

Sidenote.

The reason why I’m talking about URL Rating (UR) and not PageRank is that Google discontinued public PageRank scores in [2016](https://www.searchenginejournal.com/google-pagerank/159112/). Now there’s no way of knowing how much PageRank a page has. I’m not saying that UR is a PageRank equivalent by any stretch, but it’s the closest comparable metric we have.

So how does this relate to 301 redirects?

Before 2016, if you used a 301 redirect to redirect one page to another, there was some loss of PageRank along the way. How much? That’s debatable, but 15% seemed to be the general assumption. It’s also the range Matt Cutts, Google’s former Head of Webspam, alluded to in this 2013 video:

Sidenote.

Matt didn’t actually say that 301 redirects lost 15% of PageRank in that video. That was just the figure he used as an example. However, it’s the number that most SEO professionals seemed to run with for quite a few years. That’s likely because 15% also relates to the “damping factor” in the [original PageRank patent](https://patents.google.com/patent/US6285999B1/en).

For argument’s sake, let’s assume that the number was 15%.

Here’s how that would play out:

> **Simple 301 redirect:** *domain.com/page-1 → domain.com/page-2* = **15% loss of PageRank**

> **301 redirect chain:** *domain.com/page-1 → domain.com/page-2* *→ domain.com/page-3 → domain.com/page-4* =**38% loss of PageRank!**

However, Google changed its [official stance](https://twitter.com/methode/status/757923179641839616) on this matter in 2016:

> 30x redirects don’t lose PageRank anymore.
>
> — Gary “鯨理” Illyes (@methode) [July 26, 2016](https://twitter.com/methode/status/757923179641839616?ref_src=twsrc%5Etfw)

So, in 2019, if you redirect *domain.com/page1* to *domain.com/page2*, the redirected page should have just as much “power” as the original page.

That’s a BIG deal, and it’s part of the reason 301 redirects can be so useful for boosting organic traffic. *(More on that later!)*

But 301 redirects can cause plenty of other SEO-related issues that don’t often get talked about.

## How to fix existing 301 redirect issues on your site

Here’s how to find and fix existing issues related to 301 redirects.

### 1. Make sure the HTTP version of your site redirects to HTTPS

Every website should use HTTPS.

Not only does it add an extra layer of security for your visitors, but [Google uses HTTPS as a ranking signal](https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html). Combine that with the fact that SSL certificates are available for free via [Let’s Encrypt](https://letsencrypt.org/) and there really is no excuse not to use HTTPS in 2019.

But having an SSL certificate is only half the battle…

You also need to make sure that people actually visit the HTTPS version of your site, which means using a 301 redirect between the HTTP and HTTPS version.

To check that this redirect is in place, go to your homepage and look at the URL bar. You should see http**s**://[www].yourwebsite.com/, plus a lock icon.

Change this to http:// (not http**s**://) then hit enter. You should be redirected to the HTTPS version automatically.

If this happens, then things should be good for the most part. But there can still be issues, like:

- HTTP to HTTPS redirect isn’t implemented across all pages on your site (e.g., subdomains).
- HTTPS to HTTP redirects

To be sure there are no such issues, run a crawl with [Ahrefs’ Site Audit](https://ahrefs.com/site-audit).

Head to the **Internal pages** report and look for these issues:

**NOTE.** If you see one page with an HTTP to HTTPS warning, and it’s merely the HTTP version of the page from which the crawl began, then this isn’t an issue.

Fix these issues by applying the proper 301 redirects from the HTTP to HTTPS version(s) of the affected page(s).

### 2. Remove pages with 301 status codes from your sitemap

Google looks to sitemaps to understand which pages to crawl and index.

Because pages with 301 status codes no longer technically exist, there’s no point asking Google to crawl them. If such pages remain in your sitemap, Google may continue to revisit them each time they re-crawl your website. That’s unnecessary and wastes [crawl budget](https://ahrefs.com/blog/crawl-budget/).

Here’s one way to find such pages:

1. Find your sitemap URL (this is usually *yourdomain.com/sitemap.xml*… but not always)
2. Use [this tool](http://convertcsv.com/url-extractor.htm) to download all the URLs.
3. Paste that list of URLs into [this free HTTP status code checker](https://httpstatus.io/) (note: limited to 100 URLs at a time)
4. Filter for pages with 301 status codes.

Looking for a quicker and easier method? Use [Ahrefs’ Site Audit](https://ahrefs.com/site-audit) to crawl your website, then head to the **Overview** report and look for “3XX redirect in sitemap” errors.

Clicking this reveals all the pages with 301 status codes in your sitemap(s).

Remove these [URLs](https://ahrefs.com/blog/seo-friendly-urls/) from your sitemap and replace with the final redirect URL (if it’s not already in there).

### 3. Fix redirect chains

Redirect chains occur when there is a series of two or more redirects between the initial URL and destination URL.

Here’s [what Google says](https://support.google.com/webmasters/answer/6033086?hl=en) about these:

> While [Googlebot](https://ahrefs.com/blog/googlebot/) and browsers can follow a “chain” of multiple redirects (e.g., Page 1 > Page 2 > Page 3), **we advise redirecting to the final destination**. If this is not possible, keep the number of redirects in the chain low, ideally no more than 3 and fewer than 5.

Redirect chains serve no other purpose than to damage user experience and slow things down, so you should avoid them where possible.

You can check for redirect chains on up to 100 URLs using [this HTTP status code checker](https://httpstatus.io/).

Look for pages with two or more redirects.

To check more than 100 pages in one go, check the **Internal pages** report in [Ahrefs’ Site Audit](https://ahrefs.com/site-audit) for “Redirect chain” errors.

Clicking this will reveal all the URLs in the chain, including the final destination page.

There are two ways to fix these errors;

1. **Replace the redirect chain with a single 301 redirect.** Instead of *Page 1 > Page 2 > Page 3 > Page 4*, the redirect becomes *Page 1 > Page 4*.
2. **Replace internal links to redirected pages with direct links to the final URL**. This prevents Google and other bots from crawling the redirect chains. More importantly, it prevents *actual* humans (you know, the type who \*might\* buy something from your website) from having to deal with the slowness of multiple redirects when they click a link.

Where practical, the second solution is the best option.

To do that, sort the list of redirect chains by the “No. of inlinks” column from high to low. Then click on the number of inlinks to see all internal links to the redirected page.

Replace the internal links on the affected pages with the direct links to the final destination URL.

### 4. Fix redirect loops

Redirect loops occur when a URL redirects back to one of the other URLs in the chain. This creates an infinite loop of redirects that can confuse and trap both search engines and users alike.

**Example:** *Page 1 > Page 2 > Page 3 >* **Page 2***> Page 3 >* **Page 2***> Page 3 […]*

These are user-experience killers because they usually result in a response like this from the browser:

You can find redirect loop errors in batches of 100 using that same HTTP status code checker we used before. Look for “Exceeded maximum number of redirects” errors.

For more than 100 pages, check the **Internal pages** report in [Ahrefs’ Site Audit](https://ahrefs.com/site-audit) for “Redirect loop” errors.

Click this to reveal all pages with redirect loop issues, then fix each issue in one of two ways:

1. **If the URL is not supposed to redirect,** change its HTTP response code to 200.
2. **If the URL is supposed to redirect**, fix the final destination URL and remove the loop. Alternatively, remove or replace all inlinks to the redirecting URL.

### 5. Fix broken redirects

Broken redirects are pages that redirect to a dead page (i.e., one that returns a 4XX or 5XX HTTP response code).

**Example:** *Page 1 (301) > Page 2 (404)*

These are bad because neither visitors nor search engine bots can access the final URLs. Because of that, most visitors will leave your website, and most search engines will abandon the crawl.

You can check for these errors in batches of 100 using an HTTP status code checker.

To check more pages, look for “Broken redirect” errors in the **Internal pages** report in Ahrefs’ Site Audit.

Fix these errors by either:

1. Reinstating the dead page (if deleted accidentally)
2. Removing the inlinks to the redirected URL.

### 6. Redirect 404 pages

Pages that return a 404 status are dead, and so the browser returns a page like this:

Now, there are times when a user seeing this page makes sense. If someone types the wrong URL into their browser, for example, then the error page lets them know that something is wrong. You can see an example of that above—it makes total sense to return a 404 page for this URL.

Having said that, pages with 404 status codes are a problem when:

1. **They’re crawlable**. Crawlable *usually* equates to clickable. And if they’re clickable, some users are going to end up clicking [internal links](https://ahrefs.com/blog/internal-links-for-seo/) on your site only to see a dead page. That’s not great for user experience.
2. **They have backlinks**. Because 404 pages aren’t accessible, any backlinks that point to them are effectively wasted.

To tackle that first issue, check the **Internal links** report in Ahrefs’ Site Audit for “404 page” errors.

Click this to see all 404 pages that were found during the crawl.

Next, hit the “Manage columns” button, add the “No. of dofollow backlinks” column, hit “Apply,” then sort by this column from high to low.

Check the **Backlinks** report in [Ahrefs Site Explorer](https://ahrefs.com/site-explorer) for any pages with one or more “dofollow” backlinks. There’s a chance these links may be valuable. If they are, you’ll want to redirect (301) that page to another relevant resource on your website.

IMPORTANT

Redirecting 404 pages to **somewhere relevant** is key. Google treats irrelevant 301 redirects as soft 404’s, so there’s no real advantage of redirecting unless you’re doing so to a similar and relevant page.

Google’s John Mueller explains more in [this video](https://youtu.be/nIDZmac_rMI?t=76).

If you don’t have a similar or relevant page, and you still have a 404 page with lots of [high-quality backlinks](https://ahrefs.com/blog/high-quality-backlinks/) then, honestly, it may be worth republishing the content that used to exist at that location.

Think of it like this:

If the dead page was valuable enough to attract high-quality backlinks in the first place, then it’s worth questioning why it no longer exists. I mean, it’s clearly a topic people are interested in.

For pages **without** dofollow backlinks, fix them by either:

1. Reinstating the dead page at the given URL
2. Redirecting (301) the dead page to another **relevant** page
3. Removing or replacing all internal links to the dead page

**IMPORTANT**. If you opt for #3, make sure that you not only replace the internal links but also the anchor text and surrounding text where necessary.

### 7. Replace 302 redirects and meta refresh redirects with 301s

Never use 302 redirects or meta refresh redirects for permanent redirects.

302 redirects are for temporary moves, and Google [recommends](https://support.google.com/webmasters/answer/79812?hl=en) not to use meta refresh redirects at all if possible. So, if you have either of these on your site, you should aim to either remove them or replace with 301 redirects.

To see pages with these HTTP status codes, check the **Internal pages** report in Ahrefs’ Site Audit for “Meta refresh redirect” and “302 redirect” issues.

Luckily, both these issues can be fixed in the same way:

- **If the redirect is permanent,** use a 301 instead.
- **If the redirect isn’t permanent**, remove the redirect.

You should also aim to remove or replace internal links to redirected pages, especially if they’re likely to confuse users who click on them.

### 8. Look for redirected (301) pages that get organic traffic

Pages with HTTP 301 status codes shouldn’t get organic traffic because they shouldn’t be in Google’s index. If such pages are getting traffic, it means that Google hasn’t yet seen the redirect.

To check for 3XX pages with traffic, check the **Overview** report in Ahrefs’ Site Audit for “3XX page receives organic traffic” errors.

If you got your list of 3XX pages from elsewhere (e.g., an HTTP status code checker), then paste them into [Ahrefs’ Batch Analysis tool](https://ahrefs.com/batch-analysis) in batches of up to 200 to see page-level organic traffic.

**NOTE.** You could also check organic traffic in [Ahrefs’ Web Analytics](https://ahrefs.com/web-analytics) or Google Search Console.

Now, if you only recently added the 301 redirect, this likely isn’t much of an issue. Google should see it during their next crawl, after which they should deindex the page.

To speed up that process, paste the URL into the **URL Inspection tool** in [Google Search Console](https://search.google.com/search-console/about), then hit “Request indexing.”

You should also remove these pages from your sitemap (see #2) and re-submit via Google  Search Console.

### 9. Look for “bad” external 301s

Most websites link out to relevant third-party sites and resources.

That’s fine… until the page to which to externally link gets redirected elsewhere.

For example, imagine that you link out to a useful resource. Twelve months later, that domain expires and gets picked up by an expired domain hunter who deletes the resource and redirects to their “money” site. Now you’re unintentionally linking to something irrelevant (and potentially even harmful) to your visitors.

For this reason, it’s important to check for “bad” external 301’s from time to time.

To do this, head to the **External pages** report in Ahrefs’ Site Audit and look for “External 3XX redirect” warnings.

Click this to see a list of all the redirected external links, plus the final destination URL.

Seeing a lot of pages?

Because nofollowed external links are often things like blog comments, you can remove these to give a cleaner list. Just add a “No. of inlinks dofollow > 0” filter to the report.

This should help to prioritize things.

Next, skim the report looking at the *URL* and *Redirect URL* columns. Look for redirects that don’t seem right. In other words, ignore things like HTTP to HTTPS redirects, and *blog.domain.com/page* to*domain.com/blog/page* redirects. Look for redirects to different sites or pages.

Here’s an example I found when crawling *Backlinko*:

The issue here isn’t so much that the redirect points to another website. Those who are familiar with Neil Patel will know that he merged *blog.kissmetrics.com* with *neilpatel.com* earlier this year.

No, the issue is that the redirected page is a completely different article.

> **Original article title:** Using the Magic of Qualitative Data to Increase SaaS Conversions

> **Redirected article title:** How Understanding Your Customer Will Help You Create Copy That Sells

In these cases, it’s best to remove the internal link(s) to the redirected page.

To do this, just hit the number in the “No. of inlinks” column to see every page with internal links to the redirected page.

Go into your CMS and remove them.

## How to use 301 redirects to boost your organic traffic

By this stage, your website should be free of any SEO-hindering issues related to 301 redirects.

Now it’s time to get serious and talk about how we can use the power of redirects to massively boost organic traffic.

Here are **two** methods for doing that.

### The Cocktail Technique

You have a glass of Coke. *Mmm*. You have a glass of rum. *Tasty*!

Both of those are great drinks in their own right. Combine them, however, and you take things to another level.*Hello, [Cuba Libre](https://en.wikipedia.org/wiki/Rum_and_Coke)!*

So how does this relate to 301 redirects?

Think of both these drinks as **topically-related** pages on your website. They’re each performing okay. They have a few decent backlinks. They get *some* organic traffic. Not too bad at all. But why not merge and consolidate those two pages into one to make something even better?

In doing so, chances are that we could transform two average-performing pages into one delicious cocktail of a page that performs *way* better!

We recently did this with two of our posts on the Ahrefs blog:

1. https://ahrefs.com/blog/skyscraper-technique/
2. https://ahrefs.com/blog/skyscraper-technique-fail/

Both these articles were getting old, so we decided to merge them into [one new guide](https://ahrefs.com/blog/skyscraper-technique/).

We then republished at *ahrefs.com/blog/skyscraper-technique/* and redirected the other article to that.

The results speak for themselves:

So why does this work?

Two reasons:

1. **Consolidation of “authority”:** Remember how 301 redirects no longer “leak” PageRank? By redirecting one of these articles to the other, we were able to merge the “authority” of both pages into one. Of course, this doesn’t work if the pages are unrelated because Google treats such redirects as soft 404’s. But because these two pages are similar, this worked a treat.
2. **Better content:** Both of the articles we had were of decent quality. They were just starting to get a little outdated. By taking the best of both posts and merging them, we created a substantially better piece of content that, in our eyes, deserves more traffic.

Now, the only question that remains is how to replicate this strategy, right?

Here’s the process.

#### Step 1. Look for keyword cannibalization issues (with backlinks)

Keyword cannibalization is when two or more pages target and rank for the same keyword(s). Finding such issues is a good way to identify opportunities.

So, first things first, make a copy of [this Google Sheet](https://docs.google.com/spreadsheets/d/1KnXTPtbIq9EZxknJgHlyW5O4_UljEhBgQZYwQZAaPxo/copy).

Next, paste your site into [Ahrefs’ Site Explorer](https://ahrefs.com/site-explorer), head to the **Top Pages** report, and export it to CSV.

Import the CSV into the first tab of the Google Sheet.

To do that, Go to *File > Import… > Upload > Select the CSV > Choose “Append to current sheet” when asked*

That’s it. Go to the “Results” tab and you should have some refined results.

#### Step 2. Find relevant opportunities

Next up, you need to eyeball the results sheet for potential redirection opportunities.

Here’s a good example from the Hubspot blog:

These two pages rank in positions #5 and #6 respectively for “user generated content.”

Both of them:

1. Are topically *very* similar
2. Have plenty of backlinks from unique websites (467 referring domains combined!)
3. Get a bit of organic traffic

So let’s take a look at top-ranking pages for “user generated content” in [Ahrefs’ Keywords Explorer:](https://ahrefs.com/keywords-explorer)

Two things stand out about the current top-ranking page:

1. It gets almost 2x the traffic of the two posts from Hubspot combined!
2. It has links 192 referring domains… less than half of the 467 referring domains to Hubspot’s two posts

So if Hubspot were to merge these two posts into one, and consolidate all that delicious “link juice,” then I’d say they’d have a good chance at claiming the number one spot. This could potentially 2x their traffic!

#### Step 3. Rewrite and merge the pages

Now it’s time to take the best things about each page and combine them into one.

For example, if we were doing this for the aforementioned Hubspot articles, we’d probably keep the section about “How to Run Your Own User Generated Content Campaign” from one post:

… and keep the part explaining “Why User-Generated Content?” from the other:

To keep the relevance of the new page as high as possible, and mitigate the risk that Google will treat our 301 as a soft 404, we could also check the **Anchors** report in Site Explorer for each page:

This gives some insight into why people linked to the pages in the first place.

For example, I can see that a fair few people are quoting statistics when linking to this page, so it may be worth keeping those stats in our revamped post.

PRO TIP

You should also take the rewriting/merging of two pages as an opportunity to better serve search intent and give searchers what they’re looking for. If there are a lot of top 10 lists ranking for the target keyword, make your new revamped post a top 10 list. If there are a lot of how-to guides, well… you get the idea!

**NOTE.** That has nothing to do with 301 redirects, but it’s worth doing if you want to maximize the ROI of your efforts.

#### Step 4. Publish your revamped page and implement the 301 redirect(s)

Now it’s finally time to publish your revamped post/page.

If either of the old URLs is a good match for your new post, then feel free to republish at the same URL. You can then delete the other post/page and add a 301 redirect to the new post.

You may recall that’s what we did with our*skyscraper technique* post. We reused the /skyscraper-technique/ URL.

If neither of the old URLs is a good match for your new post/page, then it’s also perfectly fine to 301 redirect **both** pages to a totally new URL.

For example, if we were to merge those two Hubspot posts into this guide:

… then neither of the two old URLs would really fit the bill.

It would be better to publish at something like blog.hubspot.com/marketing/user-generated-content/

So, we could do that, then 301 redirect the other two pages to that URL. Simple.

TIP

Looking to take this idea even further? Do a [content audit](https://ahrefs.com/blog/content-audit/) to find pages with no organic traffic or rankings that still have backlinks.

If these pages aren’t important to your business, delete and redirect them to a **relevant** page that does matter.

### The Merger Method

Here’s what happened to one site’s organic traffic after using the merger method:

That’s a**~116% traffic increase** in 12 months!

Here’s the process in a nutshell:

1. Buy another business or website in your industry.
2. Merge their site with yours using 301 redirects.

Backlinko’s Brian Dean did this last year. He bought another [SEO blog](https://ahrefs.com/blog/)—*Point Blank SEO*—and redirected it to Backlinko. In fact, it was he who used this method to achieve the results you see in the screenshot above.

But before you start buying every website you can get your hands on, understand this:

Having success with this method isn’t as simple as just buying any old website and using 301s to redirect **all** pages to your homepage. That’s the lazy approach, and in 2019, it’s not a good idea. You also need to implement 301 redirects on a page-by-page basis.

Here’s how to do it, step-by-step:

#### 1. Re-home and redirect content

The biggest traffic gains are likely to come from re-homing and redirecting content.

Brian Dean did this with some of the posts on *pointblankseo.com*, including Jon’s infamous list of link building strategies.

You know, the one with this backlink profile:

**This original URL was:** *pointblankseo.com/link-building-strategies*

**The new (redirected) URL is:** *backlinko.com/link-building-strategies*

Because Brian moved the post from the old domain to the new with a 301 redirect, all of those links now effectively point to that same page on *backlinko.com* instead. The page has effectively just moved to a new home.

The re-homing and redirecting of content is the best option when all of these apply:

- The content has organic traffic
- The topic is relevant to your business
- The content is high-quality

Note that you can combat that final point but updating or rewriting the content after moving and redirecting it. Brian did this with that list of link building strategies, which hadn’t been updated since around 2012.

#### 2. Delete and redirect to a different page

There’s no point keeping or re-homing pages that:

- Have little or no organic traffic potential.
- Are duplicates of topics you’ve already covered

For example, there’s no point keeping the *about us* page from the website you’re merging because then you’ll have two about us pages… which makes no sense. This is also true of other pages which target the same keywords as existing pages on your website.

Re-homing these will just lead to [keyword cannibalization](https://ahrefs.com/blog/keyword-cannibalization/) issues.

Similarly, if pages have little or no traffic potential, then you may as well get rid of them and redirect elsewhere. This is what Brian did with quite a few posts on *pointblankseo.com*, such as this post about outreach platforms:

That post no longer exists. Brian redirected it to his blog post about [link building tools](https://ahrefs.com/blog/link-building-tools/).

**This original URL was:** *pointblankseo.com/outreach-platforms*

**The new (redirected) URL is:** *backlinko.com/link-building-tools*

He did this because the keyword “outreach platforms” has no search volume and no traffic potential. It’s not a topic worth targeting.

So it made more sense to redirect this post to another relevant post **with** traffic potential.

#### 3. Delete and redirect to your homepage

If there’s nowhere relevant to redirect pages, and it doesn’t make sense to move and re-home them, then the last resort is to redirect them to your homepage.

Brian did this with most of the pages on *pointblankseo.com*, such as this ego-bait guide:

**This original URL was:** *pointblankseo.com/egobait-guide*

**The new (redirected) URL is:** *backlinko.com/blog*

Why is this a last resort? Well, remember what we covered earlier about Google treating irrelevant 301 redirects as soft 404’s. This may happen when redirecting posts and pages to your homepage.

But here’s the thing: if you **don’t** redirect these pages, then there’s a 100% chance of Google treating them as soft 404’s. Conclusion: you may as well redirect them.

There’s one caveat to this, however, which is that you shouldn’t redirect pages with low-quality backlinks. Doing this is likely to cause more harm than good, so make sure to check the **Backlinks** report in [Site Explorer](https://ahrefs.com/site-explorer) for each page before redirecting.

If the backlink profile looks like this…

… then it’s probably best to just delete that page and leave it as a 404.

Or, if you really feel the need to redirect the page, then you could [disavow](https://ahrefs.com/blog/google-disavow-links/) the bad links before doing so. However, this is likely more effort than it’s worth.

## Final thoughts

301 redirects have a lot of uses when it comes to SEO.

Use them strategically and you could see huge gains in organic traffic. However, it pays to make sure there are no existing problems with 301 redirects on your website first, as these could be hindering your current and future SEO efforts.

Did I miss anything in this guide? Let me know in the comments or [via Twitter](https://twitter.com/joshuachardwick?lang=en).
