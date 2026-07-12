---
title: "GENERIC CIALIS on my website? I think my site has been hacked!"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-11-generic-cialis-on-my-website-i-think-my"
url: "https://developers.google.com/search/blog/2009/11/generic-cialis-on-my-website-i-think-my"
canonical: "https://developers.google.com/search/blog/2009/11/generic-cialis-on-my-website-i-think-my"
author: "John Mueller"
published: "2009-11-26T00:00:00+00:00"
updated: "2009-11-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:02:15+00:00"
status_code: 200
html_hash: "5da54a0654f5f8b2e114383d7528546ce390ddde2f29ddf3a7b3bc590e1dc4e6"
clean_word_count: 722
clean_char_count: 4508
---
# GENERIC CIALIS on my website? I think my site has been hacked!

*This post is the first part of the How to use "Fetch as Googlebot" series*

Has your site ever dropped suddenly from the index or disappeared mysteriously from search
results? Have you ever received a notice that your site is using cloaking techniques?
Unfortunately, sometimes a malicious party "hacks" a website: they penetrate the security of a
site and insert undesirable content. Sophisticated attackers can camouflage this spammy or
dangerous content so that it doesn't appear for normal users, and appears only to Googlebot,
which could negatively impact your site in Google's results.

In such cases it used to be very difficult to detect the problem, because the site would appear
normal in the eyes of the user. It may be possible that only requests with a
`User-agent:` of Googlebot and coming from
[Googlebot's IP](/search/blog/2006/09/how-to-verify-googlebot)
could see the hidden content. But that's over: with
[Fetch as Googlebot](/search/blog/2009/10/fetch-as-googlebot-and-malware-details),
the new Labs feature in Webmaster Tools, you can see exactly what Googlebot is seeing, and avoid
any kind of cloaking problems. We'll show you how:

Let's imagine that the administrator of `www.example.com` is searching for their site, but they
find this instead:

![search result showing hacked content](/static/search/blog/images/archived_1_buy-generic-cialis.png)

That's strange, because when they look at the source code of `www.example.com`, it
looks fine:

![the html source code of the hacked content](/static/search/blog/images/archived_1_hacked-site-source.png)

With much surprise, the site owner may receive a notice from Google warning them that their site
is not complying with Google's quality guidelines. Fortunately they registered their site with
Webmaster Tools. Let's see how they can check what Googlebot sees:

First, they log into Webmaster Tools and select `www.example.com`. The Fetch as
Googlebot feature will be at the bottom of the navigation menu, in the Labs section:

![the webmaster tools dashboard with the fetch as googlebot link highlighted](/static/search/blog/images/archived_1_wmt-1.png)

The page will contain a field where you can insert the URL to fetch. It can also be left blank to
fetch the home page.

![the webmaster tools fetch as googlebot feature with the fetch button highlighted](/static/search/blog/images/archived_1_wmt-2.png)

They can simply click Fetch and wait a few seconds. After refreshing the page, they can see the
status of the fetch request. If it succeeds, they can click on the "Success" link...

![the webmaster tools fetch as googlebot feature with the success status highlighted](/static/search/blog/images/archived_1_wmt-3.png)

...and that will show the details, with the content of the fetched page:

![the webmaster tools fetch as googlebot feature shows additional details about the successful fetch](/static/search/blog/images/archived_1_wmt-4.png)

Aha! There's the spammy content! Now they can be certain that `www.example.com` has
been hacked.

Confirming that the website has been hacked (and perhaps is still hacked) is an important step.
It is, however, only the beginning. For more information, we strongly suggest getting help from
your server administrator or hoster and reading our previous blog posts on the subject of hacked
sites:

- [My site's been hacked - now what?](/search/blog/2008/04/my-sites-been-hacked-now-what)
- [A quick security checklist for webmasters](/search/blog/2007/09/quick-security-checklist-for-webmasters)
- [Message center warnings for hackable sites](/search/blog/2008/10/message-center-warnings-for-hackable)
- [Best practices against hacking](/search/blog/2009/02/best-practices-against-hacking)

If you have any questions about how to use the Fetch as Googlebot feature, you can drop by the
[Webmaster Help Forum](https://support.google.com/webmasters/community).
If you feel that your website might be hacked but are having problems resolving it, you might
want to ask the experts in our
"[Malware and Hacked sites](https://support.google.com/webmasters/threads?amp;thread_filter=(category:security_malware_hacked))"
category.

PS Keep in mind that once you have removed hacked content from your site, it will generally still
take time for us to update our search results accordingly. There are a number of factors that
affect crawling and indexing of your content so it's impossible to give a time-frame for that.
