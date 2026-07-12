---
title: "301 vs. 302 Redirects for SEO: Which Should You Use?"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "301-vs-302-redirects"
url: "https://ahrefs.com/blog/301-vs-302-redirects/"
canonical: "https://ahrefs.com/blog/301-vs-302-redirects/"
author: "Joshua Hardwick"
published: "2020-09-08T06:00:00+00:00"
updated: "2023-10-04T14:13:59+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T11:09:18+00:00"
status_code: 200
html_hash: "cbce9eced387ce19af4e3893c8111a763569fc433d81f8c44514c67c642e56c1"
clean_word_count: 1920
clean_char_count: 11005
---
# 301 vs. 302 Redirects for SEO: Which Should You Use?

The difference between 301 and 302 redirects is that 301 redirects are for permanent moves and 302 redirects are for temporary moves.

You need to use the right one to avoid SEO issues.

Let’s take a closer look at how these redirects work and when and how to use them.

## What is a 301 redirect?

A 301 redirect is a permanent redirect. It takes visitors to the new URL and signals a permanent move to search engines.

You should use a 301 redirect when you:

- Permanently change the URL of a webpage.
- Permanently migrate to a new domain.
- Switch from [HTTP to HTTPS](https://ahrefs.com/blog/what-is-https/).
- Want to fix non-www/www [duplicate content](https://ahrefs.com/blog/duplicate-content/) issues.
- Permanently merge two or more pages or websites.
- Permanently change the URL structure of your website.

## What is a 302 redirect?

A 302 redirect is a temporary redirect. It takes visitors to the new URL and signals a temporary move to search engines.

You should use a 302 redirect when you:

- Want to redirect users to the right version of the site for them (based on location/language).
- Want to A/B split-test the functionality or design of a webpage.
- Want to get feedback about a new page without affecting the old page’s rankings.
- Run a promotion and want to redirect visitors to a sales page temporarily.

In other words, whenever you plan to bring back the old page after a short period.

## How do 301 and 302 redirects impact SEO?

Redirects impact which page ranks in the search results and how well it ranks. This is because if you redirect one URL to another, Google only indexes and shows one of them in the search results. It also usually combines link signals from both URLs at the one it indexes.

There’s some nuance to how this works. Let’s take a closer look.

### How 301 redirects impact SEO

301 redirects tell Google that a page has moved forever, so it almost always indexes and shows the new URL in the search results. After all, there’s no point keeping the old URL indexed if it’s never coming back.

Sidenote.

Redirects are a [canonicalization](https://ahrefs.com/blog/canonicalization/) signal, which is why they’re not 100% effective. Google may, in very rare cases, treat a 301 redirect as a 302 redirect.

Link signals also usually consolidate “forward” to the new URL.

For example, say you redirect a page from site1.com/x to site2.com/x without changing the content. Link signals will consolidate at site2.com/x. In other words, if site1.com/x has 10 backlinks, site2.com/x feels the benefit of them as if they point directly to it.

It’s only if a redirect is irrelevant that this doesn’t happen because [Google treats irrelevant redirects as soft 404s](https://www.youtube.com/watch?v=nIDZmac_rMI&feature=youtu.be&t=76&ab_channel=GoogleWebmasters).

For example, say you redirect a blog post to your homepage. Google may not consolidate link signals because the two pages are entirely different.

Recommendation

If you’re curious how Google is treating a 301 redirect, check whether links are consolidating to the new URL in Google Search Console.

Here’s how:

1. Open Google Search Console
2. Go to *Links > External Links > Top linked pages*
3. Find the “new” URL in the report and click it (use the “Target page” filter to help)
4. Filter the links by “Site” and paste in referring domains to the old page one by one (you can find these in the **Referring Domains** report in Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer))

If you get no matches for several referring domains, Google is likely treating the redirect as a soft 404 and not counting the old page’s backlinks toward the new URL.

If there is a match, click on the site to see the actual links. If you see the old URL in the “Target URL” column, Google is consolidating links at the new URL.

### How 302 redirects impact SEO

302 redirects tell Google that a page has moved temporarily. So usually, it keeps the old URL indexed and shows it in the search results. After all, there’s no point in removing the old URL and indexing the new URL if the old URL will be back soon.

Link signals also usually consolidate “backward” to the old URL.

Only if Google thinks you used a 302 redirect by mistake for a permanent move does this not happen. In that case, [it treats the redirect as a 301](https://www.youtube.com/watch?time_continue=1398&v=opUfIzuzJSw&feature=emb_title&ab_channel=GoogleWebmasters%5C). This means it indexes the new URL instead and consolidates link signals there.

Nobody knows how long a 302 redirect has to exist before Google starts treating it as a 301 redirect. Usually, it’s a few weeks to a few months, but it can be days, weeks, or months.

In some circumstances, Google even appears to treat 302s as 301s from the get-go.

For example, our [Patrick Stox](https://ahrefs.com/blog/author/patrick-stox/) recently ran an experiment where he redirected (302) one established site to another. When Google saw the redirect, it dropped the old domain from the search results in favor of the “new” domain.

If you’re not sure how Google is treating one of your 302 redirects, paste the redirected URL into Search Console’s [URL Inspection tool](https://support.google.com/webmasters/answer/9012289?hl=en). If it shows the “URL is not on Google” warning, Google must be treating the redirect as permanent (301). If it is on Google, then Google’s treating it as temporary (302).

Just make sure to check the last crawl date when doing this. If this date comes after you added the redirect, request reindexing and come back later.

Sidenote.

Google seems quicker to treat 302 redirects as permanent when redirecting to an established page or site. That’s likely because the new page or website has been around a while, so there’s a good chance you meant to redirect the URL permanently.

## Do you need to change accidental 302 redirects to 301s?

It depends on how Google currently treats those redirects.

If it’s figured things out and is already treating the accidental 302s as permanent moves, changing them to 301s may not impact anything. If it hasn’t figured things out, swapping the redirects from 302s to 301s is likely the best course of action.

You can use the URL Inspection tool in GSC to check how Google treats individual URLs. Unfortunately, that’s pretty time-consuming if you have a lot of redirects. A faster method is to look for 302 redirects that get organic traffic. After all, that’s a telltale sign that Google still treats the redirect as temporary.

You can do this by crawling your site with Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) and checking the **Redirects** report for the “302 redirects” warning.

If it’s there, click to view the affected URLs and sort the report by “Organic traffic” from high to low.

As this data is an estimate, it’s worth double-checking redirected URLs with traffic in GSC’s URL Inspection tool.

If the user-declared and Google-declared canonicals match, Google treats the 302 redirect as permanent.

If they don’t, the redirected page is likely getting organic traffic because it’s still indexed, and Google treats it as temporary. That isn’t desirable if you used a 302 redirect accidentally for a permanent move. Luckily, swapping the 302 redirect to a 301 should fix the issue.

## How to add redirects

You can create 301 and 302 redirects in several ways, but editing a website’s .htaccess file is the most common method. You’ll find this file in your website’s root directory.

Sidenote.

If you don’t see this file in your site’s root directory, either your server isn’t running on Apache, you don’t have this file, or it’s hidden. You can check the kind of server you’re running with [this tool](http://browserspy.dk/webserver.php). If it’s Apache, the solution is to create a .htaccess file and upload it to your root server. If you’re running Nginx, read [this](https://www.bjornjohansen.com/nginx-redirect). If you’re running Windows/IIS, read [this](https://www.bowlerhat.co.uk/301-redirects-for-seo-from-windows-server-iis).

If you’re using WordPress, a less daunting option is to use a [free SEO plugin](https://ahrefs.com/blog/best-seo-plugins-for-wordpress/) to create redirects. [RankMath](https://wordpress.org/plugins/seo-by-rank-math/) has this functionality built in, but [this plugin](https://en-gb.wordpress.org/plugins/redirection/) will also do the job.

### How to create a 301 redirect

If you want to create a 301 redirect from one URL to another, add this to your .htaccess file:

```
Redirect 301 /old-page.html /new-page.html
```

You can also do this using RankMath or the Redirections plugin. Just choose the type of redirect you want, then add your source and destination URLs.

If you’re looking to redirect the entire website, add this to your .htaccess file:

```
RewriteEngine on
RewriteCond %{HTTP_HOST} ^oldsite.com [NC,OR]
RewriteCond %{HTTP_HOST} ^www.oldsite.com [NC]
RewriteRule ^(.*)$ https://newsite.com/$1 [L,R=301,NC]
```

Just know that you’ll need to keep your old hosting active to redirect your site with .htaccess, which can be expensive. So it’s usually better to redirect through DNS. Most registrars allow you to select either a 301 or 302 redirect for this. If you’re using Google Domains, just hit *Website > Add a forwarding address* and then enter the new domain and choose “Permanent redirect.”

You can learn how to create 301 redirects for more situations (e.g., non-www to www, HTTP to HTTPS) in [our full guide to 301 redirects](https://ahrefs.com/blog/301-redirects/).

### How to create a 302 redirect

If you want to create a 302 redirect from one URL to another, add this to your .htaccess file:

```
Redirect 302 /old-page.html /new-page.html
```

You can also do this with RankMath or the Redirections plugin in WordPress:

If you’re looking to redirect the entire website, use this code:

```
RewriteEngine on
RewriteCond %{HTTP_HOST} ^oldsite.com [NC,OR]
RewriteCond %{HTTP_HOST} ^www.oldsite.com [NC]
RewriteRule ^(.*)$ https://newsite.com/$1 [L,R=302,NC]
```

Just know that you probably won’t want to use a 302 to redirect one site to another. Most domain changes are permanent, so you’ll want to use a 301. It’s the same story for redirects from HTTP to HTTPS or non-www to www (and vice versa).

## Final thoughts

Redirects aren’t that complicated. If you’re moving content to a new location permanently, use a 301 redirect. If you’re moving it temporarily, use a 302 redirect.

That said, it’s reassuring to know that if you use the wrong type of redirect, Google will likely figure out what you meant sooner or later. Does this always happen? Of course not. Google isn’t always smart enough to realize what you meant every time, so it’s [best practice](https://ahrefs.com/blog/seo-best-practices/) to use the correct type of redirect where possible.

Got questions? Ping me [on Twitter](https://twitter.com/joshuachardwick?lang=en).
