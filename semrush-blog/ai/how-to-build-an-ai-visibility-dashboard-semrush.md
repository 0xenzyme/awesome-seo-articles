---
title: "How to build an AI visibility dashboard with Semrush"
source: "semrush-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "how-to-build-an-ai-visibility-dashboard-semrush"
url: "https://www.semrush.com/blog/how-to-build-an-ai-visibility-dashboard-semrush/"
canonical: "https://www.semrush.com/blog/how-to-build-an-ai-visibility-dashboard-semrush/"
author: "Carlos Silva"
published: "2026-10-12T09:45:00+00:00"
updated: "2026-10-12T09:45:00+00:00"
categories:
  - "AI"
  - "Marketing"
freshness_reasons: []
fetched_at: "2026-10-12T10:03:28.968924+00:00"
status_code: 200
html_hash: "9377b261a3e3fd52b6746d5df13cfd993f3029e55fc173d0e063cdd1a59b9e98"
clean_word_count: 3723
clean_char_count: 22811
---
# How to build an AI visibility dashboard with Semrush

An AI visibility dashboard shows you whether AI platforms cite and recommend your brand.

We’ll help you build one that puts your prompt-level AI data from Semrush next to your page-level Google data from Search Console, so you can see whether the pages AI cites are also earning clicks.

On our test site, the first refresh surfaced a guide that AI answers cited for 50 prompts and that earned zero Google clicks.

To build your own brand visibility dashboard for AI search, you’ll need Semrush's [AI Visibility Toolkit](https://www.semrush.com/ai-seo/overview/), Google Search Console (GSC), Google Sheets, and a paid Claude plan. The Sheet holds your data. Claude turns it into a live, interactive dashboard. It took me about 90 minutes to build out this dashboard the first time and it takes 20 minutes to update each week with fresh data.

## What this AI visibility dashboard will show

This dashboard shows two measurements side by side: how visible your brand is in AI answers (from Semrush) and how your pages perform in Google (from GSC). Specifically, it tracks:

- AI visibility rate: the share of your tracked prompts where your brand appears
- Mentions and cited pages from Semrush's prompt tracking
- Generative AI impressions from GSC's [Generative AI performance report](https://www.semrush.com/blog/google-adds-ai-performance-reports/)
- Clicks, impressions, click-through rate (CTR), and average position from GSC
- A list of SEO and answer engine optimization (AEO) opportunities based on your real data

