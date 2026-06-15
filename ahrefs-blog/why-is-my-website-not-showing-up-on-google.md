---
title: "8 Fixes For When Your Website Isn't Showing Up In Google"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "why-is-my-website-not-showing-up-on-google"
url: "https://ahrefs.com/blog/why-is-my-website-not-showing-up-on-google/"
canonical: "https://ahrefs.com/blog/why-is-my-website-not-showing-up-on-google/"
author: "Joshua Hardwick"
published: "2019-10-04T01:10:19+00:00"
updated: "2024-11-04T18:29:28+00:00"
categories:
  - "General SEO"
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T12:20:05+00:00"
status_code: 200
html_hash: "34ce2ecc341d4b8168763404d001713e9175db98c04e86c2daf866f2bd656fce"
clean_word_count: 1886
clean_char_count: 10599
---
# 8 Fixes For When Your Website Isn’t Showing Up In Google

Does it feel like you’ve done everything right, yet your website is still nowhere to be seen in Google’s search results?

There are a few reasons that might be.

Let’s run through a few things to check for and how to fix them.

## 1. Check that Google has indexed your site

If your website isn’t in Google’s index, it can’t possibly show up in Google search.

To check that Google has indexed at least some pages on your website, run a search for site:yourwebsite.com

![Google site: search](https://ahrefs.com/blog/wp-content/uploads/2024/11/google-site-search.png)

Any pages that show up are capable of showing in Google’s search results.

If you want to check whether a particular page is indexed, run the same search for that page. Like: site:yourwebsite.com/a-page-you-want-to-show-up-in-google/

You can also check indexing status in Google Search Console. Just plug the URL into the URL Inspection tool. If it says “URL is on Google” then it’s indexed. If not, hit the “Request indexing” button.

## 2. Submit your sitemap to Google

Even if some of your pages show in a Google site: search, there’s a chance Google may not have all of your pages indexed. This can happen because they don’t know they exist due to a lack of [internal links](https://ahrefs.com/blog/internal-links-for-seo/) (more on that later!).

But even if an important page has no internal links, it should still be in your sitemap. Submitting this to Google tells them which pages are important on your site and where to find them.

To do this, go to: *Search Console > Sitemaps > Enter sitemap URL > Submit*

If you don’t know where your sitemap is, go to yourwebsite.com/robots.txt as this often lists the sitemap URL.

If there’s still nothing there, you might not have one. Read [our guide to creating a sitemap](https://ahrefs.com/blog/how-to-create-a-sitemap/) to fix that.

## 3. Check that you’re not blocking Google from indexing your site

If you tell Google not to show certain pages in the search results, then it won’t.

You do that with a “noindex” meta tag, which is a piece of HTML code that looks like this:

```
<meta name="robots" content="noindex"/>
```

Pages with that code won’t be indexed, even if you created a sitemap and submitted it in Google Search Console.

You probably don’t recall ever adding that code to any of your pages, but that doesn’t mean it isn’t there.

For example, WordPress adds it to every page if you check the wrong box when setting up your site.

To check for noindexed pages, sign up for a free [Ahrefs Webmaster Tools (AWT)](https://ahrefs.com/webmaster-tools) account and crawl your website with [Site Audit](https://ahrefs.com/site-audit). Look out for any issues related to indexed pages, but especially this one warning about noindexed pages in sitemap:

If you see this then you almost certainly have a problem. Check the issue details in Site Audit for instructions on how to fix.

## 4. Check that you’re not blocking Google from crawling

Google can’t crawl URLs blocked in your [robots.txt](https://ahrefs.com/blog/robots-txt/) file, which usually results in them not showing up in search results.

If you’ve submitted your sitemap via Google Search Console, it should alert you about issues related to this. Go to the “Pages” report and look for “Submitted URL blocked by robots.txt” errors.

If you see this error, then you have one of two problems:

1. **You’re blocking crawling for pages you want indexed.** Remove or edit the affecting rule in your robots.txt file.
2. **You have pages you don’t want indexed in your sitemap.** Remove them from your sitemap.

Note

Robots.txt files can be complicated, and they’re easy to mess up. If you feel that yours may be preventing pages from showing up on Google, and you don’t know much about this file, hire an expert to fix it.

## 5. Check that all important pages are internally linked

Internal links are links from one page on your site to another. If pages don’t have any internal links, the only way Google can find them is through your sitemap (or via backlinks). But often, Google still won’t index them as pages without internal links (also known as [orphan pages](https://ahrefs.com/blog/orphan-pages/)) are rarely seen as important.

Think about it this way: if there are no internal links to a page, then visitors on your site can’t find it. If visitors on your site can’t find it, why would Google bother indexing it? You’re literally telling Google it isn’t useful.

Finding pages without internal links can be technically challenging, but you can find most of them using Ahrefs’ [Site Audit](https://ahrefs.com/site-audit). Just select sitemaps as backlinks as URL sources when setting up your project:

If any pages with backlinks or in your sitemap don’t have internal links, we’ll tell you with the “Orphan page” error:

Here’s how to deal with any orphan pages you find:

Further reading

- [How to Find and Fix Orphan Pages (The Right Way)](https://ahrefs.com/blog/orphan-pages/)

## 6. Check that you have enough backlinks

Google indexes plenty of sites that have few or no backlinks, but these rarely show up in the search results for keywords anyone actually searches for. Our data proves it; there’s a clear correlation between a page’s backlinks and its search traffic:

But what’s “enough backlinks”?

Unfortunately there’s no definitive answer to that question. However, if your site has way fewer backlinks than your competitors, you’re probably going to struggle to show up in Google for anything important.

To check how you compare, use [our free website authority checker](https://ahrefs.com/website-authority-checker). This will tell you how authoritative any domain is on a scale from 0-100, as well as how many websites are linking to it.

If these numbers for your own site are much lower than your competitors, your site will probably show up in Google for more keywords if you build some more backlinks.

That said, you ideally want to build backlinks to the pages you most want to show up in Google.

For a rough idea of how many you might need, plug your target keyword into Ahrefs’ free SERP checker and look at the number of linking domains to the top three results.

Then compare those numbers to your page with [our free backlink checker](https://ahrefs.com/backlink-checker):

If the numbers are drastically different then you probably need to build more backlinks before your page will show up in Google for your target keyword (or other terms people are actually searching for).

Check out the resources below to learn how to do that.

Further reading

- [Link Building for SEO: The Beginner’s Guide](https://ahrefs.com/seo/link-building)
- [How To Get Backlinks: Add, Ask, Earn, Buy](https://ahrefs.com/blog/how-to-get-backlinks/)
- [12 Link Builders Share Strategies That Work in 2024](https://ahrefs.com/blog/link-building-strategies/)

Note

Not all backlinks are created equal, so it’s not just about raw numbers. It’s perfectly possible to show up higher in Google when you have fewer backlinks than competitors when your backlinks are higher quality.

In Ahrefs, we have a “Best links” filter in Site Explorer that will show you, well… the target’s best links only. This is a good way to see how many high quality links a competitor has and how many good links you might really need to compete.

For example, our list of link building strategies has links from 421 websites:

But if we filter for “best links” only, this number drops to just 50:

That’s a big difference, and it probably means you’d only need to build around 50 good links to compete with this page and have a chance at showing up in Google for the same keywords.

## 7. Check that your pages match “search intent”

Search intent is what the searcher is looking for when they Google the keyword you want to rank for. If your pages don’t align with this, Google isn’t going to rank it. This is because Google’s entire job is to give searchers what they want.

How do you figure out search intent? Look for commonalities between the top-ranking results.

For example, the top-ranking pages for “air fryers” are all blog posts listing top picks, not pages from stores selling air fryers.

If you want to stand the best chance of ranking in Google, this is probably what you need to create too.

That said, manual analysis of search intent isn’t always so straightforward. If that’s the case for your keyword, try plugging your keyword into Ahrefs’ Keywords Explorer and hitting the “Identify intents” button on the SERP. This uses AI to analyse the intent of the top-ranking pages and tells you what it is in plain English.

You can also use our AI Content Helper to help you optimize your page for a particular intent. Just plug in its URL along with your target keyword, pick the intent you want to optimize for, and we’ll give you subtopic suggestions to improve your page:

## 8. Check that you don’t have a Google penalty

Google has two types of penalties: manual and algorithmic.

You’ll know if you have a manual penalty because Google literally tells you in Search Console. Just go to *Security & Manual Actions > Manual Actions* to check:

If you see an issue here, consult an SEO expert because there’s a big issue and your site is unlikely to show up in Google anytime soon.

As for algorithmic penalties, these are harder to spot because Google doesn’t tell you about them in the same way. The best way to check for them is to use a tool like Ahrefs’ Site Explorer which shows when Google Updates occurred on a graph of your estimated organic traffic over time. If one of these updates coincides with a big drop in traffic, there’s a chance you might have a penalty.

For example, this site’s organic traffic fell off a cliff after Google’s March 2024 Core Update:

If things look similar for your site, I recommend consulting the advice of an [SEO expert](https://ahrefs.com/blog/seo-expert/).

## Still not showing up in Google?

It’s possible that there could be other technical SEO issues impacting your site. It may also simply be that you’re in a competitive industry and outranking behemoth brands is a difficult task, so you might just need to keep plugging away at SEO before you show up for keywords you care about.

If you want to learn more about SEO, check out [our beginner’s guide to SEO](https://ahrefs.com/seo).

Otherwise, consider hiring an [SEO consultant](https://ahrefs.com/blog/seo-consultant/) to help you.

Got questions? Ping me on [LinkedIn](https://uk.linkedin.com/in/joshuahardwick28).
