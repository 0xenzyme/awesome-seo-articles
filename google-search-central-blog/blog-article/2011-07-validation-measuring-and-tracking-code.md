---
title: "Validation: measuring and tracking code quality"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-07-validation-measuring-and-tracking-code"
url: "https://developers.google.com/search/blog/2011/07/validation-measuring-and-tracking-code"
canonical: "https://developers.google.com/search/blog/2011/07/validation-measuring-and-tracking-code"
author: "Jens O. Meiert"
published: "2011-07-11T00:00:00+00:00"
updated: "2011-07-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:14:16+00:00"
status_code: 200
html_hash: "93da2d6bfbc3a67480bb32b7143b7ace46eb95df25776c998521fc3006fc4fcb"
clean_word_count: 545
clean_char_count: 3322
---
# Validation: measuring and tracking code quality

[Google's Webmaster Team](/search/blog/2011/05/introducing-google-webmaster-team)
is responsible for most of Google's informational websites like Google's
[Jobs site](https://www.google.com/jobs) or
[Privacy Centers](https://www.google.com/privacy).
Maintaining tens of thousands of pages and constantly releasing new Google sites requires more
than just passion for the job: it requires quality management.

In this post we won't talk about all the different tests that can be run to analyze a website;
instead we'll just talk about HTML and CSS validation, and tracking quality over time.

Why does validation matter? There are different perspectives on validation—at Google there are
different approaches and priorities too—but the Webmaster Team considers validation a baseline
quality attribute. It doesn't guarantee accessibility, performance, or maintainability, but it
reduces the number of possible issues that could arise and in many cases indicates appropriate
use of technology.

While paying a lot of attention to validation, we've developed a system to use it as a quality
metric to measure how we're doing on our own pages. Here's what we do: we give each of our pages
a score from 0-10 points, where 0 is worst (pages with 10 or more
[HTML](https://validator.w3.org/) and
[CSS validation](https://jigsaw.w3.org/css-validator/)
errors) and 10 is best (0 validation errors). We started doing this more than two years ago,
first by taking samples, now monitoring all our pages.

Since the beginning we've been documenting the validation scores we were calculating so that we
could actually see how we're doing on average and where we're headed: is our output improving, or
is it getting worse?

Here's what our data say:

![HTML and CSS Validation score development at google between 2009-2011.](/static/search/blog/images/archived_1_validation.png)

**On average** there are about three validation issues per page produced by the Webmaster Team
(as we combine HTML and CSS validation in the scoring process, information about the origin gets
lost), down from about four issues per page two years ago.

This information is valuable for us as it tells us how close we are to our goal of always shipping
perfectly valid code, and it also tells us whether we're on track or not. As you can see, with
the exception of the 2nd quarter of 2009 and the 1st quarter of 2010, we are generally observing
a positive trend.

What has to be kept in mind are issues with the integrity of the data, that is, the sample size
as well as "false positives" in the validators. We're working with the
[W3C](https://www.w3.org/) in several ways, including reporting
and helping to fix issues in the validators; however, as software can never be perfect, sometimes
pages get dinged for non-issues: see for example the
[`border-radius` issue](https://www.w3.org/Bugs/Public/show_bug.cgi?id=11975)
that has recently been fixed. We know that this is negatively affecting the validation scores
we're determining, but we have no data yet to indicate how much.

Although we track more than just validation for quality control purposes, validation plays an
important role in measuring the health of Google's informational websites.

How do you use validation in your development process?
