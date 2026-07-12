---
title: "Tips on using feeds and information on subscriber counts in Reader"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-02-tips-on-using-feeds-and-information-on"
url: "https://developers.google.com/search/blog/2007/02/tips-on-using-feeds-and-information-on"
canonical: "https://developers.google.com/search/blog/2007/02/tips-on-using-feeds-and-information-on"
author: null
published: "2007-02-20T00:00:00+00:00"
updated: "2007-02-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:48:08+00:00"
status_code: 200
html_hash: "96136e6f3934908c1c3e0300b83d7a07e0f1c429be110a2267790daca0bfd5f0"
clean_word_count: 623
clean_char_count: 3746
---
# Tips on using feeds and information on subscriber counts in Reader

Does your site have a feed? A feed can connect you to your readers and keep them returning to your
content. Most blogs have feeds, but increasingly, other types of sites with frequently changing
content are making feeds available as well. Some examples of sites that offer feeds:

- News sources such as the New York Times publish
  [feeds of their latest stories](https://www.nytimes.com/services/xml/rss/index)
- Companies like Apple publish feeds of their
  [press releases](https://images.apple.com/main/rss/hotnews/pr.rss),
  as well as [a few other feeds](https://www.apple.com/rss/).
- Blogs including the Official Google Blog publish feeds with their
  [latest posts](https://googleblog.blogspot.com/feeds/posts/default)
- Shopping sites like Buy.com publish feeds with
  [noteworthy deals](https://www.buy.com/rss/feed.asp?loc=273&grp=4)

## Find out how many readers are subscribed to your feed

If your site has a feed, you can now get information about the number of
[Google Reader and Google Personalized home page subscribers](https://googlereader.blogspot.com/2007/02/one-subscriber-two-subscribers-three.html).
If you use [Feedburner](https://www.feedburner.com/), you'll start
to see numbers from these subscriptions taken into account. You can also
[find this number](https://www.google.com/help/reader/publishers.html#faq)
in the crawling data in your logs. We crawl feeds with the user-agent
`Feedfetcher-Google`, so simply look for this `user-agent` in your logs to
find the subscriber number. If multiple URLs point to the same feed, we may crawl each separately,
so in this case, just count up the subscriber numbers listed for each unique feed-id. An example
of what you might see in your logs is below:

```
User-Agent: Feedfetcher-Google; (+https://www.google.com/feedfetcher.html; 4 subscribers; feed-id=1794595805790851116)
```

## Making your feed available to Google

You can [submit your feed as a Sitemap](/search/docs/crawling-indexing/sitemaps/overview) in
Webmaster Tools. This will let us know about the URLs listed in the feed so we can crawl and index
them for web search. In addition, if you want to make sure your feed shows up in the list of
available feeds for Google products, simply add a `<link />` tag with the feed URL
to the `<head>` section of your page. For instance:

```
<link rel="alternate" type="application/atom+xml"  href="https://www.example.com/atom.xml" />
```

Remember that `Feedfetcher-Google` retrieves feeds only for use in Google Reader and
Personalized home page. For the content to appear in web search results, Googlebot will have to
crawl it as well.

## Don't yet have a feed?

If you use a content management system or blogging platform, feed functionality may be built right
now. For instance, if you use Blogger, you can go to
*Settings* > *Site Feed* and make sure that
*Publish Site Feed* is set to *Yes*. You can also set the feed to either full or short
and can add a footer. The URL listed here is what subscribers add to their feed readers. A link to
this URL will appear on your blog.

## More tips from the Google Reader team

In order to provide the best experience for your users, the Google Reader team has also put
together some
[tips for feed publishers](https://www.google.com/help/reader/publishers).
This document covers feed best practices, common implementation pitfalls, and various ways to
promote your feeds. Whether you're creating your feeds from scratch or have been publishing them
for a long time, we encourage you to take a look at our tips to make the most of your feeds. If
you have any questions, please
[get in touch](https://groups.google.com/group/Google-Labs-Reader).
