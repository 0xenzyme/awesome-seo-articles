---
title: "Frequently asked questions about JavaScript and links"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2020-05-frequently-asked-questions-about"
url: "https://developers.google.com/search/blog/2020/05/frequently-asked-questions-about"
canonical: "https://developers.google.com/search/blog/2020/05/frequently-asked-questions-about"
author: "Martin Splitt"
published: "2020-05-26T00:00:00+00:00"
updated: "2020-05-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:36:42+00:00"
status_code: 200
html_hash: "042931d195f1ee23d407839ce9e877a67b682a30051f4e5553459ae05f5d5ae6"
clean_word_count: 629
clean_char_count: 4115
---
# Frequently asked questions about JavaScript and links

We get lots of questions every day - in our
[Webmaster office hours](https://youtube.com/channel/UCWf2ZlNsCGDS89VBF_awNvA/community), at
conferences, in the [webmaster forum](https://support.google.com/webmasters/community)
and on [Twitter](https://twitter.com/googlesearchc). One of the more frequent themes among
these questions are links and especially those generated through JavaScript.

In our
[Webmaster Conference Lightning Talks](https://www.youtube.com/playlist?list=PLKoqnv2vTMUNf6w9wUu7RgxHkaTrq2Zpf)
video series, we recently addressed the most frequently asked questions on Links and JavaScript:

During the live premiere, we also had a Q&A session with a few additional questions from the
community and decided to publish those questions and our answers along with some other
frequently asked questions around the topic of links and JavaScript.

## What kinds of links can Googlebot discover?

Googlebot parses the HTML of a page, looking for links to discover the URLs of related pages to
crawl. To discover these pages, you need to make your links actual HTML links, as described in the
[webmaster guidelines on links](/search/docs/advanced/guidelines/links-crawlable).

## What kind of URLs are okay for Googlebot?

Googlebot extracts the URLs from the href attribute of your links and then enqueues them for
crawling. This means that the URL needs to be resolvable or simply put: The URL should work when
put into the address bar of a browser. See the
[webmaster guidelines on links](/search/docs/advanced/guidelines/links-crawlable)
for more information.

## Is it okay to use JavaScript to create and inject links?

As long as these links fulfill the criteria as per our
[webmaster guidelines](/search/docs/advanced/guidelines/links-crawlable)
and outlined above, yes.

When Googlebot renders a page, it executes JavaScript and then discovers the links generated from
JavaScript, too. It's worth mentioning that link discovery can happen twice: Before *and*
after JavaScript executed, so having your links in the initial server response allows Googlebot
to discover your links a bit faster.

## Does Googlebot understand fragment URLs?

Fragment URLs, also known as "hash URLs", are technically fine, but might not work the way you
expect with Googlebot.

Fragments are supposed to be used to address a piece of content within the page and when used for
this purpose, fragments are absolutely fine.

Sometimes developers decide to **use fragments with JavaScript to load different content**
than what is on the page without the fragment. That is not what fragments are meant for and won't work with Googlebot. See
[the JavaScript SEO guide](/search/docs/crawling-indexing/javascript/javascript-seo-basics#use-history-api)
on how the History API can be used instead.

## Does Googlebot still use the AJAX crawling scheme?

The
[AJAX crawling scheme has long been deprecated](/search/blog/2015/10/deprecating-our-ajax-crawling-scheme).
Do not rely on it for your pages.

The recommendation for this is to use the
[History API](https://developer.mozilla.org/en/docs/Web/API/History)
and migrate your web apps to URLs that do not rely on fragments to load different content.

## Stay tuned for more Webmaster Conference Lightning Talks

This post was inspired by the first installment of the
[Webmaster Conference Lightning Talks](https://www.youtube.com/playlist?list=PLKoqnv2vTMUNf6w9wUu7RgxHkaTrq2Zpf), but make sure to
[subscribe to our YouTube channel](https://www.youtube.com/channel/UCWf2ZlNsCGDS89VBF_awNvA?sub_confirmation=1)
for more videos to come! We definitely recommend joining the premieres on YouTube to participate
in the live chat and Q&A session for each episode!

If you are interested to see more Webmaster Conference Lightning Talks, check out the video
[Google Monetized Policies](https://www.youtube.com/watch?v=bB2FrOyKKuA&list=PLKoqnv2vTMUNf6w9wUu7RgxHkaTrq2Zpf)
and subscribe to our channel to stay tuned for the next one!

Join the webmaster community in the upcoming video premieres and in the YouTube comments!
