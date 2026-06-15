---
title: "Advanced Website Diagnostics with Google Webmaster Tools"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-09-advanced-website-diagnostics-with"
url: "https://developers.google.com/search/blog/2008/09/advanced-website-diagnostics-with"
canonical: "https://developers.google.com/search/blog/2008/09/advanced-website-diagnostics-with"
author: "John Mueller"
published: "2008-09-30T00:00:00+00:00"
updated: "2008-09-30T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T12:54:01+00:00"
status_code: 200
html_hash: "ba49e0e69e0a2a8d5ae92613ccf21e2ffd76539c41c239a42a2320968962198a"
clean_word_count: 1145
clean_char_count: 7008
---
# Advanced Website Diagnostics with Google Webmaster Tools

Running a website can be complicated—so we've provided
[Google Webmaster Tools](https://search.google.com/search-console)
to help webmasters to recognize potential issues before they become real problems. Some of the
issues that you can spot there are relatively small (such as having
[duplicate titles and descriptions](/search/blog/2007/12/new-content-analysis-and-sitemap)),
other issues can be bigger (such as your website not being reachable). While Google Webmaster
Tools can't tell you exactly what you need to change, it can help you to recognize that there
could be a problem that needs to be addressed.

Let's take a look at a few examples that we ran across in the
[Google Webmaster Help Groups](https://support.google.com/webmasters/community):

## Is your server treating Googlebot like a normal visitor?

While Googlebot tries to act like a normal user, some servers may get confused and react in
strange ways. For example, although your server may work flawlessly most of the time, some
servers running IIS may react with a server error (or some other action that is tied to a server
error occurring) when visited by a user with Googlebot's user-agent. In the Webmaster Help Group,
we've seen IIS servers return
[result code `500` (Server error)](https://groups.google.com/group/Google_Webmaster_Help-Indexing/browse_thread/thread/f8ba10ba010b6039)
and
[result code `404` (File not found)](https://groups.google.com/group/Google_Webmaster_Help-Indexing/browse_thread/thread/aee395cf58179168)
in the "Web crawl" diagnostics section, as well as
[result code `302` when submitting Sitemap files](https://support.google.com/webmasters/community).
If your server is redirecting to an error page, you should make sure that we can crawl the error
page and that it returns the proper result code. Once you've done that, we'll be able to show you
these errors in Webmaster Tools as well. For more information about this issue and possible
resolutions, please see
[https://todotnet.com/archive/0001/01/01/7472.aspx](https://blog.todotnet.com/2006/07/get-googlebot-to-crash-your-net-2-0-site/)
and
<https://www.kowitz.net/archive/2006/12/11/asp.net-2.0-mozilla-browser-detection-hole.aspx>.

If your website is hosted on a Microsoft IIS server, also keep in mind that
[URLs are case-sensitive](/search/blog/2008/06/get-audio-and-q-from-our-recent-live)
by definition (and that's how we treat them). This includes URLs in the
[robots.txt file](/search/docs/crawling-indexing/robots/create-robots-txt), which is something
that you should be careful with if your server is using URLs in a non-case-sensitive way. For
example, `disallow: /paris` will block `/paris` but not `/Paris`.

## Does your website have systematically broken links somewhere?

Modern content management systems (CMS) can make it easy to create issues that affect a large
number of pages. Sometimes these issues are straightforward and visible when you view the pages;
sometimes they're a bit harder to spot on your own. If an issue like this creates a large number
of broken links, they will generally show up in the "Web crawl" diagnostics section in your
Webmaster Tools account (provided those broken URLs return a proper `404` result
code). In one recent case, a site had a
[small encoding issue in its RSS feed](https://groups.google.com/group/Google_Webmaster_Help-Indexing/browse_thread/thread/7b2db6a15083737a),
resulting in over 60,000 bad URLs being found and listed in their Webmaster Tools account. As you
can imagine, we would have preferred to spend time crawling content instead of these
`404` errors
:).

## Is your website redirecting some users elsewhere?

For some websites, it can make sense to concentrate on a group of users in a certain geographic
location. One method of doing that can be to redirect users located elsewhere to a different page.
However, keep in mind that Googlebot might not be crawling from within your target area, so it
might be redirected as well. This could mean that Googlebot will not be able to access your home
page. If that happens, it's likely that Webmaster Tools will run into problems when it tries to
confirm the verification code on your site, resulting in your
[site becoming unverified](https://groups.google.com/group/Google_Webmaster_Help-Tools/browse_thread/thread/809674e664cb2db7/d16d20bde9856c5a).
This is not the only reason for a site becoming unverified, but if you notice this on a regular
basis, it would be a good idea to investigate. On this subject, always make sure that Googlebot
is treated the same way as other users from that location, otherwise that might be seen as
[cloaking](/search/blog/2008/06/how-google-defines-ip-delivery).

## Is your server unreachable when we try to crawl?

It can happen to the best of sites—servers can go down and firewalls can be overly protective. If
that happens when Googlebot tries to access your site, we won't be able crawl the website and you
might not even know that we tried. Luckily, we keep track of these issues and you can spot
["Network unreachable" and "robots.txt unreachable" errors](https://groups.google.com/group/Google_Webmaster_Help-Indexing/browse_thread/thread/5cb4db2a6e349c2e)
in your Webmaster Tools account when we can't reach your site.

## Has your website been hacked?

Hackers sometimes add strange, off-topic hidden content and links to questionable pages. If it's
hidden, you might not even notice it right away; but nonetheless, it can be a big problem. While
the Message Center may be able to give you a warning about some kinds of hidden text, it's best
if you also keep an eye out yourself. Google Webmaster Tools can
[show you keywords from your pages in the "What Googlebot sees" section](https://groups.google.com/group/Google_Webmaster_Help-Tools/browse_thread/thread/9afe82fed4b9e2ee/),
so you can often spot a hack there. If you see totally irrelevant keywords, it would be a good
idea to investigate what's going on. You might also try setting up
[Google Alerts](https://www.google.com/alerts)
or doing queries such as `site:example.com spammy words`, where
`spammy words` might be words like porn, viagra, tramadol, sex or other words that your
site wouldn't normally show. If you find that your site actually was hacked, I'd recommend going
through our blog post about
[things to do after being hacked](/search/blog/2008/04/my-sites-been-hacked-now-what).

There are a lot of issues that can be recognized with Webmaster Tools; these are just some of the
more common ones that we've seen lately. Because it can be really difficult to recognize some of
these problems, it's a great idea to check your Webmaster Tools account to make sure that you
catch any issues before they become real problems. If you spot something that you absolutely can't
pin down, why not post in the
[discussion group](https://support.google.com/webmasters/community)
and ask the experts there for help?

Have you checked your site lately?
