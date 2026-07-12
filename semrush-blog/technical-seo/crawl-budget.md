---
title: "Crawl Budget: What Is It and Why Is It Important for SEO?"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "crawl-budget"
url: "https://www.semrush.com/blog/crawl-budget/"
canonical: "https://www.semrush.com/blog/crawl-budget/"
author: "Marilyn Wilkinson, Chris Hanna, Simon Fogg"
published: "2023-09-25T10:14:00+00:00"
updated: "2024-06-27T10:55:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T14:52:29+00:00"
status_code: 200
html_hash: "aa454ade5cd3a0d029dc42d49404ceb5b1ae94c96d81c7562c1186da461a0d68"
clean_word_count: 4279
clean_char_count: 32419
---
# Crawl Budget: What Is It and Why Is It Important for SEO?

## What Is Crawl Budget?

Crawl budget is the number of URLs on your website that search engines like Google will crawl (discover) in a given time period. And after that, they’ll move on.

Here’s the thing:

There are billions of websites in the world. And search engines have limited resources—they can’t check every single site every day. So, they have to prioritize what and when to crawl.

Before we talk about how they do that, we need to discuss why this matters for your site’s SEO.

## Why Is Crawl Budget Important for SEO?

Google first needs to crawl and then [index your pages](https://www.semrush.com/blog/google-index/) before they can rank. And everything needs to go smoothly with those processes for your content to show in search results.

![How web crawlers work including crawling pages, fetching, sending & storing data plus influencing search results & rankings.](https://static.semrush.com/blog/uploads/media/ce/37/ce3781a366ad57cb3a52a12dee5237b0/211573c32591aa0cf62ee035c467f407/AD_4nXfmJCMjn_OFzrvfxI_-G2ICHFxtVfhYFADfBgQgEg1ilModo839PGsKYOdREIg0bZf9kdVTvsNLQY2lXhko1DJH93EigGyROoxt3rgo0HpKwurfG6bWealn9eVHiuY16hsVvmT1fIWGXrgejjXKsj9IkfXn.png)

That can significantly impact your [organic traffic](https://www.semrush.com/blog/organic-traffic/). And your overall business goals.

Most website owners don’t need to worry too much about crawl budget. Because Google is quite efficient at crawling websites.

But there are a few specific situations when Google’s crawl budget is especially important for SEO:

- **Your site is very large**: If your website is large and complex (10K+ pages), Google might not find new pages right away or recrawl all of your pages very often
- **You add lots of new pages**: If you frequently add lots of new pages, your crawl budget can impact the visibility of those pages
- **Your site has technical issues**: If [crawlability issues](https://www.semrush.com/blog/crawlability-issues/) prevent search engines from efficiently crawling your website, your content may not show up in search results

## How Does Google Determine Crawl Budget?

Your crawl budget is determined by two main elements:

### Crawl Demand

Crawl demand is how often Google crawls your site based on perceived importance. And there are three factors that affect your site’s crawl demand:

#### Perceived Inventory

Google will usually try to crawl all or most of the pages that it knows about on your site. Unless you instruct Google not to.

This means Googlebot may still try to crawl duplicate pages and pages you’ve removed if you don’t tell it to skip them. Such as through your robots.txt file (more on that later) or 404/410 [HTTP status codes](https://www.semrush.com/blog/http-status-codes/).

#### Popularity

Google generally prioritizes pages with more [backlinks](https://www.semrush.com/blog/what-are-backlinks/) (links from other websites) and those that attract higher traffic when it comes to crawling. Which can both signal to Google’s algorithm that your website is important and worth crawling more frequently.

Note the number of backlinks alone doesn’t matter—backlinks should be relevant and from authoritative sources.

Use Semrush [Backlinks](https://www.semrush.com/analytics/backlinks/) tool to see which of your pages attract the most backlinks and may attract Google’s attention.

Just enter your domain and click “**Analyze**.”

![Backlinks tool start with "chewy.com" entered as the domain and the "Analyze" button clicked.](https://static.semrush.com/blog/uploads/media/cf/29/cf29637f32671e7945a9178941568f82/fa57fff46da0387889f7b66e460d928d/AD_4nXeEvuhqaFzYVeEmG1BG-VbmYF7wDgzC-NLF-l5khD7OqlLsEXkwUVOBkK94q0WCmmkqNHmJKZldZ1-dTPqMS3Z4WoRSPQd5RzWmwyR0zTOantvA0La2cEwRFci8H9lSR53e81Bi7Ae9KFNN05CDwmuZkMxG.jpeg)

You’ll see an overview of your site’s backlink profile. But to see backlinks by page, click the “**Indexed Pages**” tab.

![Backlinks report showing an overview of a site's backlink profile along with the "Indexed Pages" tab highlighted.](https://static.semrush.com/blog/uploads/media/e0/81/e081df787d0198b3374b673790a472b3/1a5eeb54107687e2a4dfb7c11b89a959/AD_4nXfJqxB0cSLI2quE-UZD9PTseBY3KxbIoDde_X7ebOMtHJeopp8AYUsHFCQ42P0FzsJAvwXep6xFFUfWuhoKEnhL6Xrakwcb9zGclay5zC09bMgsSE9FKgMSqIl-Ci3th0x8bndZKGslHwfnOpetm1My_BUN.jpeg)

Click the “**Backlinks**” column to sort by the pages with the most backlinks.

![Indexed Pages on Backlinks showing pages sorted by number of backlinks.](https://static.semrush.com/blog/uploads/media/72/50/72509b0670585314bc661ddb21bea1b4/f4d507354e1a3a37d5ccc3c9d4ae568d/AD_4nXfdTMVhmB8fSCc-TqdF9zM7W3UGQrMEGGYoC3Ajnxbb7ivi7eVoQQzs68PxluK_o1Ir1hY-pR_nTUASlq2husSiK-8arNU6YDbYO9HlJ37oJo3Kp4JVoZMRPpyUwH3XCRZLfzSS1J2OMpldLrsAQnrEoXH5.jpeg)

These are likely the pages on your site that Google crawls most frequently (although that’s not guaranteed).

So, look out for important pages with few backlinks—they may be crawled less often. And consider implementing a [backlinking strategy](https://www.semrush.com/blog/how-to-get-backlinks/) to get more sites to link to your important pages.

#### Staleness

Search engines aim to crawl content frequently enough to pick up any changes. But if your content doesn’t change much over time, Google may start crawling it less frequently.

For example, Google typically crawls news websites a lot because they often publish new content several times a day. In this case, the website has high crawl demand.

This doesn’t mean you need to update your content every day just to try to get Google to crawl your site more often. [Google’s own guidance](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget) says it only wants to crawl high-quality content.

So prioritize content quality over making frequent, irrelevant changes in an attempt to boost crawl frequency.

### Crawl Capacity Limit

The crawl capacity limit prevents Google’s bots from slowing down your website with too many requests, which can cause performance issues.

It’s primarily affected by your site’s overall health and Google’s own crawling limits.

#### Your Site’s Crawl Health

How fast your website responds to Google’s requests can affect your crawl budget.

If your site responds quickly, your crawl capacity limit can increase. And Google may crawl your pages faster.

But if your site slows down, your crawl capacity limit may decrease.

If your site responds with server errors, this can also reduce the limit. And Google may crawl your website less often.

#### Google’s Crawling Limits

Google doesn’t have unlimited resources to spend crawling websites. That’s why there are crawl budgets in the first place.

Basically, it’s a way for Google to prioritize which pages to crawl most often.

If Google’s resources are limited for one reason or another, this can affect your website’s crawl capacity limit.

## How to Check Your Crawl Activity

[Google Search Console](https://www.semrush.com/blog/google-search-console/) (GSC) provides complete information about how Google crawls your website. Along with any issues there may be and any major changes in crawling behavior over time.

This can help you understand if there may be issues impacting your crawl budget that you can fix.

To find this information, access your GSC property and click “**Settings**.”

![Google Search Console home with the left-hand side menu highlighted and "Settings" clicked.](https://static.semrush.com/blog/uploads/media/c1/7e/c17e0dcb29cf012251df029c39d30944/e5857761b427f1636563215b7b6e65d2/AD_4nXeG_8u2vUNZlPretVpZI_7d-2r79MV0emEfOZTRV-Tjdt--4FuUhEoHzmIvuZtEj4H9AyKHl5b8JQifMltV1xsOOWjhzTUv7O0586mtww6mjli4z17Q7zDwck5K5wohOLamXsgTgeCbl47HoFYHH2efRns.jpeg)

In the “Crawling” section, you’ll see the number of crawl requests in the past 90 days.

Click “**Open Report**” to get more detailed insights.

![Settings on Google Search Console with the "Crawling" section highlighted and "Open Report" clicked.](https://static.semrush.com/blog/uploads/media/4e/4c/4e4ca154c9b59349cb9625b8d966f134/86aeb9b46fd57f6194a0eb2bb268b38f/AD_4nXebD1oNQS-y5m9MqSyPvMWsrfFCC2im4pNx8_5bwoo2f0AuUGtYZqOXMqPivJzDHWyqwrn7ZvJuuEs-wYiNKv9GIOc_yzFZz5RAvLuK3h3J1J4dtLGSAykpHn5LQdfi-9YWPqBvB1FGC2CtYy2B5ygUuoss.jpeg)

The “Crawl stats” page shows you various widgets with data:

### Over-Time Charts

At the top, there’s a chart of crawl requests Google has made to your site in the past 90 days.

!["Crawl stats" on Google Search Console showing a chart of crawl requests Google has made to a site in the past 90 days.](https://static.semrush.com/blog/uploads/media/a3/3e/a33e9daa6a725714aaaf0a52ec677f0c/8c38f15091eef4be95490fffe5d4f7a0/AD_4nXeBgGUybUa1Ic9_HpjeivFzLWT2jIHK0_a_iLSOUSXw2H1Y6iOuj6Y6AoJEjcGYT0io4GLJRjQnQYjm2qHq1Fkm0ZowrXCLUKhrkbTLnJEbS39d0BD-YR3D6J-7fa7kLnVuOWT9OQB0vlJxKMhF3AG-Ox0i.jpeg)

Here’s what each box at the top means:

- **Total crawl requests**: The number of crawl requests Google made in the past 90 days
- **Total download size**: The total amount of data Google’s crawlers downloaded when accessing your website over a specific period
- **Average response time**: The average amount of time it took for your website’s server to respond to a request from the crawler (in milliseconds)

### Host Status

Host status shows how easily Google can crawl your site.

For example, if your site wasn’t always able to meet Google’s crawl demands, you might see the message “Host had problems in the past.”

If there are any problems, you can see more details by clicking this box.

![Host status on Google Search Console showing "Host had problems last week".](https://static.semrush.com/blog/uploads/media/aa/28/aa2819719d67737bdb9e72e4c2253531/b12a97004303c5682409e3c57ef29cc9/AD_4nXcrRs-oN_IJR9xeQefURQQ_KQwpxL_mqDZEoYEzt-8LLPd7JHSwlH9c4nExCU73Q9mj_JyyrskqwD4zomhvPsUFoqn5GH-oU8yp34rnYeP606T037CUNrXzT_y3qe1teNNCL2yM35N9EYe6e_dMGTXGr7Hg.jpeg)

Under “Details” you’ll find more information about why the issues occurred.

![Crawl stats report showing a chart with failed crawled requests and a pop-up with information on why the issues occurred.](https://static.semrush.com/blog/uploads/media/59/aa/59aabf3087b8fbc4e5cfcc1f03355f2f/25d1e2027603375334a241e5a34b6ff2/AD_4nXfR8eLsOkjF4gcedv1FEuOJfGZUjUNLD9kpiErqac7O_g2O3ApEIk03GJR3_e_nAI4hJBug1Eaivw8M9iCbjMLD-lSb8m_W1HyuPJmNihfjpQGWtchu4Lop7uE_ZGHVBoPUzFWnJD-mSXGXnGaRG6pLU-4y.jpeg)

This will show you if there are any issues with:

- Fetching your robots.txt file
- Your domain name system (DNS)
- Server connectivity

### Crawl Requests Breakdown

This section of the report provides information on crawl requests and groups them according to:

- **Response** (e.g., “OK (200)” or “Not found (404)”
- **URL file type** (e.g., HTML or image)
- **Purpose of the request** (“Discovery” for a new page or “Refresh” for an existing page)
- **Googlebot type** (e.g., smartphone or desktop)

![Crawl requests breakdown grouped by response, file type, purpose, and by Googlebot type.](https://static.semrush.com/blog/uploads/media/07/99/0799d6d612b7f67d0ba8f5188e2830db/c470364b9d34c7e0c9d46d10c4b475bf/AD_4nXeg2CvyJDfGmGaoRr6RSY6TGnPD602HZ8QZRiNzcxZosIGndZlOt4J8vNP3EvNAkC8sNBlreE6lBDIoXbvnjNHtaB7beTgc4lpjTwIoMSC9x4Hp75zoqUnV6AwAyeni-Av6FrzoJlvy0iOVRwUbM-0IUQc.jpeg)

Clicking on any of the items in each widget will show you more details. Such as the pages that returned a specific status code.

![List of pages that returned "Not found (404) on the Crawl Stats report in Google Search Console.](https://static.semrush.com/blog/uploads/media/0c/45/0c45b02eb57fd3f68cc4085a51eb3b57/0fb0e842597e020b80961fa25812b875/AD_4nXeNpHy6KO6aOkSWW2cwq1eWKSXyEq9qUx9VnfIPoFqsKeZwUi5CksiaD3tXI8CzkfLR7BBLwlEIh8o5qzygqYeNDo-xkFrtH3aSdcVR7ErJtmefJYGKltp5mGjAWB938fMGC21IApmjjcj1uOPUH04sUbw.jpeg)

Google Search Console can provide useful information about your crawl budget straight from the source. But other tools can provide more detailed insights you need to improve your website’s [crawlability](https://www.semrush.com/blog/what-are-crawlability-and-indexability-of-a-website/).

## How to Analyze Your Website’s Crawlability

Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool shows you where your crawl budget is being wasted and can help you optimize your website for crawling.

Here’s how to get started:

Open the [Site Audit](https://www.semrush.com/siteaudit/) tool. If this is your first audit, you’ll need to create a new project.

Just enter your domain, give the project a name, and click “**Create project**.”

!["Create project" window on Semrush with a domain entered and the "Create project" button clicked.](https://static.semrush.com/blog/uploads/media/22/d3/22d3161f925425b89c4a4e0f274d4226/ccdb2919e8d57f34a64846d919e3a07b/AD_4nXcG7CdzwUWpYNO1YpWlmRUrYy1UE-e32nGSRkR8cNwm-RbivbMT9uQMUJuc7RpRBQlqOnzkS_QQchdWyEEDBhGfIWj5i3zVuIDJrwd1ATya-d710Z4ZHm5_grDgnpO6NhSzerFPMy8S08uhu6zmY7e4Yrak.jpeg)

Next, select the number of pages to check and the crawl source.

If you want the tool to crawl your website directly, select “**Website**” as the crawl source. Alternatively, you can upload a sitemap or a file of URLs.

![Basic settings page on Site Audit to set crawl scope, source, and limit of checked pages.](https://static.semrush.com/blog/uploads/media/f2/1c/f21c9f30b58147b6d25b45651316d34e/44e51942412ac11593321aa7c80ec996/AD_4nXeBusrOrW2ulLFqEWTpLAUkhX51NJfUKIWzyejmaSyiOAwpLH86NMbhVFFfKdtNzNyVEcUYZFKLMpWpOVh1vnDqozT1U2BqUdmSiz8EmPYFs4ecUbOZ2wOfFzvPIF-W0BTHuUIF6VdlamKTPExsAg7unLU.jpeg)

In the “Crawler settings” tab, use the drop-down to select a user agent. Choose between GoogleBot and SiteAuditBot. And mobile and desktop versions of each.

Then select your crawl-delay settings. The “Minimum delay between pages” option is usually recommended—it’s the fastest way to audit your site.

Finally, decide if you want to enable JavaScript (JS) rendering. JavaScript rendering allows the crawler to see the same content your site visitors do.

This provides more accurate results but can take longer to complete.

Then, click “**Allow-disallow URLs**.”

![Crawler settings page on Site Audit to set user agent, crawl delay, and JS rendering.](https://static.semrush.com/blog/uploads/media/54/4d/544db6a656b064d70743369a030146c9/87378fa03d9fb5aa69f47b6b01c0d32e/AD_4nXedBKVl3w8fU5k1OnkY_GS_mdZ2Zn5FgAMvgyovWwCoWufoM7eJxOljVSUQ_mpaVAGTPKm-RQgYzpBGrmWXn3oQ_3sGUwoIxOoSzt9iAgJCebHPATmqIZQOsHHgxnis9MFelNqWqP11gLVhXXszVCmv2rC-.jpeg)

If you want the crawler to only check certain URLs, you can enter them here. You can also disallow URLs to instruct the crawler to ignore them.

![Allow/disallow URLs settings page on Site Audit to set masks for specific URLs.](https://static.semrush.com/blog/uploads/media/42/eb/42ebde912cd57c54c4ca2eb3f56a2cce/4ef05c49a9a29d591a8bcd8a7bb3a567/AD_4nXc5xEPCtF1_2tkNbSDDjdkUlzoPzrKY50iIjZTxtxAc8_AoHQPGgHl84_XmqDZxqx4nSl0s5DXAsIV90d8DO9KD-EHORwKZOeJLhg-DGD9ipWxHL94FpDZd11yxdJfnaVf3YY5bJa29bfrrxY1j4rdBHOtK.jpeg)

Next, list [URL parameters](https://www.semrush.com/blog/url-parameters/) to tell the bots to ignore variations of the same page.

![Remove URL parameters settings page on Site Audit to list URL parameters to ignore during a crawl.](https://static.semrush.com/blog/uploads/media/f6/55/f655ec3a0396fc14643904ea30a74a15/bf519038f56c956ea838e271773fae7d/AD_4nXdD1iY79BiyfPaFKZH706Gox5aCyJJbgaar3RMRY2piNLOeVvG8yzzsx7R_7UyL3_14PoYUQPMAyxnqHp8hCZA8dYYFDJsjioYAMCcapTxgXGwdpvz_1rcPR2lcnvxoBNPiOtl90U7zumdlcQyh1UvQhAwJ.jpeg)

If your website is still under development, you can use “Bypass website restrictions” settings to run an audit.

![Bypass website restrictions settings page on Site Audit to bypass disallow in robots.text or crawl with your credentials.](https://static.semrush.com/blog/uploads/media/4e/62/4e6225d01edf4f1b8b9b114fe1cf6760/1039151c89cc89f7c52e55373e573e19/AD_4nXdu1L_9Q5CQMS6XOWh8Fe-xBMafaXGG6OmC1IMEigjUhI5DGWHXL2FDCJSoTa0m5he_l5sV3GAgcLspYfbPL8FSV9UHsMWC2XWo78RoXjWOTz5_38ayl9bzTef15maqbePMcMIN5J6XYcV5mO1LA674Slg.jpeg)

Finally, schedule how often you want the tool to audit your website. Regular audits are a good idea to keep an eye on your website’s health. And flag any crawlability issues early on.

Check the box to be notified via email once the audit is complete.

When you’re ready, click “**Start f**.”

![Scheduling settings page on Site Audit to set crawl frequency along with the "Start Site Audit" button highlighted.](https://static.semrush.com/blog/uploads/media/3c/4e/3c4eee57cdac00f21ac831c09db2e092/a67b97345d58abfcb4b9f73efbc36c48/AD_4nXfT0r-Mt-ZyLQoQVkdzOk8yBQFECVKxC6-A-crKmDbAukmp-WcDt8Oqo38lWw3NhyMSEqtVMTTSwZecLzgDhJZ9aqlT5PNv4CuiSYi-qT6HhvOcxQ4Fmf_SenX39AsJoLFyMKEA-mZ9bkHWm4n3n_A4s3g.jpeg)

The Site Audit “Overview” report summarizes all the data the bots collected during the crawl. And gives you valuable information about your website’s overall health.

The “Crawled Pages” widget tells you how many pages the tool crawled. And gives a breakdown of how many pages are healthy and how many have issues.

To get more in-depth insights, navigate to the “Crawlability” section and click “**View details**.”

![Site Audit Overview report with the "Crawled Pages" widget and "Crawlability" section highlighted.](https://static.semrush.com/blog/uploads/media/a8/d7/a8d7508b9943502e5dc6dc5f750704af/0d1aaa8c700ca7f6637e07b0f7627d72/AD_4nXcBev7KWX9sQs3624jGGzrj0dWdD3NsPc1w8jRo72dJnFwL8W5HHI9NWLRiGaC5jIfMYtNJsZ5vDTjEULg8lONOdFx97t6YP_7WFGrcPQucbba_fMUWBX3rAivQFBMBz5tvGr6nQ2XtqzEawfumNsHMR2It.jpeg)

Here, you’ll find how much of your site’s crawl budget was wasted and what issues got in the way. Such as temporary redirects, permanent redirects, duplicate content, and slow load speed.

Clicking any of the bars will show you a list of the pages with that issue.

![Crawlability report on Site Audit with the "Crawl Budget Waste" widget highlighted.](https://static.semrush.com/blog/uploads/media/b2/22/b222b405cd3384dc365394d8f71fff28/2077f3efd7217a72d5c728714e710617/AD_4nXfxFU9XnXw2EtePfHsNH4Pm6hg8eHNpVYzXclRStpMo_WNJD7UcceY_xr4CMCGpLF_GcEDaYt6S5Lq-E6vmp0wrhLf_DDIdjGB3jyHtLYTjF4u7OHRlde4g0oilRaXg9xl6rFEDDYqzL8VAKXBUpIkTZpyk.jpeg)

Depending on the issue, you’ll see information in various columns for each affected page.

![Crawled pages on Site Audit showing information like unique pageviews, crawl depth, issues, HTTP code, etc. for each page.](https://static.semrush.com/blog/uploads/media/e1/47/e1473ff2eda02a4fb5ccc95b7ac9c239/e76c33b2098500230b01f983c23c8ce7/AD_4nXeuJTXiKxjYxIuXNZ9Zad_eKxLwAytKqXfWBtcoV_sI-5bQC7hcV2PlkagEDzr_UPVVNPcGZZJfZFD0pdZp4EhmJXBDLbTujmueBrlQ5Vn8EAn_JjwzPbkRPc9SIDwCod8QmCKMt_AZlP4lEHRZiiG32Y8.jpeg)

Go through these pages and fix the corresponding issues. To improve your site’s crawlability.

## 7 Tips for Crawl Budget Optimization

Once you know where your site’s crawl budget issues are, you can fix them to maximize your crawl efficiency.

Here are some of the main things you can do:

### 1. Improve Your Site Speed

Improving your [site speed](https://www.semrush.com/blog/page-speed/) can help Google crawl your site faster. Which can lead to better use of your site’s crawl budget. Plus, it’s good for the [user experience (UX) and SEO](https://www.semrush.com/blog/ux-and-seo/).

To check how fast your pages load, head back to the Site Audit project you set up earlier and click “**View details**” in the “Site Performance” box.

![Site Audit overview with the "Site Performance" box highlighted and "View details" clicked.](https://static.semrush.com/blog/uploads/media/03/c4/03c42220ba8a75f89783727a03b6ab15/b02fce6c5549cfafd02c027f0f906d5d/AD_4nXdlg1rezrHs0nVHF0ShUYZk-dStem01pny9-rQszJUjihUkTmohVmgHWyVYJ9cVp9YWj8cAkLCN0svUSp-zJTFKGo3sU7-vI-TRNdWOsb3fUJMfx_jLmo0SAiJOozuMVq2fv2HrHjRgawFg55uQ0oFdPP6a.jpeg)

You’ll see a breakdown of how fast your pages load and your average page load speed. Along with a list of errors and warnings that may be leading to poor performance.

![Site Performance Report breaking down load speed by page and performance issues like page size, uncompressed pages, etc.](https://static.semrush.com/blog/uploads/media/63/a6/63a6c95ddcfe860d588e286309d65cc7/29d096481bb4cefcae81da4f7f53606d/AD_4nXd97qUX56AwsQoQo72qyIEhtzT7q5HFLpAivEcMSWP9g3qqFNqmRg7LqN1SpKWpyvH6YVZddJrvjPmv-vTz_dNAyT0zTV8dSkG1Pk4blCoFx1SixD-B6D1v9Af7iUIGQHhwxxGKOXqu4Fc0PD6SPy55PaPM.jpeg)

There are many ways to improve your page speed, including:

- [**Optimizing your images**](https://www.semrush.com/blog/image-seo/): Use online tools like [Image Compressor](https://imagecompressor.com/) to reduce file sizes without making your images blurry
- **Minimizing your code and scripts**: Consider using an online tool like [Minifier.org](https://www.minifier.org/) or a WordPress plugin like [WP Rocket](https://wp-rocket.me/) to minify your website’s code for faster loading
- **Using a content delivery network (CDN)**: A [CDN](https://www.semrush.com/blog/content-delivery-networks/) is a distributed network of servers that delivers web content to users based on their location for faster load speeds

### 2. Use Strategic Internal Linking

A smart [internal linking](https://www.semrush.com/blog/internal-links/) structure can make it easier for search engine crawlers to find and understand your content. Which can make for more efficient use of your crawl budget and increase your ranking potential.

Imagine your website a hierarchy, with the homepage at the top. Which then branches off into different categories and subcategories.

Each branch should lead to more detailed pages or posts related to the category they fall under.

This creates a clear and logical structure for your website that’s easy for users and search engines to navigate.

![Website architecture example has a few category pages that each branch into subcategory pages. These then branch into individual pages.](https://static.semrush.com/blog/uploads/media/1a/a8/1aa8c891f7ca096c41d87ce207e9f31a/978bc24f8629197948f9199fa0cc5a8e/AD_4nXedpZa_eFgXtIQs8k5aSWRi-FS9TsGkaZobAEpvuVRk8JPADABFo_8t85kLQ_8VTRMERReIcGC4rHic7HOd9ZoRtcxkid2TImqG2FanmAOxqeU0JTwMvmweEogBpCOvhFxFTLbmUgMKJXA13eF2Q19bEfN-.png)

Add internal links to all important pages to make it easier for Google to find your most important content.

This also helps you avoid [orphaned pages](https://www.semrush.com/blog/orphan-pages/)—pages with no internal links pointing to them. Google can still find these pages, but it’s much easier if you have relevant internal links pointing to them.

Click “**View details**” in the "Internal Linking” box of your [Site Audit](https://www.semrush.com/siteaudit/) project to find issues with your internal linking.

![Site Audit Overview with the "Internal Linking" score section highlighted and "View details" clicked.](https://static.semrush.com/blog/uploads/media/91/8e/918e1b610fcde815b5501cfffeb5f750/48c4c8e0eb19d355a4c0ea6a612256dc/AD_4nXcFS4KWvtg6KTRbbpIENOGJK55MmIzca9Xe2ulFEwJbN8KrGH30W3TgepwF-YC6RAAnL5TUOkwLFkHRlhzUkHUotnNFElskKRzKE0_touqUseEBZoG_HmkGK5PWLiSkTXZP66tm3LiTtNbKyqug9WGs4x0.jpeg)

You’ll see an overview of your site’s internal linking structure. Including how many clicks it takes to get to each of your pages from your homepage.

!["Page Crawl Depth" widget showing how many clicks it takes to get to each page from a site's homepage.](https://static.semrush.com/blog/uploads/media/eb/11/eb11c0560a7ef07a9e34006a7da02e89/4da02893311fa1dbb9ea3a494c5f1e65/AD_4nXfe9sqb7yxrPtiQgbLFUa6lg4gLAqwUG0Bsme5awwE9TMcSZNbidcJRBBt_Bcpxpi0LaBGn5QJsZk5b664DcooGNiPqDXMdvyreuuN1cEKkBWFe-k01uBCBQNa4ODMURWSsK1D7M1g27QNTYtSYlIDjJR4.jpeg)

You’ll also see a list of errors, warnings, and notices. These cover issues like [broken links](https://www.semrush.com/blog/broken-link/), nofollow attributes on internal links, and links with no anchor text.

![Errors, warnings, and notices on Internal Link issues including broken links, nofollow attributes, links without anchor text, etc.](https://static.semrush.com/blog/uploads/media/11/8a/118a451de3dac8146b8e2c68102b654c/cd044041bd2a35cb544351c467258c10/AD_4nXd5UMHZNj7QPaQVWm9EsD558ZW8EBKo0eSgG_hZh0z5m49OI28LX8NcDSyvfAa7AuZ6R-QEcqyGRU2T-xTjAbvODY0HEzORgnJsHztriO_u4GkBd_cLhmh885i2Rt9PqTJVAREPtWFc2ZoHro8V6pwaUxcc.jpeg)

Go through these and rectify the issues on each page. To make it easier for search engines to crawl and index your content.

### 3. Keep Your Sitemap Up to Date

Having an up-to-date XML [sitemap](https://www.semrush.com/blog/website-sitemap/) is another way you can point Google toward your most important pages. And updating your sitemap when you add new pages can make them more likely to be crawled (but that’s not guaranteed).

Your sitemap might look something like this (it can vary depending on how you generate it):

![Example of an XML sitemap which includes list of indexed URLs, a “lastmod” attribute, a "hreflang" attribute, etc.](https://static.semrush.com/blog/uploads/media/60/80/60807dd158fed67c12050c6de0c16ccc/109061eed1ca864f5c1779455df9118f/AD_4nXfau0biDOqcuo0_cGvcXOzlVnLesHah7xaUUMp62ddca9UmAfajkqDfPuK5vzQwUXuGwclCOlcPfgAR7Kj91pNruS5KC24IEBS50LsbYplAnxW433BXoOZdqFJyR0bd5D5e70gUJl7RNAXidBFr7DK__ZcM.jpeg)

[Google recommends](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget) only including URLs that you want to appear in search results in your sitemap. To avoid potentially wasting crawl budget (see the next tip for more on that).

You can also use the <lastmod> tag to indicate when you last updated a given URL. But it’s not necessary.

***Further reading****:* [*How to Submit a Sitemap to Google*](https://www.semrush.com/blog/submit-sitemap-to-google/)

### 4. Block URLs You Don’t Want Search Engines to Crawl

Use your robots.txt file (a file that tells search engine bots which pages should and shouldn’t be crawled) to minimize the chances of Google crawling pages you don’t want it to. This can help reduce crawl budget waste.

Why would you want to prevent crawling for some pages?

Because some are unimportant or private. And you probably don’t want search engines to crawl these pages and waste their resources.

Here’s an example of what a robots.txt file might look like:

![Example of robots.text file showing which pages to allow and disallow crawling on.](https://static.semrush.com/blog/uploads/media/cf/7b/cf7b90ba5901a78cc6da6d5af38efe85/f5ea54dc711a4e3cb38ec63531f45e1f/AD_4nXd_n9wd0fVXLBFPxqr0Tt9TSEj-maZOX8UeLmWNztsxzoiEln-GHAwNzMcinm23zvRhf7ITXwafGf98g18dChpuEN5OpTFqPs1FcnRMlXpiTYnsmOtIJ_bYFtLd2MLcEBQR3Fz7cs-zbZ4RaK8GVK7gGxI_.jpeg)

All pages after “Disallow:” specify the pages you don’t want search engines to crawl.

For more on how to create and use these files properly, check out our [guide to robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/).

### 5. Remove Unnecessary Redirects

Redirects take users (and bots) from one URL to another. And can slow down page load times and waste crawl budget.

This can be particularly problematic if you have redirect chains. These occur when you have more than one redirect between the original URL and the final URL.

Like this:

![How a redirect chain works with redirects from URL A to B to C.](https://static.semrush.com/blog/uploads/media/9a/fd/9afd87c3fd7778cea7d0b2c6a8759246/ffa0991466fdb2f8f05a21e8418e9f93/AD_4nXdO-KfF2-gxe0Yagrmw4-5_0e6LHQGIf8ZaSvzsDLn4GSip4mbn5U0OCQpEslBN1usurNaVgU4fOezT4JSTxqcdJ3CIrd_71U5TBINbroeuc4lNdNEWYTURYomT5c_lWUsUKvvV81nT8Zup5sOrfCxrEFs.png)

To learn more about the redirects set up on your site, open the [Site Audit](https://www.semrush.com/siteaudit/) tool and navigate to the “**Issues**” tab.

Enter “redirect” in the search bar to see issues related to your site’s redirects.

![Issues tab on Site Audit with "redirect" entered in the search bar and redirect chains and loops errors highlighted.](https://static.semrush.com/blog/uploads/media/29/02/290297c2e73683949ddcd60e2148d232/a332f3acc294f9f62680e728643f6964/AD_4nXfBsFo77Exosogb75YQtNljNv0IomBZgtT8-GN3wPNjQI41-1hVe-FSeA4bQ-AEpwFKFRs8U51xNSQYw5SOkvGFwRvyR50VfLKHBWhqQdKC4T7S46EHt9Sqb12k3QWVWviFWiS2E1U4goj33Lu__30fame2.png)

Click “**Why and how to fix it**” or “**Learn more**” to get more information about each issue. And to see guidance on how to fix it.

![Pop-up box with more information on redirect chains and loops issues and how to fix it.](https://static.semrush.com/blog/uploads/media/ca/a7/caa7d934ed1a5113645f6b0d8f808db2/ae1c1651ad7f8c8cae45ea69247d4fa7/AD_4nXfCe48-kCw6GrIDMwm_SV-a3-Wo7-6SEnyyk3UyUk2JK2omVsf-6ZtRxOkHrMM8UOd5kMwUMAErgiuCO1riu9BoMnbzFNNC3PdTzFgBmCfbvnbj4HkZDOXc3U2luRAxmWtZBf5dbRdvuLXfTAUAXRJ-iA54.jpeg)

### 6. Fix Broken Links

Broken links are those that don’t lead to live pages—they usually return a [404 error code](https://www.semrush.com/blog/what-does-error-404-not-found-mean/) instead.

This isn’t necessarily a bad thing. In fact, pages that don’t exist should typically return a 404 status code.

But having lots of links pointing to broken pages that don’t exist wastes crawl budget. Because bots may still try to crawl it, even though there is nothing of value on the page. And it’s frustrating for users who follow those links.

To identify broken links on your site, go to the “**Issues**” tab in [Site Audit](https://www.semrush.com/siteaudit/) and enter “broken” in the search bar.

Look for the “# internal links are broken” error. If you see it, click the blue link over the number to see more details.

![Issues tab on Site Audit with "broken" entered in the search bar and broken internal link errors highlighted.](https://static.semrush.com/blog/uploads/media/8d/fb/8dfb22e44c9ef0b8997838b4de863bc5/373f492c6bfdd0b9be6891d56b5d2565/AD_4nXeec4chDxJ0SUSWgX-7KCfFXZOcncB3hxN7zAlrbVvYDUYPiuC6v4_xGSaOe7VRnaxaeeV6Bbd3ihwOp0WhsxYWCikcGPK087R0tkNggb5EZU_Desgrzj05LAnmtNnnsiQomiaK67ULHg70DMm18vA7Z95z.jpeg)

You’ll then see a list of your pages with broken links. Along with the specific link on each page that’s broken.

![Pages with broken internal links on Site Audit with columns for the page URL, broken link URL, and HTTP code.](https://static.semrush.com/blog/uploads/media/3e/ab/3eab666427f2d0a0023bc5486c87d49b/64e22230e6304c27facc540089b9d4cb/AD_4nXf8OK9_FzaOaedicB9dui0oSY2jecMyBiWdX3wyZ_xV9pcxmVFLcbgivUOBqAeSwU5ifmDCEJcRpbDlBfJ5xs3MOKfwe_FBWKYb5jwMBoQhr7s7KZMJnQQ57Q6DIAgf6MxDgwIPXB6S_y5FZF1oI-o6GXQ.jpeg)

Go through these pages and fix the broken links to improve your site’s crawlability.

### 7. Eliminate Duplicate Content

[Duplicate content](https://www.semrush.com/blog/duplicate-content/) is when you have highly similar pages on your site. And this issue can waste crawl budget because bots are essentially crawling multiple versions of the same page.

Duplicate content can come in a few forms. Such as identical or nearly identical pages (you generally want to avoid this). Or variations of pages caused by [URL parameters](https://www.semrush.com/blog/url-parameters/) (common on ecommerce websites).

Go to the “**Issues**” tab within [Site Audit](https://www.semrush.com/siteaudit/) to see whether there are any duplicate content problems on your website.

![Issues tab on Site Audit with "duplicate" entered in the search bar and duplicate content errors highlighted.](https://static.semrush.com/blog/uploads/media/51/30/513067e394cb112ec6b41e9e3ca9f23f/a86519ecb15632185b445920c1965a79/AD_4nXeuVackMlbPg2Vhs4JaezPWZeFSdEmMPxuoGxLqnyjkFM-SWVyuFWAOoR7GxBZwmQIsaGvlvtYgsTRLyC4Cj9chWWXlX04t69Pzg572fXOqpkleLJT-eJaW71LGtjtR5fr5sj02WdSSEO8Hq6St__07mpaB.jpeg)

If there are, consider these options:

- Use [“rel=canonical” tags](https://www.semrush.com/blog/canonical-url-guide/) in the HTML code to tell Google which page you want to turn up in search results
- Choose one page to serve as the main page (make sure to add anything the extras include that’s missing in the main one). Then, use [301 redirects](https://www.semrush.com/blog/301-redirects/) to redirect the duplicates.

## Maximize Your Crawl Budget with Regular Site Audits

Regularly monitoring and optimizing technical aspects of your site helps web crawlers find your content.

And since search engines need to find your content in order to rank it in search results, this is critical.

Run a free [website audit](https://www.semrush.com/siteaudit/) to measure your site's health and spot errors before they cause performance issues.
