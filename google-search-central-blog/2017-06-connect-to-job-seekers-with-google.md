---
title: "Connect to job seekers with Google Search"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2017-06-connect-to-job-seekers-with-google"
url: "https://developers.google.com/search/blog/2017/06/connect-to-job-seekers-with-google"
canonical: "https://developers.google.com/search/blog/2017/06/connect-to-job-seekers-with-google"
author: "Nick Zakrasek, Product Manager"
published: "2017-06-20T00:00:00+00:00"
updated: "2017-06-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:30:29+00:00"
status_code: 200
html_hash: "acd510fd011f09401ad250ee8f7b0e5c0d6c7098e1f2937b0367b0df8609311d"
clean_word_count: 536
clean_char_count: 3450
---
# Connect to job seekers with Google Search

At Google I/O this year, we
[announced Google for Jobs](https://youtu.be/Y2VF8tmLFHw?t=6704),
a new company-wide initiative focused on helping both job seekers and employers, through
collaboration with the job matching industry. One major part of this effort is launching an
improved experience for job seekers on Google Search. We're happy to announce this new experience
is now open for all developers and site owners.

For queries with clear intent like
["head of catering jobs in nyc"](https://www.google.com/search?q=head+of+catering+jobs+nyc)
or
["entry level jobs in DC"](https://www.google.com/search?q=entry+level+jobs+in+dc),
we'll show a job listings preview, and each job can expand to display comprehensive details about
the listing:

![examples of job listings on a search result page and a detailed view of an individual job listing](/static/search/blog/images/import/869437ec8866b8381d90716ceb13e955.png)

For employers or site owners with job content, this feature brings many benefits:

- **Prominent place in Search results**: your postings are eligible to be displayed
  in the new job search feature on Google, featuring your logo, reviews, ratings, and job details.
- **More, motivated applicants**: job seekers can filter by various criteria like
  location or job title, meaning you're more likely to get applicants who are looking exactly for
  that job.
- **Increased chances of discovery and conversion**: job seekers will have a new
  avenue to interact with your postings and click through to your site.

## Get your job listings on Google

Implementation involves two steps:

1. Mark up your job listings with
   [Job Posting structured data](/search/docs/appearance/structured-data/job-posting).
2. Submit a sitemap (or an RSS or Atom feed) with a `<lastmod>` date for each
   listing.

If you have more than 100,000 job postings or more than 10,000 changes per day, you can
[express interest](https://docs.google.com/a/google.com/forms/d/e/1FAIpQLSdlj1CC6jX1wNV-jwfJ_0QNR5Cq6gpkIfjBo5e_Rx_VmYcGsg/viewform)
to use the High Change Rate feature.

If you already publish your job openings on another site like LinkedIn, Monster, DirectEmployers,
CareerBuilder, Glassdoor, and Facebook, they are eligible to appear in the feature as well.

Job search is an enriched search experience. We've created a
[dedicated guide](/search/docs/appearance/enriched-search-results) to help you
understand how Google ranking works for enriched search and practices for improving your presence.

## Keep track of how you're doing and fix issues

There's a suite of tools to help you with the implementation:

- Validate your markup with the
  [Structured Data Testing Tool](/search/docs/advanced/structured-data)
- Preview your listing in the Structured Data Testing Tool
- [Keep track of your sitemap](https://support.google.com/webmasters/answer/183669)
  status in Search Console
- [See aggregate stats and markup error examples](https://support.google.com/webmasters/answer/6381755)
  in Search Console

In the coming weeks, we'll add new job listings filters in the
[Search Analytics report](https://support.google.com/webmasters/answer/6155685)
in Search Console, so you can track clicks and impressions for your listings.

As always, if you have questions, ask in the
[forums](https://support.google.com/webmasters/community) or find us on
[Twitter](https://twitter.com/googlesearchc)!
