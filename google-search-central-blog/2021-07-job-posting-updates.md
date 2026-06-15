---
title: "Updating our job posting guidelines to improve quality of results for job seekers"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2021-07-job-posting-updates"
url: "https://developers.google.com/search/blog/2021/07/job-posting-updates"
canonical: "https://developers.google.com/search/blog/2021/07/job-posting-updates"
author: "Gilad Orly, Product Manager, Google Search"
published: "2021-07-13T00:00:00+00:00"
updated: "2021-07-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:39:30+00:00"
status_code: 200
html_hash: "46e57bceaa83819e5fc90ec360e7ad2250fe7b30af8c72c380716db13c0b82ed"
clean_word_count: 799
clean_char_count: 5167
---
# Updating our job posting guidelines to improve quality of results for job seekers

Searching for a job can be a time-consuming process and the outcome of the application may be life
changing. That's why providing job seekers with authentic, fresh, and trustworthy content when
they come to Google Search is our top priority.

To better understand our user's perspective, we asked tens of thousands of job seekers around the
world to tell us more about their experience when applying to jobs online. Based on this feedback,
we were able to identify common themes to help improve the quality of our results. Today we are
announcing a [new structured data
property](/search/docs/appearance/structured-data/job-posting#direct-apply) and [new editorial content policy](/search/docs/appearance/structured-data/job-posting#editorial).

## New `directApply` property

The [`directApply` property](/search/docs/appearance/structured-data/job-posting#direct-apply)
is an optional way that enables you to share if your job listing offers a *direct apply*
experience. We define a *direct apply* experience in terms of the user actions required to
apply for the job, which means that the user is offered a short and straightforward application
process on your page.

You likely offer a direct apply experience if your site provides one of the following experiences:

- The user completes the application process on your site.
- Once arriving at your page from Google, the user doesn't have to click on apply and provide
  user information more than once to complete the application process.

![Illustrations of acceptable direct apply processes](/static/search/blog/images/direct-apply-illustrations.png)

As we work to integrate this information to Google, you may not see any effect in Google Search right away.

## New editorial content policy

To ensure users can understand your content and can easily apply for the job, we're adding a
[new editorial content policy](/search/docs/appearance/structured-data/job-posting#editorial) for job postings
on Google Search. The new editorial content policy include guidance around obstructive text and images,
excessive and distractive ads, or content that doesn't add any value to the job posting. Job
listings should also follow basic grammar rules, such as proper capitalization.

This will help us improve the quality of our results and develop new functionality within the product.

To provide sufficient time for implementation, the new editorial content policy will go into effect on
October 1, 2021. For additional details, visit our [developer
documentation](/search/docs/appearance/structured-data/job-posting#editorial).

## Top issues site owners can address to improve job seeker trust

Based on our research findings, you can improve job seeker trust by addressing the following
aspects on your site:

- **Verify that there are no scammy or spammy job posts on your site**. These are job posts
  that don't represent a real job opportunity. Make sure that you only markup pages with a single
  and actionable job opportunity.
- **Ensure a good user experience.** According to our users, sites with poor user experience
  are those that ask for user information when it is not necessary, have poor quality pages (for
  example, excessive or obstructive ads), and/or have complex application processes (for example,
  lead to many redirects). Poor user experience also reduces application completion rate.
- **Remove expired job posts**. Don't leave a job post open if it is no longer accepting new
  applications. Applying and not hearing back from the employer is a common complaint of job
  seekers. When you remove the job from your site, make sure to also remove the markup or update
  the [`validThrough`](/search/docs/appearance/structured-data/job-posting#valid-through)
  property. We encourage the use of [Indexing
  API](/search/apis/indexing-api/v3/quickstart) to update us on the change. Landing on an expired job post, especially after a few
  redirects, is a very frustrating experience.
- **Make sure that the job's posting date is genuine**. Users use freshness as a signal to
  assess if a position accepts new applicants, chances to get hired, attractiveness of the position
  and more. Don't mask old jobs as new ones and don't update the [`DatePosted`](/search/docs/appearance/structured-data/job-posting#date-posted) property if there was no change to the job post.
- **Don't include wrong or misleading information in the job post or the markup**. This
  includes incorrect salary, location, working hours, employment type, or other job specific
  details. To avoid this make sure that the job post describes the job correctly and that the
  markup is an accurate representation of the job post.

We work to ensure that the results presented on Google are trustworthy and provide a good
experience for users. We have no doubt that this goal is shared with all sites that help job
seekers find a job. If you have any questions or thoughts, reach out to us on the
[Google
Search Central Community](https://support.google.com/webmasters/community) or on [Twitter](https://twitter.com/googlesearchc).
