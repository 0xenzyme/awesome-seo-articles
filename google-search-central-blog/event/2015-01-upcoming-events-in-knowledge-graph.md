---
title: "Upcoming Events In The Knowledge Graph"
source: google-search-central-blog
content_type: "event"
freshness_risk: "historical"
slug: "2015-01-upcoming-events-in-knowledge-graph"
url: "https://developers.google.com/search/blog/2015/01/upcoming-events-in-knowledge-graph"
canonical: "https://developers.google.com/search/blog/2015/01/upcoming-events-in-knowledge-graph"
author: "Justin Boyan, Product Manager, Google Search"
published: "2015-01-15T00:00:00+00:00"
updated: "2015-01-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:26:00+00:00"
status_code: 200
html_hash: "6ed4b4aff06a95a0bd67f721484dd6df283b01b7d4395916a405ca2a0dd809fa"
clean_word_count: 587
clean_char_count: 3988
---
# Upcoming Events In The Knowledge Graph

Last year, we launched a
[new way for musical artists to list their upcoming events on Google](/search/blog/2014/03/musical-artists-your-official-tour):
schema.org markup on their official websites. Now we're expanding this program in four ways:

## Official Ticket Links

For artists: if you
[mark up ticketing links](/search/docs/appearance/structured-data/event) along with the
events on your official website, we'll show an *expanded answer card for your events* in
Google Search, including the on-sale date, availability, and a direct link to your preferred
ticketing site.

![](/static/search/blog/images/import/78acea892d3c3ef416adfb23103cedfa.png)

As before, you may write the event markup directly into your site's HTML, or simply install an
event widget that builds in the markup for you automatically—like
[Bandsintown](https://www.bandsintown.com/artist_platform/tour_dates_widget),
[BandPage](https://www.bandpage.com/support/how-widgets),
[GigPress](https://gigpress.com/),
[ReverbNation](https://www.reverbnation.com/band-promotion/widgets) or
[Songkick](https://tourbox.songkick.com/).

## Delegated Event Listings

What if you can't add markup or an event widget to your official website—for example, if your
website doesn't list your events at all? Now you can use
[delegation markup](/search/docs/appearance/structured-data/event)
to tell us to source your events from a page of your choice on another website. Just add the
following markup to your home page, making sure to customize the three red values:

```
<script type="application/ld+json">
{"@context" : "https://schema.org",
"@type" : "MusicGroup",
"name" : "<span>Your Band or Performer Name</span>",
"url" : "<span>https://your-official-website.com</span>",
"event" : "https://other-event-site.com/your-event-listing-page/"
}
</script>
```

The marked-up events found on the other event site's page will then be eligible for Google events
features. Examples of sites you can point to in the "event" field include bandpage.com,
bandsintown.com, songkick.com, and ticketmaster.com.

## Comedian Events

Hey funny people! We want your performances to show up on Google, too. Just
[add `ComedyEvent` markup](/search/docs/appearance/structured-data/event)
to your official website. Or, if another site like laughstub.com has your complete event listings,
use delegation markup on your home page to point us their way.

## Venue Events

Last but definitely not least: we're starting to show venue event listings in Google Search.
Concert venues, theaters, libraries, fairgrounds, and so on: make your upcoming events eligible
for display across Google by
[adding Event markup to your official website](/search/docs/appearance/structured-data/event).

![](/static/search/blog/images/import/1b16c02e872aad26bac34ac88db168e7.png)

As with artist events, you have a choice of writing the event markup directly into your site's
HTML, or using a widget or plugin that builds in the markup for you. Also, if all your events are
ticketed by a primary ticketer whose website provides markup, you don't have to do anything!
Google will read the ticketer's markup and apply it toward your venue's event listings.

For example, venues ticketed by Ticketmaster, including its international sites and TicketWeb,
will automatically be covered. The same goes for venues that list events with Ticketfly, AXS,
LaughStub, Wantickets, Holdmyticket, ShowClix, Stranger Tickets, Ticket Alternative, Digitick, See
Tickets, Tix, Fnac Spectacles, Ticketland.ru, iTickets, MIDWESTIX, Ticketleap, or Instantseats.
All of these have already implemented
[ticketer events markup](/search/docs/appearance/structured-data/event).

Please see our [Developer Site](/search/docs/appearance/structured-data/event) for full
documentation of these features, including a video tutorial on how to write and test event markup.
Then add the markup, help new fans discover your events, and play to a packed house!
