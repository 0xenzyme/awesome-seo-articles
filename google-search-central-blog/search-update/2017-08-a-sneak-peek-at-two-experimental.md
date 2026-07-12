---
title: "The new Search Console: a sneak peek at two experimental features"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2017-08-a-sneak-peek-at-two-experimental"
url: "https://developers.google.com/search/blog/2017/08/a-sneak-peek-at-two-experimental"
canonical: "https://developers.google.com/search/blog/2017/08/a-sneak-peek-at-two-experimental"
author: "John Mueller"
published: "2017-08-01T00:00:00+00:00"
updated: "2017-08-01T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:30:41+00:00"
status_code: 200
html_hash: "9dc6b569e7e857314022c6e2483ef12aae63d71af2356ea73212540351148424"
clean_word_count: 530
clean_char_count: 3250
---
# The new Search Console: a sneak peek at two experimental features

Search Console was
[initially launched](https://sitemaps.blogspot.com/2005/11/more-stats)
with just four reports more than a decade ago. Today, the product includes more than two dozen
reports and tools covering AMP, structured data, and live testing tools, all designed to help
improve your site's performance on Google Search.

Now we have decided to embark on an extensive redesign to better serve you, our users. Our hope is
that this redesign will provide you with:

- **More actionable insights** - We will now group the identified issues by what we
  suspect is the common "root-cause" to help you find where you should fix your code. We organize
  these issues into tasks that have a state (similar to bug tracking systems) so you can easily
  see whether the issue is still open, whether Google has detected your fix, and track the
  progress of re-processing the affected pages.
- **Better support of your organizational workflow** - As we talked to many
  organizations, we've learned that multiple people are typically involved in implementing,
  diagnosing, and fixing issues. This is why we are introducing sharing functionality that allows
  you to pick-up an action item and share it with other people in your group, like developers who
  will get references to the code in question.
- **Faster feedback loops between you and Google** - We've built a mechanism to allow
  you to iterate quickly on your fixes, and not waste time waiting for Google to recrawl your
  site, only to tell you later that it's not fixed yet. Rather, we'll provide on-the-spot testing
  of fixes and are automatically speeding up crawling once we see things are ok. Similarly, the
  testing tools will include code snippets and a search preview - so you can quickly see where
  your issues are, confirm you've fixed them, and see how the pages will look on Search.

In the next few weeks, we're releasing two exciting BETA features from the new Search Console to a
small set of users—Index Coverage report and AMP fixing flow.

The new Index Coverage report shows the count of indexed pages, information about why some pages
could not be indexed, along with example pages and tips on how to fix indexing issues. It also
enables a simple sitemap submission flow, and the capability to filter all Index Coverage data to
any of the submitted sitemaps.

Here's a peek of our new Index Coverage report:

![](/static/search/blog/images/import/0f7ad6a5346eb963358cf11586735ef8.png)

## The new AMP fixing flow

The new AMP fixing experience starts with the AMP Issues report. This report shows the current AMP
issues affecting your site, grouped by the underlying error. Drill down into an issue to get more
details, including sample affected pages. After you fix the underlying issue, click a button to
verify your fix, and have Google recrawl the pages affected by that issue. Google will notify you
of the progress of the recrawl, and will update the report as your fixes are validated.

![](/static/search/blog/images/import/ecd1d6e690a8f1d7ce69c82f344a6ce9.png)

As we start to experiment with these new features, some users will be introduced to the new
redesign through the coming weeks.
