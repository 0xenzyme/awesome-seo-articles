---
title: "Mobile-first indexing"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2016-11-mobile-first-indexing"
url: "https://developers.google.com/search/blog/2016/11/mobile-first-indexing"
canonical: "https://developers.google.com/search/blog/2016/11/mobile-first-indexing"
author: "Doantam Phan, Product Manager"
published: "2016-11-04T00:00:00+00:00"
updated: "2016-11-04T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2016_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:29:44+00:00"
status_code: 200
html_hash: "b547454449e1e97043ad1c79392da2831793168b5606c577bed47b8f4e6f9487"
clean_word_count: 545
clean_char_count: 3489
---
# Mobile-first indexing

Today, most people are searching on Google using a mobile device. However, our ranking systems
still typically look at the desktop version of a page's content to evaluate its relevance to the
user. This can cause issues when the mobile page has less content than the desktop page because
our algorithms are not evaluating the actual page that is seen by a mobile searcher.

To make our results more useful, we've begun experiments to make our index mobile-first. Although
our search index will continue to be a single index of websites and apps, our algorithms will
eventually primarily use the mobile version of a site's content to rank pages from that site, to
understand structured data, and to show snippets from those pages in our results. Of course, while
our index will be built from mobile documents, we're going to continue to build a great search
experience for all users, whether they come from mobile or desktop devices.

We understand this is an important shift in our indexing and it's one we take seriously. We'll
continue to carefully experiment over the coming months on a small scale and we'll ramp up this
change when we're confident that we have a great user experience. Though we're only beginning this
process, here are a few recommendations to help webmasters prepare as we move towards a more
mobile-focused index.

- If you have a [responsive site](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#responsive-design) or
  a [dynamic serving site](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) where the
  primary content and markup is equivalent across mobile and desktop, you shouldn't have to change
  anything.
- If you have a [site configuration](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) where the
  primary content and markup is different across mobile and desktop, you should consider making
  some changes to your site.

- Make sure to serve structured markup for both the desktop and mobile version.

  Sites can verify the equivalence of their structured markup across desktop and mobile by typing
  the URLs of both versions into the
  [Structured Data Testing Tool](/search/docs/advanced/structured-data)
  and comparing the output.

  When adding structured data to a mobile site, avoid adding large amounts of markup that isn't
  relevant to the specific information content of each document.
- Use the
  [robots.txt testing tool](https://support.google.com/webmasters/answer/6062598)
  to verify that your mobile version is accessible to Googlebot.
- Sites do not have to make changes to their
  [canonical links](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#separate-urls); we'll continue to
  use these links as guides to serve the appropriate results to a user searching on desktop or
  mobile.

- If you are a site owner who has only verified their desktop site in Search Console,
  [please add and verify your mobile version](https://support.google.com/webmasters/answer/35179).
- If you only have a desktop site, we'll continue to index your desktop site just fine, even if
  we're using a mobile user agent to view your site.

If you have any questions, you can contact us via the
[Webmaster forums](https://support.google.com/webmasters/go/community)
or our [public events](/search/events). We anticipate this change will
take some time and we'll update you as we make progress on migrating our systems.
