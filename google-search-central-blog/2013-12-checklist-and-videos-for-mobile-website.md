---
title: "Checklist and videos for mobile website improvement"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2013-12-checklist-and-videos-for-mobile-website"
url: "https://developers.google.com/search/blog/2013/12/checklist-and-videos-for-mobile-website"
canonical: "https://developers.google.com/search/blog/2013/12/checklist-and-videos-for-mobile-website"
author: "Maile Ohye"
published: "2013-12-10T00:00:00+00:00"
updated: "2013-12-10T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2013_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:23:06+00:00"
status_code: 200
html_hash: "76a0ffbd861cf0ff96c627767ebf69dd408d1aa69490c809387b9c97ea819345"
clean_word_count: 558
clean_char_count: 4422
---
# Checklist and videos for mobile website improvement

Unsure where to begin improving your smartphone website? Wondering how to prioritize all the
advice? We just published a checklist to help provide an efficient approach to mobile website
improvement. Several topics in the checklist link to a relevant business case or study, other
topics include a video explaining how to make data from Google Analytics and Webmaster Tools
actionable during the improvement process. Copied below are shortened sections of the
[full checklist](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing). Please let us know if there's more
you'd like to see, or if you have additional topics for us to include.

## Step 1: Stop frustrating your customers

- Remove cumbersome extra windows from all mobile user-agents |
  [Google recommendation](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing),
  [Most hated advertising techniques](https://www.nngroup.com/articles/most-hated-advertising-techniques/)

- JavaScript pop-ups that can be difficult to close.
- Overlays, especially to download apps (instead consider a banner such as
  [iOS 6+ Smart App Banners](https://developer.apple.com/library/ios/documentation/AppleApplications/Reference/SafariWebContent/PromotingAppswithAppBanners/PromotingAppswithAppBanners)
  or equivalent, side navigation, email marketing, etc.).
- Survey requests prior to task completion.

- Provide device-appropriate functionality

- Remove features that require plugins or videos not available on a user's device (for example,
  Adobe Flash isn't playable on an iPhone or on Android versions 4.1 and higher). |
  [Business case](/search/blog/2013/06/changes-in-rankings-of-smartphone_11)
- Serve tablet users the desktop version (or if available, the tablet version). |
  [Study](https://www.nngroup.com/articles/tablet-usability/)
- Check that full desktop experience is accessible on mobile phones, and if selected, remains
  in full desktop version for duration of the session (that is, user isn't required to select
  "desktop version" after every page load). |
  [Study](https://www.nngroup.com/articles/mobile-site-vs-full-site/)

- Correct high traffic, poor user-experience mobile pages
- Make quick fixes in performance (and continue if behind competition) |
  [Business case](https://www.webperformancetoday.com/2011/11/23/case-study-slow-page-load-mobile-business-metrics/)
- To see all topics in "Stop frustrating your customers," please see the full
  [Checklist for mobile website improvement](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing).

## Step 2: Facilitate task completion

- Optimize crawling, indexing, and the searcher experience |
  [Business case](https://www.google.com/think/research-studies/mobile-path-to-purchase-5-key-findings)

- Unblock resources (CSS, JavaScript) that are robots.txt disallowed.
- Implement search-engine best practices given your mobile implementation:

- [Responsive design](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#responsive-design): Be sure
  to include CSS `@media` query.
- [Separate mobile site](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#separate-urls): Add
  `rel=alternate media` and `rel=canonical`, as well as
  `Vary: User-Agent` HTTP header which helps Google implement
  [Skip Redirect](/search/blog/2011/12/introducing-smartphone-googlebot-mobile).
- [Dynamic serving](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing): Include
  `Vary: User-Agent` HTTP header.

- Optimize popular mobile persona workflows for your site

## Step Three: Convert customers into fans!

- Consider search integration points with mobile apps |
  [Announcement](/search/blog/2013/10/indexing-apps-just-like-websites),
  [Information](https://firebase.google.com/docs/app-indexing/)
- Brainstorm new ways to provide value

- Build for mobile behavior, such as the in-store shopper. |
  [Business case](https://www.google.com/think/research-studies/mobile-in-store)
- Leverage smartphone GPS, camera, accelerometer.
- Increase sharing or social behavior. |
  [Business case](https://blogs.adobe.com/digitalmarketing/digital-marketing/mobile/adobe-2013-mobile-consumer-survey-71-of-people-use-mobile-to-access-social-media/)
- Consider intuitive/fun tactile functionality with swiping, shaking, tapping.
