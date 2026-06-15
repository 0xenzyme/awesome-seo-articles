---
title: "Open redirect URLs: Is your site being abused?"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-01-open-redirect-urls-is-your-site-being"
url: "https://developers.google.com/search/blog/2009/01/open-redirect-urls-is-your-site-being"
canonical: "https://developers.google.com/search/blog/2009/01/open-redirect-urls-is-your-site-being"
author: "Written by Jason Morrison, Search Quality Team"
published: "2009-01-31T00:00:00+00:00"
updated: "2009-01-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:56:30+00:00"
status_code: 200
html_hash: "484891b60b13370d4a407c0b7ebecc6aff6e64116830e04030a8702c9534a38d"
clean_word_count: 1498
clean_char_count: 8948
---
# Open redirect URLs: Is your site being abused?

No one wants malware or spammy URLs inserted onto their domain, which is why we all try to follow
[good security practices](/search/blog/2007/09/quick-security-checklist-for-webmasters).
But what if there were a way for spammers to take advantage of your site, without ever setting a
virtual foot in your server? There is, by **abusing open redirect URLs**.

Webmasters face a number of situations where it's helpful to redirect users to another page.
Unfortunately, redirects left open to any arbitrary destination can be abused. This is a
particularly onerous form of abuse because it takes advantage of your site's functionality rather
than exploiting a simple bug or security flaw. Spammers hope to use your domain as a temporary
"landing page" to trick email users, searchers and search engines into following links which
appear to be pointing to your site, but actually redirect to their spammy site.

We at Google are working hard to keep the abused URLs out of our index, but it's important for you
to make sure your site is not being used in this way. Chances are you don't want users finding
URLs on your domain that push them to a screen full of unwanted porn, nasty viruses and malware,
or phishing attempts. Spammers will generate links to make the redirects appear in search results,
and these links tend to come from bad neighborhoods you don't want to be associated with.

This sort of abuse has become relatively common lately so we wanted to get the word out to you and
your fellow webmasters. First we'll give some examples of redirects that are actively being
abused, then we'll talk about how to find out if your site is being abused and what to do about
it.

## Redirects being abused by spammers

We have noticed spammers going after a wide range of websites, from large well-known companies to
small local government agencies. The list below is a sample of the kinds of redirect we have seen
used. These are all perfectly legitimate techniques, but if they're used on your site you should
watch out for abuse.

- Scripts that **redirect users to a file on the server**—such as a PDF document—can sometimes
  be vulnerable. If you use a content management system (CMS) that allows you to upload files,
  you might want to make sure the links go straight to the file, rather than going through a
  redirect. This includes any redirects you might have in the downloads section of your site.
  Watch out for links like this:
  `example.com/go.php?url=example.com/ie/ie40/download/`
- **Internal site search result pages** sometimes have automatic redirect options that could be
  vulnerable. Look for patterns like this, where users are automatically sent to any page after
  the `url=` parameter:
  `example.com/search?q=user+search+keywords&url=`
- Systems to **track clicks** for affiliate programs, ad programs, or site statistics might be
  open as well. Some example URLs include:

  ```
  example.com/coupon.jsp?code=ABCDEF&url=
  example.com/cs.html?url=
  ```
- **Proxy sites**, though not always technically redirects, are designed to send users through
  to other sites and therefore can be vulnerable to this abuse. This includes those used by
  schools and libraries. For example:
  `proxy.example.com/?url=`
- In some cases, **login pages** will redirect users back to the page they were trying to
  access. Look out for URL parameters like this:
  `example.com/login?url=`
- Scripts that put up an **interstitial page when users leave a site** can be abused. Lots of
  educational, government, and large corporate web sites do this to let users know that
  information found on outgoing links isn't under their control. Look for URLs following
  patterns like this:

  ```
  example.com/redirect/
  example.com/out?
  example.com/cgi-bin/redirect.cgi?
  ```

## Is my site being abused?

Even if none of the patterns above look familiar, your site may have open redirects to keep an eye
on. There are a number of ways to see if you are vulnerable, even if you are not a developer
yourself.

