---
title: "FYI on Google Toolbar's latest features"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-12-fyi-on-google-toolbars-latest-features"
url: "https://developers.google.com/search/blog/2007/12/fyi-on-google-toolbars-latest-features"
canonical: "https://developers.google.com/search/blog/2007/12/fyi-on-google-toolbars-latest-features"
author: "John Mueller"
published: "2007-12-14T00:00:00+00:00"
updated: "2007-12-14T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:51:00+00:00"
status_code: 200
html_hash: "ff30bcf829d87b372bc8652919169bb69beece131241e0437d903b2f336a4f63"
clean_word_count: 1020
clean_char_count: 6101
---
# FYI on Google Toolbar's latest features

The latest version of
[Google Toolbar for Internet Explorer (beta)](https://toolbar.google.com/T5/intl/en/index.html)
just added a neat feature to help users arrive at your website, or at least see your content, even
when things go awry.

It's frustrating for your users to mistype your URL and receive a generic
`404 - Not Found` or try to access a part of your site that might be down.

Regardless of your site being
[useful and information-rich](/search/docs/essentials#design), when these issues arise,
most users just move on to something else. The latest release of Google Toolbar, however, helps
users by detecting site issues and providing alternatives.

Website Optimi**z**er or Website Optimi**s**er? The Toolbar can help you find it even if
you try "google.cmo" instead of "google.com".

![Google Toolbar link correction feature](/static/search/blog/images/import/49b2387a573b71279379cd3cb3b380aa.gif)

## 3 site issues detected by Google Toolbar

1. **`404` errors with default error pages**: When a visitor tries to reach your
   content with an invalid URL and your server returns a short, default error message (less than
   512 bytes), the Toolbar will suggest an alternate URL to the visitor. If this is a general
   problem in your website, you will see these URLs also listed in the crawl errors section of your
   Webmaster Tools account.
   If you choose to set up a custom error page, make sure it returns result code `404`.
   The content of the `404` page can help your visitors to understand that they tried
   to reach a missing page and provides suggestions regarding how to find the content they were
   looking for. When a site displays a custom error page the Toolbar will no longer provide
   suggestions for that site. You can check the behavior of the Toolbar by visiting an invalid URL
   on your site with the Google Toolbar installed.
2. **DNS errors**: When a URL contains a non-existent domain name (like www.google.cmo), the
   Toolbar will suggest an alternate, similar looking URL with a valid domain name.
3. **Connection failures**: When your server is unreachable, the Google Toolbar will
   automatically display a link to the cached version of your page. This feature is only available
   when Google is not explicitly forbidden from caching your pages through use of a
   [robots `meta` tag](/search/docs/crawling-indexing/robots-meta-tag)
   or crawling is blocked on the page through the
   [robots.txt file](/search/docs/crawling-indexing/robots/intro). If your server is
   regularly unreachable, you will probably want to fix that first; but it may also be a good idea
   to check the Google cache for your pages by looking at the search results for your site.

### Suggestions provided by the Google Toolbar

When one of the above situations is found, the Toolbar will try to find the most helpful links
for the user. That may include:

- **A link to the corrected URL**: When the Toolbar can find the most probable, active URL to
  match the user's input (or link they clicked on), it will display it right on top as a
  suggestion. The correction can be somewhere in the domain name, the path or the file name (the
  Toolbar does not look at any parameters in the URL).
- **A link to the cached version of the URL**: When Toolbar recognizes the URL in the Google
  cache, it will display a link to the cached version. This is particularly useful when the user
  can't access your pages for some reason. As mentioned above, Google may cache your URLs provided
  you're not explicitly forbidding this through use of a
  [robots `meta` tag](/search/docs/crawling-indexing/robots-meta-tag) or the
  [robots.txt file](/search/docs/crawling-indexing/robots/intro).
- **A link to the home page or HTML sitemap of your site**: Sometimes going to the home page or
  an HTML sitemap page is the best way to find the page that a user is really looking for. HTML
  sitemap pages (these are not
  [XML Sitemap files](/search/docs/crawling-indexing/sitemaps/overview)) are generally
  recognized based on the filename; if the Toolbar can find something called "sitemap" or similar,
  this page will probably be recognized as the HTML sitemap page. Don't worry if your HTML sitemap
  page is called something else; if a user decides to go to your home page, they'll probably find
  it right away even if the Toolbar doesn't spot it.
- **A link to a higher level folder**: Sometimes the home page or HTML sitemap page is too far
  out and the user would be better off just going one step up in the hierarchy. When the Toolbar
  can recognize that your site's structure is based on folders and sub-folders, it may suggest a
  page one step back.
- **A search within your site for keywords found in the URL**: It's a good practice to use
  descriptive URLs. If the Toolbar can recognize keywords within the URL which the user tried to
  access, it will link to a site-search with those keywords. Even if the URL has changed
  significantly in the meantime, the search may be able to find similar content based on those
  keywords. For instance, if the URL was `https://example.com/party-gifts/holidays/`
  it will suggest a search for the words "party",
  "gifts", and "holidays" within the site
  `example.com`.
- **An open Google search box**: If all else fails, there's always a chance that similar
  content already exists elsewhere on the web. The Google web search can help your users to find
  it—the Toolbar will help you by adding the keywords found in the URL to the search box.

Are you curious already?
[Download the Google Toolbar](https://toolbar.google.com/)
for your browser and give it a try on your site!

To discuss how this feature can help visitors to your site, jump in to our
[Google Webmaster Help Group](https://support.google.com/webmasters/community);
or for general Google Toolbar questions, try the
[Toolbar group for Internet Explorer](https://groups.google.com/group/IEToolbar-Group/topics?start=)
or the
[Toolbar group for Firefox](https://groups.google.com/group/FFToolbar-Group/topics).
