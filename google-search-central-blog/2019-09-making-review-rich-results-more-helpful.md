---
title: "Making Review Rich Results more helpful"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2019-09-making-review-rich-results-more-helpful"
url: "https://developers.google.com/search/blog/2019/09/making-review-rich-results-more-helpful"
canonical: "https://developers.google.com/search/blog/2019/09/making-review-rich-results-more-helpful"
author: "Yuxin Cao, Software Engineer and Sven Naumann, Trust and Safety Search"
published: "2019-09-16T00:00:00+00:00"
updated: "2019-09-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2019_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:35:05+00:00"
status_code: 200
html_hash: "71f07a4c0ef3d760213a02993bacfb54ff78776fd699614a47693c5be2632a1a"
clean_word_count: 846
clean_char_count: 5715
---
# Making Review Rich Results more helpful

Search results that are enhanced by review rich results can be extremely helpful when searching
for products or services (the scores and/or "stars" you sometimes see alongside search results).

![Review stars example in search results](/static/search/blog/images/import/ff8bd436f52348ba1080ca1ddc7ace82.png)

To make them more helpful and meaningful, we are now introducing algorithmic updates to reviews in
rich results. This also addresses some of the invalid or misleading implementations site owners
have flagged to us.

## Focus on schema types that lend themselves to reviews

While, technically, you can attach review markup to any schema type, for many types displaying
star reviews does not add much value for the user. With this change, we're limiting the pool of
schema types that can potentially trigger review rich results in search. Specifically, we'll
only display reviews with those types (and their respective subtypes):

- [schema.org/Book](https://schema.org/Book)
- [schema.org/Course](https://schema.org/Course)
- [schema.org/CreativeWorkSeason](https://schema.org/CreativeWorkSeason)
- [schema.org/CreativeWorkSeries](https://schema.org/CreativeWorkSeries)
- [schema.org/Episode](https://schema.org/Episode)
- [schema.org/Event](https://schema.org/Event)
- [schema.org/Game](https://schema.org/Game)
- [schema.org/HowTo](https://schema.org/HowTo)
- [schema.org/LocalBusiness](https://schema.org/LocalBusiness)
- [schema.org/MediaObject](https://schema.org/MediaObject)
- [schema.org/Movie](https://schema.org/Movie)
- [schema.org/MusicPlaylist](https://schema.org/MusicPlaylist)
- [schema.org/MusicRecording](https://schema.org/MusicRecording)
- [schema.org/Organization](https://schema.org/Organization)
- [schema.org/Product](https://schema.org/Product)
- [schema.org/Recipe](https://schema.org/Recipe)
- [schema.org/SoftwareApplication](https://schema.org/SoftwareApplication)

## Self-serving reviews aren't allowed for `LocalBusiness` and `Organization`

Reviews that can be perceived as "self-serving" aren't in the best interest of users. We call
reviews "self-serving" when a review about entity A is placed on the website of entity A
- either directly in their markup or via an embedded third-party widget. That's why, with this
change, we're not going to display review rich results anymore for the schema types
[`LocalBusiness`](https://schema.org/LocalBusiness) and
[`Organization`](https://schema.org/Organization) (and
their subtypes) in cases when the
entity being reviewed controls the reviews themselves.

## Updated on September 18, 2019:

To explain more, in the past, an entity like a business or an organization could add review
markup about themselves to their home page or another page and often cause a review snippet to
show
for that page. That markup could have been added directly by the entity or embedded through the
use
of a third-party widget.

We consider this "self-serving" because the entity itself has chosen to add the markup to its own
pages, about its own business or organization.

Self-serving reviews are no longer displayed for businesses and organizations (the
`LocalBusiness` and `Organization` schema types). For example, we will no
longer display rich review snippets for how people have reviewed a business, if those reviews are
considered self-serving.

Reviews are allowed and displayed for other schema types listed in the
[documentation](/search/docs/appearance/structured-data/review-snippet). For example, a
cooking site might use markup for recipes to summarize its visitor reviews. In turn, we might
include this rich review markup for when those recipes appear in search.

## FAQ

### What if I'm using a third-party widget to display reviews about my business?

Google Search won't display review snippets for those pages. Embedding a third-party
widget is
seen as controlling the process of linking reviews.

### Do I need to remove self-serving reviews from `LocalBusiness` or `Organization`?

No, you don't need to remove them. Google Search just won't display review snippets for
those pages anymore.

### Will I get a manual action for having self-serving reviews on my site?

You won't get a manual action just for this. However, we recommend making sure that your
[structured data matches our
guidelines](/search/docs/appearance/structured-data/sd-policies).

### Does this update affect my Business Profile?

No, your Business Profile is not affected as this update only relates to organic Search.

### Will sites that gather reviews about other organizations be affected?

No, that's unchanged. Sites that gather reviews can show up with review snippets (for
their
reviews of other organizations) in search results.

### Does this update apply to `AggregateRating` too?

Yes. It applies to `Review` and `AggregateRating`.

### How do I report if a self-serving review is still appearing in search results?

We're considering creating a special form for this, if needed. We're slowly rolling out
this
change, so you may still see some cases of review stars where they shouldn't be.

## Add the `name` of the item that's being reviewed

With this update, the `name`  property is now required, so you'll want
to make sure that you specify the `name` of the item that's being
reviewed.

This update will help deliver a much more meaningful review experience for users, while requiring
little to no changes on the part of most site owners. You can find all those updates documented in
[our developer documentation](/search/docs/appearance/structured-data/review-snippet). If
you have any questions, you can come to our
[webmaster forums](https://support.google.com/webmasters/community)!
