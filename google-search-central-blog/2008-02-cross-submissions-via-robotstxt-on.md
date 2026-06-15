---
title: "Cross-submissions via robots.txt on Sitemaps.org"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2008-02-cross-submissions-via-robotstxt-on"
url: "https://developers.google.com/search/blog/2008/02/cross-submissions-via-robotstxt-on"
canonical: "https://developers.google.com/search/blog/2008/02/cross-submissions-via-robotstxt-on"
author: "Prashanth Koppula, Product Manager"
published: "2008-02-28T00:00:00+00:00"
updated: "2008-02-28T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:51:29+00:00"
status_code: 200
html_hash: "60f5056973e2dd9b2e1a1cf4eab15d9ad41a4b4e891dff48494794519d27050d"
clean_word_count: 389
clean_char_count: 2421
---
# Cross-submissions via robots.txt on Sitemaps.org

Last spring, the Sitemaps protocol was expanded to include the
[autodiscovery of Sitemaps using robots.txt](/search/blog/2007/04/whats-new-with-sitemapsorg)
to let us and other search engines supporting the protocol know about your Sitemaps. We
subsequently also announced support for
[Sitemap cross-submissions using Google Webmaster Tools](/search/blog/2007/10/dealing-with-sitemap-cross-submissions),
making it possible to submit Sitemaps for multiple hosts on a single dedicated host. So it was
only time before we took the next logical step of marrying the two and allowing Sitemap
cross-submissions using robots.txt. And today we're doing just that.

We're making it
[easier for webmasters to place Sitemaps for multiple hosts on a single host](https://www.sitemaps.org/protocol.php#sitemaps_cross_submits)
and then letting us know by including the location of these Sitemaps in the appropriate
robots.txt.

How would this work? Say for example you want to submit a Sitemap for each of the two hosts you
own, `www.example.com` and `host2.google.com`. For simplicity's sake, you
may want to host the Sitemaps on one of the hosts, `www.example.com`. For example, if
you have a Content Management System (CMS), it might be easier for you to change your robots.txt
files than to change content in a directory.

You can now exercise the cross-submission support via robots.txt (by letting us know the location
of the Sitemaps):

1. The robots.txt for `www.example.com` would include:

   ```
   Sitemap: https://www.example.com/sitemap-www-example.xml
   ```
2. And similarly, the robots.txt for `host2.google.com` would include:

   ```
   Sitemap: https://www.example.com/sitemap-host2-google.xml
   ```

By indicating in each individual host's robots.txt file where that host's Sitemap lives you are
in essence proving that you own the host for which you are specifying the Sitemap. And by
choosing to host all of the Sitemaps on a single host, it becomes simpler to manage your Sitemaps.

We are making this announcement today on
[Sitemaps.org](https://www.sitemaps.org/index.html) as a joint
effort. To see what our colleagues have to say, you can also check out the blog posts published
by [Yahoo!](https://www.ysearchblog.com/archives/000524) and
[Microsoft](https://blogs.msdn.com/webmaster/archive/2008/02/27/microsoft-to-support-cross-domain-sitemaps.aspx).
