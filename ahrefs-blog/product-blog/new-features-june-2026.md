---
title: "New in June ’26: Firehose, spoofed bot detection, and more"
source: "ahrefs-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "new-features-june-2026"
url: "https://ahrefs.com/blog/new-features-june-2026/"
canonical: "https://ahrefs.com/blog/new-features-june-2026/"
author: "Andrei Țiț"
published: "2026-07-31T10:02:53+00:00"
updated: "2026-08-10T16:22:40+00:00"
categories:
  - "Product Blog"
freshness_reasons: []
fetched_at: "2026-09-08T09:16:35.130750+00:00"
status_code: 200
html_hash: "3b6a1b3525d0b3a67957cf15980b20e39438918f8f352a73db109392476eed3f"
clean_word_count: 536
clean_char_count: 3247
---
# New in June ’26: Firehose, spoofed bot detection, and more

We've got six updates this month, from Firehose, a brand-new real-time web monitoring product, to spoofed bot detection in Bot Analytics, and Tags in Social Media Manager.

## Firehose

[Firehose](https://firehose.com) is a new standalone Ahrefs product that turns the web into a live event stream.

1. Tell it what you're looking for and it will match the web for you
2. Give it a list of URLs and it tracks content changes over a set period.

Use it to [catch brand mentions](https://firehose.com/use-cases) across news sites, blogs, and forums the moment they go live, track competitor launches and pricing changes, or build real-time news feeds curated by topic.

Pricing is separate from your Ahrefs subscription:

### All platforms view includes prompt- and search-based indexes

The **All platforms** view in AI visibility reports previously showed only one index type at a time. It now combines both prompt-based and search query-based indexes in a single view.

Your **All platforms** numbers may shift because the default view now pulls in more Google data. To compare prompt-based indexes on their own, use the **Platform** filter to select them directly.

## General

### Higher competitor limits across tools

Most plans now support 20 competitors per project, up from the previous limit. Enterprise v3 goes up to 100.

The Rank Tracker API still returns 10 competitors for now. An update is in progress.

### Spoofed bot detection

[Bot Analytics](https://ahrefs.com/bot-analytics/) now verifies bots instead of trusting their User-Agent string.

A bot that claims a verifiable identity but fails the checks gets a (spoofed) suffix, for example Googlebot (spoofed), and moves into the new spoofed bot category.

Filter by **Spoofed Bot** to exclude fake traffic or to see only the fakes. Coverage will grow as more IP ranges are added.

### Post tags

You can now label posts with custom tags: post types, teams, campaigns, or whatever fits your workflow. Tags are managed from the new **Tags** section and can be applied when creating or editing any post.

Tag analytics are coming later, so you’ll be able to see which campaigns drive the most engagement and which post types perform best.

### Free Domain Rating

Do you want to check the website authority at scale?

You can now pull Domain Rating for as many domains as you need, or build it straight into your own tool.

This endpoint currently works without authentication, but from 10th August 2026 it will require an API key. API keys are free, and the endpoint remains completly free.

### New endpoints in APIv3

Three more additions landed in [APIv3](https://docs.ahrefs.com/) this month:

- **Rank Tracker tag endpoints**: Add, replace, and delete tags on keywords in Rank Tracker via the API.
- **Brand Radar citation endpoints**: Pull citation metrics and historical time-series data from the Brand Radar API.
- **Competitor domains in Rank Tracker**: A new competitor domains endpoint, added alongside the existing competitor pages endpoint.

---

That's all for this month. Check out our [full changelog](https://ahrefs.com/blog/new-features/) for the rest of the smaller updates, or leave any feature requests on our [Canny board](https://ahrefs.canny.io/). Enjoy!
