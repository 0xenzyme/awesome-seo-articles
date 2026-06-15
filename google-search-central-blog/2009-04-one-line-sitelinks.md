---
title: "One-line sitelinks"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-04-one-line-sitelinks"
url: "https://developers.google.com/search/blog/2009/04/one-line-sitelinks"
canonical: "https://developers.google.com/search/blog/2009/04/one-line-sitelinks"
author: "Doantam Phan, Software Engineer, and Raj Krishnan, Product Manager, Sitelinks Team"
published: "2009-04-16T00:00:00+00:00"
updated: "2009-04-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:57:42+00:00"
status_code: 200
html_hash: "56c8de4c409fcc199be5904e7fd5c0010b50c35bd8b517cad855ace088d4cd8f"
clean_word_count: 567
clean_char_count: 3456
---
# One-line sitelinks

You may be familiar with [sitelinks](/search/docs/appearance/sitelinks),
the links that show up underneath the first search result and which lead to specific pages deeper
within the site. Sitelinks enable users to jump directly to important parts of a site, which is
often useful for large, complex websites. Sitelinks have the additional advantage of giving
users an overview of a website's content by highlighting some of the popular parts of the site.
For webmasters, sitelinks are also beneficial because they help to expose parts of your site that
users may not know about. For instance, a search for
[NASA](https://www.google.com/search?q=NASA)
provides links to a
[gallery of images](https://www.nasa.gov/multimedia/imagegallery/iotd),
a
[page about Space Shuttle and ISS missions](https://www.nasa.gov/topics/shuttle_station/index),
and so on:

![search result with two columns of sitelinks](/static/search/blog/images/import/bb6823199af3c625091ecfda6506d9fc.png)

Until now, sitelinks have only ever appeared on the first search result, and so at most one site
could have sitelinks per query. We're now launching an expansion of sitelinks: a single row of
links can now appear for results that didn't show sitelinks before, even for results that aren't
in the first position. This means multiple results on one query can now have sitelinks. Up to four
sitelinks can show up right above the page URL, instead of the usual two columns below the URL
of the first result.
[Here's an example](https://www.google.com/search?q=nutrition)
where the first three results each have one-line sitelinks:

![search result with a single line of sitelinks](/static/search/blog/images/import/d0dbcb36521f1bd4ea39c2e23393413c.png)

These one-line sitelinks have many of the same benefits as the full two-column sitelinks, but on
a smaller scale: they show users some relevant sub-pages in the site and give an idea of what the
site is about. Comparing the sitelinks that appear for each result can even illustrate the
difference between the sites. Just like regular sitelinks, one-line sitelinks are generated
algorithmically and the decisions on when to show them and which links to display are entirely
based on the expected benefit to users.

For webmasters, this new feature means it's possible that your site will start showing sitelinks
for a number of queries where it previously didn't. We expect this will increase the visibility of
and traffic to your site, while also improving the experience of users. If, however, you
absolutely would prefer not to have a particular sitelink show up, remember that you can always
block a page from appearing as a sitelink for 90 days through
[Webmaster Tools](https://search.google.com/search-console).
In fact, as part of our ongoing efforts at improving the Webmaster Tools experience, we're
speeding up our response time to blocked pages, so you should see a blocked page get dropped as a
sitelink even faster than before. If you need a quick refresher on how to use the sitelink
blocking tool, take a look at
[this previous blog post](/search/blog/2007/10/webmasters-can-now-provide-feedback-on).
Currently you can only block sitelinks on your site's home page, but we're working on expanding
this capability so you'll soon be able to remove them from any other page as well.

We hope you find these improvements to sitelinks and Webmaster Tools helpful for both your site
and your visitors!
