---
title: "Google Uses ~40 Canonicalization Signals"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "canonicalization"
url: "https://ahrefs.com/blog/canonicalization/"
canonical: "https://ahrefs.com/blog/canonicalization/"
author: "Patrick Stox"
published: "2022-05-19T23:11:22+00:00"
updated: "2025-03-14T04:18:48+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
fetched_at: "2026-06-12T11:21:00+00:00"
status_code: 200
html_hash: "3c6df168c3b0ad29da8114fdc624cc299ebc4ea18e66da23721f2e2e233c416a"
clean_word_count: 3541
clean_char_count: 21658
---
# Google Uses ~40 Canonicalization Signals

Canonicalization is the process that search engines use to determine the main version of the URL that will be indexed and shown to users when there are duplicate URLs. Clustering creates a cluster of duplicate pages, and canonicalization chooses which version signals consolidate to and what page will be shown in search results. This process involves duplicate detection, duplicate elimination, signal forwarding, error pages, and localization.

According to Google Webmaster Trends Analyst Gary Illyes, ~60% of the internet is duplicate content.

> Google’s crawling process is highly focused on removing duplication because 60% of the internet is duplicate [@methode](https://twitter.com/methode?ref_src=twsrc%5Etfw) [#seodaydk](https://twitter.com/hashtag/seodaydk?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/OJ9OkP74DU](https://t.co/OJ9OkP74DU)
>
> — Lily Ray (@lilyraynyc) [March 30, 2022](https://twitter.com/lilyraynyc/status/1509176261884747781?ref_src=twsrc%5Etfw)

Canonicalization is complex and often misunderstood. I don’t think most of the duplicates are nefarious. It’s mostly going to be technical issues that cause them. We’ll look at this more in a bit. I’m going to talk about how the canonicalization process works, as well as the following:

- [Canonicalization signals](#canonicalization-signals)
- [How to check the canonical](#how-to-check-the-canonical)
- [Common mistakes](#canonicalization-mistakes)

## Canonicalization signals

A lot of different signals go into the canonicalization process. According to Google’s Allan Scott, there are ~40 different canonical selection signals. These include:

- Duplicates
- Canonical link elements
- Sitemap URLs
- Internal links
- External links
- Redirects
- Hreflang
- X-default hreflang
- PageRank
- HTTPS pages over HTTP
- Shorter URLs over longer URLs
- Where content was first published / seen
- Site level signals like a history of scraped content
- Pages over PDFs

Google looks at all the different signals and weighs them to determine what the canonical version should be. That’s the version of the page it will index and what it usually shows to users. This process is handled by a machine learning system and managed by a team called Dups at Google, which they say should be spelled Dupes.

A potential scenario when Google decides on the canonical based on internal links and the canonical URL.

### Duplicates

With [duplicate content](https://ahrefs.com/blog/duplicate-content/), Google will pick a canonical version to index. All the eligible pages form a cluster of pages, and the signals that go to the pages in that cluster will consolidate at the chosen canonical. That canonical may even change over time. In some really bad scenarios, a page on the wrong domain may be shown. This is referred to as hijacking.

Note: Only HTTP status code 200 pages can get clustered.

Some SEOs believe there is a [duplicate content penalty](https://ahrefs.com/blog/seo-myths/), but that’s not true. Generally, you’re going to have one version or another indexed. It may not be the version you want to be indexed, but it will be indexed and rank just as well as any other version of the same page.

Here are some examples of what can cause duplicate pages and sometimes canonicalization issues:

- **HTTP and** [**HTTPS**](https://ahrefs.com/blog/what-is-https/) **variants –** Examples: http://www.example.com and https://www.example.com. There are multiple canonicalization criteria to handle this.
- **Non-www and www variants – Examples:** http://example.com and http://www.example.com.
- **URLs with and without** [**trailing slashes**](https://ahrefs.com/blog/trailing-slash/) **– Examples:** https://example.com/page/ and https://example.com/page.
- **URLs with and without capital letters** **– Examples:** https://example.com/page/ and https://example.com/Page/.
- **Default versions of the page, such as index pages** **– Examples:** https://www.example.com/, https://www.example.com/index.htm, https://www.example.com/index.html, https://www.example.com/index.php, https://www.example.com/default.htm, etc.
- **Alternate versions of pages** **–** This could include mobile versions (e.g., example.com and m.example.com), AMP versions (e.g., example.com/page and amp.example.com/page), print versions (e.g., example.com/page and example.com/page/print), alternate versions meant for other countries but containing the same content (e.g., example.com/en-us/, example.com/en-gb/, example.com/en-au/), or versions in a dev or staging site (e.g., dev.example.com).
- [**URL parameters**](https://ahrefs.com/blog/url-parameters/) **–** Examples: example.com?parameter=whatever. These may exist because of tracking codes, faceted navigation, sorting content, session IDs, etc. There are some instances where parameters may change the page’s content so that it’s not a duplicate.
- **Other pages showing the full content –** Google may choose the wrong canonical when another page displays the content in full. This may include the main blog page, paginated pages, tag pages, category pages, or feed pages.
- **Scraped or syndicated content –** [Content syndication best practices](https://ahrefs.com/blog/content-syndication/) generally recommend having a canonical tag back to the original content or at least a link to the original content. That’s because the canonical chosen can be a completely different domain. They try to select the original source as the canonical but, in some cases, they choose the wrong page.
- **Boilerplate translations**. This is where things like menus and text that appears on every page may be translated, but the main content is not. These will be clustered together. However, if the price or currency is different, then they will try to put them in different clusters.
- **Error pages**. Error pages can cluster with each other, including soft 404s / crypto 404s, pages with JavaScript dependencies that didn’t load or didn’t get rendered, bot detection error pages, etc.

Most of these aren’t usually issues. As I mentioned, Google will usually choose one version or another as the canonical. There are a few exceptions to this.

1. Sometimes with content syndication, the original source isn’t chosen as the canonical. This is a real problem. How would you feel if someone else started ranking for an article you wrote?
2. [Hreflang](https://ahrefs.com/blog/hreflang-tags/) does not solve duplication on international sites. Google will generally try to swap to show the correct version. But it’s not guaranteed, and this setup often breaks. When this happens, users see pages from the wrong country. It’s best to avoid having the same content on multiple pages for international websites.
3. With some JavaScript sites (typically app shell models), the initial code for the pages can look like other pages or even the code from other websites. Sometimes, these pages get canonicalized to other pages on the same or even different websites.

I believe part of the problem with both hreflang and the JavaScript content is that Google may be running the duplicate detection via crawl algorithms that detect duplication patterns, again after just seeing the code and yet again after rendering the pages.

Google’s render path marked up where I believe duplicate detection systems are run.

With the pages using hreflang, if it decides that the pages are duplicates without crawling them, it may not be able to swap them properly.

Before a page is even rendered, it may “look” like another page based on the HTML content. Google may choose the canonical based on this initial version and may not prioritize it for rendering because it’s already deemed a duplicate page. This usually resolves itself after rendering, but it can take some time to clear up.

Google has a couple of rules it generally follows when it comes to canonicalization of duplicates.

#### 1. It prefers HTTPS pages over HTTP pages.

Google will generally index the HTTPS version, but there are a few issues or conflicting signals that may cause it to choose the HTTP version instead, such as:

- Having an invalid security certificate.
- HTTPS page links to HTTP resources on the page (excludes images).
- HTTPS redirecting to HTTP.
- HTTPS page having a rel=“canonical” link element pointing to the HTTP page.
- HTTPS page redirects to HTTP page which redirects to HTTPS page. It’s not secure, so it might lead to an HTTP canonical.

The key point here is that they will choose the HTTP page when it’s not secure.

#### 2. It prefers shorter URLs over longer URLs.

This has been misconstrued over the years by SEOs to say that all your URLs should be shorter. But that’s not what was meant by the original statement. What Google said was that if you had, for instance, a clean, short version of a URL and a longer version with parameters attached, it would generally choose the shorter version of the URL without the parameter as the canonical version.

### Canonical link element

This is also commonly referred to as a [canonical tag](https://ahrefs.com/blog/canonical-tags/). It looks like this:

`<link rel="canonical" href="https://www.example.com" />`

The canonical tag is sometimes referred to as a hint because it’s just one canonicalization signal, but it is considered a strong signal. Google ignores it if other signals are stronger.

The canonical link element serves multiple purposes. It’s used for clustering and to determine which version is the canonical.

If the canonical tag is respected, all signals like links will pass. However, if the canonical is ignored, no value is passed. The value isn’t lost; it stays with the original page or goes to whatever page Google chooses as the canonical.

A canonical link element can be implemented in two different ways. It can be in the <head> section or the HTTP header.

A fun anecdote. Google’s SEO Starter Guide used to be a PDF. It didn’t have a canonical tag set in the HTTP header, and people used to “steal” the listing with their own duplicate version.

Sometimes the <head> section of a page will end before it should. This is usually caused by a tag in the <head> not closed out properly. When that happens, a canonical tag may be put into the <body> section instead. If that happens, your canonical tag won’t be respected.

Invalid canonical tag located in the <body> section.

If a blank canonical link element “” (gets treated as “/”) is used on a bunch of pages, it may be ignored. Same with variables in the canonical that weren’t filled in when the page loaded. Google is trying to help you because you got it wrong.

### Sitemap URLs

The URLs you include in your [sitemap](https://ahrefs.com/seo/glossary/sitemap) are also a canonicalization signal. Most of the time, you only want to include URLs of pages that you want to be indexed.

There are some exceptions to this because sitemap URLs also help with crawling. After a [website migration](https://ahrefs.com/blog/website-migration/), you should create a sitemap that still lists the old pages, even though they aren’t canonical. This will help the redirects be processed faster. You’ll want to delete this sitemap after most of the redirects have been picked up and processed.

### Internal links

It matters how you link to pages. [Internal links](https://ahrefs.com/blog/internal-links-for-seo/) are another canonicalization signal.

Generally, you should link to the version of a page you want to be canonical and update the links to any URLs that may have changed. However, there are exceptions to this, such as with [faceted navigation](https://ahrefs.com/blog/faceted-navigation/). In some cases like this, what is best for users may trump what is best for SEO.

### External links

It matters how others link to your pages. If you can have external links updated to point to the latest version of your page, that helps to show that you want the latest version of the page indexed.

### Redirects

There are several different types of redirects, and they’re all canonicalization signals. Redirects are generally a pretty strong canonicalization signal. They pass [PageRank](https://ahrefs.com/blog/google-pagerank/) and help determine which URL gets shown in Google’s index.

Permanent redirects such as 301s send signals forward to the new URL. Temporary redirects such as 302s and some 307s send signals backward to the redirected URL. If a temporary redirect is left in place long enough or the URL it’s redirected to already exists, it may be treated as a permanent redirect and send signals forward instead. It requires enough signals to flip the scale we saw earlier for canonicalization signals. As links build up, internal links are changed, sitemap URLs are updated, etc., more signals point to the new URL than the old URL, and the flip occurs.

At some point, the scale flips for temporary redirects like 302s.

A 307 has two different cases. In cases where it’s a temporary redirect, it will be treated the same as a 302 and attempt to consolidate backward. When web servers require clients to only use HTTPS connections (HSTS policy), Google won’t see the 307 because it’s cached in the browser. The initial hit (without cache) will have a server response code that’s likely a 301 or a 302. But your browser will show you a 307 for subsequent requests.

#### Types of permanent redirects

- HTTP 301
- HTTP 308
- Meta refresh 0
- HTTP refresh 0
- JavaScript location
- Crypto redirect

#### Types of temporary redirects

- HTTP 302
- HTTP 303
- HTTP 307 (server side, not the browser cached one)
- Meta refresh >0
- HTTP refresh >0

#### Signal consolidation

Signals are usually consolidated permanently after 1 year. If a redirect is removed after that period, signals will stay at the page that was redirected to. If the original page is restored, any new signals will go to the restored page, but old signals will still consolidate at the page that was redirected to.

### Hreflang

Hreflang is another signal for canonicalization. Pages included in hreflang tags are more likely to be selected as canonical. X-default in particular is used, not for clustering, but for canonical selection.

This is also complicated when it comes to duplicate pages since generally one page may be indexed and signals consolidate there, but they may still swap the page shown to a more appropriate one for users in the search results. Fully translated pages are not duplicates, and signals will not consolidate for those.

This part is complicated and I’d recommend reading [Hreflang: The Easy Guide for Beginners](https://ahrefs.com/blog/hreflang-tags/) for more info.

### PageRank

[PageRank](https://ahrefs.com/blog/google-pagerank/) is also confirmed as a canonicalization signal. The page with a higher PageRank will have a higher weight and is more likely to be the canonical.

## How to check the canonical

Your main source of truth for what Google chose as the canonical will be the URL Inspection tool in Google Search Console. Enter the URL, and it will show what the declared canonical is and what Google chose as the canonical.

If you don’t have access to Google Search Console, the recommended way to check the version of a page Google has indexed is to paste the URL into Google. The top result is usually the canonical.

Similarly, if you check the cached version of a page in Google and a different page is shown, then Google has selected a different version of the page.

**Warning:** Don’t use site: searches for checking canonicals. It shows what Google knows about, not necessarily what’s indexed or the selected canonical.

Within Ahrefs’ [Site Audit](https://ahrefs.com/site-audit), we show many issues related to canonicalization. Keep in mind that we’re flagging best practices in most cases. Because the canonical is a hint, Google and other search engines will have to choose which version of a page to index.

Even if your website has lots of issues related to canonicalization, search engines may be able to figure out what version should be indexed and where they should consolidate signals. It may not create any real problems for them.

Fun fact. When running a site audit, we only count the canonical version of pages as crawl credits. Some other tools count every version of a page toward the credits. On many sites, this can eat multiple credits per page!

## Common mistakes

There’s a lot that can go wrong with canonicalization. Let’s look at some common mistakes.

### Mistake #1. Blocking the canonicalized URL via robots.txt

Blocking a URL in [robots.txt](https://ahrefs.com/blog/robots-txt/) prevents Google from crawling it, meaning that it cannot see any canonical tags on that page. That, in turn, prevents it from transferring any “link equity” from the non-canonical to the canonical.

Unless you have a [crawl budget](https://ahrefs.com/blog/crawl-budget/) issue, it’s probably better to let all the signals consolidate. Even if you’re going to block or noindex some versions, you may still want to check for versions with links that you should canonicalize instead. However, as Google tends to crawl non-canonical pages less over time, you may just want to wait.

### Mistake #2. Setting the canonicalized URL to “noindex”

Never mix noindex and rel=canonical. They’re contradictory instructions.

As John Mueller [states](https://www.reddit.com/r/TechSEO/comments/8yahdr/2_questions_about_the_canonical_tag/e2dey9i/?context=1), Google will usually prioritize the canonical tag over the “noindex” tag.

### Mistake #3. Setting a 4XX HTTP status code for the canonicalized URL

Setting a [4XX HTTP status code](https://ahrefs.com/blog/http-status-codes/) for a canonicalized URL has the same effect as using the “noindex” tag: Google will be unable to see the canonical tag and transfer “link equity” to the canonical version.

### Mistake #4. Canonicalizing all paginated pages to the root page

Paginated pages should not be canonicalized to the first paginated page in the series. Instead, self-referencing canonicals should be used on all paginated pages.

Why? As John [stated on Reddit](https://www.reddit.com/r/TechSEO/comments/ag77vi/canonicals_and_angular_js/), this is improper use of the rel=canonical.

> The main thing to avoid, since this post is about canonicalization, is to use the rel=canonical on page 2 pointing to page 1. Page 2 isn’t equivalent to page 1, so the rel=canonical like that would be incorrect.
>
>
>
> John Mueller, Webmaster Trends Analyst [Google](https://twitter.com/JohnMu)

We have a [guide on pagination for SEO](https://ahrefs.com/blog/rel-prev-next-pagination/) and best practices if you’re interested.

### Mistake #5. Using the URL removal tool in Google Search Console for canonicalization

This can remove all versions of a URL, effectively deindexing your page from search.

### Mistake #6. Not keeping canonicalization signals consistent

As we talked about earlier, there are many different canonicalization signals.

Having different signals suggest different canonicals means that you will be relying on Google to select a canonical for you. The more consistent signals you show Google with your preferred version, the more likely it is that version will be the chosen canonical.

### Mistake #7. Not using canonical tags with hreflang

[Hreflang tags](https://ahrefs.com/blog/hreflang-tags/) specify the language and geographical targeting of a webpage.

Google [states](https://support.google.com/webmasters/answer/139066?hl=en) that when using hreflang, you should “specify a canonical page in the same language, or the best possible substitute language if a canonical doesn’t exist for the same language.”

### Mistake #8. Having multiple rel=canonical tags

Having multiple rel=canonical tags will usually cause Google to ignore them. In many cases, this happens because tags are inserted into a system at different points, such as by the CMS, the theme, and plugin(s). This is why many plugins have an overwrite option meant to ensure they are the only source for canonical tags.

Another area where this may be a problem is with canonicals added with JavaScript. If you have no canonical URL specified in the HTML response and then add a rel=canonical tag with JavaScript, it should be respected when Google renders the page. However, if you have a canonical specified in HTML and swap the preferred version with JavaScript, you send mixed signals to Google.

### Mistake #9. Rel=canonical in the <body>

Rel=canonical should only appear in the <head> of a document. A canonical tag in the <body> section of a page will be ignored.

Where this can become a problem is with the parsing of a document. Even if the page’s source code has the rel=canonical tag in the correct place, many different things, such as unclosed tags, JavaScript injected, or <iframes> in the <head> section, can cause the <head> to end prematurely while rendering. In these cases, a canonical tag may be accidentally thrown into the <body> of a rendered page where it will not be respected.

## Final thoughts

Many of the tools SEOs had for handling canonicalization have been taken away, such as the URL Parameters Tool and Preferred Domain setting in Google Search Console. However, there are still plenty of other signals to help Google choose a canonical.

Signals can change over time. For instance, there used to be a signal for redirecting to shorter URLs, but it was deprecated because it had conflicts with HTTPS/HTTP signals. It was trying to force shorter URLs while Google wanted the HTTPS versions.

If you have questions, message me [on Twitter](https://twitter.com/patrickstox).
