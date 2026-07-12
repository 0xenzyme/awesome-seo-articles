---
title: "Deftly dealing with duplicate content"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-12-deftly-dealing-with-duplicate-content"
url: "https://developers.google.com/search/blog/2006/12/deftly-dealing-with-duplicate-content"
canonical: "https://developers.google.com/search/blog/2006/12/deftly-dealing-with-duplicate-content"
author: null
published: "2006-12-18T00:00:00+00:00"
updated: "2006-12-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:47:14+00:00"
status_code: 200
html_hash: "80cd462c3a3b93edf4c0e7c893683730a3da8ad5e508f612423f5fe078ef493c"
clean_word_count: 869
clean_char_count: 5591
---
# Deftly dealing with duplicate content

At the recent Search Engine Strategies conference in freezing Chicago, many of us Googlers were
asked questions about duplicate content. We recognize that there are many nuances and a bit of
confusion on the topic, so we'd like to help set the record straight.

## What is duplicate content?

Duplicate content generally refers to substantive blocks of content within or across domains that
either completely match other content or are appreciably similar. Most of the time when we see
this, it's unintentional or at least not malicious in origin: forums that generate both regular
and stripped-down mobile-targeted pages, store items shown (and—worse yet—linked) via
multiple distinct URLs, and so on. In some cases, content is duplicated across domains in an
attempt to manipulate search engine rankings or garner more traffic via popular or long-tail
queries.

## What isn't duplicate content?

Though we do offer
[a handy translation utility](https://translate.google.com/),
our algorithms won't view the same article written in English and Spanish as duplicate content.
Similarly, you shouldn't worry about occasional snippets (quotes and otherwise) being flagged as
duplicate content.

## Why does Google care about duplicate content?

Our users typically want to see a diverse cross-section of unique content when they do searches.
In contrast, they're understandably annoyed when they see substantially the same content within
a set of search results. Also, webmasters become sad when we show a complex URL
(`example.com/contentredir?value=shorty-george〈=en`) instead of the pretty URL
they prefer (`example.com/en/shorty-george`).

## What does Google do about it?

During our crawling and when serving search results, we try hard to index and show pages with
distinct information. This filtering means, for instance, that if your site has articles in
"regular" and "printer" versions and neither set is blocked in robots.txt or via a noindex meta
tag, we'll choose one version to list. In the rare cases in which we perceive that duplicate
content may be shown with intent to manipulate our rankings and deceive our users, we'll also
make appropriate adjustments in the indexing and ranking of the sites involved. However, we
prefer to focus on filtering rather than ranking adjustments ... so in the vast majority of
cases, the worst thing that'll befall webmasters is to see the "less desired" version of a page
shown in our index.

## How can Webmasters proactively address duplicate content issues?

- **Block appropriately:** Rather than letting our algorithms determine the "best" version of a
  document, you may wish to help guide us to your preferred version. For instance, if you don't
  want us to index the printer versions of your site's articles, disallow those directories or
  make use of regular expressions in your robots.txt file.
- **Use `301` redirects:** If you have restructured your site,
  [use `301` redirects](/search/docs/crawling-indexing/301-redirects)
  (`RedirectPermanent`) in your `.htaccess` file to smartly redirect users,
  the Googlebot, and other spiders.
- **Be consistent:** Endeavor to keep your internal linking consistent; don't link to
  `/page/` and `/page` and `/page/index.htm`.
- **Use TLDs:** To help us serve the most appropriate version of a document, use top level
  domains whenever possible to handle country-specific content. We're more likely to know that
  `.de` indicates Germany-focused content, for instance, than `/de` or
  `de.example.com`.
- **Syndicate carefully:** If you syndicate your content on other sites, make sure they include
  a link back to the original article on each syndicated article. Even with that, note that we'll
  always show the (unblocked) version we think is most appropriate for users in each given search,
  which may or may not be the version you'd prefer.
- **Use the preferred domain feature of Webmaster Tools:** If other sites link to yours using
  both the www and non-www version of your URLs, you can let us know which way you prefer your
  site to be indexed.
- **Minimize boilerplate repetition:** For instance, instead of including lengthy copyright
  text on the bottom of every page, include a very brief summary and then link to a page with more
  details.
- **Avoid publishing stubs:** Users don't like seeing "empty" pages, so avoid placeholders
  where possible. This means not publishing (or at least blocking) pages with zero reviews, no
  real estate listings, etc., so users (and bots) aren't subjected to a zillion instances of
  "Below you'll find a superb list of all the great rental opportunities in [insert cityname]..."
  with no actual listings.
- **Understand your CMS:** Make sure you're familiar with how content is displayed on your Web
  site, particularly if it includes a blog, a forum, or related system that often shows the same
  content in multiple formats.
- **Don't worry be happy:** Don't fret too much about sites that scrape (misappropriate and
  republish) your content. Though annoying, it's highly unlikely that such sites can negatively
  impact your site's presence in Google. If you do spot a case that's particularly frustrating,
  you are welcome to file a
  [DMCA request](https://support.google.com/legal/troubleshooter/1114905)
  to claim ownership of the content and have us deal with the rogue site.

In short, a general awareness of duplicate content issues and a few minutes of thoughtful
preventative maintenance should help you to help us provide users with unique and relevant
content.
