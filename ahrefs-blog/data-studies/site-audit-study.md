---
title: "We Studied Over 1 Million Domains to Find the Most Common Technical SEO Issues"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "site-audit-study"
url: "https://ahrefs.com/blog/site-audit-study/"
canonical: "https://ahrefs.com/blog/site-audit-study/"
author: "Patrick Stox"
published: "2023-08-31T05:03:17+00:00"
updated: "2024-08-19T11:32:36+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
fetched_at: "2026-06-12T12:10:06+00:00"
status_code: 200
html_hash: "d9e3a49b218e5edbe020e80a96325935a098c913b1ffb346ea78d704258ff323"
clean_word_count: 2535
clean_char_count: 14245
---
# We Studied Over 1 Million Domains to Find the Most Common Technical SEO Issues

There’s a lot that can go wrong on a website, and every site is going to have some issues to fix.

We looked at 1,002,165 domains to find the most common technical SEO issues. Keep reading to see what we found.

## The 15 most common technical SEO issues

These are the issues flagged the most across the 1 million+ domains. The number is the percentage of domains where the issues were found on at least one of their pages.

![The most common technical SEO issues from a study of over 1 million domains](https://ahrefs.com/blog/wp-content/uploads/2023/08/site-audit-study-1.png)

These are the most common issues, but every website is different. You can use Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) to get reports about the issues on your own website. This is free for verified sites with an [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) (AWT) account.

