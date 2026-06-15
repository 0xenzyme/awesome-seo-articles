---
title: "A reminder about \"event\" markup"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2017-11-a-reminder-about-event-markup"
url: "https://developers.google.com/search/blog/2017/11/a-reminder-about-event-markup"
canonical: "https://developers.google.com/search/blog/2017/11/a-reminder-about-event-markup"
author: "Sven Naumann, Trust and Safety Search Team"
published: "2017-11-27T00:00:00+00:00"
updated: "2017-11-27T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:30:54+00:00"
status_code: 200
html_hash: "2b33bc953d1ade7017f42cc5c478e00f31e5bfa7bce4d10a1960f3300fa29bfb"
clean_word_count: 287
clean_char_count: 1851
---
# A reminder about "event" markup

Lately we've been receiving feedback from users seeing non-events like coupons or vouchers showing
up in search results where "events" snippets appear. This is really confusing for users and also
against our guidelines, where we have added
[additional clarification](/search/docs/appearance/structured-data/event).

So, what's the problem?

We've seen a number of publishers in the coupons/vouchers space use the "event" markup to
describe their offers. And as much as using a discount voucher can be a very special thing, that
doesn't make coupons or vouchers events or "saleEvents". Using
[Event markup](/search/docs/appearance/structured-data/event) to describe something that
is not an event creates a bad user experience, by triggering a rich result for something that will
happen at a particular time, despite no actual event being present.

Here are some examples to illustrate the issue:

![](/static/search/blog/images/import/491a1c6f407fcd89ae8eb66589aa6959.png)

Since this creates a misleading user experience, we may take manual action on such cases. In case
your website is affected by such a manual action, you will find a notification in your Search
Console account. If a manual action is taken, it can result in structured data markup for the
whole site not being used for search results.

While we're specifically highlighting coupons and vouchers in this blogpost, this applies to all
other non-event items being annotated with "event" markup as well—or, really, for applying
a type of markup to something other than the type of thing it is meant to describe.

For more information, please visit our
[developer documentation](/search/docs/appearance/structured-data/event) or stop by our
[Webmaster Forum](https://support.google.com/webmasters/go/community)
in case you have additional questions!
