---
title: "How to Find and Fix Broken Links (to Reclaim Valuable \"Link Juice\")"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "fix-broken-links"
url: "https://ahrefs.com/blog/fix-broken-links/"
canonical: "https://ahrefs.com/blog/fix-broken-links/"
author: "Joshua Hardwick"
published: "2018-04-12T15:09:06+00:00"
updated: "2024-06-16T22:05:21+00:00"
categories:
  - "Link Building"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T11:31:28+00:00"
status_code: 200
html_hash: "444c406ec74c17c56f650a45ca1398ea3e00ae3beb64347b875d082f742919bf"
clean_word_count: 2817
clean_char_count: 16240
---
# How to Find and Fix Broken Links (to Reclaim Valuable “Link Juice”)

Do you want to reclaim “link juice” and improve user experience? Then it’s time to find and fix your site’s broken links and broken backlinks.

Doing this will almost certainly have a positive impact on your rankings.

But it’s important to note that broken links and backlinks are two entirely different problems.

As such, I’ve divided this post into two sections:

1. How to find and fix **broken links** (i.e., broken links **on** your site).
2. How to find and fix **broken backlinks** (i.e., broken inbound links **to** your site).

Both of these fixes will help to reclaim so-called “link juice” across your site and improve user experience.

> ***IMPORTANT!** This post is NOT about the so-called “broken link building” strategy, which involves exploiting your competitors’ broken backlinks to build new links to your site. If you wish to learn more about this strategy, check out [our full guide to broken link building](https://ahrefs.com/blog/broken-link-building/).*

Let’s rock!

New to link building? Check out our

[Beginner’s guide to link building](https://ahrefs.com/blog/link-building/)

## 1. How to find and fix broken links on your website

Broken links are those on your site that point to non-existent resources—these can be either internal (i.e., to other pages on your domain) or external (i.e., to pages on other domains.)

This is what a broken **internal** link looks like:

![](https://ahrefs.com/blog/wp-content/uploads/2018/04/broken-internal-links-3.gif)

*(It goes from one page on ahrefs.com to another—yet the page it points to doesn’t exist.)*

…And this is what a broken **external** link looks like:

*(It goes from a page on ahrefs.com to a non-existent page on another domain.)*

Here are the only two ways that broken (dead) links can end up on your website:

- The linked-to site decides to delete or remove the page you are linking to—this is known as “[link rot](https://ahrefs.com/blog/link-rot-study/)”;
- You unwittingly end up linking to the wrong URL (i.e., you make a mistake when adding the link to your website)

Some people say that broken outgoing links (both internal and external) effectively waste “link juice”—this is due to the way [Google’s PageRank algorithm](https://ahrefs.com/blog/google-pagerank/) works.

Some people also say that they hinder your websites crawlability.

*(For more information on the issue of “do 404’s hurt my site?”, check out* *[this article from Google](https://webmasters.googleblog.com/2011/05/do-404s-hurt-my-site.html)**.)*

But technicalities aside, one thing is for sure: **broken outgoing links (both internal and external) lead to a poor user experience**.

You should, therefore, make every effort to fix them—it’s easy, I promise!

### Step #1: Finding ALL broken links on your site

For small websites, you can use Site Explorer to find all broken **external** links.

*(It will pick up most, if not all, of the broken external links for smaller websites.)*

**[Site Explorer](https://ahrefs.com/site-explorer)** -> **yourdomain.com** -> **Outgoing links** -> **Broken links**.

Sidenote.

You can view this report for any site, it doesn’t have to be a site that you own. Check out [our guide to broken link building](https://ahrefs.com/blog/broken-link-building/) to see how this can be used to build new backlinks to your site.

But for larger websites, it’s better to use [Site Audit](https://ahrefs.com/site-audit); this will perform a live crawl of your website and thus, will ensure that you don’t miss any broken links.

To see broken **external** links (with Site Audit):

**Site Audit** -> **Project** -> **External Pages** -> [**HTTP status codes**](https://ahrefs.com/blog/http-status-codes/) -> **4XX.**

But what about broken **internal** links? (e.g., *yourdomain.com/page* -> *yourdomain.com/broken-page*)

You will need Site Audit for this, too.

To see broken **internal** links (with Site Audit):

**Site Audit** -> **Project** -> **Internal Pages** -> **HTTP status codes** -> **4XX.**

Sidenote.

Ahrefs isn’t the only tool you can use to find broken links on your site. You can also check the [crawl errors in Google Search Console](https://support.google.com/webmasters/answer/35120?hl=en), use crawling tools like [Xenu’s Link Sleuth](http://home.snafu.de/tilman/xenulink.html) and [Screaming Frog SEO Spider](https://www.screamingfrog.co.uk/seo-spider/), or if WordPress powers your website, you can install a [Broken Link Checker plugin](https://wordpress.org/plugins/broken-link-checker/).

### Step #2: Fixing ALL broken links on your site

In all honesty, this is quite an easy task—it’s just super-boring!

Here are the two possible fixes:

1. **Replace****the broken links with live links:** Depending on how many broken links you find on your website, this could take all of 5 minutes, or weeks. The process itself is pretty self-explanatory—find a replacement for the broken link, then replace it on your site. (Oh, and if you’re unsure what the link used to point to, try throwing it into the [Wayback Machine](http://archive.org/web/).)
2. **Remove the links:** Again, this can be time-consuming if you have a lot of broken links, but the process is straightforward—locate the link in the content, then just remove it.

As I said, this is a pretty mundane task, so it may be worth hiring a VA to do this for you.

They are ten a penny on UpWork.

*(Seriously, this beats doing it yourself!)*

## 2. How to find and fix broken backlinks to your website

Broken backlinks are **broken inbound links from other websites to your site**.

This is what a broken backlink looks like:

*(It goes from a page on urlprofiler.com to a page on ahrefs.com—i.e., our website.)*

Because the page on our site no longer exists, it returns a 404 error.

Here are the two most common reasons for broken (dead) backlinks to your website:

- You unwittingly delete or move a page that has existing backlinks;
- The linking site makes a mistake when linking to you (e.g., they may accidentally add an extra, unwanted character to the URL)

Want to see an example of the latter?

I was checking and fixing broken backlinks on this very blog, and found this link:

Looks fine, right?

Here’s what happened when I clicked it:

This seemed strange because I knew that the correct URL for Site Explorer is, in fact: <https://ahrefs.com/site-explorer>

So I decided to delve into the HTML:

`<a href="https://ahrefs.com/site-explorer)">https://ahrefs.com/site-explorer)</a>`

Do you see the problem?

The closing bracket is included *before* the closing </a> tag—this is wrong!

It’s an easy mistake (that was no fault of our own), but it still results in a 404.

Regardless of why they occur, broken backlinks are bad because they effectively waste “link juice.”

It just sort of evaporates—or perhaps, spills—when it hits the 404.

But I know what you might be thinking…

> *“… this link still goes to my site, so I guess it still contributes to the overall ‘authority’ of my website and helps other pages to rank, right!?”*

**NOPE.**

Google [has said](https://www.youtube.com/watch?v=gS4_JH-QqSg&feature=youtu.be&t=42m48s) that they don’t have any kind of authority score metric based on the overall backlink profile of a given domain. Therefore, these links (as they are) provide no benefit for you.

Sidenote.

It is true that broken links still contribute to your [Domain Rating](https://ahrefs.com/blog/domain-rating/) (DR). But remember, this is an [Ahrefs metric](/blog/ahrefs-seo-metrics/) that merely shows the strength of a target website’s total backlink profile (regarding its size and quality)—that’s all! By the way, you can check your [website’s Domain Rating here](https://ahrefs.com/website-authority-checker).

Here’s how to find and fix broken backlinks:

### Step #1: Finding ALL broken backlinks to your site

For this, I’ll use Ahrefs’ [Broken Link Checker](https://ahrefs.com/broken-link-checker).

Let me show you some examples using one of my favorite websites, *zenhabits.net*.

**[Site Explorer](https://ahrefs.com/site-explorer)** -> **yourdomain.com** -> **Pages** -> **Best by Links** -> **add a “404 not found” HTTP response filter**.

This report lets you quickly sort all the URLs that return a 404 code on your site by their URL Rating (UR), number of backlinks, or ref. domains count.

By default, these links are ordered by URL Rating (UR).

Personally, I prefer sorting by the number of linking domains (i.e., RDs)—this way, we’re starting with the URLs that have the most broken links pointing to them.

Do that for *zenhabits.com*, and you’ll see that one of the broken pages has **80** referring domains!

*(That’s a lot of wasted “link juice!”)*

Use the Broken Backlinks report to see all broken backlinks to all pages in a single view

If you’re already familiar with Ahrefs, you may be aware that we have a dedicated **Broken backlinks** report in Site Explorer.

This report is useful if you’d like to prioritize your broken backlinks by the Domain Rating (DR) or the URL Rating (UR) of the referring page.

But for the most part, I recommend sticking with the 404 filter in the **Best by Links** report—it’s much easier to prioritize that way. 🙂

### Step #2: Fixing ALL broken backlinks to your site

It goes without saying that you have no control over the links outside your website.

Or do you? 😉

Here are five fixes for broken backlinks:

1. **Reach out to the linking website and request a fix:** If the linking website made a mistake when linking to you (as was the case with the incorrectly formatted Site Explorer link above), it’s worth reaching out and letting them know about the issue. They may fix it.
2. **Redirect (301) the broken page to the new location:** Sometimes you may change the URL of a page and forget to redirect. This is an easy fix—just find the new page location and implement the redirect.
3. **Recreate and replace the content at the broken URL:** Find out what the broken page used to be and replace or recreate it.
4. **Redirect (301) the broken page to another relevant page on your website:** Find a similar piece of content on your site and redirect the broken page to that page. E.g., if you have a broken page entitled, “how to do broken link building;” it would make perfect sense to redirect this to a working page entitled, “the complete guide to broken link building.”
5. **Leave as a 404:** This is a totally viable option; you just need to make sure that you show a “hard” 404, not a “soft 404.” *(More on this in a moment!)*

But which solution should you use?

Well, I recommend going through these in the order that they’re listed.

By that, I mean that if option #1 (i.e., reaching out and requesting a fix) isn’t appropriate, move on to option #2, then #3, and so forth.

Make sense?

Let’s use this broken page from *zenhabits.com* example to illustrate this process:

Looking at the URL, it’s clear that there are no formatting issues (option #1). So there’s no need to reach out to anyone as the mistake is on our end, not theirs.

So let’s move on, and try to figure out what this page was before it was moved/removed.

In this instance, we can get a rough sense of what this page was about by looking at the URL. But it doesn’t give us the full picture.

So let’s use the [Wayback Machine](http://archive.org/web/) to see an archived copy of this page.

It looks like the article was about the “[beginner’s mind](https://en.wikipedia.org/wiki/Shoshin)” attitude to life.

Quick tip: what to do if the Wayback Machine fails

You’ll sometimes find that The Wayback Machine hasn’t archived the desired page.

No worries; Ahrefs to the rescue.

**Site Explorer** -> **enter the broken URL** -> **Backlinks**.

Now, look at the anchor text and surrounding text for each link.

This will almost always give some insight into what the page was about.

If you’re still unsure, try reading some of the articles that link to the broken page—these can often provide even more context.

Now that we know what the page was, the first step is to check whether the page was deleted or moved.

To do this, search in Google for: `site:yourdomain.com + "title of the page"`

If this search finds the broken page (at a different URL), then you can simply redirect the old, dead page to the new URL using a [301 redirect](https://ahrefs.com/blog/301-redirects/).

*(Check out* *[this guide](https://yoast.com/create-301-redirect-wordpress/)**from Yoast for more information on how to do that.)*

As announced by Gary Illyes from Google, 301 redirects do pass PageRank.

> 30x redirects don’t lose PageRank anymore.
>
> — Gary “鯨理” Illyes (@methode) [July 26, 2016](https://twitter.com/methode/status/757923179641839616?ref_src=twsrc%5Etfw)

But if no results are found (as is the case here), then chances are that page was deleted.

At this point, if you simply wanted to replace or recreate the page, you could—this would fix all broken links as the URL would no longer lead to a missing page.

However, nine times out of ten, you will have deleted the page for a reason, so you probably won’t want to do this.

Thus, the next step is to check to see if you have any similar content on the site, then redirect.

Here’s a Google search for that: `site:"yourdomain.com" + overall topic of the page`

Bingo!

If I managed this website, I could set up a 301 redirect from the old, broken page to point the other 80 referring domains to the live page.

You can do that for nearly every broken backlink on your site. Just keep two important things in mind:

1. **You should only redirect broken backlinks to relevant and similar content:** Broken backlinks naturally have specific anchor text and surrounding text. Make sure your redirects would not confuse, Google because [anchor text matters](https://twitter.com/JohnMu/status/864190235822899200)!
2. **Redirecting broken backlinks to the homepage might not be the best idea:** Even if we forget Google for a moment, think about your visitors. They expect to see some specific content when they click a link to your website; they don’t expect to see your homepage!

But what if there is nothing relevant to which you can redirect the broken page? What then?

To be honest, sometimes it’s perfectly fine to ignore the broken backlink; just make sure it shows an informative 404 page. And never use “[soft” 404s](https://support.google.com/webmasters/answer/181708?hl=en).

Here’s an extract from the [Google Webmaster Central Blog](https://webmasters.googleblog.com/2011/05/do-404s-hurt-my-site.html) that explains why:

> A soft 404 is when a web server returns a response code other than 404 (or 410) for a URL that doesn’t exist. A common example is when a site owner wants to return a pretty 404 page with helpful information for his users, and thinks that in order to serve content to users he has to return a 200 response code. Not so! You can return a 404 response code while serving whatever content you want. […] Keep in mind that just because a page says “404 Not Found,” doesn’t mean it’s actually returning a 404 HTTP response code—use the *[Fetch as Googlebot](https://support.google.com/webmasters/answer/6066468?hl=en)**feature in Webmaster Tools to double-check.*

Sidenote.

Google also classes the bulk redirection of any unknown or broken pages to your homepage as undesirable “soft” 404’s, so this is yet another reason to avoid doing this.

## Final thoughts

Broken links and backlinks not only waste “link equity,” but also contribute to a poor user experience. That’s why you should make every effort to find and fix them.

But this isn’t a one-time task; detecting and fixing broken links and backlinks must be an ongoing process, as a part of your sites’ regular [SEO Audits](https://ahrefs.com/site-audit). Here’s [an SEO audit template](https://ahrefs.com/blog/seo-audit-template/) you can use to do that.

*(Don’t forget that you can schedule automated audits in Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) tool, which makes it easy to keep on top of broken links and backlinks!)*

What’s your experience with fixing broken links and backlinks?

Let me know in the comments section below. 🙂
