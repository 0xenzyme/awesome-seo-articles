---
title: "Semrush MCP use cases: 16 prompts for Claude or ChatGPT"
source: "semrush-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "semrush-mcp-use-case"
url: "https://www.semrush.com/blog/semrush-mcp-use-case/"
canonical: "https://www.semrush.com/blog/semrush-mcp-use-case/"
author: "Zach Paruch"
published: "2026-09-18T14:17:00+00:00"
updated: "2026-09-18T14:17:00+00:00"
categories:
  - "AI"
  - "Marketing"
freshness_reasons: []
fetched_at: "2026-10-12T10:03:58.236784+00:00"
status_code: 200
html_hash: "511655e73470181d4220e5fa5945864b9827a6c6d9a49f56a9900073a66def24"
clean_word_count: 4362
clean_char_count: 30392
---
# Semrush MCP use cases: 16 prompts for Claude or ChatGPT

The Semrush MCP server connects Semrush's data directly to AI assistants like Claude and ChatGPT, so you can run real SEO research in plain language. The [Model Context Protocol (MCP)](https://www.semrush.com/blog/what-is-mcp-connector/) is an open standard created by Anthropic that gives AI models a universal way to connect to external data sources, files, and tools.

If you've heard of MCP but haven't put it to work yet, it’s hard to know what to ask.

This guide gives you 16 Semrush MCP use cases with copy-paste prompts, grouped by workflow: keyword strategy, competitive intelligence, content optimization, and diagnostics.

## How to set up the Semrush MCP

