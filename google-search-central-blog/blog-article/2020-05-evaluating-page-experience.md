---
title: "Evaluating page experience for a better web"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2020-05-evaluating-page-experience"
url: "https://developers.google.com/search/blog/2020/05/evaluating-page-experience"
canonical: "https://developers.google.com/search/blog/2020/05/evaluating-page-experience"
author: "Sowmya Subramanian"
published: "2020-05-28T00:00:00+00:00"
updated: "2020-05-28T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:36:40+00:00"
status_code: 200
html_hash: "32eb4cfbbebc1f7584c1f75bbb479233c24ea5589acbba569e015d2fb310fb8c"
clean_word_count: 1237
clean_char_count: 7989
---
# Evaluating page experience for a better web

Through both [internal studies](https://ai.googleblog.com/2009/06/speed-matters.html) and
[industry research](https://blog.chromium.org/2020/05/introducing-web-vitals-essential-metrics.html),
users show they prefer sites with a great page experience. In recent years, Search has added a
variety of user experience criteria, such as
[how quickly pages load](/search/blog/2018/01/using-page-speed-in-mobile-search) and
[mobile-friendliness](/search/mobile-sites), as factors for ranking results. Earlier
this month, the Chrome team announced
[Core Web
Vitals](https://blog.chromium.org/2020/05/introducing-web-vitals-essential-metrics.html), a set of metrics related to speed, responsiveness and visual stability, to help
site owners measure user experience on the web.

Today, we're building on this work and providing an early look at an upcoming Search ranking
change that incorporates these page experience metrics. We will introduce a new signal that
combines Core Web Vitals with our existing signals for page experience to provide a holistic
picture of the quality of a user's experience on a web page.

As part of this update, we'll also incorporate the page experience metrics into our ranking
criteria for the Top Stories feature in Search on mobile, and remove the AMP requirement from
Top Stories eligibility. Google continues to support AMP, and will continue to link to AMP
pages when available. We've also updated our developer tools to help site owners optimize their
page experience.

**A note on timing**: We recognize many site owners are rightfully placing their focus on
responding to the effects of COVID-19. The ranking changes described in this post will not
happen before next year, and we will provide at least six months notice before they're rolled
out. We're providing the tools now to get you started (and because site owners have
consistently requested to know about ranking changes as early as possible), **but there is no
immediate need to take action**.

## About page experience

The [page experience](/search/docs/appearance/page-experience) signal measures aspects of
how users perceive the experience of interacting with a web page. Optimizing for these factors
makes the web more delightful for users across all web browsers and surfaces, and helps sites
evolve towards user expectations on mobile. We believe this will contribute to business success
on the web as users grow more engaged and can transact with less friction.

[Core Web Vitals](https://web.dev/articles/vitals#core-web-vitals) are a set of real-world,
user-centered metrics that quantify key aspects of the user experience. They measure dimensions
of web usability such as load time, interactivity, and the stability of content as it loads (so
you don't accidentally tap that button when it shifts under your finger - how annoying!).

[![

](/search/blog/images/Accidental_Submit_Still.webp)](/static/search/blog/images/AccidentalSubmit.webm)

We're combining the signals derived from Core Web Vitals with our existing Search signals for
page experience, including
[mobile-friendliness](/search/blog/2015/02/finding-more-mobile-friendly-search),
[HTTPS-security](/search/blog/2016/11/heres-to-more-https-on-web), and
[intrusive interstitial guidelines](/search/blog/2016/08/helping-users-easily-access-content-on),
to provide a holistic picture of page experience. Because we continue to work on identifying
and measuring aspects of page experience, we plan to incorporate more page experience signals
on a yearly basis to both further align with evolving user expectations and increase the
aspects of user experience that we can measure.

![A diagram illustrating the components of Search's signal for page experience.](/static/search/blog/images/page-experience-signal.png)

## Page experience ranking

Great page experiences enable people to get more done and engage more deeply; in contrast, a
bad page experience could stand in the way of a person being able to find the valuable
information on a page. By adding page experience to the hundreds of signals that Google
considers when ranking search results, we aim to help people more easily access the information
and web pages they're looking for, and support site owners in providing an experience users
enjoy.

For some developers, understanding how their sites measure on the Core Web Vitals—and addressing
noted issues—will require some work. To help out, we've [updated](https://web.dev/articles/vitals-tools)
popular developer tools such as Lighthouse and PageSpeed Insights to surface Core Web Vitals
information and recommendations, and Google Search Console provides a dedicated
[report](https://support.google.com/webmasters/answer/9205520) to help site owners
quickly identify opportunities for improvement. We're also working with external tool developers
to bring Core Web Vitals into their offerings.

While all of the components of page experience are important, we will prioritize pages with the
best information overall, even if some aspects of page experience are subpar. A good page
experience doesn't override having great, relevant content. However, in cases where there are
multiple pages that have similar content, page experience becomes much more important for
visibility in Search.

## Page experience and the mobile Top Stories feature

The mobile Top Stories feature is a premier fresh content experience in Search that currently
emphasizes AMP results, which have been optimized to exhibit a good page experience. Over the
past several years, Top Stories has
[inspired](https://blog.amp.dev/2018/03/08/standardizing-lessons-learned-from-amp/)
new thinking about the ways we could promote better page experiences across the web.

When we roll out the page experience ranking update, we will also update the eligibility
criteria for the Top Stories experience. AMP will no longer be necessary for stories to be
featured in Top Stories on mobile; it will be open to any page. Alongside this change, page
experience will become a ranking factor in Top Stories, in addition to the many factors
assessed. As before, pages must meet the
[Google News content
policies](https://support.google.com/news/publisher-center/answer/6204050) to be eligible. Site owners who currently publish pages as AMP, or with an AMP
version, will see no change in behavior – the AMP version will be what's linked from Top
Stories.

## Summary

We believe user engagement will improve as experiences on the web get better—and that by
incorporating these new signals into Search, we'll help make the web better for everyone. We
hope that sharing our roadmap for the page experience updates and launching supporting tools
ahead of time will help the diverse ecosystem of web creators, developers, and businesses to
improve and deliver more delightful user experiences.

Please stay tuned for our future updates that will communicate more specific guidance on the
timing for these changes to come into effect. As always, if you have any questions or feedback,
visit our [webmaster
forums](https://support.google.com/webmasters/community/).

---

## Updates

- **Update on June 15, 2021**: The page experience update is rolling out to all users globally.
  It will be complete by the end of August 2021.
- **Update on August 4, 2021**:
  [Clarified that Safe Browsing isn't used as a ranking signal](/search/blog/2021/08/simplifying-the-page-experience-report).
  Safe Browsing systems continue to play an important role to keep users of Google Search safe,
  and any flags will continue to be surfaced in Search Console outside of Page Experience
  report.
- **Update on January 31, 2024**:
  [Interaction to Next Paint (INP) will replace FID](https://web.dev/blog/inp-cwv-march-12)
  as a part of Core Web Vitals on March 12, 2024.
- **Update on March 12, 2024**:
  [Interaction to Next Paint (INP) has replaced FID](https://web.dev/blog/inp-cwv-launch) as a part of Core Web Vitals.
