---
title: "Indexing apps just like websites"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2013-10-indexing-apps-just-like-websites"
url: "https://developers.google.com/search/blog/2013/10/indexing-apps-just-like-websites"
canonical: "https://developers.google.com/search/blog/2013/10/indexing-apps-just-like-websites"
author: "Lawrence Chang"
published: "2013-10-31T00:00:00+00:00"
updated: "2013-10-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2013_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:22:53+00:00"
status_code: 200
html_hash: "3aa068ec9738a8ae3cbc22b005fe6442393e0bd9b806049d6f7ae371e0367b7f"
clean_word_count: 435
clean_char_count: 2629
---
# Indexing apps just like websites

Searchers on smartphones experience many speed bumps that can slow them down. For example, any
time they need to change context from a web page to an app, or vice versa, users are likely to
encounter redirects, pop-up dialogs, and extra swipes and taps. Wouldn't it be cool if you could
give your users the choice of viewing your content either on the website or via your app, both
straight from Google's search results?

Today, we're happy to announce a new capability of Google Search, called app indexing, that uses
the expertise of webmasters to help create a seamless user experience across websites and mobile
apps.

Just like it crawls and indexes websites, Googlebot can now index content in your Android app.
Webmasters will be able to indicate which app content you'd like Google to index in the same way
you do for webpages today—through your existing Sitemap file and through Webmaster Tools. If
both the webpage and the app contents are successfully indexed, Google will then try to show deep
links to your app straight in our search results when we think they're relevant for the user's
query and if the user has the app installed. When users tap on these deep links, your app will
launch and take them directly to the content they need. Here's an example of a search for home
listings in Mountain View:

![Search results with an 'Open in app' button that takes the user to the respective app of the website](/static/search/blog/images/import/fdd2bb95fcbe939d8d6dfea5e45fb447.png)

We're currently testing app indexing with an initial group of developers. Deep links for these
applications will start to appear in Google search results for signed-in users on Android in the
US in a few weeks. If you are interested in enabling indexing for your Android app, it's easy to
get started:

1. [Let us know](https://docs.google.com/a/google.com/forms/d/1itcqPAQqggJ6e4m8aejWLM8Dc5O8P6qybgGbKCNxGV0/viewform)
   that you're interested. We're working hard to bring this functionality to more websites and apps
   in the near future.
2. [Enable](https://firebase.google.com/docs/app-indexing/)
   deep linking within your app.
3. Provide information about alternate app URIs, either in the Sitemaps file or in a link element
   in pages of your site.

For more details on implementation and for information on how to sign up,
[visit our developer site](https://firebase.google.com/docs/app-indexing/).
As always, if you have any questions, please ask in the
[mobile section of our webmaster forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:mobile_web)).
