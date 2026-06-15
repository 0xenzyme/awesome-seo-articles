---
title: "Google News now crawling with Googlebot"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-08-google-news-now-crawling-with-googlebot"
url: "https://developers.google.com/search/blog/2011/08/google-news-now-crawling-with-googlebot"
canonical: "https://developers.google.com/search/blog/2011/08/google-news-now-crawling-with-googlebot"
author: "David Smydra, Google News Product Specialist"
published: "2011-08-25T00:00:00+00:00"
updated: "2011-08-25T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:14:26+00:00"
status_code: 200
html_hash: "e6e8b2d73b63c9e3fee915bcfa7f7ef0f9e7c17fc19d8977948a8bbaf85a2cc4"
clean_word_count: 589
clean_char_count: 3779
---
# Google News now crawling with Googlebot

*Cross-posted on the
[Google News Blog](https://googlenewsblog.blogspot.com/2011/08/google-news-now-crawling-with-googlebot.html)*

Google News recently updated our infrastructure to crawl with Google's primary user-agent,
[Googlebot](/search/docs/crawling-indexing/googlebot).
What does this mean? Very little to most publishers. Any news organizations that wish to opt out
of Google News can continue to do so: Google News will still respect the robots.txt entry for
[Googlebot-News](/search/blog/2009/12/new-user-agent-for-news), our former user-agent,
if it is more restrictive than the robots.txt entry for Googlebot.

Our Help Center provides detailed
[guidance](https://www.google.com/support/news_pub/bin/answer.py?answer=93977)
on using the robots exclusion protocol for Google News, and publishers can contact the
[Google News Support Team](https://www.google.com/support/news_pub/bin/static.py?page=contact_policy.cs)
if they have any questions, but we wanted to first clarify the following:

- Although you'll now only see the Googlebot user-agent in your site's logs, no need to worry:
  the appearance of Googlebot instead of Googlebot-News is independent of our inclusion policies.
  (You can always check whether your site is included in Google News by searching with the "site:"
  operator. For instance, enter "site:yournewssite.com" in the search field for Google News, and
  if you see results then we are currently indexing your news site.)
- Your analytics tool will still be able to differentiate user traffic coming to your website from
  Google Search and traffic coming from Google News, so you should see no changes there.
  The main difference is that you will no longer see occasional automated visits to your site
  from the Googlebot-news crawler.
- If you're currently respecting our
  [guidelines for Googlebot](/search/docs/crawling-indexing/googlebot),
  you will not need to make any code changes to your site. Sites that have implemented
  subscriptions using a metered model or who have implemented
  [First Click Free](https://www.google.com/support/webmasters/bin/answer.py?answer=74536)
  will not experience any changes. For sites which require registration, payment or login prior to
  reading any full article, Google News will only be able to crawl and index the title and snippet
  that you show all users who visit your page. Our
  [Webmaster Guidelines](/search/docs/essentials)
  provide additional information about
  "[cloaking](/search/docs/essentials/spam-policies#cloaking)"
  (that is, showing a bot a different version than what users experience). Learn more about Google
  News and subscription publishers in this
  [Help Center article](https://www.google.com/support/news_pub/bin/answer.py?answer=40543).
- Rest assured, your Sitemap will still be crawled. This change does not affect how we crawl News
  Sitemaps. If you are a News publisher who hasn't yet set up a News Sitemap and are interested in
  getting started, please follow our
  [documentation about Google News](/search/docs/crawling-indexing/sitemaps/news-sitemap).
- For any publishers that wish to opt out of Google News and stay in Google Search, you can simply
  disallow Googlebot-news and allow Googlebot. For more information on how to do this, consult our
  [documentation about robots.txt](/search/docs/crawling-indexing/robots/intro).

As with any website, from time to time we need to make updates to our infrastructure. At the same
time, we want to continue to provide as much control as possible to news web sites. We hope we
have answered any questions you might have about this update. If you have additional questions,
please check out our
[Help Center](https://www.google.com/support/news_pub/).
