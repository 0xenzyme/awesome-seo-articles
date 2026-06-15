---
title: "Enabling more high quality content for users"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2017-10-enabling-more-high-quality-content"
url: "https://developers.google.com/search/blog/2017/10/enabling-more-high-quality-content"
canonical: "https://developers.google.com/search/blog/2017/10/enabling-more-high-quality-content"
author: "Cody Kwok, Principal Engineer"
published: "2017-10-02T00:00:00+00:00"
updated: "2017-10-02T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:30:52+00:00"
status_code: 200
html_hash: "e433cd3daf9536fb52db38bd38b199899aaf2a19af026aac1f3be3b76f3db5e6"
clean_word_count: 725
clean_char_count: 4695
---
# Enabling more high quality content for users

In Google's
[mission](https://www.google.com/search/howsearchworks/mission/)
to organize the world's information, we want to guide Google users to the highest quality content,
the principle exemplified in our
[quality rater guidelines](https://static.googleusercontent.com/media/www.google.com/en//insidesearch/howsearchworks/assets/searchqualityevaluatorguidelines.pdf).
Professional publishers provide the lion's share of quality content that benefits users and we
want to encourage their success.

The ecosystem is sustained via two main sources of revenue: ads and subscriptions, with the latter
requiring a delicate balance to be effective in Search. Typically subscription content is hidden
behind paywalls, so that users who don't have a subscription don't have access. Our evaluations
have shown that users who are not familiar with the high quality content behind a paywall often
turn to other sites that are offering content without a subscription or login. It is difficult to
justify a subscription if one doesn't already know how valuable the content is, and in fact, our
experiments have shown that a portion of users shy away from subscription sites. Therefore, it is
essential that sites provide some amount of sampling of their content so that users can learn how
valuable their content is.

The First Click Free (FCF) policy for both Google
[web search](/search/blog/2008/10/first-click-free-for-web-search) and
[News](https://news.googleblog.com/2007/09/first-click-free.html)
was designed to address this issue. It offers promotion and discovery opportunities for publishers
with subscription content, while giving Google users an opportunity to discover that content. Over
the past year, we have worked with publishers to investigate the effects of FCF on user
satisfaction and on the sustainability of the publishing ecosystem. We found that while FCF is a
reasonable sampling model, publishers are in a better position to determine what specific sampling
strategy works best for them. Therefore, we are removing FCF as a requirement for Search, and we
encourage publishers to experiment with different sampling schemes, as long as they stay within
the updated
[webmaster guidelines](/search/docs/essentials). We call
this **Flexible Sampling**.

One of the original motivations for FCF is to address the issues surrounding
[cloaking](/search/docs/essentials/spam-policies#cloaking), where the content served to
Googlebot is different from the content served to users. Spammers often seek to game search
engines by showing interesting content to the search engine, say healthy food recipes, but then
showing users an offer for diet pills. This "bait and switch" scheme creates a bad user experience
since users do not get the content they expected. Sites with paywalls are strongly encouraged to
apply the new
[structured data](/search/docs/appearance/structured-data/paywalled-content)
to their pages, because without it, the paywall may be interpreted as a form of cloaking, and the
pages would then be removed from search results.

Based on our investigations, we have created detailed
[best practices](/search/docs/appearance/flexible-sampling) for implementing
flexible sampling. There are two types of sampling we advise: **metering**, which provides
users with a quota of articles to consume, after which paywalls will start appearing; and
**lead-in**, which offers a portion of an article's content without it being shown in full.

For metering, we think that monthly (rather than daily) metering provides more flexibility and a
safer environment for testing. The user impact of changing from one integer value to the next is
less significant at, say, 10 monthly samples than at 3 daily samples. All publishers and their
audiences are different, so there is no single value for optimal sampling across publishers.
However, we recommend that publishers start by providing 10 clicks per month to Google search
users in order to preserve a good user experience for new potential subscribers. Publishers should
then experiment to optimize the tradeoff between discovery and conversion that works best for
their businesses.

Lead-in is generally implemented as truncated content, such as the first few sentences or 50-100
words of the article. Lead-in allows users a taste of how valuable the content may be. Compared to
a page with completely blocked content, lead-in clearly provides more utility and added value to
users.

We are excited by this change as it allows the growth of the premium content ecosystem, which
ultimately benefits users. We look forward to the prospect of serving users more high quality
content!
