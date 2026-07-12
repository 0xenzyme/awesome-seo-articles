---
title: "Sitemaps FAQs"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-01-sitemaps-faqs"
url: "https://developers.google.com/search/blog/2008/01/sitemaps-faqs"
canonical: "https://developers.google.com/search/blog/2008/01/sitemaps-faqs"
author: "Written by Susan Moskwa and Trevor Foucher, Webmaster Tools Team"
published: "2008-01-15T00:00:00+00:00"
updated: "2008-01-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:51:25+00:00"
status_code: 200
html_hash: "b2cb526d34f73b1291b4836a7723a0e10f81af47f2918ab252fe480b8c0142b4"
clean_word_count: 1128
clean_char_count: 6750
---
# Sitemaps FAQs

Last month, Trevor spoke on the **Sitemaps: Oversold, Misused or On The Money?** panel at
Search Engine Strategies in Chicago. After receiving a lot of great questions at the conference in
addition to all the feedback we receive in our
[help forum](https://support.google.com/webmasters/community),
we've pulled together a FAQ:

**I submitted a Sitemap, but my URLs haven't been crawled or indexed yet. Isn't that what a
Sitemap is for?**
Submitting a Sitemap helps you make sure Google knows about the URLs on your site. It can be
especially helpful if your content is not easily discoverable by our crawler (such as pages
accessible only through a form). It is not, however, a guarantee that those URLs will be crawled
or indexed. We use information from Sitemaps to augment our usual crawl and discovery processes,
which is explained in our
[documentation about Sitemaps](/search/docs/crawling-indexing/sitemaps/overview).

**If it doesn't get me automatically crawled and indexed, what does a Sitemap do?**
Sitemaps give information to Google to help us better understand your site. This can include
making sure we know about all your URLs, how often and when they're updated, and what their
relative importance is. Also, if you
[submit your Sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap)
via Webmaster Tools, we'll show you stats such as how many of your Sitemap's URLs are indexed.

**Will a Sitemap help me rank better?**
A Sitemap does not affect the actual ranking of your pages. However, if it helps get more of your
site crawled (by notifying us of URLs we didn't previously didn't know about, and/or by helping us
prioritize the URLs on your site), that can lead to increased presence and visibility of your site
in our index.

**If I set all of my pages to have priority 1.0, will that make them rank higher (or get crawled
faster) than someone else's pages that have priority 0.8?**
No. Priority only indicates the importance of a particular URL relative to other URLs on your
site, and doesn't impact the ranking of your pages in search results. Indicating that all of your
pages have the same priority is the same as not providing any priority information at all.

**Is there any point in submitting a Sitemap if all the metadata
(`<changefreq>,<priority>`, etc.) is the same for each URL, or if I'm not sure
it's accurate?**
If the value of a particular tag is the same for 100% of the URLs in your Sitemap, you don't
need to include that tag in your Sitemap. Including it won't hurt you, but it's essentially the
same as not submitting any information, since it doesn't help distinguish between your URLs. If
you're not sure whether your metadata is accurate (for example, you don't know when a particular
URL was last modified), it's better to omit that tag for that particular URL than to just make
up a value which may be inaccurate.

**I've heard about people who submitted a Sitemap and got penalized shortly afterward. Can a
Sitemap hurt you?**
Only if it falls on you from a great height. (Seriously, though: if it ever happened that someone
was penalized after submitting a Sitemap, it would have been purely coincidental. Google does not
penalize you for submitting a Sitemap.)

**Where can I put my Sitemap? Does it have to be at the root of my site?**
We recently enabled Sitemap cross-submissions, which means that you can put your Sitemap just
about anywhere as long as you have the following sites verified in your
[Webmaster Tools](https://search.google.com/search-console)
account:

- the site on which the Sitemap is located
- the site(s) whose URLs are referenced in the Sitemap

Note that cross-submissions may not work for search engines other than Google.
[Learn more about Sitemap cross-submissions](/search/blog/2007/10/dealing-with-sitemap-cross-submissions).

**Can I just submit the site map that my webmaster made of my site? I don't get this whole XML
thing.**
There's a difference between a (usually HTML) site map built to help humans navigate around your
site, and an XML Sitemap built for search engines. Both of them are useful, and it's great to have
both. A site map on your domain can also help search engines find your content (since crawlers
can follow the links on the page). However, if you
[submit an HTML sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap)
in place of a Sitemap, Webmaster Tools will report an error because an HTML page isn't one of our
recognized Sitemap formats. Also, if you create an XML Sitemap, you'll be able to give us more
information than you can with an HTML site map (which is just a collection of links).
[Learn more about supported Sitemap formats](/search/docs/crawling-indexing/sitemaps/build-sitemap#sitemapformat).

**Which Sitemap format is the best?**
We recommend the XML Sitemap protocol as defined by
[sitemaps.org](https://www.sitemaps.org/). XML Sitemaps have the
advantage of being upgradeable: you can start simple if you want (by just listing your URLs),
but—unlike a [text file Sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap#text)
—you can easily upgrade an XML Sitemap later on to include more metadata. XML Sitemaps are also
more comprehensive than an Atom or RSS feed submitted as a Sitemap, since feeds usually only list
your most recent URLs (rather than all the URLs you want search engines to know about).

**If I have multiple URLs that point to the same content, can I use my Sitemap to indicate my
preferred URL for that content?**
Yes. While we can't guarantee that our algorithms will display that particular URL in search
results, it's still helpful for you to indicate your preference by including that URL in your
Sitemap. We take this into consideration, along with other signals, when deciding which URL to
display in search results.
[Learn more about duplicate content](/search/docs/crawling-indexing/consolidate-duplicate-urls).

**Does the placement of a URL within a Sitemap file matter? Will the URLs at the beginning of the
file get better treatment than the URLs near the end?**
No, and no.

**If my site has multiple sections (for example, a blog, a forum, and a photo gallery), should I
submit one Sitemap for the site, or multiple Sitemaps (one for each section)?**
You may submit as few or as many Sitemaps as you like (up to
[these limits](/search/docs/crawling-indexing/sitemaps/build-sitemap)). Organize them in
whatever way you find easiest to maintain. If you create multiple Sitemaps, you can use a
[Sitemap Index file to list them all](/search/docs/crawling-indexing/sitemaps/large-sitemaps).

If your question isn't covered here, you can find even more questions and answers in our
[help forum](https://support.google.com/webmasters/community).
