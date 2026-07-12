---
title: "How to move your content to a new location"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-04-how-to-move-your-content-to-new"
url: "https://developers.google.com/search/blog/2012/04/how-to-move-your-content-to-new"
canonical: "https://developers.google.com/search/blog/2012/04/how-to-move-your-content-to-new"
author: "Fili Wiese, Kaspar Szymanski"
published: "2012-04-25T00:00:00+00:00"
updated: "2012-04-25T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:18:47+00:00"
status_code: 200
html_hash: "ccce5166122504b65c4cff11be8e233ac746dbe61370dc0b1401e291ffbcd8ee"
clean_word_count: 672
clean_char_count: 4349
---
# How to move your content to a new location

While maintaining a website, webmasters may decide to move the whole website or parts of it to a
new location. For example, you might move content from a subdirectory to a subdomain, or to a
completely new domain. Changing the location of your content can involve a bit of effort, but it's
worth doing it properly.

To help search engines understand your new site structure better and make your site more
user-friendly, make sure to follow these guidelines:

- It's important to redirect all users and bots that visit your old content location to the new
  content location using
  [`301` redirects](/search/docs/crawling-indexing/301-redirects).
  To highlight the relationship between the two locations, make sure that each old URL points to
  the new URL that hosts similar content. If you're unable to use `301` redirects, you
  may want to consider using
  [cross domain canonicals](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  for search engines instead.
- Check that you have both the
  [new and the old location verified](https://support.google.com/webmasters/answer/9008080)
  in the same Google Webmaster Tools account.
- Make sure to check if the new location is crawlable by Googlebot using the
  [Fetch as Googlebot](https://support.google.com/webmasters/answer/9128668)
  feature. It's important to make sure Google can actually access your content in the new
  location. Also make sure that the old URLs are not blocked by a robots.txt disallow rule,
  so that the redirect or `rel=canonical` can be found.
- If you're moving your content to an entirely new domain, use the
  [Change of address](https://support.google.com/webmasters/answer/9370220)
  option under Site configuration in Google Webmaster Tools to let us know about the change.
  ![Change of address option in Google Webmaster Tools](/static/search/blog/images/import/c074e96a5906249fc2a19006d07bda0d.png)
- If you've also changed your site's URL structure, make sure that it's possible to navigate it
  without running into
  [`404` error pages](/search/docs/crawling-indexing/http-network-errors).
  Google Webmaster Tools may prove useful in investigating
  [potentially broken links](/search/blog/2012/03/crawl-errors-next-generation).
  Just look for
  [Crawl errors](https://support.google.com/webmasters/bin/answer.py?answer=35120)
  for your new site.
- Check your [Sitemap](/search/docs/crawling-indexing/sitemaps/overview) and verify that it's up
  to date.
- Once you've set up your
  [`301` redirects](/search/docs/crawling-indexing/301-redirects), you
  can keep an eye on users to your
  [`404` error pages](/search/docs/crawling-indexing/http-network-errors)
  to check that users are being redirected to new pages, and not accidentally ending up on broken
  URLs. When a user comes to a `404` error page on your site, try to identify which URL
  they were trying to access, why this user was not redirected to the new location of your
  content, and then make changes to your `301` redirect rules as appropriate.
- Have a look at the
  [Links to your site](https://support.google.com/webmasters/bin/answer.py?answer=55281)
  in Google Webmaster Tools and inform the important sites that link to your content about your
  new location.
- If your site's content is specific to a particular region you may want to double check the
  [geotargeting](https://support.google.com/webmasters/bin/answer.py?answer=62399)
  preferences for your new site structure in Google Webmaster Tools.
- As a general rule of thumb, try to avoid running two crawlable sites with completely or largely
  identical content without a `301` redirection or specifying a
  [`rel="canonical"`](/search/docs/crawling-indexing/consolidate-duplicate-urls).
- Lastly, we recommend not implementing other major changes when you're moving your content to a
  new location, like large-scale content, URL structure, or navigational updates. Changing too
  much at once may confuse users and search engines.

We hope you find these suggestions useful. If you happen to have further questions on how to move
your content to a new location we'd like to encourage you to drop by our
[Google Webmaster Help Forum](https://groups.google.com/a/googleproductforums.com/forum/#%21forum/webmasters)
and seek advice from expert webmasters.
