---
title: "Do Links Still Matter for Rankings? A Study by Ahrefs"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "impact-of-links"
url: "https://ahrefs.com/blog/impact-of-links/"
canonical: "https://ahrefs.com/blog/impact-of-links/"
author: "Patrick Stox"
published: "2021-12-09T16:00:00+00:00"
updated: "2024-03-18T14:35:12+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:41:08+00:00"
status_code: 200
html_hash: "3213d0f5d8cd064d6de6804db5ca7b71b7bf22441beae3028369c38268a3f012"
clean_word_count: 935
clean_char_count: 5366
---
# Do Links Still Matter for Rankings? A Study by Ahrefs

In the past few years, I’ve seen more people saying that links are dead, they don’t matter for rankings, or they’ve lost their importance. Links are a confirmed major ranking factor, so I figured it would be interesting to test their impact.

Instead of building links to pages, I figured the easiest way to test this would be to remove links to a page and see what happened. With the help of [Joshua Hardwick](https://twitter.com/joshuachardwick?lang=en), Ahrefs’ head of content, we picked three articles and [disavowed](https://ahrefs.com/blog/google-disavow-links/) all links to these pages for a month, thus removing the value of the external links. A month later, I removed them from the disavow file, which should have restored the value of the links.

The disavow file was processed immediately, but the [links inside the file still needed to be recrawled](https://www.seroundtable.com/google-processes-disavowed-files-29008.html) before the impact of the disavow could be seen. It was the same once the disavow was removed. The linking pages had to be crawled again for us to see the impact. I figured a month for each time period should be long enough for the most important links to be crawled and for us to see an impact.

We disavowed 3,476 links across three blog posts. It was uploaded on Aug. 17 and removed four weeks later on Sept. 14.

**Spoiler alert:** Links still matter. Traffic and ranking keywords were down after I disavowed the links and up after I removed the disavow file.

Organic traffic disavow test.

Look at the immediate drop in traffic when I uploaded the disavow file on Aug. 17. The downward trend continued for a while as more of the pages linking to these blogs were crawled. You can also see the immediate lift when I removed the disavow file on Sept. 14. I suspect this immediate impact is because more valuable links are on pages that probably have higher [PageRank](https://ahrefs.com/blog/google-pagerank/) and are crawled more often.

Now let’s look at the examples in more detail.

## The test pages

The chart above shows Ahrefs’ Average Organic Traffic, which is a stable metric that measures search visibility. It approximates traffic based on rankings and expected CTR for all the keywords a page ranks for.

I wanted a stable metric because things like clicks or impressions could be impacted by seasonality or user behaviors. The metrics for clicks and impressions from Google Search Console mostly followed the same trends, but not in all cases.

The test covered three different pages in total, so let’s look at each example.

### Example 1.

**Page:** [Top YouTube Searches (2021)](https://ahrefs.com/blog/top-youtube-searches/)

I expected that we would lose rankings for some of the more popular searches and end up losing some traffic because of how competitive this topic is. That ended up being accurate. This page lost about 18% of its search traffic in the first month. But I didn’t expect it to be another 4% down after we removed the disavow file.

We’ve recovered over half of the loss since then, but the search traffic is still down overall.

Let’s look at why.

Here are some of the terms that influenced our traffic estimates the most and their ranking positions during the test.

For “youtube searches,” a YouTube page and a Google Trends page pushed our page down in the results during the test. We are back to #1 and have recovered the traffic for this term.

For “what is the most searched thing on youtube” and “most searched thing on youtube,” a competitor took the featured snippet from us and still holds it.

### Example 2.

**Page:** [SEO Pricing: ~350 Agencies, Consultants, and Freelancers Reveal How Much SEO Costs](https://ahrefs.com/blog/seo-pricing/)

I wasn’t expecting much of an impact on this page by removing the links simply because the competition here was a lot weaker. But in this case, I was wrong. While the links were disavowed, this page lost 13.3% of its traffic. But when we removed the file, the page got back to 99% of the previous traffic.

Here are some of the terms that influenced our traffic estimates the most and their ranking positions during the test.

### Example 3.

**Page:** [Top Bing Searches (2021)](https://ahrefs.com/blog/top-bing-searches/)

Because of the competition here, I expected this page to see a decent drop. Interestingly, the traffic barely dropped during the disavow period. But once I removed the disavow file, the page shot up in traffic by over 44%.

This is actually the page that messed with the trends for clicks and impressions. I think that’s mostly because a lot of the terms weren’t really impacted.

Only one term really impacted the traffic estimates for this page.

## Conclusion

Links still matter. The pages tested are still down from where they started. It could be because of algorithm changes, of links not being recrawled yet, or that other sites got more links while we dropped. But I’m hopeful we’ll be back to at least where we were.

I definitely do not recommend disavowing all the links to your pages. The disavow tool, in general, should be used with caution, as Google mostly devalues bad links for you these days.

Do you think we should run this test multiple times to see what happens? Let me know [on Twitter](https://twitter.com/patrickstox).
