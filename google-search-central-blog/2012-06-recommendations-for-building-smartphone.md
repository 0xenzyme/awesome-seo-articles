---
title: "Recommendations for building smartphone-optimized websites"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-06-recommendations-for-building-smartphone"
url: "https://developers.google.com/search/blog/2012/06/recommendations-for-building-smartphone"
canonical: "https://developers.google.com/search/blog/2012/06/recommendations-for-building-smartphone"
author: "Pierre Far"
published: "2012-06-06T00:00:00+00:00"
updated: "2012-06-06T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:19:26+00:00"
status_code: 200
html_hash: "d94ce29b8ed1dde9afc7fdc360ff5a470357c3de071e4b6e95bc8324ec16927b"
clean_word_count: 685
clean_char_count: 4595
---
# Recommendations for building smartphone-optimized websites

Every day more and more smartphones get activated and more websites are producing
smartphone-optimized content. Since we
[last](/search/blog/2011/02/making-websites-mobile-friendly) talked about how to build
mobile-friendly websites, we've been working hard on improving Google's support for
smartphone-optimized content. As part of this effort, we launched
[Googlebot-Mobile for smartphones](/search/blog/2011/12/introducing-smartphone-googlebot-mobile)
back in December 2011, which is specifically tasked with identifying such content.

Today we'd like to give you Google's recommendations for building smartphone-optimized websites
and explain how to do so in a way that gives both your desktop- and smartphone-optimized sites the
best chance of performing well in Google's search results.

## Recommendations for smartphone-optimized sites

The full details of our recommendation can be found in our
[new help site](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing), which we now summarize.

When building a website that targets smartphones, Google supports three different configurations:

1. Sites that use responsive web design, that is, sites that serve all devices on the same set of
   URLs, with each URL serving the same HTML to all devices and using just CSS to change how the
   page is rendered on the device. **This is Google's recommended configuration**.
2. Sites that dynamically serve all devices on the same set of URLs, but each URL serves different
   HTML (and CSS) depending on whether the user agent is a desktop or a mobile device.
3. Sites that have a separate mobile and desktop sites.

## Responsive web design

Responsive web design is a technique to build web pages that alter how they look using CSS3 media
queries. That is, there is one HTML code for the page regardless of the device accessing it, but
its presentation changes using CSS media queries to specify which CSS rules apply for the browser
displaying the page. You can learn more about responsive web design from
[this blog post](/search/blog/2012/04/responsive-design-harnessing-power-of)
by Google's webmasters and
[in our recommendations](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing).

Using responsive web design has multiple advantages, including:

- It keeps your desktop and mobile content on a single URL, which is easier for your users to
  interact with, share, and link to and for Google's algorithms to assign the indexing properties
  to your content.
- Google can discover your content more efficiently as we wouldn't need to crawl a page with the
  different Googlebot user agents to retrieve and index all the content.

## Device-specific HTML

However, we appreciate that for many situations it may not be possible or appropriate to use
responsive web design. That's why we support having websites serve equivalent content using
different, device-specific, HTML. The device-specific HTML can be served on the same URL (a
configuration called dynamic serving) or different URLs (such as www.example.com and
m.example.com).

If your website uses a dynamic serving configuration, we strongly recommend using the
`Vary` HTTP header to communicate to caching servers and our algorithms that the
content may change for different user agents requesting the page. We also use this as a crawling
signal for [Googlebot-Mobile](/search/docs/crawling-indexing/googlebot).

As for the separate mobile site configuration, since there are many ways to do this, our
recommendation introduces annotations that communicate to our algorithms that your desktop and
mobile pages are equivalent in purpose; that is, the new annotations describe the relationship
between the desktop and mobile content as alternatives of each other and should be treated as a
single entity with each alternative targeting a specific class of device.

These annotations will help us discover your smartphone-optimized content and help our algorithms
understand the structure of your content, giving it the best chance of performing well in our
search results.

## Conclusion

This blog post is only a brief summary of our recommendation for
[building smartphone-optimized websites](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing). Please read
the full recommendation and see which supported implementation is most suitable for your site and
users. And, as always, please ask on our
[Webmaster Help forums](https://support.google.com/webmasters/community)
if you have more questions.
