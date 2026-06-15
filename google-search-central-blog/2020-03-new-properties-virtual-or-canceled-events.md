---
title: "New properties for virtual, postponed, and canceled events"
source: google-search-central-blog
content_type: "event"
freshness_risk: "historical"
slug: "2020-03-new-properties-virtual-or-canceled-events"
url: "https://developers.google.com/search/blog/2020/03/new-properties-virtual-or-canceled-events"
canonical: "https://developers.google.com/search/blog/2020/03/new-properties-virtual-or-canceled-events"
author: "Emily Fifer, Event Search Product Manager"
published: "2020-03-17T00:00:00+00:00"
updated: "2020-03-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:36:31+00:00"
status_code: 200
html_hash: "257c5fc4ada6bb88042894afdac4f8ce1ddcaee64d5f44b05fdb11e313af12e0"
clean_word_count: 627
clean_char_count: 4622
---
# New properties for virtual, postponed, and canceled events

In the current environment and status of COVID-19 around the world, many events are being
canceled, postponed, or moved to an online-only format. Google wants to show users the latest,
most accurate information about your events in this fast-changing environment, and so we've
added some new, optional properties to our
[developer documentation](/search/docs/appearance/structured-data/event)
to help. These properties apply to all regions and languages. This is one part of our overall efforts in
[schema updates](https://blog.schema.org/2020/03/schema-for-coronavirus-special) to
support publishers and users. Here are some important tips on keeping Google up to date on your events.

## Update the status of the event

The schema.org `eventStatus` property sets the status of the event, particularly when the event has been canceled, postponed,
or rescheduled. This information is helpful because it allows Google to show users the current
status of an event, instead of dropping the event from the event search experience altogether.

- **If the event has been canceled**: Set the
  [`eventStatus`](/search/docs/appearance/structured-data/event#eventstatus)
  property to [`EventCancelled`](https://schema.org/EventCancelled)
  and keep the original date in the
  [`startDate`](/search/docs/appearance/structured-data/event#startdate) of
  the event.
- **If the event has been postponed (but the date isn't known yet)**: Keep the original date in the
  [`startDate`](/search/docs/appearance/structured-data/event#startdate) of
  the event until you know when the event will take place and update the
  [`eventStatus`](/search/docs/appearance/structured-data/event#eventstatus)
  to [`EventPostponed`](https://schema.org/EventPostponed).
  The [`startDate`](/search/docs/appearance/structured-data/event#startdate)
  property is required to help identify the unique event, and we need the date original
  [`startDate`](/search/docs/appearance/structured-data/event#startdate)
  until you know the new date. Once you know the new date information, change the
  `eventStatus` to
  [`EventRescheduled`](https://schema.org/EventRescheduled)
  and update the
  [`startDate`](/search/docs/appearance/structured-data/event#startdate) and
  [`endDate`](/search/docs/appearance/structured-data/event#enddate) with the
  new date information.
- **If the event has been rescheduled to a later date**: Update the
  [`startDate`](/search/docs/appearance/structured-data/event#startdate) and [`endDate`](/search/docs/appearance/structured-data/event#enddate)
  with the relevant new dates. Optionally, you can also mark the
  [`eventStatus`](/search/docs/appearance/structured-data/event#eventstatus)
  field as [`EventRescheduled`](https://schema.org/EventRescheduled)
  and add the [`previousStartDate`](/search/docs/appearance/structured-data/event#previous-start-date).
- **If the event has moved from in-person to online-only**: Optionally update the
  [`eventStatus`](/search/docs/appearance/structured-data/event#eventstatus)
  field to indicate the change with `EventMovedOnline`.

For more information on how to implement the `eventStatus` property, refer to the
[developer documentation](/search/docs/appearance/structured-data/event#eventstatus).

## Mark events as online only

More events are shifting to online only, and we're actively working on a way to show this
information to people on Google Search. If your event is happening only online, make sure to
use the following properties:

- Set the location to the
  [`VirtualLocation`](/search/docs/appearance/structured-data/event#virtual-location)
  type.
- Set the
  [`eventAttendanceMode`](/search/docs/appearance/structured-data/event#event-attendance-mode)
  property to
  [`OnlineEventAttendanceMode`](https://schema.org/OnlineEventAttendanceMode).

For more information on how to implement the `VirtualLocation` type,
refer to the [developer documentation](/search/docs/appearance/structured-data/event#virtual-location).

## Update Google when your event changes

After you make changes to your markup, make sure you
[update Google](/search/docs/guides/submit-URLs). We recommend that you
[make your sitemap available automatically
through your server](https://www.youtube.com/watch?v=y0TPINzAVf0). This is the best way to make sure that your new and updated content is
highlighted to search engines as quickly as possible.

If you have any questions, let us know through the
[Webmasters forum](https://support.google.com/webmasters/community) or on
[Twitter](https://twitter.com/googlesearchc).
