---
title: "A faster image search"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2013-01-faster-image-search"
url: "https://developers.google.com/search/blog/2013/01/faster-image-search"
canonical: "https://developers.google.com/search/blog/2013/01/faster-image-search"
author: "Hongyi Li"
published: "2013-01-24T00:00:00+00:00"
updated: "2013-01-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2013_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:20:53+00:00"
status_code: 200
html_hash: "80be5ea55c99aa13dcf91be29da2d762303b34acedf9bd4f600ebc86bacde270"
clean_word_count: 331
clean_char_count: 2003
---
# A faster image search

People looking for images on Google often want to browse through many images, looking both at the
images and their metadata (detailed information about the images). Based on feedback from both
users and webmasters, we redesigned Google Images to provide a better search experience. In the
next few days, you'll see image results displayed in an inline panel so it's faster, more
beautiful, and more reliable. You will be able to quickly flip through a set of images by using
the keyboard. If you want to go back to browsing other search results, just scroll down and pick
up right where you left off.

![New Google Images results using the query nasa earth as an example](/static/search/blog/images/import/0aaca32c929f36c666560dd7dce1066e.jpg)

Here's what it means for webmasters:

- We now display detailed information about the image (the metadata) right underneath the image
  in the search results, instead of redirecting users to a separate landing page.
- We're featuring some key information much more prominently next to the image: the title of the
  page hosting the image, the domain name it comes from, and the image size.
- The domain name is now clickable, and we also added a new button to visit the page the image is
  hosted on. This means that there are now four clickable targets to the source page instead of
  just two. In our tests, we've seen a net increase in the average click-through rate to the
  hosting website.
- The source page will no longer load up in an `iframe` in the background of the image
  detail view. This speeds up the experience for users, reduces the load on the source website's
  servers, and improves the accuracy of webmaster metrics such as pageviews. As usual, image
  search query data is available in
  [Top Search Queries](https://support.google.com/webmasters/answer/7576553)
  in Webmaster Tools.

As always, please ask on our
[Webmaster Help forum](https://support.google.com/webmasters/community)
if you have questions.
