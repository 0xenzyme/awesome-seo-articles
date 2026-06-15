---
title: "Sitemap Submission Made Simple"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2008-12-sitemap-submission-made-simple"
url: "https://developers.google.com/search/blog/2008/12/sitemap-submission-made-simple"
canonical: "https://developers.google.com/search/blog/2008/12/sitemap-submission-made-simple"
author: "John Mueller"
published: "2008-12-18T00:00:00+00:00"
updated: "2008-12-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:56:17+00:00"
status_code: 200
html_hash: "abb6cc6cb5d6538aa0c90cc069cd1eba7301e73149ce8302fe6a625907b19f7e"
clean_word_count: 1182
clean_char_count: 7247
---
# Sitemap Submission Made Simple

Submitting a [Sitemap](https://www.sitemaps.org/index.html) to
Google just became even easier. No longer do you have to specify the Sitemap file type—we'll
determine the type of data you're submitting automatically. Let's take a quick look at the kinds
of Sitemap files we support as well as the ways they can be submitted to us.

![A sample Webmaster Tools account with Sitemaps](/static/search/blog/images/import/cfc4f4bf6e0257089def67bb7a862ef9.png)

## Sitemap file formats supported by Google

Part of what makes the web so interesting is that there are so many different kinds of content out
there. Do you use videos on your website? If so, send us a Video Sitemap file so that we can send
you visitors to those videos! Do you host source-code samples? Submit a Code Search Sitemap! Here
are the various kinds of Sitemap files that Google supports at the moment:

- [XML Sitemap files for web pages](https://www.sitemaps.org/index.html)
  —Use these files to submit all of your web pages (this is the preferred format for web
  pages). While not all search engines may support the Sitemap types listed below, the XML Sitemap
  for web pages is supported by all search engines of
  [sitemaps.org](https://www.sitemaps.org/index.html).
- [RSS 2.0](https://cyber.law.harvard.edu/rss/rss) and
  [Atom 1.0](https://www.ietf.org/rfc/rfc4287.txt)
  feeds for web pages—Many blogs create these automatically.
- [Text files with web page URLs](/search/docs/crawling-indexing/sitemaps/build-sitemap#2)
  —If you can't automatically create one of the above formats, you can create a text file
  with your URLs in it.
- [XML Sitemap files for Video Search](/search/docs/crawling-indexing/sitemaps/video-sitemaps)
  —Videos on your website can be indexed and made available for
  [Google Video](https://video.google.com/) Search.
- [Media-RSS feeds](https://search.yahoo.com/mrss) for Video
  Search—mRSS feeds are used by various other systems, we can use these for
  [Google Video](https://video.google.com/) Search as well.
- [XML Sitemap files for Google Code Search](https://www.google.com/support/webmasters/bin/answer.py?answer=75224)
  —If you make programming samples or code available to your users, you can submit these for
  [Google Code Search](https://www.google.com/codesearch).
- [XML Sitemap files for mobile web pages](https://www.google.com/support/webmasters/bin/answer.py?answer=34648)
  —Using this kind of format allows us to recognize content that has been optimized for
  mobile devices (please note that there was recently a small change in the format).
- [XML Sitemap files for geo-data](https://www.google.com/support/webmasters/bin/answer.py?answer=94554)
  —If you have geographic data on your website in the form of
  [KML](https://code.google.com/apis/kml/documentation/) or
  [GeoRSS](https://georss.org/) files, please let us know about
  these files.
- [XML Sitemap files for News](/search/docs/crawling-indexing/sitemaps/news-sitemap)—News
  websites can submit their news content in this special Sitemap format (please note that you must
  first
  [register with Google News](https://www.google.com/support/news_pub/bin/answer.py?answer=40787)
  before these files are processed).

If you have multiple Sitemap files that you wish to submit to Google, you can include up to 1,000
of these in an
[XML Sitemap Index file](/search/docs/crawling-indexing/sitemaps/large-sitemaps). If you
have more than 1,000 Sitemap files, you can just submit multiple Sitemap Index files—we'd
love to take them all!

## Submitting your Sitemap files to Google

Once you have your Sitemap files ready and available on your server, all that's left is making
sure that the search engines can find them. Google supports three simple ways to submit Sitemap
files:

- Using
  [Google Webmaster Tools](https://search.google.com/search-console)
  —Submitting your Sitemap files through Google Webmaster Tools is the preferred way of
  letting us know about them. The main advantage of doing it this way is that you'll always have
  direct feedback about how your Sitemap files were downloaded (were we able to reach your
  server?), how they were recognized (were they in the right format?) and what happened to the
  web pages listed in them (how many were indexed?). To submit your Sitemap files, make sure
  that your website is
  [verified in Webmaster Tools](https://support.google.com/webmasters/answer/34592),
  then go to "Sitemaps" in Webmaster Tools and enter the file name of your Sitemap(s).

  Sometimes it makes sense to keep your Sitemap file on a different server / domain name. To
  submit Sitemap files like that, you must
  [verify ownership](https://support.google.com/webmasters/answer/34592)
  of both sites in Webmaster Tools and submit the Sitemap on the appropriate site. For instance,
  if your Sitemap file for `https://www.example.com` is kept on
  `https://sitemap-files.example.com/` then you need to verify ownership of both
  sites and then submit the Sitemap file under `https://sitemap-files.example.com`
  (even though the URLs listed in it are for `https://www.example.com`). For more
  information, please see our Help Center topic on
  [submitting Sitemap files for multiple sites](/search/docs/crawling-indexing/sitemaps/large-sitemaps).
- Listing Sitemap files in the robots.txt file—Another way of submitting a Sitemap file is
  to
  [specify the URL in your robots.txt file](/search/docs/crawling-indexing/sitemaps/overview).
  If you use this method of submitting a Sitemap file, it will be found by all search engines
  that support the Sitemaps protocol (although not all of them support the extensions listed
  above). Since you can specify the full URL of your Sitemap file in the robots.txt file, this
  method also allows you to store your Sitemap file on a different domain. Keep in mind that while
  Sitemap files submitted this way are processed on our side, they will not be automatically
  listed in your Webmaster Tools account. In order to receive feedback on your files, we recommend
  adding them manually to your account as well.
- Using an
  [HTTP "ping"](https://www.google.com/support/webmasters/bin/answer.py?answer=34609)
  —If your Sitemap files are generated automatically, a convenient way to submit (and
  re-submit) them is to access the "ping" URL for Google Sitemaps. This URL includes the URL of
  your Sitemap file. For more information on the "ping" URL for your website, please see the
  [Help Center article on Updating a Sitemap](https://www.google.com/support/webmasters/bin/answer.py?answer=34609).
  You can "ping" this URL whenever you update your Sitemap file—we'll know to pick it up
  and process it again. If you also have your Sitemap file registered in Webmaster Tools, we'll
  update the status there as well. This method is also valid if your Sitemap file is kept on a
  different server, but you must still verify both sites in Webmaster Tools as previously
  mentioned.

  Search engines that are a members of
  [sitemaps.org](https://www.sitemaps.org/index.html)
  support a similar way of submitting general web Sitemap files.

We hope these simplifications make it even easier for you to send us your Sitemap files!
