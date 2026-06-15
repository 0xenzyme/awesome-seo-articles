---
title: "Introducing the Indexing API for job posting URLs"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2018-06-introducing-indexing-api-for-job"
url: "https://developers.google.com/search/blog/2018/06/introducing-indexing-api-for-job"
canonical: "https://developers.google.com/search/blog/2018/06/introducing-indexing-api-for-job"
author: "Zach Clifford, Software Engineer"
published: "2018-06-26T00:00:00+00:00"
updated: "2018-06-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2018_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:32:28+00:00"
status_code: 200
html_hash: "519d7bea60512add22afe70877a4a9fff109e39dab687add65a43d7f5f4e78f1"
clean_word_count: 269
clean_char_count: 1732
---
# Introducing the Indexing API for job posting URLs

Last June we
[launched a job search experience](https://www.blog.google/products/search/connecting-more-americans-jobs/)
that has since connected tens of millions of job seekers around the world with relevant job
opportunities from third party providers across the web. Timely indexing of new job content is
critical because many jobs are filled relatively quickly. Removal of expired postings is important
because nothing's worse than finding a great job only to discover it's no longer accepting
applications.

Today we're releasing the [Indexing API](/search/apis/indexing-api) to address this
problem. This API allows any site owner to directly notify Google when job posting pages are added
or removed. This allows Google to schedule job postings for a fresh crawl, which can lead to
higher quality user traffic and job applicant satisfaction. Currently, the Indexing API can only
be used for job posting pages that include
[job posting structured data](/search/docs/appearance/structured-data/job-posting).

For websites with many short-lived pages like job postings, the Indexing API keeps job postings
fresh in Search results because it allows updates to be pushed individually. This API can be
integrated into your job posting flow, allowing high quality job postings to be searchable quickly
after publication. In addition, you can check the last time Google received each kind of
notification for a given URL.

Follow the [Quickstart](/search/apis/indexing-api/v3/quickstart) guide to see how the
Indexing API works. If you have any questions, ask us in the
[Webmaster Help Forum](https://support.google.com/webmasters/community). We look forward to hearing
from you!
