---
title: "A reminder about widget links"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2016-09-a-reminder-about-widget-links"
url: "https://developers.google.com/search/blog/2016/09/a-reminder-about-widget-links"
canonical: "https://developers.google.com/search/blog/2016/09/a-reminder-about-widget-links"
author: "Agnieszka Łata, Trust and Safety Search Team and Eric Kuan, Webmaster Relations Specialist"
published: "2016-09-08T00:00:00+00:00"
updated: "2016-09-08T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2016_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:29:10+00:00"
status_code: 200
html_hash: "cc0e37e4ba5113255674c128d04cc381d898e0e59674f3e4f4d9274a33e4821d"
clean_word_count: 410
clean_char_count: 2796
---
# A reminder about widget links

Google has long taken a
[strong stance](/search/blog/2013/02/a-reminder-about-selling-links)
[against links](/search/blog/2012/07/new-notifications-about-inbound-links)
[that manipulate a site's PageRank](/search/blog/2008/10/linking-out-often-its-just-applying).
Today we would like to reiterate our policy on the creation of keyword-rich, hidden or low-quality
links embedded in widgets that are distributed across various sites.

Widgets can help website owners enrich the experience of their site and engage users. However,
some widgets add links to a site that a webmaster did not editorially place and contain anchor
text that the webmaster does not control. Because these links are not naturally placed, they're
considered a violation of Google Webmaster Guidelines.

Below you can find the examples of widgets which contain links that violate Google Webmaster
Guidelines:

![](/static/search/blog/images/import/61d445873008f0b13ecb6b2144094835.png)
![](/static/search/blog/images/import/7dd0c289bcaffce7b8bfba8909f89aa0.png)
![](/static/search/blog/images/import/7960eca6358a26c7500d19a092b8c777.png)

Google's webspam team may take
[manual actions](https://support.google.com/webmasters/answer/2604824)
on [unnatural links](/search/docs/essentials/spam-policies#link-spam). When a manual
action is taken, Google will notify the site owners through
[Search Console](https://search.google.com/search-console). If you
receive such a warning for unnatural links to your site and you use links in widgets to promote
your site, we recommend resolving these issues and requesting reconsideration.

You can resolve issues with unnatural links by making sure they don't pass PageRank. To do this,
add a `rel="nofollow"` attribute on the widget links or remove the links entirely.
After fixing or removing widget links and any other unnatural links to your site, let Google know
about your change by
[submitting a reconsideration request in Search Console](https://support.google.com/webmasters/answer/35843).
Once the request has been reviewed, you'll get a notification about whether the reconsideration
request was successful or not.

Also, we would like to remind webmasters who use widgets on their sites to check those widgets for
any unnatural links. Add a `rel="nofollow"` attribute on those unnatural links or
remove the links entirely from the widget.

For more information, please watch our
[video about widget links](https://www.youtube.com/watch?v=chuhSmwsL7s)
and refer to our
[Webmaster Guidelines on Link Schemes](/search/docs/essentials/spam-policies#link-spam).
Additionally, you can ask questions in our
[Webmaster Help Forums](https://support.google.com/webmasters/go/community),
where a community of webmasters can help with their experience.
