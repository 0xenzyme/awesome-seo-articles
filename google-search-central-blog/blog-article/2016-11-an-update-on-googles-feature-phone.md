---
title: "An update on Google's feature-phone crawling and indexing"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2016-11-an-update-on-googles-feature-phone"
url: "https://developers.google.com/search/blog/2016/11/an-update-on-googles-feature-phone"
canonical: "https://developers.google.com/search/blog/2016/11/an-update-on-googles-feature-phone"
author: "John Mueller"
published: "2016-11-30T00:00:00+00:00"
updated: "2016-11-30T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2016_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:29:36+00:00"
status_code: 200
html_hash: "28d3cda53a1ac62a0c8a8848a7d13c72469b2defbf2929e3142e55d6787afd23"
clean_word_count: 365
clean_char_count: 2633
---
# An update on Google's feature-phone crawling and indexing

Limited mobile devices,
"[feature-phones](https://www.google.com/search?q=wap+OR+wml+feature+phones&source=lnms&tbm=isch)",
require a special form of markup or a transcoder for web content. Most websites don't provide
feature-phone-compatible content in WAP/WML any more. Given these developments, we've made changes
in how we crawl feature-phone content (note: these changes don't affect smartphone content):

1. **We've retired the feature-phone Googlebot**: We won't be using the feature-phone
   user agents for crawling for search going forward.
2. **Use "handheld" link annotations for dynamic serving of feature-phone content**:
   Some sites provide content for feature-phones through dynamic serving, based on the user's
   user agent. To understand this configuration, make sure your desktop and smartphone pages have
   a self-referential alternate URL link for handheld (feature-phone) devices:

   ```
    <link rel="alternate" media="handheld" href="[current page URL]" />
   ```

   This is a change from our previous guidance of only using the `vary: user-agent`
   HTTP header. We've updated our documentation on
   [making feature-phone pages](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#feature-phones)
   accordingly. We hope adding this link element is possible on your side, and thank you for your
   help in this regard. We'll continue to show feature-phone URLs in Search when we can recognize
   them, and when they're appropriate for users.
3. **We're retiring feature-phone tools in Search Console**: Without the
   feature-phone Googlebot, special sitemaps extensions for feature-phone, the Fetch as Google
   feature-phone options, and feature-phone crawl errors are no longer needed. We continue to
   support
   [sitemaps](https://www.sitemaps.org/index.html) and other sitemap
   extensions (such as for [videos](/search/docs/crawling-indexing/sitemaps/video-sitemaps) or
   [Google News](/search/docs/crawling-indexing/sitemaps/news-sitemap)), as well as the other
   [Fetch as Google](https://support.google.com/webmasters/answer/6066468)
   options in
   [Search Console](https://search.google.com/search-console).

We've worked to make these changes as minimal as possible. Most websites don't serve feature-phone
content, and wouldn't be affected. If your site has been providing feature-phone content, we thank
you for your help in bringing the Internet to feature-phone users worldwide!

For any questions, you can drop by our
[Webmaster Help Forums](https://support.google.com/webmasters/go/community)!
