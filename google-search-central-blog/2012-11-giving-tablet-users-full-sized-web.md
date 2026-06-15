---
title: "Giving Tablet Users the Full-Sized Web"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-11-giving-tablet-users-full-sized-web"
url: "https://developers.google.com/search/blog/2012/11/giving-tablet-users-full-sized-web"
canonical: "https://developers.google.com/search/blog/2012/11/giving-tablet-users-full-sized-web"
author: "Pierre Far, Scott Main"
published: "2012-11-12T00:00:00+00:00"
updated: "2012-11-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:20:31+00:00"
status_code: 200
html_hash: "42bcccb7b2b570a909432c35e8e05f598f09b39fd38792c1c36bb8d2ea623cf6"
clean_word_count: 544
clean_char_count: 3504
---
# Giving Tablet Users the Full-Sized Web

Since we announced Google's recommendations for building smartphone-optimized websites, a common
question we've heard from webmasters is how to best treat tablet devices. This is a similar
question Android app developers face, and for that the
[Building Quality Tablet Apps](https://android-developers.blogspot.com/2012/10/building-quality-tablet-apps.html)
guide is a great starting point.

Although we do not have specific recommendations for building search engine friendly
tablet-optimized websites, there are some tips for building websites that serve smartphone and
tablet users well.

When considering your site's visitors using tablets, it's important to think about both the
devices and what users expect. Compared to smartphones, tablets have larger touch screens and are
typically used on Wi-Fi connections. Tablets offer a browsing experience that can be as rich as
any desktop or laptop machine, in a more mobile, lightweight, and generally more convenient
package. **This means that, unless you offer tablet-optimized content, users expect to see
your desktop site rather than your site's smartphone site.**

![The NY Times mobile and tablet experience](/static/search/blog/images/archived_1_tablet-web.png)

Our recommendation for smartphone-optimized sites is to
[use responsive web design](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing), which means you have one
site to serve all devices. If your website uses responsive web design as recommended, be sure to
test your website on a variety of tablets to make sure it serves them well too. Remember, just
like for smartphones, there are a variety of device sizes and screen resolutions to test.

Another common configuration is to have separate sites for desktops and smartphones, and to
redirect users to the relevant version. If you use this configuration, be careful not to
inadvertently redirect tablet users to the smartphone-optimized site too.

### Telling Android smartphones and tablets apart

For Android-based devices, it's easy to distinguish between smartphones and tablets using the
user-agent string supplied by browsers: Although both Android smartphones and tablets will include
the word "Android" in the user-agent string, only the user-agent of smartphones will include the
word "Mobile".

In summary, any Android device that does not have the word "Mobile" in the user-agent is a tablet
(or other large screen) device that is best served the desktop site.

For example, here's the user-agent from Chrome on a Galaxy Nexus smartphone:

```
Mozilla/5.0 (Linux; Android 4.1.1; Galaxy Nexus Build/JRO03O) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19
```

Or from Firefox on the Galaxy Nexus:

```
Mozilla/5.0 (Android; Mobile; rv:16.0) Gecko/16.0 Firefox/16.0
```

Compare those to the user-agent from Chrome on Nexus 7:

```
Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03S) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
```

Or from Firefox on Nexus 7:

```
Mozilla/5.0 (Android; Tablet; rv:16.0) Gecko/16.0 Firefox/16.0
```

Because the Galaxy Nexus's user agent includes "Mobile" it should be served your
smartphone-optimized website, while the Nexus 7 should receive the full site.

We hope this helps you build better tablet-optimized websites. As always, please ask on our
[Webmaster Help forums](https://support.google.com/webmasters/community)
if you have more questions.
