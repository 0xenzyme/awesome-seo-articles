---
title: "Duplicate content due to scrapers"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-06-duplicate-content-due-to-scrapers"
url: "https://developers.google.com/search/blog/2008/06/duplicate-content-due-to-scrapers"
canonical: "https://developers.google.com/search/blog/2008/06/duplicate-content-due-to-scrapers"
author: "Written by Sven Naumann, Search Quality Team"
published: "2008-06-09T00:00:00+00:00"
updated: "2008-06-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:52:50+00:00"
status_code: 200
html_hash: "d2187a3439ab305604742b1fe53ebc46ad72ece6c9d6b13b8cf8a2a737cc63a1"
clean_word_count: 744
clean_char_count: 4663
---
# Duplicate content due to scrapers

Since duplicate content is a hot topic among webmasters, we thought it might be a good time to
address common questions we get asked regularly at conferences and on the
[Google Webmaster Help Group](https://support.google.com/webmasters/go/community).

Before diving in, I'd like to briefly touch on a concern webmasters often voice: in most cases a
webmaster has no influence on third parties that scrape and redistribute content without the
webmaster's consent. We realize that this is not the fault of the affected webmaster, which in
turn means that identical content showing up on several sites in itself is not inherently regarded
as a violation of our
[webmaster guidelines](/search/docs/essentials).
This simply leads to further processes with the intent of determining the original source of the
content—something Google is quite good at, as in most cases the original content can be
correctly identified, resulting in no negative effects for the site that originated the content.

Generally, we can differentiate between two major scenarios for issues related to duplicate
content:

- Within-your-domain-duplicate-content, that is, identical content which (often unintentionally)
  appears in more than one place on your site
- Cross-domain-duplicate-content, that is, identical content of your site which appears (again,
  often unintentionally) on different external sites

With the first scenario, you can take matters into your own hands to avoid Google indexing
duplicate content on your site. Check out Adam Lasnik's post
[Deftly dealing with duplicate content](/search/blog/2006/12/deftly-dealing-with-duplicate-content)
and Vanessa Fox's
[Duplicate content summit at SMX Advanced](/search/blog/2007/06/duplicate-content-summit-at-smx),
both of which give you some great tips on how to resolve duplicate content issues within your
site. Here's one additional tip to help avoid content on your site being crawled as duplicate:
include the preferred version of your URLs in your Sitemap file. When encountering different pages
with the same content, this may help raise the likelihood of us serving the version you prefer.
Some additional information on duplicate content can also be found in our comprehensive
[Help Center article](/search/docs/advanced/guidelines/duplicate-content)
discussing this topic.

In the second scenario, you might have the case of someone scraping your content to put it on a
different site, often to try to monetize it. It's also common for many web proxies to index parts
of sites which have been accessed through the proxy. When encountering such duplicate content on
different sites, we look at various signals to determine which site is the original one, which
usually works very well. This also means that you shouldn't be very concerned about seeing
negative effects on your site's presence on Google if you notice someone scraping your content.

In cases when you are syndicating your content but also want to make sure your site is identified
as the original source, it's useful to ask your syndication partners to include a link back to
your original content. You can find some additional tips on dealing with syndicated content in a
recent post by Vanessa Fox,
[Ranking as the original source for content you syndicate](https://www.vanessafoxnude.com/2008/05/14/ranking-as-the-original-source-for-content-you-syndicate/).

Some webmasters have asked what could cause scraped content to rank higher than the original
source. That should be a rare case, but if you do find yourself in this situation:

- Check if your content is still accessible to our crawlers. You might unintentionally have
  blocked access to parts of your content in your robots.txt file.
- You can look in your Sitemap file to see if you made changes for the particular content which
  has been scraped.
- Check if your site is in line with our webmaster guidelines.

To conclude, I'd like to point out that in the majority of cases, having duplicate content does
not have negative effects on your site's presence in the Google index. It simply gets filtered
out. If you check out some of the tips mentioned in the resources above, you'll basically learn
how to have greater control about what exactly we're crawling and indexing and which versions are
more likely to appear in the index. Only when there are signals pointing to deliberate and
malicious intent, occurrences of duplicate content might be considered a violation of the
webmaster guidelines.

If you would like to further discuss this topic, you can visit our
[Webmaster Help Group](https://support.google.com/webmasters/go/community).
