---
title: "Google+: A case study on App Download Interstitials"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-07-google-case-study-on-app-download-interstitials"
url: "https://developers.google.com/search/blog/2015/07/google-case-study-on-app-download-interstitials"
canonical: "https://developers.google.com/search/blog/2015/07/google-case-study-on-app-download-interstitials"
author: "David Morell, Software Engineer, Google+"
published: "2015-07-23T00:00:00+00:00"
updated: "2015-07-23T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:27:00+00:00"
status_code: 200
html_hash: "a7983b0c62efeb247dddb3a8af581cc09f9bb35e081ebcbe2a048215bfd055e0"
clean_word_count: 470
clean_char_count: 2921
---
# Google+: A case study on App Download Interstitials

Many mobile sites use promotional app interstitials to encourage users to download their native
mobile apps. For some apps, native can provide richer user experiences, and use features of the
device that are currently not easy to access on a browser. Because of this, many app owners
believe that they should encourage users to install the native version of their online property or
service. It's not clear how aggressively to promote the apps, and a full page interstitial can
interrupt the user from reaching their desired content.

![](/static/search/blog/images/archived_JLZQi7nFSxzyDJjJju5fEoYdzxtWHb8Dr8KXmEb9RZ3_3avuJr.png)

On Google+ mobile web, we decided to take a closer look at our own use of interstitials. Internal
user experience studies identified them as poor experiences, and Jennifer Gove gave a
[great talk](https://www.youtube.com/watch?v=xqviGwyy7y0&t=36m33s)
at IO last year which highlights this user frustration.

Despite our intuition that we should remove the interstitial, we prefer to let data guide our
decisions, so we set out to learn how the interstitial affected our users. Our analysis found
that:

- 9% of the visits to our interstitial page resulted in the 'Get App' button being pressed. (Note
  that some percentage of these users already have the app installed or may never follow through
  with the app store download.)
- 69% of the visits abandoned our page. These users neither went to the app store nor continued to
  our mobile website.

While 9% sounds like a great CTR for any campaign, we were much more focused on the number of
users who had abandoned our product due to the friction in their experience. With this data in
hand, in July 2014, we decided to run an experiment and see how removing the interstitial would
affect actual product usage. We added a Smart App Banner to continue promoting the native app in a
less intrusive way, as recommended in the
[Avoid common mistakes](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#app-download-interstitials)
section of our Mobile SEO Guide. The results were surprising:

- 1-day active users on our mobile website increased by 17%.
- G+ iOS native app installs were mostly unaffected (-2%). (We're not reporting install numbers
  from Android devices since most come with Google+ installed.)

Based on these results, we decided to permanently retire the interstitial. We believe that the
increase in users on our product makes this a net positive change, and we are sharing this with
the hope that you will reconsider the use of promotional interstitials. Let's remove friction and
make the mobile web more useful and usable!

*(Since this study, we launched a
[better mobile web experience](https://plus.google.com/+googleplus/posts/WcNhWwkvVDD)
that is currently without an app banner. The banner can still be seen on iOS 6 and below.)*
