---
title: "How to showcase your events on Google Search"
source: google-search-central-blog
content_type: "event"
freshness_risk: "historical"
slug: "2020-02-events-on-search"
url: "https://developers.google.com/search/blog/2020/02/events-on-search"
canonical: "https://developers.google.com/search/blog/2020/02/events-on-search"
author: "Emily Fifer, Product Manager"
published: "2020-02-25T00:00:00+00:00"
updated: "2020-02-25T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:36:06+00:00"
status_code: 200
html_hash: "332c46f8bc574c3da2b3cd66f5e0736fa3c7e9c570ca7f99d1f8f4d0f1e1fb89"
clean_word_count: 669
clean_char_count: 4474
---
# How to showcase your events on Google Search

It's officially 2020 and people are starting to make plans for the year ahead. If you produce
any type of event, you can help people discover your events with the event search experience on
Google.

Have a concert or hosting a workshop? Event markup allows people to discover your event when
they search for "concerts this weekend" or "workshops near me." People can also discover your
event when they search for venues, such as sports stadiums or a local pub. Events may surface
in a given venue's
[Knowledge Panel](https://support.google.com/knowledgepanel/answer/9163198)
to better help people find out what's happening at that respective location.

![Screenshots of clicking on an event in Search](/static/search/blog/images/import/b6558c62b1e66641a72e63b631e995c9.png)
![Sample event landing page screenshot](/static/search/blog/images/import/2749ea50703c0e53df593ce0820e7454.png)

## Launching in new regions and languages

We recently launched the event search experience in
[Germany](/search/blog/2019/12/events-launching-germany-spain?hl=de)
and
[Spain](/search/blog/2019/12/events-launching-germany-spain?hl=es),
which brings the event search experience on Google to nine countries and regions around the
world. For a full list of where the event search experience works, check out the
[list of available languages and regions](/search/docs/appearance/structured-data/event#region-availability).

## How to get your events on Google

There are three options to make your events eligible to appear on Google:

- If you use a third-party website to post events (for example, you post events on ticketing
  websites or social platforms), check to see if your event publisher is already participating
  in the event search experience on Google. One way to check is to search for a popular event
  shown on the platform and see if the event listing is shown. If your event publisher is
  integrated with Google, continue to post your events on the third-party website.
- If you use a CMS (for example, WordPress) and you don't have access to your HTML, check with
  your CMS to see if there's a plugin that can add structured data to your site for you.
  Alternatively, you can use the
  [Data Highlighter](https://support.google.com/webmasters/answer/2774099)
  to tell Google about your events without editing the HTML of your site.
- If you're comfortable editing your HTML,
  [use structured data to directly integrate](/search/docs/appearance/structured-data/event#integrate)
  with Google. You'll need to edit the HTML of the event pages.

## Follow best practices

If you've already implemented event structured data, we recommend that you review your
structured data to make sure it meets our guidelines. In particular, you should:

- Make sure you're including the required and recommended properties that are outlined in our
  [developer guidelines](/search/docs/appearance/structured-data/event#datatypes).
- Make sure your event details are high quality, as defined by
  [our guidelines](/search/docs/appearance/structured-data/event#guidelines). For example, use the
  description field to describe the event itself in more detail instead of repeating attributes
  such as title, date, location, or highlighting other website functionality.
- Use the
  [Rich Result Test](https://search.google.com/test/rich-results)
  to
  [test and preview your structured data](https://support.google.com/webmasters/answer/7445569).

## Monitor your performance on Search

You can check how people are interacting with your event postings with Search Console:

- Use the
  [Performance Report](https://support.google.com/webmasters/answer/7576553)
  in Search Console to show
  [event listing or detail](https://support.google.com/webmasters/answer/7042828#job)
  view data for a given event posting in Search results. You can automatically pull these results with the
  [Search Console API](/webmaster-tools/search-console-api-original/v3/how-tos/search_analytics).
- Use the
  [Rich result status report](https://support.google.com/webmasters/answer/7552505)
  in Search Console to understand what Google could or could not read from your site, and troubleshoot rich result errors.

![Search Console Rich Results report](/static/search/blog/images/import/9eb547e5e453bb20b57f84b9be5f82ff.png)

If you have any questions, please visit the
[Webmaster Central Help Forum](https://support.google.com/webmasters/community/).
