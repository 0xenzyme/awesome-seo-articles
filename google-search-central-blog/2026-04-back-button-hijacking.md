---
title: "Introducing a new spam policy for \"back button hijacking\""
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "2026-04-back-button-hijacking"
url: "https://developers.google.com/search/blog/2026/04/back-button-hijacking"
canonical: "https://developers.google.com/search/blog/2026/04/back-button-hijacking"
author: "Chris Nelson"
published: "2026-04-13T00:00:00+00:00"
updated: "2026-04-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "news_or_research"
fetched_at: "2026-06-14T13:46:14+00:00"
status_code: 200
html_hash: "490dd31e59295e35e941061d0a56a38c188b9eb5ba07a81dcfa55eba20f35b70"
clean_word_count: 533
clean_char_count: 3578
---
# Introducing a new spam policy for "back button hijacking"

Today, we are expanding our [spam policies](/search/docs/essentials/spam-policies)
to address a deceptive practice known as "back button hijacking", which will become an explicit
violation of the "[malicious practices](/search/docs/essentials/spam-policies#malicious-practices)"
of spam policies, leading to potential spam actions.

## What is back button hijacking?

When a user clicks the "back" button in the browser, they have a clear expectation: they want to
return to the previous page. Back button hijacking breaks this fundamental expectation. It occurs
when a site interferes with a user's browser navigation and prevents them from using their back
button to immediately get back to the page they came from. Instead, users might be sent to pages
they never visited before, be presented with unsolicited recommendations or ads, or are otherwise
just prevented from normally browsing the web.

## Why are we taking action?

We believe that the user experience comes first. Back button hijacking interferes with the
browser's functionality, breaks the expected user journey, and results in user frustration. People
report feeling manipulated and eventually less willing to visit unfamiliar sites. As we've [stated before](/search/blog/2013/07/reminder-about-deceptive-behavior),
inserting deceptive or manipulative pages into a user's browser history has always been against our
[Google Search Essentials](/search/docs/essentials).

We've seen a rise of this type of behavior, which is why we're designating this an explicit violation
of our [malicious practices](/search/docs/essentials/spam-policies#malicious-practices)
policy, which says:

> Malicious practices create a mismatch between user expectations and the actual outcome,
> leading to a negative and deceptive user experience, or compromised user security or privacy.

Pages that are engaging in back button hijacking may be subject to
[manual spam actions](https://support.google.com/webmasters/answer/9044175#back-button-hijacking&zippy=%2Cback-button-hijacking)
or automated demotions, which can impact the site's performance in Google Search results. To give
site owners time to make any needed changes, we're publishing this policy two months in advance of
enforcement on June 15, 2026.

## What should site owners do?

Ensure you are not doing anything to interfere with a user's ability to navigate their browser history.

If you're currently using any script or technique that inserts or replaces deceptive or
manipulative pages into a user's browser history that prevents them from using their back button
to immediately get back to the page they came from, you are expected to remove or disable it.

Notably, some instances of back button hijacking may originate from the site's included libraries
or advertising platform. We encourage site owners to thoroughly review their technical
implementation and remove or disable any code, imports or any configurations that are responsible
for back button hijacking, to ensure a helpful and non-deceptive experience for users.

If your site has been impacted by a manual action and you have fixed the issue, you can always let
us know by submitting a [reconsideration request](https://support.google.com/webmasters/answer/35843)
in Search Console. For questions or feedback, feel free to reach out on
[social media](https://www.linkedin.com/showcase/googlesearchcentral/) or discuss in
our [help community](https://support.google.com/webmasters/threads?thread_filter=(category:search_console)).
