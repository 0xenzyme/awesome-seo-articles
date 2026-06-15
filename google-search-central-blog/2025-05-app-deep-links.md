---
title: "App deep links: connecting your website and app"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "2025-05-app-deep-links"
url: "https://developers.google.com/search/blog/2025/05/app-deep-links"
canonical: "https://developers.google.com/search/blog/2025/05/app-deep-links"
author: "John Mueller"
published: "2025-05-02T00:00:00+00:00"
updated: "2025-05-02T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:45:09+00:00"
status_code: 200
html_hash: "b15e80781dc7e6ca27d50cbbec197127421a4bb88818152a66beeebab1532812"
clean_word_count: 788
clean_char_count: 5179
---
# App deep links: connecting your website and app

Since 2013, Search has recognized the importance of [app deep links in a mobile-centric world](/search/blog/2013/10/indexing-apps-just-like-websites).
In this post, we'll review the current state of app deep links — take a look at what they
are, the benefits of using them, and how to implement them effectively.

![A search result leading to a shopping mobile app](/static/search/blog/images/search-results-to-deep-link.png)

A search result leading to a shopping mobile app

## Seamlessly connecting users to in-app content

Deep links are special URIs that take users beyond your mobile app's homepage, leading them
directly to specific in-app content. Imagine a user clicking on a search result for a product on
your website or social media and being seamlessly taken to that exact product page within your
app. To do this, you need to configure deep links both on iOS (called
[Universal Links](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content))
and Android (called [App Links](https://developer.android.com/training/app-links)).
Both types are supported on Google Search.

## The benefits of deep linking

- **Enhanced user experience:** Users land directly on the content within the app
  if they have it installed. This saves them an average of 2-3 clicks, giving them more time to
  engage in the app.
- **More targeted and relevant marketing:** Deep links enhance your marketing
  initiatives by allowing you to guide users to the exact, most relevant content you want them
  to see from marketing material, such as in emails, ad campaigns, and social media posts, with a
  single link that works both for the app and the website.
- **Better analytics and increased reporting:** Deep links enable you to analyze
  in-app user behavior by attributing conversions more accurately to a specific page, which is
  particularly helpful when you're measuring the effectiveness of different campaigns.

## Deep links and SEO

Adding deep links to your website connects the website's URLs with the relevant app pages. It
doesn't change how Google Search shows your content; Search continues to use the content of your
web pages for indexing and ranking. App deep links enable users to go from Search results directly
to the corresponding app page (if installed), resulting in a better user experience.

Because Search uses your web page content for indexing and ranking, you should only add deep
links in cases where the app page contains the same content as the corresponding web page.
Otherwise, the title and snippet shown for the page in Google Search could mislead users about
the content they will see after they click. Layout or other UX differences between app pages and
the corresponding web pages are OK, as long as the content matches.

Search Console includes performance of your site's app deep links for Android. In the
[Performance report](https://support.google.com/webmasters/answer/7576553#zippy=%2Csearch-appearance),
you can use the [Android App Search appearance filter](https://support.google.com/webmasters/answer/7576553#zippy=%2Csearch-appearance)
to see when your Android app deep links are found and shown to users.

![Search Console's performance report showing the Android App search appearance filter](/static/search/blog/images/android-app-search-appearance-filter.png)

Search Console's performance report showing the Android App search appearance filter

## Implementing deep links

To set up deep linking between your website and app, check out these platform-specific implementation guides:

- **Android apps**: Use [App Links](https://developer.android.com/training/app-links).
  You can do this by associating your app with your website in the app manifest file.
- **iOS apps**: Implement [Universal Links](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).
  You can do this by setting up an `apple-app-site-association` file on your website
  and configuring it in the app.

The following tools can also help you with implementation, troubleshooting, and validation of app deep links:

- [Deep links page in the Play Developer Console](https://play.google.com/console/about/deeplinks/):
  Provides you with an overview of your existing setup, reports on ads URLs which are not
  deeplinked, and publishes app deep links fixes without needing to do a new app release.
- [Android Studio App Links Assistant](https://developer.android.com/studio/write/app-link-indexing)
  (under Tools): Provides you with an overview of your existing deep links and their validation
  statuses, a detailed view of the misconfiguration for each link, and how to automatically fix
  the configuration issues.
- [Debugging Universal Links for iOS](https://developer.apple.com/documentation/technotes/tn3155-debugging-universal-links):
  Test, debug, and set up Universal Links on iOS.

We hope these tips help you implement deep links for your app. If you have any more questions,
refer to the [Deep Links Crash Course](https://youtube.com/playlist?list=PLWz5rJ2EKKc-hZMZIfAUMBDR7kPC1m7HU&si=RzbiW8U9tZcuF8ay).
