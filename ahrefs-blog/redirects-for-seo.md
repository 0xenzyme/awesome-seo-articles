---
title: "11 Types Of Redirects & Their SEO Impact"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "redirects-for-seo"
url: "https://ahrefs.com/blog/redirects-for-seo/"
canonical: "https://ahrefs.com/blog/redirects-for-seo/"
author: "Patrick Stox"
published: "2024-05-13T13:29:04+00:00"
updated: "2024-06-27T04:44:52+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T11:58:50+00:00"
status_code: 200
html_hash: "f8040f58edb7dbc07f36f4e9c5d20590375fbcbb5ad95a4e7f2715b9381c9b00"
clean_word_count: 4845
clean_char_count: 28715
---
# 11 Types Of Redirects & Their SEO Impact

A redirect is a way to send people and bots to a new URL when they request the old URL, but the page has changed locations.

When you move to a new address in the US, you set up mail forwarding with the United States Postal Service (USPS). If someone sends mail to your old address, USPS will look at their mail forwarding rules and realize you no longer live at the old location. They’ll take the mail and deliver it to your new location instead of the old one.

That’s also how redirects work. A user or bot requests the old location, and they get forwarded to the new location. For example, we moved blog.ahrefs.com to [ahrefs.com/blog](https://ahrefs.com/blog) a while back. If you try to access blog.ahrefs.com, you will be forwarded to the new URL instead. Watch what happens.

![Redirect of blog.ahrefs.com to ahrefs.com/blog](https://ahrefs.com/blog/wp-content/uploads/2024/05/redirect-of-blog-ahrefs-com-to-ahrefs-com-blog.gif)

## When to use redirects

You’ll want to use redirects to:

- Move a website or page
- Want to consolidate duplicate pages
- Merge websites
- Send users to a new page after you delete
- Change your URL structure or clean up your URLs

## Types of redirects and their SEO impact

Redirects help combine signals between pages and help search engines determine which page they should show to users. This is a process called [canonicalization](https://ahrefs.com/blog/canonicalization/) and Google uses it to help keep duplicate pages out of its index. In other words, redirects are important for SEO.

There are a lot of myths and misunderstandings surrounding redirects in the SEO community that I hope I can clear up with this article.

Redirects can either be permanent or temporary, depending on whether you plan to leave the redirect in place or not. This also impacts which page will be indexed and shown in search engines which I’ll cover more in the next section.

Redirects can also be server-side, meaning they happen on a server somewhere, or client-side, meaning they happen inside the user’s browser.

Here are a few tables you can reference that categorize the different types of redirects. I’ll talk more about each of these in the next section.

| Permanent Redirects | | |
| --- | --- | --- |
| Server-Side | Client-Side | No Actual Redirect |
| HTTP 301 | Meta refresh (=0 seconds) | Crypto redirect |
| HTTP 308 | HTTP refresh (=0 seconds) |  |
|  | JavaScript redirects |  |

As far as which method you should choose to implement permanent redirects, my preferred order would be: 308 / 301 > Meta refresh 0 / HTTP refresh 0 > JavaScript > Crypto

| Temporary Redirects |  |
| --- | --- |
| Server-Side | Client-Side |
| HTTP 302 | Meta refresh (>0 seconds) |
| HTTP 303 | HTTP refresh (>0 seconds) |
| HTTP 307 |  |

As far as which method you should choose to implement temporary redirects, my preferred order would be: 307 / 302 / 303 > Meta refresh 0 / HTTP refresh 0

Server-side redirects don’t necessarily have to happen on your hosting server. It could be “someone else’s server” like a CDN or your domain name provider. Client-side redirects can also be added in multiple ways, but they will always fire in the user’s browser.

Here are some of the places you might find these redirects:

| Where you might find redirects | |
| --- | --- |
| Server-Side | Client-Side |
| Server-level | HTML |
| DNS-level | HTTP Header Response |
| CDN-level | CDN-level (in specific cases) |

Let’s look at these in more detail.

## Permanent redirects

A permanent redirect indicates that a resource has permanently moved to a new location.

You should use a permanent redirect when you:

- Permanently change the URL of a webpage or other resource.
- Permanently [migrate](https://ahrefs.com/blog/website-migration/) to a new domain.
- Switch from [HTTP to HTTPS](https://ahrefs.com/blog/what-is-https/).
- Want to fix non-www/www [duplicate content](https://ahrefs.com/blog/duplicate-content/) issues.
- Permanently [merge](https://ahrefs.com/blog/seo-for-mergers-acquisitions/) two or more pages or websites.
- Permanently change the URL structure of your website.

Permanent redirects are a strong hint for canonicalization that signals from a page, like links, should consolidate forward to the page the new URL. It is usually the new page that will have all the signals and be shown in search engines.

Say you redirect a page from site1.com/x to site2.com/x without changing the content. Link signals will consolidate at site2.com/x. In other words, if site1.com/x has 10 backlinks, site2.com/x feels the benefit of them as if they point directly to it.

It’s only if a redirect is irrelevant that this doesn’t happen because [Google treats irrelevant redirects as soft 404s](https://www.youtube.com/watch?v=nIDZmac_rMI&feature=youtu.be&t=76&ab_channel=GoogleWebmasters).

For example, say you redirect a blog post to your homepage. Google may not consolidate link signals because the two pages are entirely different.

Sidenote.

Google may, in very rare cases, still treat the original URL as the canonical version that gets shown in the index. Lots of SEOs know that the opposite can happen, that temporary redirects can be treated as permanent redirects, but permanent redirects can occasionally be treated as temporary redirects as well.

Want to check how google is treating a redirect?

Here’s how:

1. Open Google Search Console
2. Go to Links > External Links > Top linked pages
3. Find the “new” URL in the report and click it (use the “Target page” filter to help)
4. Filter the links by “Site” and paste in referring domains to the old page one by one (you can find these in the Referring Domains report in Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer))

If you get no matches for several referring domains, Google is likely treating the redirect as a soft 404 and not counting the old page’s backlinks toward the new URL.

If there is a match, click on the site to see the actual links. If you see the old URL in the “Target URL” column, Google is consolidating links at the new URL.

Let’s look at some of the types of permanent redirects.

#### HTTP 301

A [301 redirect](https://ahrefs.com/blog/301-redirects/) is a server-side redirect that forwards bots and users to the new URL and tells search engines that the resource has permanently moved.

#### HTTP 308

A 308 redirect is the same as a 301 redirect, except it retains the HTTP method of the original request, GET or POST, when performing the redirect. For SEO purposes, they’re the same, but if you have data being sent through forms, you don’t want to be switching between GET and POST.

#### JavaScript redirects

A JavaScript redirect uses JavaScript to instruct the browser to redirect the user or bot to a different URL.

Because a page needs to be rendered for this type of redirect to fire, it’s client-side and not preferred. Google renders every page they’re going to index, but there can be issues in this process causing rendering to fail. Other redirect types are better supported and more reliable.

Here’s an example of how the redirect might look in the HTML:

```
<script>
// Redirect to a new URL
window.location.href = "https://example.com/new-page";
</script>
```

JavaScript redirects could potentially be in the config file as well. In the Next.js config, there’s a redirect function you can use to set redirects. In other systems, you may find them in the router.

#### Meta refresh (=0 seconds)

A meta refresh redirect tells the browser to redirect the user after a set number of seconds. It happens in the browser and is client-side.

Meta refresh redirects need to be in the <head> section of the HTML. This is how they look:

```
<meta http-equiv="refresh" content="0; url=https://example.com/new-page">
```

#### HTTP refresh (=0 seconds)

An HTTP refresh is like a meta refresh but it occurs in the HTTP header response. It can be implemented server side, but it actually fires on the client side.

Here’s how it looks:

```
Refresh: 0; url=https://example.com/new-page
```

#### Crypto redirect

A redirect without actually redirecting? It sounds strange, but Google treats this as a permanent redirect. That means they should also pass all signals forward to the new URL.

A crypto redirect is a special case where you have a message about moving to a new domain, but no actual redirect occurs. It looks like this:

```
<a href="https://new-domain.com/" >We moved! Check out our new site!</a>
```

I would try to implement a different redirect method as not every bot or search engine would support crypto redirects.

### Temporary redirects

A temporary redirect indicates that a resource has temporarily moved to a new location.

You should use temporary redirects when you:

- Want to redirect users to the right version of the site for them (based on location/language).
- Want to A/B split-test the functionality or design of a webpage.
- Run a promotion and want to redirect visitors to a sales page temporarily.

Temporary redirects are a weak hint for canonicalization that signals from a page, like links, should consolidate forward to the new page. Because it is a weak signal, most of the time the signals actually consolidate to the original page that was redirected.

However, at some point, enough signals may build that a temporary redirect does consolidate forward. For a while, you may see the original URL indexed in Google and signals consolidate there, but if this swap happens then you will see the new URL in Google and signals will consolidate there instead.

There’s no set amount of time that a temporary redirect needs to exist before Google starts treating it as a permanent redirect. Usually, it’s a few weeks to a few months, but it can be days, weeks, or months.

The swap may never happen, like in the case of 302s being used to redirect users to the most relevant version of their homepage on international websites. This setup has been used by many sites for nearly a decade and they still have the original URLs indexed.

In some circumstances, Google even appears to treat temporary redirects as permanent redirects from the get-go.

For example, I ran an experiment where I redirected (302) one established site to another. When Google saw the redirect, it dropped the old domain from the search results in favor of the “new” domain.

If you’re not sure how Google is treating one of your temporary redirects, paste the redirected URL into Search Console’s [URL Inspection tool](https://support.google.com/webmasters/answer/9012289?hl=en). If it shows the “URL is not on Google” warning, Google must be treating the redirect as permanent. If it is on Google, then Google’s treating it as temporary.

Just make sure to check the last crawl date when doing this. If this date comes after you added the redirect, request reindexing and come back later.

Sidenote.

Google seems quicker to treat temporary redirects as permanent redirects when redirecting to an established page or site. That’s likely because the new page or website has been around a while, so there’s a good chance you meant to redirect the URL permanently.

Let’s look at some of the types of temporary redirects.

#### HTTP 302

A 302 redirect forwards users to the new URL and tells search engines that the resource has temporarily moved.

#### HTTP 307

A 307 redirect is the same as a 302 redirect, except it retains the HTTP method (POST, GET) of the original request when performing the redirect. For SEO, it’s the same, but if you have data being sent through forms that redirect, then you don’t want to be swapping between GET and POST.

It’s worth calling out that when troubleshooting redirect issues, you may see a different version of a 307 which is a cached redirect that happens in the browser. This is related to HSTS and tells the browser to swap to a secure connection (HTTPS) when an insecure resource is requested.

When web servers require clients to only use HTTPS connections (HSTS policy), Google won’t see the 307 because it’s cached in the browser. The initial hit (without cache) will have a server response code that’s likely a 301 or a 302. But your browser will show you a 307 for subsequent requests which makes it more difficult to troubleshoot. You will need to use a fresh Incognito session to see the returned [status code](https://ahrefs.com/blog/http-status-codes/).

#### HTTP 303

A 303 redirect forwards the user to a resource similar to the one requested and is a temporary form of redirect. It’s typically used for things like preventing form resubmissions when a user hits the “back” button in their browser. You won’t typically see 303 redirects used for SEO purposes, but if you do then it will be treated just like a 302/307.

#### Meta refresh (>0 seconds)

A meta refresh is treated as a permanent redirect when it is equal to 0 seconds and as a temporary redirect when it is greater than 0 seconds.

A meta refresh redirect tells the browser to redirect the user after a set number of seconds. It happens in the browser and is client-side.

Meta refresh redirects need to be in the <head> section of the HTML. This is how they look:

```
<meta http-equiv="refresh" content="5; url=https://example.com/new-page">
```

#### HTTP refresh (>0 seconds)

An HTTP refresh is treated as a permanent redirect when it is equal to 0 seconds and as a temporary redirect when it is greater than 0 seconds.

An HTTP refresh is like a meta refresh but it occurs in the HTTP header response. It can be implemented server side, but it actually fires on the client-side.

Here’s how it looks:

```
Refresh: 5; url=https://example.com/new-page
```

### Server-side redirects

A server-side redirect is one where the server decides where to redirect the user or search engine when a page is requested. They will usually have a corresponding status code of 301, 302, 303, 307, or 308.

Server-side redirects are the preferred method of doing redirects for SEO.

#### Server-level

These are redirects that happen on your server. How you implement them will vary depending on your website host and which server environment or script language is used for the backend. Any common type of server should be well documented. The most common are Nginx, Apache, Cloudflare Server, LiteSpeed, Microsoft-IIS, and Node.js.

If you are entering redirects in a plugin or a custom redirect solution on a CMS like WordPress, Shopify, Wix, Squarespace, Joomla, or Drupal, then the redirects are being added at the server level.

Most WordPress installs will be running Apache and the plugins used for redirecting will actually be editing a website’s .htaccess file. You’ll find this file in your website’s root directory.

Sidenote.

If you don’t see this file in your site’s root directory, either your server isn’t running on Apache, you don’t have this file, or it’s hidden. You can check the kind of server you’re running with [this tool](http://browserspy.dk/webserver.php). If it’s Apache, the solution is to create a .htaccess file and upload it to your root server. If you’re running Nginx, read [this](https://www.bjornjohansen.com/nginx-redirect). If you’re running Windows/IIS, read [this](https://www.bowlerhat.co.uk/301-redirects-for-seo-from-windows-server-iis).

To create a redirect in .htaccess from one page to another you would add:

```
Redirect 308 "/old" "https://example.com/new"
```

You can also redirect with different languages such as PHP. Here’s what that would look like:

```
header('HTTP/1.1 308 Moved Permanently');
header('Location: https://www.example.com/newurl');
exit();
```

We have a lot more examples in our post on [301 redirects](https://ahrefs.com/blog/301-redirects/) including redirecting a domain, www to non-www, non-www to www, and HTTP to HTTPS, Redirects could also be located in the server config file.

In many common systems, you can just put in a redirect and it will fire automatically. However, some systems work as error catchers. You can put in a redirect and it won’t fire until you delete the old page. This adds an extra step to the process, but is less prone to errors.

### DNS-level

Your name servers are usually managed by your domain registrar or possibly your CDN. Each provider differs a bit, but they usually have documentation that you can find.

Redirects at this level are often used for [website migrations](https://ahrefs.com/blog/website-migration/). Some hosts may let you specify the status code for a redirect such as a 301 or 302.

Some providers are even allowing HTTPS versions of pages to be redirected. Technically, HTTPS doesn’t exist at this level and this wasn’t an option in the past, but some providers have figured out a way to make this work.

### CDN-level

Many CDNs have multiple options for implementing redirects. For example, on Cloudflare you could do single or bulk redirects, there are specific redirect rules, you could write a page rule with a redirect, you can use workers and key-value pairs to implement redirects, or you could use workers to modify the headers and add a redirect.

I typically prefer to have redirects on the edge (CDN-level) over having them on the server. For others, I always recommend going with what is easiest for you to implement. For many people that is server-level redirects.

### Client-side redirects

A client-side redirect is fired by the user’s browser. A user may see a page temporarily before the redirect happens.

You generally shouldn’t do redirects on the client-side, unless that is your only option.

#### HTML

We’ve already talked about meta refresh redirects and JavaScript redirects. These are fired on the client side.

Meta refresh redirects need to be in the <head> section of the HTML. This is how they look:

```
<meta http-equiv="refresh" content="5; url=https://example.com/new-page">
```

Here’s how a JavaScript redirect might look in the HTML:

```
<script>
    // Redirect to a new URL
    window.location.href = "https://example.com/new-page";
</script>
```

#### HTTP Header Response

An HTTP refresh is like a meta refresh but it occurs in the HTTP header response. It can be implemented server side, but it actually fires on the client-side.

Here’s how it looks:

```
Refresh: 5; url=https://example.com/new-page
```

#### CDN-level (in specific cases)

I talked earlier about Cloudflare workers. These let you edit things on the edge before being served to users. You could actually re-write some of the HTML to add in a client-side redirect like a meta refresh, but this would be uncommon because there are better ways to do it.

## Best practices for redirects

Here are a few items related to redirects that you’ll want to check.

### Redirect HTTP to HTTPS

Everyone should be using [HTTPS](https://ahrefs.com/blog/what-is-https/).

There are a couple of ways to check that your site is properly redirecting from HTTP to HTTPS. The first is to install and activate Ahrefs’ [SEO Toolbar](https://ahrefs.com/seo-toolbar), then try to navigate to the HTTP version of your homepage. It should redirect.

You typically want to see a 301 or 308 redirect here, as this redirect should be permanent.

However, you may see a 307 redirect if your site uses HSTS like we do for Ahrefs.

This type of 307 fires in the browser and you still need to check the server response to make sure it’s a 301 or 308.

So here’s another method:

- Go to Ahrefs’ [Site Audit](https://ahrefs.com/site-audit)
- Click + New Project
- Click Add manually
- Change the Scope to HTTP
- Enter your domain

You should see the “Not crawlable” error for both the www and non-www versions of your homepage, along with the “301 moved permanently” notification.

### Use HSTS (to create 307 redirects)

Implementing HSTS (HTTP Strict Transport Security) on your server stops people from accessing non-secure (HTTP) content on your site. It does this by telling browsers that your server only accepts secure connections and that the browser should 307 redirect to the HTTPS version of any HTTP resource they’re asked to access.

Keep in mind that this happens within the browser. Bots won’t see this particular version of a 307.

Further reading

- [Strict-Transport-Security - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)

After implementing HSTS, consider submitting your site to the [HSTS preload list](https://hstspreload.org/). This enables HSTS for everyone trying to visit your website—even if they haven’t visited it before.

### Redirect relevant old content

Sites, and the web in general, are always changing. We ran a study that found that [~two-thirds of links to pages on the web disappeared](https://ahrefs.com/blog/link-rot-study/) in the nine-year period we looked at.

In many cases, your old URLs have links from other websites. If they’re not [redirected](https://ahrefs.com/blog/301-redirects/) to the current pages, then those links are lost and no longer count for your pages. It’s not too late to do these redirects, and you can quickly reclaim any lost value and help your content rank better.

Here’s how to find those opportunities:

- Paste your domain into [Site Explorer](https://ahrefs.com/site-explorer) (also accessible for free in [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools))
- Go to the Best by links report
- Add a “404 not found” HTTP response filter

I usually sort this by “Referring domains.”

I even created a [script to help you match redirects](https://colab.research.google.com/drive/18lMkaRHK__eNM6m5FpoyhGDlDAYr3a6P?usp=sharing). Don’t be scared away; you just have to download a couple of files and upload them. The Colab notebook walks you through it and takes care of the heavy lifting for you.

### Avoid long redirect chains

Redirect chains are when multiple redirects take place between a requested resource and its final destination.

Google’s [official documentation](https://developers.google.com/search/docs/advanced/crawling/http-network-errors) says that [Googlebot](https://ahrefs.com/blog/googlebot/) follows up to 10 redirect hops, so any redirect chains shorter than that aren’t usually a problem for SEO. They follow 5 hops in one session, and will resume where they left off in the next session.

If the crawler doesn’t receive content within 10 hops, Search Console will show a redirect error in the site’s Index Coverage report.

Many SEOs are obsessed with getting rid of even 1 additional hop for a redirect. I would not worry about this at all.

I don’t typically worry about redirect chains if they are less than 5 hops, but after 5 I’ve seen issues with them being crawled and counted properly so that’s my cutoff for recommending that people start working on them.

You can find long redirect chains for free using [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools):

- Crawl your site with [Site Audit](https://ahrefs.com/site-audit)
- Go to the Redirects report
- Click the Issues tab
- Look for the “Redirect chain too long” error

Click the issue and hit “View affected URLs” to see URLs that begin a redirect chain and all the URLs in the chain.

### Avoid redirect loops

Redirect loops are infinite loops of redirects that occur when a URL redirects to itself or when a URL in a redirect chain redirects back to a URL earlier in the chain.

They’re problematic for three reasons:

- **For users** –They cut off access to an intended resource and trigger a “too many redirects” error in the browser.
- **For bots and search engines** – They “trap” crawlers and waste the [crawl budget](https://ahrefs.com/blog/crawl-budget/).
- **For servers - they waste your resources.** Some bots will handle this well, others will not. They could potentially take down your server with a constant DDoS attack.

The simplest way to find redirect loops is to crawl your site with a tool like Ahrefs’ [Site Audit](https://ahrefs.com/site-audit). You can do this for free with an [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) account.

- Crawl your site with [Site Audit](https://ahrefs.com/site-audit)
- Go to the **Redirects** report
- Click the **Issues** tab
- Look for the “Redirect loop” error

If you then click the error and click “View affected URLs,” you’ll see a list of URLs that redirect, as well as all URLs in the chain:

The best way to fix a redirect loop depends on whether the last URL in the chain (before the loop) is the intended final destination.

If it is, remove the redirect from the final URL. Then make sure the resource is accessible and returns a 200 status code.

If it isn’t, change the looping redirect to the intended final destination.

In both cases, it’s good practice to swap out any [internal links](https://ahrefs.com/blog/internal-links-for-seo/) to remaining redirects for direct links to the final URL.

### Avoid overly broad redirects

When creating redirect rules, sometimes people match to everything after a folder. This creates situations where a bunch of pages might be redirected to a single page. You want to match redirects 1:1 as much as possible.

You can test this by typing your domain.com/asfkljlkdfs or something similar. You may want to try some of your main folders as well. If you receive a 404 page, then it’s fine. If it redirects, then someone has an overly broad rule in place.

These rules aren’t necessarily harmful, but they can send users to unexpected places. In some cases, it could be harmful. Let’s say you had a bunch of pages added via a hack and the hacker built links to these pages. If you remove the pages and then redirect them somewhere, you’re basically saying those spam links belong to you.

### Watch out for expired certificates

If you migrated to a different domain and your old site was using HTTPS, then the certificate expires, bots are passed but users will receive an error message and won’t be redirected.

There are multi-domain certificates that cover multiple sites that can help prevent this issue. Some DNS providers also allow HTTPS redirects now which would prevent this from happening.

### Keep redirects for at least 1 year

According to Google, you should keep redirects active for at least one year. After that, signals should permanently pass.

https://twitter.com/methode/status/1417920011071537153

If you don’t believe it, [I tested it](https://ahrefs.com/blog/are-pemanent-redirects-permanent/), and it seems to be true.

I’m a fan of keeping redirects as long as possible, potentially forever. You also should check if users are still hitting the old pages before removing any redirects.

### Don’t forget to redirect other files during a migration

It’s a good idea to redirect things like images and PDFs when doing a migration, not just pages. Especially if these were driving a good amount of traffic for your website. Don’t worry about things like JS, CSS, or Font files. Focus on redirecting things that get indexed by search engines and don’t worry about other file types.

## Troubleshooting Redirects for SEO

Here are some tips to help you troubleshoot redirect issues.

### Figuring out what system the redirects are in

Things can get complicated in an enterprise environment. You may have multiple different systems where redirects can be inputted and you may need to figure out which is actually firing a redirect.

You can use the information in the HTTP headers to help identify what system may have fired a redirect. For example, on our blog we use a plugin called Redirection. It adds a header tag X-redirected-by that identifies that it is the one that fired the redirect as seen below in the URL overview of Site Audit.

Our [SEO Toolbar](https://ahrefs.com/seo-toolbar) is another option for a quick header check while you’re browsing.

### Redirects may happen only for specific user-agents

Redirects can use conditional logic, meaning that they will only happen under certain conditions like for a specified user-agent. You can change your user agent using our SEO Toolbar to see if a redirect fires for a specific user-agent.

### Redirects can throw the wrong status codes

Don’t blindly trust the status codes shown. A redirect can still be happening with any status code. You may have a page that shows as a 200 OK status code, but still actually be redirecting to another location.

## Final thoughts

Regular expressions will save you a lot of time when it comes to patterns that can be matched for bulk URL redirects. Google a guide or cheat sheet and find a good regex tester. I typically use [regex101](https://regex101.com/).

Have questions? Message me on [X](https://twitter.com/patrickstox) or [LinkedIn](https://www.linkedin.com/in/patrickstox/).
