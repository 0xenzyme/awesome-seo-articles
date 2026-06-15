---
title: "Unexpected Common Words"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-02-unexpected-common-words"
url: "https://developers.google.com/search/blog/2006/02/unexpected-common-words"
canonical: "https://developers.google.com/search/blog/2006/02/unexpected-common-words"
author: "Andrey Stroilov, Google Engineering"
published: "2006-02-07T00:00:00+00:00"
updated: "2006-02-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:44:49+00:00"
status_code: 200
html_hash: "0fe50a72d83fe219986d6b5f96b31dba399d43cc0facce0c25ac58810993958d"
clean_word_count: 312
clean_char_count: 1918
---
# Unexpected Common Words

The new features released yesterday include a list of common words in your site's content and in
external links to your site. In some cases, these common words may not match what you expect from
your current content. The common words are calculated based on the results of the Googlebot
crawler. This can affect the data in a number of ways:

- **Googlebot hasn't crawled all pages on your site.** If words on particular pages
  are missing, make sure that those pages are being successfully crawled. If those pages are not
  yet in your sitemap, adding them will help guide Googlebot to those portions of your site. Also,
  make sure that you link to the pages of your site from within your site (for instance, by using
  an HTML site map).
- **Your site has changed since we last crawled it.** If you have just redesigned
  your site, made significant content changes to an existing site, or purchased an existing domain
  and changed the contents, the data will not be updated until Googlebot has successfully crawled
  the new or changed pages.
- **Googlebot is unable to re-crawl modified pages.** Googlebot may be unable to
  access your server due to network error, or may encounter a server error when trying to load
  your pages. Make sure that your server is responding properly to incoming requests.
- **Your site is not being crawled.** New sites may take some time to be fully
  crawled. Read through our
  [information for webmasters](/search/docs/fundamentals/how-search-works) for more
  information about our crawling processes. Also, make sure your site doesn't violate the
  [Webmaster Guidelines](/search/docs/essentials).

If you are seeing unexpected data and none of these apply to you, please let us know by posting
in our
[Google Group](https://support.google.com/webmasters/community).
We always appreciate user feedback and are working to improve Google Sitemaps.
