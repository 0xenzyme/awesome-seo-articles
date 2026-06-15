---
title: "Googlebot activity reports"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-10-googlebot-activity-reports"
url: "https://developers.google.com/search/blog/2006/10/googlebot-activity-reports"
canonical: "https://developers.google.com/search/blog/2006/10/googlebot-activity-reports"
author: null
published: "2006-10-19T00:00:00+00:00"
updated: "2006-10-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:46:39+00:00"
status_code: 200
html_hash: "87fb16ea3aa62f41db6a10cbe4d2bb7780cb5d11cce5cc8f71ecdcc6edc5f0b2"
clean_word_count: 507
clean_char_count: 3022
---
# Googlebot activity reports

The [Webmaster Tools](https://search.google.com/search-console)
team has a very exciting mission: we dig into our logs, find as much useful information as
possible, and pass it on to you, the webmasters. Our reward is that you more easily understand
what Google sees, and why some pages don't make it to the index.

The latest batch of information that we've put together for you is the amount of traffic between
Google and a given site. We show you the number of requests, number of kilobytes (yes, yes, I
know that tech-savvy webmasters can usually dig this out, but our new charts make it really easy
to see at a glance), and the average document download time. You can see this information in chart
form, as well as in hard numbers (the maximum, minimum, and average).

For instance, here's the number of pages Googlebot has crawled in the Webmaster Central blog over
the last 90 days. The maximum number of pages Googlebot has crawled in one day is 24 and the
minimum is 2. That makes sense, because the blog was launched less than 90 days ago, and the chart
shows that the number of pages crawled per day has increased over time. The number of pages
crawled is sometimes more than the total number of pages in the site—especially if the same
page can be accessed via several URLs. So
</search/blog/2006/10/learn-more-about-googlebots-crawl-of>
and
</search/blog/2006/10/learn-more-about-googlebots-crawl-of#enhanced-image-search>
are different, but point to the same page (the second points to an anchor within the page).

![pages crawled by googlebot graph in webmaster tools](/static/search/blog/images/import/11cff11b12cfb286ae81a63dc9757f25.png)

And here's the average number of kilobytes downloaded from this blog each day. As you can see, as
the site has grown over the last two and a half months, the number of average kilobytes downloaded
has increased as well.

![average number of kilobytes downloaded stats in webmaster tools](/static/search/blog/images/import/2b673f48a6a4b1216997fa409bbc565d.png)

The first two reports can help you diagnose the impact that changes in your site may have on its
coverage. If you overhaul your site and dramatically reduce the number of pages, you'll likely
notice a drop in the number of pages that Googlebot accesses.

The average document download time can help pinpoint subtle networking problems. If the average
time spikes, you might have network slowdowns or bottlenecks that you should investigate. Here's
the report for this blog that shows that we did have a short spike in early September (the
maximum time was 1057 ms), but it quickly went back to a normal level, so things now look OK.

![average time spent downloading from individual urls stats in webmaster tools](/static/search/blog/images/import/1e87de535746aa3ce95e1243a51ceb26.png)

In general, the load time of a page doesn't affect its ranking, but we wanted to give this info
because it can help you spot problems. We hope you will find this data as useful as we do!
