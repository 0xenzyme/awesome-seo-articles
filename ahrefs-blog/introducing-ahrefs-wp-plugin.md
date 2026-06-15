---
title: "Introducing the Ahrefs WP Plugin"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "high"
slug: "introducing-ahrefs-wp-plugin"
url: "https://ahrefs.com/blog/introducing-ahrefs-wp-plugin/"
canonical: "https://ahrefs.com/blog/introducing-ahrefs-wp-plugin/"
author: "Rebekah Bek"
published: "2022-01-17T08:54:33+00:00"
updated: "2022-01-26T08:49:20+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2022_old"
  - "product_or_tool_content"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:42:24+00:00"
status_code: 200
html_hash: "3f4767cc393940fba88286e7227f68392a3e4f9f20d039a40b0e868a76b518aa"
clean_word_count: 1072
clean_char_count: 6606
---
# Introducing the Ahrefs WP Plugin

Automate content audits and grow organic traffic to your WordPress website with Ahrefs’ new plugin.

The Ahrefs WP plugin shows you how each article on your blog performs for a chosen target keyword based on Ahrefs, GA and GSC data. Then, it suggests what you can do to improve their performance.

Since the Ahrefs WP plugin focuses on [content audits](https://ahrefs.com/blog/content-audit/), it complements other SEO plugins rather than replaces them.

Today, we’re going through how to install the plugin and run your first audit, as well as breaking down the components of your final report. Use the navigation bar to the left to jump straight to a particular section.

### Installation

To install the plugin from WP-admin, search for “Ahrefs SEO” in the **Add plugins gallery** in WordPress.

Or, install it manually by downloading it from <https://wordpress.org/plugins/ahrefs-seo>.

After activating the plugin for the first time, you’ll go through a short Setup wizard.

**Connecting accounts.** Connect your Ahrefs account if you have one. No worries if you don’t; you can opt for a free Authorization code. The free code is temporary and expires every few weeks, so you’ll have to reconnect the plugin each time this happens.

This connection to Ahrefs is needed to pull backlink stats for your articles. Then, connect your GA and GSC accounts to pull rankings and traffic stats.

**Scope of audit.** Next, select article categories and pages to include or exclude from the audit. Exclude pages whose purpose is not to rank in organic search, such as “Privacy” or “About”.

**Schedule.** You can schedule content audits to run automatically each day, week or month. All these settings can be changed later in Settings.

At the end of the wizard, start your first audit.

Tip: To make the audit go faster, we recommend leaving the browser tab open. [Learn more](https://help.ahrefs.com/en/articles/5879793-what-does-the-speed-of-the-audit-depend-on)

### Performance score and page distribution

Once your audit is complete, each audited page is placed in 1 of 4 buckets based on their performance: Well-performing, Under-performing, Non-performing and Excluded.

Look at your **performance score** to see the % of pages that are performing well as compared to all analyzed pages. On the right, the **pie chart** shows you how your pages are distributed across performance categories.

### SEO stats

You’ll see each article’s:

- Target keyword (pulled from other SEO plugins or GSC)
- Ranking position for the target keyword (pulled from GSC)
- Total traffic and organic traffic values (pulled from GA)
- Backlinks number received (pulled from Ahrefs)
- Suggested action to take

### Setting target keywords

In the first audit, we’ll try to guess the target keyword for each page based on ranking data from GSC and TF-IDF analysis of the article text.

If you already use other SEO plugins (Yoast, RankMath, AIOSEO) and have specified target keywords there, we’ll automatically assign and sync them on each audit.

If not, we strongly recommend**manually reviewing** each suggested keyword and either **approving** or **changing** it. This is critical because the plugin assesses your website’s content and builds all recommendations based on its performance for the chosen target keywords.

### Suggested actions

We suggest the following actions based on these scenarios:

1. **Do nothing:** If your article is ranking in the top 3 position for its target keyword.
2. **Update:** If your article is ranking for its target keyword within the top 3–20 positions and the target keyword is unique across all pages, we’ll suggest optimizing your article by updating it with new and unique content.
3. **Merge:** If your article is ranking for its target keyword within the top 3–20 positions and the target keyword is not unique across all pages, we’ll suggest consolidating the content from all similar articles into one.
4. **Exclude:** If your article is not ranking for its target keyword within the top 20 positions but is in the top 50th percentile when it comes to traffic across all pages on the site, this most likely means that this page is not supposed to attract organic traffic. We’ll suggest excluding it from the audit so that it doesn’t affect your performance score.
5. **Rewrite:** If your article is not ranking for its target keyword within the top 20 positions and is receiving low traffic, we suggest reviewing and matching search intent by analyzing the SERP, rewriting and republishing the article.

Click on each action to expand it and see a detailed description of the issue and how to solve it.

### Excluded pages

The “Excluded” tab contains pages that aren’t audited and don’t impact your performance score. The possible exclusion reasons are:

- **Out of scope.** These are pages that you excluded from the audit, as defined in the audit scope during Setup wizard or in Settings. Individual pages can also be excluded or included manually.

- **Newly published.** Pages need time to start ranking in Google, so we recommend waiting three months before auditing new publications. You can change this default waiting period in Settings.
- **Noindex page or Non-canonical page.** We automatically exclude pages that aren’t supposed to show up in search results.

- **Redirected page.** We automatically exclude articles that were redirected to another page.

- **Error analyzing.** When we send queries to Google API and Ahrefs API, they sometimes return an error. Articles with errors during the audit get this status. It’s possible to analyze the page again manually.
- **Added since last audit.** Any article added after the last content audit was completed is also excluded. These articles will be analyzed in the next audit.

### Handy notifications

On your subsequent audits, we show notifications at the top of your report when:

- There are articles with duplicated keywords. We’ll suggest checking them in case of keyword cannibalization issues.
- Some articles dropped from being well-performing. Since they just dropped, there’s a good chance of getting them back.
- Your last content audit was over 3 months ago. We suggest running an audit at least once a month to make sure that all pages’ metrics and rankings are updated.
- There are unapproved suggested target keywords. We’ll ask you to review and approve them to make sure that the plugin gives proper recommendations.

---

That’s all for today.

Liked this update? Feel free to share our Twitter thread:

https://twitter.com/ahrefs/status/1484039541392556036
