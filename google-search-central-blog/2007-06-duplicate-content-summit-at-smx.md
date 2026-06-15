---
title: "Duplicate content summit at SMX Advanced"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-06-duplicate-content-summit-at-smx"
url: "https://developers.google.com/search/blog/2007/06/duplicate-content-summit-at-smx"
canonical: "https://developers.google.com/search/blog/2007/06/duplicate-content-summit-at-smx"
author: "Vanessa Fox"
published: "2007-06-13T00:00:00+00:00"
updated: "2007-06-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:49:06+00:00"
status_code: 200
html_hash: "1d9d234e38884b90e8507a5b7b8585e79ab2edfee4961acdc22d8c4397e649bb"
clean_word_count: 1225
clean_char_count: 7314
---
# Duplicate content summit at SMX Advanced

Last week, I participated in the duplicate content summit at
[SMX Advanced](https://searchmarketingexpo.com/smx_advanced07/).
I couldn't resist the opportunity to show how
[Buffy is applicable to the everday Search marketing world](https://www.vanessafoxnude.com/2007/06/06/buffy-in-duplicate/),
but mostly I was there to get input from you on the duplicate content issues you face and to
brainstorm how search engines can help.

A few months ago, Adam wrote a great post on
[dealing with duplicate content](/search/blog/2006/12/deftly-dealing-with-duplicate-content).
The most important things to know about duplicate content are:

- Google wants to serve up unique results and does a great job of picking a version of your
  content to show if your sites includes duplication. If you don't want to worry about sorting
  through duplication on your site, you can let us worry about it instead.
- Duplicate content doesn't cause your site to be penalized. If duplicate pages are detected, one
  version will be returned in the search results to ensure variety for searchers.
- Duplicate content doesn't cause your site to be placed in the supplemental index. Duplication
  may indirectly influence this however, if links to your pages are split among the various
  versions, causing lower per-page PageRank.

At the summit at SMX Advanced, we asked what duplicate content issues were most worrisome. Those
in the audience were concerned about scraper sites, syndication, and internal duplication. We
discussed lots of potential solutions to these issues and we'll definitely consider these options
along with others as we continue to evolve our toolset. Here's the list of some of the potential
solutions we discussed so that those of you who couldn't attend can get in on the conversation.

## Specifying the preferred version of a URL in the site's Sitemap file

One thing we discussed was the possibility of specifying the preferred version of a URL in a
Sitemap file, with the suggestion that if we encountered multiple URLs that point to the same
content, we could consolidate links to that page and could index the preferred version.

## Providing a method for indicating parameters that should be stripped from a URL during indexing

We discussed providing this in either an interface such as Webmaster Tools on in the site's
robots.txt file. For instance, if a URL contains sessions IDs, the webmaster could indicate the
variable for the session ID, which would help search engines index the clean version of the URL
and consolidate links to it. The audience leaned towards an addition in robots.txt for this.

## Providing a way to authenticate ownership of content

This would provide search engines with extra information to help ensure we index the original
version of an article, rather than a scraped or syndicated version. Note that we do a pretty good
job of this now and not many people in the audience mentioned this to be a primary issue.
However, the audience was interested in a way of authenticating content as an extra protection.
Some suggested using the page with the earliest date, but creation dates aren't always reliable.
Someone also suggested allowing site owners to register content, although that could raise issues
as well, as non-savvy site owners wouldn't know to register content and someone else could take
the content and register it instead. We currently rely on a number of factors such as the site's
authority and the number of links to the page. If you syndicate content, we suggest that you ask
the sites who are using your content to block their version with a robots.txt file as part of the
syndication arrangement to help ensure your version is served in results.

## Making a duplicate content report available for site owners

There was great support for the idea of a duplicate content report that would list pages within a
site that search engines see as duplicate, as well as pages that are seen as duplicates of pages
on other sites. In addition, we discussed the possibility of adding an alert system to this
report so site owners could be notified via email or RSS of new duplication issues (particularly
external duplication).

## Working with blogging software and content management systems to address duplicate content issues

Some duplicate content issues within a site are due to how the software powering the site
structures URLs. For instance, a blog may have the same content on the home page, a permalink
page, a category page, and an archive page. We are definitely open to talking with software
makers about the best way to provide easy solutions for content creators.

In addition to discussing potential solutions to duplicate content issues, the audience had a few
questions.

**If I nofollow a substantial number of my internal links to reduce duplicate content issues,
will this raise a red flag with the search engines?** The number of `nofollow`
links on a site won't raise any red flags, but that is probably not the best method of blocking
the search engines from crawling duplicate pages, as other sites may link to those pages. A better
method may be to block pages you don't want crawled with a robots.txt file.

**Are the search engines continuing the Sitemaps alliance?** We launched
[sitemaps.org](https://www.sitemaps.org/)
in November of last year and have continued to meet regularly since then. In April, we added the
ability for you to let us know about your Sitemap in your robots.txt file. We plan to continue to
work together on initiatives such as this to make the lives of webmasters easier.

**Many pages on my site primarily consist of graphs. Although the graphs are different on each
page, how can I ensure that search engines don't see these pages as duplicate since they don't
read images?** To ensure that search engines see these pages as unique, include unique text on
each page (for instance, a different title, caption, and description for each graph) and include
unique alt text for each image. (For instance, rather than use `alt="graph"`, use
something like `alt="graph that shows Willow's evil trending over time"`.

**I've syndicated my content to many affiliates and now some of those sites are ranking for this
content rather than my site. What can I do?** If you've made your content available without
payment, you may need to enhance and expand the content on your site to make it unique.

**As a searcher, I want to see duplicates in search results. Can you add this as an option?**
We've found that most searchers prefer not to have duplicate results. The audience member in
particular commented that she may not want to get information from one site and would like other
choices, but for that case, other sites will likely not have identical information and therefore
will show up in the results. Bear in mind that you can add the "&filter;=0" parameter to the end
of a Google web search URL to see additional results which might be similar.

I've brought back all the issues and potential solutions that we discussed at the summit back to
my team and others within Google and we'll continue to work on providing the best search results
and expanding our partnership with you, the webmaster. If you have additional thoughts, we'd love
to hear about them!
