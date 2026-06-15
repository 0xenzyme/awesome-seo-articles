---
title: "Making your site more mobile-friendly with PageSpeed Insights"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-05-making-your-site-more-mobile-friendly"
url: "https://developers.google.com/search/blog/2014/05/making-your-site-more-mobile-friendly"
canonical: "https://developers.google.com/search/blog/2014/05/making-your-site-more-mobile-friendly"
author: "Matthew Steele and Doantam Phan, PageSpeed Insights team"
published: "2014-05-19T00:00:00+00:00"
updated: "2014-05-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:24:35+00:00"
status_code: 200
html_hash: "27e3685c75ddbf99b2191017d6c7844a38960ec4857ba73ea3f05d7c3b4df809"
clean_word_count: 488
clean_char_count: 3309
---
# Making your site more mobile-friendly with PageSpeed Insights

To help developers and webmasters make their pages mobile-friendly, we recently updated PageSpeed
Insights with additional recommendations on mobile usability.

![](/static/search/blog/images/import/fb9b25d05ac03792f8d2e3abfbbf2bb1.png)

Poor usability can diminish the benefits of a fast page load. We know the average mobile page
takes
[more than 7 seconds to load](https://analytics.blogspot.com/2013/04/is-web-getting-faster.html),
and by using the
[PageSpeed Insights tool](https://pagespeed.web.dev/)
and following its speed recommendations, you can make your page
[load much faster](/search/blog/2013/08/making-smartphone-sites-load-fast). But suppose
your fast mobile site loads in just 2 seconds instead of 7 seconds. If mobile users still have to
spend another 5 seconds once the page loads to pinch-zoom and scroll the screen before they can
start reading the text and interacting with the page, then that site isn't really fast to use
after all. PageSpeed Insights' new User Experience rules can help you find and fix these usability
issues.

These new recommendations currently cover the following areas:

- **Configure the viewport** : Without a `meta-viewport` tag, modern mobile browsers
  will assume your page is not mobile-friendly, and will fall back to a desktop viewport and
  possibly apply font-boosting, interfering with your intended page layout.
  [Configuring the viewport](/speed/docs/insights/ConfigureViewport)
  to `width=device-width` should be your first step in mobilizing your site.
- **Size content to the viewport**: Users expect mobile sites to scroll vertically, not
  horizontally. Once you've configured your viewport, make sure your page content
  [fits the width of that viewport](/speed/docs/insights/SizeContentToViewport),
  keeping in mind that not all mobile devices are the same width.
- **Use legible font sizes**: If users have to zoom in just to be able read your article text
  on their smartphone screen, then your site isn't mobile-friendly. PageSpeed Insights checks that
  your site's
  [text is large enough](/speed/docs/insights/UseLegibleFontSizes)
  for most users to read comfortably.
- **Size tap targets appropriately**: Nothing's more frustrating than trying to tap a button or
  link on a phone or tablet touchscreen, and accidentally hitting the wrong one because your
  finger pad is much bigger than a desktop mouse cursor. Make sure that your mobile site's
  touchscreen
  [tap targets are large enough](/speed/docs/insights/SizeTapTargetsAppropriately)
  to press easily.
- **Avoid plugins**: Most smartphones don't support Flash or other browser plugins, so make
  sure your mobile site
  [doesn't rely on plugins](/speed/docs/insights/AvoidPlugins).

These rules are described in more detail in
[our help pages](/speed/docs/insights/rules). When you're ready,
you can test your pages and the improvements you make using the
[PageSpeed Insights tool](https://pagespeed.web.dev/).
We've also updated PageSpeed Insights to use a mobile friendly design, and we've translated our
documents into additional languages.

As always, if you have any questions or feedback, please post in our
[discussion group](https://groups.google.com/forum/#!forum/pagespeed-insights-discuss).
