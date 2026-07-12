---
title: "Troubleshooting Instant Previews in Webmaster Tools"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2011-05-troubleshooting-instant-previews-in"
url: "https://developers.google.com/search/blog/2011/05/troubleshooting-instant-previews-in"
canonical: "https://developers.google.com/search/blog/2011/05/troubleshooting-instant-previews-in"
author: "Michael Darweesh"
published: "2011-05-18T00:00:00+00:00"
updated: "2011-05-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:13:10+00:00"
status_code: 200
html_hash: "6d3ded42dc9f4b271d1607c6e00b9d7e87904c9a244f9010d0c1b71fbcdeaf09"
clean_word_count: 299
clean_char_count: 1906
---
# Troubleshooting Instant Previews in Webmaster Tools

In November, we
[launched Instant Previews](/search/blog/2010/11/instant-previews)
to help users better understand if a particular result was relevant for a their search query.
Since launch, our Instant Previews team has been keeping an eye on common complaints and problems
related to how pages are rendered for Instant Previews.

When we see issues with preview images, they are frequently due to:

- Blocked resources due to a robots.txt entry
- [Cloaking](/search/docs/essentials/spam-policies#cloaking): Erroneous content being served
  to the Googlebot user agent
- Poor alternative content when Flash is unavailable

To help webmasters diagnose these problems, we have a new Instant Preview tool in the Labs
section of
[Webmaster Tools](https://search.google.com/search-console)
(in English only for now).

![Instant Preview tool in Webmaster Tools Labs](/static/search/blog/images/import/549bf8478f95670e4c244eecd603c44f.png)

Here, you can input the URL of any page on your site. We will then fetch the page from your site
and try to render it both as it would display in Chrome and through our Instant Preview renderer.
Please keep in mind that both of these renders are done using a recent build of Webkit which does
not include plugins such as Flash or Silverlight, so it's important to consider the value of
providing alternative content for these situations. Alternative content can be helpful to search
engines, and visitors to your site without the plugin would benefit as well.

Below the renders, you'll also see automated feedback on problems our system can detect such as
missing or roboted resources. And, in the future, we plan to add more informative and timely
feedback to help improve your Instant Previews!

Please direct your questions and feedback to the
[Webmaster Forum](https://support.google.com/webmasters/community).
