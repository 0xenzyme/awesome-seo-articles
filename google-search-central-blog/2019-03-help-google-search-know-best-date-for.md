---
title: "Help Google Search know the best date for your web page"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2019-03-help-google-search-know-best-date-for"
url: "https://developers.google.com/search/blog/2019/03/help-google-search-know-best-date-for"
canonical: "https://developers.google.com/search/blog/2019/03/help-google-search-know-best-date-for"
author: "John Mueller"
published: "2019-03-11T00:00:00+00:00"
updated: "2019-03-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:33:47+00:00"
status_code: 200
html_hash: "f47eb8ddb83f613ad1048a44474c75733b2184c6076c7e74ad0b8d8ca9deed94"
clean_word_count: 850
clean_char_count: 5316
---
# Help Google Search know the best date for your web page

Sometimes, Google shows dates next to listings in its search results. In this post, we'll answer
some commonly-asked questions webmasters have about how these dates are determined and provide
some best practices to help improve their accuracy.

## How dates are determined

Google shows the date of a page when its automated systems determine that it would be relevant to
do so, such as for pages that can be time-sensitive, including news content:

![A byline date in a search result](/static/search/blog/images/import/bf90c8fe7728d85bc37c243ef7bd1511.png)

Google determines a date using a variety of factors, including but not limited to: any prominent
date listed on the page itself or dates provided by the publisher through structured markup.

Google doesn't depend on one single factor because all of them can be prone to issues. Publishers
may not always provide a clear visible date. Sometimes, structured data may be lacking or may not
be adjusted to the correct time zone. That's why our systems look at several factors to come up
with what we consider to be our best estimate of when a page was published or significantly
updated.

## How to specify a date on a page

To help Google to pick the right date, site owners and publishers should:

- **Show a clear date**: Show a visible date prominently on the page.
- **Use structured data**: Use the `datePublished` and
  `dateModified` schema with the correct time zone designator for
  [AMP](/search/docs/appearance/structured-data/article#amp) or
  [non-AMP pages](/search/docs/appearance/structured-data/article#non-amp). When using
  structured data, make sure to use the
  [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) for dates.

## Guidelines specific to Google News

Google News requires clearly showing both the date and the time that content was published or
updated. Structured data alone is not enough, though it is recommended to use in addition to a
visible date and time. Date and time should be positioned between the headline and the article
text. For more guidance, also see our
[help page about article dates](https://support.google.com/news/publisher-center/answer/9607104).

If an article has been substantially changed, it can make sense to give it a fresh date and
time. However, don't artificially freshen a story without adding significant information or
some other compelling reason for the freshening. Also, do not create a very slightly updated
story from one previously published, then delete the old story and redirect to the new one.
That's against our
[article URLs](https://support.google.com/news/publisher-center/answer/68323)
guidelines.

## More best practices for dates on web pages

In addition to the most important requirements listed above, here are additional best practices
to help Google determine the best page to consider showing for a web page:

- **Show when a page has been updated**: If you update a page significantly, also update the
  visible date (and time, if you display that). If desired, you can show two dates: when a page
  was originally published and when it was updated. Just do so in a way that's visually clear to
  your readers. If showing both dates, it's also highly recommended to use
  `datePublished` and `dateModified` for
  [AMP](/search/docs/appearance/structured-data/article#amp) or
  [non-AMP pages](/search/docs/appearance/structured-data/article#non-amp)
  to make it easier for algorithms to recognize.
- **Use the right time zone**: If specifying a time, make sure to provide the
  [correct timezone](https://en.wikipedia.org/wiki/ISO_8601#Time_zone_designators),
  taking into account
  [daylight saving time](https://en.wikipedia.org/wiki/Daylight_saving_time)
  as appropriate.
- **Be consistent in usage**. Within a page, make sure to use exactly the same date (and,
  potentially, time) in structured data as well as in the visible part of the page. Make sure to
  use the same timezone if you specify one on the page.
- **Don't use future dates or dates related to what a page is about**: Always use a date for
  when a page itself was published or updated, not a date linked to something like an event that
  the page is writing about, especially for events or other subjects that happen in the future
  (you may use [Event markup](/search/docs/appearance/structured-data/event) separately,
  if appropriate).
- **Follow Google's structured data guidelines**: While Google doesn't guarantee that a date
  (or structured data in general) specified on a page will be used, following our
  [structured data guidelines](/search/docs/appearance/structured-data/sd-policies)
  does help our algorithms to have it available in a machine-readable way.
- **Troubleshoot by minimizing other dates on the page**: If you've followed the best
  practices above and find incorrect dates are being selected, consider if you can remove or
  minimize other dates that may appear on the page, such as those that might be next to related
  stories.

We hope these guidelines help to make it easier to specify the right date on your website's
pages! For questions or comments on this, or other structured data topics, you can drop by our
[webmaster help forums](https://support.google.com/webmasters/go/community).
