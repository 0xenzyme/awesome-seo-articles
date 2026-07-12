---
title: "Watch out for your .yu domain!"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-06-watch-out-for-your-yu-domain"
url: "https://developers.google.com/search/blog/2009/06/watch-out-for-your-yu-domain"
canonical: "https://developers.google.com/search/blog/2009/06/watch-out-for-your-yu-domain"
author: "Written by Luisella Mazza, Search Quality Senior Analyst"
published: "2009-06-24T00:00:00+00:00"
updated: "2009-06-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:59:04+00:00"
status_code: 200
html_hash: "cfb187cdc71c3f994f41850145d8853ddfb7e8a4eab9ffdf15cc68cbd66e1d1c"
clean_word_count: 494
clean_char_count: 2916
---
# Watch out for your .yu domain!

Are you the owner of
[a .yu domain](https://en.wikipedia.org/wiki/.yu)? Then you might
have heard the news: as of September 30,
[all .yu domains will stop working](https://www.nic.yu/index-e),
regardless of their renewal date. This means that any content you're hosting on a .yu domain
will no longer be online. For those of you who would still like to have your site online, we've
prepared some recommendations to make sure that Google keeps crawling, indexing, and serving your
content appropriately.

- **Check your backlinks**. Since it won't be possible to set up a redirection from the old
  .yu domain to your new one, all links pointing to .yu domains will lead to dead ends. This
  means that it will be increasingly difficult for search engines to retrieve your new content.
  To find out who is linking to you, sign up with Google Webmaster Tools and check the
  [links to your site](https://www.google.com/support/webmasters/bin/answer.py?answer=55281)
  (you can also download this list as a
  "comma separated value"—.csv—file for ease of use). Then read through the list for
  sites that you recognize as important and contact their webmasters to make sure that they
  update their links to your new website.
- **Check your internal links**. If you are planning to simply move your content in bulk from
  the old to the new site, make sure that the new
  [internal navigation](https://www.google.com/support/webmasters/bin/answer.py?answer=138752)
  is up to date. For example, if you are renaming pages on your site from
  "www.example.yu/home.htm" to "www.example.com/home.htm" make sure that your internal navigation
  reflects such changes to prevent broken links.
- **Start moving the site to your new domain**. It's a good idea to start moving while you can
  still maintain control of your old domain, so don't wait! As mentioned in our
  [best practices when moving your site](/search/blog/2008/04/best-practices-when-moving-your-site),
  we recommend starting by moving a single directory or subdomain, and testing the results before
  completing the move. Remember that you will not be able to keep a `301` redirection
  on your old domain after September 30, so start your test early.

While you're moving your site, you can test how Google crawls and indexes your new site at its
new location by [submitting a Sitemap](/search/docs/crawling-indexing/sitemaps/overview)
via Google Webmaster Tools. Although we may not crawl or index all the pages listed in each
Sitemap, we recommend that you submit one because doing so helps Google understand your site
better. You can read more on this topic in our answers to the most
[frequently asked questions on Sitemaps](/search/blog/2008/01/sitemaps-faqs).
And remember that for any question or concerns we're waiting for you in the
[Google Webmaster Help Forum](https://support.google.com/webmasters/community)!
