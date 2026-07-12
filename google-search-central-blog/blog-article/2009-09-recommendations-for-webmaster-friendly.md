---
title: "Recommendations for webmaster friendly hosting services"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-09-recommendations-for-webmaster-friendly"
url: "https://developers.google.com/search/blog/2009/09/recommendations-for-webmaster-friendly"
canonical: "https://developers.google.com/search/blog/2009/09/recommendations-for-webmaster-friendly"
author: "Greg Grothaus"
published: "2009-09-14T00:00:00+00:00"
updated: "2009-09-14T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:00:42+00:00"
status_code: 200
html_hash: "b74d0ade111fe6628c55c20659bfbd3d04cd9b0ad27e8a2315968d376365e1d8"
clean_word_count: 933
clean_char_count: 5934
---
# Recommendations for webmaster friendly hosting services

Most of the recommendations we've made in the past are for individual webmasters running their
own websites. We thought we'd offer up some best practices for websites that allow users to
create their own websites or host users' data, like
[Blogger](https://blogger.com/) or
[Google Sites](https://sites.google.com/).

- **Make sure your users can verify their website in website management suites such as
  Google's Webmaster Tools.**
  Webmaster Tools provides your users with detailed reports about their website's visibility in
  Google. Before we can grant your users access, we need to verify that they own their
  particular websites.
  [Verifying ownership of a site in Webmaster Tools](https://support.google.com/webmasters/answer/34592)
  can be done using a custom
  [HTML file](https://www.google.com/support/webmasters/bin/answer.py?answer=35658),
  a
  [`meta` tag](https://www.google.com/support/webmasters/bin/answer.py?answer=35659),
  or seamless integration in your system via
  [Google Services for Websites](/search/blog/2009/08/new-tools-for-google-services-for).
  Other website management suites such as
  [Yahoo! Site Explorer](https://siteexplorer.search.yahoo.com/)
  and
  [Bing Webmaster Tools](https://www.bing.com/toolbox/webmasters/)
  may use similar verification methods; we recommend making sure your users can access each of
  these suites.
- **Choose a unique directory or hostname for each user.**
  Webmaster Tools verifies websites based on a single URL, but assumes that users should be
  able to see data for all URLs 'beneath' this URL in the site URL hierarchy. See our article on
  [verifying subdomains and subdirectories](https://www.google.com/support/webmasters/bin/answer.py?answer=35163)
  for more information. Beyond Webmaster Tools, many automated systems on the web—such as
  search engines or aggregators—expect websites to be structured in this way, and by doing
  so you'll be making it easier for those systems to find and organize your content.
- **Set useful and descriptive page titles.**
  Let users set their own titles, or automatically set the pages on your users' websites to be
  descriptive of the content on that page. For example, all of the user page titles should not
  be "Blogger: Create your free blog". Similarly, if a user's website has more than one page
  with different content, they should not all have the same title: "User XYZ's home page".
- **Allow the addition of tags to a page.**
  Certain `meta` tags are reasonably useful for search engines and users may want to control
  them. These include tags with the `name` attribute of
  [`robots`](/search/blog/2007/03/using-robots-meta-tag),
  [`description`](/search/blog/2007/09/improve-snippets-with-meta-description),
  [`googlebot`](https://www.google.com/support/webmasters/bin/answer.py?answer=35264),
  [`slurp`](https://help.yahoo.com/l/au/yahoo7/search/indexing/indexing-11.html),
  `msnbot`. Click on the specific name attributes to learn more about what these tags
  do.
- **Allow your users to use third-party analytics packages such as Google Analytics.**
  [Google Analytics](https://analytics.google.com/) is an
  enterprise-class analytics software that can run on a website by just adding a snippet of
  JavaScript to the page. If you don't want to allow users to add arbitrary JavaScript for
  security reasons, the Google Analytics code only changes by one simple ID. If your let your
  users tell you their Google Analytics ID, you can set up the rest for them. Users get more
  value out of your service if they can understand their traffic better. For example, see
  [Weebly's support page](https://www.weebly.com/support/index.php?pg=kb.page&id=23)
  on adding Google Analytics. We recommend considering similar methods you can use for enabling
  access to other third-party applications.
- **Help your users move around.**
  Tastes change. Someone on your service might want to change their account name or
  even move to another site altogether. Help them by
  [allowing them to access their own data](https://www.mattcutts.com/blog/not-trapping-users-data-good/)
  and by letting them tell search engines when they move part or all of their site via the use
  of [`301` redirect destinations](/search/docs/crawling-indexing/301-redirects).
  Similarly, if users want to remove a page/site instead of moving it, please return a
  [`404` HTTP response code](/crawling/docs/troubleshooting/http-status-codes#4xx-client-errors)
  so that search engines will know that the page/site is no longer around. This allows users to
  use the
  [urgent URL removal tool](https://www.google.com/support/webmasters/bin/answer.py?answer=92865)
  (if necessary), and makes sure that these pages drop out of search results as soon as possible.
- **Help search engines find the good content from your users.**
  Search engines continue to crawl more and more of the web. Help our crawlers find the best
  content across your site. Allow us to crawl users' content, including media like user-uploaded
  images. Help us find users' content using
  [XML Sitemaps](https://www.sitemaps.org/). Help us to steer
  clear of duplicate versions of the same content so we can find more of the good stuff your
  users are creating by creating only one URL for each piece of content when possible, and by
  [specifying your canonical URLs](/search/blog/2009/02/specify-your-canonical)
  when not. If you're hosting blogs, create RSS feeds that we can discover in
  [Google Blog Search](https://blogsearch.google.com/). If
  your site is down or showing errors, please return `5xx` response codes. This helps
  us avoid indexing lots of "We'll be right back" pages by letting crawlers know that the content
  is temporarily unavailable.

Can you think of any other best practices that you would recommend for sites that host users'
data or pages?