![AI visibility dashboard showing Semrush prompt tracking, cited pages, and Google Search Console performance metrics](https://static.semrush.com/blog/uploads/media/ab/91/ab9136ff64ebbecafd784d2e44a27983/79a0d1394affd1b9e18ff37b26e70a16/image.png)

There are two constraints to be aware of before you begin:

1. The dashboard runs as a Claude artifact that pulls live data from your Google Sheet through the Google Drive connector. The connector itself is available to everyone, but artifacts that call connectors require a paid Claude plan (Pro, Max, Team, or Enterprise).
2. You can't share it by public link. On Team and Enterprise plans, you can share it inside your organization, and each viewer sees data only if their Google account can open your Sheet and their Claude account has the Drive connector. On Pro and Max, it stays private to you.

This is a working dashboard for whoever owns reporting, not a link you send to leadership. For stakeholder reporting, you can ask Claude to turn the dashboard’s report into an HTML file they can open in any browser even without the connections.

## Step 1: Decide what you want to measure

Before you open any tool, decide what you want to measure:

- Your target domain, plus brand-name variations AI might use
- Which AI platforms you want to track (Semrush's [Prompt Tracking](https://www.semrush.com/position-tracking/) supports ChatGPT, Google AI Mode, and Gemini)
- Location and language
- A stable set of prompts tied to how buyers actually talk to AI
- Your desired reporting period, such as the latest 28 days versus the previous 28 days

## Step 2: Set up AI prompt tracking in Semrush

To set up AI prompt tracking, create a campaign in the [Prompt Tracking](https://www.semrush.com/position-tracking/) tool, which checks a fixed set of prompts against the chosen AI platform every day and records whether your brand appears.

*Each tracking campaign follows one AI platform. Tracking two platforms means two campaigns with the same prompts, which also counts double against your plan's prompt limit (25 to 200 tracked prompts, depending on plan). Claude and Perplexity aren't currently supported. I recommend starting with ChatGPT and Google AI Mode. If Bing and Copilot matter to your audience, add a Position Tracking campaign for Bing.*

### Choose and add your prompts

Add prompts that [mirror how your buyers talk to AI](https://www.semrush.com/blog/which-ai-search-prompts-to-track/). If you can, mine customer support tickets, sales calls, and forum posts. You can feed transcripts and text posts into Claude to get better prompt options based on the patterns it sees.

Spread your prompts across the full journey rather than clustering on brand terms. I used 30 prompts, six in each of five groups:

1. **Customer problems**: The issues your potential customers are dealing with (e.g., "I was just named executor of my dad's estate and have no idea where to start. What do I do first?")
2. **Product or category discovery**: When your customers don’t know your product or service exists yet, and they’re trying to find a solution; e.g., "Is there software that helps executors settle an estate?"
3. **Comparisons**: Comparing your brand to a competitor’s brand; e.g., "Which is better for [your ideal customer or one specific problem you help solve], [your brand] or [competitor]?"
4. **Product selection**: Researching product or service options beyond direct comparison; e.g., "What are the best tools for an estate without a will?"
5. **Branded questions**: Questions directly about your brand; e.g., "Is [brand] legit?"

Start with around 30 prompts. Monitored daily, that's roughly 200 observations a week, enough for a stable site-wide visibility rate. The entry AI Visibility Toolkit plan covers 25 prompts, so 30 means a higher tier or a prompt add-on.

Group-level numbers will swing. With six prompts per group, one prompt changing moves that group's rate by 17 points, so treat group changes as leads to investigate. If stakeholders want dependable group-level reporting, expand each group to 15 or more prompts over time, and only add prompts that mirror real buyer language.

Your branded prompts will almost always show your brand, which lifts your overall rate. Report on all prompts and non-branded only. The non-branded number tells you whether AI recommends you to people who don't know you yet.

Keep the same core prompts stable for at least a month once tracking starts. Every trend line in your dashboard depends on the prompt set staying constant. If you swap prompts mid-stream, you break the reporting.

![Semrush Position Tracking setup screen for adding AI prompts to a campaign before starting tracking](https://static.semrush.com/blog/uploads/media/98/a3/98a321b790634a4d0a4a5e1d11f5b4d8/c6af8fdb2cefb5af0c1e0b75a14edb2d/image.png)

### Organize your prompts with tags

Tag each prompt with the group it belongs to, so you can compare visibility across meaningful segments instead of one blended score.

In your campaign, open the "**Tags**" tab and click "**Manage tags**" to create and assign them. I used one tag for each of my five prompt groups. The screenshot below is from my Google AI Mode campaign, which tracks a smaller set of prompts across the same five groups. Semrush also shows its own topic groupings in this view, and you can ignore those for the dashboard.

![Semrush AI Visibility Tags report showing visibility, mentions, and average position for different prompt groups](https://static.semrush.com/blog/uploads/media/c6/ff/c6ff99880745e2fb038284de34749d93/297e22727b45eafc4e825260dffff430/image.png)

## Step 3: Export your Semrush AI visibility data

You’ll need to export two datasets from the [AI Visibility Toolkit](https://www.semrush.com/ai-seo/overview/) into Google Sheets: prompt-level performance from the tracking campaign you set up in step 2, and the pages AI platforms cite.

Neither dataset is available through the Semrush API yet, so the data gets to your Sheet by export. You can schedule those exports via email (more on that below).

### Export prompt-level performance

Your prompt tracking campaign opens in a Position Tracking view with "AI Visibility" toggled on. Once the data is populated (it may take a few hours), scroll down to the “Top Prompts” section and click “**View all X prompts**.” Then, click “**Export**” in the top-right corner and choose Google Sheets.

![Semrush Position Tracking export menu with Google Sheets selected for exporting AI visibility data](https://static.semrush.com/blog/uploads/media/d8/27/d82757a363bde32ccae39a9cec600c40/020991e2e1ea971c338591492cfc02d0/image.png)

You should see one row per prompt, with a column group for each day showing your brand's position in the answer, the answer type, and the landing page cited. A position of "-" means your brand didn't appear that day. You'll reshape this in the master Sheet step.

### Export cited pages and sources

In [Visibility Overview](https://www.semrush.com/ai-seo/overview/), use the platform selector to pick the same AI platform your tracking campaign follows, so your citation data and prompt data describe the same platform. Then scroll down to the “Topics & Sources” section. You’re going to export the Google Sheets data for both the “**Cited Sources**” and “**Cited Pages**” tabs.

Visibility Overview holds months of history even if you created your prompt tracking campaign yesterday, because Semrush builds it from its own ongoing analysis of the AI answer space. My test site had a mentions trend going back six months on day one.

![Semrush Cited Pages report listing URLs cited in AI answers and the number of prompts citing each page](https://static.semrush.com/blog/uploads/media/95/14/951446da6d9376aaf31bc4c574feb075/1fe377074b77175a1781953628bd4b45/image.png)

### What to do if export is unavailable

If the export button is grayed out or missing, check your access to the campaign. If someone else owns it, ask them to export the reports for you or to change your permissions. Nothing else in this workflow needs owner rights.

Reach out to [Semrush support](https://www.semrush.com/kb/264-contact-semrush) if you encounter any difficulties here.

## Step 4: Export Google Search Console data

GSC data shows what your pages actually earn in Google, next to what AI answers say about you. Which report you use depends on whether the Generative AI performance report has data for your property.

### If your Generative AI report has data

Open your property in GSC, go to "**Performance**," and open the "**Generative AI**" report. **Export** it twice. Once with the date range set to the last 3 months, for the daily trend. Once set to the last 28 days, for the pages table, so it matches your standard GSC window.

![Google Search Console Generative AI report with impressions chart and export options for Sheets, Excel, and CSV](https://static.semrush.com/blog/uploads/media/91/43/9143dfdbdc734901b274195799577708/8141db8a9599541f10b1cecb0bc1e124/image.png)

The export is a ZIP of separate one-dimension tables (daily impressions, pages, countries, devices). Impressions are currently the only metric available.

There is no prompt-to-click attribution; Google currently does not give you queries, clicks, or CTR data. The pages table is aggregated across the whole date range rather than broken out by day.

### If your Generative AI report is empty

The Generative AI report is available to every property, but it shows data only once your pages get enough impressions in AI Overviews and AI Mode. If yours is empty or thin, use the standard "Search results" performance report instead. Export page-level clicks, impressions, CTR, and average position for two matched 28-day windows.

End each export window 2-3 days before today, because the newest GSC data is incomplete and will undercount. Keep the windows the same length so period comparisons are consistent.

Note that this is overall Google Search performance, not AI-specific visibility, so label it that way in your dashboard.

## Step 5: Organize everything in one master Google Sheet

Put every export into one Google Sheet with a fixed tab structure. Mine ended up with seven data tabs, each holding one dataset:

- **semrush\_prompts**: prompt-level results reshaped to one row per prompt per day, with columns for date, prompt, platform, tag, position, and cited landing page
- **semrush\_cited\_pages**: the cited pages export, stamped with a snapshot date
- **semrush\_source\_domains** and **semrush\_topics**: the Visibility Overview exports, same stamping (topics is optional)
- **gsc\_genai\_daily** and **gsc\_genai\_pages**: the daily table from your 3-month Generative AI export and the pages table from your 28-day one
- **gsc\_pages**: standard page-level GSC data, one row set per 28-day window

Here is a prompt you can feed to Claude along with all the exports to have it build the sheet for you:

I'm building an AI visibility master sheet. Attached are my exports: a Semrush AI Visibility prompt tracking export, Semrush cited pages and source domains exports (plus topics, if included), the two Google Search Console Generative AI report ZIPs (a 3-month export and a 28-day export), and my standard Search Console page exports for two 28-day windows.

Build one Excel workbook I'll import into Google Sheets, one dataset per tab, first row as headers, using these exact tab names:

1. semrush\_prompts: one row per prompt per day, with columns snapshot\_date, prompt, platform, tag\_bucket, position, landing\_page. If the Semrush export has dates as columns, unpivot to this long format. A blank position means the brand was absent that day.
2. semrush\_cited\_pages: snapshot\_date, url, country, prompts\_count. Stamp every row with the export's snapshot date.
3. semrush\_source\_domains: snapshot\_date, domain, then the export's metric columns, then country. Same date stamping.
4. semrush\_topics (only if attached): snapshot\_date, topic, country, plus its metric columns.
5. gsc\_genai\_daily: date, gen\_ai\_impressions, from the 3-month export's daily table
6. gsc\_genai\_pages: period\_start, period\_end, page, gen\_ai\_impressions, from the 28-day export's pages table.
7. gsc\_pages: period\_start, period\_end, page, clicks, impressions, avg\_position, one row set per 28-day window attached.

Rules: never invent or estimate a value; everything must come from an attached file, and if something is missing or doesn't match what you expect, ask me instead of guessing. Normalize URLs consistently: strip protocol and www, and merge trailing-slash duplicates by summing clicks and impressions (recompute avg\_position weighted by impressions). Add a notes tab recording which file fed each tab, the date windows covered, and anything you skipped. When done, summarize row counts per tab and flag anything that looks off, like duplicate rows, mismatched date windows, or pages appearing under multiple URL variants.

On future weekly updates, I'll attach the current master sheet (downloaded as .xlsx) plus new exports.

![Claude generated master sheet containing tracked AI prompts, tags, positions, platforms, and landing pages](https://static.semrush.com/blog/uploads/media/f4/5a/f45a39dc54211de7f57f9b269f486b63/f2bf9d163eaa9ea53b8f90bce69160c2/image.png)

## Step 6: Turn the Google Sheet into a live Claude artifact

Next, we’ll turn the Sheet into a dashboard by asking Claude to build a live artifact that reads the Sheet through your Google Drive connector.

### Connect the Google Sheet to Claude

Connect Google Drive in [Claude's connector settings](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors), then confirm Claude can open the master Sheet before asking for anything visual. The connector lets the artifact re-read the live Sheet on demand, so it updates every time you add the new data.

![Claude connectors settings showing Google Drive and Semrush connected for accessing dashboard data](https://static.semrush.com/blog/uploads/media/52/84/528482c8213dcb113e28abee9758393e/02b3abd5b168551f9e949e13193f0473/image.png)

### Tell Claude what to include

Prompt Claude to build the visual dashboard connected to your master sheet. Make sure you replace [sheet name] with your Sheet’s name and [domain] with your domain:

Using my Google Sheet "[sheet name]" (connected via Google Drive), build me a live dashboard artifact for [domain]'s AI visibility.

I want: summary KPI cards (AI visibility rate for all prompts and for non-branded prompts only, prompts where the brand appears, cited pages, generative AI impressions, GSC clicks and impressions); latest 28 days versus previous 28 days wherever the data allows; trend charts for prompt-tracking presence by platform and daily generative AI impressions, plus cited pages compared across snapshots; a page-level table joining the pages AI cites with their Google performance, with sortable columns and a click-to-expand detail view per page (its period-over-period Google numbers plus the tracked prompts citing it); filters for platform, date, tag, country, and page type; and a data-freshness note per tab with a warning when data is more than 10 days old.

Include an opportunity section that flags five patterns: pages with high Google visibility but low AI visibility, pages with high AI visibility but low Google traffic, pages performing strongly across both channels, prompts where my brand is absent or declining, and competitor domains repeatedly cited instead of my pages.

Treat Semrush and GSC as different measurements to compare side by side, never blended into a single score. The Sheet is the source of truth: when I update it and refresh the dashboard, the numbers should update without rebuilding anything.

The freshness warnings stop you from presenting stale data as current, and the "compare, never blend" instruction keeps data separate. The opportunity section in that prompt is how the dashboard makes recommendations based on the data.

On your first build, the prompt-tracking charts will show only a few days of data. That's expected.

On our test site, the first refresh flagged three things that went straight onto the content plan. Step 8 walks through each one.

## Step 7: Test that the dashboard updates correctly

The whole point of the dashboard is to track visibility *over time*, so you’ll want to make sure it updates properly. Test the connection by changing one number in the Sheet and confirming it moves in the dashboard.

Edit a clicks value in the “**gsc\_pages**” tab, refresh the artifact, and check that the matching KPI card changes. Check the data-freshness stamp shows the current read, then undo the edit.

If a section of the dashboard goes empty after a Sheet edit, compare your column headers against the original structure. They need to match exactly.

## Step 8: Review the dashboard and prioritize actions

Use the dashboard to decide what to work on next. Here's how we read the three findings from our test site's first refresh:

- **A page AI cites that earns no Google clicks**: Our executor checklist was cited for 50 prompts and earned zero clicks. AI platforms already trust the page, so the work is on the Google side. Find a keyword it can realistically rank for, refresh the page around it, and [build links to it](https://www.semrush.com/blog/link-building/).
- **Competitors cited where you aren't**: Our [competitor list](https://www.semrush.com/blog/benchmark-brand-mentions-in-ai-answers-semrush/) was led by domains cited for seven prompts each. Open those prompts and read what gets cited. That's your list of comparison and category content to create, and of listicles to get mentioned in.
- **A whole prompt group with no presence**: We had zero visibility across all six customer-problem prompts. One weak page doesn't explain that. It points to missing content, so those six prompts became the brief for new top-of-funnel pieces.

As your history builds, watch for these patterns too:

- A page ranking well in Google but [rarely cited by AI](https://www.semrush.com/blog/brand-visibility/) usually needs clearer structure: direct answers, descriptive headings, and current dates that make passages easy to lift
- A page losing mentions after a content change is your early warning to review the edit
- Topics improving across both AI answers and Google search are your proof of what works, so document what those pages have in common

You’ll also see an “Opportunities” section, where Claude reviews the overlap between GSC and Semrush data and gives you suggestions on how to improve your AI visibility.

![AI visibility dashboard opportunities section comparing Google traffic, AI citations, prompts, and competitor sources](https://static.semrush.com/blog/uploads/media/31/86/3186a7e42b8ea7205ee2526d745900b2/3bed9a8c48e10fd39a793decae2768f4/image.png)

For example, a page can rank well in Google and still never appear in ChatGPT. ChatGPT [pulls from its own web index](https://searchengineland.com/chatgpt-retrieval-stack-index-cache-pages-485036), so a strong Google ranking doesn't guarantee a citation. Check whether the page answers the tracked prompt directly, and whether the sources ChatGPT does cite for that prompt mention you. If Bing and Copilot matter to you, Semrush's Position Tracking tool tracks Bing rankings, and you can add that data to the dashboard with one extra export.

## Step 9: Update the dashboard each week

You’ll need to update the Sheet on a fixed weekly routine to keep the data accurate. Each week, preferably on the same day:

1. Export the latest prompt tracking data (or collect it from the scheduled export email)
2. Export the latest Cited Pages  and Cited Sources tables from Visibility Overview
3. Export the latest GSC data, ending the window 2-3 days prior
4. Append the new rows with the new snapshot date, then bring the updated file into the same Google Sheet with File > Import > Replace spreadsheet. If you import it as a new file, the dashboard can keep reading the old one.
5. Refresh the artifact and confirm the freshness stamps updated
6. Note any major content changes or campaigns in the Sheet, so next month you can connect movements to causes

When you update the sheet, keep these tips in mind:

- Keep the same headers
- Stamp every Semrush export batch with its snapshot date
- Append new rows rather than replacing old ones so you get comparison data
- Normalize URLs consistently across tabs

If you don’t normalize URLs, GSC can report some of your pages twice; once with a trailing slash and once without. If your page-level numbers ever look absurdly low, URL variants are the first thing to check.

## Build your AI visibility dashboard

A brand visibility dashboard for AI search shows you how often AI cites and mentions your brand, next to what those same pages earn in Google.

Open the [AI Visibility Toolkit](https://www.semrush.com/ai-seo/overview/), create your first tracking campaign, and write 30 prompts the way your buyers actually ask. Then connect that data with your master sheet and build the dashboard in Claude.

And if you need to show the dashboard to stakeholders, ask Claude to turn the artifact into a shareable HTML file with the same data.
