---
title: "Organic traffic graphs now reflect monthly search volume trends for keywords"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "high"
slug: "new-organic-traffic-graphs"
url: "https://ahrefs.com/blog/new-organic-traffic-graphs/"
canonical: "https://ahrefs.com/blog/new-organic-traffic-graphs/"
author: "Rebekah Bek"
published: "2021-05-07T03:32:00+00:00"
updated: "2022-02-02T07:05:54+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2022_old"
  - "product_or_tool_content"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:53:12+00:00"
status_code: 200
html_hash: "15e74196b0958f18f4fcd47434b0993f7515e8cd4eafcb34421d450efc4f1608"
clean_word_count: 379
clean_char_count: 2333
---
# Organic traffic graphs now reflect monthly search volume trends for keywords

We’ve rebuilt and updated the database used in [Organic Keywords 2.0](https://app.ahrefs.com/v2-site-explorer/organic-keywords/subdomains?country=us&target=ahrefs.com%2F), [Top Pages 2.0](https://app.ahrefs.com/v2-site-explorer/top-pages/subdomains?target=ahrefs.com%2F&country=us), and the Organic search tab and metrics in your Site Explorer Overview.

This affects everyone’s favorite Organic traffic graph:

![](https://ahrefs.com/blog/wp-content/uploads/2021/05/Overview_ahrefs_com_blog_on_Ahrefs-1.jpg)

### What’s new

- Everything runs faster!
- You can now toggle to see monthly search trends for many keywords.

Let’s get into that second point.

The old “Average volume” organic traffic chart was built using the **average of data over the latest 12 months** from an update. The benefit of this: the data looks more consistent, and it’s useful to troubleshoot things like traffic drops.

On the other hand, the new “Monthly volume” organic traffic chart is built using data **specific to that month**. While the data looks more volatile, it takes **volume trend** into account and is useful for spotting search trends and monitoring seasonal traffic fluctuations.

Here’s an example: *dodoburd.com*.

They’re an online gift shop, which means that they tend to rank for seasonal keywords like this one:

So dodoburd.com generally sees their traffic peaks during Christmas time. This wasn’t reflected on the old graph, but shows clearly on the new one.

Old chart: Latest 12-month average

New chart: Month-specific

And another example: *scribbr.nl*.

They’re a plagiarism checker software. Since search queries related to academic papers are used much less in the summer, the new data reflects that.

Old chart: Latest 12-month average

New chart: Month-specific

### Notes

- If you noticed **a drop in the organic traffic figures** shown on your Overview in Site Explorer, this was due to a bug in the traffic metric computation that affected some sites. We’ve **fixed this bug** and the database was rebuilt, so the numbers are now back to what they should have been.
- The old Organic keywords and Top pages/subfolders/subdomains have not been affected by this change retrospectively. The data in these reports will be updated over time.
