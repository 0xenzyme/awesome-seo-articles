---
title: "Changes in rankings of smartphone search results"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2013-06-changes-in-rankings-of-smartphone_11"
url: "https://developers.google.com/search/blog/2013/06/changes-in-rankings-of-smartphone_11"
canonical: "https://developers.google.com/search/blog/2013/06/changes-in-rankings-of-smartphone_11"
author: "Pierre Far"
published: "2013-06-11T00:00:00+00:00"
updated: "2013-06-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2013_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:22:02+00:00"
status_code: 200
html_hash: "493c472f4e919c19beeb7d9a477dba6129bec644b154cd5cd27140189a781a14"
clean_word_count: 751
clean_char_count: 5020
---
# Changes in rankings of smartphone search results

Smartphone users are a significant and fast growing segment of Internet users, and at Google we
want them to experience the full richness of the web. As part of our efforts to improve the mobile
web, we published our [recommendations](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) and the most
[common configuration mistakes](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing).

Avoiding these mistakes helps your smartphone users engage with your site fully and helps
searchers find what they're looking for faster. To improve the search experience for smartphone
users and address their pain points, we plan to roll out several ranking changes in the near
future that address sites that are misconfigured for smartphone users.

Let's now look at two of the most common mistakes and how to fix them.

## Faulty redirects

Some websites use separate URLs to serve desktop and smartphone users. A faulty redirect is when a
desktop page redirects smartphone users to an irrelevant page on the smartphone-optimized website.
A typical example is when all pages on the desktop site redirect smartphone users to the home page
of the smartphone-optimized site. For example, in the figure below, the redirects shown as red
arrows are considered faulty:

![Many URLs all redirecting to 1 URL](/static/search/blog/images/archived_N1_redirects.png)

This kind of redirect disrupts a user's workflow and may lead them to stop using the site and go
elsewhere. Even if the user doesn't abandon the site, irrelevant redirects add more work for them
to handle, which is particularly troublesome when they're on slow mobile networks. These faulty
redirects frustrate users whether they're looking for a webpage, video, or something else, and our
ranking changes will affect many types of searches.

Avoiding irrelevant redirects is very easy: Simply redirect smartphone users from a desktop page
to its equivalent smartphone-optimized page. If the content doesn't exist in a smartphone-friendly
format, showing the desktop content is better than redirecting to an irrelevant page.

We have more
[tips about redirects](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing), and be sure to
read our recommendations for having
[separate URLs](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#separate-urls) for desktop and
smartphone users.

## Smartphone-only errors

Some sites serve content to desktop users accessing a URL but show an error page to smartphone
users. There are many scenarios where smartphone-only errors are seen. Some common ones are:

- If you recognize a user is visiting a desktop page from a mobile device and you have an
  equivalent smartphone-friendly page at a different URL, redirect them to that URL instead of
  serving a `404` or a
  [`soft 404` page](/search/docs/advanced/crawling/soft-404-errors).
- Make sure that the smartphone-friendly page itself is not an error page. If your content is
  not available in a smartphone-friendly format, serve the desktop page instead. Showing the
  content the user was looking for is a much better experience than showing an error page.
- Incorrectly handling Googlebot-Mobile. A typical mistake is when Googlebot-Mobile for
  smartphones is incorrectly redirected to the website
  [optimized for feature phones](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) which, in turn,
  redirects Googlebot-Mobile for smartphones back to desktop site. This results in infinite
  redirect loop, which we recognize as error.

  Avoiding this mistake is easy: All
  [Googlebot-Mobile user agents](/search/docs/crawling-indexing/googlebot) identify
  themselves as specific mobile devices, and you should treat these Googlebot user agents
  exactly like you would treat these devices. For example, Googlebot Mobile for smartphones
  currently identifies itself as an iPhone and you should serve it the same response an iPhone
  user would get.
- Unplayable videos on smartphone devices. Many websites embed videos in a way that works well on
  desktops but is unplayable on smartphone devices. For example, if content requires Adobe Flash,
  it won't be playable on an iPhone or on Android versions 4.1 and higher.

Although we covered only two types of mistakes here, it's important for webmasters to focus on
avoiding all of the common smartphone website
[misconfigurations](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing). Try to test your
site on as many different mobile devices and operating systems, or their emulators, as possible,
including testing the videos included on your site. Doing so will improve the mobile web, make
your users happy, and allow searchers to experience your content fully.

As always, please ask in our
[forums](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:crawling_indexing_ranking))
if you have any questions.