- Check if abused URLs are showing up in Google. Try a
  [site: search](/search/docs/monitor-debug/search-operators/all-search-site)
  on your site to see if anything unfamiliar shows up in Google's results for your site. You can
  add words to the query that are unlikely to appear in your content, such as commercial terms or
  adult language. If the query [site:example.com viagra] isn't supposed to return any pages on
  your site and it does, that could be a problem. You can even automate these searches with
  [Google Alerts](https://www.google.com/alerts).
- You can also watch out for strange queries showing up in the
  [Top search queries](https://www.google.com/support/webmasters/bin/answer.py?answer=35252)
  section of Webmaster Tools. If you have a site dedicated to the genealogy of the landed gentry,
  a large number of queries for porn, pills, or casinos might be a red flag. On the other hand, if
  you have a drug info site, you might not expect to see celebrities in your top queries. Keep an
  eye on the Message Center in Webmaster Tools for any messages from Google.
- Check your server logs or web analytics package for unfamiliar URL parameters (like
  `=http:` or `=//`) or spikes in traffic to redirect URLs on your site.
  You can also check the pages with external links in Webmaster Tools.
- Watch out for user complaints about content or malware that you know for sure can not be found
  on your site. Your users may have seen your domain in the URL before being redirected and
  assumed they were still on your site.

## What you can do

Unfortunately there is no one easy way to make sure that your redirects aren't exploited. An open
redirect isn't a bug or a security flaw in and of itself—for some uses they have to be left fairly
open. But there are a few things you can do to prevent your redirects from being abused or at
least to make them less attractive targets. Some of these aren't trivial; you may need to write
some custom code or talk to your vendor about releasing a patch.

- **Change the redirect code to check the referer**, since in most cases everyone coming to
  your redirect script legitimately should come from your site, not a search engine or elsewhere.
  You may need to be permissive, since some users' browsers may not report a referer, but if you
  know a user is coming from an external site you can stop or warn them.
- If your script should only ever send users to an internal page or file (for example, on a page
  with file downloads), you should **specifically disallow off-site redirects**.
- **Consider using an allowlist** of safe destinations. In this case your code would keep a
  record of all outgoing links, and then check to make sure the redirect is a legitimate
  destination before forwarding the user on.
- **Consider signing your redirects**. If your website does have a genuine need to provide URL
  redirects, you can
  [properly hash](https://en.wikipedia.org/wiki/HMAC)
  the destination URL and then include that cryptographic signature as another parameter when
  doing the redirect. That allows your own site to do URL redirection without opening your URL
  redirector to the general public.
- If your site is really not using it, just **disable or remove the redirect**. We have noticed
  a large number of sites where the only use of the redirect is by spammers—it's probably just a
  feature left turned on by default.
- **Use [robots.txt](/search/docs/crawling-indexing/robots/intro) to exclude search engines**
  from the redirect scripts on your site. This won't solve the problem completely, as attackers
  could still use your domain in email spam. Your site will be less attractive to attackers,
  though, and users won't get tricked via web search results. If your redirect scripts reside in
  a subfolder with other scripts that don't need to appear in search results, excluding the entire
  subfolder may even make it harder for spammers to find redirect scripts in the first place.
- You can also **use Webmaster Tools to
  [remove URLs](/search/docs/crawling-indexing/remove-information)**. Chances are
  that the spammers have also hacked and abused other sites to generate links to the spammed
  section of your site. If you see suspicious sites or
  [spammed forums](/search/blog/2008/09/keeping-comment-spam-off-your-site-and)
  linking in, you can
  [report those to us,](/search/docs/advanced/guidelines/report-spam)
  preferably with the
  [verified spam report form in Webmaster Tools](/search/docs/advanced/guidelines/report-spam).

Open redirect abuse is a big issue right now but we think that the more webmasters know about it,
the harder it will be for the bad guys to take advantage of unwary sites. Please you can leave any
helpful tips in the comments below or discuss in our
[Webmaster Help Forum](https://support.google.com/webmasters/community).
