---
title: "A spider's view of Web 2.0"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-11-spiders-view-of-web-20"
url: "https://developers.google.com/search/blog/2007/11/spiders-view-of-web-20"
canonical: "https://developers.google.com/search/blog/2007/11/spiders-view-of-web-20"
author: "Greg Grothaus"
published: "2007-11-07T00:00:00+00:00"
updated: "2007-11-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:50:51+00:00"
status_code: 200
html_hash: "bb2b50595aab10c7e718faa7dde57b50068c065971cc323778ec4884853c259b"
clean_word_count: 786
clean_char_count: 4938
---
# A spider's view of Web 2.0

Many webmasters have discovered the advantages of using Ajax to improve the user experience on
their sites, creating dynamic pages that act as powerful web applications. But, like Flash, Ajax
can make a site difficult for search engines to index if the technology is not implemented
carefully. As promised in our post answering questions about
[Server location, cross-linking, and Web 2.0 technology](/search/blog/2007/08/server-location-cross-linking-and-web),
we've compiled some tips for creating Ajax-enhanced websites that are also understood by search
engines.

## How will Google see my site?

One of the main issues with Ajax sites is that while Googlebot is great at following and
understanding the structure of HTML links, it can have a difficult time finding its way around
sites which use JavaScript for navigation. While we are working to better understand JavaScript,
your best bet for creating a site that's crawlable by Google and other search engines is to
provide HTML links to your content.

## Design for accessibility

We encourage webmasters to create pages for users, not just search engines. When you're designing
your Ajax site, think about the needs of your users, including those who may not be using a
JavaScript-capable browser. There are plenty of such users on the web, including those using
screen readers or mobile devices.

One of the easiest ways to test your site's accessibility to this type of user is to explore the
site in your browser with JavaScript turned off, or by viewing it in a text-only browser such as
[Lynx](https://en.wikipedia.org/wiki/Lynx_%28web_browser%29).
Viewing a site as text-only can also help you identify other content which may be hard for
Googlebot to see, including images and Flash.

## Develop with progressive enhancement

If you're starting from scratch, one good approach is to build your site's structure and
navigation using only HTML. Then, once you have the site's pages, links, and content in place,
you can spice up the appearance and interface with Ajax. Googlebot will be happy looking at the
HTML, while users with modern browsers can enjoy your Ajax bonuses.

Of course you will likely have links requiring JavaScript for Ajax functionality, so here's a way
to help Ajax and static links coexist:

When creating your links, format them so they'll offer a static link as well as calling a
JavaScript function. That way you'll have the Ajax functionality for JavaScript users, while
non-JavaScript users can ignore the script and follow the link. For example:

```
<a href="ajax.htm?foo=32" onClick="navigate('ajax.html#foo=32'); return false">foo 32</a>
```

Note that the static link's URL has a parameter (`?foo=32`) instead of a fragment
(`#foo=32`), which is used by the Ajax code. This is important, as search engines
understand URL parameters but often ignore fragments. Web developer
[Jeremy Keith](https://adactio.com/)
labeled this technique as
[Hijax](https://domscripting.com/presentations/xtech2006/). Since
you now offer static links, users and search engines can link to the exact content they want to
share or reference.

While we're constantly improving our crawling capability, using HTML links remains a strong way to
help us (as well as other search engines, mobile devices and users) better understand your site's
structure.

## Follow the guidelines

In addition to the tips described here, we encourage you to also check out our
[Webmaster Guidelines](/search/docs/essentials)
for more information about what can make a site good for Google and your users. The guidelines
also point out some practices to avoid, including
[sneaky JavaScript redirects](/search/docs/essentials/spam-policies#cloaking).
A general rule to follow is that while you can provide users different experiences based on their
capabilities, the content should remain the same. For example, imagine we've created a page for
Wysz's Hamster Farm. The top of the page has a heading of "Wysz's Hamster Farm," and below it is
an Ajax-powered slideshow of the latest hamster arrivals. Turning JavaScript off on the same page
shouldn't surprise a user with additional text reading:

> Wysz's Hamster Farm—hamsters, best hamsters, cheap hamsters, free hamsters, pets, farms,
> hamster farmers, dancing hamsters, rodents, hampsters, hamsers, best hamster resource, pet toys,
> dancing lessons, cute, hamster tricks, pet food, hamster habitat, hamster hotels, hamster
> birthday gift ideas and more!

A more ideal implementation would display the same text whether JavaScript was enabled or not, and
in the best scenario, offer an HTML version of the slideshow to non-JavaScript users.

This is a pretty advanced topic, so please
[continue the discussion](https://groups.google.com/group/Google_Webmaster_Help-Indexing/browse_thread/thread/dabe5ab778e8dd4)
by asking questions and sharing ideas over in the Webmaster Help Group. See you there!
