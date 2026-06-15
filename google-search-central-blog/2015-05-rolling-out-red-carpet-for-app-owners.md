---
title: "Rolling out the red carpet for app owners in Search Console"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2015-05-rolling-out-red-carpet-for-app-owners"
url: "https://developers.google.com/search/blog/2015/05/rolling-out-red-carpet-for-app-owners"
canonical: "https://developers.google.com/search/blog/2015/05/rolling-out-red-carpet-for-app-owners"
author: "Hillel Maoz, Mariya Moeva"
published: "2015-05-22T00:00:00+00:00"
updated: "2015-05-22T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:26:55+00:00"
status_code: 200
html_hash: "95a2b7dba94d04a757b6e69cef6701f13e95c1e579bb1ccd99e92a98ceb8b345"
clean_word_count: 652
clean_char_count: 4019
---
# Rolling out the red carpet for app owners in Search Console

Wouldn't it be nifty if you could track where your
[indexed app content](https://firebase.google.com/docs/app-indexing/) shows up in search
results, for which queries, which app pages are most popular, and which ones have errors? Yeah, we
thought so too! So we've equipped our
[freshly renamed Search Console](/search/blog/2015/05/announcing-google-search-console-new)
with new reports to show you how Google understands and treats your app content in search results.

Our goal is to make Search Console a comprehensive source of information for everyone who cares
about Search, regardless of the format of their content. So, if you own or develop an app, Search
Console is your new go-to place for search stats.

## Add your app to Search Console

Simply
[open Search Console](https://search.google.com/search-console)
and enter your app name: `android-app://com.example`. Of course, we'll only show data
to authorized app owners, so you need to use your Google Play account to let Search Console know
you have access to the app. If you don't have access to your app in Google Play, ask an owner to
verify the app in Search Console and add you next.

## Connect your site to your app

[Associating your site](https://search.google.com/search-console/settings/associations)
with your app is necessary for
[App Indexing](https://firebase.google.com/docs/app-indexing/) to work. Plus, it helps with
understanding and ranking the app content better.

## Track your app content's performance in Search

The new
[Search Analytics report](https://search.google.com/search-console/performance/search-analytics)
provides detailed information on top queries, top app pages, and traffic by country. It also has a
[comprehensive set of filters](https://support.google.com/webmasters/answer/6155685),
allowing you to narrow down to a specific query type or region, or sort by clicks, impressions,
CTR, and positions.

![](/static/search/blog/images/import/b167b309fd1332d0bde41db1299f3214.png)

Use the Search Analytics report to compare which app content you consider most important with the
content that actually shows up in Search and gets the most clicks. If they match, you're on the
right track! Your users are finding and liking what you want them to see. If there's little
overlap, you may need to restructure your navigation, or make the most important content easier to
find. Also worth checking in this case: have you provided deep links to all the app content you
want your users to find?

## Make sure Google understands your app content

If we encounter errors while indexing your app content, we won't be able to show deep links for
those app pages in search results. The
[Crawl Errors report](https://support.google.com/webmasters/answer/9679690)
will show you the type and number of errors we've detected.

## See your app content the way Google sees it

We've created an alpha version of the
[Fetch as Google tool for apps](https://www.google.com/webmasters/tools/appbot-fetch)
to help you check if an app URI works and see how Google renders it. It can also be useful for
comparing the app content with the web page content to debug errors such as
[content mismatch](https://support.google.com/webmasters/answer/6216428#content_mismatch).
In many cases, the mismatch errors are caused by
[blocked resources](https://support.google.com/webmasters/answer/2387297)
within the app or by pop-ups asking users to sign in or register. Now you can see and resolve
these issues.

![](/static/search/blog/images/import/7908799cba2736d193a7f9348dfc2fa6.png)

To get started on optimizing and troubleshooting your own app,
[add it to Search Console now](https://search.google.com/search-console).
If you want to know more about App Indexing,
[read about it on our Developer Site](https://firebase.google.com/docs/app-indexing/). And,
as always, you're welcome to drop by the
[help forum](https://support.google.com/webmasters/go/community)
with more questions.
