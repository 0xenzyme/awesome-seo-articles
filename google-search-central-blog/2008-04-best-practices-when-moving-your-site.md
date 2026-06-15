---
title: "Best practices when moving your site"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-04-best-practices-when-moving-your-site"
url: "https://developers.google.com/search/blog/2008/04/best-practices-when-moving-your-site"
canonical: "https://developers.google.com/search/blog/2008/04/best-practices-when-moving-your-site"
author: "Rïona MacNamara, Webmaster Tools Team"
published: "2008-04-16T00:00:00+00:00"
updated: "2008-04-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T12:52:06+00:00"
status_code: 200
html_hash: "7abdd8e47017e8c8bc84e91d55b7023cd16a9b058440bb692477c4fec3273cc2"
clean_word_count: 716
clean_char_count: 4227
---
# Best practices when moving your site

Planning on moving your site to a new domain? Lots of webmasters find this a scary process. How do
you do it without hurting your site's performance in Google search results?

![moving your site](/search/blog/images/archived_moving.JPG)

Your aim is to make the transition invisible and seamless to the user, and to make sure that
Google knows that your new pages should get the same quality signals as the pages on your own
site. When you're moving your site, pesky `404 (File Not Found)` errors can harm the user experience
and negatively impact your site's performance in Google search results.

Let's cover moving your site to a new domain (for instance, changing from
`www.example.com` to `www.example.org`). This is different from moving to a
new IP address; read
[this post](/search/blog/2008/01/feeling-lucky-at-pubcon) for more information on that.

Here are the main points:

- Test the move process by moving the contents of one directory or subdomain first. Then use a
  [`301` Redirect](https://en.wikipedia.org/wiki/301_redirect)
  to permanently redirect those pages on your old site to your new site. This tells Google and
  other search engines that your site has permanently moved.
- Once this is complete, check to see that the pages on your new site are appearing in Google's
  search results. When you're satisfied that the move is working correctly, you can move your
  entire site. Don't do a blanket redirect directing all traffic from your old site to your new
  home page. This will avoid `404` errors, but it's not a good user experience. A
  page-to-page redirect (where each page on the old site gets redirected to the corresponding page
  on the new site) is more work, but gives your users a consistent and transparent experience. If
  there won't be a 1:1 match between pages on your old and new site, try to make sure that every
  page on your old site is at least redirected to a new page with similar content.
- If you're changing your domain because of site rebranding or redesign, you might want to think
  about doing this in two phases: first, move your site; and second, launch your redesign. This
  manages the amount of change your users see at any stage in the process, and can make the
  process seem smoother. Keeping the variables to a minimum also makes it easier to troubleshoot
  unexpected behavior.
- Check both
  [external and internal links to pages on your site](https://support.google.com/webmasters/answer/9049606).
  Ideally, you should contact the webmaster of each site that links to yours and ask them to
  update the links to point to the page on your new domain. If this isn't practical, make sure
  that all pages with incoming links are redirected to your new site. You should also check
  internal links within your old site, and update them to point to your new domain. Once your
  content is in place on your new server, use a link checker like
  [Xenu](https://home.snafu.de/tilman/xenulink.html)
  to make sure you don't have broken legacy links on your site. This is especially important if
  your original content included absolute links (like
  `https://www.example.com/cooking/recipes/chocolatecake.html`) instead of relative
  links (like `.../recipes/chocolatecake.html`).
- To prevent confusion, it's best to make sure you retain control of your old site domain for at
  least 180 days.
- [Add your new site to your Webmaster Tools account, and verify your ownership of it](https://support.google.com/webmasters/answer/34592).
  Then create and submit a [Sitemap](/search/docs/crawling-indexing/sitemaps/overview)
  listing the URLs on your new site. This tells Google that your content is now available on your
  new site, and that we should go and crawl it.
- Finally, keep both your new and old site verified in Webmaster Tools, and review
  [crawl errors](https://support.google.com/webmasters/answer/7440203)
  regularly to make sure that the `301` errors from the old site are working properly, and that the new
  site isn't showing unwanted `404` errors.

We'll admit it, moving is never easy - but these steps should help ensure that none of your good
web reputation falls off the truck in the process.
