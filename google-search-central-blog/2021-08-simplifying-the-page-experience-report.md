---
title: "Simplifying the Page Experience report"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2021-08-simplifying-the-page-experience-report"
url: "https://developers.google.com/search/blog/2021/08/simplifying-the-page-experience-report"
canonical: "https://developers.google.com/search/blog/2021/08/simplifying-the-page-experience-report"
author: "Jeffrey Jose, Product Manager on Search"
published: "2021-08-04T00:00:00+00:00"
updated: "2021-08-04T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:39:40+00:00"
status_code: 200
html_hash: "1e8f8aeed35291508ff7b1e112e603d1f568545b74ddfbc803842195c7460284"
clean_word_count: 552
clean_char_count: 3565
---
# Simplifying the Page Experience report

The
[Page Experience report](https://support.google.com/webmasters/answer/10218333)
in Search Console
[launched](/search/blog/2021/04/more-details-page-experience) earlier this year to
offer publishers and site owners a way to quickly understand how their sites fare against the page
experience signals. Today, we’re launching a new version that simplifies the report by removing
the Safe Browsing and Ad Experience widgets from the Page Experience report, and fixes on how
missing data is handled.

As a reminder, the page experience ranking update started
[slowly rolling out](https://twitter.com/googlesearchc/status/1404886100087246848)
on June 15, 2021 and the rollout will be completed by August 31, 2021.

## Removal of the Safe Browsing and Ad Experience widgets

[Safe Browsing](https://safebrowsing.google.com/) systems at Google
are designed to keep users safe on the internet. Sometimes sites fall victim to third-party
hijacking, which can cause Safe Browsing warnings to be surfaced. We recognize that these issues
aren't always within the control of site owners, which is why we're clarifying that Safe Browsing
isn't used as a ranking signal and won’t feature in the Page Experience report. Any Safe Browsing
flags will continue to be surfaced in the Search Console outside of the Page Experience report.

Similarly, we're removing the
[Ad Experience](https://www.google.com/webmasters/tools/ad-experience-unverified)
widget to avoid surfacing the same information on two parts of Search Console. The Ad Experience
report will continue to be available as a standalone tool that you can use to review the status of
your site and identify ad experiences that violate the Better Ads Standards. To be clear, the Ad
Experience report was never used as a factor for page experience, so this change won't affect your
site’s page experience status.

![Updated graphic of the factors that make up page experience signal, namely Loading (LCP), Interactivity (FID), Visual Stability (CLS), Mobile Friendliness, HTTPS and No Intrusive Interstitials](/static/search/blog/images/volt-post-graphic-designed.png)

*Updated graphic of the factors that make up page experience signal, namely Loading (LCP),
Interactivity (FID), Visual Stability (CLS), Mobile Friendliness, HTTPS and No Intrusive
Interstitials.*

## Other improvements to the report

Along with the two updates mentioned above, we're rolling out more improvements to how the report
handles missing data:

- Added a "No recent data" banner to the
  [Core Web Vitals report](/static/search/blog/images/cwv-past-data.png)
  and
  [Page Experience report](/static/search/blog/images/volt-past-data.png).
- Fixed a bug that caused the report to show "Failing HTTPS" when Core Web Vitals data was
  missing.
- Rephrased the empty state text in the Page Experience report and Core Web Vitals report.

We hope the improvements make it easier to use the Page Experience report, and help you build
websites with great page experience.

If you have questions or feedback, please visit our
[help forums](https://support.google.com/webmasters/community/) or let
us know through [Twitter](https://twitter.com/googlesearchc).

---

## Updates

- **Update on January 31, 2024**:
  [Interaction to Next Paint (INP) will replace FID](https://web.dev/blog/inp-cwv-march-12)
  as a part of Core Web Vitals on March 12, 2024.
- **Update on March 12, 2024**:
  [Interaction to Next Paint (INP) has replaced FID](https://web.dev/blog/inp-cwv-launch)
  as a part of Core Web Vitals.
