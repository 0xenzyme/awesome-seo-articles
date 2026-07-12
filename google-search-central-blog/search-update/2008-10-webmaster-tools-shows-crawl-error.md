---
title: "Webmaster Tools shows Crawl error sources"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2008-10-webmaster-tools-shows-crawl-error"
url: "https://developers.google.com/search/blog/2008/10/webmaster-tools-shows-crawl-error"
canonical: "https://developers.google.com/search/blog/2008/10/webmaster-tools-shows-crawl-error"
author: "Jonathan Simon"
published: "2008-10-13T00:00:00+00:00"
updated: "2008-10-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T12:55:22+00:00"
status_code: 200
html_hash: "df71c10b7678e704249a102405fba6da028845456c5fe0fe6a331629ecb06190"
clean_word_count: 432
clean_char_count: 2630
---
# Webmaster Tools shows Crawl error sources

Ever since we released the [crawl errors](/search/blog/2006/08/more-webmaster-tools)
feature in
[Webmaster Tools](https://search.google.com/search-console),
webmasters have asked for the sources of the URLs causing the errors. Well, we're listening! We
know it was difficult for those of you who wanted to identify the cause of a particular "Not
found" error, in order to prevent it in the future or even to request a correction, without
knowing the source URL. Now, Crawl error sources makes the process of tracking down the causes
of "Not found" errors a piece of cake. This helps you improve the user experience on your site
and gives you a jump start for
[links week](/search/blog/2008/10/links-information-straight-from-source)
(check out our updated post on
"[Good times with inbound links](/search/blog/2008/10/good-times-with-inbound-links)"
to get the scoop).

In our "Not Found" and "Errors for URLs in Sitemaps" reports, we've added the "Linked From"
column. For every error in these reports, the "Linked From" column now lists the number of pages
that link to a specific "Not found" URL.

![the linked from column in the 404 webmaster tools report shows the number of pages that link to a specific broken url](/static/search/blog/images/import/056e97a62ccf20ae61d19ec951565e97.png)

Clicking on an item in the "Linked From" column opens a separate dialog box which lists each page
that linked to this URL along with the date it was discovered. The source URL for the
`404` can be within or external to your site.

![](/static/search/blog/images/import/ad3700794d209fa1c33e1dfac96b6533.png)
![](/static/search/blog/images/import/6d2a57c532634d424da2e2d46d5b5223.png)

For those of you who just want the data, we've also added the ability to download all your crawl
error sources at once. Just click the "Download all sources of errors on this site" link to
download all your site's crawl error sources.

![](/static/search/blog/images/import/524b9ce46a2b51e0723c5165cb3c4863.png)

Again, if we report crawl errors for your website, you can use crawl error sources to quickly
determine if the cause is from your site or someone else's. You'll have the information you need
to contact them to get it fixed, and if needed, you can still put in place
[redirects on your own site to the appropriate URL](/search/blog/2008/08/now-that-weve-bid-farewell-to-soft-404s).
Just sign in to
[Webmaster Tools](https://search.google.com/search-console)
and check it out for your verified site. You can help people visiting your site—from anywhere on
the web—find what they're looking for.
