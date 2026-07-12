---
title: "Optimizing for Bandwidth on Apache and Nginx"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-09-optimizing-for-bandwidth-on-apache-and"
url: "https://developers.google.com/search/blog/2014/09/optimizing-for-bandwidth-on-apache-and"
canonical: "https://developers.google.com/search/blog/2014/09/optimizing-for-bandwidth-on-apache-and"
author: "Jeff Kaufman, Make the Web Fast"
published: "2014-09-04T00:00:00+00:00"
updated: "2014-09-04T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:25:27+00:00"
status_code: 200
html_hash: "20e29ec3bcc0d5fa3e8b04882706eef111f40d1e77bb97e4be0f698dc6f0d54b"
clean_word_count: 421
clean_char_count: 2770
---
# Optimizing for Bandwidth on Apache and Nginx

Everyone wants to use less bandwidth: hosts want lower bills, mobile users want to stay under
their limits, and no one wants to wait for unnecessary bytes. The web is full of opportunities to
save bandwidth: pages served without gzip, stylesheets and JavaScript served unminified, and
unoptimized images, just to name a few.

So why isn't the web already optimized for bandwidth? If these savings are good for everyone then
why haven't they been fixed yet? Mostly it's just been too much hassle. Web designers are
encouraged to "save for web" when exporting their artwork, but they don't always remember.
JavaScript programmers don't like working with minified code because it makes debugging harder.
You can set up a custom pipeline that makes sure each of these optimizations is applied to your
site every time as part of your development or deployment process, but that's a lot of work.

An easy solution for web users is to use an optimizing proxy, like
[Chrome's](https://developer.chrome.com/multidevice/data-compression).
When users opt into this service their HTTP traffic goes via Google's proxy, which optimizes their
page loads and cuts bandwidth usage by 50%. While this is great for these users, it's limited to
people using Chrome who turn the feature on and it can't optimize HTTPS traffic.

With
[Optimize for Bandwidth](/speed/pagespeed/module/optimize-for-bandwidth),
the PageSpeed team is bringing this same technology to webmasters so that everyone can benefit:
users of other browsers, secure sites, desktop users, and site owners who want to bring down their
outbound traffic bills. Just install the
[PageSpeed module](/speed/pagespeed/module)
on your Apache or Nginx server[1](#1),
[turn on](/speed/pagespeed/module/optimize-for-bandwidth)
Optimize for Bandwidth in your configuration, and PageSpeed will do the rest.

If you later decide you're interested in PageSpeed's more advanced optimizations, from
[cache extension](/speed/pagespeed/module/filter-cache-extend)
and
[inlining](/speed/pagespeed/module/filter-js-inline)
to the more aggressive
[image lazyloading](/speed/pagespeed/module/filter-lazyload-images)
and
[defer JavaScript](/speed/pagespeed/module/filter-js-defer),
it's just a matter of enabling them in your PageSpeed configuration.

Learn more about
[installing PageSpeed](/speed/pagespeed/module) or
[enabling Optimize for Bandwidth](/speed/pagespeed/module/optimize-for-bandwidth).

1: If you're using a different web server, consider running PageSpeed on an
Apache or Nginx proxy. And it's all
[open source](https://github.com/apache/incubator-pagespeed-mod),
with porting efforts underway for
[IIS](https://www.iispeed.com/),
[ATS](https://www.atspagespeed.com/), and others.
