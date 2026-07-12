---
title: "The role of page experience in creating helpful content"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2023-04-page-experience-in-search"
url: "https://developers.google.com/search/blog/2023/04/page-experience-in-search"
canonical: "https://developers.google.com/search/blog/2023/04/page-experience-in-search"
author: "Danny Sullivan"
published: "2023-04-19T00:00:00+00:00"
updated: "2023-04-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
fetched_at: "2026-06-14T13:41:50+00:00"
status_code: 200
html_hash: "aba869c14b0b795692eb072fe3e6d0b50a68f3ef91c158fa19928b43ed5ce565"
clean_word_count: 1176
clean_char_count: 7747
---
# The role of page experience in creating helpful content

Helpful content generally offers a good page experience. That's why today, we've added a section on page experience
to our [guidance on
creating helpful content](/search/docs/fundamentals/creating-helpful-content) and revised our [help page about page
experience](/search/docs/appearance/page-experience). We think this all will help site owners consider page experience more holistically as part of
the content creation process.

We haven't introduced any major new aspects of page experience to consider versus our previous
guidance. If you've been paying attention to things we've talked about in the past, such as Core Web Vitals, all
that remains as before.

## Streamlining our page experience guidance

For years, our core ranking systems have sought to reward content providing a good page experience, as covered in
guidance we gave in [2011](/search/blog/2011/05/more-guidance-on-building-high-quality),
updated in [2019](/search/blog/2019/08/core-updates) and made part of our [Creating helpful,
reliable, people-first content](/search/docs/fundamentals/creating-helpful-content) help page last year.

That help page is a key resource for our [Search
Essentials](/search/docs/essentials). We regularly refer anyone seeking to be successful with Google Search to read through the
self-assessment questions and other guidance on it. But while some aspects of page experience were covered in the
page's "Presentation and production questions" section, others were not. We've now improved this by adding a [section on
providing a great page experience](/search/docs/fundamentals/creating-helpful-content#page-experience), to explain how those hoping to be successful in Search should be
considering this.

In turn, that section links over to our revised [Understanding page
experience in Google Search results](/search/docs/appearance/page-experience) help page, which explains the role of page experience in more detail,
along with self-assessment questions and resources. That page brings together in one place some key aspects of page
experience to consider, aspects that are unchanged from what we've talked about in recent years.

## Search Console reports

In the coming months, the Page Experience report within
[Search Console](https://search.google.com/search-console/about)
will transform into a new page that links to our general guidance about page experience,
along with a dashboard-view of the individual Core Web Vitals and HTTPS reports that will
remain in Search Console.

Also starting December 1, 2023, we'll be retiring Search Console's "Mobile Usability" report, the [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) tool and [Mobile-Friendly
Test API](/webmaster-tools/search-console-api/reference/rest). This doesn't mean that mobile usability isn't important for success with Google Search. It remains
critical for users, who are using mobile devices more than ever, and as such, it remains a part of our page
experience guidance. But in the nearly ten years since we [initially
launched](/search/blog/2014/10/tracking-mobile-usability-in-webmaster) this report, many other robust resources for evaluating mobile usability have emerged, including [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) from Chrome.

Overall, we hope this work will help creators and site owners continue to succeed with their visitors by providing a
great page experience and by doing so, also succeed in Google Search.

## FAQ

### Without the Page Experience report, how do I know if my site provides a great page experience?

The page experience report was intended as a general guidepost of some metrics that aligned with good page
experience, not as a comprehensive assessment of all the different aspects. Those seeking to provide a good page
experience should take an holistic approach, including following some of our self-assessment questions covered on
our [Understanding page experience in Google Search results](/search/docs/appearance/page-experience#assess) page.

### Is there a single "page experience signal" that Google Search uses for ranking?

There is no single signal. Our core ranking systems look at a variety of signals that align with overall page
experience.

### Page experience signals had been listed as Core Web Vitals, mobile-friendly, HTTPS and no intrusive interstitials. Are these signals still used in search rankings?

While not all of these may be directly
used to inform ranking, we do find that all of these aspects of page experience align with success in search
ranking, and are worth attention.

### Are Core Web Vitals still important?

We highly recommend site owners achieve good Core Web Vitals for success with Search and to ensure a great user
experience generally. However, great page experience involves more than Core Web Vitals. Good stats within the
[Core Web Vitals report](https://support.google.com/webmasters/answer/9205520)
in Search Console or third-party Core Web Vitals reports don't guarantee good rankings.

### What does this mean for the "page experience update"?

The page experience update was a concept to describe a set of key page experience aspects for site owners to focus
on. In particular, it [introduced](/search/blog/2021/04/more-details-page-experience#details)
Core Web Vitals as a new signal that our core ranking systems considered, along with other page experience signals
such as HTTPS that they'd already been considering. It was not a separate ranking system, and it did not combine all
these signals into one single "page experience" signal.

### Is good page experience required to appear in the "Top stories" carousel on mobile?

Page experience is not an eligibility requirement to appear anywhere in the "Top stories" section. As long as
content meets [Google News best
practices](https://support.google.com/news/publisher-center/answer/9607104) and [Google News
policies](https://support.google.com/news/publisher-center/answer/6204050), our automated systems may consider it.

### Is page experience evaluated on a site-wide or page-specific basis?

Our core ranking systems generally evaluate content on a page-specific basis, including when
understanding aspects related to page experience. However, we do have some site-wide assessments.

### Does page experience factor into the helpful content system?

The helpful content system is primarily focused on signals related to content, rather than presentation and page
experience. However, just as our core ranking systems consider signals that align with good page experience, so does
the [helpful content system](/search/updates/helpful-content-update), to a
degree.

### How important is page experience to ranking success?

Google Search always seeks to show the most relevant content, even if the page experience is sub-par. But for many
queries, there is lots of helpful content available. Having a great page experience can contribute to success in
Search, in such cases.

---

## Updates

- **Update on January 31, 2024**:
  [Interaction to Next Paint (INP) will replace FID](https://web.dev/blog/inp-cwv-march-12)
  as a part of Core Web Vitals on March 12, 2024.
- **Update on November 8, 2023**: We're also retiring the Good page experience search
  appearance filter from the Performance report, as page experience has evolved to include more
  aspects than just Core Web Vitals and HTTPS. To allow time for adjusting your API calls, support
  for this search appearance filter in the Search Console API will be removed in 180 days.
- **Update on March 12, 2024**:
  [Interaction to Next Paint (INP) has replaced FID](https://web.dev/blog/inp-cwv-launch) as a part of Core Web Vitals.
