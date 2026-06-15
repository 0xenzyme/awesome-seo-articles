---
title: "Make your site's complete jobs information accessible to job seekers"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2017-11-make-your-sites-complete-jobs"
url: "https://developers.google.com/search/blog/2017/11/make-your-sites-complete-jobs"
canonical: "https://developers.google.com/search/blog/2017/11/make-your-sites-complete-jobs"
author: "Nick Zakrasek, Product Manager"
published: "2017-11-15T00:00:00+00:00"
updated: "2017-11-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:31:02+00:00"
status_code: 200
html_hash: "629c89f58947bc8bbced1f0766021d6db31998abb273935e081e01326f2eeeb1"
clean_word_count: 512
clean_char_count: 3521
---
# Make your site's complete jobs information accessible to job seekers

In June, we
[announced a new experience](https://www.blog.google/products/search/connecting-more-americans-jobs/)
that put the convenience of Search into the hands of job seekers. Today, we are taking the next
step in improving the job search experience on Google by adding a feature that shows estimated
salary information from the web alongside job postings, as well as adding new UI features for
users.

Salary information has been one of the most requested additions from job seekers. This helps
people evaluate whether a job is a good fit, and is an opportunity for sites with estimated salary
information to:

- **Increase brand awareness**: Estimated salary information shows a representative logo from
  the estimated salary provider.
- **Get more referral traffic**: Users can click through directly to salary estimate pages
  when salary information surfaces in job search results.

If your site provides salary estimates, you can take advantage of these changes in the following
ways:

## Specify actual salary information

Actual salary refers to the base salary information that is provided by the employer. If your site
publishes job listings, you can add
[`JobPosting` structured data](/search/docs/appearance/structured-data/job-posting)
and populate the `baseSalary` property to be eligible for inclusion in job search
results.

This salary information will be made available in both the list and the detail views.

![](/static/search/blog/images/import/168fd1020e88b207e21efeaade7604f8.png)

## Provide estimated salary information

In cases where employers don't provide actual salary, job seekers may see estimated salaries
sourced from multiple partners for the same or similar occupation. If your site provides salary
estimate information, you can add
[Occupation structured data](/search/docs/appearance/structured-data/estimated-salary)
to be eligible for inclusion in job search results.

![](/static/search/blog/images/import/b77558145b0598d7311af59f1bf8791a.png)

## Include exact location information

We've heard from users that having accurate, street-level location information helps them to focus
on opportunities that work best for them. Sites that publish job listings can do this by using the
jobLocation property in
[JobPosting structured data](/search/docs/appearance/structured-data/job-posting#JobPosting-definition).

## Validate your structured data

To double-check the structured data on your pages, we'll be updating the
[Structured Data Testing Tool](/search/docs/advanced/structured-data)
and the
[Search Console reports](https://support.google.com/webmasters/answer/6381755)
in the near future. In the meantime, you can
[monitor the performance of your job postings in Search Analytics](https://support.google.com/webmasters/answer/7042828).
Stay tuned!

Since launching this summer, we've seen over 60% growth in number of companies with jobs showing
on Google and connected tens of millions of people to new job opportunities. We are excited to
help users find jobs with salaries that meet their needs, and to route them to your site for more
information. We invite sites that provide salary estimates to mark up their salary pages using the
[Occupation structured data](/search/docs/appearance/structured-data/estimated-salary).
Should you have any questions regarding the use of structured data on your site, drop by our
[webmaster help forums](https://support.google.com/webmasters/go/community).
