---
title: "Android app indexing is now open for everyone!"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-06-android-app-indexing-is-now-open-for"
url: "https://developers.google.com/search/blog/2014/06/android-app-indexing-is-now-open-for"
canonical: "https://developers.google.com/search/blog/2014/06/android-app-indexing-is-now-open-for"
author: "Mariya Moeva"
published: "2014-06-25T00:00:00+00:00"
updated: "2014-06-25T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:24:44+00:00"
status_code: 200
html_hash: "81799978870c9eef8888b8a8483155984ebb7e4cca728ade29878bd3afddd805"
clean_word_count: 505
clean_char_count: 2998
---
# Android app indexing is now open for everyone!

Do you have an Android app in addition to your website? You can now connect the two so that users
searching from their smartphones and tablets can easily find and reach your app content.

App deep links in search results help your users find your content more easily and re-engage with
your app after they've installed it. As a site owner, you can show your users the right content at
the right time—by connecting pages of your website to the relevant parts of your app you
control when your users are directed to your app and when they go to your website.

![](/static/search/blog/images/import/2bd4eb8381f3952d500955e7b27f5d8e.png)

Hundreds of apps have
[already implemented app indexing](https://firebase.google.com/docs/app-indexing/).
This week at Google I/O, we're announcing a set of new features that will make it even easier to
set up deep links in your app, connect your site to your app, and keep track of performance and
potential errors.

## Getting started is easy

We've greatly simplified the process to get your app deep links indexed. If your app supports HTTP
deep linking schemes, here's what you need to do:

1. [Add deep link support to your app](https://firebase.google.com/docs/app-indexing/)
2. [Connect your site and your app](https://firebase.google.com/docs/app-indexing/)
3. There is no step 3 (:

As we index your URLs, we'll discover and index the app / site connections and may begin to
surface app deep links in search results.

We can discover and index your app deep links on our own, but we recommend you publish the deep
links. This is also the case if your app only supports a custom deep link scheme. You can publish
them in one of the following ways:

- Add a `rel=alternate` `<link />` element to specify the
  corresponding app URI. You can insert it in the `<head>` section of each web
  page, or in your sitemap.
  [Find out how to implement these methods](https://firebase.google.com/docs/app-indexing/)
  on our developer site.
- [Use the App indexing API](https://firebase.google.com/docs/app-indexing/)

There's one more thing: we've added a
[new feature in Webmaster Tools](https://support.google.com/webmasters/answer/9679690)
to help you debug any issues that might arise during app indexing. It will show you what type of
errors we've detected for the app page-web page pairs, together with example app URIs so you can
debug:

![](/static/search/blog/images/import/6b3b444600548ea57c7860557b5d7795.png)

We'll also give you detailed instructions on how to debug each issue, including a QR code for the
app deep links, so you can easily open them on your phone or tablet. We'll send you Webmaster
Tools error notifications as well, so you can keep up to date.

![](/static/search/blog/images/import/377e37b6af69fc42f63c49ba9bd6f263.png)

Give app indexing a spin, and as always, if you need more help ask questions on the
[Webmaster help forum](https://support.google.com/webmasters/community/).
