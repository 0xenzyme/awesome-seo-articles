---
title: "Helping users easily access content on mobile"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2016-08-helping-users-easily-access-content-on"
url: "https://developers.google.com/search/blog/2016/08/helping-users-easily-access-content-on"
canonical: "https://developers.google.com/search/blog/2016/08/helping-users-easily-access-content-on"
author: "Doantam Phan, Product Manager"
published: "2016-08-23T00:00:00+00:00"
updated: "2016-08-23T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2016_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:29:02+00:00"
status_code: 200
html_hash: "1cb5e611268defad5b86c39dd1c233d393704dae1b87eb56ea071a6664854ad5"
clean_word_count: 805
clean_char_count: 5207
---
# Helping users easily access content on mobile

In Google Search, our goal is to help users quickly find the best answers to their questions,
regardless of the device they're using. Today, we're announcing two upcoming changes to mobile
search results that make finding content easier for users.

## Simplifying mobile search results

Two years ago, we added a
[mobile-friendly label](/search/blog/2014/11/helping-users-find-mobile-friendly-pages)
to help users find pages where the text and content was readable without zooming and the tap
targets were appropriately spaced. Since then, we've seen the ecosystem evolve and we recently
found that 85% of all pages in the mobile search results now meet this criteria and show the
mobile-friendly label. To keep search results uncluttered, we'll be removing the label, although
the mobile-friendly criteria will continue to be a ranking signal. We'll continue providing the
[Mobile Usability report](https://search.google.com/search-console/mobile-usability)
in Search Console and the
[Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) to help
webmasters evaluate the effect of the mobile-friendly signal on their pages.

## Helping users find the content they're looking for

Although the majority of pages now have text and content on the page that is readable without
zooming, we've recently seen many examples where these pages show intrusive interstitials to users.
While the underlying content is present on the page and available to be indexed by Google, content
may be visually obscured by an interstitial. This can frustrate users because they are unable to
easily access the content that they were expecting when they tapped on the search result.

Pages that show intrusive interstitials provide a poorer experience to users than other pages where
content is immediately accessible. This can be problematic on mobile devices where screens are
often smaller. To improve the mobile search experience, after January 10, 2017, pages where content
is not easily accessible to a user on the transition from the mobile search results may not rank as highly.

Here are some examples of techniques that make content less accessible to a user:

- Showing a popup that covers the main content, either immediately after the user navigates to a
  page from the search results, or while they are looking through the page.
- Displaying a standalone interstitial that the user has to dismiss before accessing the main content.
- Using a layout where the above-the-fold portion of the page appears similar to a standalone
  interstitial, but the original content has been inlined underneath the fold.

## Examples of interstitials that make content less accessible

Here's an example of an intrusive popup:

![An example of an intrusive popup](/static/search/blog/images/interstitials-1.png)

Here's an example of an intrusive standalone interstitial:

![An example of an intrusive standalone interstitial](/static/search/blog/images/interstitials-2.png)

Here's another example of an intrusive standalone interstitial:

![Another example of an intrusive standalone interstitial](/static/search/blog/images/interstitials-3.png)

By contrast, here are some examples of techniques that, used responsibly, would not be affected by
the new signal:

- Interstitials that appear to be in response to a legal obligation, such as for cookie usage or
  for age verification.
- Login dialogs on sites where content is not publicly indexable. For example, this would include
  private content such as email or unindexable content that is behind a paywall.
- Banners that use a reasonable amount of screen space and are easily dismissible. For example,
  the app install banners provided by Safari and Chrome are examples of banners that use a
  reasonable amount of screen space.

## Examples of interstitials that would not be affected by the new signal, if used responsibly

Here's an example of an interstitial for cookie usage:

![An example of an interstitial for cookie usage](/static/search/blog/images/interstitials-4.png)

Here's an example of an interstitial for age verification:

![An example of an interstitial for age verification](/static/search/blog/images/interstitials-5.png)

Here's an example of a banner that uses a reasonable amount of screen space:

![An example of a banner that uses a reasonable amount of screen space](/static/search/blog/images/interstitials-6.png)

We previously explored a signal that checked for interstitials that ask a user to install a mobile
app. As we continued our development efforts, we saw the need to broaden our focus to interstitials
more generally. Accordingly, to avoid duplication in our signals, we've removed the check for
app-install interstitials from the mobile-friendly test and have incorporated it into this new
signal in Search.

Remember, this new signal is just one of hundreds of signals that are used in ranking. The intent
of the search query is still a very strong signal, so a page may still rank highly if it has great,
relevant content. As always, if you have any questions or feedback, please visit our
[webmaster forums](https://support.google.com/webmasters/go/community).
