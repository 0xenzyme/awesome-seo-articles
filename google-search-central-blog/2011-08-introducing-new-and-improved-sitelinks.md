---
title: "Introducing new and improved sitelinks"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-08-introducing-new-and-improved-sitelinks"
url: "https://developers.google.com/search/blog/2011/08/introducing-new-and-improved-sitelinks"
canonical: "https://developers.google.com/search/blog/2011/08/introducing-new-and-improved-sitelinks"
author: "Written by Harvey Jones, Software Engineer, and Raj Krishnan, Product Manager, Sitelinks team"
published: "2011-08-16T00:00:00+00:00"
updated: "2011-08-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:14:32+00:00"
status_code: 200
html_hash: "ce4ee0ca2cefec338f9ce4c9f73b0248455900372a9008c2ec58497db8cc2501"
clean_word_count: 676
clean_char_count: 4344
---
# Introducing new and improved sitelinks

This week we launched an
[update to sitelinks](https://googleblog.blogspot.com/2011/08/evolution-of-sitelinks-expanded-and.html)
to improve the organization and quality of our search results. Sitelinks are the two columns of
links that appear under some search results and ads that help users easily navigate deeper into
the site. Sitelinks haven't changed fundamentally: they're still generated and ranked
algorithmically based on the link structure of your site, and they'll only appear if useful for
a particular query.

![A search result with sitelinks as it appeared before the announced change](/static/search/blog/images/import/40d0055579fc07e954000bdb2aea16f1.png)

Here's how we've improved sitelinks with today's launch:

- **Visibility.** The links have been boosted to full-sized text, and augmented with a green
  URL and one line of text snippet, much like regular search results. This increases the
  prominence of both the individual sitelinks and the top site overall, making them easier to
  find.
- **Flexibility.** Until now, each site had a fixed list of sitelinks that would either all
  appear or not appear; there was no query-specific ranking of the links. With today's launch,
  sitelink selection and ranking can change from query to query, allowing more optimized results.
  In addition, the maximum number of sitelinks that can appear for a site has been raised from
  eight to 12, and the number shown also varies by query.
- **Clarity.** Previously, pages from your site could either appear in the sitelinks, in the
  regular results, or both. Now we're making the separation between the top domain and other
  domains a bit clearer. If sitelinks appear for the top result, then the rest of the results
  below them will be from other domains. One exception to this is if the top result for a query
  is a subpart of a domain. For instance, the query
  ["the met exhibitions"](https://www.google.com/search?q=the+met+exhibitions)
  has www.metmuseum.org/special/ as the top result, and its sitelinks are all from within the
  www.metmuseum.org/special section of the site. However, the rest of the results may be from
  other parts of the metmuseum.org domain, like store.metmuseum.org or
  blog.metmuseum.org/alexandermcqueen/about.
- **Quality.** These user-visible changes are accompanied by quality improvements behind the
  scenes. The core improvement is that we've combined the signals we use for sitelinks generation
  and ranking—like the link structure of your site—with our more traditional ranking
  system, creating a better, unified algorithm. From a ranking perspective, there's really no
  separation between "regular" results and sitelinks anymore.

![A search result with sitelinks as it appears after the announced change](/static/search/blog/images/import/a19cf8771777e5db6d3ffc3309a20854.png)

These changes are also reflected in
[Webmaster Tools](https://search.google.com/search-console),
where you can manage the sitelinks that appear for your site. You can now suggest a demotion to
a sitelink if it's inappropriate or incorrect, and the algorithms will take these demotions into
account when showing and ranking the links (although removal is not guaranteed). Since sitelinks
can vary over time and by query, it no longer makes sense to select from a set list of
links—now, you can suggest a demotion of any URL for any parent page. Up to 100 demotions
will be allowed per site. Finally, all current sitelink blocks in Webmaster Tools will
automatically be converted to the demotions system. More information can be found in our
[documentation about sitelinks](/search/docs/appearance/sitelinks).

It's also worth mentioning a few things that haven't changed.
[One-line sitelinks](/search/blog/2009/04/one-line-sitelinks), where sitelinks can
appear as a row of links on multiple results, and
[sitelinks on ads](https://adwords.blogspot.com/2009/11/increasing-choice-and-relevancy-in)
aren't affected. Existing
[best practices](/search/docs/appearance/sitelinks) for the link structure of
your site are still relevant today, both for generating good quality sitelinks and to make it
easier for your visitors. And, as always, you can raise any questions or comments in our
[Webmaster Help Forum](https://support.google.com/webmasters/community).