I made a sheet with [the rest of the issues](https://docs.google.com/spreadsheets/d/1u1vKUmRBvG6k_sWoKu-_8a8M_JTQA42P/edit?usp=sharing&ouid=102636613735538965223&rtpof=true&sd=true) if you just want the data. If you want my commentary on the top issues and prioritization for fixing them, keep reading.

### 3XX redirect – 95.2% of sites

Most sites use [redirects](https://ahrefs.com/blog/301-redirects/), and it’s not usually anything to worry about. Sites, and the web in general, are always changing. We ran a study that found that [~two-thirds of links to pages on the web disappeared](https://ahrefs.com/blog/link-rot-study/) in the nine-year period we looked at.

I’d be concerned if there are redirect loops, where a page gets redirected infinitely, or when there is a long chain of redirects. Google will follow up to five redirect hops in one session. And when it resumes crawling in the next session, it will follow up to five more. Anything over 10 hops won’t consolidate signals (like links) properly to the final URL.

You can find both of these in the “Issues” tab in the **Redirects** report in [Site Audit](https://ahrefs.com/site-audit).

### HTTP to HTTPS redirect – 88% of sites

If you see this, great! You want your site to be on [HTTPS](https://ahrefs.com/blog/what-is-https/).

We have this as a notification in [Site Audit](https://ahrefs.com/site-audit), and you shouldn’t be concerned unless the redirect is going the other way—from HTTPS to HTTP. You can find the HTTPS to HTTP redirects in the “Issues” tab of the **Internal pages** report in Site Audit:

A surprising number of sites, >6%, are redirecting the wrong way.

One of the other issues that can happen along with HTTP to HTTPS redirects is “mixed content” issues. You can find this in the “Issues” tab of the **Internal pages** report in Site Audit:

Some people spend a lot of time updating all of the references to other file types to solve these. There’s a better way.

If you set a [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) for upgrade-insecure-requests, it will solve all of your “mixed content” issues. It only takes a couple of minutes to set a rule in your .htaccess or server config for this.

In .htaccess, you simply add:

`<ifModule mod_headers.c>
Header always set Content-Security-Policy "upgrade-insecure-requests;"
</IfModule>`

### Missing alt attributes – 80.4% of sites

Missing [alt attributes](https://ahrefs.com/blog/alt-text/) is an accessibility issue, which may turn into a legal issue. Most big companies have been sued for ADA compliance issues on their websites, and some get sued multiple times a year. I’d fix this for the main content images, but not for things like placeholder or decorative images where you can leave the alt attributes blank.

For web search, the text in alt attributes counts as text on the page, but that’s really the only role it plays. Its importance is often overstated for SEO, in my opinion. However, it does help with image search and image rankings.

You can find missing alt attributes in the **Images** report:

### Meta description tag missing or empty – 72.9% of sites

I don’t worry much about missing [meta descriptions](https://ahrefs.com/blog/meta-description/). They don’t impact rankings. Google will write one for you if you don’t have one or sometimes rewrite yours even if you do have one. When we ran a study, we found that [Google rewrites meta descriptions 62.78% of the time](https://ahrefs.com/blog/meta-description-study/).

Still, there are times when I focus on them. Try to add meta descriptions when creating a page. If it’s missing on a page you really care about or that gets a lot of traffic, you may want to add it. You may also want to add one if you have a unique selling point or offer you think can be compelling for users.

You’ll find the “missing meta description” issue in the **Content** report in [Site Audit](https://ahrefs.com/site-audit).

If you click into the issue, you can sort the pages by “Organic traffic” in the report.

### Slow page – 72.3% of sites

We usually deem a page as slow by using our own subjective measure of speed. To get a better idea, I recommend enabling [Core Web Vitals](https://ahrefs.com/blog/core-web-vitals/) in your project’s crawl settings.

This is going to connect you to [Google PageSpeed Insights](https://ahrefs.com/blog/pagespeed-insights/) and will pull the Core Web Vitals metrics into [Site Audit](https://ahrefs.com/site-audit). These are the metrics Google actually uses in its rankings and are pulled from the same data source.

Some other auditors will pull lab test versions of these metrics. But if the tool isn’t connecting to PageSpeed Insights, you’re not getting the actual Core Web Vitals data, which comes from real-world users of Google Chrome. If they’re showing you Total Blocking Time (TBT) from Lighthouse instead of [First Input Delay (FID)](https://ahrefs.com/blog/first-input-delay-fid/) or Interaction to Next Paint (INP), that’s an easy way to tell the difference.

We give you the Lighthouse-based test scores, as well as the Core Web Vitals test scores. Check out the **Performance** report in Site Audit for these issues and more.

### Page and SERP titles do not match – 68.5% of sites

You may want to improve the [page title](https://ahrefs.com/blog/title-tag-seo/) if it’s not relevant to the page since it is a ranking factor. You may also want to improve titles for pages getting a lot of search traffic where you think you can do a better job than Google.

You can find the “Page and SERP titles do not match” issue in the “Issues” tab of the **Content** report in [Site Audit](https://ahrefs.com/site-audit).

If you click into the issue, you can sort the pages by “Organic traffic” in the report.

I made a script a while back that you can use to see which of your titles Google changed the most from their original text. It’s really easy to use. Here’s the [script](https://colab.research.google.com/drive/1mg3DTWVkgX0KHD3Hx2Y3WyMAUDjdm3cB?usp=sharing) and a video of how to use it.

https://www.youtube.com/watch?v=rHEhV-8vvn4

### Page has only one dofollow incoming internal link – 66.2% of sites

At least it’s not a completely [orphaned page](https://ahrefs.com/blog/orphan-pages/). But if it’s a page that you want to rank, you may want to add some more [internal links](https://ahrefs.com/blog/internal-links-for-seo/).

The easiest way to see internal link opportunities is with our tool in [Site Audit](https://ahrefs.com/site-audit). We look at what your pages are ranking for and suggest links from other pages on your site that talk about those things.

### Title too long – 63.2% of sites

We estimate if the title tag is being cut off on the [SERPs](https://ahrefs.com/blog/serps/), but you may want to manually check if it’s cut off on desktop or mobile searches. Mobile typically allows longer titles than desktop. We plan to actually check the SERPs for you in the future. But for now, you may want to check pages that are important to you.

If the title is cut off, you may want to adjust your tag to fit. However, the ranking is based on the whole title tag, not just what is shown on the SERPs, so you may want to leave it alone.

### Page has links to redirect – 62.7% of sites

As long as the redirects resolve to another page and there are fewer than 10 hops (like I mentioned earlier), this is fine. I usually put issues like this in the backlog for someone to clean up when they get a chance, but I don’t consider it a big issue and don’t prioritize it.

You may want to check if any of the chains are too long. Look for this in the “Issues” tab in the **Redirects** report.

![Redirect chain too long and redirect loop issues, via Ahrefs' Site Audit

### H1 tag missing or empty – 59.5% of sites

I consider [H1 tags](https://ahrefs.com/blog/h1-tag/) missing a minor issue, especially if the text is wrapped in an H2 tag instead. It’s usually an easy fix to change them, so I’ll mostly do it—but I don’t expect much impact.

You can find the issue in the **Content** report in [Site Audit](https://ahrefs.com/site-audit).

### Meta description too short – 59.2% of sites

You already saw that I generally don’t worry about missing meta descriptions, so why would I worry if they’re too short? But if it’s a page you care about and you have something to add to the description, go for it.

Like I mentioned before, I think meta descriptions are a good place to add unique selling points or offers if you have them.

You can find the issue in the **Content** report in [Site Audit](https://ahrefs.com/site-audit).

### Open Graph tags incomplete – 56% of sites

Not every page needs [Open Graph meta tags](https://ahrefs.com/blog/open-graph-meta-tags/), so I’m not surprised by how often these are missing. They’re really only needed for pages that you may share on social media.

I typically don’t consider these tags to be related to SEO. The only time they may be used for something SEO-related is when they’re used in Google Discover instead of your title or feature image.

The only benefit they can have for SEO is that you may get a bit more exposure on social media, which potentially leads to some additional links. They are not used directly in rankings.

### Meta description too long – 54.5% of sites

If you haven’t already realized it, I don’t focus much on meta descriptions. If it’s a page that’s important to you and you can write a better meta description that fits, go for it.

I’ve just seen too many audits recommending that someone should rewrite 800 meta descriptions, and I cry for that poor soul.

You can find the issue in the **Content** report in [Site Audit](https://ahrefs.com/site-audit).

### Multiple H1 tags – 51.3% of sites

Multiple [H1 tags](https://ahrefs.com/blog/h1-tag/) are allowed in modern HTML, and Google has said this is not a problem. HTML5 has supported multiple H1s since it launched in 2014.

I’d just check to make sure all of the headings you have as H1s are relevant to the page.

You can find the issue in the **Content** report in [Site Audit](https://ahrefs.com/site-audit).

![Pie chart showing H1 issues, via Ahrefs' Site Audit

### Meta description tag missing or empty (non-indexable page) – 50.8% of sites

We split a lot of different issues based on if a page is indexable or not indexable. This is meant to save you time by not focusing on issues on pages that aren’t indexed anyway.

For instance, you wouldn’t worry about a meta description on a page that can’t be indexed because that meta description can’t show up in a search result. Don’t spend time here.

Tip

Once again, here’s a sheet with [the rest of the issues](https://docs.google.com/spreadsheets/d/1u1vKUmRBvG6k_sWoKu-_8a8M_JTQA42P/edit?usp=sharing&ouid=102636613735538965223&rtpof=true&sd=true). Keep reading to learn more about prioritization of issues, which is what I consider the hardest thing for SEOs to get right.

## What should you fix?

What you prioritize to fix will be determined by the scale of the issues and which ones you think will have the most impact for your site.

We have a default prioritization for issues in [Site Audit](https://ahrefs.com/site-audit), but you can edit the priority by going to “Issue settings” at the top right of the Site Audit dashboard. I’ll warn you now that changing the issue prioritization will impact your Health Score!

In fact, you can fully [customize the issues](https://help.ahrefs.com/en/articles/1420169-how-to-configure-pre-set-issues-within-ahrefs-site-audit). You can edit existing issues, create new issues, change the priority of issues, or turn off ones that don’t matter to you.

Prioritizing fixes or even determining if you should fix some issues is one of the hardest parts of technical SEO. It gets even more complicated when you have to weigh fixing technical issues along with things like creating content or links.

Sometimes, the best course of action is to do nothing because the costs outweigh the benefits.

I don’t want to make assumptions about your sites in this study, but I have listed some of the projects I would prioritize in our [beginner’s guide to technical SEO](https://ahrefs.com/seo/technical-seo). We also have guides on doing a [technical audit](https://ahrefs.com/blog/technical-seo-audit/) and [fixing technical SEO issues](https://ahrefs.com/blog/seo-issues/) to give you more ideas.

The way I usually prioritize issues is by the impact I believe they will have and the effort that I (or my dev team) believe it will take to fix them. This makes for a nice visual for presentations and helps you see which fixes will have the most impact with the least effort.

## Final thoughts

A huge thanks and shoutout to my colleague, [Oleksiy Golvoko](https://twitter.com/zindelzindel?lang=en), for helping me gather this data! It was interesting to see the issues at a scale that has never been done before.

In case you missed the other two links to it, here is a [sheet with the rest of the issues](https://docs.google.com/spreadsheets/d/1u1vKUmRBvG6k_sWoKu-_8a8M_JTQA42P/edit?usp=sharing&ouid=102636613735538965223&rtpof=true&sd=true).

If you have any questions, message me [on Twitter](https://twitter.com/patrickstox).
