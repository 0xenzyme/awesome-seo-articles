---
title: "Making Websites Mobile Friendly"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-02-making-websites-mobile-friendly"
url: "https://developers.google.com/search/blog/2011/02/making-websites-mobile-friendly"
canonical: "https://developers.google.com/search/blog/2011/02/making-websites-mobile-friendly"
author: "Pierre Far"
published: "2011-02-22T00:00:00+00:00"
updated: "2011-02-22T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:11:14+00:00"
status_code: 200
html_hash: "5ad7a14e60a04a503e3b00fdaa4cf60110e56a50c6636670fe186860aa1b070e"
clean_word_count: 1069
clean_char_count: 6822
---
# Making Websites Mobile Friendly

We've noticed a rise in the number of questions from webmasters about how best to structure a
website for mobile phones and how websites can best interact with Googlebot-Mobile. In this post
we'll explain the current situation and give you specific recommendations you can implement now.

## Some Background

Let's start with a simple question: what do we mean by "mobile phone" when talking about
mobile-friendly websites?

A good way to answer this question is to think about the capabilities of the mobile phone's web
browser, especially in relation to the capabilities of modern desktop browsers. To simplify
matters, we can break mobile phones into a few classifications:

1. Traditional mobile phones: Phones with browsers that cannot render normal desktop webpages.
   This includes browsers for cHTML (iMode), WML, WAP, and the like.
2. Smartphones: Phones with browsers that render normal desktop pages, at least to some extent.
   This category includes a diversity of devices, such Windows Phone 7, Blackberry devices,
   iPhones, and Android phones, and also tablets and eBook readers.We can further break down this
   category by support for HTML5:

- Devices with browsers that do not support HTML5
- Devices with browsers that support HTML5

Once upon a time, mobile phones connected to the Internet using browsers with limited rendering
capabilities; but this is clearly a changing situation with the fast rise of smartphones which
have browsers that rival the full desktop experience. As such, it's important to note that the
distinction we are making here is based on the current situation as we see it and might change in
the future.

## Googlebot and Mobile Content

Google has two crawlers relevant to this topic: Googlebot and Googlebot-Mobile. Googlebot crawls
desktop-browser type of webpages and content embedded in them and Googlebot-Mobile crawls mobile
content. The questions we're seeing more of can be summed up as follows:
Given the diversity of capabilities of mobile web browsers, what kind of content should I serve to
Googlebot-Mobile?

The answer lies in the User-agent that Googlebot-Mobile supplies when crawling. There are several
User-agent strings in use by Googlebot-Mobile, all of which use this format:

```
[Phone name(s)] (compatible; Googlebot-Mobile/2.1; +https://www.google.com/bot.html)
```

To decide which content to serve, assess which content your website has that best serves the
phone(s) in the User-agent string. A
[full list of Googlebot-Mobile User-agents can be found here](/search/docs/crawling-indexing/overview-google-crawlers).

Notice that we currently do not crawl with Googlebot-Mobile using a smartphone User-agent string.
Thus at the current time, a correctly-configured content serving system will serve
Googlebot-Mobile content only for the traditional phones described above, because that's what the
User-agent strings in use today dictate. This may change in the future, and if so, it may mean
there would be a new Googlebot-Mobile User-agent string.

For now, we expect smartphones to handle desktop experience content so there is no real need for
mobile-specific effort from webmasters. However, for many websites it may still make sense for the
content to be formatted differently for smartphones, and the decision to do so should be based on
how you can best serve your users.

## URL Structure for Mobile Content

The next set of questions ask about the URLs mobile content should be served from. Let's look in
detail at some common use cases.

### Websites with only Desktop Experience Content

Most websites currently have only one version of their content, namely in HTML that is designed
for desktop web browsers. This means all browsers access the content from the same URL.

These websites may not be serving traditional mobile phone users. The quality experienced by their
smartphone users depends on the mobile browser they are using and it could be as good as browsing
from the desktop.

If you serve only desktop experience content for all User Agents, you should do so for
Googlebot-Mobile too; that is, treat Googlebot-Mobile as you treat all other or unknown
User Agents. In these cases,
[Google may modify your webpages](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
for an improved mobile experience.

### Websites with Dedicated Mobile Content

Many websites have content specifically optimized for mobile users. The content could be simply
reformatted for the typically smaller mobile displays, or it could be in a different format (for
example, served using WAP, etc.).

A very common question we see is: Does it matter if the different types of content are served from
the same URL or from different URLs? For example, some websites have www.example.com as the URL
desktop browsers are meant to access and have m.example.com or wap.example.com for the different
mobile devices. Other websites serve all types of content from just one URL structure like
www.example.com.

For Googlebot and Googlebot-Mobile, it does not matter what the URL structure is as long as it
returns exactly what a user sees too. For example, if you redirect mobile users from
www.example.com to m.example.com, that will be recognized by Googlebot-Mobile and both websites
will be crawled and added to the correct index. In this case, use a `301` redirect for both users
and Googlebot-Mobile.

If you serve all types of content from www.example.com, that is, serving desktop-optimized content
or mobile-optimized content from the same URL depending on the User-agent, this will also lead to
correct crawling by Googlebot and Googlebot-Mobile. This is not considered cloaking by Google.

It is worth repeating that regardless of URL structure, you must correctly detect the User-agent
as given by your users and Googlebot-Mobile, and serve both the same content. Don't forget to keep
the default content, the desktop-optimized content, for when an unknown User-agent requests it.

## Mobile Sitemaps in Webmaster Tools

Finally, we receive many questions about what URLs to put in Mobile Sitemaps. As explained in our
[Mobile Sitemaps Help Center articles](/search/docs/crawling-indexing/mobile),
you should include only mobile content URLs in Mobile Sitemaps, even if these URLs also return
non-mobile content when accessed by a non-mobile User-agent.

## More Questions?

A good place to start is our
[Mobile Sites Help Center articles](https://www.google.com/support/webmasters/bin/topic.py?topic=28803)
and the relevant sections in our
[Search Engine Optimization Starter Guide](/search/docs/fundamentals/seo-starter-guide).
We also created a
[thread in our forums](https://support.google.com/webmasters/community/thread?tid=64f43a49a3ac2e27)
for you to ask questions about this post.
