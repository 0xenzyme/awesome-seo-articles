---
title: "Introducing the new Search Console"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2018-01-introducing-new-search-console"
url: "https://developers.google.com/search/blog/2018/01/introducing-new-search-console"
canonical: "https://developers.google.com/search/blog/2018/01/introducing-new-search-console"
author: "John Mueller, Ofir Roval, Hillel Maoz"
published: "2018-01-08T00:00:00+00:00"
updated: "2018-01-08T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2018_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:31:39+00:00"
status_code: 200
html_hash: "e24c5dc07aa7c8a1f486d3f87e54a5497cd1aceed0e05c1c76891c58bb8714bb"
clean_word_count: 1159
clean_char_count: 7198
---
# Introducing the new Search Console

A few months ago we
[released a beta version](/search/blog/2017/08/a-sneak-peek-at-two-experimental)
of a new Search Console experience to a limited number of users. We are now starting to release
this beta version to all users of Search Console, so that everyone can explore this simplified
process of optimizing a website's presence on Google Search. The functionality will include
[Search performance](https://support.google.com/webmasters/answer/7576553),
[Index Coverage](https://support.google.com/webmasters/answer/7440203),
[AMP status](https://support.google.com/webmasters/answer/7450883), and
[Job posting](https://support.google.com/webmasters/answer/7552505)
reports. We will send a message once your site is ready in the new Search Console.

We started by adding some of the most popular functionality in the new Search Console (which can
now be used in your day-to-day flow of addressing these topics). We are not done yet, so over the
course of the year the new Search Console (beta) will continue to add functionality from the
classic Search Console. Until the new Search Console is complete, **both versions will live
side-by-side** and will be easily interconnected via links in the navigation bar, so you can
use both.

The new Search Console was rebuilt from the ground up by surfacing the most actionable insights
and creating an interaction model which guides you through the process of fixing any pending
issues. We've also added ability to share reports within your own organization in order to
simplify internal collaboration.

## Search Performance: with 16 months of data!

![Search Performance view in Search Console](/static/search/blog/images/import/acc989ed580c0441bb5520641da3ebc4.png)

If you've been a fan of Search Analytics, you'll love the new
[Search Performance report](https://support.google.com/webmasters/answer/7576553).
Over the years, users have been consistent in asking us for more data in Search Analytics. With
the new report, you'll have 16 months of data, to make analyzing longer-term trends easier and
enable year-over-year comparisons. In the near future, this data will also be available via the
[Search Console API](/webmaster-tools/search-console-api-original).

## Index Coverage: a comprehensive view on Google's indexing

![Index Coverage view in Search Console](/static/search/blog/images/import/909357f886a7c02a1f98e84fbd9b632a.png)

The updated
[Index Coverage report](https://support.google.com/webmasters/answer/7440203)
gives you insight into the indexing of URLs from your website. It shows correctly indexed URLs,
warnings about potential issues, and reasons why Google isn't indexing some URLs. The report is
built on our new Issue tracking functionality that alerts you when new issues are detected and
helps you monitor their fix.

So how does that work?

1. When you drill down into a specific issue you will see a sample of URLs from your site. Clicking
   on error URLs brings up the **page details** with links to diagnostic-tools that
   help you understand what is the source of the problem.
2. Fixing Search issues often involves multiple teams within a company. Giving the right people
   access to information about the current status, or about issues that have come up there, is
   critical to improving an implementation quickly. Now, within most reports in the new Search
   Console, you can do that with the **share button** on top of the report which will
   create a shareable link to the report. Once things are resolved, you can disable sharing just as
   easily.
3. The new Search Console can also help you confirm that you've resolved an issue, and help us to
   update our index accordingly. To do this, select a flagged issue, and click **validate
   fix**. Google will then crawl and reprocess the affected URLs with a higher priority,
   helping your site to get back on track faster than ever.
4. The Index Coverage report works best for sites that submit
   [sitemap files](https://support.google.com/webmasters/answer/183668).
   Sitemap files are a great way to let search engines know about new and updated URLs. Once you've
   submitted a sitemap file, you can now use the **sitemap filter** over the Index
   Coverage data, so that you're able to focus on an exact list of URLs.

## Search Enhancements: improve your AMP and Job Postings pages

The new Search Console is also aimed at helping you implement Search Enhancements such as
[AMP](https://support.google.com/webmasters/answer/7450883) and
[Job Postings](https://support.google.com/webmasters/answer/7552505)
(more to come). These reports provide details into the specific errors and warnings that Google
identified for these topics. In addition to the functionally described in the index coverage
report, we augmented the reports with two extra features:

- The first feature is aimed at providing faster feedback in the process of fixing an issue. This
  is achieved by running several instantaneous tests once you click the **validate
  fix** button. If your pages don't pass this test we provide you with an immediate
  notification, otherwise we go ahead and reprocess the rest of the affected pages.
- The second new feature is aimed at providing positive feedback during the fix process by
  expanding the **validation log** with a list of URLs that were identified as fixed
  (in addition to URLs that failed the validation or might still be pending).

Similar to the AMP report, the new Search Console provides a
[Job postings report](https://support.google.com/webmasters/answer/7552505).
If you have jobs listings on your website, you may be eligible to have those shown directly
through [Google for Jobs](/search/blog/2017/06/connect-to-job-seekers-with-google)
(currently only available in certain locations).

## Feedback welcome

We couldn't have gotten so far without the ongoing feedback from our diligent trusted testers (we
plan to share more on how their feedback helped us dramatically improve Search Console). However,
**your continued feedback is critical for us**: if there's something you find
confusing or wrong, or if there's something you really like, **please let us know through
the feedback feature** in the sidebar. Also note that the mobile experience in the new
Search Console is still a work in progress.

We want to end this blog sharing an encouraging response we got from a user who has been testing
the new Search Console recently:

> "The UX of new Search Console is clean and well laid out, everything is where we expect it to be.
> I can even kick-off validation of my fixes and get email notifications with the result. It's been
> a massive help in fixing up some pesky AMP errors and warnings that were affecting pages on our
> site. On top of all this, the Search Analytics report now extends to 16 months of data which is a
> total game changer for us" - Noah Szubski, Chief Product Officer, DailyMail.com

Are there any other tools that would make your life as a webmaster easier? Let us know in the
comments here, and you can jump into our
[webmaster help forums](https://support.google.com/webmasters/go/community)
to discuss your ideas with others!
