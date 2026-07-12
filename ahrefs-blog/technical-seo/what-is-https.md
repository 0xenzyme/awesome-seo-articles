---
title: "What is HTTPS? Everything You Need to Know"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "what-is-https"
url: "https://ahrefs.com/blog/what-is-https/"
canonical: "https://ahrefs.com/blog/what-is-https/"
author: "Michal Pecánek"
published: "2020-05-07T16:43:16+00:00"
updated: "2026-03-19T17:21:33+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
fetched_at: "2026-06-12T12:16:43+00:00"
status_code: 200
html_hash: "492b79bfe9def2f0315891f71d1a718452adfeb0189dcf7deb50fafbe6d1e509"
clean_word_count: 3272
clean_char_count: 20102
---
# What is HTTPS? Everything You Need to Know

HyperText Transfer Protocol Secure (HTTPS) is an encrypted version of HTTP, which is the main protocol used for transferring data over the World Wide Web.

HTTPS protects the communication between your browser and server from being intercepted and tampered with by attackers. This provides confidentiality, integrity and authentication to the vast majority of today’s WWW traffic.

Any website that shows a lock icon in the address bar is using HTTPS.

In this article, you’ll learn:

- [The basics of HTTP and HTTPS](#https-vs-https)
- [How TLS certificates work](#how-tls-works)
- [How HTTPS helps SEO](#https-and-seo)
- [How to set up HTTPS](#how-to-set-up-https)
- [Common HTTPS errors and how to fix them](#common-https-errors)
- [How to check for potential HTTPS migration mistakes](#common-https-mistakes)

New to technical SEO? Check out our

[Beginner’s guide to technical SEO](https://ahrefs.com/blog/technical-seo/)

## HTTP vs. HTTPS: Understanding the basics

First, let me simplify and illustrate the communication between the client (browser) and server when there’s an attacker in between.

As you can see, attackers can get hold of sensitive data like login and payment details or inject malicious code into the requested resources.

Potential network attacks can happen anywhere with an untrusted router or ISP. Any public WiFi network is therefore vulnerable to such attacks. Fortunately, it seems that the general public is getting aware of this fact (increasing usage of VPNs).

However, the burden of making everyone’s browsing experience secure is and should be on webmasters.

That’s where the adoption of HTTPS comes into play.

HTTPS encrypts HTTP requests and responses so an intercepting attacker would only see random characters instead of credit card details, for example.

An analogy to how HTTPS works would be sending valuables in an indestructible locked combination box. Only the sending and receiving parties know the combination and if attackers get hold of it, they won’t get inside.

Now, a lot of things happen when a HTTPS connection is formed. Mainly, HTTPS relies on TLS (Transfer Layer Security) encryption to secure the connections.

### Attacks HTTPS prevents

Without HTTPS, your site is vulnerable to several well-known attacks:

- **Man-in-the-middle (MITM)**: Attacker intercepts communication between browser and server
- **Session hijacking**: Stealing session cookies sent over unencrypted connections
- **SSL stripping**: Downgrading HTTPS to HTTP without user knowledge
- **Credential theft**: Capturing login credentials sent in plaintext

HSTS (HTTP Strict Transport Security) specifically prevents SSL stripping by forcing HTTPS connections—we’ll cover that later.

## How TLS certificates work

The only way to enable HTTPS on your website is to get a TLS certificate and install it on your server. You’ll also encounter it as an SSL or SSL/TLS certificate but don’t worry, it’s all the same thing. SSL is still widely used terminology even though we all technically use its successor TLS.

TLS certificates are issued by Certificate Authorities (CA). The role of CA is to be a trusted third-party in the client-server relationship. Basically, anyone can issue TLS certificates but only the publicly trusted CAs are supported by browsers.

You can check every website’s TLS certificate and its issuing CA by clicking on the lock icon in your browser’s address bar.

You can click through the certificate to learn more. The important thing here is the “Issued to:” line. This is when we get into different types of validation standards for TLS certificates, which is what mainly sets the free and paid certificates apart.

### TLS versions: Why 1.3 matters

Not all TLS is created equal. Here’s what you need to know about TLS versions:

- **TLS 1.3 (2018)**: Current standard. Faster handshakes, stronger encryption, removes vulnerable ciphers
- **TLS 1.2 (2008)**: Still acceptable and widely supported
- **TLS 1.0/1.1**: Deprecated. Major browsers dropped support in 2020, and Microsoft deprecated these versions in February 2026

Best practice: Configure servers to support TLS 1.3 with TLS 1.2 fallback. Disable older versions entirely.

### DV, OV and EV: What does it mean and which one to choose?

Free TLS certificates that come with your hosting and [CDN](https://en.wikipedia.org/wiki/Content_delivery_network) plans only do domain validation (DV). This validates that a certificate owner controls a given domain name. Such a basic validation technique is good enough for blogs and websites that don’t handle sensitive information, but isn’t ideal for those that do.

Websites using a DV TLS certificate appear secure but you won’t see the “Issued to:” line when you click the lock icon.

The most common DV TLS certificate comes from a non-profit CA called [Let’s Encrypt](https://letsencrypt.org/), which holds about 64% market share among SSL certificate authorities. That’s what most companies offering free automatically renewable TLS certificates use.

There’s nothing wrong with DV-only certificates, after all it’s the only type of TLS certificate that can be automatically issued at scale. However, HTTPS is only as strong as the underlying certificate that authenticates the server you’re talking to.

If your website allows logins or payments, you should invest in a TLS certificate that offers organization validation (OV) or extended validation (EV). These two types differ in the verification process with the EV being more rigorous.

If you’re looking to buy just one, I’d recommend going straight for the EV TLS certificate. It’s the most trustworthy one and it doesn’t cost much more than OV.

### Wildcard and SAN TLS certificates

Leaving validation standards behind, let’s move onto another category of TLS certificates.

Wildcard and SAN certificates are used to secure multiple (sub)domains at once. If you bought a standard EV TLS certificate for example.com, you’d need a separate certificate for blog.example.com.

Wildcard certificates can secure unlimited subdomains (example.com, blog.example.com, docs.example.com) while SAN certificates also have the option to secure other domains as well (example.com, blog.example.com, different.org).

These types are combined with the validation types so you’ll see all sorts of combinations when you browse through the options CAs offer. They will also guide you through the validation process.

## How HTTPS helps SEO

Pretty much all the benefits of HTTPS tie back to SEO:

- Lightweight ranking signal
- Better security and privacy
- Preserves referral data
- Enables the use of modern protocols that enhance security and site speed

### Lightweight ranking signal

Google [announced](https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html) that HTTPS is a lightweight [ranking factor](https://ahrefs.com/blog/google-ranking-factors/) way back in 2014. It’s more like a tiebreaker than something that would skyrocket your rankings if other ranking factor variables remained unchanged.

This is basically Google’s contribution to faster worldwide HTTPS adoption.

### Better security and privacy

We already talked about this one. But how is this connected to SEO?

When you land on an unsecure website, you’ll see something like this:

It doesn’t really build trust, right? I’m aware of my professional bias but I personally pay attention to this and quickly form a bad first impression if I see that on any website.

My guess is that migrating to HTTPS [can improve dwell time](https://ahrefs.com/seo/glossary/dwell-time) and prevent pogo sticking. While these are only theorised (not confirmed) ranking factors, making people ‘stick’ when they land on your website is something you want regardless of SEO.

**Important update for 2026:** Google Chrome is rolling out “HTTPS-by-default” starting October 2026 (Chrome 154). This means Chrome will automatically attempt HTTPS connections and display a warning before loading any HTTP site. The rollout begins April 2026 for Enhanced Safe Browsing users. If your site still uses HTTP, you have until late 2026 before Chrome actively warns visitors away.

### Preserves referral data

If your website is still on HTTP and you’re using web analytics services like Google Analytics, I have bad news for you: No referral data is passed from HTTPS to HTTP pages.

As the vast majority of the web now runs on HTTPS (89% of all websites as of 2026, [according to W3Techs](https://w3techs.com/technologies/details/ce-httpsdefault)), the source of most referral traffic (clicks on links from other websites) will be labeled as direct in most analytics software.

One disadvantage of this is that it makes your data messy and skewed. Another is that you’re unable to see your best referral sources—which is a wasted [link building opportunity](https://ahrefs.com/blog/link-building-strategies/).

### Enables the use of modern protocols that enhance security and site speed

On paper, HTTPS is slower than HTTP because of the added security features. However, having HTTPS is the prerequisite for using the latest security and web performance technology.

In other words, besides security, HTTPS also enables your website to improve its [page speed](https://ahrefs.com/blog/core-web-vitals/) when you use protocols like [TLS 1.3](https://kinsta.com/blog/tls-1-3/), [HTTP/2](https://www.distilled.net/resources/an-introduction-to-http2-for-seos/), and HTTP/3.

**HTTP/3 and QUIC:** HTTP/3 is the latest HTTP protocol version, using QUIC instead of TCP for transport. Key benefits include faster connection establishment (0-RTT handshakes), better performance on unreliable networks like mobile and WiFi, and built-in encryption since QUIC requires TLS 1.3. HTTP/3 has reached about 35% global adoption as of 2025.

And apart from better user experience, Google considers page speed as a lightweight ranking factor similar to HTTPS:

> Ranking wise it’s a teeny tiny factor, very similar to https ranking boost. That particular one is not surprising. You do that primarily to enable users to convert.— Socially distant Gary Illyes (@methode) [April 28, 2020](https://twitter.com/methode/status/1255224116648476675?ref_src=twsrc%5Etfw)

## Common HTTPS errors and how to fix them

Before we dive into migration mistakes, here’s a quick reference for common HTTPS errors users encounter and what causes them:

| Cause | Error | Fix |
| --- | --- | --- |
| Certificate expired | NET::ERR\_CERT\_DATE\_INVALID | Renew certificate immediately |
| Domain name doesn’t match certificate | NET::ERR\_CERT\_COMMON\_NAME\_INVALID | Reissue certificate with correct domain |
| Certificate not in CT logs | NET::ERR\_CERTIFICATE\_TRANSPARENCY\_REQUIRED | Use a CT-compliant Certificate Authority |
| Server using outdated TLS version | ERR\_SSL\_VERSION\_OR\_CIPHER\_MISMATCH | Enable TLS 1.2 and TLS 1.3 on server |
| HTTP resources loaded on HTTPS page | Mixed content warning | Update all resource URLs to HTTPS |

Most of these errors stem from misconfigured servers or expired certificates. If you’re seeing these on your own site, address them immediately—browsers will warn visitors away.

## How to set up HTTPS

This depends on your scenario.

### 1. You’re launching a new website

You’ve won the lottery. Go with HTTPS from the beginning and you won’t ever have to worry about HTTP and errors associated with the [migration](https://ahrefs.com/blog/website-migration/).

All you need to do is to have a good hosting provider that will guide you through the process, and that supports the latest HTTP and TLS protocol versions. After all is up and running, [implement HSTS](https://https.cio.gov/hsts/) as the last step to seal the security.

### 2. You already have an HTTPS-enabled website

The fact that you’re reading this article tells me that it’s probably not set up correctly. Follow the advice in the [next section](#common-https-mistakes) to check for common errors.

### 3. You still have a website running on HTTP

It will take a while to get everything prepared and done. The complexity of the migration depends on:

- The size and complexity of your website
- What kind of CMS you use
- Your hosting/CDN providers
- Your technical abilities

While I believe that owners of small websites running on popular CMS and solid hosting can do the migration themselves, there are a lot of variables at play.

I suggest you check the documentation of your CMS/server/hosting/CDN and proceed accordingly—and with caution. There are quite a lot of steps you need to execute so [create or follow a migration checklist](https://searchengineland.com/http-https-seos-guide-securing-website-246940) and don’t try to fit in other activities.

If all of this sounds too technical for you, hire a professional. It will save you hours of your time, save your nerves, and ensure future-proof implementation.

## How to check for potential HTTPS migration mistakes

Even if you ticked off the whole HTTPS migration checklist, chances are that you’ll still encounter some issues.

While HTTPS adoption has improved dramatically, implementation errors remain common—particularly during migrations. Our 2016 study of 10,000 domains found widespread issues at the time, and many of the same mistake patterns persist today.

I’d recommend that you check for the five common HTTPS migration mistakes below. It won’t take long, and most of them aren’t that hard to fix.

You can also enable [Always-on Audit in Ahrefs Site Audit](https://ahrefs.com/blog/always-on-audit/). It monitors your site 24/7 and alerts you about critical issues—like HTTP pages slipping through or broken redirects—as soon as they pop up. This is especially useful after an HTTPS migration when issues can surface unexpectedly.

### Mistake 1: HTTP pages left

First and foremost, you need to make sure that all pages on your site are already on HTTPS.

You can discover leftover HTTP pages by thoroughly crawling the website. This shouldn’t be anything new if you stuck to any HTTPS migration checklist. Just make sure that the crawler has all the required URL sources so it doesn’t leave pages behind.

To do that, you can use [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) for free with the following setup:

After it’s done, open the latest crawl, go to Page Explorer and apply the following filter:

Export the list of HTTP URLs and redirect them to finish the migration.

TIP

You can also enable [IndexNow auto-submit](https://help.ahrefs.com/en/articles/9317209-how-to-submit-pages-to-indexnow-within-site-audit) in your Site Audit settings. After you fix redirect issues or update pages, Site Audit will automatically notify Bing and other search engines about the changes—so they recrawl your updated pages faster.

Remember: pages that are not in your [sitemap](https://ahrefs.com/blog/how-to-create-a-sitemap/) and have zero links pointing to them are impossible to discover by crawling. This can often happen with dedicated PPC landing pages. One way to find these is to export the URL list from your ads managers like Google Ads or FB Business Manager.

From there, make sure the orphaned pages were migrated properly. And don’t forget to update them in your campaign dashboards to the newer HTTPS format.

### Mistake 2: HTTPS pages with HTTP content

This mistake occurs when the initial HTML file is loaded using HTTPS but its resource files (images, CSS, JavaScript) haven’t been updated to HTTPS yet.

If this is an issue on your website, you’ll see it both in the crawl overview and Internal pages report. All errors, warnings and notices in the free Ahrefs Webmaster Tools contain a description of the issue and advice on how to fix it.

### Mistake 3: Internal links not updated to HTTPS

Not updating your [internal links](https://ahrefs.com/blog/internal-links-for-seo/) to HTTPS causes unnecessary redirects. That’s obviously better than landing on an HTTP page but we’ve already gone through this mistake. It’s easy to spot these links and fix them.

You’ll find this issue under the Links report in Site Audit within [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools):

Just rewrite the URLs to https:// and you’re done. This is only applicable if you’ve already made sure that no HTTP pages are left using the advice under mistake #1.

### Mistake 4: Tags not updated to HTTPS

There are two types of tags you might be using on your website that also need their URLs updating to HTTPS: Canonical tags and Open Graph tags.

[Canonical tags](https://ahrefs.com/blog/canonical-tags/) tell Google what you consider to be the most authoritative page from a bunch of similar or duplicate pages. Pointing that to an HTTP version can definitely send a bad signal to Google and will be most likely ignored.

If you use [Open Graph tags](https://ahrefs.com/blog/open-graph-meta-tags/) to optimize your social media posts, then URL tags are required by Facebook. They should be the same as canonical URLs.

To find pages with HTTP canonical and OG tags, set up this custom filter in Page Explorer:

Again, all that’s left is to rewrite them to https:// given a completely finished migration.

TIP

You can fix canonical tags directly in Site Audit using [Patches.](https://ahrefs.com/patches) Click “Patch it” on any affected URL, update the canonical to the correct HTTPS version, and publish the change—no developers needed. You can even test your edits first and roll them back if something goes wrong.

### Mistake 5: Failed redirects

Redirects can be tricky. There’s quite a lot that could go wrong—from broken redirects, to redirect chains and loops.

Fortunately, it’s easy to spot these errors with Site Audit. Just check the Redirects report and go through all the issues.

After you click on the “View affected URLs” button, you’ll see a report similar to this, just with more default columns and metrics:

The best thing here is that you’ll really see all the affected URLs—the redirected ones, ones inside the redirect chain, and those that link to the redirected ones.

There are two things you should do here.

The first one is splitting up the redirects, in this case:

*https://blog.example.com/123/> -> 301 redirect -> >https://example.com/blog/987/*

This would ensure that all backlinks pointing to both https://blog.example.com/123/ and https://example.com/blog/123/ would be redirected only once. That’s fine for external backlinks as reaching out to webmasters with link edit requests would be highly ineffective and quite annoying.

We can do better internally though.

You should strive for the least number of redirects. That’s when the number of inlinks column comes into play.

Inlinks are URLs that link to the URL affected by the redirect chain. You’ll want to swap the links on those pages for URLs that return a [200 HTTP status code](https://ahrefs.com/blog/http-status-codes/). If you click through the number of inlinks, you’ll see all of them:

Of course, again, the next step would be checking the inlinks of the URLs within the redirect chain. However, that’s of a lower priority as we already broke the redirect chain. These would be tagged as standard 301 redirects in the 3XX Redirects report upon the next crawl.

## Final thoughts

HTTPS is essential for website security and is now expected by users and search engines alike. With Chrome’s 2026 HTTPS-by-default rollout approaching, there’s no better time to ensure your site is properly configured.

The migration process can be complex, but the benefits—improved security, better SEO signals, preserved referral data, and access to modern protocols like HTTP/3—make it worthwhile.

Use [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) to audit your HTTPS implementation and catch common migration mistakes before they impact your site’s performance. And with features like [Always-on Audit](https://ahrefs.com/blog/always-on-audit/) and [Patches](https://ahrefs.com/patches), you can monitor issues continuously and fix them without waiting on developers.
