---
title: "Dealing with Sitemap cross-submissions"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2007-10-dealing-with-sitemap-cross-submissions"
url: "https://developers.google.com/search/blog/2007/10/dealing-with-sitemap-cross-submissions"
canonical: "https://developers.google.com/search/blog/2007/10/dealing-with-sitemap-cross-submissions"
author: "Mickey Kataria, Google Zürich"
published: "2007-10-25T00:00:00+00:00"
updated: "2007-10-25T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:50:30+00:00"
status_code: 200
html_hash: "095843b0ac8947f1102b8533126249dcb23094d3557cbb37e0b2b96ed83cba4a"
clean_word_count: 354
clean_char_count: 2264
---
# Dealing with Sitemap cross-submissions

Since the
[launch of Sitemaps](https://googleblog.blogspot.com/2005/06/webmaster-friendly.html),
webmasters have been asking if they could submit their Sitemaps for multiple hosts on a single
dedicated host. A fair question—and now you can!

Why would someone want to do this? Let's say that you own www.example.com and mysite.google.com
and you have Sitemaps for both hosts, for example, sitemap-example.xml and sitemap-mysite.xml.
Until today, you would have to store each Sitemap on its respective host. If you tried to place
sitemap-mysite.xml on www.example.com, you would
[get an error](https://www.google.com/support/webmasters/bin/answer.py?answer=35143)
because, for security reasons, a Sitemap on www.example.com can only contains URLs from
www.example.com. So how do we solve this? Well, if you can "prove" that you own or control both
of these hosts, then either one can host a Sitemap containing URLs for the other. Just follow the
normal
[verification process](https://support.google.com/webmasters/answer/34592)
in
[Google Webmaster Tools](https://search.google.com/search-console)
and any verified site in your account will be able to host Sitemaps for any other verified site
in the same account.

Here is an example showing both sites verified:

![webmaster tools dashboard](/static/search/blog/images/import/8a968ca6d9764414c331c34ff7d0d52b.jpg)

And now, from a single host, you can submit Sitemaps for both sites without any errors.
*sitemap-example.xml* contains URLs from www.example.com and *sitemap-mysite.xml*
contains URLs from mysite.google.com but both now reside on www.example.com:

![sitemap cross submission in webmaster tools](/static/search/blog/images/import/b836795405824fef3cdac2bc0be11a6d.jpg)

We've also added more information on
[handling cross-submits](/search/docs/advanced/sitemaps/large-sitemaps) in our
[Webmaster Help Center](https://www.google.com/support/webmasters).

For those of you wondering how this affects the other search engines that support the Sitemap
Protocol, rest assured that we're talking to them about how to make cross-submissions work
seamlessly across all of them. Until then, this specific solution will work only for users of
Google Webmaster Tools.
