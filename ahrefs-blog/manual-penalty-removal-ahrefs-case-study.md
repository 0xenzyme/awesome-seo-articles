---
title: "Manual Penalty Removal: An Ahrefs Case Study"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "manual-penalty-removal-ahrefs-case-study"
url: "https://ahrefs.com/blog/manual-penalty-removal-ahrefs-case-study/"
canonical: "https://ahrefs.com/blog/manual-penalty-removal-ahrefs-case-study/"
author: "Chris Dreyer"
published: "2017-02-03T15:13:00+00:00"
updated: "2025-12-18T14:18:36+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:47:14+00:00"
status_code: 200
html_hash: "9bc54bde81f7be17fc47471b8f8b77fc35027eee9d2ebfb74d4c2d3e5ee34226"
clean_word_count: 1066
clean_char_count: 6301
---
# Manual Penalty Removal: An Ahrefs Case Study

Making a site perform well in search sometimes means removing things like spammy links, which could be hurting a website’s performance. This process can be tedious and time consuming, but very beneficial once it’s complete.

We have documented a process we’ve used to successfully remove a manual penalty, so that other webmasters can see just how it’s done using Ahrefs [Site Explorer](https://ahrefs.com/site-explorer) and Google’s process for cleaning up bad links.

### Finding Toxic Links

A site we are working on already had a manual penalty. Keep in mind, most website owners will not need to go through a comprehensive link removal campaign. But in this case, the website owner was assigned a manual penalty and we had to take action to get it removed.

The best way to find out if you have received a penalty is to configure your website with Google Webmaster Tools. Google will inform you by email if it has applied manual action against your site as a result of unnatural links.

Once you know that you have a penalty, the first step in the process is finding the links that are pointing at the site, that may be [contributing to the penalty](https://ahrefs.com/blog/bad-links/). In our scenario, we used Ahrefs to analyze the backlink profile of the penalized website.

Ahrefs provides metrics for identifying domain authority, inbound links, link acquisition timeframe, anchor-text and more. By understanding what these metrics mean, we were able to narrow down the list of suspects.

In the backlinks report in Ahrefs, we sorted referring domains by Ahrefs Domain Rating and anchor text in the following ways:

1. We sorted all domains by Domain Rating. We added all sites with DR 40 to our outreach list.
2. We did an anchor-text distribution sort. If we found a high percentage of Exact Match Anchors on a site with DR 50 (or a site that just appeared to be spammy), we added them to our outreach list as well.

#### Sorting by Domain Rating

![](https://ahrefs.com/blog/wp-content/uploads/2015/02/DR-sort-in-backlinks-report.jpg)

#### Sorting by anchor text

### Inspecting Our Links

By using Ahrefs we were able to narrow down the list of suspected toxic domains using their metrics (like DR) that indicate their quality.

We went through our initial list and identified any domains that appeared spammy, had low domain authority, were not curated, had an unnatural anchor-text distribution percentage, irrelevant anchor-text use and added them to our “outreach list”.

This part of the process can be very subjective. In general, we were looking for websites that clearly didn’t have any real value to offer. They may have had poorly written content or were just completely irrelevant to the main site they were linking to. We did not want the website we were trying to recover to be associated with any site that may have violated Google quality guidelines.

### Outreach

Once we had our outreach list finished, the next step was to manually contact these site owners and ask that the links be taken down.

The link removal outreach process is very time consuming depending upon the number of outreach candidates. Not all websites have contact information clearly listed. In those instances, we had to rely on whois lookup services to find administrative contact information. We sent emails and submitted to contact forms to owners requesting they remove our link from their site.

In many cases, we had to send multiple [outreach messages](https://ahrefs.com/blog/outreach) (up to 6 per/domain) in order to get a website owner’s attention. In other cases, there were no responses at all.

Sometimes site owners requested a bounty for removing links. This is simply a request for payment and in this case study, no bounty ever exceeded 20 dollars.

For our case study, the outreach lasted for about 2 months. We sent 6 emails and/or contact form messages per violating domain.

### Disavowing Links and the Reconsideration Request

Google understands that it isn’t always possible to get every site owner to communicate with you and remove links. That’s one reason they may have created the link disavow tool. As a method of collecting violating domains by volume.

We created a file of all the domains where we were unsuccessful with our outreach. We submitted the file to Google via the disavow links tool.

Editor’s Note

Today Ahrefs has a built-in tool to create disavow lists.

You can add domains or URLs to your disavow list directly from the backlinks report, as you inspect your backlink profile. Then you can easily export your disavow list from Ahrefs and import it into Google Disavow Tool.

Nick Churick

Along with the disavow links file, we also submitted a reconsideration request.

The request and the disavow file work in combination with one another. The disavow file lets Google know which specific pages or domains we do not want linking to our website. The request details our process for fixing the problem on our own and the steps we took to do that. The more information you can provide to Google as to exactly how you tried to remove bad links, the better. They want to see that you’ve made a concerted effort to clean things up before asking for their help.

The [request template](http://www.poweredbysearch.com/google-reconsideration-request-example/) that worked for us was created by Powered by Search. Instead of writing it from scratch, we were able to simply insert the relevant information where appropriate.

Once everything was in order, we submitted the request to google.

### The Result

It took about 4 weeks for the review process to take place. We then received the email below from Google stating that the manual action against the website we were working with had been removed.

This entire process took about 3 months from start to finish. With manual penalty removals, you have to be patient and meticulous. It may take more than one reconsideration request. Just be sure to document your efforts and abide by Google’s quality guidelines.

Further reading

Getting penalized by Google might be a result of a negative SEO attack.

Read this guide to learn how to identify negative SEO and fight it:

[How To Detect (And Deflect) Negative SEO](https://ahrefs.com/blog/negative-seo/)
