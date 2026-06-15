---
title: "How to Find & Fix ChatGPT 404 Referrals"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "fix-chatgpt-404-referrals"
url: "https://www.semrush.com/blog/fix-chatgpt-404-referrals/"
canonical: "https://www.semrush.com/blog/fix-chatgpt-404-referrals/"
author: "Cecilia Meis"
published: "2025-10-24T11:04:00+00:00"
updated: "2025-10-24T11:04:00+00:00"
categories:
  - "AI"
freshness_reasons:
  - "ai_search_topic"
schema_genre: "AI"
fetched_at: "2026-06-12T15:23:16+00:00"
status_code: 200
html_hash: "bb602092dbe2f22b5be8007123b5720c22e83fff9afb6c72c64cc9d12983e203"
clean_word_count: 2011
clean_char_count: 13370
---
# How to Find & Fix ChatGPT 404 Referrals

A case study documented on LinkedIn found that over 3% of visitors from ChatGPT landed on a 404 page instead of real content. These “phantom URLs” waste valuable clicks, damage user trust, and can affect SEO.

The fix? Audit your analytics, patch phantom links, and optimize your 404 page so lost visitors still convert. This guide walks you through the process step by step.

## Why Does ChatGPT Create 404 Referrals?

[ChatGPT](https://www.semrush.com/blog/what-is-chatgpt/) doesn’t crawl the web like a search engine. The model predicts patterns based on training data rather than pulling live, verified links. Because of that, it sometimes generates “hallucinated” links that look real but don’t exist.

Phantom URLs cause problems for site owners, including:

- **Lost traffic**: Users who click a broken link often leave
- **Eroded trust**: Visitors may blame your brand, not the AI
- **SEO risks**: Search engines can treat excessive redirects or soft-404s as poor site quality
- **Missed opportunities**: Each phantom click is a lost potential customer

Google’s John Mueller has [cautioned](https://www.searchenginejournal.com/googles-mueller-predicts-hallucinated-links-redirect-or-not/542312/) that hallucinated links may spike for months before leveling off.

***Further reading****:* [*What Is a 404 Error? How It Affects SEO & How to Fix It*](https://www.semrush.com/blog/404-error/)

## Are AI Referrals Worth Optimizing For?

Dan Hinckley, co-founder of Go Fish Digital, [analyzed](https://www.linkedin.com/posts/danielhinckley_seo-insight-chatgpt-can-hallucinate-urls-activity-7335716571698393091-Zb8A/) 18,000+ landing pages ChatGPT sent traffic to. About 3.35% returned a 404 page.

But it gets worse.

Alex Galinos, an international SEO expert, [found](https://www.linkedin.com/posts/alexgalinos_seo-searchengineoptimization-searchengineoptimisation-activity-7336374801420185600-W1iw/) an even higher number: 57% of one client’s ChatGPT referrals landed on 404s.

These numbers represent new customers who are lost before they ever see your content.

So yes, AI referrals are worth addressing.

Here’s how to find them.

## How to Identify Phantom URLs in Google Analytics 4

To find ChatGPT-generated 404s, open [GA4](https://analytics.google.com/) and go to **Reports → Life cycle → Engagement → Pages and screens**. This report shows the pages users visit on your site.

![Open Pages and Screens report in GA4 with arrows pointing to navigation steps](https://static.semrush.com/blog/uploads/media/6f/e0/6fe0b464ae4477e10113960ec002f23f/6c18895c5127839ca503bdd083322faf/image.png)

Inside the report, set the primary dimension to **Page title and screen class**. This groups pages by their titles.

![Dropdown showing Page title and screen class highlighted as primary dimension](https://static.semrush.com/blog/uploads/media/dd/22/dd224344b8c2cdd5a4e87ad55a8ef891/3fc8e145bbbc5561c67677d3f677fd6d/image.png)

Next, add a secondary dimension by clicking the “+” icon and selecting **Session source / medium** under **Traffic source** → **Cross-channel**.

![Add secondary dimension menu with Traffic source and Session source/medium highlighted](https://static.semrush.com/blog/uploads/media/2d/1e/2d1e6e6c42957fcff27432aa0ac5a8af/feaa02b55dd027a1acef561b95bf9d0a/image.png)

In the search bar above the table, insert **chatgpt.com / referral**. GA4 will now only display visits referred by ChatGPT.

If your 404 page is titled “Page Not Found,” it will appear in the table alongside ChatGPT as the referral source.

This confirms whether ChatGPT traffic is hitting broken or phantom URLs.

![Report showing Page Not Found from chatgpt.com referral highlighted in table](https://static.semrush.com/blog/uploads/media/29/6f/296fca0ca68ed4149890e76430e90841/b735a513cbf07f21aff30ca1a949ca0b/image.png)

Save this report to avoid rebuilding it every time. Click the pencil icon in the top-right corner.

![Arrow pointing to Customize report button in GA4 toolbar](https://static.semrush.com/blog/uploads/media/7b/e5/7be5d47aedf9a710be9a610578124224/4007f323b1ef67131f87980cb9bbb058/image.png)

In the right sidebar, add a filter for **Session source / medium**. Set it to **Exactly matches**, then insert **chatgpt.com / referral**, and click “**Apply**.”

![Build filter panel with Session source/medium equals chatgpt.com referral and Apply highlighted](https://static.semrush.com/blog/uploads/media/15/7d/157d14a927b179a7aa24b19400255c86/dbe0e5f1e14cf4a4933a8372eddb1455/image.png)

Click “**Save**,” then “**Save as a new report**” with a clear name like ChatGPT Referrals or ChatGPT Landing Pages.

![Save menu with Save as a new report option highlighted in GA4.](https://static.semrush.com/blog/uploads/media/b3/f3/b3f32d7f20c9e6b45b033f6906a77c16/2fdf803bd286c47542d6faee8f1365bf/image.png)

Finally, go to **Library** at the bottom of the Reports panel. In the Life cycle collection, drag your new report into the Engagement folder and click “**Save**.”

![Customize collection screen with ChatGPT Landing Pages added and Save button highlighted.](https://static.semrush.com/blog/uploads/media/d9/7f/d97ff5419a1290fcc9ec22ff1664563c/430af4f042d6a9c240bb1ce0426292ea/image.png)

From now on, you’ll have a dedicated ChatGPT referral report in your GA4 sidebar. Each time you open it, you’ll see ChatGPT traffic, which pages users landed on, and whether those visits resulted in 404 errors.

## Should You Redirect or Leave the 404 Page?

Google [may treat](https://www.searchenginejournal.com/googles-martin-splitt-warns-against-redirecting-404s-to-homepage/541549/) bulk redirects to irrelevant pages (like the homepage) as soft 404s. Soft 404s waste crawl efficiency (how easily bots can crawl and index your site) and dilute site quality.

For larger sites with thousands of URLs, this inefficiency can compound. If AI referrals generate hundreds of phantom URLs, bots may crawl dead ends instead of your most important pages.

Use this simple decision framework for handling phantom URLs:

- **Redirect when the page (or a close match) exists.** Example: “/blog/chatgpt-integrations” doesn’t exist, but you have a live post on ChatGPT SEO tools. Redirecting helps users find relevant content and preserves [link equity](https://www.semrush.com/blog/internal-linking-mistakes/) (more on that below).
- **Redirect when the page has backlinks pointing to it.** Even if you don’t plan to build the page, backlinks passing authority to a 404 are wasted equity. Redirect those URLs to the most relevant live page to preserve [site authority](https://www.semrush.com/blog/semrush-authority-score-explained/).
- **Create (or recreate) the content if the phantom URL suggests real demand.** If GA4 shows steady traffic to a phantom page, it might be worth building the page. This turns phantom clicks into new content and engagement opportunities.
- **Leave it as a 404 if the URL is irrelevant or low quality.** Example: “/features/data-dashboard” was never a real page and has no backlinks. Redirecting it would only confuse users and send weak signals to Google. A clean 404 is the better choice.

![Decision tree showing when to redirect a phantom URL, when to recreate content, when to leave it as a 404, and when to redirect because backlinks point to the page.](https://static.semrush.com/blog/uploads/media/f9/1b/f91b4b66eb0156694c7a16a4456d5636/d1161dfee94b36fc43a31c7a4a360080/image.png)

Let’s break down how to understand this using real data.

### How to Use Semrush to Prioritize Phantom URL Fixes

GA4 shows which ChatGPT links sent traffic, but Semrush shows why those pages broke and how to fix them without harming SEO.

For example, imagine you’ve built your ChatGPT referral report in GA4 and spot three key referrals:

1. **/pricing** received 150 visits and worked normally
2. **/blog/chatgpt-integrations** got 60 visits, all landing on a 404 page
3. **/features/data-dashboard** had 20 visits and also showed as a 404

At first glance, GA4 tells you what happened: ChatGPT sent traffic, and two URLs didn’t exist.

But GA4 alone doesn’t show if the pages ever existed, if they should be redirected, or if they create SEO risks.

This is where Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool helps.

First, export your GA4 referral report as a CSV.

![Export report menu with Download CSV option highlighted.](https://static.semrush.com/blog/uploads/media/7f/f2/7ff236c64e52b11bc05a635db859abcb/bc8d40f42209f50fee630d601abd8f03/image.png)

Next, upload that CSV into a Site Audit crawl and navigate to the “**Issues**” tab. Click “**X pages**” next “returned 4XX status code” under Errors.

![Semrush Issues tab showing errors with arrow pointing to 2 pages returned 4XX status code.](https://static.semrush.com/blog/uploads/media/af/b1/afb11ea474f1e9a84bc19788c828ab48/728c08e346eae3f00f6a64acebc3f45b/image.png)

Now you can see the technical reality behind the traffic:

- **/blog/chatgpt-integrations** shows as a 404 Not Found, but it has 10 backlinks pointing to it. That means you should either recreate the content or 301 redirect the page to preserve link equity.
- **/features/data-dashboard** shows up as a soft 404. This is essentially a thin placeholder page that Google recognizes as low quality, and so it shouldn’t be redirected. Leaving it as a clean 404 is the better SEO move.
- **/pricing** is a 200 OK, but Site Audit flags a duplicate title tag. Not a broken page, but still something worth fixing to avoid SEO crawl efficiency issues.

By combining GA4 and Semrush, you move from “We know ChatGPT sent users to a broken page” to “We know which broken pages matter most, why they broke, and the right action to take.”

***Further reading****:* [*Redirects: What They Are & How to Use Them*](https://www.semrush.com/blog/redirects/)

## Turn Phantom Links into Content Opportunities

If ChatGPT sends traffic to a nonexistent page, that’s a signal of real user interest. GA4 referral data helps you decide whether to create new content.

Take the “/blog/chatgpt-integrations” example. GA4 showed 60 visits from ChatGPT, all hitting a 404 error.

This proves demand exists. Instead of losing those clicks, capture them by publishing content on the missing topic.

Here’s the simplest way to prioritize which pieces to create:

1. Open your saved ChatGPT referral report in GA4
2. Sort by “Views” to see which URLs got the most visits
3. Flag the 404s with significant traffic. These are your best candidates for new content.

![GA4 table highlighting /blog/chatgpt-integrations row with views and engagement metrics.](https://static.semrush.com/blog/uploads/media/a2/c8/a2c8d7ebda3cc46afe58fe26267be2f1/fc1c49b5fa5677d53388c1a3d5153831/image.png)

If a phantom URL gets one or two clicks a month, it’s not worth building out.

But if a phantom URL gets dozens or even hundreds of visits, building that page can turn wasted traffic into engagement and conversions.

But create content only if you can make it strong and useful. Thin or rushed content won’t perform.

***Further reading****:*[*Quality Content: What It Is + 10 Actionable Tips for Success*](https://www.semrush.com/blog/quality-content/)

## Designing an AI-Optimized 404 Page

When you can’t redirect or rebuild a phantom URL, your 404 page acts as the safety net. A strong 404 page can keep users engaged instead of bouncing.

Most default 404s say “Page Not Found” and leave users stranded.

![Basic 404 error page showing Page Not Found message.](https://static.semrush.com/blog/uploads/media/30/7f/307fe20a98af77eeff4acc3a2050926e/fbd22c33e3a6a4ca85a1d356f600cb46/image.png)

But with AI referrals, users expect a real page. Your 404 needs to guide them forward, not just apologize.

Here’s what to include in an AI-optimized 404:

- **Educate users about AI hallucinations.** Add a short, clear note: “AI may have generated this link. Here’s what we do have on this topic.” Acknowledge the issue to build trust.
- **Use the URL as a search query.** If the phantom link is “/blog/chatgpt-integrations,” display related content or search results for “ChatGPT integrations.” This gives users a next step.
- **Offer navigation and helpful links.** Add links to top articles, product pages, or a search bar. Make recovery simple.
- **Keep the design clean and on-brand.** A polished 404 page shows professionalism and reduces frustration.

Here’s an excellent example by [Mani](https://x.com/megabored/status/1938863992849735752) from The Mind Clan:

![MindClan 404 page with cartoon cat and message about AI assistant sharing a broken link.](https://static.semrush.com/blog/uploads/media/3a/06/3a06704743ef998cb0c6a12cba16dc1f/4fc4b553154e10770c71e95ce33d37d1/image.png)

## Fix ChatGPT 404 Referrals Today

ChatGPT referrals can bring new visitors, but some will land on phantom URLs. Fixing these errors improves crawl efficiency, builds trust, and saves conversions.

Here’s how:

- **Use GA4 to find phantom URLs** and measure traffic
- **Run a Semrush** [**Site Audit**](https://www.semrush.com/siteaudit/) to confirm which URLs are broken
- **Redirect, recreate, or leave as 404** depending on the page’s relevance and value
- **Optimize your 404 page** to guide users back into your site
- **Monitor AI referrals over time** and turn hallucinated links into opportunities
