---
title: "Help job seekers understand your job postings by including a complete description"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2021-11-improve-job-posting-description"
url: "https://developers.google.com/search/blog/2021/11/improve-job-posting-description"
canonical: "https://developers.google.com/search/blog/2021/11/improve-job-posting-description"
author: "Bobby Panczer, Software Engineer"
published: "2021-11-01T00:00:00+00:00"
updated: "2021-11-01T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:39:53+00:00"
status_code: 200
html_hash: "38fad25c976a476f3f7d85fcfaa93c460fdf461cde08f689c8fd6348ff3f0592"
clean_word_count: 412
clean_char_count: 2949
---
# Help job seekers understand your job postings by including a complete description

We've uncovered an opportunity to improve your job posting pages, and it only takes a few changes to the `description` field.

In the `description` section of a posting in the jobs experience on Google Search, we only present text that is included in the [`description`](/search/docs/appearance/structured-data/job-posting#description) property. That's why it's important
to include information about job qualifications, skills, benefits, etc. in the `description` field.

The following screenshot illustates proper use of the `description` field, as the job posting includes all relevant data for the user to make a
more informed decision on whether or not they'd be interested in applying for the job.

![description of a job posting in Google Search results](/static/search/blog/images/job-posting-in-search.png "description of a job posting in Google Search")

Here are two examples of both a complete and incomplete
job posting markup implementation:

Here's an example of a **complete `description` field**. The job `description` field includes all of the relevant information about the job, including qualifications.

```
{
    "@context" : "https://schema.org/",
    "@type" : "JobPosting",
    "title" : "Software Engineer",
    "description" : "Software Engineer responsible for creating web applications. Knowledge of HTML, Javascript, APIs, and relational databases. Must have 2-5 years of experience.", // this description was shortened for this example
    "qualifications": "Knowledge of HTML, Javascript, APIs, and relational databases. Must have 2-5 years of experience." // this is an optional property
    }
```

Here is an example of an **incomplete `description` field**. The `description` only includes a brief `description` of the job, and the qualifications are only listed in the
`qualifications` property. To correct this, include all information from the `qualifications` field in the `description` field.

```
{
  "@context" : "https://schema.org/",
  "@type" : "JobPosting",
  "title" : "Software Engineer",
  "description" : "Software Engineer responsible for creating web applications",
  "qualifications": "Knowledge of HTML, Javascript, APIs, and relational databases. Must have 2-5 years of experience."
  }
```

To make sure users can view the full job description in the jobs experience on Google Search, review the `description` field and make sure it includes all information that
you may have included only in specific fields (like the `qualifications` property). You don't need to remove the more specific fields; just make sure that you also include
the same information in the `description` property itself.

If you have any questions, you can discuss with experts in the [Search Central community](https://support.google.com/webmasters/community), or get in touch with
us [on Twitter](https://twitter.com/googlesearchc).