[Setting up the Semrush MCP](https://www.semrush.com/mcp/) takes four steps:

1. **Check your plan**. MCP access comes with Semrush One Starter, Semrush One Pro+, SEO Classic Pro, and SEO Classic Guru, each including 50,000 API units. Traffic & Market reports need a separate Trends API subscription, which I'll flag when it comes up.
2. **Connect from inside your AI client**. In Claude, go to “Settings”, then "**Connectors**." Click “**Add**,” then “**Browse Connectors.**” Search for Semrush MCP, and approve the permissions. In ChatGPT, go to Settings, then Apps, find Semrush, and click Connect. Both use OAuth, so there's no key to paste.
3. **Use the endpoint for other clients**. Cursor, VS Code, Gemini, Perplexity, and custom agents connect to https://mcp.semrush.com/v2/mcp with an API key in the Authorization header. The [developer docs](https://developer.semrush.com/api/introduction/semrush-mcp/) have the config for each one. If you're working in a terminal, [Claude Code with Semrush](https://www.semrush.com/blog/claude-code-seo/) is the same idea with more automation on top.
4. **Confirm the connection**. Ask something cheap, like "What's the Semrush Rank for my domain in the US database?" If a number comes back, you're live. If there's an error, ask the AI to walk you through fixing it.

Every prompt below is in the [Semrush MCP prompt library](https://www.semrush.com/mcp/prompt-library), where each use case is a workflow of three or four chained prompts.

I've featured the first prompt in each workflow, since that's the one that pulls the data, and linked the full workflow so you can run the follow-ups. To use one, paste it, swap your own domain, country, and keywords into the {brackets}, run it, and read the output before you act on it.

*The MCP pulls live Semrush data on demand; it doesn't monitor anything or send alerts. Anything that needs watching over time, like rank tracking or competitor alerts, gets set up inside Semrush itself. The MCP is also read-only, so it can retrieve your data but never change it.*

## Search demand & keyword strategy

These search demand and keyword strategy prompts uncover where the demand in your niche actually sits, which keywords competitors own that you don't, and which gaps deserve effort first.

### Spot shifts in search demand

This prompt maps your niche's biggest keyword clusters by combined volume before the [full workflow](https://www.semrush.com/mcp/prompt-library/spot-search-demand-trends/workflow/7) layers rising, declining, and SERP-opportunity views on top. Use it when you're planning a quarter and need to know where demand lives before deciding what to build.

`Using Semrush keyword data for {country}:  
  
Identify the top 8 keyword clusters for "{niche}" by combined monthly search volume.  
  
Return ONE table:  
  
Columns:  
  
* cluster_name  
* combined_monthly_volume  
* example_keywords (up to 5)  
  
Limit: 8 clusters exactly.`

![Semrush keyword clusters for “probate court,” with combined monthly search volumes and example keywords](https://static.semrush.com/blog/uploads/media/99/e6/99e66af61c41c7a623413635aca20955/d3c5e1cbc62451891964db1563c4fa14/image.png)

You get a table of eight clusters ranked by combined volume. Next, run the workflow's trend prompts to see which clusters are growing.

### Turn keyword gaps into roadmaps

The prompt below finds keywords competitors rank for that you don't, plus the ones where you rank far behind. The [full workflow](https://www.semrush.com/mcp/prompt-library/close-keyword-gaps/workflow/16) then clusters them and plans pages. Reach for it when you know traffic is going to competitors but not through which doors.

`If {competitor-domains} are provided, use them directly (up to 5). If not, first find {your-domain.com}'s top organic search competitors (limit 5); exclude domains with Competitor Relevance = 0.00 and organic traffic > 10M (e.g., YouTube, Reddit, Wikipedia).  
  
Use Semrush data for {country} to analyze {your-domain.com} against its top organic competitors.  
  
Find and prioritize two opportunity types:  
  
* Missing keywords: competitors rank, but {your-domain.com} does not.  
* Weak shared keywords: both rank, but {your-domain.com} ranks much lower than the strongest competitor.  
  
Prioritize low-hanging fruit that look actionable through content or on-page improvements.  
  
Return ONE table (up to 50 rows):  
  
Columns:  
  
* keyword  
* opportunity_type  
* monthly_volume  
* intent  
* top_competitor_domain  
* competitor_rank  
* your_rank  
* rank_gap  
* recommended_action  
* rationale  
  
If direct gap analysis is unavailable, approximate using competitor keyword overlap plus ranking-gap comparison, and explain the method briefly.`

You get a 50-row table splitting gaps into "missing" and "weak shared" with a recommended action per row. The workflow's next prompts cluster the list into themes.

### Prioritize gaps by demand and intent

This prompt estimates the [search intent](https://www.semrush.com/blog/search-intent/) mix inside each gap cluster so you can sequence them by business value rather than raw volume. The [full workflow](https://www.semrush.com/mcp/prompt-library/close-keyword-gaps/workflow/17) then carries it through competitor difficulty checks into a six-week sprint plan. Run it as a follow-up once a gap list exists.

`Using Semrush keyword data for {country}:  
  
For the 8 gap clusters, estimate intent distribution.  
  
If gap clusters already exist in this conversation, use them.  
  
If no gap clusters are available, first identify keyword gaps for {your-domain.com} against up to 5 competitor domains, then cluster them into exactly 8 themes.  
  
Return ONE table:  
  
Columns:  
  
* cluster_name  
* informational_share_pct (est)  
* commercial_share_pct (est)  
* transactional_share_pct (est)  
* top_intent_keywords (up to 5)  
  
Limit: 8 rows.  
  
If intent labels are unavailable, infer from SERP/page types and label as estimate.`

The output is an eight-row table of estimated intent shares per cluster. Make sure you spot-check a SERP or two before trusting the roadmap, since they're model-generated estimates.

## Competitive intelligence

These competitive intelligence prompts identify who you actually compete with in search, how the traffic splits, who's growing, and how to watch them without living in dashboards.

### Identify your true search competitors

The prompt below ranks the domains sharing your keywords by Semrush's Competitor Relevance score rather than by who you assume you compete with; the [full workflow](https://www.semrush.com/mcp/prompt-library/uncover-search-competitors/workflow/10) maps overlap clusters and SERP feature wins next.

`Using Semrush data for {country}:  
  
Identify the top 10 organic competitors of {your-domain.com}, excluding high-traffic generic domains (Competitor Relevance = 0.00 or organic traffic > 10M, e.g., YouTube, Reddit, Wikipedia).  
  
Return ONE table:  
  
Columns:  
  
* competitor_domain  
  
* estimated_organic_traffic  
  
* ranking_keywords  
  
* keyword_overlap_with_{your-domain.com}  
  
* overlap_pct (if available)  
  
Limit: top 10 competitors.  
  
If overlap metrics are not available, return best-effort and label missing fields as N/A.`

![Competitor analysis for executor.org showing organic traffic, ranking keywords, keyword overlap, and relevance scores](https://static.semrush.com/blog/uploads/media/a3/1c/a31cde24785f3db3112f60787e1c2cb4/8840213f43c2605f7084d45f4f51a1ac/image.png)

The output is a 10-row table with traffic, keyword counts, and overlap per domain. Feed those names into the next four prompts.

### Prioritize strengths, gaps, and attacks

This prompt finds the clusters where you're strong and competitors are weak, so you know what to defend before choosing what to chase; the [full workflow](https://www.semrush.com/mcp/prompt-library/uncover-search-competitors/workflow/11) ends in a defend-versus-attack map.

`Using Semrush data for {country}:  
  
Identify keyword clusters where {your-domain.com} has relatively strong visibility but the top 5 competitors have weaker presence.  
  
If a previous competitor focus or cluster analysis exists in this conversation, use it as a starting point. Give special consideration to clusters previously identified as open, untargeted, weakly covered by competitors, or strong opportunities for {your-domain.com}.  
  
If no prior analysis is available, identify the clusters directly from Semrush keyword and competitor data.  
  
Return ONE table:  
  
Columns:  
  
* unique_cluster  
  
* why_unique (1 sentence)  
  
* example_keywords (up to 5)  
  
* suggested_defense_action  
  
Limit: 8 clusters.  
  
If "relative visibility" is unavailable, infer using ranking keyword coverage and label as inferred.`

You get up to eight clusters you lead, each with a defense action. The workflow's next prompts then show where competitors outrank you.

### Size traffic share across competitors

Use the prompt below to pull each domain's traffic and engagement and compute market share. Note that it calls [Traffic Analytics](https://www.semrush.com/analytics/traffic/), which needs a Trends API subscription; the [full workflow](https://www.semrush.com/mcp/prompt-library/map-the-market-landscape/workflow/6) continues into channel and geography splits.

`For each competitor domain ({competitor-domains}) in {country}, use Semrush Traffic Analytics to retrieve each domain's overall traffic summary (visits, unique visitors, engagement). It accepts multiple domains per request — pass all domains together in a single call. If {competitor-domains} are not provided, use competitor domains identified earlier in this use case as top organic/search competitors, market competitors, or strongest keyword-overlap competitors.  
  
If both {competitor-domains} and previously identified competitors are available, combine them, remove duplicates, and limit to the 5 most relevant competitor domains.  
  
Request columns:  
  
* target  
  
* rank  
  
* visits  
  
* users  
  
* pages_per_visit  
  
* bounce_rate  
  
* time_on_site  
  
Build a single comparison table:  
  
| Domain | Rank | Visits | Unique Visitors | Pages/Visit | Bounce Rate | Avg Duration (s) | Traffic Share % |  
  
Traffic Share % = each domain's visits / sum of all visits (calculate after all data is returned).  
  
After the table, derive:  
  
* total_market_traffic: sum of all visits  
  
* market_leader: domain with highest visits  
  
* traffic_concentration: combined traffic share % of the top 2 domains  
  
If data unavailable for a domain, label as low_data. Return all data in a single response.`

Back comes a share-of-market table with total market traffic, the market leader, and top-two concentration; on a plan without the Trends API, the MCP reports the gap and falls back to organic estimates, so low\_data engagement columns mean your plan, not a broken prompt.

### Find competitors gaining organic traffic

To find competitors gaining organic traffic, run the prompt below. It pulls 12 months of traffic history per competitor and ranks them by absolute growth; the [full workflow](https://www.semrush.com/mcp/prompt-library/break-down-competitor-growth/workflow/13) turns the winners' patterns into playbooks.

`Using Semrush data for {country} over the last 12 months, identify the top 10 competitors of {your-domain.com} by organic traffic growth.  
  
Process:  
  
1. Find the top organic competitors of {your-domain.com}  
  
2. Select top 10 by keyword overlap or competitive relevance  
  
   Exclude domains with Competitor Relevance = 0.00 and Organic Traffic > 10M — these are mega-platforms (YouTube, Reddit, Facebook), not niche competitors.  
  
3. For each competitor, pull its organic traffic trend over time (one call per domain)  
  
4. Extract: traffic_12m_ago, traffic_now  
  
5. Compute:  
  
   - traffic_change_abs = traffic_now − traffic_12m_ago  
  
   - traffic_change_pct = (traffic_change_abs / traffic_12m_ago) × 100  
  
   Flag any competitor where traffic_12m_ago < 100 as low_data — % growth from a tiny base is misleading.  
  
6. Determine top_growth_cluster driving traffic growth  
  
Return ONE table:  
  
Columns:  
  
* competitor_domain  
  
* traffic_change_abs  
  
* traffic_change_pct  
  
* top_growth_cluster  
  
Limit: top 10 by traffic_change_abs.  
  
Complete all sequential calls before returning the final table.  
  
Use closest available dates if 12-month data is incomplete.`

You get a growth leaderboard with the cluster driving each gain. The low\_data flag matters, because percentage growth from a tiny base will otherwise top the table.

### Track competitor visibility shifts

To track competitor visibility shifts, set the watch list first with the prompt below. It builds a monitoring table of your 10 most relevant competitors and the cluster each competes on. The [full workflow](https://www.semrush.com/mcp/prompt-library/monitor-competitor-moves/workflow/28) then establishes the baseline you measure shifts against.

`Using Semrush data for {country}:  
  
Identify the top 10 organic competitors of {your-domain.com} to monitor. Sort by competitor relevance (Cr) descending.  
  
Return ONE table:  
  
Columns:  
  
* competitor_domain  
  
* estimated_organic_traffic  
  
* keyword_overlap (if available)  
  
* primary_competing_cluster (1)  
  
Limit: 10 competitors.`

Out comes a compact watch list. Regenerate the list monthly and hand it to the alerts prompt below.

### Build alerts and response plays

Use this prompt to get alerts when a competitor gains rankings or you lose them. Remember that the MCP writes the rules but can't create alerts. Implement the output inside Semrush, for example as [Position Tracking](https://www.semrush.com/position-tracking/) campaigns; the [full workflow](https://www.semrush.com/mcp/prompt-library/monitor-competitor-moves/workflow/29) adds response playbooks.

`Create a competitor monitoring alert ruleset for {your-domain.com} in {country}.  
  
These alerts are designed to detect when monitored competitors make meaningful moves and when {your-domain.com} loses ground. Do NOT generate alerts for {your-domain.com} gains — the purpose is early warning, not reporting success.  
  
Cover two signal categories:  
  
* competitor_gain: a monitored competitor gains organic traffic, rankings, or visibility above threshold in clusters overlapping with {your-domain.com}  
  
* own_loss: {your-domain.com} drops in rankings, traffic share, or keyword visibility in a monitored cluster  
  
Base metric signals on organic traffic trend over time and on position changes in shared keywords (organic search results).  
  
Return ONE table:  
  
Columns:  
  
* alert_name  
  
* signal_type (competitor_gain / own_loss)  
  
* metric  
  
* threshold  
  
* cadence  
  
* action_owner_role  
  
* what_to_investigate  
  
Include at least 8 alert rules — minimum 5 of type competitor_gain, minimum 2 of type own_loss.`

You get a rules table with thresholds, cadences, and owners. If you run this in the same conversation as the earlier competitive prompts, the AI will calibrate against real baselines in the conversation and every threshold will carry both a percentage and an absolute floor instead of a generic number. Backtest it against a prior year’s data before you accept the output.

## Content creation & optimization

These content creation and optimization prompts find the pages losing traffic, baseline them for refreshes, map demand around your product, and turn competitor gaps into a publish plan.

### Prioritize declining pages for recovery

To find and prioritize declining pages for recovery, run the prompt below. It compares your pages against a six-month-old snapshot and traces each drop to a keyword position change. The [full workflow](https://www.semrush.com/mcp/prompt-library/refresh-underperforming-pages/workflow/32) then scores recovery potential.

`Using Semrush data for {country}:  
  
Identify pages on {your-domain.com} that have lost the most organic traffic over the past 6 months.  
  
Step 1 — Use Semrush Organic Research to get {your-domain.com}'s pages by organic traffic, sorted by traffic ascending. Exclude the homepage, pagination pages, and tag/category pages.  
  
Step 2 — For each of the top 20 pages by lowest current traffic: use Semrush to pull each page's ranking history for the past 6 months for the top keyword per page.  
  
Return ONE table:  
  
Columns:  
  
* page_url  
  
* current_monthly_traffic  
  
* traffic_6mo_ago (estimated)  
  
* traffic_change (%)  
  
* top_keyword  
  
* current_position  
  
* position_6mo_ago  
  
Limit: 20 pages.  
  
Sort by traffic_change ascending (largest drop first). If historical data is unavailable for a page, mark as low_data.`

![Semrush comparison of declining executor.org pages showing current vs. six-month-old traffic and keyword rankings](https://static.semrush.com/blog/uploads/media/6f/89/6f8941a080d05cd74c1beb405c89e05a/76808d5241bc047644f3fece8e0e02c9/image.png)

The output is a decline table sorted by biggest drop, with the keyword behind each. Read the AI's interpretation notes too, as it can catch errors you might otherwise miss.

### Create briefs and drafts for refreshes

This prompt fetches your live pages and combines their current content with your Semrush keyword baselines; the [full workflow](https://www.semrush.com/mcp/prompt-library/refresh-underperforming-pages/workflow/33) then finds keyword targets and drafts a refreshed article.

`` For each page selected for content refresh, extract the current content and SEO performance baseline for {your-domain.com} in {country}.  
  
Pages to analyze:  
  
* If {paste URLs here} are provided, include those pages.  
  
* If a refresh backlog already exists in this conversation, also include all pages marked `full_rewrite` or `targeted_update`.  
  
* If both sources are available, combine them and remove duplicate URLs.  
  
For each page:  
  
1. Fetch the current page content.  
  
2. Pull the page's current keywords, positions, and estimated traffic ({country}).  
  
Return ONE table:  
  
Columns:  
  
* page_url  
  
* source (provided_url / refresh_backlog / both)  
  
* word_count  
  
* h1  
  
* meta_description (first 160 chars)  
  
* top_3_keywords (keyword: position)  
  
* estimated_monthly_traffic  
  
* content_issues (thin / outdated / missing_keywords / none)  
  
Content issue rules:  
  
* thin = word_count < 800  
  
* outdated = content references specific years prior to {current_year} - 2  
  
* missing_keywords = page ranks for fewer than 5 keywords  
  
* none = no obvious issues detected  
  
If multiple issues apply, list all separated by commas.  
  
Complete all calls before returning the final table. ``

You get one row per page with issue flags attached. That baseline carries straight into the workflow's brief-writing step.

### Turn product demand into page blueprints

This prompt maps search demand for your product across five intent clusters and reads the SERP for each. The [full workflow](https://www.semrush.com/mcp/prompt-library/increase-product-page-visibility/workflow/35) then converts the map into page structures, and its sibling workflow prepares pages for newer surfaces. This could become more important as [agentic commerce](https://www.semrush.com/blog/agentic-commerce-optimization/) and the [Universal Commerce Protocol](https://www.semrush.com/blog/universal-commerce-protocol/) route product discovery through AI agents.

`Using Semrush keyword data for {country}:  
  
Map the search demand landscape for the product in category {niche}.  
  
Step 1 — Identify 3–5 core intent clusters:  
  
* product name / branded searches  
  
* category searches (generic)  
  
* use-case searches ("best {niche} for [job]")  
  
* comparison searches ("{niche} vs", "{niche} alternatives")  
  
* transactional modifiers ("buy {niche}", "{niche} price")  
  
Step 2 — For each cluster, run keyword research and extract the top 2–3 representative keywords via a bulk keyword lookup (several keywords in one request).  
  
Step 3 — For each keyword return: search volume, keyword difficulty, intent (commercial / transactional / informational), and dominant SERP page type. Look at the organic search results (including SERP features) to identify SERP page types and active SERP features if the bulk lookup doesn't return SERP-feature data.  
  
Return ONE table:  
  
Columns:  
  
* intent_cluster  
  
* example_keyword  
  
* monthly_volume  
  
* kd  
  
* intent  
  
* dominant_serp_page_type  
  
* opportunity (high/med/low)  
  
Opportunity rule:  
  
* high = volume ≥ 500 AND kd ≤ 65 AND intent = commercial or transactional  
  
* med = volume 100–499 OR kd 66–80  
  
* low = volume < 100 OR kd > 80  
  
Limit: 12 rows.  
  
Complete all keyword calls before returning the table.  
  
If volume data is unavailable for a keyword, mark as low_data.  
  
Also return: ONE sentence — primary keyword recommendation for the product page title tag.`

You get a 12-row demand map plus a title tag recommendation.

### Turn gaps into publish-ready plans

This prompt takes your top content gap clusters, checks whether you already have a page for each, and classifies every cluster as a refresh or a create; the [full workflow](https://www.semrush.com/mcp/prompt-library/uncover-content-gap-opportunities/workflow/23) then specs the briefs.

`Using the top 3 prioritized content gap clusters and their existing_coverage data:  
  
If prioritized content gaps already exist in this conversation, use the top 3 clusters from that output.  
  
If no prioritized content gaps are available, first identify and prioritize content gaps for {your-domain.com} in {country}:  
  
* If competitor domains are provided, use them directly, up to 5 domains.  
  
* If no competitors are provided, identify top organic competitors for {your-domain.com} using Semrush data for {country}.  
  
* Identify content topic clusters competitors cover where {your-domain.com} has low or no visibility.  
  
* Check whether {your-domain.com} appears in the top 50 results for each cluster's primary keyword.  
  
* Prioritize clusters by demand, keyword difficulty, existing coverage, and business fit.  
  
* Select the top 3 clusters.  
  
Classify each cluster:  
  
* refresh: existing_coverage = yes — {your-domain.com} already has a page on this topic  
  
* create: existing_coverage = no — no existing page; build from scratch  
  
Return ONE table:  
  
Columns:  
  
* cluster_name  
  
* action_type (refresh / create)  
  
* existing_page_url (from coverage check, or n/a)  
  
* priority_rank  
  
* why_prioritized (1 sentence)  
  
Limit: 3 rows.`

The output is a three-row plan, each cluster tagged “refresh” or “create” with a one-sentence case. Pick the competitor set carefully, since one bad domain can pollute the whole gap pull.

## Diagnostics & reporting

These diagnostics and reporting prompts find quick wins, package performance for leadership, and separate site-specific traffic losses from market-wide ones.

### Surface fast-moving SEO opportunities

This prompt pulls your keywords ranking in positions 5 to 20 and tiers them by a quick-win rule that combines position, volume, and difficulty. The [full workflow](https://www.semrush.com/mcp/prompt-library/capture-search-quick-wins/workflow/20) converts the winners into a sprint.

`Using Semrush ranking data for {country}:  
  
Find the top 50 keywords for {your-domain.com} currently ranking positions 5–20.  
  
Return ONE table:  
  
Columns:  
  
* keyword  
  
* current_position  
  
* monthly_volume  
  
* keyword_difficulty  
  
* landing_page  
  
* intent (if available)  
  
* quick_win_signal (high/med/low)  
  
Quick win signal rule:  
  
* high: position 5–10 AND monthly_volume ≥ 500 AND keyword_difficulty ≤ 60  
  
* med: position 11–20 OR monthly_volume 100–499 OR keyword_difficulty 61–75  
  
* low: monthly_volume < 100 OR keyword_difficulty > 75  
  
Sort: high first, then by monthly_volume descending.  
  
Limit: 50 rows.`

Out comes a 50-row tiered list with landing pages attached; on my run the "high" tier was mostly low-value dictionary queries while the real wins sat in "med," so re-rank by business relevance before executing it. The MCP finds the rows; deciding which rows matter is still your job.

### Turn SEO insights into board-ready decisions

Run the prompt below to compress your competitive position and traffic trend into three tables: a competitor snapshot, five insights with cited metrics, and five decisions with urgency ratings. It's the second half of the [executive reporting workflow](https://www.semrush.com/mcp/prompt-library/build-executive-SEO-reports/workflow/31).

`Using Semrush data for {your-domain.com} in {country} (last 30 days):  
  
1. Find {your-domain.com}'s top 5 organic search competitors, sorted by competitive relevance, highest first. Columns: domain, organic_traffic, competitor_relevance.  
  
2. Pull {your-domain.com}'s organic traffic trend over time — retrieve last 3 months of data.  
  
Build Table A — Competitor snapshot (5 rows):  
  
Columns:  
  
* competitor_domain  
  
* est_organic_traffic  
  
* competitor_relevance  
  
* traffic_vs_your_domain (% of your traffic)  
  
Build Table B — 5 strategic insights:  
  
Columns:  
  
* insight  
  
* data_signal (cite specific metric)  
  
* action_point (1 sentence)  
  
Build Table C — 5 decisions leadership should make:  
  
Columns:  
  
* decision  
  
* reasoning (1 sentence)  
  
* urgency (high/med/low)  
  
If a performance snapshot, risks, or opportunities already exist in this conversation: incorporate the performance snapshot, risks, and opportunities from those steps into Tables B and C.  
  
Limit: 5 rows each for Tables B and C.  
  
Label estimates as "estimate". Complete all calls before returning the tables.`

![Strategic SEO insights showing traffic and keyword trends, supporting data signals, and recommended actions](https://static.semrush.com/blog/uploads/media/b9/3b/b93b9b20d44729641701d1de5a89437f/3d99489eb0b641431abe3795aa472c6c/image.png)

You get a one-pager you can bring to a leadership meeting.

### Trace organic traffic losses to root causes

This prompt tells you whether the whole market dropped or just you, by comparing your decline window against five competitors. The [full workflow](https://www.semrush.com/mcp/prompt-library/diagnose-organic-traffic-drops/workflow/26) then classifies the scope of a site-specific drop.

`Before diagnosing site-level causes, determine whether the organic traffic drop for {your-domain.com} in {country} reflects an industry-wide event.  
  
Step 1 — Sensor reference: note the approximate drop window. Check Semrush Sensor (semrush.com/sensor) manually for that period — SERP volatility above 3.5 signals a confirmed or suspected algorithm update.  
  
Step 2 — Market comparison: identify 5 direct organic competitors of {your-domain.com}. For each competitor domain, use Semrush Traffic Analytics to retrieve visits for the drop window and an equivalent prior period. Call one domain at a time.  
  
Return ONE table:  
  
Columns:  
  
* domain  
  
* visits_pre_drop  
  
* visits_during_drop  
  
* traffic_change_pct  
  
* also_dropped (yes/no)  
  
After the table:  
  
* industry_wide_signal: true if 3 or more competitor domains also show a negative traffic_change_pct during the same period  
  
* conclusion: if industry_wide_signal is true → "Likely algorithm update or market-wide SERP event — correlate with Semrush Sensor before continuing"; if false → "Drop appears site-specific — proceed to scope classification"  
  
Return all data in a single response. If Traffic Analytics data is unavailable for a domain, use the Domain Overview tool or the Organic Research for the organic traffic trend data. Complete all calls before returning the table.`

The output is a comparison table plus an explicit verdict. Note that [Semrush Sensor](https://www.semrush.com/sensor/) isn't exposed through the MCP, so the volatility check is still manual.

## Tips for getting more out of the Semrush MCP

Getting more out of the Semrush MCP mostly comes down to prompting it like an analyst:

- **Be specific.** Name the domain, market, and timeframe so the MCP makes one precise request instead of several vague ones.
- **Give it one job at a time.** Chain use cases across messages; the library's workflows are built this way, and later prompts reuse earlier outputs from the same conversation.
- **Set the database and device** wherever the data depends on it. Every library prompt carries a {country} placeholder for this reason.
- **Ask the AI to show the numbers it pulled** so you can sanity-check its judgment calls before acting on them.
- **Watch your API units.** Every MCP request spends Semrush API units, and unit costs scale with how much data a query requests, so "top 50 keywords in the US" costs less than "all keywords globally." Specificity is efficiency.
- **Adapt the prompts.** Adjust the input in {brackets}. Change thresholds, add a business-value tiebreaker to the quick-wins rule, or match alerts to your site's real traffic numbers.

My test site had a 36% traffic drop, a competitor at parity, and a duties page losing to a single law firm article. Every one of those facts was sitting in Semrush's data waiting for someone to find it. Pick a use case from the [Semrush MCP prompt library](https://www.semrush.com/mcp/prompt-library) and find the data hiding under your nose.
