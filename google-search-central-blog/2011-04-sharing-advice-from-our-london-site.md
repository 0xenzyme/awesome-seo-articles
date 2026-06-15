---
title: "Sharing advice from our London site clinic"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-04-sharing-advice-from-our-london-site"
url: "https://developers.google.com/search/blog/2011/04/sharing-advice-from-our-london-site"
canonical: "https://developers.google.com/search/blog/2011/04/sharing-advice-from-our-london-site"
author: "Kaspar Szymanski, Pierre Far, Sven Naumann"
published: "2011-04-12T00:00:00+00:00"
updated: "2011-04-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:12:29+00:00"
status_code: 200
html_hash: "91b85523aeaec49e96643790f2e12f16349ac1f43b76fd4daec6b48555d176f7"
clean_word_count: 880
clean_char_count: 5650
---
# Sharing advice from our London site clinic

We recently hosted our second site clinic, this time at TechHub in London, UK. Like
[last year](/search/blog/2010/03/sharing-advice-from-our-site-clinic), here's our
summary of the topics that came up.

- Title tags and meta description tags are easy ways to improve your site's visibility in Google
  search results, yet we still see webmasters not fully utilizing their potential. We have a bit
  of help available about writing
  [good page titles](/search/docs/appearance/title-link)
  and
  [descriptions](/search/blog/2007/09/improve-snippets-with-meta-description)
  which you can read to brush up on the subject. That said, you can
  [ignore the meta keywords](/search/blog/2009/09/google-does-not-use-keywords-meta-tag),
  at least as far as Google is concerned.
- One way Google's algorithms determine the context of content on a page is by looking at the
  page's
  [headings](https://www.w3.org/TR/html401/struct/global.html#h-7.5.5).
  The way semantic markup is used throughout a site, including `h1`, `h2`,
  and `h3` tags, helps us to understand the priorities of a site's content. One should
  not fret, though, about every single `H` tag. Using common sense is the way to go.
- Just as we recommend you structuring pages logically, it is similarly important to structure the
  whole website, particularly by linking to related documents within your site as necessary. This
  helps both users and search engine bots explore all the content you provide. To augment this,
  be sure to provide a regularly updated
  [Sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap),
  which can be conveniently
  [linked to from your site's robots.txt file](https://www.sitemaps.org/protocol.php#submit_robots)
  for automatic discovery by Google and other search engines.
- [Duplicate content](/search/docs/advanced/guidelines/duplicate-content)
  and
  [canonicalization](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  issues were discussed for many websites reviewed at the site clinic. Duplicate content within a
  website is generally not a problem, but can make it more difficult for search engines to
  properly index your content and serve the right version to users. There are two common ways to
  signal what your preferred versions of your content are: By using
  [`301` redirects](/search/docs/crawling-indexing/301-redirects)
  to point to your preferred versions, or by using the
  [`rel="canonical"`](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  `link` element. If you're concerned about setting your preferred domain in terms of
  whether to use www or non-www, we recommend you check out the related feature for
  [setting the preferred domain feature in Webmaster Tools](https://www.google.com/support/webmasters/bin/answer.py?answer=44231).
- Another commonly seen issue is that some sites have error pages which do not return an error
  HTTP result code, but instead return the HTTP success code `200`. Only documents that
  are actually available should reply with the HTTP success result code `200`. When a
  page no longer exists, it should return a `404 (Not found)` response. Header
  responses of any URL can be checked using
  [Fetch as Googlebot](https://www.google.com/support/webmasters/bin/answer.py?answer=158587 class=)
  in Webmaster Tools or using third party tools such as the
  [Live HTTP Headers Firefox addon](https://addons.mozilla.org/en-US/firefox/addon/live-http-headers/)
  or web-sniffer.net.
- Ranking for misspelled queries, for example, local business names including typos, seems to be
  an area of concern. In some cases,
  [Google's automatic spelling correction](https://www.google.com/intl/en/help/features_list.html#spell)
  gets the job done for users by suggesting the correct spelling. It isn't a wise idea to stuff
  a site's content with every typo imaginable. It's also not advisable to hide this or any other
  type of content using JavaScript, CSS or similar techniques. These methods are in violation of
  [Google's Webmaster Guidelines](/search/docs/essentials)
  and we may take appropriate action against a site that employs them. If you're not sure how
  Googlebot "sees" your pages, for example, when using lots of JavaScript, you can get a better
  idea by looking at the text-only version of the cached copy in Google web search results.
- Users love fast websites. That's why
  [webpage loading speed](/search/blog/2010/04/using-site-speed-in-web-search-ranking)
  is an important consideration for your users. We offer a wide range of tools and recommendations
  to help webmasters understand the performance of their websites and how to improve them. The
  easiest way to get started is to use
  [Page Speed Online](https://pagespeed.googlelabs.com/),
  which is the web-based version of our popular
  [Page Speed Chrome extension](https://code.google.com/speed/page-speed/docs/using_chrome).
  Our
  [Let's make the web faster page](https://code.google.com/speed/tools)
  has great list of resources from Google and elsewhere for improving website speed, which we
  recommend you to read.

We'd like to thank the
[TechHub](https://www.techhub.com/)
team, who helped us facilitate the event, and give a big thank you to all participants. We hope
you found the presentation and Q&A; session interesting. We've embedded the presentation below.

And as we mentioned in the site clinic, sign up at the
[Google Webmaster Help Forum](https://support.google.com/webmasters/community)
to discuss any further questions you might have and keep an eye on our
[Webmaster Central Blog](/search/blog).
