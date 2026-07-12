---
title: "Here's to more HTTPS on the web!"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2016-11-heres-to-more-https-on-web"
url: "https://developers.google.com/search/blog/2016/11/heres-to-more-https-on-web"
canonical: "https://developers.google.com/search/blog/2016/11/heres-to-more-https-on-web"
author: "Adriana Porter Felt"
published: "2016-11-04T00:00:00+00:00"
updated: "2016-11-04T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2016_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:29:41+00:00"
status_code: 200
html_hash: "b4ccd2aed0c8c53f7fb259c99640c718d38b71b35573a3fc51e747ff995f9c64"
clean_word_count: 666
clean_char_count: 4497
---
# Here's to more HTTPS on the web!

*Cross-posted from the
[Google Security Blog](https://security.googleblog.com/2016/11/heres-to-more-https-on-web.html)*.

Security has always been critical to the web, but challenges involved in site migration have
inhibited HTTPS adoption for several years. In the interest of a safer web for all, at Google
we've worked alongside many others across the online ecosystem to better understand and address
these challenges, resulting in real change. A web with ubiquitous HTTPS is not the distant future.
It's happening now, with secure browsing becoming standard for users of Chrome.

Today, we're adding a
[new section to the HTTPS Report Card in our Transparency Report](https://www.google.com/transparencyreport/https/metrics/)
that includes data about how HTTPS usage has been increasing over time. More than half of pages
loaded and two-thirds of total time spent by Chrome desktop users occur via HTTPS, and we expect
these metrics to continue their strong upward trajectory.

![](/static/search/blog/images/import/4574e2cc5c47d3837e52740f2a2052b1.png "Percentage of pages loaded over HTTPS in Chrome")

As the remainder of the web transitions to HTTPS, we'll continue working to ensure that migrating
to HTTPS is a no-brainer, providing business benefit beyond increased security. HTTPS currently
enables the [best](https://istlsfastyet.com/)
[performance](https://blog.chromium.org/2013/11/making-web-faster-with-spdy-and-http2.html)
the web offers and powerful features that [benefit](/web/showcase)
site conversions, including both new features such as
[service workers](/web/fundamentals/getting-started/primers/service-workers)
or offline support and
[web push notifications](https://www.mobify.com/insights/google-web-push-notifications-case-study/),
and existing features such as
[credit card autofill](/web/updates/2015/06/checkout-faster-with-autofill)
and the
[HTML5 geolocation API](/web/updates/2016/04/geolocation-on-secure-contexts-only)
that are
[too powerful to be used](https://www.chromium.org/Home/chromium-security/deprecating-powerful-features-on-insecure-origins)
over non-secure HTTP. As with all major site migrations, there are certain steps that site owners
should take to ensure that search ranking transitions are smooth when moving to HTTPS. To help
with this, we've posted
[FAQs](/search/docs/crawling-indexing/site-move-with-url-changes#http-to-https-migration-faqs)
to help sites transition correctly, and will continue to improve our
[web fundamentals guidance](/web/fundamentals/security/encrypt-in-transit/why-https).

We've seen many sites successfully transition with negligible effect on their search ranking and
traffic. Brian Wood, Director of Marketing SEO at Wayfair, a large retail site, commented: "We
were able to migrate Wayfair.com to HTTPS with no meaningful impact to Google rankings or Google
organic search traffic. We are very pleased to say that all Wayfair sites are now fully HTTPS."
CNET, a large tech news site, had a similar experience: "We successfully completed our move of
CNET.com to HTTPS last month," said John Sherwood, Vice President of Engineering and Technology
at CNET. "Since then, there has been no change in our Google rankings or Google organic search
traffic."

Site owners that include ads on their sites also should carefully monitor ad performance and
revenue during large site migrations. The portion of Google ad traffic served over HTTPS has
[increased dramatically](https://transparencyreport.google.com/https/overview) over the past 3 years.
All ads that come from any Google source always support HTTPS, including AdWords, AdSense, or
DoubleClick Ad Exchange; ads sold directly, such as those through DoubleClick for Publishers,
still need to be designed to be HTTPS-friendly. This means there will be no change to the
Google-sourced ads that appear on a site after migrating to HTTPS. Many publishing partners have
seen this in practice after a successful HTTPS transition. Jason Tollestrup, Director of
Programmatic Advertising for the
[Washington Post](https://developer.washingtonpost.com/pb/blog/post/2015/12/10/moving-the-washington-post-to-https/),
"saw no material impact to AdX revenue with the transition to SSL."

As migrating to HTTPS becomes even easier,
[we'll continue](https://security.googleblog.com/2016/09/moving-towards-more-secure-web.html)
working towards a web that's secure by default. Don't hesitate to start planning your HTTPS migration today!
