---
title: "Adaptive search mode, entities in Brand Radar, and more (July + August 2026)"
source: "ahrefs-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "new-features-july-august-2026"
url: "https://ahrefs.com/blog/new-features-july-august-2026/"
canonical: "https://ahrefs.com/blog/new-features-july-august-2026/"
author: "Kamila Olexa"
published: "2026-09-29T15:06:38+00:00"
updated: "2026-09-30T09:26:52+00:00"
categories:
  - "Product Blog"
freshness_reasons: []
fetched_at: "2026-10-12T10:03:08.856823+00:00"
status_code: 200
html_hash: "7fd8d70e9eb08fbed389b3815668e04876a216c1064fc5a916e9257b681134b5"
clean_word_count: 470
clean_char_count: 2972
---
# Adaptive search mode, entities in Brand Radar, and more (July + August 2026)

Here are the biggest hits to know about.

## Site Explorer

### Adaptive organic traffic model

[Site Explorer](https://app.ahrefs.com/site-explorer) now has an Adaptive organic traffic model you can enable in **settings**. It assigns individual CTR weights to 15 SERP feature types, including AI Overviews, instead of lumping them together.

Estimates are recalibrated monthly against real Web Analytics data, and you can switch between the old Static mode and Adaptive anytime.

The new mode is also available via the [API](https://docs.ahrefs.com/en/api/reference/site-explorer/get-metrics) with the `traffic\_mode=adaptive` parameter.

Adaptive mode becomes the default after testing wraps up.

### AI appearances in Top Pages

The Top Pages report now shows how many **AI responses** each page appears in, across different AI platforms, except search-query-based AI Overviews and AI Mode.

## Brand Radar

### Entity matching

[Brand Radar](https://app.ahrefs.com/brand-radar) now extracts **entities** from AI responses and uses them in report setup, filters, and the overview. You can match a brand as an entity instead of plain text, which helps with ambiguous names like Apple or Notion.

Each term supports **Entity is**, **Entity contains**, or **Text matching**, with optional **Company** or **Product category** filters.

### AI adjusted volume

AI visibility reports now use a new **AI adjusted volume** instead of Google search volume.

For each prompt, Ahrefs finds the parent keyword, takes its Google volume, and multiplies by that platform's estimated usage ratio. The same prompt gets a different volume on each platform, and can be used by your [API](https://docs.ahrefs.com/en/api/reference/brand-radar/get-ai-responses) with the new `**search\_volume\_type**` parameter.

A temporary toggle in each report header lets you revert to the old calculation. It disappears after September 30, 2026.

### Doubled prompt dataset

The Brand Radar prompt dataset has grown from around 14 million to 30 million prompts. The source is the same (Google's People Also Ask), but a lower search volume threshold now pulls in more questions.

Country distribution stays roughly the same, and about 5% of prompts refresh each month.

## Web Analytics

### Google Analytics import without Ahrefs script

You can now view imported Google Analytics data in [Web Analytics](https://app.ahrefs.com/dashboard?tab=webAnalytics) even if the Ahrefs script is not installed. Connect a Google account with GA access, and after the first import, GA becomes the default dataset for that project.

With both sources connected, you can switch between Ahrefs, combined, or GA alone.

Reports and filters unsupported in GA-only mode are hidden automatically.

---

That's all for this month. Check out our [full changelog](https://ahrefs.com/blog/new-features/) for the rest of the smaller updates, or leave any feature requests on our [Canny board](https://ahrefs.canny.io/). Enjoy!
